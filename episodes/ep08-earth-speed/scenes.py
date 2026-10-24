# MAX WISE ep08 — You're sitting still, so how fast are you moving?  Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
SEA = "#BFE3F7"; LAND = "#CFE8B8"

def globe_svg(pid, r=200, rings=False):
    """doodle Earth; #pid-eq dashed equator, #pid-land continents group, optional latitude rings #pid-r1/#pid-r2"""
    d = 2 * r + 40; c = r + 20
    ring = ""
    if rings:
        for k, lat in [(1, 0.62), (2, 0.92)]:
            yy = c - r * lat; rx = r * (1 - lat * lat) ** 0.5
            ring += f'<ellipse id="{pid}-r{k}" cx="{c}" cy="{yy:.0f}" rx="{rx:.0f}" ry="{rx*0.16:.0f}" fill="none" stroke="{C["blue"]}" stroke-width="6" stroke-dasharray="14 10"/>'
    return f'''<svg id="{pid}" width="{d}" height="{d}" viewBox="0 0 {d} {d}" style="overflow:visible" data-layout-ignore>
  <circle cx="{c}" cy="{c}" r="{r}" fill="{SEA}" {WSF}/>
  <g id="{pid}-land">
    <path d="M{c-r*0.7:.0f},{c-r*0.35:.0f} Q{c-r*0.4:.0f},{c-r*0.7:.0f} {c-r*0.05:.0f},{c-r*0.45:.0f} Q{c+r*0.1:.0f},{c-r*0.1:.0f} {c-r*0.25:.0f},{c+r*0.05:.0f} Q{c-r*0.55:.0f},{c+r*0.2:.0f} {c-r*0.7:.0f},{c-r*0.35:.0f} Z" fill="{LAND}" stroke="{K}" stroke-width="4"/>
    <path d="M{c+r*0.25:.0f},{c+r*0.15:.0f} Q{c+r*0.6:.0f},{c-r*0.05:.0f} {c+r*0.7:.0f},{c+r*0.3:.0f} Q{c+r*0.6:.0f},{c+r*0.7:.0f} {c+r*0.35:.0f},{c+r*0.6:.0f} Q{c+r*0.15:.0f},{c+r*0.4:.0f} {c+r*0.25:.0f},{c+r*0.15:.0f} Z" fill="{LAND}" stroke="{K}" stroke-width="4"/></g>
  <ellipse id="{pid}-eq" cx="{c}" cy="{c}" rx="{r}" ry="{r*0.16:.0f}" fill="none" stroke="{C['red']}" stroke-width="6" stroke-dasharray="16 10"/>
  {ring}
</svg>'''

