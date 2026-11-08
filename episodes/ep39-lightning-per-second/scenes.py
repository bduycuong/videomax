# MAX WISE ep39 — How many times does lightning flash on Earth every second?
# Kit: ink / morph / along helpers + one three.js scene (hook: toon Earth with flashes popping on the continents).
# Sources: Christian et al., NASA Optical Transient Detector global lightning (NTRS 20020051098): ~44 +/- 5 flashes per second,
#  ~1.4 billion per year, land:ocean ~10:1. US National Weather Service "Introduction to Lightning": the old 100 per second
#  figure is a 1925 estimate; up to ~2,000 thunderstorms in progress at any moment. NWS "How hot is lightning?": ~50,000 F,
#  about five times the surface of the Sun.
# Maths: 44 x 60 = 2,640 per minute; 44 x 86,400 x 365 = 1.388e9 ~ 1.4 billion per year.
# === SCENES ===
import math as _m, random as _r, json as _json
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SEA = "#BFE3F7"; LAND = "#9BD08F"; BOLT = "#FFC23A"
SIM = """
const sim = (dur, fn) => { const st={t:0}; tl.fromTo(st, {t:0}, {t:dur, duration:dur, ease:"none", onUpdate:()=>fn(st.t)}, 0); fn(0); };
const clamp = v => Math.max(0, Math.min(1, v));
"""
def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.92)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 26px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff;white-space:nowrap">{txt}</span></div>')
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
BP = [(0.1, -1), (-0.5, 0.15), (-0.05, 0.15), (-0.25, 1), (0.5, -0.2), (0.05, -0.2), (0.35, -1)]
def bolt_d(s):
    """closed lightning-bolt outline around 0,0, height 2s"""
    return "M" + " L".join(f"{x*s:.1f},{y*s:.1f}" for x, y in BP) + " Z"
def bolt(s, idn="", cls="", fill=BOLT, sw=4):
    a = (f' id="{idn}"' if idn else "") + (f' class="{cls}"' if cls else "")
    return f'<path{a} d="{bolt_d(s)}" fill="{fill}" stroke="{K}" stroke-width="{sw}" stroke-linejoin="round"/>'
def earth2d(cx, cy, r, idp):
    return (f'<clipPath id="{idp}-clip"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SEA}" stroke="{K}" stroke-width="5"/>'
            f'<g clip-path="url(#{idp}-clip)"><path d="M{cx-r*0.7:.0f},{cy-r*0.3:.0f} Q{cx-r*0.3:.0f},{cy-r*0.75:.0f} {cx+r*0.05:.0f},{cy-r*0.45:.0f} Q{cx+r*0.15:.0f},{cy-r*0.05:.0f} {cx-r*0.25:.0f},{cy+r*0.05:.0f} Q{cx-r*0.6:.0f},{cy+r*0.1:.0f} {cx-r*0.7:.0f},{cy-r*0.3:.0f} Z" fill="{LAND}" stroke="{K}" stroke-width="4"/>'
            f'<path d="M{cx+r*0.25:.0f},{cy+r*0.3:.0f} Q{cx+r*0.7:.0f},{cy+r*0.15:.0f} {cx+r*0.75:.0f},{cy+r*0.5:.0f} Q{cx+r*0.55:.0f},{cy+r*0.85:.0f} {cx+r*0.3:.0f},{cy+r*0.7:.0f} Z" fill="{LAND}" stroke="{K}" stroke-width="4"/></g>')
OC = '{from:{transformOrigin:"50% 50%"}, to:{}}'

