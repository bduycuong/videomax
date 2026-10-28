#!/usr/bin/env python3
"""Prepare scraped feed videos for watching in the app's Reels tab.

usage: feedprep.py [--budget SECONDS] [--limit N] [--model small] [--no-subs]

For the newest feed items (status "new", scraped in the last 7 days):
  1. preview: if missing, fetch the video again via TikHub, transcode to H.264 + AAC (plays on iPhone, with sound),
     <= 25 MB, upload to Storage feed/<platform>/<id>.mp4
  2. Vietnamese subtitles: transcribe the speech (faster-whisper), translate every line with DeepSeek
     (edge function `translate`), upload WebVTT to feed/subs/<id>.vtt, set subs_path. No speech -> subs_status "none".
Stops when the time budget is used up; the next run continues. Prints a JSON summary.
"""
import argparse, datetime, json, os, re, ssl, subprocess, sys, tempfile, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "supabase.json")))
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
REF = {"douyin": "https://www.douyin.com/", "tiktok": "https://www.tiktok.com/", "instagram": "https://www.instagram.com/",
       "youtube": "https://www.youtube.com/", "xiaohongshu": "https://www.xiaohongshu.com/"}

ap = argparse.ArgumentParser()
ap.add_argument("--budget", type=int, default=1500)
ap.add_argument("--limit", type=int, default=60)
ap.add_argument("--model", default="small")
ap.add_argument("--no-subs", action="store_true")
a = ap.parse_args()
T0 = time.time()


def http(method, url, body=None, headers=None, raw=False, timeout=300):
    h = dict(headers or {}); data = None
    h.setdefault("User-Agent", "Mozilla/5.0 (compatible; videomax-studio/1.0)")  # Cloudflare blocks the urllib UA
    if body is not None:
        if isinstance(body, (bytes, bytearray)): data = body
        else: data = json.dumps(body).encode(); h.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        b = r.read()
        return b if raw else (json.loads(b) if b else None)


tok = http("POST", f"{CFG['url']}/auth/v1/token?grant_type=password", {"email": CFG["engine_email"], "password": CFG["engine_password"]},
           {"apikey": CFG["anon_key"]})["access_token"]
H = {"apikey": CFG["anon_key"], "Authorization": f"Bearer {tok}"}
rest = lambda m, p, b=None: http(m, f"{CFG['url']}/rest/v1/{p}", b, H)


def upload(path, file, ctype):
    with open(file, "rb") as f:
        http("POST", f"{CFG['url']}/storage/v1/object/feed/{urllib.parse.quote(path)}", f.read(), {**H, "Content-Type": ctype, "x-upsert": "true"})


def signed(path):
    s = http("POST", f"{CFG['url']}/storage/v1/object/sign/feed/{urllib.parse.quote(path)}", {"expiresIn": 3600}, H)
    return f"{CFG['url']}/storage/v1{s['signedURL']}"


def probe(src):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_tag_string", "-of", "csv=p=0", src], capture_output=True, text=True).stdout
    return o


def source_urls(it):
    """Candidate download URLs, best first: H.264 with sound (play_addr_h264 / download_addr) before anything else."""
    tk = json.load(open(os.path.join(ROOT, "tikhub.json")))["token"]
    pf, aid = it["platform"], it["aweme_id"]
    apis = {"douyin": [f"/api/v1/douyin/app/v3/fetch_one_video?aweme_id={aid}", f"/api/v1/douyin/web/fetch_one_video?aweme_id={aid}"],
            "tiktok": [f"/api/v1/tiktok/app/v3/fetch_one_video?aweme_id={aid}"],
            "instagram": [f"/api/v1/instagram/v2/fetch_post_info?code_or_url={urllib.parse.quote(it.get('share_url') or aid)}"],
            "xiaohongshu": [f"/api/v1/xiaohongshu/app_v2/get_video_note_detail?note_id={aid}"]}.get(pf, [])
    d = None
    for api in apis:
        try:
            d = http("GET", "https://api.tikhub.io" + api, headers={"Authorization": f"Bearer {tk}"}).get("data") or {}
            break
        except Exception as e:
            print("tikhub:", api.split("?")[0], str(e)[:80])
    if not d: return []
    out = []
    if pf in ("douyin", "tiktok"):
        a = d.get("aweme_detail") or (d.get("aweme_details") or [{}])[0] or d
        v = a.get("video") or {}
        for k in ("play_addr_h264", "download_addr", "play_addr"):
            out += (v.get(k) or {}).get("url_list") or []
        for b in v.get("bit_rate") or []:
            if not b.get("is_h265"): out += (b.get("play_addr") or {}).get("url_list") or []
    def walk(o, ctx=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, str) and v.startswith("http") and re.search(r"url|src|master|backup", k, re.I) and \
                   re.search(r"play|video|mp4|h264|stream|download", ctx + k + v, re.I) and not re.search(r"\.(jpe?g|webp|png)|image|avatar|cover|media-audio|/share/", v, re.I):
                    out.append(v)
                else: walk(v, ctx + "/" + k)
        elif isinstance(o, list):
            for x in o: walk(x, ctx)
    if not out: walk(d)
    return list(dict.fromkeys(out))[:10]


