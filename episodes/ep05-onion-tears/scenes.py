# MAX WISE ep05 — Why does chopping an onion make you cry? Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
ON = "#F2C9A0"; ONL = "#E7A97A"; GAS = "#CFE8B8"
def onion_svg(pid, w=300):
    return (f'<svg id="{pid}" width="{w}" height="{w*1.1:.0f}" viewBox="0 0 200 220" style="overflow:visible" data-layout-ignore>'
            f'<path d="M100,28 Q96,10 104,2 M100,28 Q110,12 122,10" {WS}/>'
            f'<path d="M100,30 Q170,60 176,130 Q178,196 100,206 Q22,196 24,130 Q30,60 100,30 Z" fill="{ON}" {WSF}/>'
            f'<path d="M100,34 Q140,80 140,130 Q138,180 100,202 M100,34 Q60,80 60,130 Q62,180 100,202 M100,34 L100,202" stroke="{ONL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
            f'<path d="M84,206 L80,216 M100,207 L100,218 M116,206 L120,216" {WS}/></svg>')
def cloud(pid, x, y, sc=1.0):
    return (f'<g id="{pid}"><g transform="translate({x},{y}) scale({sc})"><path d="M-60,20 Q-80,-10 -50,-24 Q-40,-56 -6,-46 Q14,-70 42,-46 Q78,-50 72,-14 Q92,10 60,26 Q0,36 -60,20 Z" fill="{GAS}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></g></g>')

# 1 HOOK
s = "hook"; tco = aw(s, "chopping an onion"); tcr = aw(s, "make you cry"); tns = aw(s, "not sad")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:84px; }}
#hk-on {{ position:absolute; left:250px; top:560px; }}
#hk-eye {{ position:absolute; left:570px; top:600px; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">Why does chopping an <span class="hl">onion</span> make you cry?</div>
  <div id="hk-on">{onion_svg('hk-o', 260)}</div>
  <div id="hk-eye">{eye_svg('hk-e', 280)}
    <svg class="abs" style="left:110px;top:150px" width="60" height="140" data-layout-ignore><path id="hk-t" d="M30,4 Q48,40 30,60 Q12,40 30,4 Z" fill="#BFE3F7" stroke="{C['blue']}" stroke-width="4"/></svg></div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tco-0.4:.2f}); pop("#hk-on", {tco:.2f}); pop("#hk-eye", {tcr:.2f}); tl.set("#hk-e-lid", {{scaleY:0}}, 0);