# 1 HOOK — 3D Earth turning, seeded flashes pop on the continents
s = "hook"; tq = aw(s, "how many"); tfl = aw(s, "lightning flash"); tev = aw(s, "every second"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-now {{ position:absolute; left:0; right:0; top:170px; text-align:center; }}
#hk-q {{ top:150px; font-size:76px; }}
#hk-cv {{ position:absolute; left:40px; top:400px; width:1000px; height:560px; }}
#hk-qm {{ position:absolute; left:860px; top:420px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-now"><span class="chip" style="font-size:64px">Right now…</span></div>
  <div id="hk-q" class="h1">How many times does <span class="hl">lightning flash</span> on Earth every second?</div>
  <canvas id="hk-cv" width="1000" height="560"></canvas>
  <div id="hk-qm">?</div>
""", J("""
const S = T3.stage("#hk-cv", 1000, 560, 34); S.cam.position.set(0, 1.4, 7.6); S.cam.lookAt(0, 0, 0);
const R = 1.9;
const earth = T3.inked(new THREE.SphereGeometry(R, 48, 32), 0x4F9BE0, 0.04); S.scene.add(earth); earth.rotation.z = 0.3;
const body = earth.userData.body; const rnd = T3.seeded(7); const spots = [];
for (let i=0;i<16;i++) { const th = 0.6+rnd()*1.9, ph = -3.0 + i*0.28 + rnd()*0.2, sz = R*(0.2+rnd()*0.16);
  const m = new THREE.Mesh(new THREE.SphereGeometry(sz, 20, 14), T3.toon(0x7CC46A));
  m.position.setFromSphericalCoords(R*0.93, th, ph); m.scale.set(1,1,0.3); m.lookAt(0,0,0); body.add(m); spots.push([th, ph, sz/R]); }
const sh = new THREE.Shape(); [[0.1,-1],[-0.5,0.15],[-0.05,0.15],[-0.25,1],[0.5,-0.2],[0.05,-0.2],[0.35,-1]].forEach(([x,y],i) => i ? sh.lineTo(x*0.16,-y*0.16) : sh.moveTo(x*0.16,-y*0.16));
const bgeo = new THREE.ShapeGeometry(sh), hgeo = new THREE.CircleGeometry(0.26, 24);
const bmat = new THREE.MeshBasicMaterial({color:0xFFC23A, side:THREE.DoubleSide}), hmat = new THREE.MeshBasicMaterial({color:0xFFFFFF, transparent:true, opacity:0.75, side:THREE.DoubleSide});
const F = [];
for (let j=0;j<110;j++) { const tb = 0.35 + j*0.062 + rnd()*0.04; let sp = spots[0];
  for (let k=0;k<40;k++) { sp = spots[Math.floor(rnd()*spots.length)]; const a = sp[1] + 0.28*tb; if (Math.abs(a) < 1.0 && sp[0] > 0.8 && sp[0] < 2.3) break; }
  const g = new THREE.Group(); const h = new THREE.Mesh(hgeo, hmat); const b = new THREE.Mesh(bgeo, bmat); b.position.z = -0.02; g.add(h); g.add(b);
  g.position.setFromSphericalCoords(R*1.07, sp[0] + (rnd()-0.5)*sp[2]*1.4, sp[1] + (rnd()-0.5)*sp[2]*1.6); g.lookAt(0,0,0);
  body.add(g); F.push([g, tb]); }
drive(@d, t => {
  const s = t < 0.5 ? 0.6 + 0.4*gsap.parseEase("back.out(2)")(t/0.5) : 1;
  earth.scale.setScalar(s); body.rotation.y = 0.28*t;
  for (const [g, tb] of F) { const k = (t - tb)/0.42; g.visible = k > 0 && k < 1;
    if (g.visible) g.scale.setScalar(k < 0.2 ? 0.3 + 3.5*k : 1 - 0.8*(k - 0.2)/0.8); }
  S.render();
});
pop("#hk-now .chip", 0.1, {from:{rotation:-10}, to:{rotation:-3}});
tl.to("#hk-now", {opacity:0, y:-20, duration:0.2}, @tq0);
rise("#hk-q", @tq);
pop("#hk-qm", @tev, {from:{rotation:-20}, to:{rotation:8}});
""", d=d, tq0=tq - 0.35, tq=tq - 0.1, tev=tev + 0.1))

# 2 GUESS — three sticky notes, bolts ink themselves
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "four"); t2 = aw(s, "forty"); t3 = aw(s, "hundred thousand")
notes = [("a", "4?", -6, 110, C['hi'], 96), ("b", "40?", 4, 405, "#BFE3F7", 96), ("c", "100,000?", -3, 700, "#FFC9C2", 60)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:330px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1;padding-top:{60 if fs > 80 else 75}px">{txt}</div>' for k, txt, r, x, bg, fs in notes)
def zz(x, y, cls):
    return f'<path class="{cls}" d="M{x+12},{y-40} L{x-12},{y-2} L{x+10},{y+2} L{x-10},{y+44}" stroke="{C["red"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
doodles = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>'
           + zz(247, 600, "gs-da") + zz(512, 605, "gs-db") + zz(572, 605, "gs-db")
           + zz(778, 600, "gs-dc") + zz(838, 600, "gs-dc") + zz(898, 600, "gs-dc") + '</svg>')
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink(".gs-da", @ta, 0.25); ink(".gs-db", @tb, 0.25, {stagger:0.12}); ink(".gs-dc", @tc, 0.25, {stagger:0.1});
""", tg=tg, t1=t1, t2=t2, t3=t3 - 0.1, ta=t1 + 0.25, tb=t2 + 0.25, tc=t3 + 0.2))

