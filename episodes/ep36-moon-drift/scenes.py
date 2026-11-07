# MAX WISE ep36 — Is the Moon running away from Earth?
# Kit: ink / morph / along helpers + two three.js scenes (hook, tides).
# Sources: NASA Goddard "Measuring the Moon's Distance" (eclipse.gsfc.nasa.gov/help/ApolloLaser.html), NASA JPL "Apollo 11 experiment
#  continues to return valuable data" (about 3.8 cm per year, Apollo retroreflectors, tides); Space.com physicist explainer (bulge dragged
#  ahead pulls the Moon into a larger orbit, Earth's spin slows, the Moon will not escape, the Sun boils off the oceans in ~1 billion years);
#  NASA Space Place "How far away is the Moon?" (384,400 km average).
# Maths: 3.8 cm x 80 yr = 304 cm ~ 3 m; 3 m / 384,400 km ~ 8e-9.
# === SCENES ===
import math as _m
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
MOONC = "#D9D5CC"; SEA = "#BFE3F7"; LAND = "#9BD08F"
SIM = """
const sim = (dur, fn) => { const st={t:0}; tl.fromTo(st, {t:0}, {t:dur, duration:dur, ease:"none", onUpdate:()=>fn(st.t)}, 0); fn(0); };
const clamp = v => Math.max(0, Math.min(1, v));
const sm = k => { k = clamp(k); return k*k*(3-2*k); };
"""
def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.92)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 26px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff;white-space:nowrap">{txt}</span></div>')
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
def moon2d(r, craters=True):
    cr = "".join(f'<circle cx="{r*dx:.1f}" cy="{r*dy:.1f}" r="{r*rr:.1f}" fill="#BDB8AE" stroke="{K}" stroke-width="3"/>'
                 for dx, dy, rr in [(-0.35, -0.3, 0.2), (0.3, 0.2, 0.16), (-0.1, 0.45, 0.12), (0.4, -0.35, 0.1)]) if craters else ""
    return f'<circle cx="0" cy="0" r="{r}" fill="{MOONC}" stroke="{K}" stroke-width="5"/>{cr}'
def earth2d(cx, cy, r, idp):
    return (f'<clipPath id="{idp}-clip"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SEA}" stroke="{K}" stroke-width="5"/>'
            f'<g clip-path="url(#{idp}-clip)"><path d="M{cx-r*0.7:.0f},{cy-r*0.3:.0f} Q{cx-r*0.3:.0f},{cy-r*0.75:.0f} {cx+r*0.05:.0f},{cy-r*0.45:.0f} Q{cx+r*0.15:.0f},{cy-r*0.05:.0f} {cx-r*0.25:.0f},{cy+r*0.05:.0f} Q{cx-r*0.6:.0f},{cy+r*0.1:.0f} {cx-r*0.7:.0f},{cy-r*0.3:.0f} Z" fill="{LAND}" stroke="{K}" stroke-width="4"/>'
            f'<path d="M{cx+r*0.25:.0f},{cy+r*0.3:.0f} Q{cx+r*0.7:.0f},{cy+r*0.15:.0f} {cx+r*0.75:.0f},{cy+r*0.5:.0f} Q{cx+r*0.55:.0f},{cy+r*0.85:.0f} {cx+r*0.3:.0f},{cy+r*0.7:.0f} Z" fill="{LAND}" stroke="{K}" stroke-width="4"/></g>')

# shared 3D builders: toon Earth with land patches, lumpy grey Moon with craters (seeded)
WORLD_JS = """
function makeEarth(R) {
  const g = T3.inked(new THREE.SphereGeometry(R, 48, 32), 0x4F9BE0, 0.05); const rnd = T3.seeded(5);
  for (let i=0;i<9;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(R*(0.24+rnd()*0.2), 20, 14), T3.toon(0x7CC46A));
    m.position.setFromSphericalCoords(R*0.93, 0.45+rnd()*2.2, rnd()*6.283); m.scale.set(1,1,0.3); m.lookAt(0,0,0); g.userData.body.add(m); }
  return g;
}
function makeMoon(R) {
  const geo = new THREE.SphereGeometry(R, 40, 28); const p = geo.attributes.position, v = new THREE.Vector3(); const rnd = T3.seeded(9);
  const bumps = Array.from({length:6}, () => [rnd()*6.283, rnd()*3.14]);
  for (let i=0;i<p.count;i++) { v.fromBufferAttribute(p,i); const th=Math.acos(Math.max(-1, Math.min(1, v.y/R))), ph=Math.atan2(v.z,v.x); let k=1;
    for (const [a,b] of bumps) k += 0.012*Math.cos(3*(ph-a))*Math.sin(2*(th-b)); v.multiplyScalar(k); p.setXYZ(i,v.x,v.y,v.z); }
  geo.computeVertexNormals();
  const g = T3.inked(geo, 0xD9D5CC, 0.07);
  for (let i=0;i<6;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(R*(0.16+rnd()*0.12), 14, 10), T3.toon(0xA8A398));
    m.position.setFromSphericalCoords(R*0.95, 0.5+rnd()*2.1, rnd()*6.283); m.scale.set(1,1,0.3); m.lookAt(0,0,0); g.userData.body.add(m); }
  return g;
}
"""

