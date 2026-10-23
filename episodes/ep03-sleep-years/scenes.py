# MAX WISE ep03 — How many years of your life will you spend asleep?
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
NIGHT = "#3B4A8C"
def moon_svg(pid, w):
    return (f'<svg id="{pid}" viewBox="0 0 120 120" width="{w}" height="{w}" style="overflow:visible" data-layout-ignore>'
            f'<path d="M78,12 Q30,18 26,64 Q30,110 80,112 Q50,96 48,62 Q50,28 78,12 Z" fill="{C["hi"]}" {WSF}/></svg>')
def zzz(pid, x, y, s=1.0):
    return "".join(f'<div id="{pid}{i}" class="abs" style="left:{x+i*50*s:.0f}px;top:{y-i*55*s:.0f}px;font-family:Gochi Hand,cursive;font-size:{int((60+i*20)*s)}px;color:{C["blue"]};opacity:0">Z</div>' for i in range(3))
ZJS = lambda pid, t: f'for (let i=0;i<3;i++) pop("#{pid}"+i, {t:.2f}+i*0.25);'
def life_bar(pid, Y, frac, color):
    X0, X1 = 110, 970
    ticks = "".join(f'<path d="M{X0+(X1-X0)*y/80:.1f},{Y-(26 if y%20==0 else 14)} L{X0+(X1-X0)*y/80:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                    (f'<text x="{X0+(X1-X0)*y/80:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 20 == 0 else "") for y in range(0, 81, 5))
    html = (f'<div id="{pid}-bar" class="abs" style="left:{X0}px;top:{Y-70}px;width:{X1-X0}px;height:60px;border:4px solid {K};{SKETCH}background:#fff;overflow:hidden">'
            f'<div id="{pid}-seg" class="abs" style="left:0;top:0;height:100%;width:{(X1-X0)*frac:.1f}px;background:{color};transform-origin:0 50%"></div></div>'
            f'<svg class="abs" style="left:0;top:0" width="{W}" height="{Y+70}" data-layout-ignore>{ticks}</svg>')
    return html

# 1 HOOK
s = "hook"; tq = aw(s, "how many"); tas = aw(s, "spend asleep")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:86px; }}
#hk-moon {{ position:absolute; left:420px; top:600px; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many <span class="hl">years</span> of your life will you spend asleep?</div>
  <div id="hk-moon">{moon_svg('hk-m', 260)}</div>
  {zzz('hk-z', 700, 760)}
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tq-0.05:.2f}); pop("#hk-moon", {tas-0.4:.2f}, {{from:{{rotation:-30}}, to:{{rotation:0}}}});
{ZJS('hk-z', tas+0.1)}
tl.fromTo("#hk-moon", {{rotation:0}}, {{rotation:-8, duration:0.8, yoyo:true, repeat:1, ease:"sine.inOut"}}, {tas+0.5:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t5 = aw(s, "five years"); t15 = aw(s, "fifteen years"); tm = aw(s, "even more")
notes = [("y5", "5<br>years?", -6, 110, C['hi']), ("y15", "15<br>years?", 4, 405, "#BFE3F7"), ("more", "Even<br>more?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:62px;line-height:1.05">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-y5", {t5:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-y15", {t15:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-more", {tm:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
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

# 4 NEED — at least 7 hours
s = "need"; tex = aw(s, "sleep experts"); t7 = aw(s, "seven hours")
scenes[s] = scene_file(s, f"""
#nd-bed {{ position:absolute; left:250px; top:190px; }}
#nd-num {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#nd-num .big {{ font-size:120px; }}
""", f"""
  <svg id="nd-bed" width="580" height="340" viewBox="0 0 290 170" style="overflow:visible" data-layout-ignore>
    <path d="M14,40 L14,160 M276,96 L276,160 M14,124 L276,124" {WS}/>
    <path d="M14,96 Q140,90 276,96 L276,124 L14,124 Z" fill="#BFE3F7" {WSF}/>
    <path d="M26,74 Q50,62 80,72 Q86,88 74,96 Q46,100 26,94 Z" fill="#fff" {WSF}/>
    <path d="M90,96 Q150,64 250,90 L276,96 Q160,104 90,96 Z" fill="{NIGHT}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>
    <circle cx="66" cy="70" r="16" fill="#FFE2C4" stroke="{K}" stroke-width="4"/><path d="M58,70 Q62,74 66,70 M70,70 Q74,74 78,70" stroke="{K}" stroke-width="3" fill="none" stroke-linecap="round"/></svg>
  {zzz('nd-z', 700, 230, 0.8)}
  <div id="nd-num"><div class="big">at least <span class="red">7</span> hours</div><div style="font-size:56px;margin-top:10px">every night, for adults</div></div>
""", f"""
pop("#nd-bed", {max(tex-0.2,0):.2f}); {ZJS('nd-z', tex+0.4)}
pop("#nd-num", {t7-0.5:.2f});
tl.fromTo("#nd-num .red", {{scale:1}}, {{scale:1.3, duration:0.15, yoyo:true, repeat:1}}, {t7:.2f});
""")

# 5 DAY — 8 of 24 = one third
s = "day"; t8 = aw(s, "eight hours"); t24 = aw(s, "twenty four hours"); t3 = aw(s, "one third")
scenes[s] = scene_file(s, f"""
#dy-pie {{ position:absolute; left:110px; top:220px; }}
#dy-rows {{ position:absolute; left:560px; top:250px; width:440px; }}
#dy-rows div {{ font-family:'Gochi Hand',cursive; font-size:74px; line-height:1.35; }}
#dy-ans {{ position:absolute; left:0; right:0; top:700px; text-align:center; }}
#dy-ans span {{ font-size:92px; color:{C['blue']}; }}
""", f"""
  <div id="dy-title" class="h1" style="top:140px;font-size:66px">One day</div>
  <svg id="dy-pie" width="400" height="400" viewBox="0 0 300 300" data-layout-ignore>
    <circle cx="150" cy="150" r="130" fill="#fff" stroke="{K}" stroke-width="6"/>
    <path id="dy-wedge" d="M150,150 L150,20 A130,130 0 0 1 262.6,215 Z" fill="{NIGHT}" stroke="{K}" stroke-width="5" stroke-linejoin="round" style="opacity:0"/>
    {''.join(f'<path d="M150,24 L150,{36 if i%6 else 44}" transform="rotate({i*15} 150 150)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(24))}
    <circle cx="150" cy="150" r="6" fill="{K}"/></svg>
  <div id="dy-rows"><div id="dy-r1">sleep: <span class="blue">8 h</span></div><div id="dy-r2">day: 24 h</div><div id="dy-r3">8 ÷ 24 = <span class="red">1/3</span></div></div>
  <div id="dy-ans"><span class="pill">exactly one third!</span></div>
""", f"""
rise("#dy-title", 0.0); pop("#dy-pie", 0.1);
tl.fromTo("#dy-wedge", {{opacity:0, scale:0.2, svgOrigin:"150 150"}}, {{opacity:1, scale:1, duration:0.4, ease:"back.out(1.8)"}}, {t8:.2f});
rise("#dy-r1", {t8:.2f}); rise("#dy-r2", {t24:.2f}); rise("#dy-r3", {t3-0.6:.2f});
pop("#dy-ans span", {t3:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
""")

# 6 LIFE — 80 years, one third = ~27 years
s = "life"; t80 = aw(s, "eighty years"); t13 = aw(s, "one third"); t27 = aw(s, "twenty seven")
scenes[s] = scene_file(s, f"""
#lf-lab {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#lf-lab .big {{ font-size:120px; color:{NIGHT}; }}
""", f"""
  <div id="lf-title" class="h1" style="top:160px;font-size:76px">A whole life: <span class="hl">80 years</span></div>
  {life_bar('lf', 440, 1/3, NIGHT)}
  <div id="lf-lab"><div class="big">≈ 27 years</div><div style="font-size:60px;margin-top:10px"><span class="hl">fast asleep!</span></div></div>
""", f"""
rise("#lf-title", {max(t80-0.6,0):.2f}); rise("#lf-bar", 0.1);
tl.fromTo("#lf-seg", {{scaleX:0}}, {{scaleX:1, duration:0.7, ease:"power2.out"}}, {t13:.2f});
pop("#lf-lab", {t27:.2f}, {{from:{{scale:0.3}}, to:{{duration:0.45}}}});
""")

# 7 SEVEN — 7 h -> ~23 years
s = "seven"; t7 = aw(s, "seven hours"); t23 = aw(s, "twenty three")
scenes[s] = scene_file(s, f"""
#sv-lab {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#sv-lab .big {{ font-size:120px; color:{NIGHT}; }}
""", f"""
  <div id="sv-title" class="h1" style="top:160px;font-size:76px">Only <span class="hl">7 hours</span> a night?</div>
  {life_bar('sv', 440, 7/24, NIGHT)}
  <div id="sv-lab"><div class="big">still ≈ 23 years</div></div>
""", f"""
rise("#sv-title", {max(t7-0.4,0):.2f}); rise("#sv-bar", 0.1);
tl.fromTo("#sv-seg", {{scaleX:0}}, {{scaleX:1, duration:0.7, ease:"power2.out"}}, {t7+0.3:.2f});
pop("#sv-lab", {t23:.2f});
""")

# 8 BABY — newborns 14 to 17 hours
s = "baby"; tnb = aw(s, "newborn babies"); t14 = aw(s, "fourteen to")
scenes[s] = scene_file(s, f"""
#bb-baby {{ position:absolute; left:330px; top:170px; }}
#bb-num {{ position:absolute; left:0; right:0; top:610px; text-align:center; }}
#bb-num .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <svg id="bb-baby" width="420" height="360" viewBox="0 0 210 180" style="overflow:visible" data-layout-ignore>
    <path d="M30,120 Q30,60 105,56 Q180,60 180,120 Q176,170 105,172 Q34,170 30,120 Z" fill="#FFC9C2" {WSF}/>
    <circle cx="105" cy="78" r="44" fill="#FFE2C4" stroke="{K}" stroke-width="5"/>
    <path d="M86,80 Q92,86 98,80 M112,80 Q118,86 124,80 M98,100 Q105,104 112,100" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path d="M100,36 Q108,24 116,34" {WS}/>
    <path d="M40,130 Q105,112 170,130" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".5"/></svg>
  {zzz('bb-z', 760, 260, 0.8)}
  <div id="bb-num"><div style="font-size:60px">newborns sleep</div><div class="big">14–17 hours</div><div style="font-size:60px">a day!</div></div>
""", f"""
pop("#bb-baby", {max(tnb-0.2,0):.2f}); {ZJS('bb-z', tnb+0.5)}
pop("#bb-num", {t14:.2f});
""")

# 9 SHORT — more than 1 in 3 adults sleep < 7 h
s = "short"; t13 = aw(s, "one in three"); tl7 = aw(s, "less than seven"); tti = aw(s, "tired people")
def person(pid, x, col, tired=False):
    eyes = (f'<path d="M-14,-6 L-4,-6 M4,-6 L14,-6" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' if tired else
            f'<circle cx="-9" cy="-6" r="4" fill="{K}"/><circle cx="9" cy="-6" r="4" fill="{K}"/>')
    mouth = f'<path d="M-8,12 Q0,6 8,12" {WS}/>' if tired else f'<path d="M-9,8 Q0,16 9,8" {WS}/>'
    return (f'<g id="{pid}" transform="translate({x},0)"><circle cx="0" cy="0" r="40" fill="{col}" {WSF}/>{eyes}{mouth}'
            f'<path d="M0,40 L0,140 M0,70 L-40,110 M0,70 L40,110 M0,140 L-30,210 M0,140 L30,210" {WS}/></g>')
scenes[s] = scene_file(s, f"""
#sh-ppl {{ position:absolute; left:140px; top:330px; }}
#sh-lab {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#sh-lab .big {{ font-size:84px; }}
#sh-sub {{ position:absolute; left:0; right:0; top:640px; text-align:center; font-size:60px; }}
""", f"""
  <div id="sh-lab"><div class="big">more than <span class="red">1 in 3</span> US adults</div></div>
  <svg id="sh-ppl" width="800" height="300" viewBox="-60 -60 800 300" style="overflow:visible" data-layout-ignore>
    {person('sh-p0', 60, '#FFE2C4')}{person('sh-p1', 340, '#FFE2C4')}{person('sh-p2', 620, '#FFC9C2', True)}</svg>
  {zzz('sh-z', 890, 360, 0.7)}
  <div id="sh-sub">sleep <span class="hl">less than 7 hours</span></div>
""", f"""
rise("#sh-lab", {t13-0.4:.2f});
for (let i=0;i<3;i++) pop("#sh-p"+i, {t13-0.3:.2f}+i*0.15);
rise("#sh-sub", {tl7:.2f}); {ZJS('sh-z', tti)}
""")

# 10 WHY — brain sorts memories, body repairs
s = "why"; tw = aw(s, "isn't wasted"); tbr = aw(s, "your brain"); tmem = aw(s, "your memories"); trep = aw(s, "repairs itself")
cards = "".join(f'<rect id="wy-c{i}" x="{150+i*40}" y="{40+i*8}" width="60" height="44" rx="4" fill="{c}" stroke="{K}" stroke-width="4" transform="rotate({r} {180+i*40} {62+i*8})"/>' for i, (c, r) in enumerate([(C['hi'], -10), ("#BFE3F7", 4), ("#FFC9C2", 12)]))
scenes[s] = scene_file(s, f"""
#wy-brain {{ position:absolute; left:90px; top:300px; }}
#wy-wr {{ position:absolute; left:660px; top:330px; }}
#wy-l1 {{ position:absolute; left:80px; top:690px; width:480px; text-align:center; font-size:56px; }}
#wy-l2 {{ position:absolute; left:580px; top:690px; width:420px; text-align:center; font-size:56px; }}
""", f"""
  <div id="wy-title" class="h1" style="top:150px;font-size:76px">Sleep is <span class="hl">not wasted</span></div>
  <svg id="wy-brain" width="480" height="360" viewBox="0 0 280 210" style="overflow:visible" data-layout-ignore>
    <path d="M40,150 Q10,140 18,100 Q8,64 40,52 Q50,20 90,28 Q110,8 136,24 Q172,14 182,50 Q212,62 200,100 Q210,140 176,150 Q170,180 136,174 Q112,194 88,178 Q56,190 40,150 Z" fill="#FFD6E0" {WSF}/>
    <path d="M60,80 Q80,68 92,90 Q102,112 124,96 M70,124 Q98,118 112,140 M134,62 Q156,52 166,74 M144,116 Q166,110 176,126" {WS}/>
    {cards}</svg>
  <svg id="wy-wr" width="300" height="300" viewBox="0 0 150 150" data-layout-ignore>
    <g id="wy-wrench"><path d="M40,110 L96,54" stroke="{K}" stroke-width="16" stroke-linecap="round"/>
    <path d="M90,30 Q110,16 128,30 L112,46 L120,58 L136,46 Q148,64 132,82 Q116,92 98,78" fill="#fff" stroke="{K}" stroke-width="5" stroke-linejoin="round"/></g></svg>
  <div id="wy-l1"><span class="blue">brain</span>: sorts memories</div>
  <div id="wy-l2"><span class="red">body</span>: repairs</div>
""", f"""
rise("#wy-title", {tw-0.6:.2f}); pop("#wy-brain", {tbr:.2f});
for (let i=0;i<3;i++) tl.fromTo("#wy-c"+i, {{opacity:0, y:-50}}, {{opacity:1, y:0, duration:0.3, ease:"back.out(2)"}}, {tmem:.2f}+i*0.18);
rise("#wy-l1", {tmem:.2f}); pop("#wy-wr", {trep-0.3:.2f}); tl.set("#wy-wrench", {{rotation:0, svgOrigin:"75 80"}}, 0);
tl.to("#wy-wrench", {{rotation:-25, duration:0.2, yoyo:true, repeat:3, ease:"sine.inOut"}}, {trep:.2f}); rise("#wy-l2", {trep:.2f});
""")

# 11 OUTRO
s = "outro"; ta = aw(s, "twenty seven"); tbr = aw(s, "awake years"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">27 years</span> of sleep</div>
  <div id="ou-b" class="h1">…that keep your awake years bright.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {ta:.2f}); rise("#ou-b", {ta+0.8:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "five years"), 2.8)
wave(g("intro", "I'm Max"))
point(g("need", "seven hours"), 1.2)
point(g("day", "one third"), 1.2)
wow(g("life", "twenty seven"), 1.6)
point(g("seven", "twenty three"), 1.2)
wow(g("baby", "fourteen to"), 1.3)
think(SC["short"]["start"] + 0.05, g("short", "less than seven"))
point(g("why", "your brain"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "spend asleep"), 0.35), ("pop.mp3", A("guess", "five years"), 0.5), ("pop.mp3", A("guess", "fifteen years"), 0.5),
        ("pop.mp3", A("guess", "even more"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("need", "seven hours"), 0.6),
        ("click.mp3", A("day", "eight hours"), 0.45), ("pop.mp3", A("day", "one third"), 0.55),
        ("impact-bass-1.mp3", A("life", "twenty seven"), 0.45), ("pop.mp3", A("baby", "fourteen to"), 0.5),
        ("click-soft.mp3", A("why", "repairs itself"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