# 3 INTRO — logo, underline and two bolts ink themselves (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tls = aw(s, "let's count"); tsp = aw(s, "space")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-bz" d="M120,150 L70,250 L120,250 L80,340" stroke="{BOLT}" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="in-bz" d="M980,150 L930,250 L980,250 L940,340" stroke="{BOLT}" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    {"".join(f'<circle class="in-st" cx="{x}" cy="{y}" r="7" fill="{K}"/>' for x, y in [(160, 520), (300, 560), (780, 545), (930, 510), (540, 590)])}
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count from space!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
ink(".in-bz", @tb, 0.3, {stagger:0.15});
rise("#in-sub", @tls); tl.fromTo(".in-st", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:0.06, ease:"back.out(3)"}, @tsp);
""", tmw=tmw, tu=tmw + 0.3, tb=tmw + 0.15, tls=tls, tsp=tsp))

# 4 SAT — satellite rides its orbit (MotionPath), calendar flips, flashes counted
s = "sat"; tsat = aw(s, "satellite"); tcam = aw(s, "lightning camera"); tyr = aw(s, "year after"); tcnt = aw(s, "counted"); d = SC[s]["slot"]
ECX, ECY, ER = 540, 640, 190
orb = f"M{ECX+430},{ECY} A430,130 0 1 1 {ECX-430},{ECY} A430,130 0 1 1 {ECX+430},{ECY}"
rs = _r.Random(39); fl = []
while len(fl) < 14:
    x, y = rs.uniform(-170, 170), rs.uniform(-170, 170)
    if x*x + y*y < 165**2: fl.append((ECX + x, ECY + y))
sat_g = (f'<g id="st-sat" opacity="0"><rect x="-78" y="-13" width="50" height="26" fill="{SEA}" stroke="{K}" stroke-width="4"/>'
         f'<rect x="28" y="-13" width="50" height="26" fill="{SEA}" stroke="{K}" stroke-width="4"/>'
         f'<path d="M-62,-13 L-62,13 M-45,-13 L-45,13 M44,-13 L44,13 M61,-13 L61,13 M-28,0 L-22,0 M22,0 L28,0" stroke="{K}" stroke-width="3"/>'
         f'<rect x="-22" y="-22" width="44" height="44" rx="6" fill="#FFFFFF" stroke="{K}" stroke-width="4"/>'
         f'<circle cx="0" cy="26" r="10" fill="{K}"/><circle cx="3" cy="23" r="3" fill="#FFFFFF"/>'
         f'<path d="M0,-22 L0,-40" stroke="{K}" stroke-width="4" stroke-linecap="round"/><circle cx="0" cy="-44" r="5" fill="{C["red"]}" stroke="{K}" stroke-width="3"/></g>')
tal = "".join(f'<path class="st-ty" d="M{760+i*30+(i//5)*40},300 L{764+i*30+(i//5)*40},380" stroke="{K}" stroke-width="6" stroke-linecap="round" fill="none"/>' if i % 5 != 4 else
              f'<path class="st-ty" d="M{745+(i//5)*190},360 L{895+(i//5)*190},320" stroke="{C["red"]}" stroke-width="6" stroke-linecap="round" fill="none"/>' for i in range(10))
scenes[s] = scene_file(s, f"""
#st-od {{ position:absolute; left:400px; right:60px; top:875px; text-align:center; white-space:nowrap; font-family:'Courier New',monospace; font-size:32px; letter-spacing:1px; color:{K}; opacity:0; }}
#st-od span {{ background:#FFFFFF; border:3px solid {K}; padding:2px 14px; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {earth2d(ECX, ECY, ER, "st-e")}
    {"".join(f'<g transform="translate({x:.0f},{y:.0f})"><g class="st-f" opacity="0"><circle r="20" fill="#FFFFFF" opacity=".8"/>{bolt(17, sw=3)}</g></g>' for x, y in fl)}
    <path id="st-orb" d="{orb}" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-dasharray="12 12"/>
    <g transform="translate(110,300)"><rect x="0" y="0" width="170" height="150" rx="10" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>
      <rect x="0" y="0" width="170" height="40" rx="10" fill="{C['red']}" stroke="{K}" stroke-width="5"/>
      <path d="M40,-14 L40,14 M130,-14 L130,14" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
      <g id="st-page"><rect x="12" y="50" width="146" height="90" fill="{C['hi']}" stroke="{K}" stroke-width="3"/>
        <path d="M30,75 L140,75 M30,98 L140,98 M30,121 L110,121" stroke="{K}" stroke-width="3" stroke-linecap="round"/></g></g>
    {tal}
    {sat_g}
  </svg>
  {tape("st-t1", "NASA satellite", 80, 170, -3, 50)}
  {tape("st-t2", "lightning camera", 560, 170, 3, 50, "rgba(255,201,194,.95)")}
  <div id="st-od"><span>Optical Transient Detector</span></div>
