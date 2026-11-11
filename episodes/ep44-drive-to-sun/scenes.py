# MAX WISE ep44 — If you could drive a car to the Sun, how long would it take?
# Kit: ink / morph / along helpers + one three.js scene (hook: Earth, Sun and a tiny car, camera pull-back).
# Sources: NASA Science "Sun: Facts" (about 150 million km / 93 million miles); NASA "Cosmic Distances" (1 AU, ~8 light-minutes).
# Maths: 149.6e6 km / 100 km/h = 1.496e6 h = 62,333 d = 170.7 yr ~ 170; jet 900 km/h -> 18.96 ~ 19 yr; light 499 s ~ 8 min.
# === SCENES ===
import math as _m, random as _r
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SUN = "#FFC93C"; SUN2 = "#F59E2A"; SEA = "#7FB8E6"; LAND = "#9BD08F"
SIM = """
const sim = (dur, fn) => { const st={t:0}; tl.fromTo(st, {t:0}, {t:dur, duration:dur, ease:"none", onUpdate:()=>fn(st.t)}, 0); fn(0); };
"""
def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.92)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 26px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff;white-space:nowrap">{txt}</span></div>')
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
def circ(cx, cy, r):  # one sub-path circle, starts at top, clockwise
    return f"M{cx},{cy-r} A{r},{r} 0 1 1 {cx-0.1:.1f},{cy-r}"
def earth(cx, cy, r, idn=""):
    i = f' id="{idn}"' if idn else ""
    return (f'<g{i}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{SEA}" stroke="{K}" stroke-width="5"/>'
            f'<path d="M{cx-r*0.5:.0f},{cy-r*0.3:.0f} q{r*0.3:.0f},-{r*0.4:.0f} {r*0.6:.0f},-{r*0.1:.0f} q-{r*0.1:.0f},{r*0.4:.0f} -{r*0.5:.0f},{r*0.5:.0f} z" fill="{LAND}"/>'
            f'<path d="M{cx+r*0.1:.0f},{cy+r*0.3:.0f} q{r*0.3:.0f},-{r*0.2:.0f} {r*0.5:.0f},{r*0.1:.0f} q-{r*0.2:.0f},{r*0.3:.0f} -{r*0.5:.0f},{r*0.2:.0f} z" fill="{LAND}"/></g>')
def sun(cx, cy, r, idn="", rays=True):
    i = f' id="{idn}"' if idn else ""
    ry = ""
    if rays:
        for k in range(12):
            a = k * _m.pi / 6
            ry += f'<path d="M{cx+(r+18)*_m.cos(a):.0f},{cy+(r+18)*_m.sin(a):.0f} L{cx+(r+60)*_m.cos(a):.0f},{cy+(r+60)*_m.sin(a):.0f}" stroke="{SUN2}" stroke-width="10" stroke-linecap="round"/>'
    return f'<g{i}>{ry}<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SUN}" stroke="{K}" stroke-width="6"/></g>'
def car(idn, sc=1.0, extra=""):  # car drawn around 0,0 (for along)
    return (f'<g id="{idn}" {extra}><g transform="scale({sc})">'
            f'<path d="M-46,4 L-46,-14 L-26,-16 L-14,-34 L20,-34 L32,-16 L46,-12 L46,4 Z" fill="{C["red"]}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M-10,-30 L-10,-18 L4,-18 L4,-30 Z M10,-30 L10,-18 L24,-18 L18,-30 Z" fill="#DFF1FB" stroke="{K}" stroke-width="3"/>'
            f'<circle cx="-24" cy="6" r="11" fill="{K}"/><circle cx="26" cy="6" r="11" fill="{K}"/>'
            f'<circle cx="-24" cy="6" r="4" fill="#FFFFFF"/><circle cx="26" cy="6" r="4" fill="#FFFFFF"/></g></g>')

