# MAX WISE ep10 — How many years of your life will you spend staring at your phone?  Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"

def phone_svg(pid, w=300, screen=""):
    """doodle phone, viewBox 160x280; screen area x36-124, y30-236"""
    return f'''<svg id="{pid}" width="{w}" height="{w*1.75:.0f}" viewBox="0 0 160 280" data-layout-ignore>
    <defs><clipPath id="{pid}-clip"><path d="M36,30 Q80,27 124,31 L122,236 Q80,239 38,236 Z"/></clipPath></defs>
    <path d="M24,8 Q80,4 136,9 Q150,140 135,272 Q80,276 25,271 Q10,140 24,8 Z" fill="#fff" {WSF}/>
    <path d="M36,30 Q80,27 124,31 L122,236 Q80,239 38,236 Z" fill="#DDEFF7" stroke="{K}" stroke-width="3"/>
    <g clip-path="url(#{pid}-clip)">{screen}</g>
    <circle cx="80" cy="254" r="9" fill="none" stroke="{K}" stroke-width="3"/></svg>'''

# 1 HOOK — the question, phone with endless feed
s = "hook"; tph = aw(s, "holding your phone"); tst = aw(s, "staring"); tyr = aw(s, "how many years")
feed = "".join(f'<rect x="46" y="{40+k*58}" width="68" height="30" rx="5" fill="{[C["hi"], PINK, SKY][k%3]}" stroke="{K}" stroke-width="2"/>'
               f'<path d="M46,{80+k*58} L{100 - (k*13)%30},{80+k*58}" stroke="{C["pencil"]}" stroke-width="4" stroke-linecap="round"/>' for k in range(14))
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:80px; }}
#hk-ph {{ position:absolute; left:400px; top:520px; }}
#hk-eyes {{ position:absolute; left:430px; top:560px; opacity:0; }}
#hk-qm {{ position:absolute; left:760px; top:600px; font-size:160px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many <span class="hl">years</span> of your life<br>on your phone?</div>
  <div id="hk-ph">{phone_svg('hk-p', 250, f'<g id="hk-feed">{feed}</g>')}</div>
  <svg id="hk-eyes" width="190" height="80" viewBox="0 0 190 80" data-layout-ignore>
    <ellipse cx="50" cy="40" rx="38" ry="28" fill="#fff" stroke="{K}" stroke-width="5"/><circle cx="56" cy="44" r="13" fill="{K}"/>
    <ellipse cx="140" cy="40" rx="38" ry="28" fill="#fff" stroke="{K}" stroke-width="5"/><circle cx="146" cy="44" r="13" fill="{K}"/></svg>
  <div id="hk-qm" class="big">?!</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", 0.1); pop("#hk-ph", {tph:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
