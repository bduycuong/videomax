# MAX WISE ep46 — On which planet is one day longer than one whole year?
# Kit: two three.js scenes (hook: Venus in space; spin: Venus turning with a marker) + ink / along / morph.
# Source: NASA Space Place "All About Venus" — day 243 Earth days, year 225 Earth days, spins backwards
# (Sun rises in the west), hottest planet though not closest. Maths: 243 - 225 = 18.
# === SCENES ===
import math as _m
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SUN = "#FFC93C"; SUN2 = "#F59E2A"; SEA = "#7FB8E6"; LAND = "#9BD08F"; VEN = "#EBC877"; VEN2 = "#D9A548"
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
def earth(cx, cy, r, idn=""):
    i = f' id="{idn}"' if idn else ""
    return (f'<g{i}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{SEA}" stroke="{K}" stroke-width="5"/>'
            f'<path d="M{cx-r*0.5:.0f},{cy-r*0.3:.0f} q{r*0.3:.0f},-{r*0.4:.0f} {r*0.6:.0f},-{r*0.1:.0f} q-{r*0.1:.0f},{r*0.4:.0f} -{r*0.5:.0f},{r*0.5:.0f} z" fill="{LAND}"/>'
            f'<path d="M{cx+r*0.1:.0f},{cy+r*0.3:.0f} q{r*0.3:.0f},-{r*0.2:.0f} {r*0.5:.0f},{r*0.1:.0f} q-{r*0.2:.0f},{r*0.3:.0f} -{r*0.5:.0f},{r*0.2:.0f} z" fill="{LAND}"/></g>')
def venus(cx, cy, r, idn="", extra=""):
    i = f' id="{idn}"' if idn else ""
    return (f'<g{i} {extra}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{VEN}" stroke="{K}" stroke-width="5"/>'
            f'<path d="M{cx-r*0.8:.0f},{cy-r*0.25:.0f} Q{cx:.0f},{cy-r*0.45:.0f} {cx+r*0.8:.0f},{cy-r*0.2:.0f}" stroke="{VEN2}" stroke-width="{max(3,r*0.12):.0f}" fill="none" stroke-linecap="round"/>'
            f'<path d="M{cx-r*0.7:.0f},{cy+r*0.3:.0f} Q{cx:.0f},{cy+r*0.1:.0f} {cx+r*0.75:.0f},{cy+r*0.35:.0f}" stroke="{VEN2}" stroke-width="{max(3,r*0.1):.0f}" fill="none" stroke-linecap="round"/></g>')
def sun(cx, cy, r, idn="", rays=True):
    i = f' id="{idn}"' if idn else ""
    ry = ""
    if rays:
        for k in range(12):
            a = k * _m.pi / 6
            ry += f'<path d="M{cx+(r+14)*_m.cos(a):.0f},{cy+(r+14)*_m.sin(a):.0f} L{cx+(r+44)*_m.cos(a):.0f},{cy+(r+44)*_m.sin(a):.0f}" stroke="{SUN2}" stroke-width="9" stroke-linecap="round"/>'
    return f'<g{i}>{ry}<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SUN}" stroke="{K}" stroke-width="6"/></g>'
def ellipse_path(cx, cy, rx, ry):  # one sub-path, starts at right, goes counter-clockwise on screen (top first)
    return f"M{cx+rx},{cy} A{rx},{ry} 0 1 0 {cx-rx},{cy} A{rx},{ry} 0 1 0 {cx+rx-0.1:.1f},{cy-0.5}"

VENUS3D = """
const S = T3.stage("@cv", @w, @h, 34);
const rnd = T3.seeded(11);
const stars = new THREE.Group();
for (let i=0;i<60;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.03+rnd()*0.03, 6, 4), T3.toon(0x2B2B2B));
  m.position.set((rnd()-0.5)*14, (rnd()-0.5)*8, -4 - rnd()*3); stars.add(m); }
S.scene.add(stars);
const ven = T3.inked(new THREE.SphereGeometry(1.25, 48, 32), 0xEBC877, 0.05); S.scene.add(ven);
for (let i=0;i<5;i++) { const b = new THREE.Mesh(new THREE.TorusGeometry(1.255*Math.cos((i-2)*0.32), 0.05, 6, 48), T3.toon(0xD9A548));
  b.rotation.x = Math.PI/2; b.position.y = 1.255*Math.sin((i-2)*0.32); ven.add(b); }
"""