def ensure_preview(it, work):
    """Return a local playable mp4 (H.264+AAC) for this item, uploading it as the preview when needed."""
    local = os.path.join(work, f"{it['id']}.mp4")
    if it.get("preview_path"):
        src = signed(it["preview_path"])
        info = probe(src)
        if "avc1" in info and "audio" in info:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-c", "copy", local], check=False)
            return local if os.path.exists(local) else None
        cands = [src]
    else:
        cands = []
    if it["platform"] != "youtube":
        try: cands += source_urls(it)
        except Exception as e: print("tikhub:", str(e)[:120])
    for u in cands:
        raw = local + ".src"
        try:
            if u.startswith(CFG["url"]):
                data = http("GET", u, raw=True)
            else:
                data = http("GET", u, headers={"User-Agent": "Mozilla/5.0", "Referer": REF.get(it["platform"], "")}, raw=True)
            open(raw, "wb").write(data)
        except Exception:
            continue
        info = probe(raw)
        if "video" not in info: continue
        if "audio" not in info and any(x != u for x in cands[cands.index(u) + 1:]): continue  # try a variant with sound first
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-map", "0:v:0", "-map", "0:a:0?", "-vf", "scale='min(540,iw)':-2",
                            "-c:v", "libx264", "-preset", "veryfast", "-crf", "30", "-maxrate", "1000k", "-bufsize", "2000k",
                            "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", local], capture_output=True)
        if r.returncode == 0 and os.path.getsize(local) > 50_000:
            safe = re.sub(r"[^\w-]", "_", it["aweme_id"])
            key = f"{it['platform']}/{safe}.mp4"
            upload(key, local, "video/mp4")
            rest("PATCH", f"feed_items?id=eq.{it['id']}", {"preview_path": key})
            return local
    return None


def vtt_time(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


model = None
def subtitles(it, local, work):
    global model
    import numpy as np
    if model is None:
        from faster_whisper import WhisperModel
        model = WhisperModel(a.model, device="cpu", compute_type="int8")
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", local, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    if len(pcm) < 32000:
        rest("PATCH", f"feed_items?id=eq.{it['id']}", {"subs_status": "none"}); return "none"
    audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0
    segs, info = model.transcribe(audio, vad_filter=True, beam_size=3)
    lines = []
    for s in segs:
        t = s.text.strip()
        if not t: continue
        parts = [p for p in re.split(r"(?<=[，。！？,.!?；;])", t) if p.strip()] if (s.end - s.start) > 6 and len(t) > 20 else [t]
        step = (s.end - s.start) / len(parts)
        for i, p in enumerate(parts):
            lines.append((s.start + i * step, s.start + (i + 1) * step, p.strip()))
    if not lines or (info.language_probability < 0.4 and len(lines) < 3):
        rest("PATCH", f"feed_items?id=eq.{it['id']}", {"subs_status": "none"}); return "none"
    if info.language == "vi":
        vi = [l[2] for l in lines]
    else:
        vi = http("POST", f"{CFG['url']}/functions/v1/translate", {"texts": [l[2] for l in lines]}, H).get("vi") or []
        if len(vi) != len(lines): raise RuntimeError("translation mismatch")
    vtt = os.path.join(work, f"{it['id']}.vtt")
    with open(vtt, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for (st, en, _), t in zip(lines, vi):
            f.write(f"{vtt_time(st)} --> {vtt_time(en)}\n{t}\n\n")
    key = f"subs/{it['id']}.vtt"
    upload(key, vtt, "text/vtt")
    rest("PATCH", f"feed_items?id=eq.{it['id']}", {"subs_path": key, "subs_status": "done"})
    return "done"


since = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)).isoformat()
items = rest("GET", f"feed_items?select=id,platform,aweme_id,share_url,preview_path,subs_status&status=eq.new&scraped_at=gt.{urllib.parse.quote(since)}"
                    f"&or=(preview_path.is.null,subs_status.is.null)&platform=neq.youtube&order=platform.asc,scraped_at.desc&limit={a.limit}")
stats = {"items": len(items), "previews": 0, "subs": 0, "no_speech": 0, "failed": 0, "left": 0}
with tempfile.TemporaryDirectory() as work:
    # phase 1: playable previews with sound for everything first (fast), within half the budget
    for it in [x for x in items if not x.get("preview_path")]:
        if time.time() - T0 > a.budget / 2: break
        try:
            local = ensure_preview(it, work)
            if local:
                stats["previews"] += 1
                it["preview_path"] = rest("GET", f"feed_items?select=preview_path&id=eq.{it['id']}")[0]["preview_path"]
                it["_new"] = True
        except Exception as e:
            print("preview failed:", it["id"], str(e)[:120])
        for f in os.listdir(work): os.remove(os.path.join(work, f))
    if a.no_subs: items = []
    # phase 2: Vietnamese subtitles
    for n, it in enumerate(items):
        if time.time() - T0 > a.budget:
            stats["left"] = len(items) - n; break
        try:
            had = bool(it.get("preview_path")) or it.get("_new")
            local = ensure_preview(it, work)
            if local and not had and not it.get("_new"): stats["previews"] += 1
            if local and not a.no_subs and not it.get("subs_status"):
                r = subtitles(it, local, work)
                stats["subs" if r == "done" else "no_speech"] += 1
            elif not local and not it.get("subs_status"):
                rest("PATCH", f"feed_items?id=eq.{it['id']}", {"subs_status": "failed"}); stats["failed"] += 1
        except Exception as e:
            print("item failed:", it["id"], str(e)[:160]); stats["failed"] += 1
            try: rest("PATCH", f"feed_items?id=eq.{it['id']}", {"subs_status": "failed"})
            except Exception: pass
        for f in os.listdir(work): os.remove(os.path.join(work, f))
stats["seconds"] = int(time.time() - T0)
print(json.dumps(stats))
