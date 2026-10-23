#!/usr/bin/env python3
"""MAX WISE engine: python3 maxwise.py <episode_dir> <project_dir>. Run make_audio.py first. Episode scenes.py has sections # === SCENES ===, # === GESTURES ===, # === SFX ===."""
import json, re, random, unicodedata, os, subprocess

import sys
EP = os.path.abspath(sys.argv[1]); P = os.path.abspath(sys.argv[2])
T = json.load(open(os.path.join(P, "assets/timing.json")))
SC = {s["id"]: s for s in T["scenes"]}
TOTAL = T["total"]
MOUTH = json.load(open(os.path.join(P, "assets/mouth.json")))
_EP_SRC = open(os.path.join(EP, "scenes.py")).read()
def _section(name):
    parts = _EP_SRC.split("# === ")
    for p in parts:
        if p.startswith(name + " ==="): return p.split("\n", 1)[1]
    return ""
W, H = 1080, 1920
C = dict(paper="#FFFDF6", rule="#D3E3F1", margin="#F0A3A0", ink="#262A3B", blue="#2F5DA8", red="#E0483C",
         hi="#FFE27A", pencil="#8C8C8C", muted="#6E6A62", vi="#3E4560")
SKETCH = "border-radius:255px 18px 225px 18px/18px 225px 18px 255px;"
FONTS = """@font-face { font-family:'Patrick Hand'; src:url('assets/fonts/patrick-hand.woff2') format('woff2'); unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD; }
@font-face { font-family:'Patrick Hand'; src:url('assets/fonts/patrick-hand-ext.woff2') format('woff2'); unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF; }
@font-face { font-family:'Patrick Hand'; src:url('assets/fonts/patrick-hand-vi.woff2') format('woff2'); unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB; }
@font-face { font-family:'Gochi Hand'; src:url('assets/fonts/gochi-hand.woff2') format('woff2'); }"""

def norm(s): return re.sub(r"[^\w]", "", unicodedata.normalize("NFC", s.lower()))
def aw(sid, phrase, occ=1):
    words = SC[sid]["words"]; toks = [norm(w["text"]) for w in words]; ph = [norm(x) for x in phrase.split()]
    n = 0
    for i in range(len(toks) - len(ph) + 1):
        if toks[i:i + len(ph)] == ph:
            n += 1
            if n == occ: return round(words[i]["start"], 3)
    raise SystemExit(f"anchor not found: {sid} / {phrase} in {toks}")
def boil_defs(fid):
    return (f'<svg width="0" height="0" style="position:absolute"><filter id="{fid}" x="-5%" y="-5%" width="110%" height="110%">'
            f'<feTurbulence id="{fid}-t" type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="1"/>'
            f'<feDisplacementMap in="SourceGraphic" scale="4"/></filter></svg>')
def boil_js(fid, dur):
    return f'for (let k=0, t=0; t<{dur:.2f}; k++, t+=0.125) tl.set("#{fid}-t", {{attr:{{seed:(k%5)+1}}}}, t);'

K = C['ink']
WS = f'stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"'

# ---------------- props ----------------
def eye_svg(pid, w=420):
    """big doodle eye; #pid-lid is the closing lid (scaleY from top)"""
    return f'''<svg viewBox="0 0 300 170" width="{w}" height="{w*170/300:.0f}" style="overflow:visible" data-layout-ignore>
  <path d="M20,85 Q150,-10 280,85 Q150,180 20,85 Z" fill="#FFFFFF" {WS.replace('fill="none" ', '')}/>
  <circle cx="150" cy="85" r="42" fill="{C['blue']}" stroke="{K}" stroke-width="5"/>
  <circle cx="150" cy="85" r="19" fill="{K}"/><circle cx="162" cy="72" r="8" fill="#fff"/>
  <path id="{pid}-lid" d="M18,85 Q150,-12 282,85 Q150,40 18,85 Z" fill="{C['hi']}" stroke="{K}" stroke-width="5" stroke-linejoin="round" style="transform-origin:150px 20px; transform-box:view-box"/>
  <path d="M60,40 L50,22 M110,22 L106,4 M190,22 L194,4 M240,40 L250,22" {WS}/>
</svg>'''