def gauge_svg(pid, w=420, label="mph"):
    """speedometer; rotate #pid-needle (svgOrigin 150 160) from -90 (left) to +90 (right)"""
    ticks = "".join(f'<path d="M150,40 L150,{58 if i%2==0 else 50}" transform="rotate({-90+i*18} 150 160)" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for i in range(11))
    return f'''<svg id="{pid}" width="{w}" height="{w*0.66:.0f}" viewBox="0 0 300 198" data-layout-ignore>
  <path d="M20,165 Q20,30 150,28 Q280,30 280,165 Z" fill="#fff" {WSF}/>
  <path d="M40,160 Q44,52 150,48" stroke="{C['hi']}" stroke-width="16" fill="none" stroke-linecap="round" opacity=".9"/>
  {ticks}
  <g id="{pid}-needle"><path d="M150,160 L150,62" stroke="{C['red']}" stroke-width="8" stroke-linecap="round"/></g>
  <circle cx="150" cy="160" r="12" fill="{K}"/>
  <text x="150" y="192" text-anchor="middle" font-family="Gochi Hand" font-size="30" fill="{K}">{label}</text></svg>'''

# 1 HOOK — sitting still?
s = "hook"; tst = aw(s, "perfectly still"); thf = aw(s, "how fast"); tmv = aw(s, "really moving")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:84px; }}
#hk-chair {{ position:absolute; left:120px; top:520px; }}
#hk-g {{ position:absolute; left:560px; top:560px; }}
#hk-zero {{ position:absolute; left:560px; top:850px; width:420px; text-align:center; font-size:62px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">Sitting <span class="hl">perfectly still</span>…<br>how fast are you moving?</div>
  <svg id="hk-chair" width="380" height="330" viewBox="0 0 190 165" data-layout-ignore>
    <path d="M30,40 Q30,14 60,14 L130,14 Q160,14 160,40 L160,100 L30,100 Z" fill="#FFC9C2" {WSF}/>
    <path d="M12,80 Q12,64 28,64 L40,64 L40,128 L12,128 Z M150,64 L162,64 Q178,64 178,80 L178,128 L150,128 Z" fill="#FFC9C2" {WSF}/>
    <path d="M40,100 L150,100 L150,128 L40,128 Z" fill="#fff" {WSF}/>
    <path d="M24,128 L22,156 M166,128 L168,156" {WS}/></svg>
  <div id="hk-g">{gauge_svg('hk-gg', 420)}</div>
  <div id="hk-zero" class="big">0 mph… right?</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tst-0.6:.2f}); pop("#hk-chair", {tst:.2f});
tl.set("#hk-gg-needle", {{rotation:-90, svgOrigin:"150 160"}}, 0);
pop("#hk-g", {thf-0.3:.2f}); pop("#hk-zero", {thf:.2f}, {{from:{{rotation:6}}, to:{{rotation:-2}}}});
tl.to("#hk-gg-needle", {{rotation:-78, duration:0.08, yoyo:true, repeat:7, ease:"sine.inOut"}}, {tmv:.2f});
""")

# 2 GUESS — zero / car / rocket
s = "guess"; tg = aw(s, "take a guess"); t0 = aw(s, "zero"); tc = aw(s, "as fast as a car"); tr = aw(s, "or faster")
notes = [("zero", "Zero?", -6, 110, C['hi']), ("car", "A car?", 4, 405, "#BFE3F7"), ("rock", "A<br>rocket?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:60px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore><path id="gs-ar" d="M200,720 Q540,820 860,700" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="16 12"/>
    <path id="gs-ah" d="M830,690 L862,700 L846,730" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" opacity="0"/></svg>
  <div id="gs-sub" class="h2" style="top:800px">slow ··· fast</div>
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-zero", {t0:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-car", {tc:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-rock", {tr:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
draw("#gs-ar", {tr+0.2:.2f}, 0.5); tl.to("#gs-ah", {{opacity:1, duration:0.1}}, {tr+0.65:.2f}); rise("#gs-sub", {tr+0.5:.2f});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tbu = aw(s, "buckle up")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Buckle up!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
pop("#in-sub", {tbu:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 4 SPIN — one lap a day, 25,000 miles
s = "spin"; tsp = aw(s, "spins"); tday = aw(s, "once a day"); tmid = aw(s, "around its middle"); t25 = aw(s, "twenty five thousand")
scenes[s] = scene_file(s, f"""
#sp-gl {{ position:absolute; left:290px; top:260px; }}
#sp-dot {{ position:absolute; left:0; top:0; }}
#sp-lab {{ position:absolute; left:440px; top:770px; width:560px; text-align:center; }}
#sp-lab span {{ font-size:78px; }}
#sp-day {{ position:absolute; left:760px; top:250px; font-size:54px; transform:rotate(6deg); }}
""", f"""
  <div id="sp-title" class="h1" style="top:150px;font-size:74px">Earth <span class="hl">spins</span></div>
  <div id="sp-gl">{globe_svg('sp-g', 220)}</div>
  <svg id="sp-dot" class="abs" width="{W}" height="900" data-layout-ignore>
    <path id="sp-arc" d="M300,500 Q300,440 360,420" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="sp-arh" d="M340,410 L362,420 L350,442" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <circle id="sp-pt" cx="0" cy="0" r="16" fill="{C['red']}" stroke="{K}" stroke-width="4" style="opacity:0"/></svg>
  <div id="sp-day" class="pill">1 lap / day</div>
  <div id="sp-lab"><span class="pill">≈ 25,000 miles</span></div>