# 1 HOOK — 3D Earth, Moon on a widening dotted orbit
s = "hook"; tq = aw(s, "is the moon"); trun = aw(s, "running away"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:84px; }}
#hk-cv {{ position:absolute; left:40px; top:330px; width:1000px; height:600px; }}
#hk-qm {{ position:absolute; left:830px; top:360px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-q" class="h1">Is the Moon <span class="hl">running away</span>?</div>
  <canvas id="hk-cv" width="1000" height="600"></canvas>
  <div id="hk-qm">?</div>
""", WORLD_JS + J("""
const S = T3.stage("#hk-cv", 1000, 600, 34); S.cam.position.set(0.4, 4.6, 9.6); S.cam.lookAt(0.4, -0.3, 0);
const earth = makeEarth(1.25); S.scene.add(earth); earth.rotation.z = 0.35;
const moon = makeMoon(0.42); S.scene.add(moon);
const dots = []; for (let i=0;i<64;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.035, 8, 6), new THREE.MeshBasicMaterial({color:0x262A3B})); S.scene.add(m); dots.push(m); }
drive(@d, t => {
  const s = t < 0.5 ? 0.6 + 0.4*gsap.parseEase("back.out(2)")(t/0.5) : 1;
  earth.scale.setScalar(s); earth.userData.body.rotation.y = 0.9*t;
  const r = 3.0 + 0.4*Math.max(0, t - @tr0), a = 0.5 + 0.55*t;
  moon.position.set(r*Math.cos(a), 0, -r*Math.sin(a)); moon.rotation.y = a; moon.scale.setScalar(s);
  dots.forEach((m, i) => { const b = i/64*6.2832; m.position.set(r*Math.cos(b), 0, -r*Math.sin(b)); m.visible = t > 0.3; });
  S.render();
});
rise("#hk-q", @tq);
pop("#hk-qm", @trun, {from:{rotation:-20}, to:{rotation:8}});
""", d=d, tr0=trun - 0.3, tq=tq - 0.3, trun=trun + 0.2))

# 2 GUESS — three sticky notes with inked doodles
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "staying put"); t2 = aw(s, "coming closer"); t3 = aw(s, "drifting away")
notes = [("a", "Staying put?", -6, 110, C['hi']), ("b", "Coming closer?", 4, 405, "#BFE3F7"), ("c", "Drifting away?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:330px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:56px;line-height:1.05;padding:40px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
doodles = f'''
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <g transform="translate(205,610) rotate(-6)"><circle cx="-36" cy="0" r="22" fill="{SEA}" stroke="{K}" stroke-width="4"/><circle cx="36" cy="0" r="11" fill="{MOONC}" stroke="{K}" stroke-width="4"/>
      <path id="gs-da" d="M-6,-18 L6,-18 M-6,18 L6,18" {WS}/></g>
    <g transform="translate(540,610) rotate(4)"><circle cx="-60" cy="0" r="22" fill="{SEA}" stroke="{K}" stroke-width="4"/><circle cx="60" cy="0" r="11" fill="{MOONC}" stroke="{K}" stroke-width="4"/>
      <path class="gs-db" d="M38,0 L-30,0" {WS}/><path class="gs-db" d="M-14,-12 L-30,0 L-14,12" {WS}/></g>
    <g transform="translate(838,610) rotate(-3)"><circle cx="-70" cy="0" r="22" fill="{SEA}" stroke="{K}" stroke-width="4"/><circle cx="-10" cy="0" r="11" fill="{MOONC}" stroke="{K}" stroke-width="4"/>
      <path class="gs-dc" d="M8,0 L72,0" {WS}/><path class="gs-dc" d="M56,-12 L72,0 L56,12" {WS}/></g>
  </svg>'''
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink("#gs-da", @ta, 0.3); ink(".gs-db", @tb, 0.35, {stagger:0.15}); ink(".gs-dc", @tc, 0.35, {stagger:0.15});
""", tg=tg, t1=t1, t2=t2, t3=t3, ta=t1 + 0.25, tb=t2 + 0.25, tc=t3 + 0.25))

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tls = aw(s, "let's measure"); tlz = aw(s, "laser")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="300" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="in-beam" d="M150,250 L300,190 L450,250 L600,190 L750,250 L930,180" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's measure it!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tls); ink("#in-beam", @tb, 0.5, {ease:"power2.out"});
""", tmw=tmw, tu=tmw + 0.3, tls=tls, tb=tlz - 0.1))

# 4 MIRROR — Apollo mirror, laser up and back, stopwatch
s = "mirror"; tap = aw(s, "Apollo"); tmi = aw(s, "mirrors"); tbo = aw(s, "bounce lasers"); ttm = aw(s, "time the trip")
cells = "".join(f'<rect x="{-54+i*27}" y="{-40+j*27}" width="27" height="27" fill="#E8F3FB" stroke="{K}" stroke-width="3"/>' for i in range(4) for j in range(3))
tks = "".join(f'<path d="M0,-80 L0,{-66 if i%3 else -60}" transform="rotate({i*30})" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(12))
scenes[s] = scene_file(s, f"""
#mr-svg {{ position:absolute; left:0; top:150px; }}
""", f"""
  <svg id="mr-svg" width="{W}" height="820" viewBox="0 0 {W} 820" data-layout-ignore>
    <g transform="translate(800,240)"><g id="mr-moon">{moon2d(200, False)}
      <circle cx="-120" cy="-80" r="30" fill="#BDB8AE" stroke="{K}" stroke-width="3"/><circle cx="110" cy="70" r="22" fill="#BDB8AE" stroke="{K}" stroke-width="3"/></g></g>
    <g transform="translate(740,330) rotate(-8)"><g id="mr-panel">{cells}<rect x="-54" y="-40" width="108" height="81" fill="none" stroke="{K}" stroke-width="5"/></g></g>
    <path id="mr-ground" d="M420,800 Q740,700 1080,760" stroke="{K}" stroke-width="6" fill="{SEA}" />
    <g transform="translate(560,700)"><g id="mr-tel"><path d="M-40,40 L0,0 L40,40" {WS}/><g transform="rotate(22)"><rect x="-22" y="-90" width="44" height="100" rx="8" fill="#FFFFFF" stroke="{K}" stroke-width="5"/></g></g></g>
    <path id="mr-beam" d="M620,640 L740,330" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="mr-trip" d="M620,640 L740,330 L620,640" fill="none" stroke="none"/>
    <g id="mr-dot" opacity="0"><circle r="26" fill="#FF8A7A" opacity=".45"/><circle r="13" fill="{C['red']}" stroke="{K}" stroke-width="4"/></g>
    <g id="mr-watch" transform="translate(220,200)" opacity="0"><path d="M-14,-104 L14,-104 M0,-104 L0,-88" {WS}/>
      <circle r="86" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>{tks}<g id="mr-hand"><path d="M0,0 L0,-62" stroke="{C['red']}" stroke-width="7" stroke-linecap="round"/></g><circle r="7" fill="{K}"/></g>
  </svg>
  {tape("mr-t1", "Apollo mirror", 300, 470, -4, 48)}
  {tape("mr-t2", "laser", 700, 690, 3, 44, "rgba(255,201,194,.95)")}
  {tape("mr-t3", "time it!", 120, 470, -3, 46)}
