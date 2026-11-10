# MAX WISE ep42 — How much does all the air on Earth weigh?
# Kit: ink / morph / along helpers + two three.js scenes (hook: Earth in an air shell on a scale; planet: Earth sprouts air columns, pull-back).
# Sources: Trenberth & Smith 2005 J. Climate (NCAR): atmosphere mass 5.148e18 kg ~ 5.15e15 t ("about five quadrillion tons").
#  Sea-level pressure 101325 Pa / 9.81 = 10,329 kg per m2 (~10 t). UCAR MetEd: half the mass below 500 mb ~ 5.5 km.
#  Standard atmosphere at 8,849 m: 314 hPa = 31% of sea level -> ~two thirds below Everest. Skin ~1.8 m2 x 10.3 t ~ 18 t.
# === SCENES ===
import math as _m, random as _r
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SEA = "#BFE3F7"; LAND = "#9BD08F"; AIR = "#9CCBEA"
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
def wt(x, y, cls, s=1.0):  # a weight block with handle
    return (f'<path class="{cls}" d="M{x-30*s},{y+30*s} L{x-22*s},{y-8*s} L{x+22*s},{y-8*s} L{x+30*s},{y+30*s} Z" {WS}/>'
            f'<path class="{cls}" d="M{x-10*s},{y-8*s} Q{x},{y-26*s} {x+10*s},{y-8*s}" {WS}/>')
def car(x, y, cls, col):  # little doodle car, ~120 x 56, (x,y) = bottom-left
    return (f'<g class="{cls}" opacity="0"><path d="M{x},{y-14} L{x+4},{y-34} L{x+30},{y-36} L{x+44},{y-56} L{x+84},{y-56} L{x+100},{y-36} L{x+118},{y-32} L{x+120},{y-14} Z" '
            f'fill="{col}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M{x+50},{y-50} L{x+80},{y-50} L{x+92},{y-36} L{x+40},{y-36} Z" fill="#FFFFFF" stroke="{K}" stroke-width="3"/>'
            f'<circle cx="{x+28}" cy="{y-12}" r="11" fill="{K}"/><circle cx="{x+94}" cy="{y-12}" r="11" fill="{K}"/></g>')

EARTH_JS = """
function buildEarth(S, R, seed) {
  const earth = T3.inked(new THREE.SphereGeometry(R, 48, 32), 0x4F9BE0, 0.04); S.scene.add(earth); earth.rotation.z = 0.3;
  const body = earth.userData.body; const rnd = T3.seeded(seed);
  for (let i=0;i<16;i++) { const th = 0.6+rnd()*1.9, ph = -3.0 + i*0.39 + rnd()*0.2, sz = R*(0.2+rnd()*0.16);
    const m = new THREE.Mesh(new THREE.SphereGeometry(sz, 20, 14), T3.toon(0x7CC46A));
    m.position.setFromSphericalCoords(R*0.93, th, ph); m.scale.set(1,1,0.3); m.lookAt(0,0,0); body.add(m); }
  return earth;
}
"""