""", J("""
tl.set("#st-sat", {x:@sx, y:@sy}, 0); tl.to("#st-sat", {opacity:1, duration:0.2}, @tsat0);
along("#st-sat", "#st-orb", @tsat0, @lap, {ease:"none", repeat:2});
rise("#st-t1", @tsat); rise("#st-t2", @tcam); rise("#st-od", @tcam1);
tl.set("#st-page", {svgOrigin:"85 50"}, 0);
for (let k=0;k<3;k++) tl.fromTo("#st-page", {scaleY:1}, {scaleY:0, duration:0.28, ease:"power2.in", immediateRender:false}, @tyr + k*0.4);
tl.set("#st-page", {scaleY:1}, @tyr + 1.15);
ink(".st-ty", @tcnt, 0.12, {stagger:0.11});
document.querySelectorAll(".st-f").forEach((el, i) => { const t0 = @tf0 + i*0.3;
  tl.fromTo(el, {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1.15, duration:0.12}, t0);
  tl.to(el, {opacity:0, scale:0.7, duration:0.35}, t0 + 0.25); });
""", sx=float(ECX + 430), sy=float(ECY), tsat0=tsat - 0.2, lap=2.4, tsat=tsat, tcam=tcam, tcam1=tcam + 0.4, tyr=tyr, tcnt=tcnt, tf0=tcam))

# 5 ANSWER — real flashes at exactly 44 per second on a world strip; counter tallies one second; honest +/- 5 bar
s = "answer"; tan = aw(s, "the answer"); t44 = aw(s, "forty four"); tgv = aw(s, "give or"); tfv = aw(s, "take five"); d = SC[s]["slot"]
MX, MY, MW, MH = 60, 270, 960, 300
lands = [(250, 400, 120, 95), (590, 380, 170, 80), (870, 480, 85, 50)]
def blob(cx, cy, rx, ry, ph):
    pts = [(cx + rx*(1 + 0.09*_m.sin(3*a + ph))*_m.cos(a), cy + ry*(1 + 0.09*_m.sin(3*a + ph))*_m.sin(a)) for a in [i*2*_m.pi/14 for i in range(14)]]
    return "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts) + " Z"
ra = _r.Random(44); FL = []
nfl = int((d - t44) * 44) + 2
for k in range(nfl):
    if ra.random() < 10/11:
        cx, cy, rx, ry = lands[ra.randrange(3)]; a, q = ra.uniform(0, 6.283), ra.uniform(0, 0.8) ** 0.5
        x, y = cx + rx*q*_m.cos(a), cy + ry*q*_m.sin(a)
    else:
        x, y = ra.uniform(MX + 30, MX + MW - 30), ra.uniform(MY + 30, MY + MH - 30)
    FL.append([round(x - MX), round(y - MY)])
scenes[s] = scene_file(s, f"""
#an-cv {{ position:absolute; left:{MX}px; top:{MY}px; width:{MW}px; height:{MH}px; }}
#an-ans {{ position:absolute; left:0; right:0; top:600px; text-align:center; opacity:0; }}
#an-n {{ font-size:170px; color:{C['red']}; }}
#an-pm {{ position:absolute; left:860px; top:790px; {GH} font-size:64px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="an-title" class="h1" style="top:150px;font-size:76px">The answer…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <rect x="{MX}" y="{MY}" width="{MW}" height="{MH}" rx="26" fill="{SEA}" stroke="{K}" stroke-width="5"/>
    {"".join(f'<path d="{blob(cx, cy, rx, ry, i*1.7)}" fill="{LAND}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>' for i, (cx, cy, rx, ry) in enumerate(lands))}
    <path id="an-bar" d="M440,830 L840,830" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="an-cap" d="M440,800 L440,860" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="an-cap" d="M840,800 L840,860" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <circle id="an-dot" cx="640" cy="830" r="16" fill="{C['red']}" stroke="{K}" stroke-width="4" opacity="0"/>
  </svg>
  <canvas id="an-cv" width="{MW}" height="{MH}"></canvas>
  <div id="an-ans"><span class="big" style="font-size:110px">≈ </span><span id="an-n" class="big">0</span><span class="big" style="font-size:66px"> flashes / second</span></div>
  <div id="an-pm">± 5</div>