def max_svg():
    return f'''<svg id="mx-svg" viewBox="0 0 300 380" width="400" height="507" style="overflow:visible">
  <path d="M90,350 Q150,345 214,351" stroke="{C['pencil']}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".55"/>
  <g id="mx-all">
    <g id="mx-legs"><path d="M132,292 L131,338 M168,292 L169,338 M110,341 L136,340 M164,340 L192,341" {WS}/></g>
    <g id="mx-larm"><path d="M108,202 L84,268" {WS}/><circle cx="81" cy="277" r="9" fill="#fff" stroke="{K}" stroke-width="4.5"/></g>
    <g id="mx-larmt" opacity="0"><path d="M108,206 Q90,236 104,250 Q118,222 124,190" {WS}/><circle cx="125" cy="182" r="9" fill="#fff" stroke="{K}" stroke-width="4.5"/></g>
    <g id="mx-body">
      <path d="M108,190 Q150,187 192,191 Q194,240 191,292 Q150,295 109,292 Q106,240 108,190 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M121,224 Q150,221 179,225 L178,262 Q150,265 122,262 Z" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>
      <text x="150" y="252" text-anchor="middle" font-family="Patrick Hand" font-size="27" fill="{K}">Max</text>
    </g>
    <g id="mx-arm"><path d="M192,202 L216,268" {WS}/><circle cx="219" cy="277" r="9" fill="#fff" stroke="{K}" stroke-width="4.5"/>
      <g id="mx-plines" opacity="0"><path d="M236,292 L246,302 M228,298 L232,312 M240,280 L254,282" stroke="{K}" stroke-width="4" stroke-linecap="round"/></g>
      <g id="mx-warcs" opacity="0"><path d="M236,268 Q244,276 238,286 M246,262 Q258,276 248,292" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/></g></g>
    <g id="mx-head">
      <path d="M140,172 L140,190 M160,172 L160,190" {WS}/>
      <g id="mx-ant"><path d="M150,72 Q147,54 151,38" {WS}/><circle cx="151" cy="31" r="8" fill="{C['red']}" stroke="{K}" stroke-width="4"/></g>
      <path d="M86,72 Q150,68 214,73 Q217,122 213,170 Q150,174 87,170 Q83,122 86,72 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M102,88 Q150,85 198,89 Q200,122 197,154 Q150,157 103,154 Q100,122 102,88 Z" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>
      <path d="M66,112 L84,112 M66,128 L84,128 M216,112 L234,112 M216,128 L234,128" {WS}/>
      <g id="mx-eo"><circle cx="130" cy="116" r="6.5" fill="{K}"/><circle cx="170" cy="116" r="6.5" fill="{K}"/></g>
      <g id="mx-eb" opacity="0"><path d="M123,118 Q130,122 137,118 M163,118 Q170,122 177,118" {WS}/></g>
      <g id="mx-m0"><path d="M139,133 Q150,143 161,133" {WS}/></g>
      <g id="mx-m1" opacity="0"><ellipse cx="150" cy="137" rx="6" ry="5" fill="{K}"/></g>
      <g id="mx-m2" opacity="0"><path d="M139,131 Q150,130 161,131 Q160,146 150,146 Q140,146 139,131 Z" fill="{K}"/><ellipse cx="150" cy="142" rx="5" ry="2.4" fill="{C['red']}"/></g>
      <g id="mx-wow" opacity="0"><path d="M70,60 L56,46 M230,60 L244,46 M62,84 L44,80 M238,84 L256,80" stroke="{K}" stroke-width="4" stroke-linecap="round"/></g>
      <text id="mx-q" x="236" y="66" font-family="Gochi Hand" font-size="54" fill="{K}" opacity="0">?</text>
    </g>
  </g>
</svg>'''