tl.fromTo("#hk-feed", {{y:0}}, {{y:-560, duration:7, ease:"none"}}, {tph+0.2:.2f});
pop("#hk-eyes", {tst:.2f});
pop("#hk-qm", {tyr:.2f}, {{from:{{rotation:20}}, to:{{rotation:6}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "one year"); t5 = aw(s, "five years"); t10 = aw(s, "more than ten")
notes = [("one", "1 year?", -6, 110, C['hi']), ("five", "5 years?", 4, 405, SKY), ("ten", "10+<br>years?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:64px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  <div id="gs-sub" class="h2" style="top:710px">years of your life, staring at a phone</div>
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-one", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); rise("#gs-sub", {t1+0.4:.2f});
pop("#gs-five", {t5:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-ten", {t10:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tmt = aw(s, "do the math")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's do the math!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tmt:.2f});
""")

# 4 DAILY — 24 hour squares, 3 h 46 min filled
s = "daily"; taw = aw(s, "around the world"); tav = aw(s, "average person"); t3 = aw(s, "three hours"); tday = aw(s, "a day on")
SQ, GAP, X0, Y0 = 64, 8, 108, 470
hsq = "".join(f'<div class="abs" style="left:{X0+(k%12)*(SQ+GAP)}px;top:{Y0+(k//12)*(SQ+GAP)}px;width:{SQ}px;height:{SQ}px;border:3px solid {K};border-radius:6px 10px 5px 9px;background:#fff"></div>' for k in range(24))
fills = "".join(f'<div id="dl-f{k}" class="abs" style="left:{X0+k*(SQ+GAP)+3}px;top:{Y0+3}px;width:{SQ-6}px;height:{SQ-6}px;background:{C["hi"]};transform-origin:0 50%"></div>' for k in range(4))
scenes[s] = scene_file(s, f"""
#dl-title {{ top:160px; font-size:72px; }}
#dl-tag {{ position:absolute; left:0; right:0; top:270px; text-align:center; }}
#dl-num {{ position:absolute; left:0; right:0; top:660px; text-align:center; font-size:120px; }}
#dl-key {{ position:absolute; left:108px; top:400px; font-size:40px; color:{C['muted']}; }}
""", f"""
  <div id="dl-title" class="h1">Phone time, <span class="hl">every day</span></div>
  <div id="dl-tag"><span class="chip" style="font-size:44px">world average</span></div>
  <div id="dl-key">1 square = 1 hour of your day</div>
  {hsq}{fills}
  <div id="dl-num" class="big"><span id="dl-t" class="red">0 h 00 min</span></div>
""", f"""
rise("#dl-title", 0.0); pop("#dl-tag .chip", {tav:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#dl-key", {taw:.2f});
for (let k=0;k<4;k++) tl.fromTo("#dl-f"+k, {{scaleX:0}}, {{scaleX:(k<3?1:0.77), duration:0.4, ease:"power1.inOut"}}, {t3:.2f}+k*0.4);
pop("#dl-num", {t3-0.1:.2f});
count("#dl-t", 0, 226, {t3:.2f}, 1.6, v => Math.floor(v/60) + " h " + String(Math.round(v)%60).padStart(2,"0") + " min");
tl.fromTo("#dl-num", {{scale:1}}, {{scale:1.1, duration:0.14, yoyo:true, repeat:1}}, {tday:.2f});
""")

# 5 AWAKE — hatched pie of 16 waking hours, ~1/4 wedge
s = "awake"; t16 = aw(s, "sixteen hours"); tq = aw(s, "almost a quarter")
import math
ang = 360 * 3.7667 / 16
cx, cy, r = 200, 200, 180
ex = cx + r * math.sin(math.radians(ang)); ey = cy - r * math.cos(math.radians(ang))
scenes[s] = scene_file(s, f"""
#aw-title {{ top:160px; font-size:72px; }}
#aw-pie {{ position:absolute; left:110px; top:330px; }}
#aw-lab {{ position:absolute; left:560px; top:380px; width:440px; text-align:center; }}
#aw-lab .big {{ font-size:110px; color:{C['red']}; }}
#aw-16 {{ position:absolute; left:560px; top:640px; width:440px; text-align:center; font-size:52px; }}
""", f"""
  <div id="aw-title" class="h1">Your <span class="hl">waking</span> day</div>
  <svg id="aw-pie" width="400" height="400" viewBox="0 0 400 400" data-layout-ignore>
    <defs><pattern id="aw-h" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="12" fill="{C['red']}"/></pattern></defs>
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{SKY}" {WSF}/>
    <g id="aw-w"><path d="M{cx},{cy} L{cx},{cy-r} A{r},{r} 0 0 1 {ex:.1f},{ey:.1f} Z" fill="url(#aw-h)" stroke="{C['red']}" stroke-width="5" stroke-linejoin="round"/></g>
    <path d="M{cx},{cy-r} L{cx},{cy-r+18}" stroke="{K}" stroke-width="5"/></svg>
  <div id="aw-lab"><div class="big">almost ¼</div><div style="font-size:46px">on the phone</div></div>
  <div id="aw-16">pie = <span class="blue">16 h</span> awake</div>
""", f"""
rise("#aw-title", 0.0); pop("#aw-pie", {t16-0.3:.2f}); rise("#aw-16", {t16:.2f});
tl.fromTo("#aw-w", {{opacity:0, scale:0.3, svgOrigin:"{cx} {cy}"}}, {{opacity:1, scale:1, svgOrigin:"{cx} {cy}", duration:0.4, ease:"back.out(2)"}}, {tq:.2f});
pop("#aw-lab", {tq+0.2:.2f});
""")

# 6 WEEK — 7 blocks stack past the 24 h line
s = "week"; tweek = aw(s, "one week"); t26 = aw(s, "twenty six"); twd = aw(s, "a whole day")
PX = 25; BASE = 930; BH = 3.7667 * PX
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
blocks = "".join(f'<div id="wk-b{k}" class="abs" style="left:600px;top:{BASE-(k+1)*BH:.1f}px;width:220px;height:{BH-4:.1f}px;background:{[C["hi"], PINK, SKY][k%3]};border:3px solid {K};border-radius:8px 12px 6px 10px;font-family:Gochi Hand,cursive;font-size:40px;line-height:{BH-8:.0f}px;text-align:center;opacity:0">{days[k]}</div>' for k in range(7))
scenes[s] = scene_file(s, f"""
#wk-title {{ top:150px; font-size:72px; }}
#wk-day {{ position:absolute; left:420px; top:{BASE-24*PX}px; width:130px; height:{24*PX}px; border:4px dashed {K}; border-radius:10px; background:#fff; }}
#wk-dlab {{ position:absolute; left:230px; top:{BASE-24*PX+10}px; width:170px; text-align:center; font-size:40px; }}
#wk-line {{ position:absolute; left:410px; top:{BASE-24*PX-3}px; width:460px; height:0; border-top:5px solid {C['red']}; opacity:0; }}
#wk-lab {{ position:absolute; left:840px; top:{BASE-7*BH-10:.0f}px; width:220px; font-size:62px; color:{C['red']}; }}
""", f"""
  <div id="wk-title" class="h1">One <span class="hl">week</span></div>
  <div id="wk-day"></div><div id="wk-dlab">1 day<br>= 24 h</div>
  {blocks}
  <div id="wk-line"></div>
  <div id="wk-lab" class="big">26+ h</div>
""", f"""
rise("#wk-title", 0.0); pop("#wk-day", 0.15); rise("#wk-dlab", 0.25);
for (let k=0;k<7;k++) tl.fromTo("#wk-b"+k, {{opacity:0, y:-80}}, {{opacity:1, y:0, duration:0.25, ease:"back.out(1.6)"}}, {tweek:.2f}+k*0.22);
pop("#wk-lab", {t26:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
tl.to("#wk-line", {{opacity:1, duration:0.15}}, {twd:.2f}); tl.fromTo("#wk-line", {{scaleX:0, transformOrigin:"0 50%"}}, {{scaleX:1, duration:0.35}}, {twd:.2f});
""")

# 7 YEAR — 365-square calendar, 57 red
s = "year"; tyr = aw(s, "one year"); t57 = aw(s, "fifty seven"); tclk = aw(s, "around the clock")
CS, CG, CX, CY = 30, 6, 90, 280
cal = "".join(f'<rect id="yr-c{k}" x="{(k%25)*(CS+CG)}" y="{(k//25)*(CS+CG)}" width="{CS}" height="{CS}" rx="4" fill="#fff" stroke="{K}" stroke-width="2.5"/>' for k in range(365))
scenes[s] = scene_file(s, f"""
#yr-title {{ top:150px; font-size:72px; }}
#yr-cal {{ position:absolute; left:{CX}px; top:{CY}px; }}
#yr-lab {{ position:absolute; left:400px; top:840px; width:600px; text-align:right; }}
#yr-lab .big {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="yr-title" class="h1">One <span class="hl">year</span> = 365 squares</div>
  <svg id="yr-cal" width="{25*(CS+CG)}" height="{15*(CS+CG)}" data-layout-ignore>{cal}</svg>
  <div id="yr-lab"><span class="big">≈ <span id="yr-n">0</span> full days</span></div>
""", f"""
rise("#yr-title", 0.0); tl.fromTo("#yr-cal", {{opacity:0}}, {{opacity:1, duration:0.4}}, {tyr-0.3:.2f});
for (let k=0;k<57;k++) tl.to("#yr-c"+k, {{fill:"{C['red']}", duration:0.05}}, {t57:.2f}+k*0.025);
pop("#yr-lab", {t57-0.1:.2f}); count("#yr-n", 0, 57, {t57:.2f}, 1.45, fmtInt);
tl.fromTo("#yr-lab", {{scale:1}}, {{scale:1.08, duration:0.14, yoyo:true, repeat:1}}, {tclk:.2f});
""")

# 8 LIFE — 0-70 ruler, 11 years hatched
s = "life"; t70 = aw(s, "seventy years"); t11 = aw(s, "eleven years")
X0, X1, Y = 110, 970, 520
ticks = "".join(f'<path d="M{X0+(X1-X0)*y/70:.1f},{Y-(26 if y%10==0 else 14)} L{X0+(X1-X0)*y/70:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{X0+(X1-X0)*y/70:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 10 == 0 else "") for y in range(0, 71, 5))
seg = (X1 - X0) * 11 / 70
scenes[s] = scene_file(s, f"""
#lf-bar {{ position:absolute; left:{X0}px; top:{Y-70}px; width:{X1-X0}px; height:60px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-seg {{ position:absolute; right:0; top:0; height:100%; width:{seg:.1f}px; transform-origin:100% 50%; }}
#lf-lab {{ position:absolute; right:90px; top:620px; text-align:right; }}
#lf-lab .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="lf-title" class="h1" style="top:160px;font-size:76px">Keep it up for <span class="hl">70 years</span></div>
  <div id="lf-bar"><div id="lf-seg" class="hatch-r"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="720" data-layout-ignore>{ticks}
    <path id="lf-arrow" d="M760,690 Q890,670 900,{Y+20}" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="lf-lab"><div class="big">≈ 11 years</div><div style="font-size:46px;color:{C['muted']}">looking at a phone</div></div>
""", f"""
rise("#lf-title", 0.0); rise("#lf-bar", {t70-0.2:.2f});
tl.fromTo("#lf-seg", {{scaleX:0}}, {{scaleX:1, duration:0.6, ease:"power2.out"}}, {t11:.2f});
draw("#lf-arrow", {t11+0.2:.2f}, 0.4); pop("#lf-lab", {t11+0.3:.2f});
""")

# 9 RANGE — honest range 11 to 15 years
s = "range"; tavg = aw(s, "just the average"); t5h = aw(s, "five hours"); t15 = aw(s, "fifteen years")
LX0, LX1, LY = 130, 950, 560
def lx(v): return LX0 + (LX1 - LX0) * v / 20
nticks = "".join(f'<path d="M{lx(v):.1f},{LY-16} L{lx(v):.1f},{LY+16}" stroke="{K}" stroke-width="4" stroke-linecap="round"/><text x="{lx(v):.1f}" y="{LY+62}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{v}</text>' for v in range(0, 21, 5))
scenes[s] = scene_file(s, f"""
#rg-title {{ top:160px; font-size:72px; }}
#rg-a {{ position:absolute; left:{lx(11)-150:.0f}px; top:330px; width:300px; text-align:center; font-size:42px; }}
#rg-b {{ position:absolute; left:{lx(15)-150:.0f}px; top:690px; width:300px; text-align:center; font-size:42px; }}
#rg-big {{ position:absolute; left:400px; top:810px; width:600px; text-align:right; font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="rg-title" class="h1">Your number <span class="hl">may be bigger</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <rect id="rg-band" x="{lx(11):.1f}" y="{LY-34}" width="{lx(15)-lx(11):.1f}" height="68" rx="10" fill="{C['hi']}" opacity="0"/>
    <path d="M{LX0-20},{LY} Q540,{LY-6} {LX1+30},{LY+2}" {WS}/>{nticks}
    <text x="{LX1+30}" y="{LY+110}" text-anchor="end" font-family="Patrick Hand" font-size="34" fill="{C['muted']}">years of life</text>
    <g id="rg-d1" opacity="0"><circle cx="{lx(11):.1f}" cy="{LY}" r="18" fill="{C['blue']}" stroke="{K}" stroke-width="4"/><path d="M{lx(11):.1f},{LY-24} L{lx(11):.1f},{LY-120}" stroke="{C['blue']}" stroke-width="5" stroke-dasharray="10 8"/></g>
    <g id="rg-d2" opacity="0"><circle cx="{lx(15):.1f}" cy="{LY}" r="18" fill="{C['red']}" stroke="{K}" stroke-width="4"/><path d="M{lx(15):.1f},{LY+78} L{lx(15):.1f},{LY+118}" stroke="{C['red']}" stroke-width="5" stroke-dasharray="10 8"/></g></svg>
  <div id="rg-a"><span class="blue">average</span><br>3 h 46 min / day</div>
  <div id="rg-b"><span class="red">5 h / day</span></div>
  <div id="rg-big" class="big">≈ 15 years</div>
""", f"""
rise("#rg-title", 0.0);
tl.to("#rg-d1", {{opacity:1, duration:0.2}}, {tavg:.2f}); pop("#rg-a", {tavg+0.1:.2f});
tl.to("#rg-d2", {{opacity:1, duration:0.2}}, {t5h:.2f}); pop("#rg-b", {t5h+0.1:.2f});
tl.to("#rg-band", {{opacity:0.85, duration:0.3}}, {t15-0.2:.2f}); pop("#rg-big", {t15:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 10 TIP — not all wasted + check your screen time
s = "tip"; tnw = aw(s, "not all"); tmp = aw(s, "maps"); tcl = aw(s, "calls"); tle = aw(s, "learning"); ton = aw(s, "tonight"); tscr = aw(s, "screen time")
chips = [("mp", "maps", tmp, 230), ("cl", "calls", tcl, 330), ("le", "learning", tle, 430)]
ch = "".join(f'<div id="tp-{k}" class="abs" style="left:110px;top:{y}px;font-size:58px;opacity:0"><span class="pill blue">✓ {txt}</span></div>' for k, txt, t, y in chips)
bars = "".join(f'<rect id="tp-bar{k}" x="48" y="{70+k*34}" width="{w}" height="20" rx="5" fill="{c}" stroke="{K}" stroke-width="2" style="transform-box:fill-box;transform-origin:0 50%"/>' for k, (w, c) in enumerate([(66, C["red"]), (48, C["hi"]), (34, SKY), (22, PINK)]))
screen = f'<text x="80" y="54" text-anchor="middle" font-family="Gochi Hand" font-size="17" fill="{K}">screen time</text>{bars}<text x="80" y="220" text-anchor="middle" font-family="Gochi Hand" font-size="22" fill="{C["red"]}">?? h</text>'
scenes[s] = scene_file(s, f"""
#tp-title {{ top:150px; font-size:66px; }}
#tp-ph {{ position:absolute; left:640px; top:260px; }}
#tp-to {{ position:absolute; left:80px; top:640px; width:520px; text-align:center; }}
#tp-to .big {{ font-size:72px; }}
""", f"""
  <div id="tp-title" class="h1" style="opacity:0">Not all <span class="hl">wasted</span></div>
  {ch}
  <div id="tp-ph">{phone_svg('tp-p', 300, screen)}</div>
  <div id="tp-to"><div class="big">Tonight:<br><span class="hl">check yours!</span></div></div>
""", f"""
rise("#tp-title", {tnw:.2f});
{"".join(f'pop("#tp-{k}", {t:.2f}, {{from:{{rotation:-8}}, to:{{rotation:0}}}});' for k, _, t, _ in chips)}
pop("#tp-ph", {ton-0.1:.2f}, {{from:{{rotation:10}}, to:{{rotation:3}}}});
for (let k=0;k<4;k++) tl.fromTo("#tp-bar"+k, {{scaleX:0}}, {{scaleX:1, duration:0.3, ease:"power2.out"}}, {tscr:.2f}+k*0.12);
pop("#tp-to", {ton+0.2:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
""")

# 11 OUTRO
s = "outro"; t11o = aw(s, "eleven years"); tmc = aw(s, "make them count"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:72px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">11 years</span> on a phone…</div>
  <div id="ou-b" class="h1"><span class="red">Make them count!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {t11o:.2f}); pop("#ou-b", {tmc:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "quick question"), SC["guess"]["start"] + 0.2)
point(g("guess", "one year"), 2.4)
wave(g("intro", "I'm Max"))
point(g("daily", "three hours"), 1.6)
point(g("awake", "almost a quarter"), 1.2)
wow(g("week", "twenty six"), 1.2)
point(g("year", "fifty seven"), 1.4)
wow(g("life", "eleven years"), 1.6)
think(g("range", "just the average"), g("range", "five hours"))
wow(g("range", "fifteen years"), 1.2)
point(g("tip", "tonight"), 1.6)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "staring"), 0.35), ("pop.mp3", A("guess", "one year"), 0.5), ("pop.mp3", A("guess", "five years"), 0.5),
        ("pop.mp3", A("guess", "more than ten"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("daily", "three hours"), 0.6),
        ("pop.mp3", A("week", "twenty six"), 0.55), ("ping.mp3", A("year", "fifty seven"), 0.35),
        ("impact-bass-1.mp3", A("life", "eleven years") + 0.3, 0.45), ("click.mp3", A("range", "five hours"), 0.45),
        ("pop.mp3", A("tip", "maps"), 0.4), ("pop.mp3", A("tip", "learning"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
