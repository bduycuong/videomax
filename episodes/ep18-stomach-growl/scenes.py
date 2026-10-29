# MAX WISE ep18 — Why does your stomach growl?
# === SCENES ===
def stomach(pid, w=360, fill="#FFD6E0", inner=""):
    return f'''<svg viewBox="0 0 200 200" width="{w}" height="{w}" style="overflow:visible" data-layout-ignore>
  <path id="{pid}-body" d="M78,18 L102,18 Q100,48 116,60 Q176,58 182,112 Q186,170 128,182 Q60,192 46,140 Q38,104 70,84 Q82,70 78,18 Z" fill="{fill}" {WS.replace('fill="none" ', '')}/>
  <path d="M88,96 Q110,90 130,104 M70,140 Q100,150 140,138" stroke="#E79AAE" stroke-width="4" fill="none" stroke-linecap="round"/>
  {inner}
  <path d="M120,182 Q126,196 112,200" {WS}/></svg>'''

# 1 HOOK
s = "hook"; tqt = aw(s, "quiet"); tru = aw(s, "rumbles"); twh = aw(s, "why does")
scenes[s] = scene_file(s, f"""
#hk-shh {{ position:absolute; left:120px; top:170px; transform:rotate(-5deg); }}
#hk-st {{ position:absolute; left:360px; top:290px; }}
#hk-gr {{ position:absolute; left:640px; top:260px; font-family:'Gochi Hand',cursive; font-size:120px; color:{C['red']}; transform:rotate(8deg); }}
#hk-q {{ top:760px; font-size:84px; }}
""", f"""
  <div id="hk-shh"><span class="chip" style="background:#fff">shhh… quiet room</span></div>
  <div id="hk-st">{stomach('hk-s', 380)}</div>
  <div id="hk-gr">GRRR!</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <path id="hk-w1" d="M770,420 Q800,470 770,520" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="hk-w2" d="M810,390 Q860,470 810,550" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="hk-w3" d="M340,420 Q310,470 340,520" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="hk-q" class="h1">Why does your stomach <span class="hl">growl</span>?</div>
""", f"""
pop("#hk-shh .chip", {max(tqt-0.3,0):.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#hk-st", 0.2);
tl.fromTo("#hk-st", {{rotation:0}}, {{rotation:5, duration:0.07, yoyo:true, repeat:9, ease:"sine.inOut"}}, {tru:.2f});
pop("#hk-gr", {tru+0.05:.2f}, {{from:{{rotation:30, scale:0.2}}, to:{{rotation:8}}}});
draw("#hk-w1", {tru+0.1:.2f}, 0.2); draw("#hk-w2", {tru+0.2:.2f}, 0.2); draw("#hk-w3", {tru+0.15:.2f}, 0.2);
rise("#hk-q", {twh:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "hunger pain"); t2 = aw(s, "air you"); t3 = aw(s, "your gut")
notes = [("a", "Hunger<br>pain?", -6, 110, C['hi']), ("b", "Swallowed<br>air?", 4, 405, "#BFE3F7"), ("c", "Gut<br>cleaning?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;font-family:Gochi Hand,cursive;font-size:58px;line-height:1.05;padding-top:60px;box-sizing:border-box">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's listen")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's listen inside!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 SQUEEZE — travelling squeeze ring pushes a food blob
s = "squeeze"; tgt = aw(s, "your gut"); tsq = aw(s, "stops squeezing"); tpu = aw(s, "it pushes"); ttp = aw(s, "like toothpaste")
NSEG = 20; X0 = 100; SW = 44; TY = 430
segs = "".join(f'<div id="sq-s{i}" class="abs" style="left:{X0+i*SW}px;top:{TY}px;width:{SW+2}px;height:150px;background:#FFD6E0;border-top:5px solid {K};border-bottom:5px solid {K};box-sizing:border-box;transform-origin:50% 50%"></div>' for i in range(NSEG))
scenes[s] = scene_file(s, f"""
#sq-title {{ top:160px; font-size:76px; }}
#sq-blob {{ position:absolute; left:{X0}px; top:{TY+45}px; width:60px; height:60px; border-radius:50%; background:#C9A26B; border:4px solid {K}; opacity:0; }}
#sq-lab {{ position:absolute; left:{X0}px; top:{TY+180}px; font-size:48px; }}
#sq-tp {{ position:absolute; left:560px; top:700px; transform:rotate(-4deg); }}
""", f"""
  <div id="sq-title" class="h1">A tube that <span class="hl">never stops</span> squeezing</div>
  {segs}
  <div id="sq-blob"></div>
  <div id="sq-lab" class="blue">food, fluid + gas →</div>
  <div id="sq-tp"><span class="chip" style="background:#BFE3F7">like toothpaste!</span></div>
""", f"""
rise("#sq-title", {max(tgt-0.4,0):.2f});
for (let i=0;i<{NSEG};i++) tl.fromTo("#sq-s"+i, {{opacity:0, scaleY:0.3}}, {{opacity:1, scaleY:1, duration:0.2, ease:"back.out(2)"}}, {tgt:.2f}+i*0.04);
for (let k=0;k<3;k++) {{ const t0={tsq:.2f}+k*2.4;
  for (let i=0;i<{NSEG};i++) {{ const t=t0+i*0.1; tl.to("#sq-s"+i, {{scaleY:0.5, duration:0.12, ease:"sine.in"}}, t); tl.to("#sq-s"+i, {{scaleY:1, duration:0.18, ease:"sine.out"}}, t+0.14); }}
  tl.set("#sq-blob", {{x:0}}, t0+0.2); tl.to("#sq-blob", {{x:{(NSEG-2)*SW}, duration:1.9, ease:"none"}}, t0+0.25); }}
tl.to("#sq-blob", {{opacity:1, duration:0.1}}, {tsq+0.2:.2f});
rise("#sq-lab", {tpu:.2f}); pop("#sq-tp .chip", {ttp:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
""")

# 5 BEAT — 3 vs 12 per minute
s = "beat"; tdr = aw(s, "drummer"); t3 = aw(s, "three times"); t12 = aw(s, "twelve times"); tsi = aw(s, "your small")
d3 = "".join(f'<circle id="bt-a{i}" cx="{470+i*120}" cy="470" r="38" fill="{C["hi"]}" stroke="{K}" stroke-width="5"/>' for i in range(3))
d12 = "".join(f'<circle id="bt-b{i}" cx="{140+i*72}" cy="760" r="28" fill="#BFE3F7" stroke="{K}" stroke-width="4"/>' for i in range(12))
scenes[s] = scene_file(s, f"""
#bt-drum {{ position:absolute; left:400px; top:150px; }}
#bt-l1 {{ position:absolute; left:110px; top:430px; font-size:56px; }}
#bt-n1 {{ position:absolute; left:820px; top:425px; font-size:70px; color:{C['red']}; }}
#bt-l2 {{ position:absolute; left:110px; top:610px; font-size:56px; }}
#bt-n2 {{ position:absolute; left:740px; top:605px; font-size:70px; color:{C['red']}; }}
""", f"""
  <svg id="bt-drum" width="280" height="220" viewBox="0 0 140 110" data-layout-ignore>
    <ellipse cx="70" cy="50" rx="52" ry="16" fill="#fff" stroke="{K}" stroke-width="4"/>
    <path d="M18,50 L18,88 Q70,110 122,88 L122,50" fill="{C['red']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>
    <path d="M30,60 L50,98 L70,62 L90,100 L110,60" stroke="#fff" stroke-width="3" fill="none"/>
    <g id="bt-stick"><path d="M110,6 L74,44" stroke="{K}" stroke-width="5" stroke-linecap="round"/><circle cx="74" cy="44" r="5" fill="{K}"/></g></svg>
  <div id="bt-l1">Stomach</div><div id="bt-n1" class="big">3 / min</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="820" data-layout-ignore>{d3}{d12}</svg>
  <div id="bt-l2">Small intestine</div><div id="bt-n2" class="big">12 / min</div>
""", f"""
pop("#bt-drum", {max(tdr-0.5,0):.2f}); tl.set("#bt-stick", {{rotation:0, svgOrigin:"110 6"}}, 0);
for (let k=0;k<4;k++) {{ tl.to("#bt-stick", {{rotation:-14, duration:0.08}}, {tdr:.2f}+k*0.3); tl.to("#bt-stick", {{rotation:0, duration:0.1}}, {tdr+0.1:.2f}+k*0.3); }}
rise("#bt-l1", {t3-0.6:.2f});
for (let i=0;i<3;i++) pop("#bt-a"+i, {t3:.2f}+i*0.25);
pop("#bt-n1", {t3+0.8:.2f});
rise("#bt-l2", {tsi:.2f});
for (let i=0;i<12;i++) pop("#bt-b"+i, {t12-0.1:.2f}+i*0.08);
pop("#bt-n2", {t12+0.6:.2f});
for (let k=0;k<6;k++) for (let i=0;i<12;i++) {{ const t={t12+1.2:.2f}+k*0.5+i*0.04; tl.to("#bt-b"+i, {{fill:"{C['blue']}", duration:0.05}}, t); tl.to("#bt-b"+i, {{fill:"#BFE3F7", duration:0.1}}, t+0.08); }}
""")

# 6 EMPTY — 2 hours, cleaning wave, 10–20 min
s = "empty"; thp = aw(s, "hungry part"); t2h = aw(s, "two hours"); tcw = aw(s, "cleaning wave"); tsw = aw(s, "it sweeps"); t1020 = aw(s, "ten to twenty")
crumbs = "".join(f'<circle id="em-c{i}" cx="{560+i*55}" cy="{600+(i%2)*18}" r="12" fill="#C9A26B" stroke="{K}" stroke-width="3"/>' for i in range(6))
scenes[s] = scene_file(s, f"""
#em-title {{ top:150px; font-size:74px; }}
#em-clock {{ position:absolute; left:120px; top:270px; }}
#em-2h {{ position:absolute; left:360px; top:320px; }}
#em-st {{ position:absolute; left:790px; top:230px; }}
#em-rng {{ position:absolute; left:450px; top:770px; width:520px; text-align:center; }}
""", f"""
  <div id="em-title" class="h1">Empty stomach…</div>
  <svg id="em-clock" width="220" height="220" viewBox="0 0 110 110" data-layout-ignore>
    <circle cx="55" cy="55" r="48" fill="#fff" stroke="{K}" stroke-width="5"/>
    <g id="em-hand"><path d="M55,55 L55,20" stroke="{C['red']}" stroke-width="5" stroke-linecap="round"/></g>
    <path d="M55,55 L78,55" stroke="{K}" stroke-width="5" stroke-linecap="round"/><circle cx="55" cy="55" r="4" fill="{K}"/></svg>
  <div id="em-2h"><span class="pill red" style="font-size:64px">2 hours later</span></div>
  <div id="em-st">{stomach('em-s', 200, fill="#fff")}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <path id="em-tube" d="M110,560 L980,560 M110,660 L980,660" {WS}/>
    {crumbs}
    <g id="em-wave" style="opacity:0"><path d="M130,560 Q190,610 130,660" stroke="{C['blue']}" stroke-width="12" fill="none" stroke-linecap="round"/>
      <path d="M100,575 Q150,610 100,645" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round" opacity=".6"/></g></svg>
  <div id="em-rng"><div style="font-size:46px">each wave lasts</div>
    <svg width="460" height="40" data-layout-ignore><path id="em-bar" d="M20,8 L20,32 M20,20 L440,20 M440,8 L440,32" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
    <div class="big" style="font-size:72px">10–20 min</div></div>
""", f"""
rise("#em-title", {thp:.2f}); pop("#em-clock", {thp+0.3:.2f}); tl.set("#em-hand", {{rotation:0, svgOrigin:"55 55"}}, 0);
tl.to("#em-hand", {{rotation:720, duration:1.0, ease:"power2.inOut"}}, {t2h-0.6:.2f});
pop("#em-2h .pill", {t2h:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); pop("#em-st", {t2h+0.3:.2f});
draw("#em-tube", {tcw-0.5:.2f}, 0.4);
for (let i=0;i<6;i++) pop("#em-c"+i, {tcw-0.3:.2f}+i*0.05);
tl.to("#em-wave", {{opacity:1, duration:0.15}}, {tcw:.2f});
tl.fromTo("#em-wave", {{x:0}}, {{x:820, duration:2.6, ease:"power1.inOut"}}, {tsw-0.6:.2f});
for (let i=0;i<6;i++) tl.to("#em-c"+i, {{x:{820}-i*55+380-470, duration:2.6-0.3*i/6, ease:"power1.inOut"}}, {tsw-0.6:.2f}+0.25+i*0.28);
for (let i=0;i<6;i++) tl.to("#em-c"+i, {{opacity:0, duration:0.2}}, {tsw+1.9:.2f});
rise("#em-rng", {t1020-0.4:.2f}); draw("#em-bar", {t1020:.2f}, 0.5);
""")

# 7 REPEAT — timeline of returning waves
s = "repeat"; tstill = aw(s, "still don't"); tcb = aw(s, "comes back"); t12 = aw(s, "one to two")
humps = [(170, 330), (420, 610), (690, 880)]
hp = "".join(f'<path id="rp-h{i}" d="M{a},560 Q{(a+b)/2},380 {b},560" stroke="{C["blue"]}" stroke-width="8" fill="#BFE3F7" stroke-linecap="round"/>' for i, (a, b) in enumerate(humps))
scenes[s] = scene_file(s, f"""
#rp-title {{ top:150px; font-size:76px; }}
#rp-lab {{ position:absolute; left:0; right:0; top:680px; text-align:center; }}
#rp-fork {{ position:absolute; left:820px; top:250px; }}
""", f"""
  <div id="rp-title" class="h1">Still no snack?</div>
  <svg id="rp-fork" width="150" height="170" viewBox="0 0 75 85" data-layout-ignore>
    <path d="M25,5 L25,30 M37,5 L37,30 M49,5 L49,30 M25,30 Q37,42 49,30 M37,36 L37,80" {WS}/>
    <path id="rp-x" d="M5,10 L70,78 M70,10 L5,78" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore>
    <path id="rp-axis" d="M90,560 L1000,560 M980,545 L1000,560 L980,575" {WS}/>{hp}
    <path id="rp-ar1" d="M330,600 Q375,640 420,600" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path id="rp-ar2" d="M610,600 Q650,640 690,600" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>
  <div id="rp-lab"><span class="pill red" style="font-size:72px">every 1–2 hours</span></div>
""", f"""
rise("#rp-title", 0.0); pop("#rp-fork", {tstill:.2f}); draw("#rp-x", {tstill+0.5:.2f}, 0.3);
draw("#rp-axis", 0.2, 0.5);
tl.fromTo("#rp-h0", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:0.4, ease:"back.out(2)"}}, 0.5);
tl.fromTo("#rp-h1", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:0.4, ease:"back.out(2)"}}, {tcb:.2f});
tl.fromTo("#rp-h2", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:0.4, ease:"back.out(2)"}}, {tcb+0.6:.2f});
draw("#rp-ar1", {t12-0.2:.2f}, 0.3); draw("#rp-ar2", {t12+0.1:.2f}, 0.3);
pop("#rp-lab .pill", {t12:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 8 LOUD — cutaway of an empty, sloshing tube
s = "loud"; tsl = aw(s, "so loud"); tnm = aw(s, "nothing muffles"); tgf = aw(s, "gas and"); tdr = aw(s, "a drum")
bub = [(330, 560, 24), (470, 520, 18), (600, 570, 28), (740, 530, 20), (850, 560, 16)]
bb = "".join(f'<circle id="ld-b{i}" cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{C["blue"]}" stroke-width="4"/>' for i, (x, y, r) in enumerate(bub))
scenes[s] = scene_file(s, f"""
#ld-title {{ top:150px; font-size:74px; }}
#ld-blub {{ position:absolute; left:560px; top:262px; font-family:'Gochi Hand',cursive; font-size:90px; color:{C['blue']}; transform:rotate(-6deg); }}
#ld-drum {{ position:absolute; left:470px; top:790px; }}
""", f"""
  <div id="ld-title" class="h1">Nothing to <span class="hl">muffle</span> it</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="780" data-layout-ignore>
    <defs><clipPath id="ld-clip"><rect x="160" y="420" width="760" height="260" rx="120"/></clipPath></defs>
    <rect x="160" y="420" width="760" height="260" rx="120" fill="#FFF1F4"/>
    <g clip-path="url(#ld-clip)"><path id="ld-fluid" d="M100,620 Q200,590 300,620 T500,620 T700,620 T900,620 T1100,620 L1100,700 L100,700 Z" fill="#BFE3F7" stroke="{C['blue']}" stroke-width="4"/>{bb}</g>
    <rect x="160" y="420" width="760" height="260" rx="120" fill="none" stroke="{K}" stroke-width="6"/>
    <path id="ld-cut" d="M140,400 L940,400" stroke="{C['red']}" stroke-width="4" stroke-dasharray="14 10" fill="none"/>
    <path id="ld-s1" d="M950,480 Q990,550 950,620" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="ld-s2" d="M990,450 Q1050,550 990,650" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="ld-blub">blub… GLUG!</div>
  <div id="ld-drum"><span class="chip" style="background:#fff">= an empty drum</span></div>
""", f"""
rise("#ld-title", {tnm-0.3:.2f}); draw("#ld-cut", {tsl:.2f}, 0.5);
tl.fromTo("#ld-fluid", {{x:0}}, {{x:-200, duration:1.2, ease:"sine.inOut", yoyo:true, repeat:3}}, {tgf-0.4:.2f});
for (let i=0;i<5;i++) tl.fromTo("#ld-b"+i, {{y:60, opacity:0}}, {{y:-90, opacity:1, duration:1.6, ease:"power1.out", repeat:1}}, {tgf:.2f}+i*0.25);
pop("#ld-blub", {tgf+0.4:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
draw("#ld-s1", {tnm+0.2:.2f}, 0.25); draw("#ld-s2", {tnm+0.35:.2f}, 0.25);
pop("#ld-drum .chip", {tdr:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}});
""")

# 9 NAME — borborygmi
s = "name"; tbb = aw(s, "borborygmi"); tag = aw(s, "ancient Greek"); tru = aw(s, "a rumble")
word = "BORBORYGMI"
lt = "".join(f'<span id="nm-l{i}" style="display:inline-block;opacity:0">{ch}</span>' for i, ch in enumerate(word))
scenes[s] = scene_file(s, f"""
#nm-title {{ top:160px; font-size:70px; }}
#nm-tape {{ position:absolute; left:80px; top:360px; width:920px; height:170px; background:#fff; border:4px solid {K}; transform:rotate(-2deg); font-family:'Courier New',monospace; font-weight:bold; font-size:118px; line-height:170px; text-align:center; letter-spacing:4px; }}
#nm-gk {{ position:absolute; left:140px; top:590px; width:330px; height:74px; background:rgba(191,227,247,.85); transform:rotate(-6deg); font-size:46px; text-align:center; line-height:74px; }}
""", f"""
  <div id="nm-title" class="h1">Doctors call it…</div>
  <div id="nm-tape">{lt}</div>
  <div id="nm-gk">ancient Greek</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore>
    <path id="nm-sq" d="M520,760 Q550,700 580,760 T640,760 T700,760 T760,760 T820,760 T880,760 T940,760" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
""", f"""
rise("#nm-title", 0.0); rise("#nm-tape", {tbb-0.4:.2f});
for (let i=0;i<{len(word)};i++) tl.fromTo("#nm-l"+i, {{opacity:0, y:-20}}, {{opacity:1, y:0, duration:0.06}}, {tbb:.2f}+i*0.07);
pop("#nm-gk", {tag:.2f}, {{from:{{rotation:-16}}, to:{{rotation:-6}}}});
draw("#nm-sq", {tru:.2f}, 0.6);
""")

# 10 FULL — same stomach, two states
s = "full"; tfb = aw(s, "full belly"); tch = aw(s, "can't hear")
food = "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#C9A26B" stroke="{K}" stroke-width="3"/>' for x, y in [(90,120),(120,110),(150,125),(105,150),(140,155),(75,140),(165,145),(125,170)])
bars = lambda pid, n, col: "".join(f'<rect id="{pid}{i}" x="{i*34}" y="{100-i*22}" width="24" height="{20+i*22}" fill="{col}" stroke="{K}" stroke-width="3"/>' for i in range(n))
scenes[s] = scene_file(s, f"""
#fu-title {{ top:150px; font-size:72px; }}
#fu-a {{ position:absolute; left:110px; top:300px; text-align:center; width:380px; }}
#fu-b {{ position:absolute; left:590px; top:300px; text-align:center; width:380px; }}
#fu-ga {{ position:absolute; left:330px; top:300px; font-family:'Gochi Hand',cursive; font-size:48px; color:{C['pencil']}; }}
#fu-gb {{ position:absolute; left:800px; top:270px; font-family:'Gochi Hand',cursive; font-size:96px; color:{C['red']}; transform:rotate(8deg); }}
#fu-va {{ position:absolute; left:220px; top:700px; }}
#fu-vb {{ position:absolute; left:690px; top:700px; }}
""", f"""
  <div id="fu-title" class="h1">Full bellies rumble too</div>
  <div id="fu-a">{stomach('fu-sa', 300, inner=food)}<div style="font-size:52px">full</div></div>
  <div id="fu-b">{stomach('fu-sb', 300, fill="#fff")}<div style="font-size:52px">empty</div></div>
  <div id="fu-ga">grr…</div><div id="fu-gb">GRRR!</div>
  <svg id="fu-va" width="140" height="130" viewBox="0 0 140 130" data-layout-ignore>{bars('fu-va', 1, C['pencil'])}</svg>
  <svg id="fu-vb" width="180" height="130" viewBox="0 0 180 130" data-layout-ignore>{bars('fu-vb', 5, C['red'])}</svg>
""", f"""
rise("#fu-title", 0.0); pop("#fu-a", {tfb:.2f}); pop("#fu-ga", {tfb+0.5:.2f});
pop("#fu-b", {tch-0.4:.2f}); pop("#fu-gb", {tch:.2f}, {{from:{{rotation:30}}, to:{{rotation:8}}}});
rise("#fu-va", {tch:.2f}); rise("#fu-vb", {tch+0.2:.2f});
tl.fromTo("#fu-b", {{rotation:0}}, {{rotation:4, duration:0.07, yoyo:true, repeat:7}}, {tch+0.1:.2f});
""")

# 11 OUTRO
s = "outro"; tcl = aw(s, "doing the cleaning"); tem = aw(s, "empty echoey"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:170px; font-size:74px; }}
#ou-b {{ top:340px; font-size:74px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">cleaning wave</span> + empty tube</div>
  <div id="ou-b" class="h1">= <span class="red">GRRR!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tcl:.2f}); pop("#ou-b", {tem:.2f}, {{from:{{rotation:-10}}, to:{{}}}});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "why does"), SC["guess"]["start"] + 0.2)
point(g("guess", "hunger pain"), 2.6)
wave(g("intro", "I'm Max"))
point(g("squeeze", "it pushes"), 1.4)
point(g("beat", "three times"), 1.2)
wow(g("beat", "twelve times"), 1.2)
point(g("empty", "cleaning wave"), 1.4)
point(g("repeat", "one to two"), 1.2)
think(SC["loud"]["start"] + 0.05, g("loud", "with no"))
wow(g("name", "borborygmi"), 1.3)
point(g("full", "full belly"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("impact-bass-1.mp3", A("hook", "rumbles"), 0.45), ("pop.mp3", A("guess", "hunger pain"), 0.5), ("pop.mp3", A("guess", "air you"), 0.5),
        ("pop.mp3", A("guess", "your gut"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("beat", "drummer"), 0.6),
        ("ping.mp3", A("beat", "twelve times") + 0.6, 0.35), ("riser.mp3", A("empty", "cleaning wave") - 0.3, 0.3),
        ("pop.mp3", A("repeat", "one to two"), 0.5), ("impact-bass-2.mp3", A("loud", "a drum"), 0.4),
        ("click.mp3", A("name", "borborygmi"), 0.4), ("pop.mp3", A("full", "can't hear"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
