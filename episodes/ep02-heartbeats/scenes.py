# MAX WISE ep02 — How many times will your heart beat in your whole life?
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
def heart_svg(pid, w, fill=None):
    fill = fill or C['red']
    return (f'<svg id="{pid}" viewBox="0 0 200 180" width="{w}" height="{w*0.9:.0f}" style="overflow:visible;transform-origin:50% 55%" data-layout-ignore>'
            f'<path d="M100,170 Q34,122 20,72 Q10,24 56,16 Q88,12 100,48 Q112,12 144,16 Q190,24 180,72 Q166,122 100,170 Z" fill="{fill}" {WSF}/>'
            f'<path d="M48,44 Q38,58 42,76" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".8"/></svg>')
BEAT = 'const beat=(sel,t,s)=>tl.fromTo(sel,{scale:1},{scale:s||1.14,duration:0.1,yoyo:true,repeat:1,ease:"power1.out"},t);'
ECG = "M0,60 L120,60 L140,40 L160,60 L190,60 L205,5 L222,110 L238,60 L300,60 L320,44 L340,60 L420,60"

# 1 HOOK
s = "hook"; tq = aw(s, "how many"); thb = aw(s, "heart beat"); twl = aw(s, "whole life")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:86px; }}
#hk-heart {{ position:absolute; left:400px; top:590px; }}
#hk-qm1 {{ position:absolute; left:770px; top:560px; font-family:'Gochi Hand',cursive; font-size:130px; color:{C['blue']}; }}
#hk-qm2 {{ position:absolute; left:860px; top:700px; font-family:'Gochi Hand',cursive; font-size:90px; color:{C['blue']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many times will your heart beat in your <span class="hl">whole life</span>?</div>
  <div id="hk-heart">{heart_svg('hk-h', 320)}</div>
  <div id="hk-qm1">?</div><div id="hk-qm2">?</div>