BASE_CSS = FONTS + f"""
#root {{ position:absolute; inset:0; font-family:'Patrick Hand',cursive; color:{K}; }}
.h1 {{ position:absolute; left:70px; right:70px; text-align:center; font-family:'Gochi Hand',cursive; font-size:80px; line-height:1.02; }}
.h2 {{ position:absolute; left:80px; right:80px; text-align:center; font-size:46px; color:{C['muted']}; }}
.hl {{ background:linear-gradient(transparent 18%, {C['hi']} 18%, {C['hi']} 88%, transparent 88%); padding:0 10px; }}
.chip {{ display:inline-block; padding:2px 28px; border:4px solid {K}; {SKETCH} background:{C['hi']}; font-family:'Gochi Hand',cursive; font-size:50px; }}
.card {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} }}
.blue {{ color:{C['blue']}; }} .red {{ color:{C['red']}; }}
.abs {{ position:absolute; }}
.pill {{ display:inline-block; border:4px solid currentColor; {SKETCH} padding:2px 26px; font-family:'Gochi Hand',cursive; background:#FFFFFF; }}
.big {{ font-family:'Gochi Hand',cursive; line-height:1; }}
.hatch-r {{ background:repeating-linear-gradient(45deg, {C['red']} 0 3px, transparent 3px 11px); }}
"""
HELP_JS = """
const tl = gsap.timeline({ paused: true });
const pop = (sel, t, x) => tl.fromTo(sel, Object.assign({opacity:0, scale:0.5, y:16}, x&&x.from||{}), Object.assign({opacity:1, scale:1, y:0, duration:0.3, ease:"back.out(2.2)"}, x&&x.to||{}), t);
const rise = (sel, t, d) => tl.fromTo(sel, {opacity:0, y:30}, {opacity:1, y:0, duration:d||0.32, ease:"power3.out"}, t);
const draw = (sel, t, d, ease) => { const el=document.querySelector(sel); const L=el.getTotalLength(); tl.fromTo(sel, {strokeDasharray:L, strokeDashoffset:L}, {strokeDashoffset:0, duration:d, ease:ease||"power1.inOut"}, t); };
const count = (sel, a, b, t, d, fmt) => { const o={v:a}; const el=document.querySelector(sel); el.textContent=fmt(a); tl.to(o,{v:b,duration:d,ease:"power1.out",onUpdate:()=>{el.textContent=fmt(o.v);}},t); };
const blink = (sel, t) => { tl.to(sel, {scaleY:1, duration:0.08, ease:"power2.in"}, t); tl.to(sel, {scaleY:0, duration:0.1, ease:"power2.out"}, t+0.1); };
const fmtInt = v => Math.round(v).toLocaleString("en-US");
"""
def scene_file(sid, css, html, js, fade=True):
    d = SC[sid]["slot"]; fid = f"{sid}-boil"
    out = f'tl.to("#{sid}-wrap", {{opacity:0, y:-24, duration:0.22, ease:"power2.in"}}, {d-0.26:.3f});' if fade else ""
    return f"""<template>
<style>{BASE_CSS}{css}
#{sid}-wrap {{ position:absolute; inset:0; filter:url(#{fid}); }}</style>
<div id="root" data-composition-id="{sid}" data-width="{W}" data-height="{H}" data-duration="{d}" data-layout-allow-overlap>
{boil_defs(fid)}
<div id="{sid}-wrap">
{html}
</div>
</div>
<script>
{HELP_JS}
{boil_js(fid, d)}
{js}
{out}
window.__timelines["{sid}"] = tl;
</script>
</template>
"""
scenes = {}
LID0 = "transform:scaleY(0)"

# ---- episode scenes ----
exec(_section('SCENES'))

# ---------------- Max rig ----------------
REST = dict(x=-10, y=860); CEN = dict(x=340, y=640)
_ids = [s["id"] for s in T["scenes"]]
i0 = SC["intro"]["start"]; o0 = SC["outro"]["start"]
NEXT_AFTER_INTRO = T["scenes"][_ids.index("intro")+1]["start"]
mj = [f"tl.set('#mx-pos', {{x:{REST['x']}, y:1980}}, 0); tl.set('#mx-all', {{scaleX:1, scaleY:1, svgOrigin:'150 340'}}, 0);"
      f"tl.set('#mx-arm', {{rotation:0, svgOrigin:'192 202'}}, 0); tl.set('#mx-larm', {{rotation:0, svgOrigin:'108 202'}}, 0);"
      f"tl.set('#mx-head', {{rotation:0, svgOrigin:'150 190'}}, 0); tl.set('#mx-ant', {{rotation:0, svgOrigin:'150 72'}}, 0);"]
mj.append(f"tl.to('#mx-pos', {{y:{REST['y']}, duration:0.5, ease:'back.out(1.5)'}}, 0.15);")
mj.append(f"tl.to('#mx-pos', {{x:{CEN['x']}, y:{CEN['y']}, duration:0.45, ease:'power3.inOut'}}, {i0-0.2:.2f});")
mj.append(f"tl.to('#mx-pos', {{x:{REST['x']}, y:{REST['y']}, duration:0.45, ease:'power3.inOut'}}, {NEXT_AFTER_INTRO-0.3:.2f});")
mj.append(f"tl.to('#mx-pos', {{x:{CEN['x']}, y:{CEN['y']}, duration:0.45, ease:'power3.inOut'}}, {o0-0.2:.2f});")
for t in [0.65, i0 + 0.25, NEXT_AFTER_INTRO + 0.15, o0 + 0.25]:
    mj.append(f"tl.set('#mx-all', {{scaleY:0.9, scaleX:1.07}}, {t:.2f}); tl.to('#mx-all', {{scaleY:1, scaleX:1, duration:0.4, ease:'elastic.out(1,0.5)'}}, {t+0.01:.2f});")
