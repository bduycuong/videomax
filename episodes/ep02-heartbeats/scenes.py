# MAX WISE ep02 — How many times will your heart beat? Executed inside engine/maxwise.py.
# === SCENES ===
HP = "M100,172 Q22,112 22,64 Q24,20 64,20 Q90,21 100,54 Q110,21 136,20 Q176,20 178,64 Q178,112 100,172 Z"
def heart_svg(pid, w=300, fill=None):
    fill = fill or C['red']
    return (f'<svg id="{pid}" viewBox="0 0 200 190" width="{w}" height="{w*190/200:.0f}" style="overflow:visible" data-layout-ignore>'
            f'<path d="{HP}" fill="{fill}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M52,58 Q56,40 72,38" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".8"/></svg>')
def beat_js(sel, t0, n, gap=0.75):
    return f'for (let k=0;k<{n};k++) {{ const t={t0:.2f}+k*{gap}; tl.to("{sel}", {{scale:1.14, duration:0.1, ease:"power2.out"}}, t); tl.to("{sel}", {{scale:1, duration:0.18, ease:"power2.in"}}, t+0.1); tl.to("{sel}", {{scale:1.07, duration:0.08}}, t+0.3); tl.to("{sel}", {{scale:1, duration:0.15}}, t+0.38); }}'

# 1 HOOK — hand on your chest
s = "hook"; thd = aw(s, "put your hand"); thm = aw(s, "how many"); thb = aw(s, "heart beat"); twl = aw(s, "whole life")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:84px; }}
#hk-heart {{ position:absolute; left:380px; top:560px; width:340px; }}
#hk-lines {{ position:absolute; left:250px; top:540px; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many times will your <span class="hl">heart beat</span> in your whole life?</div>
  <svg id="hk-lines" width="600" height="380" data-layout-ignore>
    <path id="hk-l1" d="M60,120 Q30,190 60,260" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="hk-l2" d="M20,90 Q-20,190 20,290" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="hk-l3" d="M540,120 Q570,190 540,260" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="hk-l4" d="M580,90 Q620,190 580,290" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="hk-heart">{heart_svg('hk-h', 340)}</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#hk-heart", {thd:.2f}); rise("#hk-q", {thm-0.05:.2f});
{beat_js("#hk-heart", thd+0.4, 6)}
for (let i=1;i<=4;i++) draw("#hk-l"+i, {thb:.2f}+(i%2)*0.1, 0.25);
""")

# 2 GUESS — million? billion? more?
s = "guess"; tg = aw(s, "take a guess"); tmi = aw(s, "a million"); tbi = aw(s, "a billion"); tmo = aw(s, "even more")
notes = [("mi", "a million?", -6, 110, C['hi']), ("bi", "a billion?", 4, 400, "#BFE3F7"), ("mo", "even more?", -3, 690, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:280px;height:250px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:62px;line-height:1.05">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-mi", {tmi:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-bi", {tbi:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-mo", {tmo:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's count")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count it!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 MINUTE — 60 to 100, call it 80
s = "minute"; tgr = aw(s, "a grown up"); t60 = aw(s, "about sixty"); t100 = aw(s, "one hundred"); t80 = aw(s, "call it eighty")
X0, X1, Y = 140, 940, 640
xv = lambda v: X0 + (X1 - X0) * (v - 50) / 60
ecg = "M40,160 L250,160 L280,120 L300,160 L330,160 L350,40 L375,260 L400,160 L440,160 L470,130 L500,160 L1000,160"
scenes[s] = scene_file(s, f"""
#mn-title {{ top:150px; font-size:72px; }}
#mn-ecg {{ position:absolute; left:0; top:270px; }}
#mn-80 {{ position:absolute; left:{xv(80)-110:.0f}px; top:770px; width:220px; text-align:center; font-size:120px; color:{C['red']}; }}
#mn-unit {{ position:absolute; left:{xv(80)+110:.0f}px; top:810px; font-size:50px; }}
""", f"""
  <div id="mn-title" class="h1">Beats per <span class="hl">minute</span></div>
  <svg id="mn-ecg" width="{W}" height="320" viewBox="0 0 1040 320" data-layout-ignore><path id="mn-line" d="{ecg}" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <path d="M{X0},{Y} L{X1},{Y}" {WS}/>
    {''.join(f'<path d="M{xv(v):.0f},{Y-14} L{xv(v):.0f},{Y+14}" {WS}/><text x="{xv(v):.0f}" y="{Y+62}" text-anchor="middle" font-family="Patrick Hand" font-size="44" fill="{K}">{v}</text>' for v in (60, 80, 100))}
    <rect id="mn-band" x="{xv(60):.0f}" y="{Y-30}" width="{xv(100)-xv(60):.0f}" height="60" fill="{C['hi']}" opacity=".7" style="transform-origin:{xv(60):.0f}px {Y}px"/>
    <path id="mn-ring" d="M{xv(80)-70:.0f},{Y+40} Q{xv(80):.0f},{Y-10} {xv(80)+66:.0f},{Y+38} Q{xv(80)+70:.0f},{Y+100} {xv(80):.0f},{Y+96} Q{xv(80)-74:.0f},{Y+96} {xv(80)-64:.0f},{Y+30}" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="mn-80" class="big">80</div>
  <div id="mn-unit">beats / minute</div>
