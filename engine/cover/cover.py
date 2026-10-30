#!/usr/bin/env python3
"""Episode cover (1080x1920 PNG + small JPG) drawn from code with Satori.
usage: python3 engine/cover/cover.py --title "When you see sunlight, how old is it?" --hl "how old" [--tag "SPACE"] --out cover.png
Needs `npm install` once in engine/cover. Max is taken from engine/maxwise.py and squeezed with SVGO."""
import argparse, json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ENG = os.path.dirname(HERE)
ap = argparse.ArgumentParser(); ap.add_argument("--title", required=True); ap.add_argument("--hl", default=""); ap.add_argument("--tag", default="")
ap.add_argument("--out", required=True); a = ap.parse_args()
if not os.path.exists(os.path.join(HERE, "node_modules")): subprocess.run(["npm", "install", "--silent"], cwd=HERE, check=True)
src = open(os.path.join(ENG, "maxwise.py")).read()
ns = {}
exec(src[src.index("C = dict("):src.index("BASE_CSS")], ns)   # palette + Max drawing only
svg = ns["max_svg"]().replace('<text x="150" y="252" text-anchor="middle" font-family="Patrick Hand" font-size="27" fill="#262A3B">Max</text>', "")
svg = re.sub(r'<g id="mx-larmt" opacity="0">.*?</g>|<g id="mx-[a-z]+" opacity="0">.*?</g>', "", svg, flags=re.S)  # hidden poses
svg = svg.replace('<svg id="mx-svg"', '<svg xmlns="http://www.w3.org/2000/svg"')
raw = os.path.join(HERE, "max.svg"); open(raw, "w").write(svg)
subprocess.run(["npx", "svgo", "-q", raw, "-o", raw], cwd=HERE, check=True)
subprocess.run(["node", os.path.join(HERE, "cover.mjs"), json.dumps({"title": a.title, "hl": a.hl, "tag": a.tag, "out": os.path.abspath(a.out), "max": raw})], cwd=HERE, check=True)
print(a.out)