""", J("""
pop("#mr-moon", 0.05, {from:{scale:0.7}, to:{}});
pop("#mr-panel", @tmi); rise("#mr-t1", @tmi1);
pop("#mr-tel", @tbo0); ink("#mr-beam", @tbo, 0.45); rise("#mr-t2", @tbo1);
tl.set("#mr-dot", {opacity:1}, @tbo1); along("#mr-dot", "#mr-trip", @tbo1, @lap, {ease:"none", repeat:2});
tl.set("#mr-dot", {opacity:0}, @tdend);
tl.to("#mr-watch", {opacity:1, duration:0.2}, @ttm0); tl.set("#mr-hand", {rotation:0, svgOrigin:"0 0"}, 0);
tl.to("#mr-hand", {rotation:360, duration:1.0, ease:"power1.inOut"}, @ttm); rise("#mr-t3", @ttm);
""", tmi=tmi - 0.1, tmi1=tmi + 0.3, tbo0=tbo - 0.5, tbo=tbo - 0.1, tbo1=tbo + 0.35, lap=0.6, tdend=tbo + 0.35 + 1.8, ttm0=ttm - 0.4, ttm=ttm))

# 5 DRIFT — ruler, Moon slides to 3.8 cm, counter
s = "drift"; tan = aw(s, "the answer"); t38 = aw(s, "three point eight"); tfar = aw(s, "farther away"); tey = aw(s, "every year")
X0, CM, RY = 110, 170, 300
rt = "".join(f'<path d="M{X0+i*CM/10:.1f},{RY} L{X0+i*CM/10:.1f},{RY+(54 if i%10==0 else 34 if i%5==0 else 20)}" stroke="{K}" stroke-width="{4 if i%10==0 else 3}" stroke-linecap="round"/>' for i in range(51))
rn = "".join(f'<text x="{X0+i*CM}" y="{RY+100}" text-anchor="middle" font-family="Patrick Hand" font-size="40" fill="{K}">{i}</text>' for i in range(6))
scenes[s] = scene_file(s, f"""
#dr-svg {{ position:absolute; left:0; top:150px; }}
#dr-ans {{ position:absolute; left:0; right:0; top:610px; text-align:center; }}
#dr-n {{ font-size:150px; color:{C['red']}; }}
#dr-chip {{ position:absolute; left:0; right:0; top:785px; text-align:center; }}
""", f"""
  <div id="dr-title" class="h1" style="top:150px;font-size:76px">The answer…</div>
  <svg id="dr-svg" width="{W}" height="450" viewBox="0 0 {W} 450" data-layout-ignore>
    <rect id="dr-body" x="{X0-30}" y="{RY}" width="{5*CM+60}" height="120" fill="#FFF3C4" stroke="{K}" stroke-width="5" rx="6"/>
    <rect id="dr-bar" x="{X0}" y="{RY-26}" width="{3.8*CM:.1f}" height="20" fill="{C['red']}" opacity=".85"/>
    {rt}{rn}
    <text x="{X0+5*CM+10}" y="{RY+100}" font-family="Patrick Hand" font-size="34" fill="{C['muted']}">cm</text>
    <g transform="translate({X0},{RY-100})"><g id="dr-moon">{moon2d(62)}</g></g>
  </svg>
  <div id="dr-ans"><span id="dr-n" class="big">0.0</span><span class="big" style="font-size:90px"> cm</span></div>
  <div id="dr-chip"><span class="chip">farther away every year</span></div>