""", f"""
rise("#mn-title", 0.0); draw("#mn-line", {tgr:.2f}, 1.4, "none");
tl.fromTo("#mn-band", {{scaleX:0}}, {{scaleX:1, duration:0.9, ease:"power2.out"}}, {t60:.2f});
draw("#mn-ring", {t80-0.2:.2f}, 0.35); pop("#mn-80", {t80:.2f}); rise("#mn-unit", {t80+0.2:.2f});
""")

# 5 HOUR — 80 x 60 = 4,800
s = "hour"; te = aw(s, "eighty beats"); ts = aw(s, "sixty minutes"); t48 = aw(s, "four thousand"); teh = aw(s, "every hour")
scenes[s] = scene_file(s, f"""
#hr-title {{ top:150px; font-size:72px; }}
#hr-r1 {{ position:absolute; left:0; right:0; top:330px; text-align:center; font-size:100px; }}
#hr-ans {{ position:absolute; left:0; right:0; top:540px; text-align:center; }}
#hr-ans span {{ font-size:120px; color:{C['red']}; }}
#hr-sub {{ top:760px; font-size:54px; }}
""", f"""
  <div id="hr-title" class="h1">One <span class="hl">hour</span></div>
  <div id="hr-r1" class="big"><span id="hr-a">80</span> <span id="hr-x">×</span> <span id="hr-b" class="blue">60 min</span></div>
  <div id="hr-ans"><span class="pill">= 4,800</span></div>
  <div id="hr-sub" class="h2">beats every hour</div>