""", f"""
rise("#sp-title", 0.0); pop("#sp-gl", 0.1);
tl.fromTo("#sp-g-land", {{x:-30}}, {{x:30, duration:{SC[s]['slot']-0.4:.2f}, ease:"none"}}, {tsp:.2f});
draw("#sp-arc", {tsp:.2f}, 0.3); tl.fromTo("#sp-arh", {{opacity:0}}, {{opacity:1, duration:0.1}}, {tsp+0.3:.2f});
pop("#sp-day", {tday:.2f}, {{from:{{rotation:20}}, to:{{rotation:6}}}});
tl.to("#sp-pt", {{opacity:1, duration:0.1}}, {tmid:.2f});
const o = {{a:0}}; const pt = document.querySelector("#sp-pt");
const place = () => {{ const a=o.a*Math.PI/180; pt.setAttribute("cx", 530+220*Math.cos(a)); pt.setAttribute("cy", 500+35*Math.sin(a)); }}; place();
tl.to(o, {{a:720, duration:{SC[s]['slot']-tmid-0.3:.2f}, ease:"none", onUpdate:place}}, {tmid:.2f});
pop("#sp-lab span", {t25:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 5 EQUATOR — 25,000 / 24 = ~1,000 mph; faster than a jet
s = "equator"; tdv = aw(s, "divide"); tgr = aw(s, "the ground"); t1k = aw(s, "one thousand"); tjet = aw(s, "faster than a jet")
scenes[s] = scene_file(s, f"""
#eq-card {{ left:110px; top:170px; width:860px; height:330px; }}
#eq-l1 {{ position:absolute; left:0; right:0; top:40px; text-align:center; font-size:84px; }}
#eq-l2 {{ position:absolute; left:0; right:0; top:180px; text-align:center; font-size:96px; color:{C['red']}; }}
#eq-race {{ position:absolute; left:120px; top:560px; }}
#eq-pf {{ position:absolute; left:640px; top:880px; font-size:60px; color:{C['red']}; }}
""", f"""
  <div id="eq-card" class="card">
    <div id="eq-l1" class="big">25,000 mi ÷ 24 h</div>
    <div id="eq-l2" class="big">≈ <span class="hl">1,000 mph</span></div></div>
  <svg id="eq-race" width="860" height="300" viewBox="0 0 860 300" data-layout-ignore>
    <path d="M0,250 Q430,240 860,252" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g id="eq-grd"><path d="M10,210 L240,210" stroke="{C['red']}" stroke-width="12" stroke-linecap="round"/><path d="M220,190 L250,210 L220,230" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="268" y="222" font-family="Gochi Hand" font-size="40" fill="{K}">ground</text></g>
    <g id="eq-jet"><path d="M20,90 Q90,70 170,84 L200,90 L170,98 Q90,108 20,92 Z" fill="#fff" {WSF}/>
      <path d="M80,88 L120,40 L138,40 L118,88 M80,96 L110,130 L126,130 L112,96 M24,90 L10,62 L30,62 L46,86" fill="#fff" {WSF}/>
      <text x="214" y="102" font-family="Gochi Hand" font-size="40" fill="{K}">jet</text></g></svg>
  <div id="eq-pf" class="big">ZOOM!</div>
""", f"""
pop("#eq-card", {tdv-0.1:.2f}); rise("#eq-l1", {tdv+0.1:.2f});
pop("#eq-l2", {t1k:.2f});
rise("#eq-race", {tgr:.2f});
tl.fromTo("#eq-grd", {{x:0}}, {{x:420, duration:1.6, ease:"power1.in"}}, {tjet-0.4:.2f});
tl.fromTo("#eq-jet", {{x:0}}, {{x:200, duration:1.6, ease:"power1.in"}}, {tjet-0.4:.2f});
pop("#eq-pf", {tjet+0.4:.2f}, {{from:{{rotation:-16}}, to:{{rotation:-6}}}});
""")

# 6 POLES — smaller circles, New York ~800 mph
s = "poles"; tsm = aw(s, "gets smaller"); tny = aw(s, "new york"); t800 = aw(s, "eight hundred")
scenes[s] = scene_file(s, f"""
#pl-gl {{ position:absolute; left:90px; top:250px; }}
#pl-l0 {{ position:absolute; left:580px; top:520px; font-size:46px; white-space:nowrap; }}
#pl-l1 {{ position:absolute; left:580px; top:300px; font-size:46px; white-space:nowrap; }}
#pl-ny {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="pl-title" class="h1" style="top:150px;font-size:72px">Smaller circle = <span class="hl">slower</span></div>
  <div id="pl-gl">{globe_svg('pl-g', 210, rings=True)}</div>
  <svg id="pl-ny" class="abs" width="{W}" height="900" data-layout-ignore>
    <path id="pl-ld1" d="M445,366 Q510,345 575,335" stroke="{K}" stroke-width="4" fill="none" stroke-dasharray="8 7"/>
    <circle id="pl-nyd" cx="432" cy="370" r="13" fill="{C['blue']}" stroke="{K}" stroke-width="4" style="opacity:0"/>
    <path id="pl-ld0" d="M532,484 Q555,515 575,548" stroke="{K}" stroke-width="4" fill="none" stroke-dasharray="8 7"/></svg>
  <div id="pl-l0" class="pill red">equator ≈ 1,000 mph</div>
  <div id="pl-l1" class="pill blue">New York ≈ 800 mph</div>
""", f"""
rise("#pl-title", 0.0); pop("#pl-gl", 0.1);
draw("#pl-ld0", 0.4, 0.3); pop("#pl-l0", 0.6);
tl.fromTo("#pl-g-r1, #pl-g-r2", {{opacity:0, scale:1.6, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.5, ease:"back.out(1.6)", stagger:0.2}}, {tsm-0.3:.2f});
pop("#pl-nyd", {tny:.2f}); draw("#pl-ld1", {tny+0.15:.2f}, 0.3); pop("#pl-l1", {t800:.2f});
""")

# 7 ORBIT — pull out to the Sun; ~600 million miles, 1 year
s = "orbit"; trc = aw(s, "racing around"); tsun = aw(s, "Sun"); tlap = aw(s, "one lap"); t600 = aw(s, "six hundred million"); tyr = aw(s, "takes a year")
scenes[s] = scene_file(s, f"""
#ob-cam {{ position:absolute; left:0; top:0; width:{W}px; height:980px; transform-origin:540px 520px; }}
#ob-big {{ position:absolute; left:290px; top:270px; }}
#ob-lab {{ position:absolute; left:440px; top:820px; width:560px; text-align:center; }}
#ob-lab span {{ font-size:66px; }}
#ob-yr {{ position:absolute; left:780px; top:180px; font-size:56px; transform:rotate(5deg); }}
""", f"""
  <div id="ob-cam">
    <svg class="abs" style="left:0;top:0" width="{W}" height="980" data-layout-ignore>
      <ellipse id="ob-path" cx="540" cy="520" rx="400" ry="230" fill="none" stroke="{C['blue']}" stroke-width="6" stroke-dasharray="18 12"/>
      <g id="ob-sun">{"".join(f'<path d="M540,{520-118} L540,{520-150}" transform="rotate({i*30} 540 520)" stroke="{C["red"]}" stroke-width="7" stroke-linecap="round"/>' for i in range(12))}
        <circle cx="540" cy="520" r="96" fill="{C['hi']}" {WSF}/>
        <text x="540" y="535" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{K}">Sun</text></g>
      <g id="ob-earth"><circle cx="0" cy="0" r="30" fill="{SEA}" {WSF}/><path d="M-14,-8 Q0,-22 10,-6 Q2,6 -14,-8 Z" fill="{LAND}" stroke="{K}" stroke-width="3"/></g></svg>
  </div>
  <div id="ob-big">{globe_svg('ob-g', 220)}</div>
  <div id="ob-yr" class="pill">1 lap = 1 year</div>
  <div id="ob-lab"><span class="pill blue">≈ 600 million miles</span></div>
""", f"""
pop("#ob-big", 0.0);
tl.to("#ob-big", {{scale:0.12, x:400, y:0, opacity:0, duration:0.7, ease:"power2.inOut"}}, {trc:.2f});
tl.fromTo("#ob-cam", {{scale:2.4, opacity:0}}, {{scale:1, opacity:1, duration:0.8, ease:"power2.out"}}, {trc+0.1:.2f});
tl.set("#ob-path", {{opacity:1}}, 0);
draw("#ob-path", {tlap:.2f}, 1.2);
const e = document.querySelector("#ob-earth"); const o = {{a:0}};
const place = () => {{ const a=o.a*Math.PI/180; e.setAttribute("transform", `translate(${{540+400*Math.cos(a)}},${{520+230*Math.sin(a)}})`); }}; place();
tl.to(o, {{a:-300, duration:{SC[s]['slot']-trc-0.5:.2f}, ease:"none", onUpdate:place}}, {trc+0.3:.2f});
pop("#ob-lab span", {t600:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#ob-yr", {tyr:.2f}, {{from:{{rotation:20}}, to:{{rotation:5}}}});
""")

# 8 FAST — counter to 67,000 mph; 1,000+ miles a minute
s = "fast"; t67 = aw(s, "sixty seven thousand"); tmin = aw(s, "over a thousand"); tev = aw(s, "every minute")
scenes[s] = scene_file(s, f"""
#fs-g {{ position:absolute; left:270px; top:250px; }}
#fs-num {{ position:absolute; left:0; right:0; top:590px; text-align:center; font-size:150px; }}
#fs-sub {{ position:absolute; left:420px; top:820px; width:600px; text-align:center; }}
#fs-sub span {{ font-size:54px; }}
""", f"""
  <div id="fs-title" class="h1" style="top:150px;font-size:72px">Around the Sun</div>
  <div id="fs-g">{gauge_svg('fs-gg', 540)}</div>
  <div id="fs-num" class="big"><span id="fs-n" class="red">0</span> mph</div>
  <div id="fs-sub"><span class="pill blue">1,000+ miles every minute</span></div>
""", f"""
rise("#fs-title", 0.0); pop("#fs-g", 0.1); tl.set("#fs-gg-needle", {{rotation:-90, svgOrigin:"150 160"}}, 0);
rise("#fs-num", 0.2);
tl.to("#fs-gg-needle", {{rotation:86, duration:1.6, ease:"power2.out"}}, {t67-0.6:.2f});
tl.to("#fs-gg-needle", {{rotation:80, duration:0.06, yoyo:true, repeat:9}}, {t67+1.0:.2f});
count("#fs-n", 0, 67000, {t67-0.6:.2f}, 1.6, fmtInt);
pop("#fs-sub span", {tmin:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.fromTo("#fs-sub span", {{scale:1}}, {{scale:1.1, duration:0.14, yoyo:true, repeat:1}}, {tev:.2f});
""")

# 9 FEEL — everything moves with you; you feel only changes
s = "feel"; tw = aw(s, "why don't"); tair = aw(s, "the air"); tch = aw(s, "your chair"); tgd = aw(s, "the ground"); tmw = aw(s, "move with you"); tsu = aw(s, "speeding up"); tsl = aw(s, "slowing down")
rows = [("fl-a", "air", 300, tair), ("fl-c", "chair", 430, tch), ("fl-g", "ground", 560, tgd)]
rh = "".join(f'<div id="{i}" class="abs" style="left:110px;top:{y}px;width:860px;height:100px;opacity:0"><div class="big" style="position:absolute;left:0;top:14px;width:220px;font-size:60px">{lab}</div>'
             f'<svg class="abs" style="left:240px;top:10px" width="600" height="80" data-layout-ignore><path d="M10,40 Q300,30 560,42" stroke="{C["blue"]}" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M530,16 L572,42 L530,66" stroke="{C["blue"]}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>' for i, lab, y, _ in rows)
scenes[s] = scene_file(s, f"""
#fl-q {{ top:150px; font-size:72px; }}
#fl-same {{ position:absolute; left:440px; top:700px; width:560px; text-align:center; }}
#fl-same span {{ font-size:56px; }}
#fl-whoa {{ position:absolute; left:0; right:0; top:330px; text-align:center; font-size:170px; color:{C['red']}; opacity:0; }}
#fl-feel {{ position:absolute; left:440px; top:600px; width:560px; text-align:center; opacity:0; }}
#fl-feel span {{ font-size:54px; }}
""", f"""
  <div id="fl-q" class="h1">Why don't you <span class="hl">feel it</span>?</div>
  <div id="fl-rows">{rh}</div>
  <div id="fl-same"><span class="pill">all the same speed</span></div>
  <div id="fl-whoa" class="big">WHOA!</div>
  <div id="fl-feel"><span class="pill red">you feel only changes</span></div>
""", f"""
rise("#fl-q", {tw-0.1:.2f});
{"".join(f'tl.fromTo("#{i}", {{opacity:0, x:-60}}, {{opacity:1, x:0, duration:0.3, ease:"back.out(1.6)"}}, {t:.2f});' for i, _, _, t in rows)}
pop("#fl-same span", {tmw:.2f});
tl.to("#fl-rows, #fl-same", {{opacity:0, y:-20, duration:0.25}}, {tsu-0.3:.2f});
tl.fromTo("#fl-whoa", {{opacity:0, scale:0.4, rotation:-12}}, {{opacity:1, scale:1, rotation:-4, duration:0.3, ease:"back.out(2.5)"}}, {tsu:.2f});
tl.to("#fl-whoa", {{x:24, duration:0.07, yoyo:true, repeat:5}}, {tsl:.2f});
pop("#fl-feel", {tsu+0.4:.2f});
""")

# 10 GALAXY — pull out: Sun on a galaxy arm, ~450,000 mph
s = "galaxy"; tgx = aw(s, "galaxy"); t450 = aw(s, "four hundred fifty")
import math
arms = ""
for a0 in (0, 180):
    pts = []
    for k in range(60):
        th = k * 0.09; rr = 30 + k * 6.2
        pts.append(f"{540 + rr*math.cos(th + math.radians(a0)):.1f},{520 + 0.6*rr*math.sin(th + math.radians(a0)):.1f}")
    arms += f'<path id="gx-arm{a0}" d="M{" L".join(pts)}" stroke="{C["blue"]}" stroke-width="9" fill="none" stroke-linecap="round"/>'
rnd_g = random.Random(8)
stars = "".join(f'<circle cx="{rnd_g.uniform(150,930):.0f}" cy="{rnd_g.uniform(300,740):.0f}" r="{rnd_g.uniform(3,6):.1f}" fill="{C["pencil"]}"/>' for _ in range(40))
sx, sy = 540 + 340*math.cos(5.6), 520 + 0.6*340*math.sin(5.6)
scenes[s] = scene_file(s, f"""
#gx-cam {{ position:absolute; left:0; top:0; width:{W}px; height:980px; transform-origin:{sx:.0f}px {sy:.0f}px; }}
#gx-lab {{ position:absolute; left:440px; top:800px; width:560px; text-align:center; }}
#gx-lab span {{ font-size:66px; }}
""", f"""
  <div id="gx-title" class="h1" style="top:150px;font-size:72px">Our <span class="hl">galaxy</span></div>
  <div id="gx-cam"><svg class="abs" style="left:0;top:0" width="{W}" height="980" data-layout-ignore>
    {stars}{arms}
    <ellipse cx="540" cy="520" rx="60" ry="38" fill="{C['hi']}" {WSF}/>
    <g id="gx-sun"><circle cx="{sx:.0f}" cy="{sy:.0f}" r="22" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>
      <path d="M{sx-40:.0f},{sy-50:.0f} L{sx-14:.0f},{sy-24:.0f}" stroke="{K}" stroke-width="4"/>
      <text x="{sx-50:.0f}" y="{sy-60:.0f}" text-anchor="middle" font-family="Gochi Hand" font-size="42" fill="{K}">Sun</text></g></svg></div>
  <div id="gx-lab"><span class="pill red">≈ 450,000 mph</span></div>
""", f"""
rise("#gx-title", {tgx-0.3:.2f});
tl.fromTo("#gx-cam", {{scale:3.2}}, {{scale:1, duration:1.4, ease:"power2.inOut"}}, 0.1);
draw("#gx-arm0", 0.1, 1.2); draw("#gx-arm180", 0.1, 1.2);
tl.fromTo("#gx-cam svg", {{rotation:0, svgOrigin:"540 520"}}, {{rotation:-8, duration:{SC[s]['slot']:.2f}, ease:"none"}}, 0);
pop("#gx-lab span", {t450:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 11 OUTRO
s = "outro"; tss = aw(s, "sitting still"); tzm = aw(s, "zooming"); t67 = aw(s, "sixty seven"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:76px; }}
#ou-b {{ position:absolute; left:0; right:0; top:300px; text-align:center; }}
#ou-b .big {{ font-size:120px; color:{C['red']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">Sitting still? <span class="hl">Zooming!</span></div>
  <div id="ou-b"><div class="big">67,000 mph</div><div style="font-size:50px;color:{C['muted']}">around the Sun</div></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
rise("#ou-a", {tss:.2f}); pop("#ou-b", {t67:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "so how"), SC["guess"]["start"] + 0.2)
point(g("guess", "zero"), 3.0)
wave(g("intro", "I'm Max"))
point(g("spin", "twenty five"), 1.4)
point(g("equator", "one thousand"), 1.2)
wow(g("equator", "faster than"), 1.2)
point(g("poles", "eight hundred"), 1.2)
point(g("orbit", "six hundred"), 1.4)
wow(g("fast", "sixty seven"), 1.6)
think(g("feel", "so why"), g("feel", "the air"))
wow(g("feel", "speeding up"), 1.2)
wow(g("galaxy", "four hundred"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("click-soft.mp3", A("hook", "perfectly still"), 0.5), ("ping.mp3", A("hook", "how fast"), 0.35),
        ("pop.mp3", A("guess", "zero"), 0.5), ("pop.mp3", A("guess", "as fast"), 0.5), ("pop.mp3", A("guess", "or faster"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("spin", "twenty five"), 0.5),
        ("pop.mp3", A("equator", "one thousand"), 0.5), ("whoosh-short.mp3", A("equator", "faster than") - 0.3, 0.4),
        ("click.mp3", A("poles", "eight hundred"), 0.45), ("riser.mp3", A("fast", "sixty seven") - 0.6, 0.3),
        ("impact-bass-1.mp3", A("fast", "sixty seven") + 1.0, 0.45), ("impact-bass-2.mp3", A("feel", "speeding up"), 0.4),
        ("pop.mp3", A("galaxy", "four hundred"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