# 1 HOOK — 3D Earth in a pale air shell, sitting on a doodle bathroom scale
s = "hook"; tlu = aw(s, "look up"); tal = aw(s, "all that air"); thw = aw(s, "how much"); twe = aw(s, "weigh"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-now {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#hk-q {{ top:150px; font-size:80px; }}
#hk-cv {{ position:absolute; left:140px; top:390px; width:800px; height:470px; }}
#hk-sc {{ position:absolute; left:0; top:0; }}
#hk-qm {{ position:absolute; left:880px; top:420px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-now"><span class="chip" style="font-size:64px">Look up!</span></div>
  <div id="hk-q" class="h1">How much does all the <span class="hl">air on Earth</span> weigh?</div>
  <canvas id="hk-cv" width="800" height="470"></canvas>
  <svg id="hk-sc" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <g id="hk-scale" opacity="0">
      <path d="M380,850 Q540,842 700,850 L712,940 Q540,948 368,940 Z" fill="#FFFFFF" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
      <path d="M492,872 Q540,866 588,872 L586,918 Q540,922 494,918 Z" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>
      <g id="hk-ndl"><path d="M540,914 L540,880" stroke="{C['red']}" stroke-width="5" stroke-linecap="round"/></g>
    </g>
  </svg>
  {tape("hk-tp", "air has weight!", 600, 420, 4, 46)}
  <div id="hk-qm">?</div>
""", EARTH_JS + J("""
const S = T3.stage("#hk-cv", 800, 470, 34); S.cam.position.set(0, 0.6, 7.4); S.cam.lookAt(0, 0.25, 0);
const R = 1.6; const earth = buildEarth(S, R, 7);
const air = new THREE.Mesh(new THREE.SphereGeometry(R*1.2, 48, 32), new THREE.MeshBasicMaterial({color:0xBFE3F7, transparent:true, opacity:0.0, depthWrite:false}));
S.scene.add(air);
drive(@d, t => {
  const s = t < 0.5 ? 0.6 + 0.4*gsap.parseEase("back.out(2)")(t/0.5) : 1;
  earth.scale.setScalar(s); earth.userData.body.rotation.y = 0.3*t;
  const a = Math.max(0, Math.min(1, (t - @tal)/0.6)); air.material.opacity = 0.42*a; air.scale.setScalar(s*(1 + 0.02*Math.sin(t*3)));
  S.render();
});
pop("#hk-now .chip", @tlu, {from:{rotation:-10}, to:{rotation:-3}});
pop("#hk-scale", 0.3, {from:{y:40}, to:{}}); tl.set("#hk-ndl", {rotation:0, svgOrigin:"540 914"}, 0);
rise("#hk-tp", @tal2);
tl.to("#hk-now", {opacity:0, y:-20, duration:0.2}, @tq0);
rise("#hk-q", @tq);
tl.to("#hk-ndl", {rotation:60, duration:0.6, ease:"elastic.out(1,0.35)"}, @twe);
tl.to("#hk-tp", {opacity:0, duration:0.2}, @tq0);
pop("#hk-qm", @twe, {from:{rotation:-20}, to:{rotation:8}});
""", d=d, tlu=max(0.05, tlu - 0.1), tal=tal, tal2=tal + 0.3, tq0=thw - 0.35, tq=thw - 0.1, twe=twe + 0.1))

# 2 GUESS — sticky notes, weight doodles ink themselves
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "few tons"); t2 = aw(s, "billion tons"); t3 = aw(s, "way way more")
notes = [("a", "a few tons?", -6, 110, C['hi'], 58), ("b", "a billion tons?", 4, 405, "#BFE3F7", 54), ("c", "way, way more?", -3, 700, "#FFC9C2", 56)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:340px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding:40px 16px 0">{txt}</div>' for k, txt, r, x, bg, fs in notes)
heap = [(800, 650), (860, 650), (920, 650), (830, 596), (890, 596), (860, 542)]
doodles = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>'
           + wt(248, 620, "gs-da") + wt(500, 650, "gs-db", 0.8) + wt(560, 650, "gs-db", 0.8) + wt(530, 604, "gs-db", 0.8)
           + "".join(wt(x, y, "gs-dc", 0.8) for x, y in heap) + '</svg>')
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink(".gs-da", @ta, 0.3, {stagger:0.1}); ink(".gs-db", @tb, 0.3, {stagger:0.06}); ink(".gs-dc", @tc, 0.3, {stagger:0.04});
""", tg=tg, t1=t1 - 0.1, t2=t2 - 0.1, t3=t3 - 0.1, ta=t1 + 0.25, tb=t2 + 0.25, tc=t3 + 0.2))

# 3 INTRO — logo, underline, a balance scale inks itself (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tlw = aw(s, "let's weigh"); tsk = aw(s, "the sky")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:390px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-bs" d="M540,600 L540,500" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-bs" d="M470,604 L610,604" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-bs" d="M400,500 L680,500" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-bs" d="M400,500 L370,560 M400,500 L430,560" stroke="{K}" stroke-width="4" fill="none"/>
    <path class="in-bs" d="M350,560 Q400,590 450,560" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path class="in-bs" d="M680,500 L650,560 M680,500 L710,560" stroke="{K}" stroke-width="4" fill="none"/>
    <path class="in-bs" d="M630,560 Q680,590 730,560" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="in-cl" d="M370,552 Q366,530 384,528 Q390,512 406,518 Q422,510 428,528 Q444,532 432,552 Z" fill="#FFFFFF" stroke="{C['blue']}" stroke-width="4" opacity="0"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's weigh the sky!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tlw); ink(".in-bs", @tlw2, 0.3, {stagger:0.08});