""", f"""
{BEAT}
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tq-0.05:.2f}); pop("#hk-heart", {thb-0.2:.2f});
for (let i=0;i<5;i++) beat("#hk-h", {thb+0.3:.2f}+i*0.75);
pop("#hk-qm1", {twl:.2f}, {{from:{{rotation:20}}, to:{{rotation:8}}}}); pop("#hk-qm2", {twl+0.2:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "a million"); t2 = aw(s, "a hundred million"); t3 = aw(s, "or billions")
notes = [("m1", "1<br>million?", -6, 110, C['hi']), ("m100", "100<br>million?", 4, 405, "#BFE3F7"), ("bn", "Billions?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:58px;line-height:1.05">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-m1", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-m100", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-bn", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's count")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count the beats!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 FEEL — fingers on the wrist
s = "feel"; tt = aw(s, "try this"); tfi = aw(s, "two fingers"); tth = aw(s, "steady thump")
scenes[s] = scene_file(s, f"""
#fe-arm {{ position:absolute; left:110px; top:330px; }}
#fe-lab {{ position:absolute; left:0; right:0; top:760px; text-align:center; font-size:64px; color:{C['red']}; }}
""", f"""
  <div id="fe-title" class="h1" style="top:160px;font-size:78px"><span class="hl">Try this!</span></div>
  <svg id="fe-arm" width="860" height="400" viewBox="0 0 430 200" style="overflow:visible" data-layout-ignore>
    <path d="M0,70 Q140,62 250,66 Q300,60 330,52 Q380,44 410,70 Q424,100 404,128 Q370,150 320,140 Q280,136 250,138 Q140,142 0,136" fill="#FFF3E2" {WS.replace('fill="none" ', '')}/>
    <path d="M230,74 Q236,102 230,130" stroke="{C['pencil']}" stroke-width="3" fill="none" stroke-linecap="round"/>
    <g id="fe-fing">
      <path d="M150,20 Q186,16 214,24 Q226,38 212,52 Q180,58 150,52 Z" fill="#FFE2C4" {WS.replace('fill="none" ', '')}/>
      <path d="M150,58 Q186,54 216,62 Q228,76 214,90 Q182,96 150,90 Z" fill="#FFE2C4" {WS.replace('fill="none" ', '')}/>
      <path d="M150,20 Q90,30 60,10 M150,90 Q100,96 70,120" {WS}/></g>
    <g id="fe-rings" style="opacity:0"><path d="M240,104 m-24,-30 a40,40 0 0 1 0,60" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <path d="M262,60 a60,60 0 0 1 0,88" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/></g></svg>
  <div id="fe-lab">thump… thump… thump…</div>
""", f"""
rise("#fe-title", {tt:.2f}); rise("#fe-arm", 0.15);
tl.fromTo("#fe-fing", {{opacity:0, y:-60}}, {{opacity:1, y:0, duration:0.35, ease:"power2.out"}}, {tfi:.2f});
for (let i=0;i<4;i++) {{ const t={tth:.2f}+i*0.8; tl.fromTo("#fe-rings", {{opacity:1, scale:0.7, svgOrigin:"240 104"}}, {{opacity:0, scale:1.3, duration:0.6, ease:"power1.out"}}, t); }}
rise("#fe-lab", {tth:.2f});
""")

# 5 RATE — 60 to 100, call it 70
s = "rate"; t60 = aw(s, "sixty to"); t70 = aw(s, "call it seventy") + 0.3; tra = aw(s, "resting adult")
X0, X1 = 150, 930
xs = lambda v: X0 + (X1 - X0) * (v - 50) / 60
ticks = "".join(f'<path d="M{xs(v):.0f},560 L{xs(v):.0f},{536 if v % 10 == 0 else 548}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{xs(v):.0f}" y="610" text-anchor="middle" font-family="Patrick Hand" font-size="40" fill="{K}">{v}</text>' if v in (60, 70, 80, 90, 100) else "") for v in range(50, 111, 5))
scenes[s] = scene_file(s, f"""
#rt-ecg {{ position:absolute; left:110px; top:180px; }}
#rt-band {{ position:absolute; left:{xs(60):.0f}px; top:470px; width:{xs(100)-xs(60):.0f}px; height:60px; background:#FFC9C2; border:4px solid {K}; {SKETCH} transform-origin:0 50%; }}
#rt-num {{ position:absolute; left:0; right:0; top:690px; text-align:center; font-size:110px; }}
""", f"""
  <svg id="rt-ecg" width="860" height="230" viewBox="0 0 420 115" data-layout-ignore><path id="rt-line" d="{ECG}" stroke="{C['red']}" stroke-width="4" fill="none" stroke-linejoin="round" stroke-linecap="round"/></svg>
  <div id="rt-band"></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="640" data-layout-ignore>{ticks}
    <g id="rt-mk"><path d="M{xs(70):.0f},455 L{xs(70)-18:.0f},420 L{xs(70)+18:.0f},420 Z" fill="{C['blue']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></g></svg>
  <div id="rt-num" class="big">≈ <span class="red">70</span> beats / minute</div>
""", f"""
draw("#rt-line", {tra:.2f}, 1.2, "none");
tl.fromTo("#rt-band", {{scaleX:0, opacity:0}}, {{scaleX:1, opacity:1, duration:0.6, ease:"power2.out"}}, {t60:.2f});
pop("#rt-mk", {t70:.2f}, {{from:{{y:-40}}, to:{{}}}}); pop("#rt-num", {t70+0.1:.2f});
""")

# 6 HOUR — 4,200
s = "hour"; th = aw(s, "one hour"); t42 = aw(s, "four thousand")
scenes[s] = scene_file(s, f"""
#hr-clock {{ position:absolute; left:390px; top:170px; }}
#hr-cnt {{ position:absolute; left:0; right:0; top:560px; text-align:center; }}
#hr-cnt .big {{ font-size:170px; color:{C['red']}; }}
""", f"""
  <svg id="hr-clock" width="300" height="300" viewBox="0 0 200 200" data-layout-ignore>
    <path d="M100,12 Q186,14 188,100 Q186,186 100,188 Q14,186 12,100 Q14,14 100,12 Z" fill="#fff" {WS.replace('fill="none" ', '')}/>
    {''.join(f'<path d="M100,24 L100,36" transform="rotate({i*30} 100 100)" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for i in range(12))}
    <path d="M100,100 L100,58" stroke="{K}" stroke-width="7" stroke-linecap="round"/>
    <g id="hr-min"><path d="M100,100 L100,34" stroke="{C['red']}" stroke-width="5" stroke-linecap="round"/></g>
    <circle cx="100" cy="100" r="7" fill="{K}"/></svg>
  <div id="hr-cnt"><div style="font-size:60px">1 hour =</div><div id="hr-n" class="big">0</div><div style="font-size:60px">beats</div></div>
""", f"""
pop("#hr-clock", {th-0.1:.2f}); tl.set("#hr-min", {{rotation:0, svgOrigin:"100 100"}}, 0);
tl.to("#hr-min", {{rotation:360, duration:1.4, ease:"power1.inOut"}}, {th:.2f});
rise("#hr-cnt", {th:.2f}); count("#hr-n", 0, 4200, {th+0.1:.2f}, {t42-th+0.6:.2f}, fmtInt);
""")

# 7 DAY — 100,000
s = "day"; td = aw(s, "one day"); t100 = aw(s, "one hundred thousand"); tnv = aw(s, "never have")
scenes[s] = scene_file(s, f"""
#dy-sun {{ position:absolute; left:420px; top:160px; }}
#dy-cnt {{ position:absolute; left:0; right:0; top:450px; text-align:center; }}
#dy-cnt .big {{ font-size:150px; color:{C['red']}; }}
#dy-auto {{ position:absolute; left:440px; top:790px; width:560px; text-align:center; }}
#dy-auto span {{ font-size:58px; color:{C['blue']}; }}
""", f"""
  <svg id="dy-sun" width="240" height="240" viewBox="0 0 120 120" data-layout-ignore>
    <circle cx="60" cy="60" r="28" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>
    {''.join(f'<path d="M60,14 L60,24" transform="rotate({i*45} 60 60)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(8))}</svg>
  <div id="dy-cnt"><div style="font-size:60px">1 day ≈</div><div id="dy-n" class="big">4,200</div><div style="font-size:60px">beats</div></div>
  <div id="dy-auto"><span class="pill">on autopilot!</span></div>
""", f"""
pop("#dy-sun", {td-0.1:.2f}); tl.fromTo("#dy-sun", {{rotation:0}}, {{rotation:90, duration:4, ease:"none"}}, {td:.2f});
rise("#dy-cnt", {td:.2f}); count("#dy-n", 4200, 100000, {td+0.1:.2f}, {t100-td+0.8:.2f}, fmtInt);
pop("#dy-auto span", {tnv:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
""")

# 8 YEAR — 37 million
s = "year"; ty = aw(s, "one year"); t37 = aw(s, "thirty seven")
cal = "".join(f'<div class="abs" style="left:{130+(i%6)*140}px;top:{180+(i//6)*120}px;width:120px;height:100px;border:4px solid {K};{SKETCH}background:#fff;text-align:center;font-size:30px;line-height:96px" id="yr-m{i}">{m}</div>' for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()))
scenes[s] = scene_file(s, f"""
#yr-cnt {{ position:absolute; left:0; right:0; top:470px; text-align:center; }}
#yr-cnt .big {{ font-size:124px; color:{C['red']}; }}
""", f"""
  {cal}
  <div id="yr-cnt"><div style="font-size:60px">1 year ≈</div><div id="yr-n" class="big">100,000</div><div style="font-size:60px">beats</div></div>
""", f"""
for (let i=0;i<12;i++) pop("#yr-m"+i, {max(ty-0.2,0):.2f}+i*0.06);
rise("#yr-cnt", {ty:.2f}); count("#yr-n", 100000, 37000000, {ty+0.1:.2f}, {t37-ty+0.9:.2f}, fmtInt);
""")