""", J("""
rise("#dr-title", @tan); rise("#dr-svg", 0.05);
tl.fromTo("#dr-moon", {x:0}, {x:@dx, duration:1.4, ease:"power2.inOut"}, @t38);
tl.fromTo("#dr-bar", {scaleX:0, svgOrigin:"@bx0 @by0"}, {scaleX:1, duration:1.4, ease:"power2.inOut"}, @t38);
rise("#dr-ans", @t38a); count("#dr-n", 0, 3.8, @t38, 1.4, v => (Math.round(v*10)/10).toFixed(1));
pop("#dr-chip .chip", @tfar, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#dr-chip .chip", {scale:1}, {scale:1.1, duration:0.14, yoyo:true, repeat:1}, @tey);
""", tan=tan, t38=t38 - 0.1, t38a=t38 - 0.3, dx=round(3.8 * CM, 1), bx0=X0, by0=RY, tfar=tfar, tey=tey))

# 6 TIDES — 3D top-down Earth with ocean bulge dragged ahead of the Moon
s = "tides"; twhy = aw(s, "why"); tgrav = aw(s, "gravity"); tbul = aw(s, "bulge"); tspin = aw(s, "spins fast"); tdrag = aw(s, "drags"); tahd = aw(s, "ahead"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#td-cv {{ position:absolute; left:40px; top:200px; width:1000px; height:700px; }}
#td-arc {{ position:absolute; left:40px; top:200px; }}
#td-why {{ position:absolute; left:90px; top:150px; }}
""", f"""
  <canvas id="td-cv" width="1000" height="700"></canvas>
  <svg id="td-arc" width="1000" height="700" viewBox="0 0 1000 700" data-layout-ignore>
    <path id="td-spin" d="M0,0 L1,1" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="td-spinh" d="M0,0 L1,1" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="td-pull" d="M0,0 L1,1" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="14 12"/>
  </svg>
  <div id="td-why"><span class="chip">Why?</span></div>
  {tape("td-t1", "ocean bulge", 0, 0, -4, 46, "rgba(191,227,247,.95)")}
  {tape("td-t2", "Moon", 0, 0, 3, 46)}
  {tape("td-t3", "ahead!", 0, 0, -6, 52, "rgba(255,201,194,.95)")}
""", WORLD_JS + SIM + J("""
const S = T3.stage("#td-cv", 1000, 700, 34); S.cam.position.set(0.9, 12.5, 2.6); S.cam.lookAt(0.9, 0, -0.2);
const R = 1.45, D = 4.6;
const earth = makeEarth(R); S.scene.add(earth);
const bulge = T3.inked(new THREE.SphereGeometry(R, 48, 32), 0x9FD8F5, 0.03); S.scene.add(bulge);
const moon = makeMoon(0.55); S.scene.add(moon);
const mA = t => 0.10 + 0.03*t;                       // Moon creeps along its orbit (counter-clockwise from above)
const pr = (v) => { const q = v.clone().project(S.cam); return [(q.x+1)*500, (1-q.y)*350]; };
S.cam.updateMatrixWorld();
const P = (a, r) => new THREE.Vector3(r*Math.cos(a), 0, -r*Math.sin(a));
// overlay positions (projected once)
const c0 = pr(new THREE.Vector3(0,0,0)), mEnd = pr(P(mA(@d), D)), bEnd = pr(P(mA(@d)+0.5, R*1.75));
const arcR = 225, a0 = 2.3, a1 = 3.9;   // spin arrow round Earth, in screen space
const ap = (a) => [c0[0] + arcR*Math.cos(a), c0[1] - arcR*Math.sin(a)];
const [sx, sy] = ap(a0), [ex, ey] = ap(a1);
document.getElementById("td-spin").setAttribute("d", `M${sx.toFixed(1)},${sy.toFixed(1)} A${arcR},${arcR} 0 0 0 ${ex.toFixed(1)},${ey.toFixed(1)}`);
const hx = ex, hy = ey; const tg = [Math.sin(a1), Math.cos(a1)];  // tangent direction of travel (counter-clockwise on screen)
document.getElementById("td-spinh").setAttribute("d", `M${(hx - 26*tg[0] - 22*tg[1]).toFixed(1)},${(hy - 26*tg[1] + 22*tg[0]).toFixed(1)} L${hx.toFixed(1)},${hy.toFixed(1)} L${(hx - 26*tg[0] + 22*tg[1]).toFixed(1)},${(hy - 26*tg[1] - 22*tg[0]).toFixed(1)}`);
document.getElementById("td-pull").setAttribute("d", `M${(c0[0]+60).toFixed(1)},${c0[1].toFixed(1)} L${(mEnd[0]-70).toFixed(1)},${mEnd[1].toFixed(1)}`);
gsap.set("#td-t1", {left: 40 + c0[0] - 330, top: 200 + c0[1] + 150});
gsap.set("#td-t2", {left: 40 + mEnd[0] - 80, top: 200 + mEnd[1] + 70});
gsap.set("#td-t3", {left: 40 + bEnd[0] - 40, top: 200 + bEnd[1] - 130});
drive(@d, t => {
  const ma = mA(t); moon.position.copy(P(ma, D)); moon.rotation.y = ma;
  earth.userData.body.rotation.y = 0.15*t + 1.1*Math.max(0, t - @tspin);
  const g = sm((t - @tb0)/0.8); bulge.scale.set(1 + 0.42*g, 0.86, 0.86);   // x = Earth-Moon axis
  bulge.rotation.y = ma + 0.5*sm((t - @tdrag)/1.3);
  bulge.visible = g > 0.02;
  S.render();
});
pop("#td-why .chip", @twhy, {from:{rotation:-12}, to:{rotation:-4}});
ink("#td-pull", @tgrav, 0.6); rise("#td-t2", @tgrav);
rise("#td-t1", @tbul);
ink("#td-spin", @tspin, 0.6); ink("#td-spinh", @tspinh, 0.2);
pop("#td-t3", @tahd, {from:{rotation:-20}, to:{rotation:0}});
""", d=d, tspin=tspin, tb0=tbul - 0.5, tdrag=tdrag, twhy=twhy, tgrav=tgrav, tbul=tbul + 0.3, tspinh=tspin + 0.6, tahd=tahd))