pop("#in-cl", @tsk, {from:{y:-60}, to:{}});
""", tmw=tmw, tu=tmw + 0.3, tlw=tlw - 0.1, tlw2=tlw + 0.1, tsk=tsk + 0.2))

# 4 SQUARE — 1 m2 square inks on the ground, air column grows, ~10 tons card, a pile of ten small cars
s = "square"; tdr = aw(s, "draw one"); tsm = aw(s, "square meter"); tcol = aw(s, "tall column"); t10 = aw(s, "ten tons"); tcar = aw(s, "ten small cars")
SQ = "M520,890 L860,890 L960,800 L620,800 Z"
rs = _r.Random(42)
dots = []
while len(dots) < 110:
    y = 160 + 640 * (1 - rs.random() ** 1.8)   # denser near the ground
    x = 570 + rs.uniform(0, 340) + (800 - y) * 0
    dots.append((x, y))
stip = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rs.uniform(3,5):.1f}" fill="{C["blue"]}" opacity=".55"/>' for x, y in dots)
cols = ["#FFC9C2", "#BFE3F7", C['hi'], "#C9E8B8", "#E3D1F2"]
cars = "".join(car(70 + (i % 2) * 150, 860 - (i // 2) * 62, "sq-car", cols[i % 5]) for i in range(10))
scenes[s] = scene_file(s, f"""
#sq-svg {{ position:absolute; left:0; top:0; }}
#sq-card {{ position:absolute; left:60px; top:170px; width:400px; height:150px; opacity:0; }}
#sq-card .big {{ position:absolute; left:0; right:0; top:22px; text-align:center; font-size:96px; color:{C['red']}; }}
""", f"""
  <svg id="sq-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="sq-gnd" d="M440,890 L1040,890" stroke="{C['pencil']}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <g id="sq-col" opacity="0"><path d="M570,845 L910,845 L910,160 L570,160 Z" fill="#E6F3FB" stroke="{C['blue']}" stroke-width="4" stroke-dasharray="14 10"/>{stip}</g>
    <path id="sq-sqf" d="{SQ}" fill="{C['hi']}" stroke="none" opacity="0"/>
    <path id="sq-sq" d="{SQ}" stroke="{K}" stroke-width="6" fill="none" stroke-linejoin="round"/>
    <text id="sq-lab" x="740" y="862" text-anchor="middle" font-family="Gochi Hand" font-size="50" fill="{K}" opacity="0">1 m²</text>
    <path id="sq-up" d="M960,780 L960,190 M940,214 L960,184 L980,214" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    {cars}
  </svg>
  <div id="sq-card" class="card"><div class="big">≈ 10 tons</div></div>
  {tape("sq-tp", "column of air", 610, 470, -4, 48, "rgba(191,227,247,.95)")}
  {tape("sq-x", "= 10 small cars", 60, 360, 3, 46)}