# 1 HOOK — 3D Venus in a starfield, slow push-in; question text
s = "hook"; tpz = aw(s, "puzzle"); tpl = aw(s, "which planet"); tlo = aw(s, "longer"); tyr = aw(s, "whole year"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q0 {{ top:160px; font-size:76px; }}
#hk-q {{ top:150px; font-size:72px; }}
#hk-cv {{ position:absolute; left:40px; top:400px; width:1000px; height:540px; }}
#hk-qm {{ position:absolute; left:800px; top:360px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-q0" class="h1">A <span class="hl">puzzle</span>…</div>
  <div id="hk-q" class="h1" style="opacity:0">1 <span class="hl">day</span> longer than<br>1 whole <span class="hl">year</span>?</div>
  <canvas id="hk-cv" width="1000" height="540"></canvas>
  <div id="hk-qm">?</div>
""", J(VENUS3D + """
drive(@d, t => {
  const s = t < 0.6 ? 0.5 + 0.5*gsap.parseEase("back.out(2)")(t/0.6) : 1; ven.scale.setScalar(s);
  ven.rotation.y = -t*0.12; ven.rotation.z = 0.05;
  const p = Math.min(1, t/@d); const e = p*p*(3-2*p);
  S.cam.position.set(0.6 - 0.6*e, 0.4, 6.2 - 1.6*e); S.cam.lookAt(0, 0, 0); S.render();
});
tl.to("#hk-q0", {opacity:0, y:-20, duration:0.25}, @tq0);
rise("#hk-q", @tq);
pop("#hk-qm", @tqm, {from:{rotation:-20}, to:{rotation:8}});
""", cv="#hk-cv", w=1000, h=540, d=d, tq0=tpl - 0.4, tq=tpl - 0.15, tqm=tyr + 0.2))

# 2 GUESS — sticky notes with mini planets inking
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "Mercury"); t2 = aw(s, "Venus"); t3 = aw(s, "Neptune")
notes = [("a", "Mercury?", -6, 110, C['hi'], 58), ("b", "Venus?", 4, 405, "#BFE3F7", 62), ("c", "Neptune?", -3, 700, "#FFC9C2", 58)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:340px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding:40px 16px 0">{txt}</div>' for k, txt, r, x, bg, fs in notes)
def mini(cx, cy, r, fill, cls):
    return (f'<path class="{cls}" d="M{cx},{cy-r} A{r},{r} 0 1 1 {cx-0.1:.1f},{cy-r}" stroke="{K}" stroke-width="5" fill="{fill}"/>'
            f'<path class="{cls}" d="M{cx-r-20},{cy+6} Q{cx},{cy-r*0.2} {cx+r+20},{cy-6}" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>')
doodles = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>'
           + mini(248, 605, 40, "#B9B4AE", "gs-da") + mini(545, 615, 48, VEN, "gs-db") + mini(838, 610, 52, "#6E8FE0", "gs-dc") + '</svg>')
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink(".gs-da", @ta, 0.35, {stagger:0.1}); ink(".gs-db", @tb, 0.35, {stagger:0.1}); ink(".gs-dc", @tc, 0.35, {stagger:0.1});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.3, ta=t1 + 0.2, tb=t2 + 0.2, tc=t3))

# 3 INTRO — logo, underline, spin arrow ink (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tsp = aw(s, "spin some")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {venus(150, 560, 42, "in-v1")}
    <path class="in-ar" d="M90,510 Q150,470 214,512" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {earth(930, 560, 42, "in-e1")}
    <path class="in-ar" d="M870,512 Q930,470 994,510" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's spin!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tsp); pop("#in-v1", @tsp2, {from:{scale:0.3}, to:{}}); pop("#in-e1", @tsp2, {from:{scale:0.3}, to:{}});
ink(".in-ar", @tsp3, 0.35, {stagger:0.1});
""", tmw=tmw, tu=tmw + 0.3, tsp=tsp - 0.2, tsp2=tsp, tsp3=tsp + 0.3))