# 7 TUG — bulge tugs the Moon forward; orbit morphs bigger, Moon spirals out
s = "tug"; tbg = aw(s, "that bulge"); ttug = aw(s, "tugs"); tfw = aw(s, "forward"); tnud = aw(s, "nudges"); tbig = aw(s, "bigger orbit")
CX, CY = 540, 420
def circ(r): return f"M{CX+r},{CY} A{r},{r} 0 1 0 {CX-r},{CY} A{r},{r} 0 1 0 {CX+r},{CY}"
mx0, my0 = CX + 230, CY
scenes[s] = scene_file(s, f"""
#tg-svg {{ position:absolute; left:0; top:130px; }}
""", f"""
  <svg id="tg-svg" width="{W}" height="840" viewBox="0 0 {W} 840" data-layout-ignore>
    <path id="tg-orb" d="{circ(230)}" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-dasharray="12 12"/>
    <path id="tg-orb2" d="{circ(320)}" fill="none" stroke="none"/>
    <g transform="translate({CX},{CY}) rotate(-28)"><ellipse cx="0" cy="0" rx="128" ry="80" fill="#DDF1FB" stroke="{K}" stroke-width="4" stroke-dasharray="8 7"/></g>
    {earth2d(CX, CY, 88, "tg-e")}
    <path id="tg-spiral" d="M{mx0},{my0} C{mx0+20},{my0-120} {CX+230},{CY-260} {CX+80},{CY-315}" fill="none" stroke="none"/>
    <path id="tg-arr" d="M{mx0+80},{my0+10} L{mx0+80},{my0-150}" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="tg-arrh" d="M{mx0+58},{my0-122} L{mx0+80},{my0-150} L{mx0+102},{my0-122}" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="tg-rope" d="M{CX+100},{CY-55} Q{CX+170},{CY-60} {mx0-40},{my0-20}" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="4 10"/>
    <g id="tg-moon">{moon2d(42)}</g>
  </svg>
  {stamp("tg-tug", "TUG!", 860, 600, -10, 70)}
  {tape("tg-t1", "bulge", 300, 640, -4, 46, "rgba(191,227,247,.95)")}
  {tape("tg-t2", "bigger orbit", 90, 170, -3, 52)}
""", J("""
tl.set("#tg-moon", {x:@mx0, y:@my0}, 0);
rise("#tg-t1", @tbg); ink("#tg-rope", @tbg2, 0.5);
ink("#tg-arr", @ttug, 0.4); ink("#tg-arrh", @tarh, 0.15); pop("#tg-tug", @ttug2, {from:{rotation:-25, scale:1.6}, to:{rotation:-10}});
tl.to("#tg-arr, #tg-arrh, #tg-rope", {opacity:0, duration:0.2}, @tnud);
morph("#tg-orb", "#tg-orb2", @tnud, 1.3, {ease:"power2.inOut"});
along("#tg-moon", "#tg-spiral", @tnud, 1.3, {ease:"power2.inOut"});
tl.to("#tg-tug", {opacity:0, duration:0.2}, @tnud);
pop("#tg-t2", @tbig, {from:{rotation:-15}, to:{rotation:-3}});
""", mx0=float(mx0), my0=float(my0), tbg=tbg, tbg2=tbg + 0.2, ttug=ttug - 0.05, tarh=ttug + 0.35, ttug2=ttug, tnud=tnud - 0.1, tbig=tbig))