""", J("""
ink("#sq-gnd", 0.1, 0.4);
ink("#sq-sq", @tdr, 0.8); tl.to("#sq-sqf", {opacity:0.7, duration:0.3}, @tsm); rise("#sq-lab", @tsm);
tl.set("#sq-col", {opacity:1}, @tcol); tl.fromTo("#sq-col", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.9, ease:"power2.out"}, @tcol);
ink("#sq-up", @tcol2, 0.6); rise("#sq-tp", @tcol3);
pop("#sq-card", @t10, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo(".sq-car", {opacity:0, y:-80}, {opacity:1, y:0, duration:0.25, stagger:0.09, ease:"back.out(2)"}, @tcar);
rise("#sq-x", @tcar2);
""", tdr=tdr, tsm=tsm, tcol=tcol, tcol2=tcol + 0.3, tcol3=tcol + 0.9, t10=t10 - 0.05, tcar=tcar - 0.2, tcar2=tcar + 0.6))

# 5 HALF — altitude ruler; air dots fall and pile densely near the ground; half below 5.5 km; Everest at 8.8 km
s = "half"; tsq = aw(s, "squashed"); thf = aw(s, "half of it"); t55 = aw(s, "five and a"); tev = aw(s, "Mount Everest"); t23 = aw(s, "two thirds"); d = SC[s]["slot"]
RX, Y0, PXK = 470, 900, 44.0   # ruler x, ground y, px per km (0..16 km)
ky = lambda km: Y0 - km * PXK
ticks = "".join(f'<path class="hf-tk" d="M{RX},{ky(k):.0f} L{RX + (26 if k % 4 == 0 else 14)},{ky(k):.0f}" stroke="{K}" stroke-width="{5 if k % 4 == 0 else 3}" fill="none" stroke-linecap="round"/>' for k in range(17))
labs = "".join(f'<text class="hf-tl" x="{RX - 14}" y="{ky(k) + 14:.0f}" text-anchor="end" font-family="Patrick Hand" font-size="38" fill="{K}" opacity="0">{k} km</text>' for k in (0, 4, 8, 12, 16))
rs = _r.Random(55)
air = []
while len(air) < 150:
    km = -7.4 * _m.log(1 - rs.random() * (1 - _m.exp(-16 / 7.4)))   # scale-height ~7.4 km, truncated at 16 km
    air.append((rs.uniform(520, 1010), ky(km) - 5))
adots = "".join(f'<circle class="hf-d" cx="{x:.0f}" cy="0" data-y="{y:.0f}" data-t="{rs.uniform(0,0.8):.2f}" r="6" fill="{C["blue"]}" opacity=".7"/>' for x, y in air)
EV = f"M560,{Y0} L700,{ky(5.2):.0f} L740,{ky(6.4):.0f} L800,{ky(8.8):.0f} L860,{ky(6.8):.0f} L900,{ky(7.4):.0f} L1010,{Y0}"
scenes[s] = scene_file(s, f"""
#hf-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <svg id="hf-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <rect id="hf-band" x="{RX + 30}" y="{ky(5.5):.0f}" width="{1030 - RX - 30}" height="{5.5 * PXK:.0f}" fill="{C['hi']}" opacity="0"/>
    <path id="hf-l55" d="M{RX},{ky(5.5):.0f} L1030,{ky(5.5):.0f}" stroke="{C['red']}" stroke-width="5" stroke-dasharray="14 10" fill="none"/>
    <path id="hf-ev" d="{EV}" fill="#E8E1D6" stroke="{K}" stroke-width="6" stroke-linejoin="round" opacity="0"/>
    <path id="hf-evs" d="M760,{ky(7.3):.0f} L800,{ky(8.8):.0f} L835,{ky(7.7):.0f} L815,{ky(7.4):.0f} L795,{ky(7.8):.0f} L775,{ky(7.2):.0f} Z" fill="#FFFFFF" stroke="{K}" stroke-width="3" opacity="0"/>
    <g id="hf-flag" opacity="0"><path d="M800,{ky(8.8):.0f} L800,{ky(8.8) - 70:.0f}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
      <path d="M800,{ky(8.8) - 68:.0f} L850,{ky(8.8) - 56:.0f} L800,{ky(8.8) - 44:.0f} Z" fill="{C['red']}" stroke="{K}" stroke-width="3"/></g>
    {adots}
    <path id="hf-rl" d="M{RX},{Y0} L{RX},{ky(16):.0f}" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>{ticks}{labs}
    <path id="hf-gnd" d="M{RX},{Y0} L1040,{Y0}" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("hf-half", "half the air", 540, int(ky(2.6)) - 30, -3, 52)}
  {tape("hf-55", "5.5 km", 880, int(ky(5.5)) - 70, 3, 46, "rgba(255,201,194,.95)")}
  {tape("hf-ev2", "≈ 2/3 of the air below!", 560, 280, -2, 44, "rgba(191,227,247,.95)")}
""", SIM + J("""
ink("#hf-rl", 0.05, 0.5); ink(".hf-tk", 0.3, 0.5, {stagger:0.02}); ink("#hf-gnd", 0.2, 0.4);
tl.fromTo(".hf-tl", {opacity:0}, {opacity:1, duration:0.3, stagger:0.06}, 0.5);
const D = Array.from(document.querySelectorAll(".hf-d"));
sim(@d, t => { D.forEach(e => { const k = Math.max(0, Math.min(1, (t - @tsq - (+e.dataset.t))/0.7)); const e2 = 1 - Math.pow(1-k, 3);
  e.setAttribute("cy", (130 + (+e.dataset.y - 130)*e2).toFixed(1)); e.setAttribute("opacity", k > 0 ? 0.7 : 0); }); });