# 1 HOOK — 3D: Earth, big Sun, a tiny car sets off; camera pulls back
s = "hook"; tcar = aw(s, "car"); tsun = aw(s, "the Sun"); tns = aw(s, "no stops"); thw = aw(s, "how long"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q0 {{ top:160px; font-size:76px; }}
#hk-q {{ top:150px; font-size:80px; }}
#hk-cv {{ position:absolute; left:40px; top:380px; width:1000px; height:560px; }}
#hk-qm {{ position:absolute; left:470px; top:330px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-q0" class="h1">Drive a <span class="hl">car</span> to the Sun…</div>
  <div id="hk-q" class="h1" style="opacity:0">How <span class="hl">long</span> would it take?</div>
  <canvas id="hk-cv" width="1000" height="560"></canvas>
  <div id="hk-qm">?</div>
""", J("""
const S = T3.stage("#hk-cv", 1000, 560, 34);
const earth = T3.inked(new THREE.SphereGeometry(0.42, 40, 28), 0x4F9BE0, 0.05); earth.position.set(-2.6, 0, 0); S.scene.add(earth);
const rnd = T3.seeded(7);
for (let i=0;i<7;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.42*(0.25+rnd()*0.2), 14, 10), T3.toon(0x7CC46A));
  m.position.setFromSphericalCoords(0.41, 0.6+rnd()*1.9, rnd()*6.28); m.scale.set(1,1,0.3); m.lookAt(0,0,0); earth.add(m); }
const sunG = T3.inked(new THREE.SphereGeometry(1.5, 48, 32), 0xFFC93C, 0.05); sunG.position.set(3.2, 0, 0); S.scene.add(sunG);
const car = new THREE.Group(); car.scale.setScalar(2.2);
const body = T3.inked(new THREE.BoxGeometry(0.26, 0.09, 0.14), 0xE0483C, 0.02); car.add(body);
const top = T3.inked(new THREE.BoxGeometry(0.14, 0.07, 0.12), 0xE0483C, 0.02); top.position.set(-0.01, 0.075, 0); car.add(top);
S.scene.add(car);
drive(@d, t => {
  const s = t < 0.6 ? 0.6 + 0.4*gsap.parseEase("back.out(2)")(t/0.6) : 1; sunG.scale.setScalar(s); earth.scale.setScalar(s);
  earth.rotation.y = t*0.5; sunG.rotation.y = t*0.1;
  const k = Math.max(0, t - @tc); car.visible = t > @tc;
  car.position.set(-1.8 + 0.12*k, 0.1*Math.abs(Math.sin(k*9)), 0.0);
  const p = Math.min(1, t/@d); const e = p*p*(3-2*p);
  const zc = 3.0 + 4.6*e, xc = -2.1 + 2.4*e;
  S.cam.position.set(xc, 0.9 + 0.8*e, zc); S.cam.lookAt(xc, 0, 0); S.render();
});
tl.to("#hk-q0", {opacity:0, y:-20, duration:0.25}, @tq0);
rise("#hk-q", @tq);
pop("#hk-qm", @tqm, {from:{rotation:-20}, to:{rotation:8}});
""", d=d, tc=tcar, tq0=thw - 0.4, tq=thw - 0.15, tqm=thw + 0.6))

# 2 GUESS — sticky notes; calendars ink themselves
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "a month"); t2 = aw(s, "ten years"); t3 = aw(s, "century")
notes = [("a", "a month?", -6, 110, C['hi'], 62), ("b", "10 years?", 4, 405, "#BFE3F7", 62), ("c", "100+ years?", -3, 700, "#FFC9C2", 56)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:340px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding:40px 16px 0">{txt}</div>' for k, txt, r, x, bg, fs in notes)
def cal(cx, cy, cls, n):
    out = (f'<path class="{cls}" d="M{cx-55},{cy-45} L{cx+55},{cy-45} L{cx+55},{cy+50} L{cx-55},{cy+50} Z" {WS}/>'
           f'<path class="{cls}" d="M{cx-55},{cy-20} L{cx+55},{cy-20}" {WS}/>'
           f'<path class="{cls}" d="M{cx-28},{cy-58} L{cx-28},{cy-34}" {WS}/><path class="{cls}" d="M{cx+28},{cy-58} L{cx+28},{cy-34}" {WS}/>')
    for i in range(n):
        x = cx - 40 + (i % 4) * 26; y = cy - 2 + (i // 4) * 24
        out += f'<path class="{cls}" d="M{x},{y} L{x+12},{y+10}" stroke="{C["red"]}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    return out
doodles = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>' + cal(248, 600, "gs-da", 1) + cal(545, 610, "gs-db", 4)
           + cal(838, 610, "gs-dc", 8) + '</svg>')
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink(".gs-da", @ta, 0.3, {stagger:0.06}); ink(".gs-db", @tb, 0.3, {stagger:0.04}); ink(".gs-dc", @tc, 0.3, {stagger:0.03});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.35, ta=t1 + 0.2, tb=t2 + 0.2, tc=t3 - 0.1))

# 3 INTRO — logo, underline, car + buckle ink (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tbu = aw(s, "buckle up"); tma = aw(s, "math")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-bk" d="M90,540 L150,540 L150,590 L90,590 Z" stroke="{K}" stroke-width="7" fill="#DDE3EA" stroke-linejoin="round"/>
    <path class="in-bk" d="M150,565 L230,565" stroke="{C['blue']}" stroke-width="14" fill="none" stroke-linecap="round"/>
    <path class="in-bk" d="M30,565 L90,565" stroke="{C['blue']}" stroke-width="14" fill="none" stroke-linecap="round"/>
    <path class="in-mt" d="M820,560 L880,560 M850,530 L850,590" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="in-mt" d="M920,540 L980,580 M980,540 L920,580" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Buckle up!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tbu); ink(".in-bk", @tbu2, 0.3, {stagger:0.12}); ink(".in-mt", @tma, 0.3, {stagger:0.1});
""", tmw=tmw, tu=tmw + 0.3, tbu=tbu - 0.15, tbu2=tbu + 0.05, tma=tma - 0.2))