""", SIM + J("""
const FL = @fl; const cv = document.getElementById("an-cv"); const ctx = cv.getContext("2d");
const BP = [[0.1,-1],[-0.5,0.15],[-0.05,0.15],[-0.25,1],[0.5,-0.2],[0.05,-0.2],[0.35,-1]];
const nEl = document.getElementById("an-n");
sim(@d, t => {
  ctx.clearRect(0, 0, @mw, @mh); ctx.lineJoin = "round";
  const born = Math.floor((t - @t0) * 44);
  for (let k = Math.max(0, born - 14); k <= born && k < FL.length; k++) {
    const age = t - (@t0 + k/44); if (age < 0) continue; const life = age/0.3; if (life > 1) continue;
    const sc = 26 * (life < 0.25 ? 0.5 + 2*life : 1 - 0.6*(life - 0.25)/0.75), [x, y] = FL[k];
    ctx.globalAlpha = life < 0.6 ? 1 : 1 - (life - 0.6)/0.4;
    ctx.fillStyle = "rgba(255,255,255,0.75)"; ctx.beginPath(); ctx.arc(x, y, sc*1.1, 0, 6.283); ctx.fill();
    ctx.beginPath(); BP.forEach(([bx, by], i) => i ? ctx.lineTo(x + bx*sc, y + by*sc) : ctx.moveTo(x + bx*sc, y + by*sc)); ctx.closePath();
    ctx.fillStyle = "@bolt"; ctx.fill(); ctx.strokeStyle = "@ink"; ctx.lineWidth = 3; ctx.stroke(); }
  ctx.globalAlpha = 1;
  nEl.textContent = String(Math.max(0, Math.min(44, Math.floor((t - @t0) * 44 + 1e-6))));
});
rise("#an-title", @tan); tl.to("#an-ans", {opacity:1, duration:0.2}, @t0);
tl.fromTo("#an-n", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1, transformOrigin:"50% 60%"}, @t1s);
ink("#an-bar", @tgv, 0.5); ink(".an-cap", @tgv2, 0.2); pop("#an-dot", @tgv, @oc);
pop("#an-pm", @tfv, {from:{rotation:-15}, to:{rotation:-4}});
""", fl=_json.dumps(FL), d=d, mw=MW, mh=MH, t0=t44, t1s=t44 + 1.0, tan=tan, tgv=tgv, tgv2=tgv + 0.45, tfv=tfv, oc=OC, bolt=BOLT, ink=K))

# 6 SCALE — cards grow one after another: second -> minute -> year
s = "scale"; t2k = aw(s, "two thousand"); tmin = aw(s, "every minute"); tal_ = aw(s, "almost"); t14 = aw(s, "one point four"); tyr = aw(s, "every year")
cards = [("sc-c1", 90, 190, 360, 170, "1 second", "sc-n1", "44", 100, K),
         ("sc-c2", 90, 390, 660, 170, "1 minute", "sc-n2", "2,640", 110, C['blue']),
         ("sc-c3", 90, 590, 900, 210, "1 year", "sc-n3", "≈ 1.4 billion", 120, C['red'])]
ch = "".join(f'<div id="{i}" class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform-origin:0% 50%;opacity:0">'
             f'<div style="position:absolute;left:30px;top:14px;font-size:44px;color:{C["muted"]}">{lab}</div>'
             f'<div id="{ni}" class="big" style="position:absolute;right:34px;bottom:14px;font-size:{fs}px;color:{col};white-space:nowrap">{val}</div></div>'
             for i, x, y, w, h, lab, ni, val, fs, col in cards)
scenes[s] = scene_file(s, "", f"""
  {ch}
""", J("""
const card = (sel, t) => { tl.fromTo(sel, {opacity:0, scaleX:0.15}, {opacity:1, scaleX:1, duration:0.4, ease:"back.out(1.6)"}, t); };
card("#sc-c1", 0.05);
card("#sc-c2", @tc2); rise("#sc-n2", @t2k); count("#sc-n2", 44, 2640, @t2k, 1.5, v => fmtInt(Math.round(v)));
tl.fromTo("#sc-n2", {scale:1}, {scale:1.12, duration:0.14, yoyo:true, repeat:1}, @tmin);
card("#sc-c3", @tc3); rise("#sc-n3", @t14); count("#sc-n3", 0, 1.4, @t14, 0.9, v => "≈ " + v.toFixed(1) + " billion");
tl.fromTo("#sc-c3", {rotation:0}, {rotation:-1.5, duration:0.12, yoyo:true, repeat:3}, @tyr);
""", tc2=t2k - 0.25, t2k=t2k, tmin=tmin, tc3=tal_ - 0.1, t14=t14, tyr=tyr))

# 7 MYTH — the old 100 per second, struck out in red pen
s = "myth"; tot = aw(s, "old textbooks"); t100 = aw(s, "one hundred"); tbut = aw(s, "but that"); trg = aw(s, "rough guess"); t19 = aw(s, "nineteen")
book = (f'<path d="M540,320 Q450,292 370,312 L370,182 Q450,162 540,190 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
        f'<path d="M540,320 Q630,292 710,312 L710,182 Q630,162 540,190 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
        f'<path d="M400,220 Q460,206 515,222 M400,250 Q460,236 515,252 M400,280 Q460,266 515,282 M565,222 Q620,206 680,220 M565,252 Q620,236 680,250 M565,282 Q620,266 680,280" stroke="{C["pencil"]}" stroke-width="4" fill="none" stroke-linecap="round"/>')
scenes[s] = scene_file(s, f"""
#my-old {{ position:absolute; left:0; right:0; top:370px; text-align:center; {GH} font-size:124px; color:{C['pencil']}; opacity:0; }}
#my-new {{ position:absolute; left:0; right:0; top:560px; text-align:center; opacity:0; }}
#my-new .big {{ font-size:100px; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="my-book">{book}</g>
    <path id="my-x" d="M190,452 Q540,420 900,440" stroke="{C['red']}" stroke-width="13" fill="none" stroke-linecap="round"/>
    <path id="my-x2" d="M210,478 Q540,456 880,470" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("my-t0", "old textbooks", 70, 205, -6, 48)}
  <div id="my-old">100 / second</div>
  <div id="my-new"><span class="big hl">≈ 44 / second</span></div>
  {tape("my-t1", "a rough guess", 150, 730, -4, 54, "rgba(255,201,194,.95)")}
  {stamp("my-st", "1925", 640, 715, -8, 72)}