for t, st in MOUTH:
    mj.append(f"tl.set('#mx-m0',{{opacity:{int(st==0)}}},{t});tl.set('#mx-m1',{{opacity:{int(st==1)}}},{t});tl.set('#mx-m2',{{opacity:{int(st==2)}}},{t});")
rnd = random.Random(5); t = 1.6
while t < TOTAL - 0.5:
    mj.append(f"tl.set('#mx-eo',{{opacity:0}},{t:.2f});tl.set('#mx-eb',{{opacity:1}},{t:.2f});tl.set('#mx-eo',{{opacity:1}},{t+0.12:.2f});tl.set('#mx-eb',{{opacity:0}},{t+0.12:.2f});")
    t += rnd.uniform(2.4, 4.0)
t = 0.9; k = 0
while t < TOTAL - 0.8:
    mj.append(f"tl.to('#mx-head', {{rotation:{[-3,2,-1.5,3,0][k%5]}, duration:0.45, ease:'sine.inOut'}}, {t:.2f});")
    mj.append(f"tl.to('#mx-ant', {{rotation:{[8,-10,6,-6,0][k%5]}, duration:0.35, ease:'sine.inOut'}}, {t+0.1:.2f});")
    t += rnd.uniform(0.7, 1.0); k += 1
g = lambda sid, ph: SC[sid]["start"] + aw(sid, ph)
def think(t0, t1):
    mj.append(f"tl.set('#mx-larm', {{opacity:0}}, {t0:.2f}); tl.set('#mx-larmt', {{opacity:1}}, {t0:.2f});")
    mj.append(f"tl.to('#mx-q', {{opacity:1, duration:0.2}}, {t0+0.1:.2f});")
    mj.append(f"tl.set('#mx-larm', {{opacity:1}}, {t1:.2f}); tl.set('#mx-larmt', {{opacity:0}}, {t1:.2f}); tl.to('#mx-q', {{opacity:0, duration:0.15}}, {t1:.2f});")
def point(t, hold=1.2, ang=-95):
    mj.append(f"tl.to('#mx-arm', {{rotation:{ang}, duration:0.25, ease:'back.out(2)'}}, {t:.2f}); tl.to('#mx-plines', {{opacity:1, duration:0.1}}, {t+0.2:.2f});")
    mj.append(f"tl.to('#mx-plines', {{opacity:0, duration:0.1}}, {t+hold-0.1:.2f}); tl.to('#mx-arm', {{rotation:0, duration:0.35, ease:'power2.inOut'}}, {t+hold:.2f});")
def wow(t, hold=1.3):
    mj.append(f"tl.to('#mx-arm', {{rotation:-118, duration:0.22, ease:'back.out(2)'}}, {t:.2f}); tl.to('#mx-larm', {{rotation:118, duration:0.22, ease:'back.out(2)'}}, {t:.2f});")
    mj.append(f"tl.to('#mx-wow', {{opacity:1, duration:0.1}}, {t+0.1:.2f}); tl.to('#mx-all', {{y:-26, duration:0.18, ease:'power2.out'}}, {t:.2f}); tl.to('#mx-all', {{y:0, duration:0.2, ease:'power2.in'}}, {t+0.2:.2f});")
    mj.append(f"tl.to('#mx-wow', {{opacity:0, duration:0.15}}, {t+hold-0.1:.2f}); tl.to('#mx-arm', {{rotation:0, duration:0.35}}, {t+hold:.2f}); tl.to('#mx-larm', {{rotation:0, duration:0.35}}, {t+hold:.2f});")
