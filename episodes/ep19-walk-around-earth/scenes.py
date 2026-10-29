# MAX WISE ep19 — How long would it take to walk around the Earth?
# === SCENES ===
CONT = '<path d="M-60,-40 Q-30,-70 0,-50 Q20,-20 -10,0 Q-40,20 -60,-10 Z M40,10 Q70,-10 90,20 Q80,60 50,60 Q30,40 40,10 Z M-110,30 Q-90,10 -70,40 Q-80,70 -110,60 Z" fill="#9BD08F" stroke="#262A3B" stroke-width="4" stroke-linejoin="round"/>'
def globe(pid, r=200, eq=True):
    conts = "".join(f'<g transform="translate({dx},0)">{CONT}</g>' for dx in (-400, -200, 0, 200, 400))
    return f'''<svg viewBox="{-r-10} {-r-10} {2*r+20} {2*r+20}" width="{2*r+20}" height="{2*r+20}" style="overflow:visible" data-layout-ignore>
  <defs><clipPath id="{pid}-clip"><circle cx="0" cy="0" r="{r}"/></clipPath></defs>
  <circle cx="0" cy="0" r="{r}" fill="#BFE3F7"/>
  <g clip-path="url(#{pid}-clip)"><g id="{pid}-land" transform="scale({r/200})">{conts}</g></g>
  <circle cx="0" cy="0" r="{r}" fill="none" stroke="{K}" stroke-width="6"/>
  {f'<path id="{pid}-eq" d="M{-r},0 Q0,{r*0.18} {r},0" stroke="{C["red"]}" stroke-width="6" stroke-dasharray="16 10" fill="none"/>' if eq else ''}
</svg>'''