# 4 DISTANCE — Earth, road inks to the Sun, tape-measure ruler
s = "distance"; tdi = aw(s, "distance"); tsa = aw(s, "Sun is about"); t150 = aw(s, "one hundred fifty million"); tkm = aw(s, "kilometers away")
ROAD = "M180,560 C330,500 520,620 840,560"
ticks = "".join(f'<path class="ds-tk" d="M{180+i*66},{700} L{180+i*66},{700-(28 if i%5==0 else 16)}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(11))
scenes[s] = scene_file(s, f"""
#ds-title {{ top:150px; font-size:76px; }}
#ds-lab {{ position:absolute; left:0; right:0; top:740px; text-align:center; opacity:0; }}
#ds-lab .big {{ font-size:96px; color:{C['blue']}; }}
""", f"""
  <div id="ds-title" class="h1">First, the <span class="hl">distance</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {sun(1060, 560, 190, "ds-sun")}
    {earth(130, 560, 50, "ds-earth")}
    <path id="ds-road" d="{ROAD}" stroke="{C['pencil']}" stroke-width="16" fill="none" stroke-linecap="round"/>
    <path id="ds-ru" d="M180,700 L840,700" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    {ticks}
    {car("ds-car", 0.9, 'opacity="0"')}
  </svg>
  <div id="ds-lab"><span class="big">≈ 150 million km</span></div>
""", J("""
rise("#ds-title", @tdi);
pop("#ds-earth", @te, {from:{scale:0.3}, to:{}}); pop("#ds-sun", @tsa, {from:{scale:0.6}, to:{}});
ink("#ds-road", @tsa2, 0.8, {ease:"power2.inOut"});
tl.set("#ds-car", {opacity:1}, @tsa2); along("#ds-car", "#ds-road", @tsa2, @dcar, {ease:"power1.inOut", rotate:true});
ink("#ds-ru", @t150, 0.5); ink(".ds-tk", @t150b, 0.3, {stagger:0.03});
pop("#ds-lab", @t150c, {from:{rotation:-8}, to:{rotation:-2}});
""", tdi=tdi - 0.2, te=tdi + 0.1, tsa=tsa - 0.2, tsa2=tsa + 0.1, dcar=round(SC[s]["slot"] - (tsa + 0.1) - 0.3, 3), t150=t150 - 0.2, t150b=t150 + 0.2, t150c=t150 + 0.3))

# 5 SPEED — speedometer needle sweeps to 100 (simulated); ≈ 60 mph chip; highway tape
s = "speed"; tcc = aw(s, "cruise control"); t100 = aw(s, "one hundred kilometers"); t60 = aw(s, "sixty miles"); thw = aw(s, "highway"); d = SC[s]["slot"]
CX, CY, R = 540, 680, 300
def pt(v, rr):  # 0..150 mapped to left..right on upper half circle
    a = _m.pi - v / 150 * _m.pi
    return CX + rr * _m.cos(a), CY - rr * _m.sin(a)
dial = f'<path class="sp-d" d="M{CX-R},{CY} A{R},{R} 0 0 1 {CX+R},{CY}" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>'
for v in range(0, 151, 10):
    x1, y1 = pt(v, R); x2, y2 = pt(v, R - (38 if v % 50 == 0 else 20))
    dial += f'<path class="sp-d" d="M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>'
labs = "".join(f'<text x="{pt(v, R-80)[0]:.0f}" y="{pt(v, R-80)[1]+14:.0f}" text-anchor="middle" font-family="Patrick Hand" font-size="46" fill="{K}">{v}</text>' for v in (0, 50, 100, 150))
x100a, y100a = pt(95, R + 8); x100b, y100b = pt(105, R + 8)
scenes[s] = scene_file(s, f"""
#sp-title {{ top:150px; font-size:72px; }}
#sp-v {{ position:absolute; left:0; right:0; top:720px; text-align:center; opacity:0; }}
#sp-v .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="sp-title" class="h1">Cruise control: <span class="hl">on</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path d="M{CX-R+20},{CY} A{R-20},{R-20} 0 0 1 {CX+R-20},{CY} Z" fill="#FFFFFF" opacity=".8"/>
    <path id="sp-hl" d="M{x100a:.0f},{y100a:.0f} A{R+8},{R+8} 0 0 1 {x100b:.0f},{y100b:.0f}" stroke="{C['hi']}" stroke-width="30" fill="none"/>
    {dial}
    <g id="sp-lab" opacity="0">{labs}</g>
    <g id="sp-n"><path d="M{CX},{CY} L{CX-R+60},{CY}" stroke="{C['red']}" stroke-width="12" stroke-linecap="round"/><circle cx="{CX}" cy="{CY}" r="22" fill="{K}"/></g>
  </svg>
  <div id="sp-v"><span class="big">100 km/h</span></div>
  {tape("sp-mph", "≈ 60 mph", 640, 840, 3, 54, "rgba(191,227,247,.95)")}
  {tape("sp-hw", "normal highway speed", 300, 270, -2, 46)}
""", SIM + J("""
rise("#sp-title", @tcc); ink(".sp-d", @tcc2, 0.7, {stagger:0.02}); tl.to("#sp-lab", {opacity:1, duration:0.3}, @tcc3);
sim(@d, t => { const k = Math.max(0, t - @t100); const p = Math.min(1, k/1.2); const e = 1 - Math.pow(1-p, 3);
  const v = 100*e + (p >= 1 ? 1.2*Math.sin(k*7) : 0); gsap.set("#sp-n", {rotation: v/150*180, svgOrigin:"@cx @cy"}); });
pop("#sp-v", @t100b); tl.fromTo("#sp-hl", {opacity:0}, {opacity:1, duration:0.3}, @t100b);
rise("#sp-mph", @t60); rise("#sp-hw", @thw);
""", tcc=tcc - 0.6, tcc2=tcc - 0.3, tcc3=tcc + 0.3, d=d, t100=t100, cx=CX, cy=CY, t100b=t100 + 1.0, t60=t60 - 0.1, thw=thw - 0.2))

# 6 HOURS — notebook division; counter to ≈ 1.5 million hours
s = "hours"; tdv = aw(s, "divide"); tsp = aw(s, "by the speed"); tget = aw(s, "you get"); t15 = aw(s, "one and a half million"); thr = aw(s, "hours of driving")
scenes[s] = scene_file(s, f"""
#hr-title {{ top:150px; font-size:76px; }}
.hr-l {{ position:absolute; right:200px; {GH} font-size:84px; text-align:right; white-space:nowrap; opacity:0; }}
#hr-res {{ position:absolute; left:0; right:0; top:690px; text-align:center; opacity:0; }}
#hr-res .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="hr-title" class="h1"><span class="hl">Divide!</span></div>
  <div id="hr-a" class="hr-l" style="top:320px">150 million km</div>
  <div id="hr-b" class="hr-l" style="top:450px"><span style="color:{C['blue']}">÷</span> 100 km/h</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="hr-ul" d="M240,600 Q560,590 900,598" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="hr-box" d="M120,680 L960,676 L962,830 L118,834 Z" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linejoin="round"/>
  </svg>
  <div id="hr-res"><span class="big" id="hr-n">≈ 0 hours</span></div>
""", J("""
rise("#hr-title", @tdv); rise("#hr-a", @tdv2); rise("#hr-b", @tsp); ink("#hr-ul", @tget, 0.4);
rise("#hr-res", @tget2); count("#hr-n", 0, 1.5, @tget2, @dc, v => "≈ " + (v >= 1.49 ? "1.5" : v.toFixed(1)) + " million hours");
ink("#hr-box", @thr, 0.6);
""", tdv=tdv - 0.3, tdv2=tdv, tsp=tsp - 0.1, tget=tget - 0.2, tget2=tget, dc=round(t15 + 0.9 - tget, 3), thr=thr))

# 7 DAYS — countable units: 62 calendar squares (1 square = 1,000 days)
s = "days"; t62 = aw(s, "sixty two thousand"); tday = aw(s, "days behind"); twh = aw(s, "wheel")
sq = ""
for i in range(63):
    c, r = i % 10, i // 10
    x = 160 + c * 76; y = 320 + r * 76
    fill = C['hi'] if i < 62 else "#FFFFFF"
    w = 64 if i < 62 else 64
    sq += f'<rect class="dy-s{"" if i < 62 else "x"}" x="{x}" y="{y}" width="{w}" height="64" rx="6" fill="{fill}" stroke="{K}" stroke-width="4" opacity="0"/>'
scenes[s] = scene_file(s, f"""
#dy-title {{ top:150px; font-size:84px; }}
""", f"""
  <div id="dy-title" class="h1" style="opacity:0"><span class="hl">62,000+ days</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>{sq}</svg>
  {tape("dy-key", "1 square = 1,000 days", 440, 860, -2, 44)}
""", J("""
tl.fromTo(".dy-s", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.18, ease:"back.out(2)", stagger:0.028}, @t0);
tl.fromTo(".dy-sx", {opacity:0}, {opacity:0.5, duration:0.2}, @tx);
pop("#dy-title", @t62);
rise("#dy-key", @tday);
""", t0=0.15, tx=0.15 + 62 * 0.028, t62=t62 - 0.1, tday=tday))

# 8 YEARS — timeline ruler 0 → 170 years, car slides along it
s = "years"; t170 = aw(s, "one hundred seventy"); tnb = aw(s, "nobody"); tth = aw(s, "make it there")
X0, X1, Y = 120, 960, 600
def yx(yr): return X0 + (X1 - X0) * yr / 170
tk = "".join(f'<path class="yr-tk" d="M{yx(v):.0f},{Y} L{yx(v):.0f},{Y-(30 if v%50==0 else 16)}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for v in range(0, 171, 10))
tl_ = "".join(f'<text x="{yx(v):.0f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="40" fill="{K}">{v}</text>' for v in (0, 50, 100, 150))
scenes[s] = scene_file(s, f"""
#yr-st {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="yr-ax" d="M{X0},{Y} L{X1},{Y}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {tk}{tl_}
    <text x="{X1}" y="{Y+52}" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{C['red']}">170</text>
    <text x="{(X0+X1)/2:.0f}" y="{Y+110}" text-anchor="middle" font-family="Gochi Hand" font-size="42" fill="{C['muted']}">years of driving</text>
    <path id="yr-p" d="M{X0},{Y-30} L{X1},{Y-30}" stroke="none" fill="none"/>
    <path id="yr-tr" d="M{X0},{Y-12} L{X1},{Y-12}" stroke="{C['hi']}" stroke-width="16" fill="none"/>
    {sun(X1+70, Y-150, 70, "yr-sun", rays=False)}
    {car("yr-car", 1.1)}
  </svg>
  <div id="yr-st" style="opacity:0"><span style="display:inline-block;{GH}font-size:110px;color:{C['red']};border:6px solid {C['red']};padding:0 30px;border-radius:14px;background:#fff;transform:rotate(-4deg)">≈ 170 years!</span></div>
  {tape("yr-nb", "nobody alive today arrives", 430, 790, -3, 44, "rgba(255,201,194,.95)")}
""", J("""
ink("#yr-ax", 0.05, 0.4); ink(".yr-tk", 0.2, 0.3, {stagger:0.02});
tl.set("#yr-car", {x:@x0, y:@yc}, 0);
along("#yr-car", "#yr-p", @tc, @dc, {ease:"power1.inOut"});
ink("#yr-tr", @tc, @dc, {ease:"power1.inOut"});
pop("#yr-st", @t170, {from:{rotation:-20, scale:1.6}, to:{}});
rise("#yr-nb", @tnb);
""", x0=X0, yc=Y - 30, tc=0.3, dc=round(t170 + 0.9 - 0.3, 3), t170=t170 + 0.2, tnb=tnb - 0.1))

# 9 JET — side-by-side bars: car 170 years vs jet 19 years
s = "jet"; tjp = aw(s, "jet plane"); t900 = aw(s, "nine hundred"); t19 = aw(s, "nineteen years")
BX = 150; L = 760
LJ = L * 19 / 170
PLANE = (f'<g transform="translate({BX+LJ+70:.0f},560) scale(1.4)"><g id="jt-pl" opacity="0"><path d="M-40,0 L40,0 Q52,0 52,6 Q52,12 40,12 L-40,12 Z" fill="#FFFFFF" stroke="{K}" stroke-width="4"/>'
         f'<path d="M-6,4 L-26,-30 L-12,-30 L14,4 Z M-6,10 L-26,40 L-12,40 L14,10 Z M-40,2 L-50,-18 L-40,-18 L-30,2 Z" fill="#BFE3F7" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></g></g>')
scenes[s] = scene_file(s, f"""
#jt-title {{ top:150px; font-size:72px; }}
""", f"""
  <div id="jt-title" class="h1">Even a <span class="hl">jet plane</span>…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="jt-cb" d="M{BX},400 L{BX+L},400" stroke="{C['red']}" stroke-width="44" fill="none" stroke-linecap="round"/>
    <path id="jt-jb" d="M{BX},566 L{BX+LJ:.0f},566" stroke="{C['blue']}" stroke-width="44" fill="none" stroke-linecap="round"/>
    {PLANE}
  </svg>
  <div class="abs" id="jt-cl" style="left:{BX}px;top:300px;{GH}font-size:52px">car ≈ 170 years</div>
  <div class="abs" id="jt-jl" style="left:{BX}px;top:620px;{GH}font-size:52px;opacity:0">jet ≈ 19 years</div>
  {tape("jt-sp", "900 km/h", 560, 470, 3, 50, "rgba(191,227,247,.95)")}
""", J("""
rise("#jt-title", @tjp0); ink("#jt-cb", 0.05, 0.4);
pop("#jt-pl", @tjp, {from:{x:-200}, to:{x:0}});
rise("#jt-sp", @t900);
ink("#jt-jb", @t900b, 0.6);
pop("#jt-jl", @t19, {from:{rotation:-8}, to:{}});
""", tjp0=0.1, tjp=tjp, t900=t900 - 0.1, t900b=t900 + 0.3, t19=t19 - 0.1))

# 10 LIGHT — sunbeam ZAP to Earth in ≈ 8 min
s = "light"; tsl = aw(s, "sunlight"); t8 = aw(s, "eight minutes"); tfc = aw(s, "your face"); tago = aw(s, "eight minutes ago")
BEAM = "M840,330 L260,700"
scenes[s] = scene_file(s, f"""
#lt-title {{ top:150px; font-size:76px; }}
#lt-zap {{ position:absolute; left:470px; top:380px; {GH} font-size:110px; color:{SUN2}; opacity:0; -webkit-text-stroke:3px {K}; }}
#lt-t {{ position:absolute; left:500px; top:640px; opacity:0; }}
#lt-t .big {{ font-size:100px; color:{C['red']}; }}
""", f"""
  <div id="lt-title" class="h1">But <span class="hl">sunlight</span>…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {sun(930, 300, 130, "lt-sun")}
    {earth(220, 720, 70, "lt-earth")}
    <path id="lt-b" d="{BEAM}" stroke="{SUN}" stroke-width="26" fill="none" stroke-linecap="round"/>
    <path id="lt-b2" d="{BEAM}" stroke="{SUN2}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <g id="lt-sw" opacity="0"><circle cx="460" cy="690" r="0" fill="none"/></g>
  </svg>
  <div id="lt-zap">ZAP!</div>
  <div id="lt-t"><span class="big">≈ 8 min</span></div>
  {tape("lt-ago", "left the Sun 8 min ago", 420, 820, -3, 44)}
""", J("""
rise("#lt-title", @tsl0); pop("#lt-sun", 0.1, {from:{scale:0.6}, to:{}}); pop("#lt-earth", 0.2, {from:{scale:0.5}, to:{}});
ink("#lt-b", @tsl, 0.35, {ease:"power3.in"}); ink("#lt-b2", @tsl, 0.35, {ease:"power3.in"});
pop("#lt-zap", @tsl2, {from:{rotation:-20, scale:1.8}, to:{rotation:-8}});
pop("#lt-t", @t8, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#lt-earth", {scale:1}, {scale:1.15, transformOrigin:"50% 50%", duration:0.15, yoyo:true, repeat:1}, @tfc);
rise("#lt-ago", @tago);
""", tsl0=0.05, tsl=tsl + 0.1, tsl2=tsl + 0.45, t8=t8 - 0.1, tfc=tfc, tago=tago - 0.4))

# 11 OUTRO — red "?" morphs into a tick; chip ≈ 170 years by car; Stay curious (Max centre: keep y < 620)
s = "outro"; t170 = aw(s, "one hundred seventy"); tbc = aw(s, "by car"); tsc = aw(s, "stay curious")
QM = "M470,230 Q470,150 540,150 Q610,150 610,215 Q610,262 545,290 L545,350"
TICK = "M440,250 Q470,280 500,320 Q520,345 530,350 Q580,250 650,160"
scenes[s] = scene_file(s, f"""
#ou-chip {{ position:absolute; left:0; right:0; top:440px; text-align:center; opacity:0; }}
#ou-chip .chip {{ font-size:60px; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" class="abs" style="left:0;top:0" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <path id="ou-qk" d="{QM}" stroke="{K}" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-q" d="{QM}" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="ou-qd" cx="545" cy="410" r="20" fill="{C['red']}" stroke="{K}" stroke-width="7"/>
  </svg>
  <div id="ou-chip"><span class="chip">≈ 170 years by car!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-svg", 0.05, {from:{scale:0.8}, to:{}});
morph("#ou-qk", "@tick", @t1, 0.55, {ease:"back.out(1.4)"}); morph("#ou-q", "@tick", @t1, 0.55, {ease:"back.out(1.4)"});
tl.to("#ou-q", {stroke:"#3FA34D", duration:0.3}, @t1b);
tl.to("#ou-qd", {opacity:0, scale:0, transformOrigin:"50% 50%", duration:0.2}, @t1);
pop("#ou-chip", @t1c, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#ou-chip", {scale:1}, {scale:1.1, duration:0.14, yoyo:true, repeat:1}, @tbc);
tl.to("#ou-qk, #ou-q, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
pop("#ou-c", @tsc1);
""", tick=TICK, t1=t170 - 0.05, t1b=t170 + 0.25, t1c=t170 + 0.4, tbc=tbc, tsc0=tsc - 0.45, tsc1=tsc - 0.2), fade=False)
# === GESTURES ===
think(g("hook", "how long"), SC["guess"]["start"] + 0.2)
point(g("guess", "a month"), 2.4)
wave(g("intro", "I'm Max"))
point(g("distance", "one hundred fifty million"), 1.4)
point(g("speed", "one hundred kilometers"), 1.2)
think(g("hours", "divide"), g("hours", "you get"))
wow(g("hours", "one and a half million"), 1.2)
point(g("days", "sixty two thousand"), 1.2)
wow(g("years", "one hundred seventy"), 1.4)
point(g("jet", "nineteen years"), 1.2)
wow(g("light", "eight minutes"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "car"), 0.35), ("ping.mp3", A("hook", "how long") + 0.6, 0.35),
        ("pop.mp3", A("guess", "a month"), 0.5), ("pop.mp3", A("guess", "ten years"), 0.5), ("pop.mp3", A("guess", "century") - 0.3, 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("distance", "one hundred fifty million") + 0.3, 0.5),
        ("riser.mp3", A("speed", "one hundred kilometers") - 0.1, 0.2), ("click-soft.mp3", A("hours", "you get"), 0.5),
        ("impact-bass-2.mp3", A("hours", "one and a half million") + 0.8, 0.35), ("pop.mp3", A("days", "sixty two thousand"), 0.5),
        ("impact-bass-1.mp3", A("years", "one hundred seventy") + 0.2, 0.4), ("pop.mp3", A("jet", "nineteen years"), 0.5),
        ("ping.mp3", A("light", "sunlight") + 0.45, 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