def wave(t, n=3):
    mj.append(f"tl.to('#mx-arm', {{rotation:-150, duration:0.22, ease:'power2.out'}}, {t:.2f}); tl.to('#mx-warcs', {{opacity:1, duration:0.1}}, {t+0.2:.2f});")
    for j in range(n):
        mj.append(f"tl.to('#mx-arm', {{rotation:-122, duration:0.17, ease:'sine.inOut'}}, {t+0.23+j*0.36:.2f}); tl.to('#mx-arm', {{rotation:-150, duration:0.17, ease:'sine.inOut'}}, {t+0.41+j*0.36:.2f});")
    mj.append(f"tl.to('#mx-warcs', {{opacity:0, duration:0.1}}, {t+0.5+n*0.36:.2f}); tl.to('#mx-arm', {{rotation:0, duration:0.35, ease:'power2.inOut'}}, {t+0.6+n*0.36:.2f});")
exec(_section('GESTURES'))
MAX_FILE = f"""<template>
<style>{FONTS} #root {{ position:absolute; inset:0; }} #mx-pos {{ position:absolute; left:0; top:0; width:400px; height:507px; filter:url(#mx-boil); }}</style>
<div id="root" data-composition-id="max" data-width="{W}" data-height="{H}" data-duration="{TOTAL}">
  {boil_defs('mx-boil')}
  <div id="mx-pos" data-layout-ignore>{max_svg()}</div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{boil_js('mx-boil', TOTAL)}
{chr(10).join(mj)}
window.__timelines["max"] = tl;
</script>
</template>
"""

# ---------------- bilingual captions ----------------
groups = []; vis = []
for sc in T["scenes"]:
    ws = sc["words"]; wi = 0
    for si, sent in enumerate(sc["en"]):
        toks = [t for t in sent.split() if norm(t)]; sw = ws[wi:wi + len(toks)]; wi += len(toks)
        cur = []
        for j, (tok, w) in enumerate(zip(toks, sw)):
            cur.append((tok, sc["start"] + w["start"], sc["start"] + w["end"]))
            brk = tok[-1] in ",?!:" or len(cur) >= 4 or j == len(toks) - 1
            if not brk and j + 1 < len(sw) and sw[j + 1]["start"] - w["end"] > 0.18: brk = True
            if brk: groups.append((sc["id"], cur)); cur = []
        a, b = sc["sent_spans"][si]
        vis.append((sc["id"], sc["vi"][si], sc["start"] + a - 0.05, sc["start"] + b + 0.3))
# make VI windows not overlap
for i in range(len(vis) - 1):
    if vis[i][3] > vis[i + 1][2]: vis[i] = (vis[i][0], vis[i][1], vis[i][2], vis[i + 1][2])
ch = []; cj = []
center = lambda sid: sid in ("intro", "outro")
for gi, (sid, ws) in enumerate(groups):
    start = ws[0][1] - 0.05
    nxt = groups[gi + 1][1][0][1] - 0.05 if gi + 1 < len(groups) else TOTAL - 0.2
    end = min(max(ws[-1][2] + 0.25, start + 0.6), nxt)
    spans = " ".join(f'<span id="en{gi}-w{j}" class="cw">{tok}</span>' for j, (tok, _, _) in enumerate(ws))
    ch.append(f'<div id="en{gi}" class="en {"ctr" if center(sid) else ""}">{spans}</div>')
    cj.append(f"tl.fromTo('#en{gi}', {{opacity:0, y:10}}, {{opacity:1, y:0, duration:0.1, ease:'power2.out'}}, {start:.3f});")
    for j, (tok, ts, te) in enumerate(ws):
        cj.append(f"tl.set('#en{gi}-w{j}', {{color:'{C['red']}'}}, {ts:.3f});")
        if j < len(ws) - 1: cj.append(f"tl.set('#en{gi}-w{j}', {{color:'{K}'}}, {ws[j+1][1]:.3f});")
    cj.append(f"tl.to('#en{gi}', {{opacity:0, duration:0.08}}, {end-0.08:.3f}); tl.set('#en{gi}', {{opacity:0, visibility:'hidden'}}, {end:.3f});")
for vi_, (sid, txt, a, b) in enumerate(vis):
    ch.append(f'<div id="vi{vi_}" class="vi {"ctr" if center(sid) else ""}">{txt}</div>')
    cj.append(f"tl.fromTo('#vi{vi_}', {{opacity:0}}, {{opacity:1, duration:0.12}}, {a:.3f}); tl.to('#vi{vi_}', {{opacity:0, duration:0.1}}, {b-0.1:.3f}); tl.set('#vi{vi_}', {{opacity:0, visibility:'hidden'}}, {b:.3f});")