# 4 WORDS — DAY = one spin (arrow inks round a planet), YEAR = one trip (dot travels along orbit)
s = "words"; tid = aw(s, "two simple"); tday = aw(s, "a day"); tspin = aw(s, "full spin"); tyr = aw(s, "a year"); ttrip = aw(s, "full trip")
ORB = ellipse_path(770, 560, 210, 120)
scenes[s] = scene_file(s, f"""
#wd-title {{ top:150px; font-size:76px; }}
.wd-l {{ position:absolute; top:300px; {GH} font-size:80px; width:440px; text-align:center; opacity:0; }}
""", f"""
  <div id="wd-title" class="h1">Two <span class="hl">ideas</span></div>
  <div id="wd-dl" class="wd-l" style="left:40px">DAY</div>
  <div id="wd-yl" class="wd-l" style="left:550px">YEAR</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="wd-div" d="M520,300 L524,820" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-dasharray="14 12"/>
    {earth(260, 560, 95, "wd-e")}
    <path id="wd-sp" d="M260,435 A125,125 0 1 1 140,600" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path id="wd-sph" d="M126,572 L140,604 L170,588" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    {sun(770, 560, 50, "wd-sun", rays=False)}
    <path id="wd-orb" d="{ORB}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-dasharray="2 0"/>
    <g id="wd-dot" opacity="0" transform="translate(980,560)"><circle r="26" fill="{SEA}" stroke="{K}" stroke-width="5"/></g>
  </svg>
  {tape("wd-dt", "1 spin", 150, 760, -3, 52)}
  {tape("wd-yt", "1 trip around the Sun", 560, 760, 2, 42, "rgba(191,227,247,.95)")}
""", J("""
rise("#wd-title", @tid);
rise("#wd-dl", @tday); pop("#wd-e", @tday2, {from:{scale:0.4}, to:{}});
ink("#wd-sp", @tspin, 0.6, {ease:"power2.inOut"}); ink("#wd-sph", @tspin2, 0.2);
tl.fromTo("#wd-e", {rotation:0}, {rotation:360, svgOrigin:"260 560", duration:1.2, ease:"power1.inOut"}, @tspin);
rise("#wd-dt", @tspin3);
rise("#wd-yl", @tyr); pop("#wd-sun", @tyr2, {from:{scale:0.4}, to:{}});
ink("#wd-orb", @tyr3, 0.5);
tl.to("#wd-dot", {opacity:1, duration:0.1}, @ttrip);
along("#wd-dot", "#wd-orb", @ttrip, 1.6, {ease:"power1.inOut"});
rise("#wd-yt", @ttrip2);
""", tid=tid - 0.2, tday=tday - 0.1, tday2=tday + 0.1, tspin=tspin - 0.1, tspin2=tspin + 0.5, tspin3=tspin + 0.6,
   tyr=tyr - 0.1, tyr2=tyr + 0.1, tyr3=tyr + 0.2, ttrip=ttrip, ttrip2=ttrip - 0.3))

# 5 EARTH — countable units: 1 square (day) vs 365 tiny ticks filling a calendar grid
s = "earth"; tez = aw(s, "On Earth"); tonce = aw(s, "once every day"); tcir = aw(s, "circle the Sun"); t365 = aw(s, "three hundred sixty five")
cells = ""
for i in range(365):
    c, r = i % 25, i // 25
    x = 160 + c * 30; y = 470 + r * 26
    cells += f'<rect class="ea-c" x="{x}" y="{y}" width="22" height="18" rx="3" fill="{C["hi"]}" stroke="{K}" stroke-width="2" opacity="0"/>'