# 8 BRAKE — Earth's spin decays (land slides past slower), SCREECH, day bar grows a sliver
s = "brake"; tsp = aw(s, "spin"); tbr = aw(s, "brakes"); tdy = aw(s, "our days"); ttb = aw(s, "tiny bit"); d = SC[s]["slot"]
ER, ECX, ECY = 230, 540, 420
land = "".join(f'<path class="bk-land" d="M{x},{y} q{a},{-b} {2*a},0 q{a//2},{b} {-a//2},{b+30} q{-a},{20} {-3*a//2},{-30} z" fill="{LAND}" stroke="{K}" stroke-width="4"/>'
               for x, y, a, b in [(-60, 330, 70, 60), (150, 470, 60, 40), (330, 360, 50, 70), (-250, 450, 55, 45), (-420, 340, 60, 50)])
scenes[s] = scene_file(s, f"""
#bk-svg {{ position:absolute; left:0; top:150px; }}
#bk-lab {{ position:absolute; left:440px; top:705px; font-size:46px; }}
#bk-plus {{ position:absolute; left:640px; top:835px; white-space:nowrap; font-size:44px; color:{C['red']}; opacity:0; }}
""", f"""
  <svg id="bk-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <clipPath id="bk-clip"><circle cx="{ECX}" cy="{ECY - 150}" r="{ER}"/></clipPath>
    <circle cx="{ECX}" cy="{ECY - 150}" r="{ER}" fill="{SEA}" stroke="{K}" stroke-width="6"/>
    <g clip-path="url(#bk-clip)"><g id="bk-roll" transform="translate({ECX},{ECY - 150 - 380})">{land}<g transform="translate(-1000,0)">{land}</g><g transform="translate(1000,0)">{land}</g></g></g>
    <circle cx="{ECX}" cy="{ECY - 150}" r="{ER}" fill="none" stroke="{K}" stroke-width="6"/>
    <path id="bk-arc" d="M{ECX - 200},{ECY - 150 + 175} Q{ECX},{ECY - 150 + 300} {ECX + 200},{ECY - 150 + 175}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="bk-arch" d="M{ECX + 168},{ECY - 150 + 172} L{ECX + 200},{ECY - 150 + 175} L{ECX + 186},{ECY - 150 + 205}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <g id="bk-bar" opacity="0"><rect x="440" y="610" width="440" height="60" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>
      <rect id="bk-sliver" x="880" y="610" width="36" height="60" fill="url(#bk-hatch)" stroke="{C['red']}" stroke-width="4"/></g>
    <defs><pattern id="bk-hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="10" fill="{C['red']}"/></pattern></defs>
  </svg>
  {stamp("bk-scr", "SCREECH!", 690, 160, 8, 64)}
  <div id="bk-lab" style="opacity:0">a day</div>
  <div id="bk-plus">a tiny bit longer</div>
""", SIM + J("""
const roll = document.getElementById("bk-roll");
sim(@d, t => { // spin speed decays after "brakes": position = integral of speed
  const v0 = 520, tb = @tbr; let x;
  if (t < tb) x = v0*t; else { const k = 0.9; x = v0*tb + v0*(1 - Math.exp(-k*(t - tb)))/k; }
  const xx = ((x % 1000) + 1000) % 1000;
  roll.setAttribute("transform", `translate(${(@ecx + xx).toFixed(1)},@ecy)`);
});
ink("#bk-arc", @tsp, 0.5); ink("#bk-arch", @tsp2, 0.15);
pop("#bk-scr", @tbr, {from:{rotation:20, scale:1.6}, to:{rotation:8}});
tl.fromTo("#bk-scr span", {x:0}, {x:8, duration:0.05, yoyo:true, repeat:7}, @tbr2);
tl.to("#bk-bar", {opacity:1, duration:0.2}, @tdy); rise("#bk-lab", @tdy);
tl.fromTo("#bk-sliver", {scaleX:0, svgOrigin:"880 640"}, {scaleX:1, duration:0.6, ease:"back.out(2)"}, @ttb);
rise("#bk-plus", @ttb2);
""", d=d, tbr=tbr, tbr2=tbr + 0.3, ecx=float(ECX - 500), ecy=float(ECY - 150 - 420), tsp=tsp - 0.3, tsp2=tsp + 0.2, tdy=tdy - 0.2, ttb=ttb, ttb2=ttb + 0.3))