""", J("""
pop("#my-book", @tot, {from:{rotation:-8}, to:{rotation:0}}); rise("#my-t0", @tot2);
rise("#my-old", @t100);
ink("#my-x", @tbut, 0.35, {ease:"power2.out"}); ink("#my-x2", @tbut2, 0.3, {ease:"power2.out"});
pop("#my-new", @tnew, {from:{rotation:-6}, to:{rotation:0}});
rise("#my-t1", @trg); pop("#my-st", @t19, {from:{rotation:-30, scale:1.8}, to:{}});
""", tot=tot, tot2=tot + 0.25, t100=t100 - 0.1, tbut=tbut, tbut2=tbut + 0.3, tnew=tbut + 0.7, trg=trg, t19=t19))

# 8 LAND — seesaw: ten bolts over land outweigh one over the ocean
s = "land"; tmo = aw(s, "most lightning"); tol = aw(s, "over land"); toc = aw(s, "ocean"); tlg = aw(s, "land gets"); tten = aw(s, "ten")
lb = [(190 + i*55, 500 - 70*(r)) for r in range(2) for i in range(5)]
scenes[s] = scene_file(s, f"""
#ld-r {{ position:absolute; left:0; right:0; top:775px; text-align:center; opacity:0; }}
#ld-r .big {{ font-size:110px; }}
""", f"""
  <div id="ld-title" class="h1" style="top:150px;font-size:74px">Most lightning hits <span class="hl">land</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path d="M540,640 L475,745 L605,745 Z" fill="{C['hi']}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
    <path d="M420,748 L660,748" {WS}/>
    <g id="ld-see">
      <rect x="130" y="620" width="820" height="22" rx="8" fill="#E9D3AE" stroke="{K}" stroke-width="5"/>
      <path d="M160,620 Q300,520 440,620 Z" fill="{LAND}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M650,620 L650,578 Q690,556 730,578 Q770,600 810,578 Q850,556 890,578 L890,620 Z" fill="{SEA}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      {"".join(f'<g transform="translate({x},{y})"><g class="ld-b">{bolt(28, sw=3.5)}</g></g>' for x, y in lb)}
      <g transform="translate(770,500)"><g id="ld-ob">{bolt(28, sw=3.5)}</g></g>
      <text x="300" y="690" text-anchor="middle" font-family="Gochi Hand" font-size="50" fill="{K}">land</text>
      <text x="770" y="690" text-anchor="middle" font-family="Gochi Hand" font-size="50" fill="{C['blue']}">ocean</text>
    </g>
  </svg>
  <div id="ld-r"><span class="big">10 : 1</span></div>
""", J("""
rise("#ld-title", @tmo);
tl.set("#ld-see", {svgOrigin:"540 631"}, 0);
tl.fromTo(".ld-b", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.22, stagger:0.07, ease:"back.out(3)"}, @tol);
pop("#ld-ob", @toc, @oc);
tl.fromTo("#ld-see", {rotation:0}, {rotation:-7, duration:0.7, ease:"elastic.out(1,0.45)", immediateRender:false}, @tlg);
pop("#ld-r", @tten, {from:{rotation:-10}, to:{rotation:-2}});
""", tmo=tmo - 0.05, tol=tol - 0.1, toc=toc, tlg=tlg, tten=tten, oc=OC))

# 9 STORMS — storm clouds pop up all over the globe, counter to 2,000, RUMBLE!
s = "storms"; twhy = aw(s, "why so"); tam = aw(s, "at any"); t2k = aw(s, "two thousand"); trum = aw(s, "rumbling"); d = SC[s]["slot"]
GX, GY, GR = 540, 580, 270
rc = _r.Random(2000); cl = []
while len(cl) < 34:
    x, y = rc.uniform(-235, 235), rc.uniform(-235, 235)
    if x*x + y*y < 230**2 and all((x - a)**2 + (y - b)**2 > 62**2 for a, b in cl): cl.append((x, y))
cloud = (f'<path d="M-34,10 Q-46,-8 -24,-14 Q-18,-34 2,-27 Q18,-38 30,-18 Q48,-14 40,10 Z" fill="#D9DDE6" stroke="{K}" stroke-width="3.5" stroke-linejoin="round"/>')
cl_svg = "".join(f'<g transform="translate({GX + x:.0f},{GY + y:.0f})"><g class="sm-c"><g class="sm-b{i % 3}"><path d="M2,9 L-9,26 L0,26 L-7,42 L10,20 L2,20 L8,9 Z" fill="{BOLT}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/></g>{cloud}</g></g>' for i, (x, y) in enumerate(cl))
scenes[s] = scene_file(s, f"""
#sm-why {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#sm-cnt {{ position:absolute; left:560px; top:880px; white-space:nowrap; opacity:0; }}
#sm-cnt .pill {{ font-size:54px; color:{C['red']}; }}
""", f"""
  <div id="sm-why"><span class="chip">Why so many?</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {earth2d(GX, GY, GR, "sm-e")}
    {cl_svg}
  </svg>
  {stamp("sm-rb", "RUMBLE!", 660, 270, 9, 70, K)}
  <div id="sm-cnt"><span class="pill">up to <span id="sm-n">0</span> storms</span></div>