scenes[s] = scene_file(s, f"""
#ea-title {{ top:150px; font-size:76px; }}
#ea-one {{ position:absolute; left:160px; top:290px; {GH} font-size:62px; opacity:0; }}
#ea-n {{ position:absolute; left:0; right:0; top:860px; text-align:center; opacity:0; }}
#ea-n .big {{ font-size:84px; color:{C['blue']}; }}
""", f"""
  <div id="ea-title" class="h1">On <span class="hl">Earth</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {earth(900, 330, 70, "ea-e")}
    <rect id="ea-sq" x="560" y="300" width="80" height="64" rx="6" fill="#FFC9C2" stroke="{K}" stroke-width="4" opacity="0"/>
    {cells}
  </svg>
  <div id="ea-one">1 spin = 1 day</div>
  <div id="ea-n"><span class="big" id="ea-cnt">0 days = 1 year</span></div>
""", J("""
rise("#ea-title", @tez); pop("#ea-e", @tez2, {from:{scale:0.4}, to:{}});
tl.fromTo("#ea-e", {rotation:0}, {rotation:360, svgOrigin:"900 330", duration:1.0, ease:"power1.inOut"}, @tonce);
rise("#ea-one", @tonce);
tl.fromTo(".ea-c", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.12, ease:"back.out(2)", stagger:@stg}, @tcir);
rise("#ea-n", @tcir); count("#ea-cnt", 0, 365, @tcir, @dc, v => Math.round(v) + " days = 1 year");
""", tez=tez - 0.2, tez2=tez, tonce=tonce, tcir=tcir, stg=round((t365 + 1.0 - tcir) / 365, 4), dc=round(t365 + 1.0 - tcir, 3)))

# 6 SPIN — 3D Venus turning with a flag marker; day counter 0 -> 243 (simulated)
s = "spin"; tmv = aw(s, "meet Venus"); tslow = aw(s, "so slowly"); tturn = aw(s, "one turn"); t243 = aw(s, "two hundred forty three"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#sp-title {{ top:150px; font-size:76px; }}
#sp-cv {{ position:absolute; left:140px; top:270px; width:800px; height:560px; }}
#sp-n {{ position:absolute; left:0; right:0; top:830px; text-align:center; opacity:0; }}
#sp-n .big {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="sp-title" class="h1">Meet <span class="hl">Venus</span></div>
  <canvas id="sp-cv" width="800" height="560"></canvas>
  <div id="sp-n"><span class="big" id="sp-cnt">day 0</span></div>
  {tape("sp-sl", "s l o w  spin", 640, 300, 4, 46)}
""", J(VENUS3D + """
const flag = new THREE.Group();
const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 0.5, 6), T3.toon(0x2B2B2B)); pole.position.y = 0.25; flag.add(pole);
const cloth = T3.inked(new THREE.BoxGeometry(0.28, 0.17, 0.02), 0xE0483C, 0.015); cloth.position.set(0.15, 0.42, 0); flag.add(cloth);
const holder = new THREE.Group(); holder.add(flag); flag.position.set(0, 0, 0); flag.rotation.x = Math.PI/2; flag.position.z = 1.22;
ven.add(holder);
const T0 = @tturn, T1 = @tend;
drive(@d, t => {
  const s = t < 0.5 ? 0.5 + 0.5*gsap.parseEase("back.out(2)")(t/0.5) : 1; ven.scale.setScalar(s);
  const p = Math.max(0, Math.min(1, (t - T0)/(T1 - T0)));
  ven.rotation.y = -0.6 - p*Math.PI*2;
  S.cam.position.set(0, 0.9, 5.2); S.cam.lookAt(0, 0, 0); S.render();
});
""", cv="#sp-cv", w=800, h=560, d=d, tturn=tturn, tend=t243 + 1.2) + J("""
rise("#sp-title", @tmv); rise("#sp-sl", @tslow);
rise("#sp-n", @tturn); count("#sp-cnt", 0, 243, @tturn, @dc, v => "1 turn = " + Math.round(v) + " Earth days");
""", tmv=tmv - 0.2, tslow=tslow, tturn=tturn, dc=round(t243 + 1.2 - tturn, 3)))

# 7 ORBIT — Venus travels along its orbit around the Sun; counter 0 -> 225
s = "orbit"; tbut = aw(s, "But"); ttrip = aw(s, "trip around"); t225 = aw(s, "two hundred twenty five")
ORB2 = ellipse_path(540, 560, 360, 220)
scenes[s] = scene_file(s, f"""
#ob-title {{ top:150px; font-size:72px; }}
#ob-n {{ position:absolute; left:0; right:0; top:820px; text-align:center; opacity:0; }}
#ob-n .big {{ font-size:84px; color:{C['blue']}; }}
""", f"""
  <div id="ob-title" class="h1">One trip around the <span class="hl">Sun</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {sun(540, 560, 80, "ob-sun")}
    <path id="ob-orb" d="{ORB2}" stroke="{C['blue']}" stroke-width="6" fill="none"/>
    <path id="ob-tr" d="{ORB2}" stroke="{C['hi']}" stroke-width="18" fill="none" opacity=".8"/>
    <g id="ob-v" transform="translate(900,560)">{venus(0, 0, 40)}</g>
  </svg>
  <div id="ob-n"><span class="big" id="ob-cnt">0 Earth days</span></div>