# 9 LIFE — 80 years -> ~3 m, out of ~384,000 km
s = "life"; t80 = aw(s, "eighty year"); t3m = aw(s, "three meters"); tout = aw(s, "out of"); t384 = aw(s, "three hundred eighty")
TX0, TPX = 130, 250
tm = "".join(f'<path d="M{TX0+i*TPX/10:.1f},300 L{TX0+i*TPX/10:.1f},{300+(40 if i%10==0 else 18)}" stroke="{K}" stroke-width="{4 if i%10==0 else 2.5}"/>' for i in range(31))
tn = "".join(f'<text x="{TX0+i*TPX+ (14 if i==0 else 0)}" y="390" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{i} m</text>' for i in range(4))
scenes[s] = scene_file(s, f"""
#lf-svg {{ position:absolute; left:0; top:0; }}
#lf-title {{ top:150px; font-size:74px; }}
#lf-3m {{ position:absolute; left:0; right:0; top:410px; text-align:center; }}
#lf-3m .big {{ font-size:100px; color:{C['red']}; }}
#lf-km {{ position:absolute; left:0; right:0; top:760px; text-align:center; }}
#lf-kn {{ font-size:84px; color:{C['blue']}; }}
""", f"""
  <div id="lf-title" class="h1">An <span class="hl">80-year</span> lifetime</div>
  <svg id="lf-svg" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <g id="lf-tape"><rect x="{TX0}" y="290" width="{3*TPX}" height="60" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>{tm}</g>
    <rect x="{TX0-85}" y="270" width="70" height="100" rx="14" fill="#E0483C" stroke="{K}" stroke-width="5"/>
    {tn}
    <g transform="translate(150,680)"><circle r="62" fill="{SEA}" stroke="{K}" stroke-width="5"/><path d="M-40,-10 Q-10,-50 20,-20 Q10,10 -30,15 Z" fill="{LAND}" stroke="{K}" stroke-width="3"/></g>
    <path id="lf-line" d="M225,680 L895,680" stroke="{K}" stroke-width="5" fill="none" stroke-dasharray="16 12" stroke-linecap="round"/>
    <g transform="translate(940,680)">{moon2d(32)}</g>
    <path id="lf-tick" d="M904,648 L904,712" stroke="{C['red']}" stroke-width="4" stroke-linecap="round"/>
  </svg>
  <div id="lf-3m"><span class="big">≈ 3 m</span><span style="font-size:48px"> farther away</span></div>
  <div id="lf-speck" class="abs" style="left:700px;top:590px;font-size:36px;color:{C['red']};opacity:0">3 m = a speck!</div>
  <div id="lf-km"><span id="lf-kn" class="big">0</span><span class="big" style="font-size:64px"> km</span></div>
""", J("""
rise("#lf-title", @t80);
tl.fromTo("#lf-tape", {scaleX:0, svgOrigin:"@tx0 320"}, {scaleX:1, duration:1.1, ease:"power2.out"}, @tt0);
pop("#lf-3m", @t3m);
ink("#lf-line", @tout, 0.7); rise("#lf-km", @t384a);
count("#lf-kn", 0, 384000, @t384, 1.6, v => "≈ " + fmtInt(Math.round(v/1000)*1000));
ink("#lf-tick", @ttk, 0.2); rise("#lf-speck", @ttk);
""", t80=t80 - 0.2, tx0=TX0, tt0=t80 + 0.6, t3m=t3m - 0.2, tout=tout, t384a=t384 - 0.4, t384=t384, ttk=t384 + 1.7))

# 10 ESCAPE — myth crossed out, snail too slow, Sun boils the oceans
s = "escape"; tesc = aw(s, "escape"); tnope = aw(s, "nope"); tslow = aw(s, "far too slow"); tbil = aw(s, "billion"); tsun = aw(s, "the sun"); tboil = aw(s, "boil away")
snail = (f'<g id="es-snail"><path d="M-46,0 Q-50,-12 -36,-12 L30,-12 Q44,-12 46,0 Z" fill="#E9D3AE" stroke="{K}" stroke-width="4"/>'
         f'<circle cx="-4" cy="-36" r="28" fill="#F2B33D" stroke="{K}" stroke-width="4"/><path d="M-4,-36 m-14,0 a14,14 0 1 1 14,14" fill="none" stroke="{K}" stroke-width="3"/>'
         f'<path d="M38,-12 L46,-34 M44,-12 L56,-30" stroke="{K}" stroke-width="3" stroke-linecap="round"/></g>')
