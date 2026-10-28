#!/usr/bin/env python3
"""Shrink scraped preview videos in Storage bucket `feed` (Supabase free plan = 1 GB).
usage: compress.py [--over-mb 4] [--budget 1500]
Re-encodes every preview larger than --over-mb to 540p H.264 CRF 30 + AAC 64k (≈1–2 MB/min, still plays with sound
on iPhone) and uploads it to the same path. Prints a JSON summary."""
import argparse, json, os, subprocess, sys, tempfile, time, urllib.parse
sys.argv_backup = sys.argv; ap = argparse.ArgumentParser(); ap.add_argument("--over-mb", type=float, default=4); ap.add_argument("--budget", type=int, default=1500)
A = ap.parse_args(); sys.argv = [sys.argv[0], "--limit", "0"]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "feedprep.py")).read().split("since = ")[0])  # reuse http/auth/upload/signed helpers
T1 = time.time()
rows = http("POST", f"{CFG['url']}/rest/v1/rpc/big_previews", {"min_bytes": int(A.over_mb * 1048576)}, H) or []
st = {"candidates": len(rows), "done": 0, "saved_mb": 0.0, "left": 0}
with tempfile.TemporaryDirectory() as w:
    for i, r in enumerate(rows):
        if time.time() - T1 > A.budget: st["left"] = len(rows) - i; break
        src, out = os.path.join(w, "in.mp4"), os.path.join(w, "out.mp4")
        try:
            open(src, "wb").write(http("GET", signed(r["name"]), raw=True))
            p = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-map", "0:v:0", "-map", "0:a:0?", "-vf", "scale='min(540,iw)':-2",
                                "-c:v", "libx264", "-preset", "veryfast", "-crf", "30", "-maxrate", "1000k", "-bufsize", "2000k",
                                "-c:a", "aac", "-b:a", "64k", "-ac", "2", "-movflags", "+faststart", out], capture_output=True)
            if p.returncode or os.path.getsize(out) >= os.path.getsize(src) * 0.9: continue
            st["saved_mb"] += (os.path.getsize(src) - os.path.getsize(out)) / 1048576
            upload(r["name"], out, "video/mp4"); st["done"] += 1
        except Exception as e:
            print("skip", r["name"], str(e)[:100])
st["saved_mb"] = round(st["saved_mb"]); st["seconds"] = int(time.time() - T1)
print(json.dumps(st))