""", J("""
rise("#ob-title", @tbut); pop("#ob-sun", @tbut2, {from:{scale:0.4}, to:{}});
ink("#ob-orb", @tbut3, 0.5);
along("#ob-v", "#ob-orb", @ttrip, @dd, {ease:"power1.inOut"});
ink("#ob-tr", @ttrip, @dd, {ease:"power1.inOut"});
rise("#ob-n", @ttrip); count("#ob-cnt", 0, 225, @ttrip, @dd, v => "1 year = " + Math.round(v) + " Earth days");
""", tbut=tbut - 0.2, tbut2=tbut, tbut3=tbut + 0.2, ttrip=ttrip, dd=round(t225 + 1.2 - ttrip, 3)))

# 8 COMPARE — side-by-side bars: DAY 243 vs YEAR 225, bracket +18
s = "compare"; tsp = aw(s, "one spin"); twy = aw(s, "whole year"); t18 = aw(s, "eighteen days")
BX = 120; L = 760
LD = L; LY = L * 225 / 243
scenes[s] = scene_file(s, f"""
#cp-title {{ top:150px; font-size:72px; }}
.cp-l {{ position:absolute; left:{BX}px; {GH} font-size:52px; opacity:0; }}
""", f"""
  <div id="cp-title" class="h1">Day <span class="hl">vs</span> year</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="cp-db" d="M{BX},420 L{BX+LD:.0f},420" stroke="{C['red']}" stroke-width="54" fill="none" stroke-linecap="butt"/>
    <path id="cp-yb" d="M{BX},640 L{BX+LY:.0f},640" stroke="{C['blue']}" stroke-width="54" fill="none" stroke-linecap="butt"/>
    <path id="cp-g1" d="M{BX+LY:.0f},600 L{BX+LY:.0f},760" stroke="{K}" stroke-width="4" stroke-dasharray="10 8" fill="none"/>
    <path id="cp-br" d="M{BX+LY:.0f},770 Q{BX+LY:.0f},790 {(2*BX+LY+LD)/2:.0f},790 Q{BX+LD:.0f},790 {BX+LD:.0f},770" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path id="cp-g2" d="M{BX+LD:.0f},450 L{BX+LD:.0f},770" stroke="{K}" stroke-width="4" stroke-dasharray="10 8" fill="none"/>
  </svg>
  <div id="cp-dl" class="cp-l" style="top:320px">1 day = 243 Earth days</div>
  <div id="cp-yl" class="cp-l" style="top:540px">1 year = 225 Earth days</div>
  {stamp("cp-18", "+18 days", 590, 830, -3, 64)}
