# MAX WISE ep03 — How many years of your life will you spend asleep? Executed inside engine/maxwise.py.
# === SCENES ===
import math
WSF = WS.replace('fill="none" ', '')
HB = f"background:repeating-linear-gradient(45deg, {C['blue']} 0 3px, transparent 3px 11px);"
def zzz(pid, x, y, c=None):
    c = c or C['blue']
    return "".join(f'<text id="{pid}{i}" x="{x+i*26}" y="{y-i*30}" font-family="Patrick Hand" font-weight="bold" font-size="{34+i*12}" fill="{c}">Z</text>' for i in range(3))
def ruler(X0, X1, Y):
    return "".join(f'<path d="M{X0+(X1-X0)*y/80:.1f},{Y-(26 if y%20==0 else 14)} L{X0+(X1-X0)*y/80:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                   (f'<text x="{X0+(X1-X0)*y/80:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 20 == 0 else "") for y in range(0, 81, 5))
def zzz_js(pid, t):
    return f'for (let i=0;i<3;i++) pop("#{pid}"+i, {t:.2f}+i*0.18);'

# 1 HOOK — sleepy question
s = "hook"; tsl = aw(s, "sleepy question"); thm = aw(s, "how many"); tas = aw(s, "asleep")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:84px; }}
#hk-bed {{ position:absolute; left:300px; top:560px; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many <span class="hl">years</span> of your life will you spend asleep?</div>
  <svg id="hk-bed" width="520" height="360" viewBox="0 0 260 180" style="overflow:visible" data-layout-ignore>
    <path d="M20,60 L20,160 M240,110 L240,160 M20,130 Q130,126 240,130" {WS}/>
    <path d="M22,112 Q130,106 238,112 L238,130 Q130,134 22,130 Z" fill="#BFE3F7" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
    <path d="M30,92 Q50,80 72,90 Q76,108 52,112 Q30,110 30,92 Z" fill="#fff" {WS.replace('fill="none" ', '')}/>
    <circle cx="96" cy="94" r="18" fill="#F6D2B0" stroke="{K}" stroke-width="4"/>
    <path d="M88,94 Q92,98 96,94 M100,94 Q104,98 108,94" stroke="{K}" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M100,106 Q160,92 236,110" {WS}/>
    {zzz('hk-z', 140, 70)}</svg>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#hk-bed", {tsl:.2f}); {zzz_js('hk-z', tsl+0.3)}