tl.to("#hf-band", {opacity:0.55, duration:0.4}, @thf); rise("#hf-half", @thf2);
ink("#hf-l55", @t55, 0.5); pop("#hf-55", @t55b, {from:{rotation:-10}, to:{rotation:3}});
tl.to("#hf-ev", {opacity:1, duration:0.3}, @tev); tl.to("#hf-evs", {opacity:1, duration:0.3}, @tev2); pop("#hf-flag", @tev2, {from:{y:-30}, to:{}});
rise("#hf-ev2", @t23);
""", d=d, tsq=tsq - 0.3, thf=thf, thf2=thf + 0.3, t55=t55 - 0.1, t55b=t55 + 0.4, tev=tev - 0.1, tev2=tev + 0.3, t23=t23 - 0.1))

# 6 PLANET — 3D Earth sprouts air columns in a wave, camera pulls back; counter to 5 quadrillion tons
s = "planet"; tcv = aw(s, "cover the"); twp = aw(s, "whole planet"); ttot = aw(s, "the total"); t5q = aw(s, "five quadrillion"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#pl-cv {{ position:absolute; left:40px; top:150px; width:1000px; height:560px; }}
#pl-lab {{ position:absolute; left:0; right:0; top:700px; text-align:center; white-space:nowrap; opacity:0; }}
#pl-n {{ font-size:100px; color:{C['red']}; }}
#pl-z {{ position:absolute; left:420px; right:20px; top:840px; text-align:center; font-size:44px; color:{C['muted']}; opacity:0; }}
""", f"""
  <canvas id="pl-cv" width="1000" height="560"></canvas>
  {tape("pl-tp", "whole planet!", 360, 170, -4, 54)}
  <div id="pl-lab"><span id="pl-n" class="big">≈ 5 quadrillion tons</span></div>
  <div id="pl-z">5,000,000,000,000,000 tons</div>
""", EARTH_JS + J("""
const S = T3.stage("#pl-cv", 1000, 560, 34);
const R = 1.7; const earth = buildEarth(S, R, 11);
const rnd = T3.seeded(77); const cols = [];
const cg = new THREE.CylinderGeometry(0.05, 0.05, 1, 6); cg.translate(0, 0.5, 0);
const cm = new THREE.MeshBasicMaterial({color:0xBFE3F7, transparent:true, opacity:0.85});
const N = 260;
for (let i=0;i<N;i++) { const y = 1 - 2*(i + 0.5)/N, r = Math.sqrt(1 - y*y), ph = i*2.39996;
  const v = new THREE.Vector3(r*Math.cos(ph), y, r*Math.sin(ph));
  const m = new THREE.Mesh(cg, cm); m.position.copy(v).multiplyScalar(R*0.99);
  m.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0), v); m.scale.set(1, 0.001, 1);
  earth.userData.body.add(m); cols.push({m, tb: @tcv + rnd()*1.4}); }
const cam = k => { const e = k*k*(3-2*k); const dist = 3.2 + 4.8*e; S.cam.position.set(0.8*(1-e), 0.9*(1-e) + 0.5*e, dist); S.cam.lookAt(0.5*(1-e), 0.7*(1-e), 0); };
drive(@d, t => { cam(Math.min(1, Math.max(0, (t - @tp0)/@pd)));
  earth.userData.body.rotation.y = 0.25*t;
  for (const c of cols) { const k = Math.max(0, Math.min(1, (t - c.tb)/0.4)); c.m.scale.set(1, 0.001 + 0.42*k, 1); }
  S.render(); });
pop("#pl-tp", @twp, {from:{rotation:-12}, to:{rotation:-4}});
tl.to("#pl-tp", {opacity:0, duration:0.2}, @ttot);
pop("#pl-lab", @t5q, {from:{scale:1.5}, to:{}});
rise("#pl-z", @t5q2);
""", d=d, tcv=tcv, tp0=tcv + 0.2, pd=round(ttot - tcv, 3), twp=twp, ttot=ttot, t5q=t5q - 0.05, t5q2=t5q + 0.7))

# 7 BODY — a person doodle inks itself; red arrows dart in from every side; ~18 tons
s = "body"; tw = aw(s, "weird part"); tyb = aw(s, "your body"); t18 = aw(s, "eighteen tons"); trn = aw(s, "right now")
PX, PY = 700, 0
person = [
    "M700,250 C740,250 760,280 760,315 C760,350 740,380 700,380 C660,380 640,350 640,315 C640,280 660,250 700,250 Z",
    "M700,380 L700,620", "M700,430 L600,540", "M700,430 L800,540", "M700,620 L630,820", "M700,620 L770,820"]
