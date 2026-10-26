#!/usr/bin/env python3
"""Footage episodes: cut the source video into the 1040x668 panel, timed to the new voice.

usage: python3 engine/footage_panel.py <episode_dir> <project_dir>   (run after make_audio.py)
episode_dir/footage.json = {"source": "<path to mp4>", "crop": [w, h, x, y]}
   crop = the region of the source frame to keep, chosen so every burned-in caption, logo and
   watermark text is OUTSIDE it (check frames first). Aspect is forced to the 1040x668 panel.
episode_dir/script.json scenes carry "src": [start_s, end_s] = the source shots for that scene.
Each scene plays its source range at 0.85–1.8x, centred, holding the last frame if it runs short.
"""
import json, os, subprocess, sys

EP, P = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
F = json.load(open(os.path.join(EP, "footage.json")))
src = F["source"] if os.path.isabs(F["source"]) else os.path.join(EP, F["source"])
w, h, x, y = F["crop"]
CROP = f"crop={w}:{h}:{x}:{y},scale=1040:668:force_original_aspect_ratio=increase,crop=1040:668,fps=30,setsar=1"
T = json.load(open(os.path.join(P, "assets", "timing.json")))
S = {s["id"]: s for s in json.load(open(os.path.join(EP, "script.json")))}

segs = [("lead", 0.0, 0.04, T["scenes"][0]["start"], 1.0)]
for sc in T["scenes"]:
    a, b = S[sc["id"]]["src"]; L = b - a; dur = sc["slot"]
    sp = min(1.8, max(0.85, L / dur)); cov = min(dur * sp, L)
    segs.append((sc["id"], a + max(0, (L - dur * sp) / 2), cov, dur, sp))
tmp = os.path.join(P, "panel_segs"); os.makedirs(tmp, exist_ok=True)
lst = []
for i, (name, st, cov, dur, sp) in enumerate(segs):
    out = os.path.join(tmp, f"{i:02d}.mp4")
    vf = f"setpts=(PTS-STARTPTS)/{sp:.4f},{CROP},tpad=stop_mode=clone:stop_duration=3,trim=0:{dur:.3f},setpts=PTS-STARTPTS"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{st:.3f}", "-t", f"{cov:.3f}", "-i", src, "-vf", vf, "-an",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "30", out], check=True)
    lst.append(f"file '{out}'")
open(os.path.join(tmp, "list.txt"), "w").write("\n".join(lst))
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "list.txt"), "-c", "copy",
                os.path.join(P, "assets", "panel.mp4")], check=True)
print("panel ready:", os.path.join(P, "assets", "panel.mp4"))
