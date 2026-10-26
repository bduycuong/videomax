# MAX WISE ep12 — How many ants are crawling on Earth right now?  Executed inside engine/maxwise.py.
# === SCENES ===
import random as _r
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; SOIL = "#E9D2B4"; LEAF = "#BFE3A8"

def ant(x, y, s=1.0, rot=0, col=None, aid=""):
    """doodle ant centred at x,y facing right; the outer <g> keeps the placement transform, the inner one is free for GSAP"""
    col = col or K
    ida = f' id="{aid}"' if aid else ""
    legs = "".join(f'<path d="M{dx},0 L{dx+lx},{sy*14}" stroke="{col}" stroke-width="3" stroke-linecap="round" fill="none"/>'
                   for dx, lx in [(-8, -8), (-4, 0), (0, 8)] for sy in (1, -1))
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><g{ida}>{legs}'
            f'<ellipse cx="-22" cy="0" rx="12" ry="9" fill="{col}"/><ellipse cx="-5" cy="0" rx="7" ry="5.5" fill="{col}"/>'
            f'<circle cx="9" cy="-1" r="7" fill="{col}"/>'
            f'<path d="M13,-6 Q18,-16 26,-15 M11,-7 Q12,-18 19,-21" stroke="{col}" stroke-width="2.5" fill="none" stroke-linecap="round"/></g></g>')

# 1 HOOK — question + a line of marching ants
s = "hook"; tan = aw(s, "how many"); tcr = aw(s, "crawling"); trn = aw(s, "right now")
row = "".join(ant(80 + k * 120, 760 + (12 if k % 2 else 0), 1.5, 0) for k in range(9))
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:84px; }}
#hk-qm {{ position:absolute; left:820px; top:520px; font-size:170px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many <span class="hl">ants</span> are on Earth<br>right now?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore>
    <path id="hk-trail" d="M20,800 Q300,786 540,800 T1060,796" stroke="{C['pencil']}" stroke-width="4" stroke-dasharray="10 12" fill="none"/>
    <g id="hk-ants" style="opacity:0">{row}</g></svg>
  <div id="hk-qm" class="big">?!</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {max(0.1, tan-0.3):.2f});