""", f"""
rise("#hr-title", 0.0); pop("#hr-a", {te:.2f}); pop("#hr-x", {ts-0.25:.2f}); pop("#hr-b", {ts:.2f});
pop("#hr-ans span", {t48:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#hr-sub", {teh:.2f});
""")

# 6 DAY — 115,000 a day, even asleep
s = "day"; tod = aw(s, "over one day"); t115 = aw(s, "one hundred fifteen"); tsl = aw(s, "while you sleep")
scenes[s] = scene_file(s, f"""
#dy-title {{ top:150px; font-size:72px; }}
#dy-num {{ position:absolute; left:0; right:0; top:330px; text-align:center; font-size:130px; color:{C['red']}; }}
#dy-sub {{ top:490px; font-size:54px; }}
#dy-moon {{ position:absolute; left:560px; top:600px; }}
#dy-heart {{ position:absolute; left:420px; top:680px; width:150px; }}
""", f"""
  <div id="dy-title" class="h1">One <span class="hl">day</span></div>
  <div id="dy-num" class="big">≈ <span id="dy-n">0</span></div>
  <div id="dy-sub" class="h2">beats a day</div>
  <svg id="dy-moon" width="360" height="300" viewBox="0 0 180 150" data-layout-ignore>
    <path d="M70,20 Q20,40 26,90 Q34,136 84,138 Q120,136 136,110 Q90,116 72,84 Q56,52 70,20 Z" fill="{C['hi']}" {WS.replace('fill="none" ', '')}/>
    <text id="dy-z1" x="118" y="58" font-family="Gochi Hand" font-size="34" fill="{C['blue']}">z</text>
    <text id="dy-z2" x="138" y="36" font-family="Gochi Hand" font-size="44" fill="{C['blue']}">z</text></svg>
  <div id="dy-heart">{heart_svg('dy-h', 150)}</div>
""", f"""
rise("#dy-title", 0.0); pop("#dy-num", {tod:.2f});
count("#dy-n", 0, 115000, {tod+0.1:.2f}, {t115-tod+0.9:.2f}, fmtInt); rise("#dy-sub", {t115+0.5:.2f});
pop("#dy-moon", {tsl-0.3:.2f}); pop("#dy-heart", {tsl:.2f}); pop("#dy-z1", {tsl+0.3:.2f}); pop("#dy-z2", {tsl+0.5:.2f});
{beat_js("#dy-heart", tsl+0.3, 2, 0.7)}
""")

# 7 YEAR — 42 million
s = "year"; toy = aw(s, "one year"); t42 = aw(s, "forty two")
cells = "".join(f'<rect x="{30+(i%7)*44}" y="{70+(i//7)*40}" width="34" height="30" fill="{C["red"] if (i*7)%5==0 else "#fff"}" stroke="{K}" stroke-width="3" opacity="{0.85 if (i*7)%5==0 else 1}"/>' for i in range(35))
scenes[s] = scene_file(s, f"""
#yr-title {{ top:150px; font-size:72px; }}
#yr-cal {{ position:absolute; left:370px; top:290px; }}
#yr-num {{ position:absolute; left:0; right:0; top:620px; text-align:center; font-size:120px; color:{C['red']}; }}
#yr-sub {{ top:760px; font-size:54px; }}
""", f"""
  <div id="yr-title" class="h1">One <span class="hl">year</span></div>
  <svg id="yr-cal" width="340" height="300" viewBox="0 0 340 300" data-layout-ignore>
    <path d="M14,24 Q170,18 326,25 L324,286 Q170,290 16,285 Z" fill="#fff" {WS.replace('fill="none" ', '')}/>
    <path d="M14,24 L326,25 L326,56 L14,56 Z" fill="{C['red']}" stroke="{K}" stroke-width="5"/>
    <path d="M80,8 L80,40 M260,8 L260,40" {WS}/>{cells}</svg>
  <div id="yr-num" class="big">≈ <span id="yr-n">0</span></div>
  <div id="yr-sub" class="h2">beats a year</div>
""", f"""
rise("#yr-title", 0.0); pop("#yr-cal", {toy:.2f}); pop("#yr-num", {toy+0.2:.2f});
count("#yr-n", 0, 42000000, {toy+0.3:.2f}, {t42-toy+0.6:.2f}, fmtInt); rise("#yr-sub", {t42+0.5:.2f});
""")

# 8 LIFE — 80 years -> 3 billion+
s = "life"; t80y = aw(s, "eighty years"); tmt = aw(s, "more than three"); thb = aw(s, "heartbeats")
X0, X1, Y = 110, 970, 470
ticks = "".join(f'<path d="M{X0+(X1-X0)*y/80:.1f},{Y-(26 if y%20==0 else 14)} L{X0+(X1-X0)*y/80:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{X0+(X1-X0)*y/80:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 20 == 0 else "") for y in range(0, 81, 5))
scenes[s] = scene_file(s, f"""
#lf-title {{ top:150px; font-size:76px; }}
#lf-bar {{ position:absolute; left:{X0}px; top:{Y-70}px; width:{X1-X0}px; height:60px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-fill {{ position:absolute; left:0; top:0; height:100%; width:100%; transform-origin:0 50%; }}
#lf-num {{ position:absolute; left:0; right:0; top:620px; text-align:center; font-size:112px; color:{C['red']}; }}
#lf-sub {{ top:760px; font-size:56px; }}
""", f"""
  <div id="lf-title" class="h1">A whole life: <span class="hl">80 years</span></div>
  <div id="lf-bar"><div id="lf-fill" class="hatch-r"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="600" data-layout-ignore>{ticks}</svg>
  <div id="lf-num" class="big"><span id="lf-n">0</span><span id="lf-plus">+</span></div>
  <div id="lf-sub" class="h2">more than <b class="red">three billion</b> heartbeats!</div>
""", f"""
rise("#lf-title", 0.0); rise("#lf-bar", 0.1);
tl.fromTo("#lf-fill", {{scaleX:0}}, {{scaleX:1, duration:{tmt-t80y+0.2:.2f}, ease:"none"}}, {t80y:.2f});
pop("#lf-num", {t80y+0.2:.2f}); count("#lf-n", 0, 3000000000, {t80y+0.3:.2f}, {tmt-t80y+0.4:.2f}, fmtInt);
tl.fromTo("#lf-plus", {{opacity:0}}, {{opacity:1, duration:0.1}}, {tmt+0.6:.2f});
rise("#lf-sub", {thb-0.3:.2f}); tl.fromTo("#lf-num", {{scale:1}}, {{scale:1.1, duration:0.14, yoyo:true, repeat:1}}, {thb:.2f});
""")

# 9 PUMP — fist-sized, never stops
s = "pump"; tnb = aw(s, "never takes"); tfi = aw(s, "your fist"); tdn = aw(s, "day and night")
scenes[s] = scene_file(s, f"""
#pm-title {{ top:150px; font-size:72px; }}
#pm-heart {{ position:absolute; left:150px; top:330px; width:330px; }}
#pm-fist {{ position:absolute; left:600px; top:330px; }}
#pm-eq {{ position:absolute; left:470px; top:420px; width:140px; text-align:center; font-size:100px; }}
#pm-lab {{ position:absolute; left:0; right:0; top:700px; text-align:center; font-size:58px; }}
""", f"""
  <div id="pm-title" class="h1">It <span class="hl">never</span> takes a break</div>
  <div id="pm-heart">{heart_svg('pm-h', 330)}</div>
  <div id="pm-eq" class="big">≈</div>
  <svg id="pm-fist" width="330" height="320" viewBox="0 0 165 160" data-layout-ignore>
    <path d="M30,52 Q32,26 56,28 Q60,14 80,18 Q90,8 108,16 Q126,12 130,32 Q150,40 144,74 Q142,118 106,136 L104,154 L52,154 L52,134 Q24,118 26,84 Q16,66 30,52 Z" fill="#F6D2B0" {WS.replace('fill="none" ', '')}/>
    <path d="M56,28 Q58,52 60,60 M80,18 Q82,48 84,58 M108,16 Q108,46 110,58 M30,52 Q60,66 130,60 M40,88 Q70,74 92,86" {WS}/></svg>
  <div id="pm-lab"><span class="pill">squeezing day &amp; night</span></div>
""", f"""
rise("#pm-title", {tnb-0.1:.2f}); pop("#pm-heart", 0.1);
{beat_js("#pm-heart", 0.4, 8, 0.72)}
pop("#pm-eq", {tfi-0.3:.2f}); pop("#pm-fist", {tfi:.2f}, {{from:{{rotation:-15}}, to:{{rotation:0}}}});
pop("#pm-lab .pill", {tdn:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 10 KIDS — faster beats, higher total
s = "kids"; tch = aw(s, "children have"); tfh = aw(s, "faster heartbeats"); thi = aw(s, "even higher")
scenes[s] = scene_file(s, f"""
#kd-title {{ top:150px; font-size:72px; }}
#kd-a {{ position:absolute; left:150px; top:330px; width:330px; text-align:center; }}
#kd-b {{ position:absolute; left:600px; top:330px; width:330px; text-align:center; }}
#kd-a .lab, #kd-b .lab {{ font-family:'Gochi Hand',cursive; font-size:58px; margin-top:6px; }}
#kd-up {{ position:absolute; left:0; right:0; top:720px; text-align:center; }}
#kd-up span {{ font-size:66px; color:{C['red']}; }}
""", f"""
  <div id="kd-title" class="h1"><span class="hl">Kids</span> beat faster</div>
  <div id="kd-a"><div id="kd-ha" style="width:180px;margin:40px auto 0">{heart_svg('kd-h1', 180)}</div><div class="lab">grown up</div></div>
  <div id="kd-b"><div id="kd-hb" style="width:150px;margin:55px auto 0">{heart_svg('kd-h2', 150, '#F27A6E')}</div><div class="lab red">child</div></div>
  <div id="kd-up"><span class="pill">real total: even higher!</span></div>
""", f"""
rise("#kd-title", 0.0); pop("#kd-a", 0.15); pop("#kd-b", {tch:.2f});
{beat_js("#kd-ha", 0.5, 6, 0.85)}
{beat_js("#kd-hb", tfh, 6, 0.56)}
pop("#kd-up .pill", {thi-0.2:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 11 OUTRO
s = "outro"; tm3 = aw(s, "more than three"); tev = aw(s, "every single"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">3 billion+</span> beats…</div>
  <div id="ou-b" class="h1">…and every single one kept you going.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tm3:.2f}); rise("#ou-b", {tm3+1.0:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "a million"), 2.4)
wave(g("intro", "I'm Max"))
point(g("minute", "call it eighty"), 1.2)
point(g("hour", "four thousand"), 1.4)
wow(g("day", "while you sleep"), 1.2)
point(g("year", "forty two"), 1.2)
wow(g("life", "more than three"), 1.8)
point(g("pump", "your fist"), 1.4)
think(SC["kids"]["start"] + 0.05, g("kids", "even higher"))
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "heart beat"), 0.35), ("pop.mp3", A("guess", "a million"), 0.5), ("pop.mp3", A("guess", "a billion"), 0.5),
        ("pop.mp3", A("guess", "even more"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("minute", "call it eighty"), 0.6),
        ("pop.mp3", A("hour", "four thousand"), 0.55), ("click-soft.mp3", A("life", "eighty years"), 0.5),
        ("impact-bass-1.mp3", A("life", "more than three") + 0.4, 0.45), ("pop.mp3", A("pump", "your fist"), 0.5),
        ("click.mp3", A("kids", "even higher") - 0.2, 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