""", J("""
pop("#sm-why .chip", @twhy, {from:{rotation:-12}, to:{rotation:-3}});
tl.fromTo(".sm-c", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:@ea, ease:"back.out(2.5)"}, @tam);
for (let k=0, t=@tam + 0.4; t < @d - 0.3; k++, t += 0.16) { tl.set(".sm-b0", {opacity: k%3==0 ? 0.15 : 1}, t); tl.set(".sm-b1", {opacity: k%3==1 ? 0.15 : 1}, t); tl.set(".sm-b2", {opacity: k%3==2 ? 0.15 : 1}, t); }
rise("#sm-cnt", @t2k0); count("#sm-n", 0, 2000, @t2k, 1.2, v => fmtInt(Math.round(v/10)*10));
pop("#sm-rb", @trum, {from:{rotation:30, scale:1.7}, to:{rotation:9}});
tl.fromTo("#sm-rb span", {x:0}, {x:7, duration:0.05, yoyo:true, repeat:9}, @trum2);
""", twhy=twhy, tam=tam, ea=round((t2k + 0.9 - tam) / 34, 3), d=d, t2k0=t2k - 0.2, t2k=t2k, trum=trum, trum2=trum + 0.3))

# 10 HEAT — thermometer climbs to 50,000 F; one Sun-surface unit vs five
s = "heat"; tbo = aw(s, "bolt"); tht = aw(s, "heats"); t50 = aw(s, "fifty thousand"); tth = aw(s, "that's about"); t5 = aw(s, "five times"); thot = aw(s, "hotter"); tsun = aw(s, "sun")
sun = lambda: (f'<circle r="34" fill="{BOLT}" stroke="{K}" stroke-width="4"/>' +
               "".join(f'<path d="M{_m.cos(a)*42:.1f},{_m.sin(a)*42:.1f} L{_m.cos(a)*54:.1f},{_m.sin(a)*54:.1f}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for a in [i*_m.pi/4 for i in range(8)]))
ticks = "".join(f'<path d="M236,{260 + i*50} L{256 if i % 2 == 0 else 248},{260 + i*50}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(10))
scenes[s] = scene_file(s, f"""
#ht-n {{ position:absolute; left:330px; top:190px; width:700px; text-align:center; font-size:112px; color:{C['red']}; opacity:0; white-space:nowrap; }}
.ht-lab {{ position:absolute; left:400px; font-size:44px; color:{C['muted']}; opacity:0; }}
#ht-pill {{ position:absolute; left:560px; top:800px; opacity:0; white-space:nowrap; }}
#ht-pill .pill {{ font-size:60px; color:{C['red']}; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path d="M170,760 L170,240 A30,30 0 0 1 230,240 L230,760 A50,50 0 1 1 170,760 Z" fill="#FFFFFF" stroke="none"/>
    <circle cx="200" cy="800" r="37" fill="{C['red']}"/>
    <rect id="ht-col" x="186" y="250" width="28" height="545" fill="{C['red']}"/>
    <path id="ht-tube" d="M170,760 L170,240 A30,30 0 0 1 230,240 L230,760 A50,50 0 1 1 170,760 Z" fill="none" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    {ticks}
    <g transform="translate(470,535)"><g id="ht-s0">{sun()}</g></g>
    {"".join(f'<g transform="translate({470 + i*112},715)"><g class="ht-s">{sun()}</g></g>' for i in range(5))}
    <path id="ht-bz" d="M330,330 L300,390 L330,390 L305,450" stroke="{BOLT}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="ht-n" class="big">≈ 0 °F</div>
  <div id="ht-l1" class="ht-lab" style="top:430px">Sun's surface</div>
  <div id="ht-l2" class="ht-lab" style="top:610px">lightning</div>
  <div id="ht-pill"><span class="pill">5× hotter!</span></div>
