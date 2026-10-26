# MAX WISE ep13 — How much does a fluffy cloud weigh?  Executed inside engine/maxwise.py.
# === SCENES ===
import random as _r
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; GREY = "#C9CED6"; OIL = "#FFE9A8"
CLOUD_D = "M60,200 Q10,200 20,150 Q0,100 60,90 Q70,30 140,50 Q180,0 240,40 Q310,20 320,90 Q390,100 370,160 Q380,210 320,205 Z"

def cloud_svg(cid, w, fill="#fff", extra=""):
    return f'<svg id="{cid}" width="{w}" height="{w*0.6:.0f}" viewBox="0 0 400 240" data-layout-ignore><path d="{CLOUD_D}" fill="{fill}" {WSF}/>{extra}</svg>'

def elephant(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="26" ry="18" fill="{GREY}" stroke="{K}" stroke-width="3"/>'
            f'<circle cx="26" cy="-8" r="13" fill="{GREY}" stroke="{K}" stroke-width="3"/>'
            f'<path d="M36,-2 Q42,14 34,22" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>'
            f'<path d="M-16,14 L-16,26 M-4,16 L-4,26 M8,16 L8,26 M18,12 L18,26" stroke="{K}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="29" cy="-11" r="2.5" fill="{K}"/></g>')

# 1 HOOK — a fluffy cloud with a "? kg" tag
s = "hook"; tcl = aw(s, "white cloud"); thm = aw(s, "how much"); twg = aw(s, "it weighs")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:84px; }}
#hk-cl {{ position:absolute; left:220px; top:470px; }}
#hk-kg {{ position:absolute; left:620px; top:700px; transform-origin:50% 0; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How much does a<br><span class="hl">fluffy cloud</span> weigh?</div>
  <div id="hk-cl">{cloud_svg('hk-c', 640)}</div>
  <div id="hk-kg"><svg width="200" height="200" viewBox="0 0 200 200" data-layout-ignore>
    <path d="M60,0 L60,60" stroke="{K}" stroke-width="4"/><path d="M0,60 L140,60 L170,110 L140,160 L0,160 Z" fill="{C['hi']}" {WSF}/>
    <circle cx="148" cy="110" r="8" fill="#fff" stroke="{K}" stroke-width="3"/>
    <text x="68" y="126" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{C['red']}">? kg</text></svg></div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#hk-cl", {tcl-0.6:.2f}); rise("#hk-q", {thm-0.2:.2f});