rise("#hk-q", {thm-0.05:.2f});
tl.fromTo("#hk-bed", {{rotation:0}}, {{rotation:2, duration:0.2, yoyo:true, repeat:3}}, {tas:.2f});
""")

# 2 GUESS — 5? 10? more than 20?
s = "guess"; tg = aw(s, "take a guess"); t5 = aw(s, "five years"); t10 = aw(s, "ten years"); t20 = aw(s, "more than twenty")
notes = [("a", "5 years?", -6, 110, C['hi']), ("b", "10 years?", 4, 400, "#BFE3F7"), ("c", "more than 20?", -3, 690, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:280px;height:250px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:62px;line-height:1.05">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t5:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t10:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t20:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's do")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's do the math!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 NIGHT — at least 7 hours, use 8
s = "night"; tex = aw(s, "health experts"); t7 = aw(s, "seven hours"); t8 = aw(s, "use eight")
scenes[s] = scene_file(s, f"""
#nt-title {{ top:150px; font-size:72px; }}
#nt-clock {{ position:absolute; left:110px; top:300px; }}
#nt-7 {{ position:absolute; left:560px; top:360px; width:440px; text-align:center; font-size:70px; }}
#nt-8 {{ position:absolute; left:560px; top:560px; width:440px; text-align:center; }}
#nt-8 span {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="nt-title" class="h1">Sleep per <span class="hl">night</span></div>
  <svg id="nt-clock" width="400" height="400" viewBox="0 0 200 200" data-layout-ignore>
    <path d="M100,12 Q186,14 188,100 Q186,188 100,190 Q14,188 12,100 Q14,14 100,12 Z" fill="#fff" {WS.replace('fill="none" ', '')}/>
    {''.join(f'<path d="M100,24 L100,{36 if i%3==0 else 32}" transform="rotate({i*30} 100 100)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(12))}
    <g id="nt-hh"><path d="M100,100 L100,58" stroke="{K}" stroke-width="7" stroke-linecap="round"/></g>
    <g id="nt-mh"><path d="M100,100 L100,36" stroke="{C['red']}" stroke-width="5" stroke-linecap="round"/></g>
    <circle cx="100" cy="100" r="6" fill="{K}"/></svg>
  <div id="nt-7" class="big">at least<br><span class="blue" style="font-size:110px">7 hours</span></div>
  <div id="nt-8"><span class="pill">use 8 h</span></div>
""", f"""
rise("#nt-title", 0.0); pop("#nt-clock", {tex:.2f});
tl.set("#nt-mh", {{rotation:0, svgOrigin:"100 100"}}, 0); tl.set("#nt-hh", {{rotation:-60, svgOrigin:"100 100"}}, 0);
tl.to("#nt-mh", {{rotation:360*7, duration:{t8-t7+0.3:.2f}, ease:"power1.inOut"}}, {t7:.2f});
tl.to("#nt-hh", {{rotation:180, duration:{t8-t7+0.3:.2f}, ease:"power1.inOut"}}, {t7:.2f});
pop("#nt-7", {t7:.2f}); pop("#nt-8 span", {t8:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 5 DAY — 8 / 24 = one third
s = "day"; te = aw(s, "eight hours"); t24 = aw(s, "twenty four"); t3 = aw(s, "one third")
cx, cy, r = 540, 560, 220
a0, a1 = -math.pi / 2, -math.pi / 2 + 2 * math.pi / 3
wedge = f"M{cx},{cy} L{cx+r*math.cos(a0):.1f},{cy+r*math.sin(a0):.1f} A{r},{r} 0 0 1 {cx+r*math.cos(a1):.1f},{cy+r*math.sin(a1):.1f} Z"
spokes = "".join(f'<path d="M{cx+(r-16)*math.cos(-math.pi/2+i*math.pi/12):.1f},{cy+(r-16)*math.sin(-math.pi/2+i*math.pi/12):.1f} L{cx+r*math.cos(-math.pi/2+i*math.pi/12):.1f},{cy+r*math.sin(-math.pi/2+i*math.pi/12):.1f}" stroke="{K}" stroke-width="3"/>' for i in range(24))
scenes[s] = scene_file(s, f"""
#dy-eq {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-size:90px; }}
#dy-lab {{ position:absolute; left:575px; top:440px; font-size:70px; color:#fff; }}
#dy-third {{ position:absolute; left:0; right:0; top:820px; text-align:center; }}
#dy-third span {{ font-size:84px; color:{C['blue']}; }}
""", f"""
  <div id="dy-eq" class="big"><span id="dy-a">8 h</span> <span id="dy-b">/ 24 h</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" data-layout-ignore>
    <circle id="dy-pie" cx="{cx}" cy="{cy}" r="{r}" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>
    <path id="dy-w" d="{wedge}" fill="{C['blue']}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    {spokes}</svg>
  <div id="dy-lab" class="big">8 h</div>
  <div id="dy-third"><span class="pill">= exactly 1/3</span></div>
""", f"""
pop("#dy-a", {te:.2f}); pop("#dy-pie", {te:.2f}); pop("#dy-b", {t24:.2f});
tl.fromTo("#dy-w", {{opacity:0, scale:0.3, svgOrigin:"{cx} {cy}"}}, {{opacity:1, scale:1, svgOrigin:"{cx} {cy}", duration:0.4, ease:"back.out(2)"}}, {t24+0.2:.2f});
pop("#dy-lab", {t24+0.4:.2f}); pop("#dy-third span", {t3:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 6 LIFE — one third of 80 years
s = "life"; t80 = aw(s, "eighty year"); t13 = aw(s, "one third"); t27 = aw(s, "almost twenty")
X0, X1, Y = 110, 970, 470
seg = (X1 - X0) / 3
scenes[s] = scene_file(s, f"""
#lf-title {{ top:150px; font-size:76px; }}
#lf-bar {{ position:absolute; left:{X0}px; top:{Y-70}px; width:{X1-X0}px; height:60px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-seg {{ position:absolute; left:0; top:0; height:100%; width:{seg:.1f}px; transform-origin:0 50%; {HB} }}
#lf-num {{ position:absolute; left:0; right:0; top:640px; text-align:center; }}
#lf-num .big {{ font-size:110px; color:{C['blue']}; }}
""", f"""
  <div id="lf-title" class="h1">A life: <span class="hl">80 years</span></div>
  <div id="lf-bar"><div id="lf-seg"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>{ruler(X0, X1, Y)}
    <path id="lf-br" d="M{X0},{Y-90} Q{X0+seg/2:.0f},{Y-130} {X0+seg:.0f},{Y-90}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <text id="lf-13" x="{X0+seg/2:.0f}" y="{Y-130}" text-anchor="middle" font-family="Gochi Hand" font-size="54" fill="{C['blue']}">1/3</text></svg>
  <div id="lf-num"><div class="big">almost 27 years</div><div style="font-size:52px;margin-top:10px">of sleep!</div></div>
""", f"""
rise("#lf-title", {t80-0.1:.2f}); rise("#lf-bar", {t80:.2f});
tl.fromTo("#lf-seg", {{scaleX:0}}, {{scaleX:1, duration:0.6, ease:"power2.out"}}, {t13:.2f});
draw("#lf-br", {t13+0.3:.2f}, 0.3); pop("#lf-13", {t13+0.4:.2f});
pop("#lf-num", {t27:.2f});
""")

# 7 SEVEN — 7 h still ~23 years
s = "seven"; ts7 = aw(s, "seven hours"); t23 = aw(s, "twenty three")
X0 = 300
w8, w7 = 18 * 80 / 3, 18 * 80 * 7 / 24
scenes[s] = scene_file(s, f"""
#sv-title {{ top:150px; font-size:72px; }}
.sv-row {{ position:absolute; left:100px; width:900px; height:110px; }}
.sv-lab {{ position:absolute; left:0; top:20px; font-family:'Gochi Hand',cursive; font-size:60px; }}
.sv-bar {{ position:absolute; left:{X0-100}px; top:20px; height:70px; border:4px solid {K}; {SKETCH} transform-origin:0 50%; {HB} }}
.sv-yr {{ position:absolute; top:26px; font-family:'Gochi Hand',cursive; font-size:54px; white-space:nowrap; }}
""", f"""
  <div id="sv-title" class="h1">Only <span class="hl">7 hours</span>?</div>
  <div id="sv-r8" class="sv-row" style="top:350px"><div class="sv-lab">8 h</div><div class="sv-bar" style="width:{w8:.0f}px"></div><div class="sv-yr blue" style="left:{X0-100+w8+20:.0f}px">almost 27</div></div>
  <div id="sv-r7" class="sv-row" style="top:520px"><div class="sv-lab red">7 h</div><div id="sv-b7" class="sv-bar" style="width:{w7:.0f}px"></div><div id="sv-y7" class="sv-yr red" style="left:{X0-100+w7+20:.0f}px">≈ 23 years</div></div>
""", f"""
rise("#sv-title", 0.0); rise("#sv-r8", 0.1); rise("#sv-r7", {ts7-0.2:.2f});
tl.fromTo("#sv-b7", {{scaleX:0}}, {{scaleX:1, duration:0.6, ease:"power2.out"}}, {ts7:.2f});
pop("#sv-y7", {t23:.2f});
""")

# 8 BABY — newborn 16 h, teens 9 h
s = "baby"; tch = aw(s, "sleep champions"); t16 = aw(s, "sixteen hours"); t9 = aw(s, "around nine")
scenes[s] = scene_file(s, f"""
#bb-title {{ top:150px; font-size:72px; }}
#bb-a {{ position:absolute; left:110px; top:300px; width:400px; height:520px; }}
#bb-b {{ position:absolute; left:570px; top:300px; width:400px; height:520px; }}
.bb-n {{ position:absolute; left:0; right:0; top:330px; text-align:center; font-family:'Gochi Hand',cursive; font-size:96px; }}
.bb-l {{ position:absolute; left:0; right:0; top:440px; text-align:center; font-size:46px; }}
""", f"""
  <div id="bb-title" class="h1">Sleep <span class="hl">champions</span></div>
  <div id="bb-a" class="card">
    <svg class="abs" style="left:70px;top:40px" width="260" height="260" viewBox="0 0 130 130" data-layout-ignore>
      <path d="M14,60 L14,120 M116,60 L116,120 M14,70 L116,70 M14,112 L116,112 M34,70 L34,112 M54,70 L54,112 M76,70 L76,112 M96,70 L96,112" {WS}/>
      <circle cx="56" cy="56" r="20" fill="#F6D2B0" stroke="{K}" stroke-width="4"/>
      <path d="M46,56 Q50,60 54,56 M58,56 Q62,60 66,56" stroke="{K}" stroke-width="3" fill="none" stroke-linecap="round"/>
      {zzz('bb-z', 82, 40)}</svg>
    <div class="bb-n red">≈ 16 h</div><div class="bb-l">newborn, per day</div></div>
  <div id="bb-b" class="card">
    <svg class="abs" style="left:70px;top:40px" width="260" height="260" viewBox="0 0 130 130" data-layout-ignore>
      <circle cx="65" cy="40" r="22" fill="#F6D2B0" stroke="{K}" stroke-width="4"/>
      <path d="M44,34 Q60,10 88,30" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
      <path d="M56,40 Q59,43 62,40 M68,40 Q71,43 74,40" stroke="{K}" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M40,120 Q42,72 65,66 Q88,72 90,120" fill="#BFE3F7" {WS.replace('fill="none" ', '')}/></svg>
    <div class="bb-n blue">≈ 9 h</div><div class="bb-l">teens</div></div>
""", f"""
rise("#bb-title", {tch-0.6:.2f}); pop("#bb-a", {t16-0.5:.2f}); {zzz_js('bb-z', t16)}
tl.fromTo("#bb-a .bb-n", {{scale:1}}, {{scale:1.12, duration:0.14, yoyo:true, repeat:1}}, {t16:.2f});
pop("#bb-b", {t9-0.3:.2f});
""")

# 9 SHORT — 1 in 3 adults under 7 hours
s = "short"; to3 = aw(s, "one in three"); tl7 = aw(s, "less than seven"); tti = aw(s, "tired people")
def person(pid, x, col, tired=False):
    eyes = (f'<path d="M-14,-118 L-4,-118 M4,-118 L14,-118" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' if tired else
            f'<circle cx="-9" cy="-118" r="4" fill="{K}"/><circle cx="9" cy="-118" r="4" fill="{K}"/>')
    mouth = f'<ellipse cx="0" cy="-100" rx="7" ry="9" fill="{K}"/>' if tired else f'<path d="M-8,-102 Q0,-95 8,-102" {WS}/>'
    return (f'<g id="{pid}"><g transform="translate({x},560)"><circle cx="0" cy="-115" r="34" fill="{col}" stroke="{K}" stroke-width="5"/>{eyes}{mouth}'
            f'<path d="M0,-80 L0,10 M0,-55 L-40,-15 M0,-55 L40,-15 M0,10 L-30,80 M0,10 L30,80" {WS}/></g></g>')
scenes[s] = scene_file(s, f"""
#sh-title {{ top:150px; font-size:72px; }}
#sh-lab {{ position:absolute; left:0; right:0; top:690px; text-align:center; }}
#sh-lab span {{ font-size:64px; color:{C['red']}; }}
""", f"""
  <div id="sh-title" class="h1"><span class="hl">1 in 3</span> US adults</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="680" data-layout-ignore>
    {person('sh-p1', 280, '#fff')}{person('sh-p2', 540, '#fff')}{person('sh-p3', 800, '#FFC9C2', True)}
    <path id="sh-ring" d="M720,330 Q800,300 880,330 Q920,460 880,650 Q800,672 720,650 Q690,460 720,330" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="sh-lab"><span class="pill">sleep less than 7 h</span></div>
""", f"""
rise("#sh-title", {to3-0.4:.2f});
pop("#sh-p1", {to3:.2f}); pop("#sh-p2", {to3+0.15:.2f}); pop("#sh-p3", {to3+0.3:.2f});
draw("#sh-ring", {tl7-0.2:.2f}, 0.4); pop("#sh-lab .pill", {tl7:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.fromTo("#sh-p3", {{rotation:0}}, {{rotation:-8, svgOrigin:"800 640", duration:0.3, yoyo:true, repeat:1}}, {tti:.2f});
""")

# 10 WHY — brain sorts memories, body repairs
s = "why"; tnw = aw(s, "isn't wasted"); tsm = aw(s, "sorts memories"); trp = aw(s, "repairs itself")
scenes[s] = scene_file(s, f"""
#wy-title {{ top:150px; font-size:72px; }}
#wy-brain {{ position:absolute; left:100px; top:300px; }}
#wy-files {{ position:absolute; left:140px; top:640px; }}
#wy-body {{ position:absolute; left:640px; top:300px; }}
#wy-l1 {{ position:absolute; left:80px; top:820px; width:440px; text-align:center; font-size:48px; }}
#wy-l2 {{ position:absolute; left:580px; top:820px; width:420px; text-align:center; font-size:48px; }}
""", f"""
  <div id="wy-title" class="h1">Not <span class="hl">wasted</span> time</div>
  <svg id="wy-brain" width="420" height="340" viewBox="0 0 210 170" data-layout-ignore>
    <path d="M40,120 Q10,110 18,80 Q8,50 40,40 Q50,12 86,20 Q106,4 130,18 Q166,10 176,42 Q206,54 194,88 Q204,120 172,128 Q166,154 134,148 Q112,166 88,150 Q58,160 40,120 Z" fill="#FFD6E0" {WS.replace('fill="none" ', '')}/>
    <path d="M60,60 Q80,50 90,70 Q100,90 120,76 M70,100 Q96,96 110,116 M130,48 Q150,40 160,60 M140,96 Q160,90 170,104" {WS}/></svg>
  <svg id="wy-files" width="340" height="170" viewBox="0 0 340 170" data-layout-ignore>
    {''.join(f'<g id="wy-f{i}"><path d="M{20+i*105},40 L{60+i*105},40 L{70+i*105},54 L{110+i*105},54 L{110+i*105},140 L{20+i*105},140 Z" fill="{["#FFE27A","#BFE3F7","#FFC9C2"][i]}" {WSF}/></g>' for i in range(3))}</svg>
  <svg id="wy-body" width="320" height="480" viewBox="0 0 160 240" data-layout-ignore>
    <circle cx="80" cy="40" r="28" fill="#F6D2B0" stroke="{K}" stroke-width="5"/>
    <path d="M80,68 L80,150 M80,90 L40,130 M80,90 L120,130 M80,150 L50,220 M80,150 L110,220" {WS}/>
    <g id="wy-band"><rect x="98" y="104" width="34" height="16" rx="5" fill="{C['hi']}" stroke="{K}" stroke-width="3" transform="rotate(42 115 112)"/></g>
    <g id="wy-spark"><path d="M140,70 L146,84 L160,90 L146,96 L140,110 L134,96 L120,90 L134,84 Z" fill="{C['hi']}" stroke="{K}" stroke-width="3"/></g></svg>
  <div id="wy-l1">brain: sorts memories</div>
  <div id="wy-l2">body: repairs itself</div>
""", f"""
rise("#wy-title", {tnw-0.5:.2f}); pop("#wy-brain", {tsm-0.6:.2f});
for (let i=0;i<3;i++) pop("#wy-f"+i, {tsm:.2f}+i*0.15);
rise("#wy-l1", {tsm+0.2:.2f}); pop("#wy-body", {trp-0.6:.2f}); pop("#wy-band", {trp:.2f}); pop("#wy-spark", {trp+0.2:.2f});
rise("#wy-l2", {trp+0.2:.2f});
""")

# 11 OUTRO
s = "outro"; tat = aw(s, "a third"); twl = aw(s, "time well"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">1/3</span> of your life in bed…</div>
  <div id="ou-b" class="h1">…and it's time well spent.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tat:.2f}); rise("#ou-b", {min(twl, tat+1.0):.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "five years"), 2.6)
wave(g("intro", "I'm Max"))
point(g("night", "seven hours"), 1.2)
point(g("day", "one third"), 1.2)
wow(g("life", "almost twenty"), 1.6)
point(g("seven", "twenty three"), 1.2)
wow(g("baby", "sixteen hours"), 1.2)
point(g("short", "one in three"), 1.4)
point(g("why", "sorts memories"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "asleep"), 0.35), ("pop.mp3", A("guess", "five years"), 0.5), ("pop.mp3", A("guess", "ten years"), 0.5),
        ("pop.mp3", A("guess", "more than twenty"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("night", "use eight"), 0.6),
        ("pop.mp3", A("day", "one third"), 0.55), ("impact-bass-1.mp3", A("life", "almost twenty"), 0.45),
        ("click.mp3", A("seven", "twenty three"), 0.45), ("pop.mp3", A("baby", "sixteen hours"), 0.5),
        ("pop.mp3", A("short", "less than seven"), 0.5), ("sparkle.mp3", A("why", "repairs itself"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