""", J("""
ink("#ht-tube", 0.05, 0.6);
tl.fromTo("#ht-col", {scaleY:0.04, svgOrigin:"200 795"}, {scaleY:1, duration:@up, ease:"power2.inOut"}, @tht);
ink("#ht-bz", @tbo, 0.3);
rise("#ht-n", @t50a); count("#ht-n", 0, 50000, @t50, 1.1, v => "≈ " + fmtInt(Math.round(v/1000)*1000) + " °F");
rise("#ht-l1", @tth); pop("#ht-s0", @tth, @oc);
rise("#ht-l2", @t5a); tl.fromTo(".ht-s", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:0.11, ease:"back.out(2.5)"}, @t5);
pop("#ht-pill", @thot, {from:{rotation:-14}, to:{rotation:-3}});
tl.fromTo("#ht-s0", {scale:1}, {scale:1.25, duration:0.15, yoyo:true, repeat:1, transformOrigin:"50% 50%", immediateRender:false}, @tsun);
""", tht=tht, up=round(t50 + 1.1 - tht, 2), tbo=tbo - 0.05, t50a=t50 - 0.25, t50=t50, tth=tth, t5a=t5 - 0.15, t5=t5, thot=thot, tsun=tsun, oc=OC))

# 11 OUTRO — the red "?" morphs into a lightning bolt (callback), Stay curious (Max centre: keep y < 620)
s = "outro"; t44 = aw(s, "forty four"); tes = aw(s, "every second"); tadl = aw(s, "all day"); tsc = aw(s, "stay curious")
QM = "M470,230 Q470,150 540,150 Q610,150 610,215 Q610,262 545,290 L545,350"
BZ = "M590,140 L495,290 L575,290 L490,440"
scenes[s] = scene_file(s, f"""
#ou-chip {{ position:absolute; left:0; right:0; top:480px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" class="abs" style="left:0;top:0" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <path id="ou-qk" d="{QM}" stroke="{K}" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-q" d="{QM}" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="ou-qd" cx="545" cy="420" r="20" fill="{C['red']}" stroke="{K}" stroke-width="7"/>
    {"".join(f'<path class="ou-ry" d="M{540 + _m.cos(a)*190:.0f},{290 + _m.sin(a)*190:.0f} L{540 + _m.cos(a)*240:.0f},{290 + _m.sin(a)*240:.0f}" stroke="{K}" stroke-width="7" stroke-linecap="round" fill="none"/>' for a in [_m.pi*(0.15 + i*0.233) for i in range(9)] if not (0.8 < a < 2.4))}
  </svg>
  <div id="ou-chip"><span class="chip">≈ 44 flashes / second</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-svg", 0.05, {from:{scale:0.8}, to:{}});
morph("#ou-qk", "@bz", @t44, 0.55, {ease:"back.out(1.4)"}); morph("#ou-q", "@bz", @t44, 0.55, {ease:"back.out(1.4)"});
tl.to("#ou-q", {stroke:"@bolt", duration:0.3}, @t44b); tl.to("#ou-qd", {opacity:0, scale:0, transformOrigin:"50% 50%", duration:0.2}, @t44);
pop("#ou-chip", @tes, {from:{rotation:-10}, to:{rotation:-2}});
ink(".ou-ry", @tadl, 0.25, {stagger:0.05});
tl.to("#ou-svg, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
pop("#ou-c", @tsc1);
""", bz=BZ, bolt=BOLT, t44=t44 - 0.05, t44b=t44 + 0.2, tes=tes, tadl=tadl, tsc0=tsc - 0.45, tsc1=tsc - 0.2), fade=False)

# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "four"), 2.4)
wave(g("intro", "I'm Max"))
point(g("sat", "satellite"), 1.4)
wow(g("answer", "forty four"), 1.4)
point(g("scale", "one point four"), 1.2)
point(g("myth", "but that"), 1.2)
wow(g("land", "about ten"), 1.0)
think(SC["storms"]["start"] + 0.05, g("storms", "at any"))
wow(g("storms", "two thousand"), 1.2)
wow(g("heat", "five times"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "every second") + 0.1, 0.35), ("pop.mp3", A("guess", "four"), 0.5), ("pop.mp3", A("guess", "forty"), 0.5),
        ("pop.mp3", A("guess", "hundred thousand"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("sat", "lightning camera"), 0.55),
        ("riser.mp3", A("answer", "about") - 0.3, 0.22), ("impact-bass-1.mp3", A("scale", "one point four"), 0.4),
        ("click.mp3", A("myth", "but that"), 0.5), ("pop.mp3", A("land", "ocean"), 0.5),
        ("impact-bass-2.mp3", A("storms", "rumbling"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
