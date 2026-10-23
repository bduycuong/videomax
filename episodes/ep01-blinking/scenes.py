# MAX WISE episode scenes. Executed inside engine/maxwise.py (all engine helpers are in scope).
# === SCENES ===
# 1 HOOK — the curious question
s = "hook"; tq = aw(s, "how much"); tcl = aw(s, "eyes closed"); taw = aw(s, "wide awake")
scenes[s] = scene_file(s, f"""
#hook-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hook-q {{ top:260px; font-size:86px; }}
#hook-eye {{ position:absolute; left:330px; top:620px; }}
#hook-aw {{ position:absolute; left:0; right:0; top:790px; text-align:center; font-size:58px; color:{C['red']}; }}
""", f"""
  <div id="hook-tag"><span class="chip">MAX WISE</span></div>
  <div id="hook-q" class="h1">How much of your life do you spend with your <span class="hl">eyes closed</span>?</div>
  <div id="hook-eye">{eye_svg('hook-e', 420)}</div>
  <div id="hook-aw">…while you're wide awake?!</div>
""", f"""
pop("#hook-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hook-q", {tq-0.05:.2f}); tl.set("#hook-e-lid", {{scaleY:0}}, 0);
pop("#hook-eye", {tcl-0.3:.2f}); blink("#hook-e-lid", {tcl+0.2:.2f}); blink("#hook-e-lid", {taw:.2f});
pop("#hook-aw", {taw:.2f}, {{from:{{rotation:6}}, to:{{rotation:-2}}}});
""")