tl.to("#hk-ants", {{opacity:1, duration:0.2}}, {tcr-0.3:.2f});
tl.fromTo("#hk-ants", {{x:-260}}, {{x:120, duration:{SC['hook']['slot']-tcr+0.3:.2f}, ease:"none"}}, {tcr-0.3:.2f});
pop("#hk-qm", {trn:.2f}, {{from:{{rotation:20}}, to:{{rotation:6}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); tb = aw(s, "a billion"); tt = aw(s, "a trillion"); tw = aw(s, "way more")
notes = [("bil", "1 billion?", -6, 110, C['hi']), ("tril", "1 trillion?", 4, 405, SKY), ("more", "way<br>more?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:60px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  <div id="gs-sub" class="h2" style="top:720px">ants on Earth, right now</div>
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-bil", {tb:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); rise("#gs-sub", {tb+0.4:.2f});
pop("#gs-tril", {tt:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-more", {tw:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "count some")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count some ants!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tct:.2f});
""")

# 4 STUDY — 2022, ~500 survey pins on a doodle globe
s = "study"; t22 = aw(s, "twenty twenty two"); tsc = aw(s, "scientists"); t500 = aw(s, "five hundred"); twd = aw(s, "the world")
GX, GY, GR = 540, 530, 250
rnd = _r.Random(12); pins = []
while len(pins) < 500:
    px, py = rnd.uniform(-GR, GR), rnd.uniform(-GR, GR)
    if px * px + py * py < (GR - 14) ** 2: pins.append((GX + px, GY + py))
pin_g = "".join(f'<g id="st-g{k}" style="opacity:0">' + "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="{C["red"]}" stroke="{K}" stroke-width="1.5"/>' for x, y in pins[k*50:(k+1)*50]) + '</g>' for k in range(10))
land = (f'<path d="M370,420 Q420,350 500,380 Q560,330 600,400 Q560,460 500,450 Q430,500 370,420 Z M600,560 Q680,520 720,590 Q700,690 640,700 Q590,640 600,560 Z '
        f'M380,580 Q430,550 470,600 Q460,680 410,690 Q360,640 380,580 Z M640,330 Q700,320 720,360 Q690,380 650,370 Z" fill="{LEAF}" stroke="{K}" stroke-width="4"/>')
scenes[s] = scene_file(s, f"""
#st-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#st-lab {{ position:absolute; left:0; right:0; top:800px; text-align:center; font-size:64px; }}
""", f"""
  <div id="st-tag"><span class="chip" style="font-size:60px">2022</span></div>
  <svg id="st-globe" class="abs" style="left:0;top:0" width="{W}" height="800" data-layout-ignore>
    <circle cx="{GX}" cy="{GY}" r="{GR}" fill="{SKY}" stroke="{K}" stroke-width="6"/>{land}{pin_g}</svg>
  <div id="st-lab" class="big">nearly <span id="st-n" class="red">0</span> ant surveys</div>
""", f"""
pop("#st-tag .chip", {t22:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#st-globe", {tsc-0.2:.2f});
rise("#st-lab", {t500-0.3:.2f});
for (let k=0;k<10;k++) tl.to("#st-g"+k, {{opacity:1, duration:0.12}}, {t500:.2f}+k*0.12);
count("#st-n", 0, 500, {t500:.2f}, 1.2, fmtInt);
tl.fromTo("#st-globe", {{rotation:0}}, {{rotation:-4, duration:0.5, yoyo:true, repeat:1, transformOrigin:"540px 530px"}}, {twd:.2f});
""")

# 5 SCALE — a small patch, then forest / desert / city
s = "scale"; tpa = aw(s, "small patches"); tsu = aw(s, "scaled it"); tfo = aw(s, "forest"); tde = aw(s, "desert"); tci = aw(s, "city")
patch_ants = "".join(ant(40 + (k % 4) * 60, 60 + (k // 4) * 80, 1.0, rnd.uniform(-40, 40)) for k in range(12))
def tile(tid, x, inner, lab):
    return (f'<div id="{tid}" class="abs" style="left:{x}px;top:500px;width:270px;opacity:0">'
            f'<svg width="270" height="240" viewBox="0 0 270 240" data-layout-ignore><rect x="6" y="6" width="258" height="228" rx="18" fill="#fff" stroke="{K}" stroke-width="5"/>{inner}</svg>'
            f'<div style="text-align:center;font-family:Gochi Hand,cursive;font-size:56px">{lab}</div></div>')
forest = "".join(f'<path d="M{x},190 L{x},150" stroke="{K}" stroke-width="6"/><path d="M{x-38},160 L{x},60 L{x+38},160 Z" fill="{LEAF}" stroke="{K}" stroke-width="4"/>' for x in (70, 135, 200))
desert = (f'<circle cx="205" cy="65" r="30" fill="{C["hi"]}" stroke="{K}" stroke-width="4"/><path d="M20,200 Q90,160 150,190 Q210,170 250,200" fill="none" stroke="{K}" stroke-width="4"/>'
          f'<path d="M95,190 L95,95 Q95,80 110,80 Q125,80 125,95 L125,190 M95,140 L70,140 L70,115 M125,125 L150,125 L150,100" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round"/>')
city = "".join(f'<rect x="{x}" y="{y}" width="50" height="{200-y}" fill="{c}" stroke="{K}" stroke-width="4"/>' for x, y, c in [(30, 90, SKY), (90, 50, "#fff"), (150, 110, PINK), (205, 75, SKY)])
scenes[s] = scene_file(s, f"""
#sc-patch {{ position:absolute; left:390px; top:180px; width:300px; height:300px; border:5px dashed {K}; border-radius:14px; background:{SOIL}; }}
#sc-plab {{ position:absolute; left:700px; top:290px; font-size:48px; color:{C['blue']}; }}
""", f"""
  <div id="sc-patch"><svg width="290" height="290" data-layout-ignore>{patch_ants}</svg></div>
  <div id="sc-plab" class="big">counted!</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="520" data-layout-ignore>
    <path id="sc-a1" d="M470,440 Q330,450 250,500" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="sc-a2" d="M540,450 L540,500" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="sc-a3" d="M610,440 Q750,450 830,500" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  {tile('sc-t1', 105, forest, 'forest')}{tile('sc-t2', 405, desert, 'desert')}{tile('sc-t3', 705, city, 'city')}
""", f"""
pop("#sc-patch", {tpa-0.2:.2f}); rise("#sc-plab", {tpa+0.5:.2f});
tl.to("#sc-patch", {{scale:0.55, y:-40, duration:0.5, ease:"power3.inOut"}}, {tsu-0.1:.2f}); tl.to("#sc-plab", {{opacity:0, duration:0.2}}, {tsu-0.1:.2f});
draw("#sc-a1", {tfo-0.25:.2f}, 0.25); pop("#sc-t1", {tfo:.2f});
draw("#sc-a2", {tde-0.2:.2f}, 0.2); pop("#sc-t2", {tde:.2f});
draw("#sc-a3", {tci-0.25:.2f}, 0.25); pop("#sc-t3", {tci:.2f});
""")

# 6 TOTAL — 20,000,000,000,000,000 and its sixteen zeros
s = "total"; tans = aw(s, "their answer"); t20 = aw(s, "twenty quadrillion"); ttwo = aw(s, "a two"); t16 = aw(s, "sixteen zeros")
digits = "20,000,000,000,000,000"
dspans = ""; zi = 0
for ch in digits:
    if ch == "0": dspans += f'<span id="tt-z{zi}" class="tt-d">0</span>'; zi += 1
    elif ch == ",": dspans += '<span class="tt-d tt-c">,</span>'
    else: dspans += f'<span id="tt-two" class="tt-d">{ch}</span>'
scenes[s] = scene_file(s, f"""
#tt-q {{ top:160px; font-size:72px; }}
#tt-a {{ position:absolute; left:0; right:0; top:290px; text-align:center; font-size:96px; }}
#tt-num {{ position:absolute; left:40px; right:40px; top:470px; text-align:center; font-family:'Gochi Hand',cursive; font-size:84px; white-space:nowrap; }}
.tt-d {{ display:inline-block; opacity:0; }} .tt-c {{ color:{C['pencil']}; }}
#tt-pill {{ position:absolute; left:0; right:0; top:640px; text-align:center; }}
#tt-pill span {{ font-size:72px; color:{C['red']}; }}
""", f"""
  <div id="tt-q" class="h1">Their answer…</div>
  <div id="tt-a" class="big">≈ <span class="hl">20 quadrillion</span> ants</div>
  <div id="tt-num">{dspans}</div>
  <div id="tt-pill"><span class="pill">2 + 16 zeros!</span></div>
  <svg class="abs" style="left:0;top:780px" width="{W}" height="120" data-layout-ignore><g id="tt-row">{"".join(ant(440 + k*90, 60, 1.1) for k in range(7))}</g></svg>
""", f"""
rise("#tt-q", {tans:.2f}); pop("#tt-a", {t20:.2f});
tl.to("#tt-num .tt-d", {{opacity:1, duration:0.08, stagger:0.05}}, {t20+0.2:.2f});
tl.fromTo("#tt-row", {{x:-200, opacity:0}}, {{x:120, opacity:1, duration:{SC['total']['slot']-t20:.2f}, ease:"none"}}, {t20:.2f});
tl.to("#tt-two", {{color:"{C['blue']}", scale:1.3, duration:0.2}}, {ttwo:.2f});
for (let i=0;i<16;i++) tl.to("#tt-z"+i, {{color:"{C['red']}", duration:0.05}}, {t16-0.2:.2f}+i*0.05);
pop("#tt-pill span", {t16+0.4:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 7 SECONDS — one ant a second vs. a ruler of years
s = "seconds"; tct = aw(s, "counted one"); tes = aw(s, "every second"); tnd = aw(s, "would need"); t600 = aw(s, "six hundred million")
RX0, RX1, RY = 470, 990, 560
rticks = "".join(f'<path d="M{RX0+(RX1-RX0)*k/6:.0f},{RY-(24 if k%3==0 else 12)} L{RX0+(RX1-RX0)*k/6:.0f},{RY}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(7))
scenes[s] = scene_file(s, f"""
#se-watch {{ position:absolute; left:110px; top:250px; }}
#se-wlab {{ position:absolute; left:60px; top:600px; width:400px; text-align:center; font-size:52px; }}
#se-bar {{ position:absolute; left:{RX0}px; top:{RY-80}px; width:{RX1-RX0}px; height:56px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#se-fill {{ position:absolute; left:0; top:0; height:100%; width:100%; transform-origin:0 50%; }}
#se-cnt {{ position:absolute; left:440px; right:60px; top:640px; text-align:center; }}
#se-cnt .big {{ font-size:84px; }}
""", f"""
  <div id="se-title" class="h1" style="top:150px;font-size:70px">Count <span class="hl">1 ant</span> a second…</div>
  <svg id="se-watch" width="300" height="322" viewBox="0 0 200 215" data-layout-ignore>
    <path d="M86,10 L114,10 M100,10 L100,26" {WS}/>
    <path d="M100,28 Q182,30 184,118 Q182,206 100,208 Q18,206 16,118 Q18,30 100,28 Z" fill="#fff" {WSF}/>
    {''.join(f'<path d="M100,{44 if i%3==0 else 50} L100,54" transform="rotate({i*30} 100 118)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(12))}
    <g id="se-hand"><path d="M100,118 L100,52" stroke="{C['red']}" stroke-width="6" stroke-linecap="round"/></g>
    <circle cx="100" cy="118" r="6" fill="{K}"/></svg>
  <div id="se-wlab"><span class="red">1</span> ant = <span class="red">1</span> second</div>
  <div id="se-bar"><div id="se-fill" class="hatch-r"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>{rticks}</svg>
  <div id="se-rlab" class="abs" style="left:{RX0}px;top:{RY-140}px;font-size:46px;color:{C['muted']}">years of counting</div>
  <div id="se-cnt"><div class="big"><span id="se-n" class="red">0</span> years</div></div>
""", f"""
rise("#se-title", 0.0); pop("#se-watch", {tct:.2f}); tl.set("#se-hand", {{rotation:0, svgOrigin:"100 118"}}, 0);
tl.to("#se-hand", {{rotation:360*5, duration:{SC['seconds']['slot']-tct:.2f}, ease:"none"}}, {tct:.2f});
rise("#se-wlab", {tes:.2f});
rise("#se-bar", {tnd-0.3:.2f}); rise("#se-rlab", {tnd-0.3:.2f}); pop("#se-cnt", {tnd:.2f});
tl.fromTo("#se-fill", {{scaleX:0}}, {{scaleX:1, duration:{t600-tnd+0.9:.2f}, ease:"power2.in"}}, {tnd:.2f});
count("#se-n", 0, 600000000, {tnd:.2f}, {t600-tnd+0.9:.2f}, v => fmtInt(v) + (v >= 599999999 ? "+" : ""));
""")

# 8 SHARE — one person, one sack of ants
s = "share"; tsh = aw(s, "share them"); tep = aw(s, "every person"); t25 = aw(s, "two and a half")
def stick(x, y, c=K):
    return (f'<circle cx="{x}" cy="{y}" r="22" fill="#fff" stroke="{c}" stroke-width="5"/>'
            f'<path d="M{x},{y+22} L{x},{y+95} M{x},{y+45} L{x-32},{y+75} M{x},{y+45} L{x+32},{y+75} M{x},{y+95} L{x-26},{y+150} M{x},{y+95} L{x+26},{y+150}" stroke="{c}" stroke-width="5" fill="none" stroke-linecap="round"/>')
people = "".join(stick(150 + k * 130, 260) for k in range(7))
sack_ants = "".join(ant(rnd.uniform(-120, 120), rnd.uniform(-40, 40), 0.9, rnd.uniform(-180, 180)) for _ in range(9))
scenes[s] = scene_file(s, f"""
#sh-lab {{ position:absolute; left:200px; right:30px; top:820px; text-align:center; font-size:58px; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <g id="sh-people" style="opacity:0">{people}</g>
    <path id="sh-ring" d="M480,250 Q545,220 605,255 Q640,330 615,410 Q545,450 475,410 Q445,330 480,250 Z" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="sh-arr" d="M540,440 Q560,500 540,540" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <g id="sh-sack" style="opacity:0"><g transform="translate(0,-40)"><path d="M420,600 Q540,560 660,600 Q720,700 680,790 Q540,820 400,790 Q360,700 420,600 Z" fill="{SOIL}" {WSF}/>
      <path d="M470,600 Q540,640 610,600" {WS}/><g transform="translate(540,710)">{sack_ants}</g></g></g></svg>
  <div id="sh-lab" class="big">almost <span class="red">2.5 million</span> ants each!</div>
""", f"""
tl.to("#sh-people", {{opacity:1, duration:0.3}}, {tsh:.2f});
draw("#sh-ring", {tep:.2f}, 0.4); draw("#sh-arr", {tep+0.4:.2f}, 0.25);
pop("#sh-sack", {t25-0.4:.2f}); pop("#sh-lab", {t25:.2f});
""")

# 9 WEIGH — giant seesaw: ants vs. all wild birds and mammals
s = "weigh"; tgs = aw(s, "giant scale"); tow = aw(s, "outweigh"); tbd = aw(s, "wild bird"); tmm = aw(s, "wild mammal")
heap = "".join(ant(rnd.uniform(-90, 90), -rnd.uniform(0, 60) * (1 - 0) + 0, 0.8, rnd.uniform(-180, 180)) for _ in range(26))
bird = (f'<g id="wg-bird" style="opacity:0"><path d="M-70,-60 Q-40,-100 0,-80 Q30,-70 20,-40 Q-20,-20 -70,-60 Z" fill="{SKY}" {WSF}/>'
        f'<circle cx="8" cy="-76" r="5" fill="{K}"/><path d="M22,-72 L40,-66 L22,-62" fill="{C["hi"]}" stroke="{K}" stroke-width="3"/></g>')
deer = (f'<g id="wg-deer" style="opacity:0"><path d="M30,-50 Q70,-70 110,-50 Q115,-30 100,-25 Q60,-20 35,-28 Z" fill="{SOIL}" {WSF}/>'
        f'<path d="M45,-28 L42,0 M95,-28 L98,0 M60,-26 L60,0 M85,-26 L85,0 M108,-48 L120,-80" {WS}/><circle cx="124" cy="-86" r="10" fill="{SOIL}" stroke="{K}" stroke-width="4"/>'
        f'<path d="M120,-94 L112,-112 M128,-94 L136,-112" {WS}/></g>')
scenes[s] = scene_file(s, f"""
#wg-crk {{ position:absolute; left:640px; top:720px; font-size:88px; color:{C['red']}; }}
""", f"""
  <div id="wg-title" class="h1" style="top:150px;font-size:72px">A <span class="hl">giant</span> scale</div>
  <svg id="wg-svg" class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <path d="M540,640 L470,860 L610,860 Z" fill="#fff" {WSF}/>
    <g id="wg-beam">
      <path d="M110,640 Q540,630 970,640" stroke="{K}" stroke-width="12" fill="none" stroke-linecap="round"/>
      <path d="M140,640 L120,600 L300,600 L280,640" fill="#fff" {WSF}/><path d="M800,640 L780,600 L960,600 L940,640" fill="#fff" {WSF}/>
      <g id="wg-heap" style="opacity:0"><g transform="translate(210,560)">{heap}</g></g>
      <g transform="translate(870,600)">{bird}{deer}</g>
      <text id="wg-l1" x="210" y="440" text-anchor="middle" font-family="Gochi Hand" font-size="50" fill="{K}" opacity="0">all ants</text>
      <text id="wg-l2" x="860" y="440" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{K}" opacity="0">wild birds</text>
      <text id="wg-l3" x="860" y="490" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{K}" opacity="0">+ wild mammals</text>
    </g></svg>
  <div id="wg-crk" class="big">CREAK!</div>
""", f"""
rise("#wg-title", 0.0); pop("#wg-svg", {tgs-0.3:.2f}); tl.set("#wg-beam", {{rotation:7, svgOrigin:"540 640"}}, 0);
tl.to("#wg-heap", {{opacity:1, duration:0.3}}, {tgs:.2f});
tl.to("#wg-l1", {{opacity:1, duration:0.2}}, {tgs+0.2:.2f});
tl.to("#wg-beam", {{rotation:-9, duration:0.7, ease:"back.out(1.6)"}}, {tow:.2f});
pop("#wg-crk", {tow+0.2:.2f}, {{from:{{rotation:16}}, to:{{rotation:6}}}});
tl.to("#wg-bird", {{opacity:1, duration:0.2}}, {tbd:.2f}); tl.to("#wg-l2", {{opacity:1, duration:0.2}}, {tbd:.2f});
tl.to("#wg-deer", {{opacity:1, duration:0.2}}, {tmm:.2f}); tl.to("#wg-l3", {{opacity:1, duration:0.2}}, {tmm:.2f});
tl.fromTo("#wg-beam", {{rotation:-9}}, {{rotation:-11, duration:0.12, yoyo:true, repeat:3}}, {tmm+0.4:.2f});
""")

# 10 LOW — cutaway: ants hiding in trees and underground
s = "low"; tle = aw(s, "low estimate"); ttr = aw(s, "in trees"); tug = aw(s, "deep underground"); thc = aw(s, "hard to count")
tunnels = (f'<path d="M180,560 Q260,620 230,700 Q200,740 300,780 M560,560 Q600,640 700,660 Q820,690 860,770 M300,780 Q420,810 520,770" '
           f'stroke="#B08A5E" stroke-width="34" fill="none" stroke-linecap="round"/>')
ug_ants = "".join(f'<g class="lw-ua" style="opacity:0">{ant(x, y, 1.0, r)}<text x="{x+22}" y="{y-16}" font-family="Gochi Hand" font-size="40" fill="{C["red"]}">?</text></g>'
                  for x, y, r in [(232, 700, 80), (700, 662, 10), (420, 796, 170), (850, 762, 70)])
tr_ants = "".join(f'<g class="lw-ta" style="opacity:0">{ant(x, y, 0.9, r)}<text x="{x+18}" y="{y-14}" font-family="Gochi Hand" font-size="36" fill="{C["red"]}">?</text></g>'
                  for x, y, r in [(740, 330, -20), (880, 300, 15), (800, 420, 90)])
scenes[s] = scene_file(s, f"""
#lw-stamp {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#lw-stamp span {{ font-size:66px; color:{C['red']}; }}
#lw-l1 {{ position:absolute; left:120px; top:330px; font-size:52px; color:{C['blue']}; }}
#lw-l2 {{ position:absolute; left:560px; top:775px; font-size:52px; color:{C['blue']}; }}
""", f"""
  <div id="lw-stamp"><span class="pill">a LOW estimate</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <rect x="70" y="540" width="940" height="300" rx="18" fill="{SOIL}" stroke="{K}" stroke-width="5"/>
    <path d="M70,540 Q300,528 540,542 T1010,538" stroke="{K}" stroke-width="6" fill="none"/>
    <g id="lw-tun" style="opacity:0">{tunnels}</g>
    <g id="lw-tree" style="opacity:0"><path d="M800,540 L800,400" stroke="#8A6440" stroke-width="26" stroke-linecap="round"/>
      <path d="M690,380 Q680,280 760,260 Q800,200 870,240 Q950,240 950,330 Q960,420 870,420 Q820,450 760,420 Q690,430 690,380 Z" fill="{LEAF}" {WSF}/></g>
    {tr_ants}{ug_ants}</svg>
  <div id="lw-l1" class="big">up in trees</div>
  <div id="lw-l2" class="big">deep underground</div>
""", f"""
pop("#lw-stamp span", {tle:.2f}, {{from:{{rotation:-16, scale:1.8}}, to:{{rotation:-4}}}});
tl.to("#lw-tree", {{opacity:1, duration:0.3}}, {ttr-0.6:.2f}); rise("#lw-l1", {ttr:.2f});
tl.to(".lw-ta", {{opacity:1, duration:0.15, stagger:0.15}}, {ttr+0.1:.2f});
tl.to("#lw-tun", {{opacity:1, duration:0.3}}, {tug-0.4:.2f}); rise("#lw-l2", {tug:.2f});
tl.to(".lw-ua", {{opacity:1, duration:0.15, stagger:0.15}}, {tug+0.1:.2f});
tl.fromTo(".lw-ua text, .lw-ta text", {{y:0}}, {{y:-8, duration:0.15, yoyo:true, repeat:3}}, {thc:.2f});
""")

# 11 OUTRO
s = "outro"; t20 = aw(s, "twenty quadrillion"); tyr = aw(s, "are yours"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:80px; }}
#ou-b {{ top:300px; font-size:64px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">20 quadrillion</span> ants…</div>
  <div id="ou-b" class="h1">…almost <span class="red">2.5 million</span> are yours!</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {t20:.2f}); rise("#ou-b", {tyr-0.6:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "quick question"), SC["guess"]["start"] + 0.2)
point(g("guess", "a billion"), 2.4)
wave(g("intro", "I'm Max"))
point(g("study", "five hundred"), 1.2)
point(g("scale", "forest"), 1.4)
wow(g("total", "twenty quadrillion"), 1.4)
think(g("seconds", "if you"), g("seconds", "would need"))
wow(g("seconds", "six hundred million"), 1.4)
point(g("share", "every person"), 1.4)
wow(g("weigh", "outweigh"), 1.4)
think(g("low", "hard to count") - 0.6, g("low", "hard to count") + 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "how many"), 0.35), ("pop.mp3", A("guess", "a billion"), 0.5), ("pop.mp3", A("guess", "a trillion"), 0.5),
        ("pop.mp3", A("guess", "way more"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("study", "five hundred"), 0.5),
        ("pop.mp3", A("scale", "forest"), 0.45), ("pop.mp3", A("scale", "city"), 0.45),
        ("impact-bass-1.mp3", A("total", "twenty quadrillion"), 0.45), ("click.mp3", A("seconds", "every second"), 0.4),
        ("pop.mp3", A("share", "two and a half"), 0.5), ("impact-bass-2.mp3", A("weigh", "outweigh") + 0.2, 0.4),
        ("click-soft.mp3", A("low", "low estimate"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