tl.fromTo("#hk-t", {{opacity:0, y:0}}, {{opacity:1, y:70, duration:0.9, ease:"power1.in"}}, {tcr+0.3:.2f});
blink("#hk-e-lid", {tns:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); ta = aw(s, "the smell"); tb = aw(s, "the juice"); tc = aw(s, "invisible gas")
notes = [("a", "the smell?", -6, 110, C['hi']), ("b", "the juice?", 4, 400, "#BFE3F7"), ("c", "an invisible gas?", -3, 690, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:280px;height:250px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:60px;line-height:1.05;padding:10px">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {ta:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {tb:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {tc:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's zoom")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's zoom in!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 CELLS — tiny cells with sulfur chemicals
s = "cells"; tc = aw(s, "tiny cells"); ts = aw(s, "contain sulfur")
cells = "".join(f'<g id="ce-c{i}"><path d="M{x},{y} Q{x+60},{y-6} {x+120},{y} Q{x+126},{y+50} {x+120},{y+100} Q{x+60},{y+106} {x},{y+100} Q{x-6},{y+50} {x},{y} Z" fill="#FFF3E2" stroke="{ONL}" stroke-width="4"/>'
                f'<circle class="ce-s" cx="{x+40}" cy="{y+40}" r="11" fill="{C["hi"]}" stroke="{K}" stroke-width="3"/><circle class="ce-s" cx="{x+80}" cy="{y+66}" r="11" fill="{C["hi"]}" stroke="{K}" stroke-width="3"/></g>'
                for i, (x, y) in enumerate([(150 + c * 140, 330 + r * 120 + (c % 2) * 30) for r in range(3) for c in range(6)]))
scenes[s] = scene_file(s, f"""
#ce-title {{ top:150px; font-size:76px; }}
#ce-lab {{ position:absolute; left:0; right:0; top:760px; text-align:center; font-size:56px; }}
""", f"""
  <div id="ce-title" class="h1">Zoom: <span class="hl">onion cells</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="740" data-layout-ignore>{cells}</svg>
  <div id="ce-lab"><span style="display:inline-block;width:30px;height:30px;border-radius:50%;background:{C['hi']};border:3px solid {K};vertical-align:middle"></span> = sulfur chemicals</div>
""", f"""
rise("#ce-title", 0.0);
tl.fromTo("[id^='ce-c']", {{opacity:0, scale:0.6, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.25, stagger:0.05, ease:"back.out(2)"}}, {tc-0.2:.2f});
tl.fromTo(".ce-s", {{scale:0, transformOrigin:"50% 50%"}}, {{scale:1, duration:0.2, stagger:0.02, ease:"back.out(3)"}}, {ts-0.3:.2f});
rise("#ce-lab", {ts:.2f});
""")

# 5 CUT — knife bursts the cells
s = "cut"; tk = aw(s, "your knife"); tb = aw(s, "burst open"); tm = aw(s, "chemicals mix")
scenes[s] = scene_file(s, f"""
#cu-title {{ top:150px; font-size:76px; }}
#cu-on {{ position:absolute; left:360px; top:330px; }}
#cu-knife {{ position:absolute; left:150px; top:280px; }}
#cu-lab {{ position:absolute; left:0; right:0; top:800px; text-align:center; }}
#cu-lab span {{ font-size:60px; color:{C['red']}; }}
""", f"""
  <div id="cu-title" class="h1"><span class="hl">Slice!</span></div>
  <div id="cu-on">{onion_svg('cu-o', 360)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" data-layout-ignore>
    {''.join(f'<circle id="cu-b{i}" cx="{540+90*__import__("math").cos(i*0.9):.0f}" cy="{560+70*__import__("math").sin(i*0.9):.0f}" r="{10+(i%3)*4}" fill="{C["hi"]}" stroke="{K}" stroke-width="3"/>' for i in range(7))}</svg>
  <svg id="cu-knife" width="760" height="200" viewBox="0 0 380 100" data-layout-ignore>
    <path d="M10,60 Q120,30 260,50 L262,74 Q130,82 10,60 Z" fill="#E8EEF2" {WSF}/>
    <path d="M262,48 L370,44 Q376,62 370,78 L262,76 Z" fill="{C['red']}" {WSF}/></svg>
  <div id="cu-lab"><span class="pill">cells burst, chemicals mix</span></div>
""", f"""
rise("#cu-title", {tk-0.3:.2f}); pop("#cu-on", 0.1);
tl.fromTo("#cu-knife", {{x:500, y:-40, opacity:0}}, {{x:0, y:200, opacity:1, duration:0.5, ease:"power2.in"}}, {tk:.2f});
tl.fromTo("[id^='cu-b']", {{scale:0, opacity:0, transformOrigin:"50% 50%"}}, {{scale:1, opacity:1, duration:0.3, stagger:0.06, ease:"back.out(3)"}}, {tb:.2f});
tl.fromTo("#cu-on", {{rotation:0}}, {{rotation:4, duration:0.08, yoyo:true, repeat:3}}, {tb:.2f});
pop("#cu-lab .pill", {tm:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 6 ENZYME — chemicals -> unstable acid -> irritating gas
s = "enzyme"; te = aw(s, "enzymes turn"); ta = aw(s, "unstable acid"); tg = aw(s, "irritating gas")
scenes[s] = scene_file(s, f"""
#ez-title {{ top:150px; font-size:76px; }}
.ez-box {{ position:absolute; left:220px; width:640px; height:110px; background:#fff; border:4px solid {K}; {SKETCH} display:flex; align-items:center; justify-content:center; font-family:'Gochi Hand',cursive; font-size:56px; }}
.ez-ar {{ position:absolute; left:500px; width:80px; height:70px; }}
#ez-tag {{ position:absolute; left:600px; top:400px; font-size:40px; color:{C['blue']}; }}
""", f"""
  <div id="ez-title" class="h1">The <span class="hl">chain</span></div>
  <div id="ez-1" class="ez-box" style="top:290px;background:#FFF3E2">sulfur chemicals</div>
  <svg id="ez-a1" class="ez-ar" style="top:405px" viewBox="0 0 80 70" data-layout-ignore><path d="M40,4 L40,60 M22,42 L40,62 L58,42" {WS}/></svg>
  <div id="ez-tag">+ enzymes</div>
  <div id="ez-2" class="ez-box" style="top:480px;background:{C['hi']}">unstable acid</div>
  <svg id="ez-a2" class="ez-ar" style="top:595px" viewBox="0 0 80 70" data-layout-ignore><path d="M40,4 L40,60 M22,42 L40,62 L58,42" {WS}/></svg>
  <div id="ez-3" class="ez-box" style="top:670px;background:{GAS}">irritating gas!</div>
""", f"""
rise("#ez-title", 0.0); rise("#ez-1", 0.1);
pop("#ez-a1", {te:.2f}); pop("#ez-tag", {te+0.1:.2f}); pop("#ez-2", {ta:.2f});
pop("#ez-a2", {tg-0.5:.2f}); pop("#ez-3", {tg:.2f});
tl.fromTo("#ez-3", {{rotation:0}}, {{rotation:2, duration:0.1, yoyo:true, repeat:5}}, {tg+0.4:.2f});
""")

# 7 GAS — floats up into your eyes
s = "gas"; tf = aw(s, "floats up"); te = aw(s, "your eyes")
scenes[s] = scene_file(s, f"""
#gs2-eye {{ position:absolute; left:330px; top:170px; }}
#gs2-on {{ position:absolute; left:440px; top:700px; }}
""", f"""
  <div id="gs2-eye">{eye_svg('ge-e', 420)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore>
    {cloud('ge-c1', 520, 640, 0.7)}{cloud('ge-c2', 600, 560, 0.6)}{cloud('ge-c3', 480, 480, 0.55)}
    <path id="ge-w1" d="M560,690 Q520,620 560,560 Q600,500 560,420" stroke="{C['muted']}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="10 12"/></svg>
  <div id="gs2-on">{onion_svg('ge-o', 200)}</div>
""", f"""
pop("#gs2-eye", 0.0); tl.set("#ge-e-lid", {{scaleY:0}}, 0); pop("#gs2-on", 0.1);
for (let i=1;i<=3;i++) tl.fromTo("#ge-c"+i, {{opacity:0, y:120}}, {{opacity:0.95, y:0, duration:1.0, ease:"power1.out"}}, {tf-0.2:.2f}+i*0.2);
draw("#ge-w1", {tf:.2f}, 0.8);
blink("#ge-e-lid", {te:.2f}); blink("#ge-e-lid", {te+0.4:.2f});
""")

# 8 TEARS — glands flood the eyes
s = "tears"; tat = aw(s, "the attack"); tgl = aw(s, "tear glands"); tcr = aw(s, "the crying")
drops = "".join(f'<path id="tr-d{i}" d="M{x},0 Q{x+16},32 {x},48 Q{x-16},32 {x},0 Z" fill="#BFE3F7" stroke="{C["blue"]}" stroke-width="4"/>' for i, x in enumerate([420, 520, 620, 470, 570]))
scenes[s] = scene_file(s, f"""
#tr-title {{ top:150px; font-size:76px; }}
#tr-eye {{ position:absolute; left:290px; top:280px; }}
#tr-drops {{ position:absolute; left:0; top:560px; }}
#tr-lab {{ position:absolute; left:0; right:0; top:820px; text-align:center; }}
#tr-lab span {{ font-size:62px; color:{C['blue']}; }}
""", f"""
  <div id="tr-title" class="h1">Tear <span class="hl">flood!</span></div>
  <div id="tr-eye">{eye_svg('tr-e', 500)}</div>
  <svg id="tr-drops" width="{W}" height="250" data-layout-ignore>{drops}</svg>
  <div id="tr-lab"><span class="pill">wash it away</span></div>
""", f"""
rise("#tr-title", {tgl-0.4:.2f}); pop("#tr-eye", 0.0); tl.set("#tr-e-lid", {{scaleY:0}}, 0);
blink("#tr-e-lid", {tat:.2f});
for (let k=0;k<3;k++) for (let i=0;i<5;i++) tl.fromTo("#tr-d"+i, {{opacity:0, y:0}}, {{opacity:1, y:180, duration:0.7, ease:"power1.in"}}, {tgl:.2f}+k*0.8+i*0.12);
pop("#tr-lab .pill", {tgl+0.6:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.fromTo("#tr-eye", {{rotation:0}}, {{rotation:-4, duration:0.1, yoyo:true, repeat:3}}, {tcr:.2f});
""")

# 9 FOUND — key enzyme pinned down in 2002
s = "found"; tsc = aw(s, "scientists only"); tk = aw(s, "key tear"); ty = aw(s, "two thousand")
scenes[s] = scene_file(s, f"""
#fd-title {{ top:150px; font-size:76px; }}
#fd-mag {{ position:absolute; left:140px; top:300px; }}
#fd-year {{ position:absolute; left:540px; top:350px; width:440px; text-align:center; font-size:150px; color:{C['red']}; }}
#fd-lab {{ position:absolute; left:500px; top:540px; width:520px; text-align:center; font-size:52px; }}
""", f"""
  <div id="fd-title" class="h1">Only <span class="hl">recently</span> solved</div>
  <svg id="fd-mag" width="340" height="400" viewBox="0 0 170 200" data-layout-ignore>
    <circle cx="70" cy="70" r="54" fill="#E9F4FB" stroke="{K}" stroke-width="6"/>
    <path d="M110,110 L160,180" stroke="{K}" stroke-width="14" stroke-linecap="round"/>
    <path id="fd-mol" d="M40,70 L58,56 L78,70 L98,56 M58,56 L58,36 M78,70 L78,92" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <circle cx="40" cy="70" r="7" fill="{C['hi']}" stroke="{K}" stroke-width="3"/><circle cx="98" cy="56" r="7" fill="{C['red']}" stroke="{K}" stroke-width="3"/></svg>
  <div id="fd-year" class="big">2002</div>
  <div id="fd-lab">the key tear-making enzyme found</div>
""", f"""
rise("#fd-title", {tsc:.2f}); pop("#fd-mag", {tsc+0.3:.2f}); draw("#fd-mol", {tk-0.3:.2f}, 0.5);
rise("#fd-lab", {tk:.2f}); pop("#fd-year", {ty:.2f}, {{from:{{scale:1.6}}, to:{{}}}});
""")

# 10 MASK — anti-onion gas mask ~100 years ago
s = "mask"; th = aw(s, "hundred years"); tca = aw(s, "in California"); tm = aw(s, "gas mask")
scenes[s] = scene_file(s, f"""
#mk-title {{ top:150px; font-size:72px; }}
#mk-mask {{ position:absolute; left:120px; top:290px; }}
#mk-yr {{ position:absolute; left:520px; top:340px; width:500px; text-align:center; font-size:72px; white-space:nowrap; color:{C['red']}; }}
#mk-ca {{ position:absolute; left:540px; top:470px; width:460px; text-align:center; font-size:50px; }}
#mk-lab {{ position:absolute; left:0; right:0; top:730px; text-align:center; }}
#mk-lab span {{ font-size:62px; }}
""", f"""
  <div id="mk-title" class="h1">Onion <span class="hl">armor</span></div>
  <svg id="mk-mask" width="380" height="420" viewBox="0 0 190 210" data-layout-ignore>
    <path d="M30,60 Q95,10 160,60 Q178,120 140,160 Q95,190 50,160 Q12,120 30,60 Z" fill="#9FB39A" {WSF}/>
    <circle cx="66" cy="82" r="22" fill="#E9F4FB" stroke="{K}" stroke-width="5"/><circle cx="124" cy="82" r="22" fill="#E9F4FB" stroke="{K}" stroke-width="5"/>
    <path d="M78,150 L112,150 L118,196 L72,196 Z" fill="#7C8C78" {WSF}/>
    <path d="M76,166 L114,166 M74,180 L116,180" {WS}/>
    <path d="M30,60 L6,40 M160,60 L184,40" {WS}/></svg>
  <div id="mk-yr" class="big">≈ 100 years ago</div>
  <div id="mk-ca">an army camp in California</div>
  <div id="mk-lab"><span class="pill">anti-onion gas mask!</span></div>
""", f"""
rise("#mk-title", 0.0); pop("#mk-yr", {th-0.3:.2f}); rise("#mk-ca", {tca-0.4:.2f});
pop("#mk-mask", {tm-0.6:.2f}, {{from:{{rotation:-12}}, to:{{rotation:0}}}}); pop("#mk-lab .pill", {tm:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 11 OUTRO
s = "outro"; tns = aw(s, "not sadness"); tcl = aw(s, "tiny cloud"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:66px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">Not sadness…</div>
  <div id="ou-b" class="h1">…a tiny cloud of <span class="hl">onion chemistry</span>.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tns:.2f}); rise("#ou-b", {tcl-0.3:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "why does"), SC["guess"]["start"] + 0.2)
point(g("guess", "the smell"), 2.6)
wave(g("intro", "I'm Max"))
point(g("cells", "tiny cells"), 1.4)
wow(g("cut", "burst open"), 1.2)
point(g("enzyme", "irritating gas"), 1.4)
think(SC["gas"]["start"] + 0.1, g("gas", "your eyes"))
wow(g("tears", "the crying"), 1.2)
point(g("found", "two thousand"), 1.4)
wow(g("mask", "gas mask"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "make you cry"), 0.35), ("pop.mp3", A("guess", "the smell"), 0.5), ("pop.mp3", A("guess", "the juice"), 0.5),
        ("pop.mp3", A("guess", "invisible gas"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("whoosh-short.mp3", A("cut", "your knife"), 0.4),
        ("pop.mp3", A("cut", "burst open"), 0.55), ("click-soft.mp3", A("enzyme", "unstable acid"), 0.55), ("pop.mp3", A("enzyme", "irritating gas"), 0.5),
        ("impact-bass-1.mp3", A("found", "two thousand"), 0.4), ("pop.mp3", A("mask", "gas mask"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
