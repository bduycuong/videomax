#!/usr/bin/env python3
"""Vietnamese subtitles for a source video (keeps the original audio).

usage:
  subvi.py SRC.mp4 OUT.mp4 [--cover Y0:Y1] [--model small|medium] [--lang zh|en|auto] [--credit "@channel"]
           [--srt-only OUT.srt]

1. transcribes the speech with faster-whisper (any language),
2. translates every line to Vietnamese with DeepSeek (Supabase edge function `translate`),
3. optionally blurs a horizontal band where the source has burned-in captions (--cover 0.78:0.92 = fractions of height),
4. burns the Vietnamese subtitles (white bold text, dark outline, lower third) and writes OUT.mp4
   (H.264 CRF 23, AAC, faststart; re-encodes down to <= 45 MB if needed).
Prints a JSON summary. Look at a few frames of OUT.mp4 before exporting it.
"""
import argparse, json, os, re, ssl, subprocess, sys, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "supabase.json")))
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
FONT_DIR = os.path.join(ROOT, "assets", "fonts")

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--cover", help="blur band Y0:Y1 as fractions of height, e.g. 0.78:0.93")
ap.add_argument("--model", default="small")
ap.add_argument("--lang", default="auto")
ap.add_argument("--credit")
ap.add_argument("--srt-only")
a = ap.parse_args()


def post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST", headers={**headers, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
        return json.loads(r.read())


def token():
    d = post(f"{CFG['url']}/auth/v1/token?grant_type=password", {"email": CFG["engine_email"], "password": CFG["engine_password"]}, {"apikey": CFG["anon_key"]})
    return d["access_token"]


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                          "-of", "json", path], capture_output=True, text=True).stdout
    d = json.loads(out)
    s = d["streams"][0]
    return int(s["width"]), int(s["height"]), float(d["format"]["duration"])


# 1) transcribe
import numpy as np
from faster_whisper import WhisperModel
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", a.src, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0
model = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, info = model.transcribe(audio, language=None if a.lang == "auto" else a.lang, vad_filter=True, beam_size=5)
lines = []
for s in segs:
    t = s.text.strip()
    if not t: continue
    # split long lines (> 7 s) at punctuation so each subtitle stays readable
    parts = [p for p in re.split(r"(?<=[，。！？,.!?；;])", t) if p.strip()] if (s.end - s.start) > 7 and len(t) > 24 else [t]
    step = (s.end - s.start) / len(parts)
    for i, p in enumerate(parts):
        lines.append({"start": s.start + i * step, "end": s.start + (i + 1) * step, "text": p.strip()})
if not lines:
    sys.exit("no speech found – nothing to subtitle")

# 2) translate
tk = token()
vi = post(f"{CFG['url']}/functions/v1/translate", {"texts": [l["text"] for l in lines]},
          {"apikey": CFG["anon_key"], "Authorization": f"Bearer {tk}"}).get("vi")
if not vi or len(vi) != len(lines):
    sys.exit("translation failed")
for l, t in zip(lines, vi): l["vi"] = t


def ts(x, sep=","):
    h, r = divmod(max(0.0, x), 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", sep)


def ats(x):  # ASS time H:MM:SS.cc
    cs = int(round(max(0.0, x) * 100)); h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); sec, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{sec:02d}.{cs:02d}"


if a.srt_only:
    with open(a.srt_only, "w") as f:
        for i, l in enumerate(lines, 1):
            f.write(f"{i}\n{ts(l['start'])} --> {ts(l['end'])}\n{l['vi']}\n\n")
    print(json.dumps({"lines": len(lines), "language": info.language, "srt": a.srt_only}, ensure_ascii=False)); sys.exit(0)

# 3) ASS subtitles sized to the video
W, H, D = probe(a.src)
fs = max(28, round(min(W, H) * (0.058 if H > W else 0.065)))
marg_v = round(H * (0.16 if H > W else 0.07))
ass = tempfile.NamedTemporaryFile("w", suffix=".ass", delete=False, encoding="utf-8")
ass.write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: VI,DejaVu Sans,{fs},&H00FFFFFF,&H00FFFFFF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,{max(2, fs // 12)},{max(1, fs // 24)},2,{round(W*0.06)},{round(W*0.06)},{marg_v},1
Style: CR,DejaVu Sans,{round(fs*0.5)},&H40FFFFFF,&H00FFFFFF,&H00101010,&H00000000,-1,0,0,0,100,100,0,0,1,1,0,9,{round(W*0.03)},{round(W*0.03)},{round(H*0.03)},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""")
for l in lines:
    t = l["vi"].replace("\n", " ").replace("{", "(").replace("}", ")")
    ass.write(f"Dialogue: 0,{ats(l['start'])},{ats(l['end'])},VI,,0,0,0,,{t}\n")
if a.credit:
    ass.write(f"Dialogue: 0,0:00:00.00,{ats(D)},CR,,0,0,0,,{a.credit}\n")
ass.close()

# 4) burn
vf = []
if a.cover:
    y0, y1 = [float(x) for x in a.cover.split(":")]
    y0p, hp = int(H * y0) // 2 * 2, max(2, int(H * (y1 - y0)) // 2 * 2)
    vf.append(f"split[base][band];[band]crop=iw:{hp}:0:{y0p},boxblur=20:3[bl];[base][bl]overlay=0:{y0p}")
vf.append(f"ass='{ass.name}':fontsdir='{FONT_DIR}'")
filt = ",".join(vf)
cmd = ["ffmpeg", "-y", "-v", "error", "-i", a.src, "-filter_complex" if a.cover else "-vf", filt,
       "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", a.out]
subprocess.run(cmd, check=True)
size = os.path.getsize(a.out)
if size > 45 * 1024 * 1024:
    kbps = int((44 * 8 * 1024) / D) - 160
    tmp = a.out + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", a.out, "-c:v", "libx264", "-b:v", f"{kbps}k", "-maxrate", f"{kbps}k", "-bufsize", f"{2*kbps}k",
                    "-c:a", "copy", "-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, a.out); size = os.path.getsize(a.out)
print(json.dumps({"out": a.out, "lines": len(lines), "language": info.language, "duration": round(D, 1), "mb": round(size / 1048576, 1),
                  "sample": [l["vi"] for l in lines[:3]]}, ensure_ascii=False))
