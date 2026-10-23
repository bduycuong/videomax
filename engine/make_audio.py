#!/usr/bin/env python3
"""Prepare a MAX WISE project: copy template + assets, synthesize the male EN voice per scene,
assemble voice.mp3 + bgm.mp3, write timing.json and mouth.json.

usage: python3 make_audio.py <episode_dir> <project_dir>
episode_dir/script.json = [{"id":..., "en":[sentences], "vi":[sentences]}, ...]
Required scene ids: "intro" (Max says hi, centre stage) and "outro" (last scene). Each en/vi list must be the same length.
"""
import asyncio, json, os, re, shutil, subprocess, sys
import numpy as np

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP, P = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
VOICE = os.environ.get("MAXWISE_VOICE", "en-US-AndrewMultilingualNeural")

def norm(s): return re.sub(r"[^\w]", "", s.lower())

# ---- project skeleton ----
os.makedirs(os.path.join(P, "assets", "fonts"), exist_ok=True)
os.makedirs(os.path.join(P, "compositions"), exist_ok=True)
for f in os.listdir(os.path.join(KIT, "template")):
    shutil.copy(os.path.join(KIT, "template", f), P)
for f in os.listdir(os.path.join(KIT, "assets", "fonts")):
    shutil.copy(os.path.join(KIT, "assets", "fonts", f), os.path.join(P, "assets", "fonts"))
for f in os.listdir(os.path.join(KIT, "assets", "sfx")):
    shutil.copy(os.path.join(KIT, "assets", "sfx", f), os.path.join(P, "assets"))

S = json.load(open(os.path.join(EP, "script.json")))
ids = [s["id"] for s in S]
assert "intro" in ids and ids[-1] == "outro" and ids.index("intro") < len(ids) - 1, "need 'intro' and last scene 'outro'"
for s in S: assert len(s["en"]) == len(s["vi"]), f"en/vi sentence count mismatch in {s['id']}"

# ---- TTS (edge-tts, through the agent proxy CA) ----
import certifi
if os.path.exists("/root/.ccr/ca-bundle.crt"):
    certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
import edge_tts
tts_dir = os.path.join(P, "tts"); os.makedirs(tts_dir, exist_ok=True)

async def synth(s):
    for attempt in range(4):
        try:
            c = edge_tts.Communicate(" ".join(s["en"]), VOICE, rate="+3%", boundary="WordBoundary")
            words = []
            with open(os.path.join(tts_dir, s["id"] + ".mp3"), "wb") as f:
                async for ch in c.stream():
                    if ch["type"] == "audio": f.write(ch["data"])
                    elif ch["type"] == "WordBoundary":
                        words.append({"text": ch["text"], "start": ch["offset"] / 1e7, "end": (ch["offset"] + ch["duration"]) / 1e7})
            s["words"] = words; return
        except Exception as e:
            print("tts retry", s["id"], e); await asyncio.sleep(3)
    raise SystemExit("TTS failed for " + s["id"])

async def main():
    for s in S: await synth(s)
asyncio.run(main())

t = 0.35
for s in S:
    s["dur"] = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(tts_dir, s["id"] + ".mp3")], capture_output=True, text=True).stdout)
    s["sent_words"] = [len([w for w in x.split() if norm(w)]) for x in s["en"]]
    if sum(s["sent_words"]) != len(s["words"]):
        raise SystemExit(f"word/boundary mismatch in {s['id']}: {sum(s['sent_words'])} vs {len(s['words'])} — avoid hyphens, digits and symbols in 'en'; spell numbers out")
    spans = []; i = 0
    for n in s["sent_words"]:
        ws = s["words"][i:i + n]; spans.append([round(ws[0]["start"], 3), round(ws[-1]["end"], 3)]); i += n
    s["sent_spans"] = spans
    s["start"] = round(t, 3); s["slot"] = round(s["dur"] + 0.4, 3); t += s["slot"]
S[-1]["slot"] = round(S[-1]["slot"] + 1.8, 3)
total = round(S[-1]["start"] + S[-1]["slot"], 2)
json.dump({"total": total, "scenes": S}, open(os.path.join(P, "assets", "timing.json"), "w"), ensure_ascii=False, indent=1)

inp, flt = [], []
for i, s in enumerate(S):
    inp += ["-i", os.path.join(tts_dir, s["id"] + ".mp3")]; d = int(s["start"] * 1000)
    flt.append(f"[{i}:a]aresample=48000,adelay={d}|{d}[a{i}]")
flt.append("".join(f"[a{i}]" for i in range(len(S))) + f"amix=inputs={len(S)}:normalize=0,apad,atrim=0:{total},loudnorm=I=-16:TP=-1.5[out]")
subprocess.run(["ffmpeg", "-y", "-v", "error", *inp, "-filter_complex", ";".join(flt), "-map", "[out]", "-ac", "2", "-ar", "48000", "-b:a", "192k", os.path.join(P, "assets", "voice.mp3")], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-stream_loop", "3", "-i", os.path.join(KIT, "assets", "bgm.mp3"), "-af", f"atrim=0:{total},afade=t=in:d=0.4,afade=t=out:st={total-2.5}:d=2.5", "-b:a", "192k", os.path.join(P, "assets", "bgm.mp3")], check=True)

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(P, "assets", "voice.mp3"), "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; hop = int(16000 * 0.07)
env = np.array([float(np.sqrt(np.mean(a[i:i + hop] ** 2) + 1e-12)) for i in range(0, len(a), hop)]); ref = np.percentile(env[env > 0.01], 80)
st, prev = [], -1
for i, e in enumerate(env):
    v = 0 if e < 0.025 else (1 if e < ref * 0.75 else 2)
    if v != prev: st.append([round(i * 0.07, 3), v]); prev = v
json.dump(st, open(os.path.join(P, "assets", "mouth.json"), "w"))
print("audio ready:", total, "s")
for s in S: print(f"  {s['id']:<10} start {s['start']:>6}  slot {s['slot']:>5}  words {len(s['words'])}")