tl.fromTo("#hk-cl", {{y:0}}, {{y:-14, duration:0.9, yoyo:true, repeat:3, ease:"sine.inOut"}}, {tcl:.2f});
pop("#hk-kg", {twg:.2f}, {{from:{{rotation:30}}, to:{{rotation:0}}}});
tl.fromTo("#hk-kg", {{rotation:0}}, {{rotation:8, duration:0.3, yoyo:true, repeat:3, ease:"sine.inOut"}}, {twg+0.3:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); tf = aw(s, "a feather"); tc = aw(s, "a car"); te = aw(s, "of elephants")
notes = [("fea", "a feather?", -6, 110, C['hi']), ("car", "a car?", 4, 405, SKY), ("ele", "elephants?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:48px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  <div id="gs-sub" class="h2" style="top:720px">one fluffy cloud weighs as much as…</div>
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-fea", {tf:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); rise("#gs-sub", {tf+0.4:.2f});
pop("#gs-car", {tc:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-ele", {te:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); twc = aw(s, "weigh a")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's weigh a cloud!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {twc:.2f});
""")

# 4 BOX — wire cube around the cloud, 1 km on each edge
s = "box"; tpc = aw(s, "picture a"); tkm = aw(s, "one kilometer"); twd = aw(s, "wide"); ttl = aw(s, "tall"); tdp = aw(s, "deep")
FX0, FY0, FS, DX, DY = 270, 360, 420, 140, -110
def cube_paths(pre):
    f = f'M{FX0},{FY0} L{FX0+FS},{FY0} L{FX0+FS},{FY0+FS} L{FX0},{FY0+FS} Z'
    b = f'M{FX0+DX},{FY0+DY} L{FX0+FS+DX},{FY0+DY} L{FX0+FS+DX},{FY0+FS+DY}'
    e = f'M{FX0},{FY0} L{FX0+DX},{FY0+DY} M{FX0+FS},{FY0} L{FX0+FS+DX},{FY0+DY} M{FX0+FS},{FY0+FS} L{FX0+FS+DX},{FY0+FS+DY}'
    return (f'<path id="{pre}-f" d="{f}" stroke="{C["blue"]}" stroke-width="6" fill="none" stroke-linejoin="round"/>'
            f'<path id="{pre}-b" d="{b}" stroke="{C["blue"]}" stroke-width="5" fill="none" stroke-dasharray="14 10"/>'
            f'<path id="{pre}-e" d="{e}" stroke="{C["blue"]}" stroke-width="5" fill="none" stroke-linecap="round"/>')
def tape(tid, x, y, rot, txt="1 km"):
    return f'<div id="{tid}" class="abs" style="left:{x}px;top:{y}px;transform:rotate({rot}deg);opacity:0"><span class="chip" style="font-size:44px;padding:0 18px">{txt}</span></div>'
scenes[s] = scene_file(s, f"""
#bx-cl {{ position:absolute; left:{FX0+40}px; top:{FY0+90}px; }}
""", f"""
  <div id="bx-cl">{cloud_svg('bx-c', 420)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{cube_paths('bx')}</svg>
  {tape('bx-w', FX0+FS//2-70, FY0+FS+14, 0)}{tape('bx-t', FX0+FS+DX+10, FY0+FS//2-60, -90)}{tape('bx-d', FX0+FS+20, FY0-90, -38)}
""", f"""
pop("#bx-cl", 0.0); draw("#bx-f", {tpc+0.2:.2f}, 0.6); draw("#bx-e", {tkm-0.3:.2f}, 0.4); draw("#bx-b", {tkm:.2f}, 0.4);
pop("#bx-w", {twd:.2f}, {{from:{{rotation:-10}}, to:{{rotation:0}}}}); pop("#bx-t", {ttl:.2f}, {{from:{{rotation:-80}}, to:{{rotation:-90}}}}); pop("#bx-d", {tdp:.2f}, {{from:{{rotation:-30}}, to:{{rotation:-38}}}});
""")

# 5 FILL — a billion little 1 m³ boxes
s = "fill"; tbx = aw(s, "that box"); tbn = aw(s, "one billion"); tcm = aw(s, "cubic meters")
grid = "".join(f'<path d="M{FX0+FS*k/10:.0f},{FY0} L{FX0+FS*k/10:.0f},{FY0+FS}" stroke="{C["blue"]}" stroke-width="2" opacity=".6"/><path d="M{FX0},{FY0+FS*k/10:.0f} L{FX0+FS},{FY0+FS*k/10:.0f}" stroke="{C["blue"]}" stroke-width="2" opacity=".6"/>' for k in range(1, 10))
scenes[s] = scene_file(s, f"""
#fl-lab {{ position:absolute; left:0; right:0; top:160px; text-align:center; font-size:84px; }}
#fl-one {{ position:absolute; left:{FX0+FS+30}px; top:{FY0+FS-120}px; font-size:52px; color:{C['red']}; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{cube_paths('fl')}
    <g id="fl-grid" style="opacity:0">{grid}</g>
    <rect id="fl-cell" x="{FX0+FS*9/10:.0f}" y="{FY0+FS*9/10:.0f}" width="{FS/10:.0f}" height="{FS/10:.0f}" fill="{C['hi']}" stroke="{C['red']}" stroke-width="4" style="opacity:0"/>
    <path id="fl-arr" d="M{FX0+FS+40},{FY0+FS-60} Q{FX0+FS+20},{FY0+FS-10} {FX0+FS-12},{FY0+FS-20}" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>
  <div id="fl-lab" class="big"><span class="red">1,000,000,000</span> m³</div>
  <div id="fl-one" class="big">1 m³</div>
""", f"""
tl.to("#fl-grid", {{opacity:1, duration:0.4}}, {tbx:.2f});
pop("#fl-lab", {tbn:.2f}, {{from:{{rotation:-6}}, to:{{rotation:0}}}});
tl.to("#fl-cell", {{opacity:1, duration:0.2}}, {tcm:.2f}); draw("#fl-arr", {tcm+0.1:.2f}, 0.3); rise("#fl-one", {tcm+0.2:.2f});
""")

# 6 DROPS — one cubic meter holds about half a gram
s = "drops"; tcm = aw(s, "each cubic"); thg = aw(s, "half a gram"); ttd = aw(s, "tiny droplets"); tpc = aw(s, "paper clip"); tls = aw(s, "less than")
rnd = _r.Random(13)
drops = "".join(f'<circle class="dr-d" cx="{rnd.uniform(40,440):.0f}" cy="{rnd.uniform(40,440):.0f}" r="{rnd.uniform(4,7):.1f}" fill="{C["blue"]}"/>' for _ in range(26))
clip = (f'<path id="dr-clip" d="M30,150 L30,40 Q30,10 60,10 Q90,10 90,40 L90,170 Q90,195 65,195 Q42,195 42,170 L42,60 Q42,45 56,45 Q70,45 70,60 L70,150" '
        f'stroke="{C["pencil"]}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
scenes[s] = scene_file(s, f"""
#dr-box {{ position:absolute; left:110px; top:260px; width:480px; height:480px; border:5px solid {K}; {SKETCH} background:#fff; }}
#dr-m {{ position:absolute; left:110px; top:170px; width:480px; text-align:center; font-size:60px; }}
#dr-g {{ position:absolute; left:630px; top:280px; width:400px; text-align:center; }}
#dr-g .big {{ font-size:100px; color:{C['blue']}; }}
#dr-clipw {{ position:absolute; left:760px; top:510px; }}
#dr-cl {{ position:absolute; left:520px; top:770px; width:540px; text-align:center; font-size:50px; }}
""", f"""
  <div id="dr-m" class="big">1 m³ of cloud</div>
  <div id="dr-box"><svg width="480" height="480" data-layout-ignore><g id="dr-drops" style="opacity:0">{drops}</g></svg></div>
  <div id="dr-g"><div class="big">≈ 0.5 g</div><div style="font-size:46px">of water</div></div>
  <svg id="dr-clipw" width="130" height="220" viewBox="0 0 120 210" data-layout-ignore>{clip}</svg>
  <div id="dr-cl" class="big">lighter than <span class="hl">1 paper clip</span>!</div>
""", f"""
rise("#dr-m", {tcm:.2f}); pop("#dr-box", {tcm+0.1:.2f});
tl.to("#dr-drops", {{opacity:1, duration:0.4}}, {thg-0.3:.2f}); pop("#dr-g", {thg:.2f});
tl.to(".dr-d", {{y:"+=14", x:"-=6", duration:1.2, yoyo:true, repeat:3, ease:"sine.inOut", stagger:0.05}}, {ttd:.2f});
pop("#dr-clipw", {tls:.2f}, {{from:{{rotation:-30}}, to:{{rotation:-8}}}}); rise("#dr-cl", {tpc:.2f});
""")

# 7 MATH — half a gram times a billion
s = "math"; tmu = aw(s, "multiply"); tbl = aw(s, "a billion"); t500 = aw(s, "five hundred thousand"); tmp = aw(s, "a million pounds")
rows = [("mt-r1", '<span class="blue">0.5 g</span> × 1,000,000,000', tmu + 0.3, K), ("mt-r2", f'= <span class="red">500,000 kg</span>', t500, K)]
rh = "".join(f'<div id="{i}" class="abs big" style="left:80px;right:80px;text-align:center;top:{330+k*170}px;font-size:84px;color:{c};opacity:0">{txt}</div>' for k, (i, txt, t, c) in enumerate(rows))
scenes[s] = scene_file(s, f"""
#mt-ans {{ position:absolute; left:0; right:0; top:720px; text-align:center; }}
#mt-ans span {{ font-size:80px; color:{C['red']}; }}
#mt-line {{ position:absolute; left:120px; top:480px; }}
""", f"""
  <div id="mt-title" class="h1" style="top:160px;font-size:76px">Now <span class="hl">multiply</span>…</div>
  {rh}
  <svg id="mt-line" width="840" height="20" data-layout-ignore><path id="mt-ul" d="M4,10 Q420,2 836,12" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="mt-ans"><span class="pill">over 1 million pounds!</span></div>
""", f"""
pop("#mt-title", {tmu-0.2:.2f}); {"".join(f'rise("#{i}", {t:.2f});' for i, _, t, _ in rows)}
draw("#mt-ul", {t500-0.3:.2f}, 0.3);
pop("#mt-ans span", {tmp:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
tl.fromTo("#mt-ans span", {{scale:1}}, {{scale:1.1, duration:0.14, yoyo:true, repeat:1}}, {tmp+0.6:.2f});
""")

# 8 ELEPHANTS — a 10 x 10 herd under the cloud
s = "elephants"; t100 = aw(s, "a hundred"); tfl = aw(s, "floating"); thd = aw(s, "your head")
herd = "".join(f'<g class="el-e" style="opacity:0">{elephant(240 + (k%10)*72, 525 + (k//10)*35, 0.72)}</g>' for k in range(100))
scenes[s] = scene_file(s, f"""
#el-cl {{ position:absolute; left:330px; top:240px; }}
#el-lab {{ position:absolute; left:0; right:0; top:150px; text-align:center; font-size:72px; }}
""", f"""
  <div id="el-cl">{cloud_svg('el-c', 420)}</div>
  <div id="el-lab" class="big">≈ <span class="red">100</span> elephants</div>
  <svg id="el-herd" class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{herd}</svg>
""", f"""
pop("#el-cl", 0.0); pop("#el-lab", {t100:.2f});
tl.to(".el-e", {{opacity:1, duration:0.05, stagger:0.012}}, {t100:.2f});
tl.fromTo("#el-herd", {{y:0}}, {{y:-16, duration:0.6, yoyo:true, repeat:2, ease:"sine.inOut"}}, {tfl:.2f});
""")

# 9 FLOAT — oil on water vs. damp air on dry air
s = "float"; tfa = aw(s, "doesn't it fall"); tdm = aw(s, "the damp"); tlt = aw(s, "is lighter"); tda = aw(s, "dry air"); tfl = aw(s, "cloud floats"); toil = aw(s, "like oil")
dry = "".join(f'<circle cx="{rnd.uniform(575,985):.0f}" cy="{rnd.uniform(560,740):.0f}" r="5" fill="{C["pencil"]}"/>' for _ in range(40))
scenes[s] = scene_file(s, f"""
#fo-q {{ top:150px; font-size:76px; }}
#fo-l1 {{ position:absolute; left:560px; top:300px; width:440px; text-align:center; font-size:48px; color:{C['blue']}; }}
#fo-l2 {{ position:absolute; left:560px; top:760px; width:440px; text-align:center; font-size:48px; color:{C['muted']}; }}
#fo-gl {{ position:absolute; left:110px; top:330px; }}
#fo-gll {{ position:absolute; left:80px; top:760px; width:380px; text-align:center; font-size:50px; }}
""", f"""
  <div id="fo-q" class="h1">Why doesn't it <span class="hl">fall</span>?</div>
  <svg id="fo-air" class="abs" style="left:0;top:0;opacity:0" width="{W}" height="960" data-layout-ignore>
    <rect x="560" y="540" width="440" height="210" rx="16" fill="#F4F1EA" stroke="{K}" stroke-width="4" stroke-dasharray="12 8"/>{dry}
    <g id="fo-cl"><path d="{CLOUD_D}" transform="translate(620,360) scale(0.8)" fill="#fff" {WSF}/></g>
    <path id="fo-up1" d="M680,560 L680,500 M664,516 L680,500 L696,516" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path id="fo-up2" d="M880,560 L880,500 M864,516 L880,500 L896,516" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>
  <div id="fo-l1" class="big">damp air: lighter</div>
  <div id="fo-l2" class="big">dry air: denser</div>
  <svg id="fo-gl" width="300" height="420" viewBox="0 0 300 420" data-layout-ignore style="opacity:0">
    <path d="M40,20 L60,400 L240,400 L260,20" fill="none" {WS}/>
    <path d="M52,190 L60,396 L240,396 L248,190 Z" fill="{SKY}"/><path d="M47,110 L52,190 L248,190 L253,110 Z" fill="{OIL}"/>
    <path d="M47,110 L253,110 M52,190 L248,190" stroke="{K}" stroke-width="3"/>
    <text x="150" y="160" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{K}">oil</text>
    <text x="150" y="310" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{K}">water</text></svg>
  <div id="fo-gll" class="big">like <span class="hl">oil on water</span></div>
""", f"""
rise("#fo-q", {tfa-0.5:.2f});
tl.to("#fo-air", {{opacity:1, duration:0.3}}, {tdm:.2f}); rise("#fo-l1", {tlt:.2f});
rise("#fo-l2", {tda:.2f});
draw("#fo-up1", {tfl:.2f}, 0.3); draw("#fo-up2", {tfl+0.1:.2f}, 0.3);
tl.fromTo("#fo-cl", {{y:0}}, {{y:-14, duration:0.5, yoyo:true, repeat:3, ease:"sine.inOut"}}, {tfl:.2f});
pop("#fo-gl", {toil-0.2:.2f}); rise("#fo-gll", {toil+0.2:.2f});
""")

# 10 RAIN — droplets bump, merge, grow and fall
s = "rain"; tbp = aw(s, "bump together"); tgh = aw(s, "too heavy"); tdn = aw(s, "down they"); trn = aw(s, "as rain")
pairs = [(380, 400), (480, 380), (580, 410), (680, 385), (780, 410), (520, 470), (660, 470)]
pd = ""
for k, (x, y) in enumerate(pairs):
    pd += (f'<circle id="rn-a{k}" cx="{x-22}" cy="{y}" r="9" fill="{C["blue"]}"/>'
           f'<g id="rn-b{k}"><path d="M{x+22},{y-14} Q{x+32},{y+2} {x+22},{y+10} Q{x+12},{y+2} {x+22},{y-14} Z" fill="{C["blue"]}"/></g>')
scenes[s] = scene_file(s, f"""
#rn-plip {{ position:absolute; left:700px; top:760px; font-size:84px; color:{C['blue']}; }}
#rn-lab {{ position:absolute; left:0; right:0; top:140px; text-align:center; font-size:64px; }}
""", f"""
  <div id="rn-lab" class="big">bump… grow… <span class="hl">rain!</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <path d="{CLOUD_D}" transform="translate(200,230) scale(1.6)" fill="#F4F6FA" {WSF}/>
    <path id="rn-gr" d="M440,880 Q620,870 1000,884" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    {pd}</svg>
  <div id="rn-plip" class="big">PLIP!</div>
""", f"""
rise("#rn-lab", 0.0);
for (let k=0;k<{len(pairs)};k++) {{
  tl.to("#rn-a"+k, {{x:44, duration:0.35, ease:"power2.in"}}, {tbp:.2f}+k*0.06);
  tl.set("#rn-a"+k, {{opacity:0}}, {tbp+0.35:.2f}+k*0.06);
  tl.to("#rn-b"+k, {{scale:1.7, transformOrigin:"50% 50%", duration:0.3, ease:"back.out(2)"}}, {tbp+0.35:.2f}+k*0.06);
  tl.to("#rn-b"+k, {{y:400 + (k%3)*20, duration:0.6, ease:"power2.in"}}, {tdn:.2f}+k*0.09);
}}
tl.fromTo("#rn-b0, #rn-b2, #rn-b4", {{rotation:0}}, {{rotation:6, duration:0.08, yoyo:true, repeat:3, transformOrigin:"50% 50%"}}, {tgh:.2f});
pop("#rn-plip", {trn:.2f}, {{from:{{rotation:16}}, to:{{rotation:6}}}});
""")

# 11 OUTRO
s = "outro"; tlc = aw(s, "one little"); the = aw(s, "hundred elephants"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:80px; }}
#ou-b {{ top:300px; font-size:72px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">1 little cloud</span>…</div>
  <div id="ou-b" class="h1">≈ <span class="red">100</span> elephants!</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tlc:.2f}); pop("#ou-b", {the:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "how much"), SC["guess"]["start"] + 0.2)
point(g("guess", "a feather"), 3.0)
wave(g("intro", "I'm Max"))
point(g("box", "wide"), 1.6)
point(g("fill", "one billion"), 1.2)
point(g("drops", "half a gram"), 1.2)
wow(g("math", "five hundred thousand"), 1.4)
wow(g("elephants", "a hundred"), 1.4)
think(g("float", "so why"), g("float", "the damp"))
point(g("float", "like oil"), 1.2)
point(g("rain", "down they"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "how much"), 0.35), ("pop.mp3", A("guess", "a feather"), 0.5), ("pop.mp3", A("guess", "a car"), 0.5),
        ("pop.mp3", A("guess", "of elephants"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("box", "wide"), 0.5),
        ("click-soft.mp3", A("box", "deep"), 0.5), ("pop.mp3", A("fill", "one billion"), 0.5), ("pop.mp3", A("drops", "half a gram"), 0.5),
        ("impact-bass-1.mp3", A("math", "five hundred thousand"), 0.45), ("impact-bass-2.mp3", A("elephants", "a hundred"), 0.4),
        ("click.mp3", A("float", "like oil"), 0.4), ("pop.mp3", A("rain", "as rain"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