""", J("""
rise("#cp-title", 0.1);
ink("#cp-db", @tsp, 0.6, {ease:"power2.out"}); rise("#cp-dl", @tsp);
ink("#cp-yb", @twy, 0.6, {ease:"power2.out"}); rise("#cp-yl", @twy);
ink("#cp-g1", @t18a, 0.3); ink("#cp-g2", @t18a, 0.3); ink("#cp-br", @t18b, 0.3);
pop("#cp-18", @t18, {from:{rotation:-20, scale:1.6}, to:{}});
""", tsp=tsp - 0.1, twy=twy - 0.3, t18a=t18 - 0.6, t18b=t18 - 0.3, t18=t18))

# 9 WEST — compass W/E, Sun travels along an arc from west (left) to east (right); BACKWARDS stamp
s = "west"; tbon = aw(s, "bonus"); tbk = aw(s, "spins backwards"); trise = aw(s, "rises in the west"); tset = aw(s, "sets in the east")
ARC = "M150,700 Q540,180 930,700"
scenes[s] = scene_file(s, f"""
#ws-title {{ top:150px; font-size:76px; }}
.ws-c {{ position:absolute; top:730px; {GH} font-size:80px; opacity:0; }}
""", f"""
  <div id="ws-title" class="h1"><span class="hl">Bonus!</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="ws-gr" d="M60,710 Q300,690 540,712 Q780,730 1020,706" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="ws-hatch" d="M80,730 L110,760 M180,728 L210,758 M280,726 L310,756 M380,728 L410,758 M480,730 L510,760 M580,732 L610,762 M680,734 L710,764 M780,732 L810,762 M880,726 L910,756 M960,722 L990,752" stroke="{C['pencil']}" stroke-width="4" fill="none"/>
    <path id="ws-arc" d="{ARC}" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-dasharray="14 12"/>
    <g id="ws-sun" opacity="0">{sun(0, 0, 55)}</g>
  </svg>
  <div id="ws-w" class="ws-c" style="left:110px">W</div>
  <div id="ws-e" class="ws-c" style="left:900px">E</div>
  {tape("ws-rt", "rises in the WEST", 140, 820, -3, 44)}
  {tape("ws-st", "sets in the EAST", 600, 820, 3, 44, "rgba(191,227,247,.95)")}
  {stamp("ws-bk", "BACKWARDS!", 330, 290, -6, 64)}
""", J("""
rise("#ws-title", @tbon); ink("#ws-gr", @tbon2, 0.5); ink("#ws-hatch", @tbon3, 0.4);
pop("#ws-bk", @tbk, {from:{rotation:-20, scale:1.6}, to:{}});
pop("#ws-w", @trise); pop("#ws-e", @trise);
ink("#ws-arc", @trise, 0.6);
tl.set("#ws-sun", {opacity:1, x:150, y:700}, @trise2);
along("#ws-sun", "#ws-arc", @trise2, @dd, {ease:"power1.inOut"});
rise("#ws-rt", @trise3); rise("#ws-st", @tset);
""", tbon=tbon - 0.2, tbon2=tbon, tbon3=tbon + 0.3, tbk=tbk, trise=trise - 0.1, trise2=trise + 0.3, dd=round(tset + 1.0 - trise - 0.3, 3), trise3=trise + 0.4, tset=tset))

# 10 HOT — myth crossed out: closest = hottest? ; Mercury closest, Venus hottest; thermometer fills
s = "hot"; tcl = aw(s, "closest planet"); tyet = aw(s, "Yet"); thot = aw(s, "hottest planet")
scenes[s] = scene_file(s, f"""
#ht-myth {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:70px; color:{C['muted']}; opacity:0; }}
.ht-l {{ position:absolute; {GH} font-size:52px; text-align:center; width:360px; opacity:0; }}
""", f"""
  <div id="ht-myth">closest = hottest?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="ht-x" d="M240,230 Q540,205 840,222" stroke="{C['red']}" stroke-width="11" fill="none" stroke-linecap="round"/>
    {sun(40, 560, 120, "ht-sun")}
    <g id="ht-me"><circle cx="300" cy="560" r="34" fill="#B9B4AE" stroke="{K}" stroke-width="5"/></g>
    {venus(560, 560, 62, "ht-ve")}
    <g id="ht-th" opacity="0">
      <rect x="840" y="330" width="56" height="330" rx="28" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>
      <circle cx="868" cy="690" r="50" fill="{C['red']}" stroke="{K}" stroke-width="6"/>
      <rect id="ht-fill" x="852" y="350" width="32" height="320" rx="16" fill="{C['red']}"/>
    </g>
  </svg>
  <div id="ht-ml" class="ht-l" style="left:120px;top:640px">Mercury:<br>closest</div>
  <div id="ht-vl" class="ht-l" style="left:380px;top:660px;color:{C['red']}">Venus:<br>HOTTEST</div>