# 2 GUESS — days? months? years?
s = "guess"; tg = aw(s, "take a guess"); td = aw(s, "few days"); tm = aw(s, "few months"); ty = aw(s, "or years")
notes = [("days", "Days?", -6, 120, C['hi']), ("months", "Months?", 4, 410, "#BFE3F7"), ("years", "Years?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:250px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;font-family:Gochi Hand,cursive;font-size:70px;line-height:250px">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-days", {td:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-months", {tm:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-years", {ty:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO — Max Wise logo
s = "intro"; tmx = aw(s, "I'm Max"); tmw = aw(s, "Max Wise"); tlt = aw(s, "let's work")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's work it out!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 RATE — 15 blinks a minute
s = "rate"; tb = aw(s, "you blink"); t15 = aw(s, "fifteen times")
tally = "".join(f'<path id="rt-t{i}" d="M{150+ (i//5)*230 + (i%5)*34},560 L{150+(i//5)*230+(i%5)*34+4},680" stroke="{K}" stroke-width="7" stroke-linecap="round" fill="none"/>' if i % 5 != 4 else
                f'<path id="rt-t{i}" d="M{140+(i//5)*230},650 L{300+(i//5)*230},580" stroke="{C["red"]}" stroke-width="7" stroke-linecap="round" fill="none"/>' for i in range(15))
scenes[s] = scene_file(s, f"""
#rt-eye {{ position:absolute; left:380px; top:200px; }}
#rt-num {{ position:absolute; left:0; right:0; top:730px; text-align:center; font-size:110px; }}
""", f"""
  <div id="rt-eye">{eye_svg('rt-e', 320)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>{tally}</svg>
  <div id="rt-num" class="big"><span class="red">15</span> blinks / minute</div>
""", f"""
pop("#rt-eye", 0.0); tl.set("#rt-e-lid", {{scaleY:0}}, 0);
for (let i=0;i<15;i++) {{ const t={tb:.2f}+i*0.16; draw("#rt-t"+i, t, 0.12); blink("#rt-e-lid", t); }}
pop("#rt-num", {t15:.2f});
""")

# 5 DURATION — a fifth of a second
s = "dur"; tl5 = aw(s, "a fifth"); tsq = aw(s, "super quick")
scenes[s] = scene_file(s, f"""
#du-watch {{ position:absolute; left:340px; top:180px; }}
#du-num {{ position:absolute; left:0; right:0; top:640px; text-align:center; font-size:140px; }}
#du-sub {{ top:800px; font-size:52px; }}
""", f"""
  <svg id="du-watch" width="400" height="430" viewBox="0 0 200 215" data-layout-ignore>
    <path d="M86,10 L114,10 M100,10 L100,26" {WS}/>
    <path d="M100,28 Q182,30 184,118 Q182,206 100,208 Q18,206 16,118 Q18,30 100,28 Z" fill="#fff" {WS.replace('fill="none" ', '')}/>
    <path id="du-wedge" d="M100,118 L100,44 A74,74 0 0 1 170,95 Z" fill="{C['hi']}" stroke="none" style="opacity:0"/>
    {''.join(f'<path d="M100,{44 if i%3==0 else 50} L100,{54}" transform="rotate({i*30} 100 118)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(12))}
    <g id="du-hand"><path d="M100,118 L100,52" stroke="{C['red']}" stroke-width="6" stroke-linecap="round"/></g>
    <circle cx="100" cy="118" r="6" fill="{K}"/></svg>
  <div id="du-num" class="big">≈ <span class="red">0.2</span> s</div>
  <div id="du-sub" class="h2">a fifth of a second</div>
""", f"""
pop("#du-watch", 0.0); tl.set("#du-hand", {{rotation:0, svgOrigin:"100 118"}}, 0);
tl.to("#du-hand", {{rotation:72, duration:0.35, ease:"power2.out"}}, {tl5:.2f}); tl.to("#du-wedge", {{opacity:1, duration:0.15}}, {tl5+0.25:.2f});
pop("#du-num", {tl5:.2f}); rise("#du-sub", {tl5+0.4:.2f});
tl.fromTo("#du-watch", {{rotation:0}}, {{rotation:6, duration:0.06, yoyo:true, repeat:5}}, {tsq:.2f});
""")

# 6 DAY — the multiplication
s = "day"; tmu = aw(s, "now multiply"); t16 = aw(s, "sixteen waking"); t14 = aw(s, "fourteen thousand"); t50 = aw(s, "nearly fifty"); tev = aw(s, "every single day")
rows = [("dy-r1", "16 h awake × 60 × 15", t16, K), ("dy-r2", "= 14,400 blinks", t14, C['blue']), ("dy-r3", "× 0.2 s = 2,880 s", t50 - 0.4, K)]
rh = "".join(f'<div id="{i}" class="abs big" style="left:110px;top:{250+k*130}px;font-size:76px;color:{c}">{txt}</div>' for k, (i, txt, t, c) in enumerate(rows))
scenes[s] = scene_file(s, f"""
#dy-ans {{ position:absolute; left:0; right:0; top:690px; text-align:center; }}
#dy-ans span {{ font-size:96px; color:{C['red']}; }}
#dy-line {{ position:absolute; left:100px; top:640px; }}
""", f"""
  <div id="dy-title" class="h1" style="top:150px;font-size:72px">Now multiply…</div>
  {rh}
  <svg id="dy-line" width="880" height="20" data-layout-ignore><path id="dy-ul" d="M4,10 Q440,2 876,12" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="dy-ans"><span class="pill">≈ 48 min / day!</span></div>
""", f"""
pop("#dy-title", {tmu:.2f}); {"".join(f'rise("#{i}", {t:.2f});' for i, _, t, _ in rows)}
draw("#dy-ul", {t50-0.1:.2f}, 0.3); pop("#dy-ans span", {t50+0.3:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
tl.fromTo("#dy-ans span", {{scale:1}}, {{scale:1.12, duration:0.14, yoyo:true, repeat:1}}, {tev:.2f});
""")

# 7 LIFE — 80-year ruler
s = "life"; t80 = aw(s, "eighty years"); t3 = aw(s, "almost three")
X0, X1, Y = 110, 970, 520
ticks = "".join(f'<path d="M{X0+(X1-X0)*y/80:.1f},{Y-(26 if y%20==0 else 14)} L{X0+(X1-X0)*y/80:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{X0+(X1-X0)*y/80:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 20 == 0 else "") for y in range(0, 81, 5))
seg = (X1 - X0) * 2.7 / 80
scenes[s] = scene_file(s, f"""
#lf-bar {{ position:absolute; left:{X0}px; top:{Y-70}px; width:{X1-X0}px; height:60px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-seg {{ position:absolute; right:0; top:0; height:100%; width:{seg:.1f}px; transform-origin:100% 50%; }}
#lf-lab {{ position:absolute; right:90px; top:600px; text-align:right; }}
#lf-lab .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="lf-title" class="h1" style="top:160px;font-size:76px">A whole life: <span class="hl">80 years</span></div>
  <div id="lf-bar"><div id="lf-seg" class="hatch-r"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore>{ticks}
    <path id="lf-arrow" d="M760,700 Q900,680 930,{Y+20}" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="lf-lab"><div class="big">≈ 2.7 years</div><div style="font-size:44px;color:{C['muted']}">≈ 23,000 hours of blinking</div></div>
""", f"""
rise("#lf-title", 0.0); rise("#lf-bar", 0.1);
tl.fromTo("#lf-seg", {{scaleX:0}}, {{scaleX:1, duration:0.6, ease:"power2.out"}}, {t3:.2f});
draw("#lf-arrow", {t3+0.2:.2f}, 0.4); pop("#lf-lab", {t3+0.3:.2f});
""")

# 8 NOTICE — brain switches vision off
s = "notice"; tdk = aw(s, "go dark"); tbr = aw(s, "your brain"); tsw = aw(s, "switches off"); tng = aw(s, "never notice")
scenes[s] = scene_file(s, f"""
#nt-brain {{ position:absolute; left:120px; top:300px; }}
#nt-sw {{ position:absolute; left:640px; top:340px; width:300px; height:150px; }}
#nt-lab {{ position:absolute; left:600px; top:520px; width:400px; text-align:center; font-size:46px; }}
#nt-q {{ top:160px; font-size:70px; }}
""", f"""
  <div id="nt-q" class="h1">Why doesn't the world <span class="hl">go dark</span>?</div>
  <svg id="nt-brain" width="420" height="340" viewBox="0 0 210 170" data-layout-ignore>
    <path d="M40,120 Q10,110 18,80 Q8,50 40,40 Q50,12 86,20 Q106,4 130,18 Q166,10 176,42 Q206,54 194,88 Q204,120 172,128 Q166,154 134,148 Q112,166 88,150 Q58,160 40,120 Z" fill="#FFD6E0" {WS.replace('fill="none" ', '')}/>
    <path d="M60,60 Q80,50 90,70 Q100,90 120,76 M70,100 Q96,96 110,116 M130,48 Q150,40 160,60 M140,96 Q160,90 170,104" {WS}/></svg>
  <svg id="nt-sw" viewBox="0 0 300 150" data-layout-ignore>
    <rect x="10" y="30" width="280" height="90" rx="45" fill="#fff" stroke="{K}" stroke-width="5"/>
    <g id="nt-knob"><circle cx="60" cy="75" r="34" fill="{C['blue']}" stroke="{K}" stroke-width="5"/></g>
    <text id="nt-on" x="190" y="90" text-anchor="middle" font-family="Gochi Hand" font-size="44" fill="{K}">ON</text>
    <text id="nt-off" x="110" y="90" text-anchor="middle" font-family="Gochi Hand" font-size="44" fill="{C['red']}" opacity="0">OFF</text></svg>
  <div id="nt-lab">vision, paused<br>for every blink</div>
""", f"""
rise("#nt-q", {tdk-0.8:.2f}); pop("#nt-brain", {tbr:.2f}); pop("#nt-sw", {tbr+0.2:.2f});
for (let k=0;k<3;k++) {{ const t={tsw:.2f}+k*0.9;
  tl.to("#nt-knob", {{x:180, fill:"{C['red']}", duration:0.12}}, t); tl.set("#nt-on", {{opacity:0}}, t); tl.set("#nt-off", {{opacity:1}}, t);
  tl.to("#nt-knob", {{x:0, duration:0.12}}, t+0.3); tl.set("#nt-on", {{opacity:1}}, t+0.3); tl.set("#nt-off", {{opacity:0}}, t+0.3); }}
rise("#nt-lab", {tsw+0.3:.2f});
""")

# 9 WHY — windshield wiper
s = "why"; tww = aw(s, "windshield wiper"); tft = aw(s, "fresh tears"); tcl = aw(s, "clean and wet")
drops = "".join(f'<path id="wy-d{i}" d="M{x},{y} Q{x+10},{y+18} {x},{y+26} Q{x-10},{y+18} {x},{y} Z" fill="#BFE3F7" stroke="{C["blue"]}" stroke-width="3"/>' for i, (x, y) in enumerate([(380, 300), (520, 260), (660, 300), (450, 380), (600, 390)]))
scenes[s] = scene_file(s, f"""
#wy-eye {{ position:absolute; left:240px; top:240px; }}
#wy-lab {{ position:absolute; left:0; right:0; top:690px; text-align:center; font-size:56px; }}
""", f"""
  <div id="wy-title" class="h1" style="top:150px;font-size:74px">Built-in <span class="hl">wiper</span></div>
  <div id="wy-eye">{eye_svg('wy-e', 600)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore>{drops}
    <g id="wy-wiper" style="opacity:0"><path d="M540,640 L540,300" stroke="{K}" stroke-width="12" stroke-linecap="round"/><path d="M528,300 L552,300 L548,640 L532,640 Z" fill="{K}"/></g></svg>
  <div id="wy-lab"><span class="blue">fresh tears</span> → clean + wet</div>
""", f"""
rise("#wy-title", 0.0); pop("#wy-eye", 0.1); tl.set("#wy-e-lid", {{scaleY:0}}, 0);
tl.set("#wy-wiper", {{rotation:-60, svgOrigin:"540 640"}}, 0);
tl.to("#wy-wiper", {{opacity:1, duration:0.15}}, {tww-0.2:.2f});
for (let k=0;k<3;k++) {{ const t={tww:.2f}+k*0.8; tl.to("#wy-wiper", {{rotation:60, duration:0.35, ease:"sine.inOut"}}, t); tl.to("#wy-wiper", {{rotation:-60, duration:0.35, ease:"sine.inOut"}}, t+0.4); blink("#wy-e-lid", t+0.1); }}
for (let i=0;i<5;i++) pop("#wy-d"+i, {tft:.2f}+i*0.08);
rise("#wy-lab", {tcl-0.2:.2f});
""")

# 10 SCREEN — blinking drops
s = "screen"; tst = aw(s, "stare at"); tdr = aw(s, "drop to"); t45 = aw(s, "four or five"); tdry = aw(s, "so dry")
scenes[s] = scene_file(s, f"""
#sc-phone {{ position:absolute; left:120px; top:250px; }}
#sc-cnt {{ position:absolute; left:520px; top:300px; width:480px; text-align:center; }}
#sc-cnt .big {{ font-size:150px; }}
#sc-dry {{ position:absolute; left:520px; top:640px; width:480px; text-align:center; }}
#sc-dry span {{ color:{C['red']}; font-size:60px; }}
""", f"""
  <div id="sc-title" class="h1" style="top:150px;font-size:72px">Screens = <span class="hl">fewer blinks</span></div>
  <svg id="sc-phone" width="320" height="560" viewBox="0 0 160 280" data-layout-ignore>
    <path d="M24,8 Q80,4 136,9 Q150,140 135,272 Q80,276 25,271 Q10,140 24,8 Z" fill="#fff" {WS.replace('fill="none" ', '')}/>
    <path d="M36,30 Q80,27 124,31 L122,236 Q80,239 38,236 Z" fill="#DDEFF7" stroke="{K}" stroke-width="3"/>
    <path d="M60,90 Q80,74 100,90 Q80,106 60,90 Z" fill="#fff" stroke="{K}" stroke-width="3"/><circle cx="80" cy="90" r="7" fill="{K}"/>
    <path d="M50,130 L110,130 M50,150 L100,150 M50,170 L106,170 M50,190 L90,190" stroke="{C['pencil']}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="80" cy="254" r="9" fill="none" stroke="{K}" stroke-width="3"/></svg>
  <div id="sc-cnt"><div id="sc-n" class="big red">15</div><div style="font-size:46px">blinks / minute</div></div>
  <div id="sc-dry"><span class="pill">dry eyes!</span></div>
""", f"""
rise("#sc-title", 0.0); pop("#sc-phone", {tst:.2f}); pop("#sc-cnt", {tst+0.3:.2f});
count("#sc-n", 15, 4.5, {tdr:.2f}, {t45-tdr+0.6:.2f}, v => v < 6 ? "4–5" : String(Math.round(v)));
pop("#sc-dry span", {tdry:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-5}}}});
""")

# 11 OUTRO
s = "outro"; ta3 = aw(s, "almost three"); tnv = aw(s, "never saw"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">2.7 years</span> of blinking…</div>
  <div id="ou-b" class="h1">…and you never saw a second of it.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {ta3:.2f}); rise("#ou-b", {tnv:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "here's") , SC["guess"]["start"] + 0.2)
point(g("guess", "few days"), 2.6)
wave(g("intro", "I'm Max"))
point(g("rate", "fifteen times"), 1.2)
point(g("dur", "a fifth"), 1.0)
wow(g("day", "every single day"))
wow(g("life", "almost three"), 1.6)
think(SC["notice"]["start"] + 0.05, g("notice", "your brain"))
point(g("notice", "switches off"), 1.4)
point(g("why", "windshield wiper"), 1.4)
wow(g("screen", "four or five"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "eyes closed"), 0.35), ("pop.mp3", A("guess", "few days"), 0.5), ("pop.mp3", A("guess", "few months"), 0.5),
        ("pop.mp3", A("guess", "or years"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("dur", "a fifth"), 0.6),
        ("pop.mp3", A("day", "nearly fifty") + 0.3, 0.55), ("impact-bass-1.mp3", A("life", "almost three") + 0.3, 0.45),
        ("click.mp3", A("notice", "switches off"), 0.4), ("whoosh-short.mp3", A("why", "windshield wiper"), 0.3),
        ("pop.mp3", A("screen", "so dry"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