# 1 HOOK
s = "hook"; tsn = aw(s, "sneakers"); teq = aw(s, "the equator"); thl = aw(s, "how long")
fp = "".join(f'<ellipse id="hk-f{i}" cx="{-170+i*34}" cy="{(14 if i%2 else -6) + 32*(1-((-170+i*34)/200)**2)*0.6:.0f}" rx="9" ry="6" fill="{K}" opacity="0"/>' for i in range(11))
scenes[s] = scene_file(s, f"""
#hk-g {{ position:absolute; left:320px; top:170px; }}
#hk-fp {{ position:absolute; left:540px; top:390px; }}
#hk-sn {{ position:absolute; left:90px; top:200px; transform:rotate(-6deg); }}
#hk-q {{ top:690px; font-size:78px; }}
""", f"""
  <div id="hk-g">{globe('hk-gl', 210)}</div>
  <svg id="hk-fp" width="1" height="1" style="overflow:visible" data-layout-ignore>{fp}</svg>
  <div id="hk-sn"><span class="chip" style="background:#fff">lace up!</span></div>
  <div id="hk-q" class="h1">How long to walk <span class="hl">all the way around</span> the Earth?</div>
""", f"""
pop("#hk-g", 0.1); pop("#hk-sn .chip", {tsn:.2f}, {{from:{{rotation:-16}}, to:{{rotation:-5}}}});
draw("#hk-gl-eq", {teq-0.2:.2f}, 0.6);
for (let i=0;i<11;i++) tl.to("#hk-f"+i, {{opacity:1, duration:0.08}}, {teq+0.3:.2f}+i*0.18);
rise("#hk-q", {thl:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "a month"); t2 = aw(s, "a year"); t3 = aw(s, "ten years")
notes = [("a", "1 month?", -6, 110, C['hi']), ("b", "1 year?", 4, 405, "#BFE3F7"), ("c", "10 years?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:250px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;font-family:Gochi Hand,cursive;font-size:62px;line-height:250px">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "do the math")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">One step at a time!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 DISTANCE — ruler under the globe
s = "distance"; teq = aw(s, "around the"); t25 = aw(s, "twenty five")
ticks = "".join(f'<path d="M{100+i*44},700 L{100+i*44},{676 if i%5 else 660}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(21))
scenes[s] = scene_file(s, f"""
#ds-title {{ top:150px; font-size:76px; }}
#ds-g {{ position:absolute; left:340px; top:250px; }}
#ds-lab {{ position:absolute; left:0; right:0; top:740px; text-align:center; }}
#ds-lab .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="ds-title" class="h1">Step 1: <span class="hl">distance</span></div>
  <div id="ds-g">{globe('ds-gl', 180)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="740" data-layout-ignore>
    <rect id="ds-rule" x="90" y="640" width="900" height="70" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>{ticks}</svg>
  <div id="ds-lab"><span class="big">≈ 25,000 miles</span></div>
""", f"""
rise("#ds-title", 0.0); pop("#ds-g", 0.2);
draw("#ds-gl-eq", {teq:.2f}, 0.8);
tl.fromTo("#ds-rule", {{scaleX:0, transformOrigin:"0% 50%"}}, {{scaleX:1, duration:0.8, ease:"power2.out"}}, {teq+0.6:.2f});
pop("#ds-lab .big", {t25:.2f});
""")

# 5 SPEED — gauge needle to 3 mph
s = "speed"; tbw = aw(s, "brisk walk"); t3 = aw(s, "three miles")
scenes[s] = scene_file(s, f"""
#sp-title {{ top:150px; font-size:76px; }}
#sp-g {{ position:absolute; left:290px; top:270px; }}
#sp-lab {{ position:absolute; left:0; right:0; top:690px; text-align:center; }}
#sp-lab .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="sp-title" class="h1">Step 2: <span class="hl">speed</span></div>
  <svg id="sp-g" width="500" height="320" viewBox="0 0 250 160" data-layout-ignore>
    <path d="M20,140 A105,105 0 0 1 230,140" fill="#fff" stroke="{K}" stroke-width="6"/>
    <path d="M20,140 A105,105 0 0 1 125,35" fill="none" stroke="#9BD08F" stroke-width="14" opacity=".7"/>
    {''.join(f'<path d="M125,140 L125,48" transform="rotate({-90+i*30} 125 140)" stroke="{K}" stroke-width="3" stroke-dasharray="0 82 10 0"/>' for i in range(7))}
    <g id="sp-needle"><path d="M125,140 L125,58" stroke="{C['red']}" stroke-width="7" stroke-linecap="round"/></g>
    <circle cx="125" cy="140" r="9" fill="{K}"/></svg>
  <div id="sp-lab"><span class="big">≈ 3 mph</span><div style="font-size:48px">a brisk walk</div></div>
""", f"""
rise("#sp-title", 0.0); pop("#sp-g", 0.2); tl.set("#sp-needle", {{rotation:-90, svgOrigin:"125 140"}}, 0);
tl.to("#sp-needle", {{rotation:-38, duration:0.6, ease:"back.out(2)"}}, {tbw:.2f});
tl.to("#sp-needle", {{rotation:-30, duration:0.25, ease:"sine.inOut", yoyo:true, repeat:5}}, {tbw+0.7:.2f});
pop("#sp-lab", {t3:.2f});
""")

# 6 HOURS — miles ÷ speed
s = "hours"; tdv = aw(s, "divide"); t83 = aw(s, "eight thousand")
scenes[s] = scene_file(s, f"""
#hr-card {{ position:absolute; left:110px; top:220px; width:860px; height:220px; }}
#hr-eq {{ position:absolute; left:0; right:0; top:52px; text-align:center; font-family:'Gochi Hand',cursive; font-size:84px; }}
#hr-ans {{ position:absolute; left:0; right:0; top:540px; text-align:center; }}
#hr-n {{ font-size:150px; color:{C['red']}; }}
""", f"""
  <div id="hr-card" class="card"><div id="hr-eq"><span class="blue">miles</span> ÷ <span class="blue">speed</span></div></div>
  <div id="hr-ans"><span id="hr-n" class="big">0</span><div style="font-size:60px">hours of walking</div></div>
""", f"""
pop("#hr-card", {tdv-0.2:.2f}, {{from:{{rotation:-6}}, to:{{rotation:-1}}}});
rise("#hr-ans", {t83-0.9:.2f});
count("#hr-n", 0, 8300, {t83-0.9:.2f}, 1.0, v => "≈ " + fmtInt(Math.round(v/100)*100));
tl.fromTo("#hr-n", {{scale:1}}, {{scale:1.12, duration:0.14, yoyo:true, repeat:1}}, {t83+0.3:.2f});
""")

# 7 NONSTOP — 365-square calendar fills to 346
s = "nonstop"; tns = aw(s, "no sleep"); t346 = aw(s, "three hundred"); twy = aw(s, "whole year")
CX0, CY0, CS = 120, 300, 30
cells = "".join(f'<rect id="ns-c{i}" x="{CX0+(i%28)*CS}" y="{CY0+(i//28)*CS}" width="{CS-4}" height="{CS-4}" fill="#fff" stroke="{C["pencil"]}" stroke-width="2"/>' for i in range(365))
scenes[s] = scene_file(s, f"""
#ns-title {{ top:150px; font-size:72px; }}
#ns-chips {{ position:absolute; left:0; right:0; top:230px; text-align:center; font-size:0; }}
#ns-chips span {{ font-size:44px; margin:0 14px; }}
#ns-lab {{ position:absolute; left:420px; top:735px; width:600px; text-align:center; }}
#ns-lab .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="ns-title" class="h1">Walk <span class="hl">nonstop</span></div>
  <div id="ns-chips"><span id="ns-a" class="pill red" style="text-decoration:line-through">sleep</span><span id="ns-b" class="pill red" style="text-decoration:line-through">snacks</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="720" data-layout-ignore>{cells}</svg>
  <div id="ns-lab"><div class="big">≈ 346 days</div><div style="font-size:50px">almost a whole year!</div></div>
""", f"""
rise("#ns-title", 0.0); pop("#ns-a", {tns:.2f}); pop("#ns-b", {tns+0.5:.2f});
for (let i=0;i<365;i++) tl.to("#ns-c"+i, {{fill:i<346?"{C['hi']}":"#fff", duration:0.01}}, 0.3 + (i<346 ? i*({t346+0.6:.2f}-0.3)/346 : 99));
rise("#ns-lab", {t346:.2f}); tl.fromTo("#ns-lab .big", {{scale:1}}, {{scale:1.12, duration:0.14, yoyo:true, repeat:1}}, {twy:.2f});
""")

# 8 REAL — 8 h a day → almost 3 years
s = "real"; tsl = aw(s, "real people"); t8 = aw(s, "eight hours"); t3y = aw(s, "almost three")
bars = "".join(f'<div class="abs" style="left:{110+i*300}px;top:430px;width:260px;height:110px;border:4px solid {K};{SKETCH}background:#fff;overflow:hidden"><div id="rl-f{i}" class="hatch-r" style="position:absolute;left:0;top:0;bottom:0;width:{[100,100,84][i]}%;transform-origin:0 50%;transform:scaleX(0)"></div></div><div class="abs" style="left:{110+i*300}px;top:550px;width:260px;text-align:center;font-size:44px">year {i+1}</div>' for i in range(3))
scenes[s] = scene_file(s, f"""
#rl-title {{ top:150px; font-size:76px; }}
#rl-8 {{ position:absolute; left:0; right:0; top:290px; text-align:center; }}
#rl-lab {{ position:absolute; left:420px; top:690px; width:600px; text-align:center; }}
#rl-lab .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="rl-title" class="h1">But real people <span class="hl">sleep</span></div>
  <div id="rl-8"><span class="chip" style="background:#BFE3F7">walk 8 h a day</span></div>
  {bars}
  <div id="rl-lab"><div class="big">almost 3 years</div></div>
""", f"""
rise("#rl-title", {tsl:.2f}); pop("#rl-8 .chip", {t8:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
for (let i=0;i<3;i++) tl.to("#rl-f"+i, {{scaleX:1, duration:0.55, ease:"power1.inOut"}}, {t8+0.5:.2f}+i*0.55);
pop("#rl-lab", {t3y:.2f});
""")

# 9 OCEAN — 71 of 100 squares are water
s = "ocean"; tpr = aw(s, "one small"); t71 = aw(s, "seventy one"); tbo = aw(s, "a boat"); tws = aw(s, "wet socks")
gr = "".join(f'<rect id="oc-c{i}" x="{110+(i%10)*52}" y="{260+(i//10)*52}" width="46" height="46" fill="#C9E7B8" stroke="{K}" stroke-width="2"/>' for i in range(100))
scenes[s] = scene_file(s, f"""
#oc-title {{ top:150px; font-size:72px; }}
#oc-lab {{ position:absolute; left:660px; top:330px; width:380px; text-align:center; }}
#oc-lab .big {{ font-size:110px; color:{C['blue']}; }}
#oc-boat {{ position:absolute; left:690px; top:600px; }}
#oc-sock {{ position:absolute; left:880px; top:600px; }}
""", f"""
  <div id="oc-title" class="h1">One small problem…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" data-layout-ignore>{gr}</svg>
  <div id="oc-lab"><div class="big">71%</div><div style="font-size:50px">is water</div></div>
  <svg id="oc-boat" width="170" height="130" viewBox="0 0 170 130" data-layout-ignore>
    <path d="M10,80 L160,80 Q140,118 30,118 Z" fill="{C['red']}" {WS.replace('fill="none" ', '')}/><path d="M85,80 L85,10 L140,66 Z" fill="#fff" {WS.replace('fill="none" ', '')}/></svg>
  <svg id="oc-sock" width="120" height="170" viewBox="0 0 120 170" data-layout-ignore>
    <path d="M30,10 L80,10 L80,90 Q110,100 104,130 Q96,152 60,142 L20,128 Q8,110 30,94 Z" fill="{C['hi']}" {WS.replace('fill="none" ', '')}/>
    <path id="oc-dr" d="M70,150 Q76,160 70,166 Q64,160 70,150 Z" fill="#BFE3F7" stroke="{C['blue']}" stroke-width="3"/></svg>
""", f"""
rise("#oc-title", {tpr-0.3:.2f});
for (let i=0;i<100;i++) tl.fromTo("#oc-c"+i, {{opacity:0}}, {{opacity:1, duration:0.05}}, {tpr+0.3:.2f}+i*0.012);
for (let i=0;i<71;i++) tl.to("#oc-c"+i, {{fill:"#7FB7E0", duration:0.04}}, {t71-0.3:.2f}+i*0.02);
pop("#oc-lab", {t71+0.4:.2f}); pop("#oc-boat", {tbo:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-4}}}});
pop("#oc-sock", {tws:.2f}, {{from:{{rotation:20}}, to:{{rotation:6}}}});
tl.fromTo("#oc-dr", {{y:0, opacity:1}}, {{y:20, opacity:0, duration:0.5, repeat:3}}, {tws+0.3:.2f});
""")

# 10 SPIN — Earth carries you
s = "spin"; tsp = aw(s, "earth spins"); tst = aw(s, "just stand"); t1k = aw(s, "a thousand"); tday = aw(s, "every single day")
scenes[s] = scene_file(s, f"""
#sn-title {{ top:150px; font-size:76px; }}
#sn-g {{ position:absolute; left:110px; top:280px; }}
#sn-pin {{ position:absolute; left:250px; top:430px; }}
#sn-v {{ position:absolute; left:520px; top:300px; width:540px; text-align:center; }}
#sn-v .big {{ white-space:nowrap; font-size:88px; color:{C['red']}; }}
#sn-day {{ position:absolute; left:520px; top:680px; width:540px; text-align:center; }}
""", f"""
  <div id="sn-title" class="h1">Here's the <span class="hl">twist</span></div>
  <div id="sn-g">{globe('sn-gl', 190)}</div>
  <svg id="sn-pin" width="120" height="120" viewBox="0 0 60 60" data-layout-ignore>
    <rect x="18" y="4" width="24" height="20" fill="{C['hi']}" stroke="{K}" stroke-width="3"/><circle cx="26" cy="13" r="2" fill="{K}"/><circle cx="34" cy="13" r="2" fill="{K}"/>
    <rect x="22" y="26" width="16" height="16" fill="#fff" stroke="{K}" stroke-width="3"/><path d="M26,42 L24,56 M34,42 L36,56" stroke="{K}" stroke-width="3" stroke-linecap="round"/></svg>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <path id="sn-arc" d="M140,300 Q300,200 470,320 M450,300 L470,320 L445,330" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="sn-v"><div style="font-size:46px">standing still<br>on the equator</div><div class="big">≈ 1,000 mph</div></div>
  <div id="sn-day"><span class="pill red" style="font-size:64px">1 lap every day</span></div>
""", f"""
rise("#sn-title", 0.0); pop("#sn-g", 0.2);
tl.fromTo("#sn-gl-land", {{x:0}}, {{x:-400, duration:{SC['spin']['slot']-0.4:.2f}, ease:"none"}}, 0.3);
draw("#sn-arc", {tsp:.2f}, 0.6); pop("#sn-pin", {tst:.2f});
rise("#sn-v", {t1k-0.3:.2f}); pop("#sn-day .pill", {tday:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 11 OUTRO
s = "outro"; twk = aw(s, "nonstop walking"); tsd = aw(s, "standing still"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:160px; font-size:72px; }}
#ou-b {{ top:300px; font-size:72px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">walking: <span class="hl">almost a year</span></div>
  <div id="ou-b" class="h1">standing: <span class="red">1 day</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {twk-0.4:.2f}); pop("#ou-b", {tsd:.2f}, {{from:{{rotation:-10}}, to:{{}}}});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "how long"), SC["guess"]["start"] + 0.2)
point(g("guess", "a month"), 2.4)
wave(g("intro", "I'm Max"))
point(g("distance", "twenty five"), 1.4)
point(g("speed", "three miles"), 1.2)
wow(g("hours", "eight thousand"), 1.3)
wow(g("nonstop", "whole year"), 1.3)
point(g("real", "almost three"), 1.3)
think(SC["ocean"]["start"] + 0.05, g("ocean", "about seventy"))
point(g("ocean", "seventy one"), 1.2)
wow(g("spin", "a thousand"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "the equator"), 0.35), ("pop.mp3", A("guess", "a month"), 0.5), ("pop.mp3", A("guess", "a year"), 0.5),
        ("pop.mp3", A("guess", "ten years"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("distance", "twenty five"), 0.6),
        ("click.mp3", A("speed", "brisk walk"), 0.45), ("impact-bass-1.mp3", A("hours", "eight thousand") + 0.3, 0.45),
        ("pop.mp3", A("nonstop", "three hundred"), 0.5), ("pop.mp3", A("real", "almost three"), 0.5),
        ("whoosh-short.mp3", A("ocean", "a boat"), 0.3), ("riser.mp3", A("spin", "earth spins"), 0.3),
        ("impact-bass-2.mp3", A("spin", "a thousand"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