ph = "".join(f'<path class="bd-p" d="{p}" stroke="{K}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' for p in person)
arrows = []
for i in range(12):
    a = i / 12 * 2 * _m.pi + 0.2
    cx, cy = 700, 540
    x1, y1 = cx + 330 * _m.cos(a), cy + 310 * _m.sin(a)
    x2, y2 = cx + 220 * _m.cos(a), cy + 220 * _m.sin(a)
    if x1 < 430 and y1 > 700: continue   # keep Max's zone clear
    hx, hy = _m.cos(a), _m.sin(a); nx, ny = -hy, hx
    arrows.append(f'<g class="bd-a" opacity="0"><path d="M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}" stroke="{C["red"]}" stroke-width="8" stroke-linecap="round"/>'
                  f'<path d="M{x2 + 26*hx + 18*nx:.0f},{y2 + 26*hy + 18*ny:.0f} L{x2:.0f},{y2:.0f} L{x2 + 26*hx - 18*nx:.0f},{y2 + 26*hy - 18*ny:.0f}" stroke="{C["red"]}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
scenes[s] = scene_file(s, f"""
#bd-svg {{ position:absolute; left:0; top:0; }}
#bd-lab {{ position:absolute; left:40px; top:200px; width:420px; opacity:0; }}
#bd-lab .big {{ font-size:100px; color:{C['red']}; }}
""", f"""
  <svg id="bd-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <g id="bd-person">{ph}</g>
    {"".join(arrows)}
  </svg>
  {stamp("bd-st", "WEIRD!", 70, 170, -8, 72)}
  <div id="bd-lab"><div class="big">≈ 18 tons</div><div style="font-size:50px">of air pushing on you</div></div>
""", J("""
pop("#bd-st", @tw, {from:{rotation:-20, scale:1.8}, to:{}});
ink(".bd-p", @tyb, 0.35, {stagger:0.1});
tl.to("#bd-st", {opacity:0, duration:0.2}, @t18a);
tl.fromTo(".bd-a", {opacity:0, scale:1.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:0.06, ease:"back.out(2)"}, @t18);
rise("#bd-lab", @t18b);
tl.fromTo("#bd-person", {scaleX:1}, {scaleX:0.94, transformOrigin:"700px 540px", duration:0.12, yoyo:true, repeat:3}, @trn);
""", tw=tw - 0.1, tyb=tyb, t18a=t18 - 0.3, t18=t18 - 0.1, t18b=t18 + 0.4, trn=trn))

# 8 WHY — squashed-flat pancake crossed out; it morphs into a round cutaway: red arrows in, blue arrows out; BALANCED
s = "why"; tsf = aw(s, "squashed flat"); teq = aw(s, "equally"); tev = aw(s, "every side"); tfl = aw(s, "the fluids"); tpb = aw(s, "push right back")
FLAT = "M540,620 C680,620 820,630 820,660 C820,690 680,700 540,700 C400,700 260,690 260,660 C260,630 400,620 540,620 Z"
ROUND = "M540,330 C680,330 780,430 780,560 C780,690 680,790 540,790 C400,790 300,690 300,560 C300,430 400,330 540,330 Z"
ins, outs = [], []
for i in range(8):
    a = i / 8 * 2 * _m.pi + _m.pi / 8
    c, s_ = _m.cos(a), _m.sin(a); nx, ny = -s_, c
    x1, y1, x2, y2 = 540 + 380*c, 560 + 360*s_, 540 + 262*c, 560 + 252*s_
    ins.append(f'<g class="wy-in" opacity="0"><path d="M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f} M{x2+24*c+16*nx:.0f},{y2+24*s_+16*ny:.0f} L{x2:.0f},{y2:.0f} L{x2+24*c-16*nx:.0f},{y2+24*s_-16*ny:.0f}" stroke="{C["red"]}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
    x1, y1, x2, y2 = 540 + 90*c, 560 + 90*s_, 540 + 200*c, 560 + 196*s_
    outs.append(f'<g class="wy-out" opacity="0"><path d="M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f} M{x2-24*c+16*nx:.0f},{y2-24*s_+16*ny:.0f} L{x2:.0f},{y2:.0f} L{x2-24*c-16*nx:.0f},{y2-24*s_-16*ny:.0f}" stroke="{C["blue"]}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
scenes[s] = scene_file(s, f"""
#wy-svg {{ position:absolute; left:0; top:0; }}
#wy-q {{ top:150px; font-size:76px; }}
""", f"""
  <div id="wy-q" class="h1">Why aren't you <span class="hl">squashed flat</span>?</div>
  <svg id="wy-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="wy-b" d="{FLAT}" fill="#FFD6C9" stroke="{K}" stroke-width="7"/>
    <path id="wy-tgt" d="{ROUND}" fill="none" stroke="none"/>
    <g id="wy-face"><circle cx="500" cy="655" r="7" fill="{K}"/><circle cx="580" cy="655" r="7" fill="{K}"/></g>
    <path id="wy-x" d="M250,600 L830,720" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <g id="wy-fl" opacity="0">{"".join(f'<path d="M{430 + 50*k},{520 + (k%2)*90} q14,-18 28,0 q14,18 28,0" stroke="{C["blue"]}" stroke-width="5" fill="none" stroke-linecap="round"/>' for k in range(5))}</g>
    {"".join(ins)}{"".join(outs)}
  </svg>
  {tape("wy-tin", "air pushes in", 610, 250, 3, 44, "rgba(255,201,194,.95)")}
  {tape("wy-tout", "fluids push out", 600, 860, -3, 44, "rgba(191,227,247,.95)")}
  {stamp("wy-st", "BALANCED!", 380, 520, -6, 64, C['blue'])}
""", J("""
rise("#wy-q", 0.05); pop("#wy-b", 0.1, {from:{scaleX:0.6}, to:{}});
ink("#wy-x", @tsf, 0.4);
tl.to("#wy-x, #wy-face", {opacity:0, duration:0.2}, @tq0); tl.to("#wy-q", {opacity:0, y:-20, duration:0.25}, @tq0);
morph("#wy-b", "#wy-tgt", @teq, 0.6, {ease:"back.out(1.4)"});
tl.to("#wy-b", {fill:"#FFE9E2", duration:0.3}, @teq);
tl.fromTo(".wy-in", {opacity:0, scale:1.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.22, stagger:0.06, ease:"back.out(2)"}, @tev);
rise("#wy-tin", @tev2);
tl.to("#wy-fl", {opacity:1, duration:0.3}, @tfl);
tl.fromTo(".wy-out", {opacity:0, scale:0.5, transformOrigin:"540px 560px"}, {opacity:1, scale:1, duration:0.3, stagger:0.04, ease:"back.out(2)"}, @tpb);
rise("#wy-tout", @tpb2); pop("#wy-st", @tpb3, {from:{rotation:-20, scale:1.8}, to:{}});
""", tsf=tsf, tq0=teq - 0.5, teq=teq - 0.2, tev=tev - 0.1, tev2=tev + 0.4, tfl=tfl, tpb=tpb - 0.1, tpb2=tpb + 0.3, tpb3=tpb + 0.8))

# 9 POP — plane climbs along a dashed path; big ear; POP! lettering
s = "pop"; tch = aw(s, "push changes"); tep = aw(s, "ears pop"); tpl = aw(s, "plane"); d = SC[s]["slot"]
FP = "M460,840 C600,820 700,660 780,520 C840,420 900,360 1000,330"
scenes[s] = scene_file(s, f"""
#pp-svg {{ position:absolute; left:0; top:0; }}
#pp-pop {{ position:absolute; left:120px; top:520px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="pp-t" class="h1" style="top:150px;font-size:74px">You feel it when it <span class="hl">changes</span></div>
  <svg id="pp-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="pp-path" d="{FP}" stroke="{C['pencil']}" stroke-width="4" fill="none" stroke-dasharray="10 12"/>
    <g id="pp-plane" opacity="0"><path d="M-50,0 Q-40,-14 30,-12 Q52,-10 56,0 Q52,10 30,12 Q-40,14 -50,0 Z" fill="#FFFFFF" stroke="{K}" stroke-width="4"/>
      <path d="M0,-10 L-18,-46 L-4,-46 L18,-10 M0,10 L-18,46 L-4,46 L18,10 M-44,-4 L-58,-24 L-48,-24 L-36,-6" fill="#BFE3F7" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></g>
    <g id="pp-ear" opacity="0"><path d="M200,330 C200,250 270,210 330,230 C390,250 400,320 370,370 C350,400 330,410 330,450 C330,490 290,500 270,480" fill="#FFD6C9" stroke="{K}" stroke-width="7" stroke-linecap="round"/>
      <path d="M260,330 C260,290 300,280 320,300 C340,320 320,350 300,350" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round"/></g>
    <path class="pp-burst" d="M150,560 L110,530 M170,520 L150,470 M220,510 L230,460 M120,610 L70,610" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="pp-pop">POP!</div>
""", J("""
rise("#pp-t", 0.05); ink("#pp-path", 0.2, 0.6);
tl.set("#pp-plane", {opacity:1}, @tch); along("#pp-plane", "#pp-path", @tch, @fly, {ease:"power1.inOut", rotate:true});
pop("#pp-ear", @tep0, {from:{scale:0.5}, to:{}});
pop("#pp-pop", @tep, {from:{scale:2.2, rotation:-20}, to:{rotation:-8}}); ink(".pp-burst", @tep, 0.2);
tl.fromTo("#pp-ear", {rotation:0}, {rotation:6, transformOrigin:"300px 350px", duration:0.06, yoyo:true, repeat:5}, @tep);
""", tch=tch - 0.3, fly=round(d - (tch - 0.3) - 0.3, 3), tep0=tep - 0.8, tep=tep + 0.15))

# 10 OUTRO — red "?" (hook callback) morphs into a weight block; chip; Stay curious (Max centre: keep y < 620)
s = "outro"; t5q = aw(s, "five quadrillion"); tsh = aw(s, "your shoulders"); tsc = aw(s, "stay curious")
QM = "M470,230 Q470,150 540,150 Q610,150 610,215 Q610,262 545,290 L545,350"
WTP = "M470,230 Q470,150 540,150 Q610,150 610,230 L660,230 L700,400 L380,400 L420,230 Z"
scenes[s] = scene_file(s, f"""
#ou-chip {{ position:absolute; left:0; right:0; top:450px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" class="abs" style="left:0;top:0" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <path id="ou-q" d="{QM}" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-wt" d="{WTP}" fill="none" stroke="none"/>
    <circle id="ou-qd" cx="545" cy="420" r="20" fill="{C['red']}" stroke="{K}" stroke-width="7"/>
    <text id="ou-air" x="540" y="350" text-anchor="middle" font-family="Gochi Hand" font-size="64" fill="{K}" opacity="0">AIR</text>
  </svg>
  <div id="ou-chip"><span class="chip">≈ 5 quadrillion tons</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-svg", 0.05, {from:{scale:0.8}, to:{}});
morph("#ou-q", "#ou-wt", @t5q, 0.55, {ease:"back.out(1.4)"});
tl.to("#ou-q", {strokeWidth:8, stroke:"@ink", fill:"@air", duration:0.3}, @t5q);
tl.to("#ou-qd", {opacity:0, scale:0, transformOrigin:"50% 50%", duration:0.2}, @t5q);
tl.to("#ou-air", {opacity:1, duration:0.3}, @t5qb);
pop("#ou-chip", @t5qc, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#ou-svg", {y:0}, {y:10, duration:0.3, yoyo:true, repeat:1, ease:"sine.inOut"}, @tsh);
tl.to("#ou-svg, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
pop("#ou-c", @tsc1);
""", ink=K, air="#E6F3FB", t5q=t5q - 0.05, t5qb=t5q + 0.4, t5qc=t5q + 0.5, tsh=tsh, tsc0=tsc - 0.45, tsc1=tsc - 0.2), fade=False)
# === GESTURES ===
think(g("hook", "how much"), SC["guess"]["start"] + 0.2)
point(g("guess", "few tons"), 2.6)
wave(g("intro", "I'm Max"))
point(g("square", "square meter"), 1.2)
wow(g("square", "ten small cars"), 1.2)
point(g("half", "half of it"), 1.2)
wow(g("planet", "five quadrillion"), 1.5)
point(g("body", "eighteen tons"), 1.2)
think(SC["why"]["start"] + 0.05, g("why", "equally"))
point(g("why", "push right back"), 1.2)
wow(g("pop", "ears pop"), 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "weigh") + 0.1, 0.35), ("click-soft.mp3", A("hook", "look up"), 0.5),
        ("pop.mp3", A("guess", "few tons"), 0.5), ("pop.mp3", A("guess", "billion tons"), 0.5), ("pop.mp3", A("guess", "way way more"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("riser.mp3", A("square", "tall column") - 0.1, 0.2),
        ("impact-bass-1.mp3", A("square", "ten tons"), 0.4), ("click.mp3", A("half", "five and a") + 0.2, 0.45),
        ("pop.mp3", A("half", "Mount Everest") + 0.3, 0.45), ("impact-bass-2.mp3", A("planet", "five quadrillion"), 0.45),
        ("whoosh-short.mp3", A("body", "eighteen tons") - 0.1, 0.35), ("pop.mp3", A("why", "push right back") + 0.8, 0.5),
        ("pop.mp3", A("pop", "ears pop") + 0.15, 0.6), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