rays = "".join(f'<path class="es-ray" d="M{_m.cos(a)*92:.1f},{_m.sin(a)*92:.1f} L{_m.cos(a)*128:.1f},{_m.sin(a)*128:.1f}" stroke="{K}" stroke-width="6" stroke-linecap="round" fill="none"/>' for a in [i * _m.pi / 5 for i in range(10)])
steam = "".join(f'<path class="es-st" d="M{x},780 Q{x-18},755 {x},730 Q{x+18},705 {x},680" stroke="{C["pencil"]}" stroke-width="5" fill="none" stroke-linecap="round"/>' for x in [520, 640, 760, 880])
wv = "M430,810 " + " ".join(f"Q{430 + 40*i + 20},{795 if i % 2 == 0 else 825} {430 + 40*(i+1)},810" for i in range(15))
scenes[s] = scene_file(s, f"""
#es-svg {{ position:absolute; left:0; top:0; }}
#es-myth {{ position:absolute; left:0; right:0; top:150px; text-align:center; {GH} font-size:96px; color:{C['pencil']}; }}
#es-nope {{ position:absolute; left:0; right:0; top:270px; text-align:center; }}
""", f"""
  <div id="es-myth">Moon escapes?</div>
  <svg id="es-svg" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <path id="es-x" d="M230,215 Q540,190 860,205" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path id="es-track" d="M120,520 L960,520" stroke="{C['pencil']}" stroke-width="4" fill="none" stroke-dasharray="6 10"/>
    <path id="es-trackp" d="M170,520 L330,520" fill="none" stroke="none"/>
    {snail}
    <g id="es-sun" transform="translate(220,660)"><circle id="es-sunb" r="80" fill="#FFC23A" stroke="{K}" stroke-width="6"/>{rays}</g>
    <path id="es-sea" d="{wv} L1030,880 L430,880 Z" fill="{SEA}" stroke="{K}" stroke-width="5"/>
    {steam}
  </svg>
  <div id="es-nope"><span class="chip" style="background:#FFC9C2">Nope!</span></div>
  {tape("es-t1", "far too slow", 520, 400, -3, 50)}
  <div id="es-bil" class="abs" style="left:560px;top:570px;opacity:0"><span class="pill" style="font-size:52px;color:{C['red']}">≈ 1 billion years</span></div>
""", J("""
rise("#es-myth", 0.05);
ink("#es-x", @tnope, 0.4); pop("#es-nope .chip", @tnope2, {from:{rotation:-15}, to:{rotation:-4}});
tl.set("#es-snail", {x:170, y:520}, 0); tl.fromTo("#es-snail", {opacity:0}, {opacity:1, duration:0.2}, @tsl0);
along("#es-snail", "#es-trackp", @tsl0, 2.4, {ease:"none"}); rise("#es-t1", @tslow);
pop("#es-bil", @tbil);
pop("#es-sunb", @tsun); ink(".es-ray", @tsun2, 0.3, {stagger:0.03});
rise("#es-sea", @tsea);
ink(".es-st", @tboil, 0.45, {stagger:0.12});
tl.to("#es-sea", {y:22, duration:1.2, ease:"power1.in"}, @tboil2);
""", tnope=tnope - 0.05, tnope2=tnope + 0.2, tsl0=tslow - 0.6, tslow=tslow, tbil=tbil, tsun=tsun - 0.1, tsun2=tsun + 0.1, tsea=tsun + 0.2, tboil=tboil, tboil2=tboil + 0.3))

# 11 OUTRO — Earth and Moon on a dotted string (callback), Stay curious (Max centre; keep y < 620)
s = "outro"; tdr = aw(s, "drifting"); tnl = aw(s, "not leaving"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-svg {{ position:absolute; left:0; top:140px; }}
#ou-chip {{ position:absolute; left:0; right:0; top:470px; text-align:center; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" width="{W}" height="320" viewBox="0 0 {W} 320" data-layout-ignore>
    {earth2d(300, 170, 110, "ou-e")}
    <path id="ou-str" d="M420,170 Q560,215 700,170" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="4 12"/>
    <g transform="translate(760,170)"><g id="ou-moon">{moon2d(55)}</g></g>
  </svg>
  <div id="ou-chip"><span class="chip">drifting… not leaving!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
rise("#ou-svg", 0.05);
ink("#ou-str", @tdr, 0.5);
tl.to("#ou-moon", {x:40, duration:0.8, ease:"power2.out"}, @tdr2);
tl.to("#ou-str", {attr:{d:"M420,170 Q580,190 740,170"}, duration:0.8, ease:"power2.out"}, @tdr2);
pop("#ou-chip .chip", @tnl, {from:{rotation:-10}, to:{rotation:-2}});
tl.to("#ou-svg, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
pop("#ou-c", @tsc);
""", tdr=tdr - 0.1, tdr2=tdr + 0.4, tnl=tnl, tsc0=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "staying put"), 2.6)
wave(g("intro", "I'm Max"))
point(g("mirror", "bounce lasers"), 1.4)
wow(g("drift", "three point eight"), 1.4)
think(SC["tides"]["start"] + 0.05, g("tides", "gravity"))
point(g("tides", "ahead"), 1.0)
point(g("tug", "tugs"), 1.2)
wow(g("brake", "brakes"), 1.2)
wow(g("life", "three meters"), 1.2)
point(g("escape", "nope"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "running away") + 0.2, 0.35), ("pop.mp3", A("guess", "staying put"), 0.5), ("pop.mp3", A("guess", "coming closer"), 0.5),
        ("pop.mp3", A("guess", "drifting away"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("mirror", "bounce lasers"), 0.55),
        ("riser.mp3", A("drift", "three point eight") - 0.3, 0.22), ("impact-bass-1.mp3", A("drift", "every year"), 0.4),
        ("whoosh-short.mp3", A("tides", "spins fast"), 0.3), ("pop.mp3", A("tug", "tugs"), 0.55),
        ("click.mp3", A("brake", "brakes"), 0.5), ("impact-bass-2.mp3", A("life", "three meters"), 0.4),
        ("click.mp3", A("escape", "nope"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