""", J("""
rise("#ht-myth", 0.1); pop("#ht-sun", 0.2, {from:{scale:0.6}, to:{}});
pop("#ht-me", @tcl, {from:{scale:0.3}, to:{}}); rise("#ht-ml", @tcl);
ink("#ht-x", @tyet, 0.35);
pop("#ht-ve", @tyet2, {from:{scale:0.3}, to:{}});
tl.to("#ht-th", {opacity:1, duration:0.2}, @tyet2);
tl.fromTo("#ht-fill", {scaleY:0.05, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.9, ease:"power2.out"}, @thot);
pop("#ht-vl", @thot, {from:{rotation:-10, scale:1.4}, to:{}});
""", tcl=tcl - 0.2, tyet=tyet - 0.1, tyet2=tyet + 0.2, thot=thot - 0.1))

# 11 OUTRO — "?" morphs into a tick; chip; Stay curious (Max centre: keep y < 620)
s = "outro"; tvn = aw(s, "is Venus"); tout = aw(s, "outlasts"); tsc = aw(s, "stay curious")
QM = "M470,230 Q470,150 540,150 Q610,150 610,215 Q610,262 545,290 L545,350"
TICK = "M440,250 Q470,280 500,320 Q520,345 530,350 Q580,250 650,160"
scenes[s] = scene_file(s, f"""
#ou-chip {{ position:absolute; left:0; right:0; top:440px; text-align:center; opacity:0; }}
#ou-chip .chip {{ font-size:58px; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" class="abs" style="left:0;top:0" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <path id="ou-qk" d="{QM}" stroke="{K}" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-q" d="{QM}" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="ou-qd" cx="545" cy="410" r="20" fill="{C['red']}" stroke="{K}" stroke-width="7"/>
  </svg>
  <div id="ou-chip"><span class="chip">Venus: 1 day &gt; 1 year!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-svg", 0.05, {from:{scale:0.8}, to:{}});
morph("#ou-qk", "@tick", @t1, 0.55, {ease:"back.out(1.4)"}); morph("#ou-q", "@tick", @t1, 0.55, {ease:"back.out(1.4)"});
tl.to("#ou-q", {stroke:"#3FA34D", duration:0.3}, @t1b);
tl.to("#ou-qd", {opacity:0, scale:0, transformOrigin:"50% 50%", duration:0.2}, @t1);
pop("#ou-chip", @t1c, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#ou-chip", {scale:1}, {scale:1.1, duration:0.14, yoyo:true, repeat:1}, @tout);
tl.to("#ou-qk, #ou-q, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
pop("#ou-c", @tsc1);
""", tick=TICK, t1=tvn - 0.05, t1b=tvn + 0.25, t1c=tvn + 0.4, tout=tout, tsc0=tsc - 0.45, tsc1=tsc - 0.2), fade=False)
# === GESTURES ===
think(g("hook", "which planet"), SC["guess"]["start"] + 0.2)
point(g("guess", "Mercury"), 2.4)
wave(g("intro", "I'm Max"))
point(g("words", "full spin"), 1.2)
point(g("earth", "three hundred sixty five"), 1.2)
wow(g("spin", "two hundred forty three"), 1.4)
point(g("orbit", "two hundred twenty five"), 1.2)
wow(g("compare", "longer than"), 1.4)
point(g("west", "rises in the west"), 1.4)
wow(g("hot", "hottest planet"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "whole year") + 0.2, 0.35),
        ("pop.mp3", A("guess", "Mercury"), 0.5), ("pop.mp3", A("guess", "Venus"), 0.5), ("pop.mp3", A("guess", "Neptune") - 0.3, 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("words", "full spin"), 0.5),
        ("riser.mp3", A("earth", "circle the Sun"), 0.2), ("impact-bass-2.mp3", A("spin", "two hundred forty three") + 0.8, 0.35),
        ("click.mp3", A("orbit", "two hundred twenty five") + 0.8, 0.5), ("impact-bass-1.mp3", A("compare", "eighteen days"), 0.4),
        ("pop.mp3", A("west", "spins backwards"), 0.5), ("whoosh-short.mp3", A("west", "rises in the west") + 0.3, 0.35),
        ("ping.mp3", A("hot", "hottest planet"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