CAP_FILE = f"""<template>
<style>
{FONTS}
#root {{ position:absolute; inset:0; font-family:'Patrick Hand',cursive; }}
.en, .vi {{ position:absolute; left:390px; right:90px; text-align:center; opacity:0; }}
.en {{ bottom:{H-1150}px; line-height:1.22; transform:rotate(-1.2deg); }}
.vi {{ top:1166px; font-size:42px; line-height:1.15; color:{C['vi']}; }}
.ctr {{ left:90px; right:90px; }}
.cw {{ color:{K}; font-size:62px; background:linear-gradient(transparent 22%, {C['hi']} 22%, {C['hi']} 90%, transparent 90%); padding:0 8px; box-decoration-break:clone; -webkit-box-decoration-break:clone; }}
</style>
<div id="root" data-composition-id="caps" data-width="{W}" data-height="{H}" data-duration="{TOTAL}" data-layout-allow-overlap>
{chr(10).join(ch)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(cj)}
window.__timelines["caps"] = tl;
</script>
</template>
"""

# ---------------- audio ----------------
def adur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(P, "assets", f)], capture_output=True, text=True).stdout)
A = lambda sid, ph: SC[sid]["start"] + aw(sid, ph)
sfx = []
wh = ["whoosh-short.mp3", "whoosh.mp3"]
for i, sc in enumerate(T["scenes"][1:], 1): sfx.append((wh[i % 2], sc["start"] - 0.15, 0.25))
exec(_section('SFX'))
sfx_html = "\n  ".join(f'<audio id="sfx{i}" class="clip" src="assets/{f}" data-start="{max(0,t):.3f}" data-duration="{min(adur(f), TOTAL-max(0,t)):.3f}" data-track-index="{20+i%5}" data-volume="{v}"></audio>' for i, (f, t, v) in enumerate(sfx))
hosts = "\n  ".join(f'<div id="{sc["id"]}" data-composition-id="{sc["id"]}" data-composition-src="compositions/{sc["id"]}.html" data-start="{sc["start"]}" data-duration="{sc["slot"]}" data-track-index="2" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:{10+i}"></div>' for i, sc in enumerate(T["scenes"]))
INDEX = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ margin:0; width:{W}px; height:{H}px; overflow:hidden; background:{C['paper']}; }}
#bg {{ position:absolute; inset:0; background-color:{C['paper']}; background-image:linear-gradient({C['rule']} 2px, transparent 2px); background-size:100% 64px; background-position:0 30px; }}
#margin {{ position:absolute; top:0; bottom:0; left:64px; width:3px; background:{C['margin']}; }}
#holes {{ position:absolute; left:18px; top:0; bottom:0; width:26px; background-image:radial-gradient(circle, #E9E2D2 10px, transparent 11px); background-size:26px 300px; background-position:0 130px; }}
#ground {{ position:absolute; left:0; top:1338px; width:{W}px; height:30px; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}">
  <div id="bg"></div><div id="margin"></div><div id="holes"></div>
  <svg id="ground" width="{W}" height="30" viewBox="0 0 {W} 30"><path d="M-5,12 Q200,6 420,13 T860,10 T1090,12" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>
  {hosts}
  <div id="max" data-composition-id="max" data-composition-src="compositions/max.html" data-start="0" data-duration="{TOTAL}" data-track-index="5" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:40"></div>
  <div id="caps" data-composition-id="caps" data-composition-src="compositions/caps.html" data-start="0" data-duration="{TOTAL}" data-track-index="6" data-track-kind="captions" data-width="{W}" data-height="{H}" style="z-index:50"></div>
  <audio id="voice" class="clip" src="assets/voice.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="10" data-volume="1"></audio>
  <audio id="bgm" class="clip" src="assets/bgm.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="11" data-volume="0.15" data-fade-in="0.5" data-fade-out="2.0"></audio>
  {sfx_html}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
window.__timelines["main"] = tl;
</script>
</body>
</html>
"""
open(os.path.join(P, "index.html"), "w").write(INDEX)
for k, v in scenes.items(): open(os.path.join(P, "compositions", f"{k}.html"), "w").write(v)
open(os.path.join(P, "compositions", "max.html"), "w").write(MAX_FILE)
open(os.path.join(P, "compositions", "caps.html"), "w").write(CAP_FILE)
print("built", TOTAL, "s;", len(groups), "EN groups;", len(vis), "VI lines;", len(sfx), "sfx")