# 9 LIFE — 80 years, nearly 3 billion
s = "life"; t80 = aw(s, "eighty years"); t3 = aw(s, "nearly three")
X0, X1, Y = 110, 970, 440
ticks = "".join(f'<path d="M{X0+(X1-X0)*y/80:.1f},{Y-(26 if y%20==0 else 14)} L{X0+(X1-X0)*y/80:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{X0+(X1-X0)*y/80:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 20 == 0 else "") for y in range(0, 81, 5))
scenes[s] = scene_file(s, f"""
#lf-bar {{ position:absolute; left:{X0}px; top:{Y-70}px; width:{X1-X0}px; height:60px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-seg {{ position:absolute; left:0; top:0; height:100%; width:100%; transform-origin:0 50%; }}
#lf-lab {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#lf-lab .big {{ font-size:112px; color:{C['red']}; }}
""", f"""
  <div id="lf-title" class="h1" style="top:160px;font-size:76px">A whole life: <span class="hl">80 years</span></div>
  <div id="lf-bar"><div id="lf-seg" class="hatch-r"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="520" data-layout-ignore>{ticks}</svg>
  <div id="lf-lab"><div id="lf-n" class="big">≈ 3,000,000,000</div><div style="font-size:60px;margin-top:14px"><span class="hl">nearly 3 billion beats!</span></div></div>
""", f"""
rise("#lf-title", 0.0); rise("#lf-bar", 0.1);
tl.fromTo("#lf-seg", {{scaleX:0}}, {{scaleX:1, duration:1.4, ease:"power1.inOut"}}, {t80-0.2:.2f});
pop("#lf-lab", {t3:.2f}, {{from:{{scale:0.3}}, to:{{duration:0.45}}}});
tl.fromTo("#lf-n", {{scale:1}}, {{scale:1.08, duration:0.15, yoyo:true, repeat:1}}, {t3+0.6:.2f});
""")

# 10 KIDS — kids' hearts beat faster
s = "kids"; thi = aw(s, "probably higher"); tch = aw(s, "children's hearts"); tad = aw(s, "adult hearts")
scenes[s] = scene_file(s, f"""
#kd-kid {{ position:absolute; left:170px; top:380px; width:300px; text-align:center; }}
#kd-ad {{ position:absolute; left:600px; top:330px; width:340px; text-align:center; }}
#kd-kid .lab, #kd-ad .lab {{ font-size:54px; margin-top:10px; }}
#kd-up {{ position:absolute; left:0; right:0; top:160px; }}
""", f"""
  <div id="kd-up" class="h1" style="font-size:76px">Real total: <span class="hl">even higher</span> ↑</div>
  <div id="kd-kid">{heart_svg('kd-hk', 190)}<div class="lab red">kids: faster!</div></div>
  <div id="kd-ad">{heart_svg('kd-ha', 290, '#F28B82')}<div class="lab">adults</div></div>
""", f"""
{BEAT}
rise("#kd-up", {thi-0.3:.2f}); pop("#kd-kid", {tch:.2f}); pop("#kd-ad", {tad-0.3:.2f});
for (let i=0;i<10;i++) beat("#kd-hk", {tch+0.3:.2f}+i*0.42, 1.18);
for (let i=0;i<4;i++) beat("#kd-ha", {tad:.2f}+i*0.85);
""")

# 11 REST — exercise -> slower resting beat
s = "rest"; tb = aw(s, "bonus tip"); tex = aw(s, "regular exercise"); tst = aw(s, "stronger"); tsl = aw(s, "more slowly")
scenes[s] = scene_file(s, f"""
#rs-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#rs-db {{ position:absolute; left:140px; top:330px; }}
#rs-arrow {{ position:absolute; left:480px; top:420px; }}
#rs-heart {{ position:absolute; left:660px; top:330px; }}
#rs-lab {{ position:absolute; left:0; right:0; top:690px; text-align:center; font-size:60px; }}
""", f"""
  <div id="rs-tag"><span class="chip">BONUS TIP</span></div>
  <svg id="rs-db" width="320" height="200" viewBox="0 0 160 100" data-layout-ignore>
    <path d="M40,50 L120,50" stroke="{K}" stroke-width="8" stroke-linecap="round"/>
    <path d="M18,22 Q30,20 40,22 L40,78 Q30,80 18,78 Z M120,22 Q130,20 142,22 L142,78 Q130,80 120,78 Z" fill="{C['blue']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>
    <path d="M6,34 L18,34 L18,66 L6,66 Z M142,34 L154,34 L154,66 L142,66 Z" fill="{C['blue']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></svg>
  <svg id="rs-arrow" width="160" height="60" data-layout-ignore><path id="rs-ar" d="M8,30 Q80,20 140,30 M118,12 L144,30 L118,48" {WS}/></svg>
  <div id="rs-heart">{heart_svg('rs-h', 260)}</div>
  <div id="rs-lab"><span class="hl">stronger heart</span> = <span class="blue">calmer beat</span> at rest</div>
""", f"""
{BEAT}
pop("#rs-tag .chip", {tb:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
pop("#rs-db", {tex:.2f}); tl.fromTo("#rs-db", {{y:0}}, {{y:-40, duration:0.25, yoyo:true, repeat:3, ease:"sine.inOut"}}, {tex+0.35:.2f});
draw("#rs-ar", {tst-0.3:.2f}, 0.35); pop("#rs-heart", {tst:.2f});
for (let i=0;i<4;i++) beat("#rs-h", {tsl:.2f}+i*1.1, 1.1);
rise("#rs-lab", {tsl-0.2:.2f});
""")

# 12 OUTRO
s = "outro"; ta = aw(s, "about three"); tkg = aw(s, "kept you"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">3 billion beats</span></div>
  <div id="ou-b" class="h1">…and every single one kept you going.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {ta:.2f}); rise("#ou-b", {ta+0.7:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "a million"), 2.8)
wave(g("intro", "I'm Max"))
point(g("feel", "two fingers"), 1.4)
point(g("rate", "call it seventy"), 1.2)
point(g("hour", "four thousand"), 1.2)
point(g("day", "one hundred thousand"), 1.2)
wow(g("year", "thirty seven"), 1.2)
wow(g("life", "nearly three"), 1.6)
think(SC["kids"]["start"] + 0.05, g("kids", "children's hearts"))
point(g("rest", "regular exercise"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "heart beat"), 0.35), ("pop.mp3", A("guess", "a million"), 0.5), ("pop.mp3", A("guess", "a hundred million"), 0.5),
        ("pop.mp3", A("guess", "or billions"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("feel", "steady thump"), 0.6),
        ("click.mp3", A("rate", "call it seventy") + 0.3, 0.45), ("pop.mp3", A("year", "thirty seven") + 0.8, 0.5),
        ("impact-bass-1.mp3", A("life", "nearly three"), 0.45), ("pop.mp3", A("rest", "bonus tip"), 0.5),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
