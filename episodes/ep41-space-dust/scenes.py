# MAX WISE ep41 — How much space dust falls on Earth every year?
# Kit: ink / morph / along helpers + two three.js scenes (hook: toon Earth with dust streaks; answer: pull-back while dust rains in).
# Sources: Rojas et al. 2021, EPSL 566:116794 (micrometeorite flux at Dome C, ~20 years near Concordia): ~5,200 t/yr, mostly
#  Jupiter-family comets. CNRS press release 8 Apr 2021: 5,200 t/yr, meteorites < 10 t/yr, ~80% comets. Genge et al. 2017 Geology
#  45(2): ~500 micrometeorites from urban rooftops (Oslo, Paris gutter sediment via Project Stardust).
# Maths: 5200/365 = 14.2 t/day; 5200e3/365/24/60 = 9.9 kg/min ~ 10 kg.
# === SCENES ===
import math as _m, random as _r
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SEA = "#BFE3F7"; LAND = "#9BD08F"; DUST = "#B07A4A"; SNOW = "#EAF4FB"
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

# shared 3D builder: toon Earth with land blobs + seeded dust streaks diving toward the surface
EARTH_JS = """
function buildEarth(S, R, seed) {
  const earth = T3.inked(new THREE.SphereGeometry(R, 48, 32), 0x4F9BE0, 0.04); S.scene.add(earth); earth.rotation.z = 0.3;
  const body = earth.userData.body; const rnd = T3.seeded(seed);
  for (let i=0;i<16;i++) { const th = 0.6+rnd()*1.9, ph = -3.0 + i*0.39 + rnd()*0.2, sz = R*(0.2+rnd()*0.16);
    const m = new THREE.Mesh(new THREE.SphereGeometry(sz, 20, 14), T3.toon(0x7CC46A));
    m.position.setFromSphericalCoords(R*0.93, th, ph); m.scale.set(1,1,0.3); m.lookAt(0,0,0); body.add(m); }
  return earth;
}
function buildDust(S, R, n, seed, t0, gap, r0, len) {
  const rnd = T3.seeded(seed); const out = [];
  const hg = new THREE.SphereGeometry(0.05, 10, 8), hm = new THREE.MeshBasicMaterial({color:0xFFB347});
  const tg = new THREE.CylinderGeometry(0.012, 0.026, len, 6); tg.rotateX(Math.PI/2); tg.translate(0, 0, -len/2 - 0.03);
  const tm = new THREE.MeshBasicMaterial({color:0x262A3B});
  for (let i=0;i<n;i++) {
    let v; do { v = new THREE.Vector3(rnd()*2-1, rnd()*2-1, rnd()*2-1); } while (v.length() > 1 || v.length() < 0.2 || v.z < -0.1);
    v.normalize(); const g = new THREE.Group(); g.add(new THREE.Mesh(hg, hm)); g.add(new THREE.Mesh(tg, tm)); g.visible = false; S.scene.add(g);
    out.push({g, v, tb: t0 + i*gap + rnd()*gap, sp: 0.55 + rnd()*0.35});
  }
  return (t) => { for (const d of out) { const k = (t - d.tb)/d.sp; d.g.visible = k > 0 && k < 1;
    if (d.g.visible) { const r = r0 - (r0 - R*1.01)*k; d.g.position.copy(d.v).multiplyScalar(r); d.g.lookAt(0,0,0); } } };
}
"""

# 1 HOOK — 3D Earth turning, dust streaks dive in
s = "hook"; tti = aw(s, "tiny bits"); thw = aw(s, "how much"); tev = aw(s, "every year"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-now {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#hk-q {{ top:150px; font-size:80px; }}
#hk-cv {{ position:absolute; left:40px; top:400px; width:1000px; height:560px; }}
#hk-qm {{ position:absolute; left:850px; top:420px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-now"><span class="chip" style="font-size:64px">Right now…</span></div>
  <div id="hk-q" class="h1">How much <span class="hl">space dust</span> falls on Earth every year?</div>
  <canvas id="hk-cv" width="1000" height="560"></canvas>
  <div id="hk-qm">?</div>
""", EARTH_JS + J("""
const S = T3.stage("#hk-cv", 1000, 560, 34); S.cam.position.set(0, 1.2, 7.6); S.cam.lookAt(0, 0, 0);
const R = 1.8; const earth = buildEarth(S, R, 7);
const dust = buildDust(S, R, 90, 41, @tti, 0.065, R*2.9, 0.55);
drive(@d, t => {
  const s = t < 0.5 ? 0.6 + 0.4*gsap.parseEase("back.out(2)")(t/0.5) : 1;
  earth.scale.setScalar(s); earth.userData.body.rotation.y = 0.3*t; dust(t); S.render();
});
pop("#hk-now .chip", 0.1, {from:{rotation:-10}, to:{rotation:-3}});
tl.to("#hk-now", {opacity:0, y:-20, duration:0.2}, @tq0);
rise("#hk-q", @tq);
pop("#hk-qm", @tev, {from:{rotation:-20}, to:{rotation:8}});
""", d=d, tti=tti - 0.2, tq0=thw - 0.35, tq=thw - 0.1, tev=tev + 0.1))

# 2 GUESS — sticky notes, doodles ink themselves
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "bucketful"); t2 = aw(s, "hundred tons"); t3 = aw(s, "thousands")
notes = [("a", "a bucketful?", -6, 110, C['hi'], 56), ("b", "100 tons?", 4, 405, "#BFE3F7", 70), ("c", "thousands of tons?", -3, 700, "#FFC9C2", 54)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:340px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding:40px 16px 0">{txt}</div>' for k, txt, r, x, bg, fs in notes)
def wt(x, y, cls):  # a little weight block with handle
    return (f'<path class="{cls}" d="M{x-30},{y+30} L{x-22},{y-8} L{x+22},{y-8} L{x+30},{y+30} Z" {WS}/>'
            f'<path class="{cls}" d="M{x-10},{y-8} Q{x},{y-26} {x+10},{y-8}" {WS}/>')
doodles = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>'
           f'<path class="gs-da" d="M210,560 L222,640 Q248,652 274,640 L286,560" {WS}/><path class="gs-da" d="M206,560 Q248,546 290,560" {WS}/>'
           f'<path class="gs-da" d="M214,566 Q248,500 282,566" stroke="{C["pencil"]}" stroke-width="4" fill="none" stroke-linecap="round"/>'
           + wt(545, 620, "gs-db") + wt(780, 640, "gs-dc") + wt(850, 640, "gs-dc") + wt(815, 586, "gs-dc") + '</svg>')
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink(".gs-da", @ta, 0.3, {stagger:0.1}); ink(".gs-db", @tb, 0.3, {stagger:0.1}); ink(".gs-dc", @tc, 0.3, {stagger:0.06});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.1, ta=t1 + 0.25, tb=t2 + 0.25, tc=t3 + 0.2))

# 3 INTRO — logo, underline, magnifier inks itself (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tlg = aw(s, "let's go"); tdh = aw(s, "dust hunting")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-mg" d="M110,530 C110,490 150,460 180,460 C220,460 250,490 250,530 C250,570 220,600 180,600 C140,600 110,570 110,530 Z" stroke="{K}" stroke-width="9" fill="none"/>
    <path class="in-mg" d="M228,580 L280,630" stroke="{K}" stroke-width="18" fill="none" stroke-linecap="round"/>
    {"".join(f'<circle class="in-st" cx="{x}" cy="{y}" r="{r}" fill="{DUST}" stroke="{K}" stroke-width="3"/>' for x, y, r in [(165, 520, 9), (198, 545, 6), (186, 502, 5), (820, 540, 8), (930, 500, 6), (160, 540, 7), (980, 200, 7), (870, 150, 5)])}
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's go dust hunting!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tlg); ink(".in-mg", @tdh, 0.35, {stagger:0.2});
tl.fromTo(".in-st", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:0.06, ease:"back.out(3)"}, @tst);
""", tmw=tmw, tu=tmw + 0.3, tlg=tlg - 0.1, tdh=tdh, tst=tdh + 0.3))

# 4 SNOW — Antarctica inks itself, flag at Concordia, 20-year ruler, melt + sift (grains travel along a path)
s = "snow"; tsc = aw(s, "scientists"); tant = aw(s, "Antarctica"); t20 = aw(s, "twenty years"); tmel = aw(s, "melted"); tsif = aw(s, "sifted"); tgr = aw(s, "grains")
ANT = ("M170,330 C190,250 260,210 330,220 C380,180 450,170 500,190 C560,160 640,170 690,200 C760,190 830,230 850,290 "
       "C880,340 860,400 810,420 C770,460 700,470 640,450 C600,480 540,490 490,470 C430,500 360,480 330,440 C280,450 210,420 190,380 C170,365 165,345 170,330 Z")
RX0, RX1, RY = 90, 990, 690
ticks = "".join(f'<path class="sn-tk" d="M{RX0+(RX1-RX0)*i/20:.1f},{RY-(30 if i%5==0 else 16)} L{RX0+(RX1-RX0)*i/20:.1f},{RY}" stroke="{K}" stroke-width="{5 if i%5==0 else 3}" stroke-linecap="round" fill="none"/>' for i in range(21))
SP = "M560,800 C620,720 720,720 800,800"
grains = "".join(f'<g id="sn-g{i}" opacity="0"><circle r="{7 + (i%3)*2}" fill="{DUST}" stroke="{K}" stroke-width="3"/></g>' for i in range(5))
scenes[s] = scene_file(s, f"""
#sn-map {{ position:absolute; left:0; top:0; }}
#sn-n {{ position:absolute; left:0; right:0; top:575px; text-align:center; }}
#sn-n .big {{ font-size:66px; color:{C['red']}; }}
""", f"""
  <svg id="sn-map" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="sn-fill" d="{ANT}" fill="{SNOW}" stroke="none" opacity="0" transform="translate(30,-40)"/>
    <path id="sn-ant" d="{ANT}" stroke="{K}" stroke-width="6" fill="none" stroke-linejoin="round" transform="translate(30,-40)"/>
    <g id="sn-flag" opacity="0"><path d="M540,300 L540,190" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
      <path d="M540,192 L600,208 L540,226 Z" fill="{C['red']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/><ellipse cx="540" cy="302" rx="22" ry="7" fill="{K}"/></g>
    {"".join(f'<path class="sn-fl" d="M{x-14},{y} L{x+14},{y} M{x},{y-14} L{x},{y+14} M{x-10},{y-10} L{x+10},{y+10} M{x-10},{y+10} L{x+10},{y-10}" stroke="{C["blue"]}" stroke-width="3" stroke-linecap="round" opacity="0"/>' for x, y in [(320, 300), (420, 380), (700, 260), (780, 360), (620, 400)])}
    <path id="sn-rl" d="M{RX0},{RY} L{RX1},{RY}" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>{ticks}
    <g id="sn-pot" opacity="0"><path d="M440,800 L456,920 Q500,936 544,920 L560,800 Z" fill="#DDE3EA" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M430,800 L570,800" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
      <path id="sn-water" d="M452,850 Q500,862 548,850 L542,914 Q500,928 458,914 Z" fill="{SEA}" opacity="0"/>
      <path id="sn-ice" d="M462,800 Q470,760 500,768 Q530,752 540,800 Z" fill="#FFFFFF" stroke="{C['blue']}" stroke-width="4"/></g>
    <g id="sn-sv" opacity="0"><path d="M760,820 Q840,880 920,820 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M780,834 L900,834 M800,848 L880,848 M840,822 L840,870 M810,826 L815,856 M870,826 L865,856" stroke="{C['pencil']}" stroke-width="3"/>
      <path d="M920,820 L990,800" stroke="{K}" stroke-width="10" stroke-linecap="round"/></g>
    <path id="sn-path" d="{SP}" stroke="{C['pencil']}" stroke-width="4" fill="none" stroke-dasharray="8 12" opacity="0"/>
    {grains}
  </svg>
  {tape("sn-tp", "Concordia station", 610, 175, 4, 44)}
  {tape("sn-at", "Antarctica", 330, 400, -3, 48, "rgba(191,227,247,.95)")}
  <div id="sn-n"><span id="sn-cnt" class="big">0 years</span></div>
""", J("""
ink("#sn-ant", @tant0, 0.9); tl.to("#sn-fill", {opacity:1, duration:0.4}, @tfill);
tl.fromTo(".sn-fl", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:0.07, ease:"back.out(3)"}, @tfill);
pop("#sn-flag", @tant, {from:{y:-40}, to:{}}); rise("#sn-tp", @ttp); rise("#sn-at", @tant);
ink("#sn-rl", @t20a, 0.4); ink(".sn-tk", @t20b, 0.6, {stagger:0.03});
rise("#sn-n", @t20b); count("#sn-cnt", 0, 20, @t20b, 0.8, v => "about " + Math.round(v) + " years");
pop("#sn-pot", @tmel0); tl.to("#sn-ice", {scaleY:0, transformOrigin:"50% 100%", duration:0.7, ease:"power1.in"}, @tmel); tl.to("#sn-water", {opacity:1, duration:0.5}, @tmel);
pop("#sn-sv", @tsif0); tl.to("#sn-path", {opacity:1, duration:0.2}, @tsif);
for (let i=0;i<5;i++) { const t = @tsif + 0.15 + i*0.18; tl.set("#sn-g"+i, {opacity:1}, t); along("#sn-g"+i, "#sn-path", t, 0.6, {ease:"power1.in"}); }
tl.fromTo("#sn-sv", {scale:1}, {scale:1.08, transformOrigin:"50% 50%", duration:0.12, yoyo:true, repeat:1}, @tgr);
""", tant0=tsc + 0.2, tfill=tsc + 1.1, tant=tant, ttp=tant + 0.3, t20a=t20 - 0.6, t20b=t20 - 0.2, tmel0=tmel - 0.3, tmel=tmel,
     tsif0=tsif - 0.4, tsif=tsif, tgr=tgr + 0.3))

# 5 GRAINS — sand grain vs space grain, then one continuous dive into the dot under the microscope
s = "grains"; ttin = aw(s, "tinier"); tsand = aw(s, "sand"); tmic = aw(s, "microscope"); tsee = aw(s, "see them")
rs = _r.Random(5)
sand_d = "M200,520 C190,440 260,400 330,410 C410,400 460,450 455,520 C470,600 400,650 330,640 C250,655 195,600 200,520 Z"
stip = "".join(f'<circle cx="{330+rs.uniform(-100,100):.0f}" cy="{525+rs.uniform(-90,90):.0f}" r="{rs.uniform(2,4):.1f}" fill="{C["muted"]}"/>' for _ in range(40))
bars = "".join(f'<path d="M{380+i*22},300 L{380+i*22 + 60},820" stroke="#5B3A22" stroke-width="7" opacity=".7"/>' for i in range(-12, 16))
scenes[s] = scene_file(s, f"""
#gr-title {{ top:150px; font-size:80px; }}
#gr-cam {{ position:absolute; left:0; top:0; width:{W}px; height:980px; transform-origin:780px 560px; }}
#gr-lens {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="gr-title" class="h1">Tinier than <span class="hl">sand</span></div>
  <div id="gr-cam">
    <svg width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
      <g id="gr-sand" opacity="0"><path d="{sand_d}" fill="#F3D9A4" stroke="{K}" stroke-width="6"/>{stip}</g>
      <text id="gr-sl" x="330" y="720" text-anchor="middle" font-family="Gochi Hand" font-size="48" fill="{K}" opacity="0">a sand grain</text>
      <circle id="gr-dot" cx="780" cy="560" r="8" fill="{DUST}" stroke="{K}" stroke-width="3" opacity="0"/>
      <path id="gr-ar" d="M860,700 Q860,600 800,575" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <text id="gr-dl" x="860" y="750" text-anchor="middle" font-family="Gochi Hand" font-size="48" fill="{C['red']}" opacity="0">space grain</text>
    </svg>
  </div>
  <svg id="gr-lens" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <clipPath id="gr-clip"><circle cx="540" cy="560" r="280"/></clipPath>
    <g id="gr-view" opacity="0"><circle cx="540" cy="560" r="280" fill="#F6F1E6"/>
      <g clip-path="url(#gr-clip)"><circle cx="540" cy="560" r="190" fill="#8A5A35" stroke="{K}" stroke-width="7"/>
        <g clip-path="url(#gr-clip2)">{bars}</g>
        <circle cx="480" cy="500" r="16" fill="#3A2616"/><circle cx="600" cy="640" r="10" fill="#3A2616"/><path d="M470,430 Q520,400 580,420" stroke="#FFFFFF" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/></g></g>
    <clipPath id="gr-clip2"><circle cx="540" cy="560" r="186"/></clipPath>
    <path id="gr-ring" d="M540,280 A280,280 0 1 1 539.9,280" stroke="{K}" stroke-width="14" fill="none"/>
  </svg>
  {tape("gr-tp", "under the microscope", 430, 870, -3, 46)}
""", J("""
rise("#gr-title", 0.05);
pop("#gr-sand", @tsand, {from:{rotation:-10}, to:{}}); rise("#gr-sl", @tsand2);
pop("#gr-dot", @ttin, {from:{scale:3}, to:{}}); ink("#gr-ar", @ttin2, 0.3); rise("#gr-dl", @ttin2);
tl.to("#gr-cam", {scale:14, duration:0.9, ease:"power2.in"}, @tz); tl.to("#gr-cam", {opacity:0, duration:0.25}, @tz2);
tl.to("#gr-title", {opacity:0, y:-20, duration:0.25}, @tz);
tl.to("#gr-view", {opacity:1, duration:0.3}, @tz2); ink("#gr-ring", @tz2, 0.5);
rise("#gr-tp", @tsee);
""", tsand=tsand - 0.4, tsand2=tsand, ttin=ttin, ttin2=ttin + 0.3, tz=tmic - 0.4, tz2=tmic + 0.3, tsee=tsee - 0.3))

# 6 ANSWER — 3D pull-back from a close patch to the whole Earth while dust rains in; counter to 5,200 tons / year
s = "answer"; tsca = aw(s, "scaled"); twp = aw(s, "whole planet"); tans = aw(s, "the answer"); t52 = aw(s, "five thousand"); tyr = aw(s, "every year"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#an-cv {{ position:absolute; left:40px; top:150px; width:1000px; height:640px; }}
#an-lab {{ position:absolute; left:0; right:0; top:790px; text-align:center; white-space:nowrap; }}
#an-n {{ font-size:110px; color:{C['red']}; }}
#an-u {{ font-size:64px; }}
""", f"""
  <canvas id="an-cv" width="1000" height="640"></canvas>
  {tape("an-tp", "whole planet!", 360, 170, -4, 54)}
  <div id="an-lab"><span id="an-n" class="big">0</span><span id="an-u" class="big"> tons / year</span></div>
""", EARTH_JS + J("""
const S = T3.stage("#an-cv", 1000, 640, 34);
const R = 1.7; const earth = buildEarth(S, R, 11);
const dust = buildDust(S, R, 150, 52, 0.1, @gap, R*2.7, 0.45);
const cam = k => { const e = k*k*(3-2*k); const dist = 2.9 + 5.3*e; S.cam.position.set(0.9*(1-e), 1.0*(1-e) + 0.6*e, dist); S.cam.lookAt(0.6*(1-e), 0.8*(1-e), 0); };
drive(@d, t => { cam(Math.min(1, Math.max(0, (t - @tp0)/@pd))); earth.userData.body.rotation.y = 0.25*t; dust(t); S.render(); });
pop("#an-tp", @twp, {from:{rotation:-12}, to:{rotation:-4}});
rise("#an-lab", @tans); count("#an-n", 0, 5200, @t52, 1.3, v => "≈ " + fmtInt(v >= 5150 ? 5200 : Math.round(v/100)*100));
tl.fromTo("#an-lab", {scale:1}, {scale:1.1, duration:0.14, yoyo:true, repeat:1}, @tyr);
""", d=d, gap=round((d - 0.8) / 150, 4), tp0=tsca, pd=round(twp + 0.8 - tsca, 3), twp=twp, tans=tans, t52=t52 - 0.1, tyr=tyr))

# 7 DAY — cards per year -> per day -> per minute; a 10 kg sack drops onto a hanging scale (along)
s = "day"; t14 = aw(s, "fourteen tons"); tday = aw(s, "every day"); t10 = aw(s, "ten kilograms"); tmin = aw(s, "single minute")
rows = [("dy-r1", "per year", "≈ 5,200 tons", 0.1, K), ("dy-r2", "per day", "≈ 14 tons", t14 - 0.1, C['blue']), ("dy-r3", "per minute", "≈ 10 kg", t10 - 0.1, C['red'])]
rh = "".join(f'<div id="{i}" class="card" style="left:{90+k*30}px;top:{160+k*150}px;width:{880-k*60}px;height:124px;opacity:0">'
             f'<span style="position:absolute;left:34px;top:22px;font-size:54px;color:{C["muted"]}">{a}</span>'
             f'<span class="big" style="position:absolute;right:36px;top:14px;font-size:84px;color:{c}">{b}</span></div>' for k, (i, a, b, t, c) in enumerate(rows))
DP = "M760,560 C760,600 740,640 720,700"
scenes[s] = scene_file(s, f"""
#dy-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  {rh}
  <svg id="dy-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <g id="dy-scale" opacity="0">
      <path d="M720,620 L720,660" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
      <circle cx="720" cy="740" r="80" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>
      {"".join(f'<path d="M720,672 L720,684" transform="rotate({a} 720 740)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for a in range(-120, 121, 30))}
      <g id="dy-ndl"><path d="M720,740 L720,676" stroke="{C['red']}" stroke-width="7" stroke-linecap="round"/></g><circle cx="720" cy="740" r="9" fill="{K}"/>
      <path d="M720,820 L720,860 M650,860 L790,860 L770,900 L670,900 Z" stroke="{K}" stroke-width="6" fill="#DDE3EA" stroke-linejoin="round"/>
    </g>
    <path id="dy-path" d="M720,560 C700,640 640,700 720,800" stroke="none" fill="none"/>
    <g id="dy-sack" opacity="0"><path d="M-55,40 Q-62,-20 -30,-40 L-18,-58 L18,-58 L30,-40 Q62,-20 55,40 Q0,52 -55,40 Z" fill="#E8C98E" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M-24,-46 L24,-46" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
      <text x="0" y="22" text-anchor="middle" font-family="Gochi Hand" font-size="38" fill="{K}">10 kg</text></g>
  </svg>
  {stamp("dy-st", "every minute!", 90, 700, -5, 54)}
""", J("""
@rows
pop("#dy-scale", @tsc); tl.set("#dy-ndl", {rotation:0, svgOrigin:"720 740"}, 0);
tl.set("#dy-sack", {opacity:1}, @tsk); along("#dy-sack", "M720,520 C720,600 720,700 720,782", @tsk, 0.45, {ease:"power2.in"});
tl.to("#dy-ndl", {rotation:110, duration:0.5, ease:"elastic.out(1,0.4)"}, @tland);
pop("#dy-st", @tmin, {from:{rotation:-14}, to:{}});
""", rows="".join(f'pop("#{i}", {t:.2f}, {{from:{{x:-60}}, to:{{x:0}}}});' for i, _, _, t, _ in rows), tsc=t10 - 0.6, tsk=t10 + 0.25, tland=t10 + 0.7, tmin=tmin - 0.2))

# 8 ROCKS — balance: a meteorite drops on the right, the dust heap slams the left, DUST WINS!
s = "rocks"; tmet = aw(s, "meteorites"); tls = aw(s, "less than"); tdw = aw(s, "dust wins")
_hr = _r.Random(8); _hp = []
while len(_hp) < 80:
    x, y = _hr.uniform(-95, 95), _hr.uniform(-80, 0)
    if -y < 80 * (1 - abs(x) / 100): _hp.append((x, y))
heap = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{_hr.uniform(4,8):.1f}" fill="{DUST}" stroke="{K}" stroke-width="2"/>' for x, y in _hp)
scenes[s] = scene_file(s, f"""
#rk-title {{ top:150px; font-size:76px; }}
#rk-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="rk-title" class="h1">Big rocks vs. <span class="hl">dust</span></div>
  <svg id="rk-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="rk-post" d="M540,420 L540,850 M440,860 L640,860" stroke="{K}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <g id="rk-beam"><path id="rk-bl" d="M210,420 L870,420" stroke="{K}" stroke-width="12" fill="none" stroke-linecap="round"/>
      <circle cx="540" cy="420" r="16" fill="{C['hi']}" stroke="{K}" stroke-width="5"/></g>
    <g id="rk-pl"><path d="M210,420 L130,560 M210,420 L290,560" stroke="{K}" stroke-width="4"/>
      <path d="M110,560 L310,560 Q210,610 110,560 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <g transform="translate(210,556)"><g id="rk-heap" opacity="0">{heap}</g></g>
      <text id="rk-dl" x="210" y="660" text-anchor="middle" font-family="Gochi Hand" font-size="50" fill="{C['blue']}" opacity="0">dust ≈ 5,200 tons</text></g>
    <g id="rk-pr"><path d="M870,420 L790,560 M870,420 L950,560" stroke="{K}" stroke-width="4"/>
      <path d="M770,560 L970,560 Q870,610 770,560 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path id="rk-rock" d="M836,556 C826,520 850,496 874,500 C900,494 916,520 908,556 Z" fill="#7A7268" stroke="{K}" stroke-width="5" opacity="0"/>
      <text id="rk-rl" x="870" y="660" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{C['red']}" opacity="0">rocks &lt; 10 tons</text></g>
  </svg>
  {tape("rk-tp", "per year", 430, 300, 3, 44)}
  {stamp("rk-st", "DUST WINS!", 500, 720, -8, 76)}
""", J("""
rise("#rk-title", 0.05); ink("#rk-post", 0.15, 0.4); ink("#rk-bl", 0.3, 0.4);
tl.set("#rk-beam", {rotation:0, svgOrigin:"540 420"}, 0);
tl.fromTo("#rk-rock", {opacity:0, y:-240}, {opacity:1, y:0, duration:0.35, ease:"bounce.out"}, @tmet);
tl.to("#rk-beam", {rotation:6, duration:0.4, ease:"back.out(2)"}, @tmet2); tl.to("#rk-pr", {y:34, duration:0.4, ease:"back.out(2)"}, @tmet2); tl.to("#rk-pl", {y:-34, duration:0.4, ease:"back.out(2)"}, @tmet2);
rise("#rk-rl", @tls); rise("#rk-tp", @tls2);
tl.fromTo("#rk-heap", {opacity:0, y:-300}, {opacity:1, y:0, duration:0.3, ease:"power3.in"}, @tdw0);
tl.to("#rk-beam", {rotation:-16, duration:0.45, ease:"back.out(2.5)"}, @tdw); tl.to("#rk-pl", {y:90, duration:0.45, ease:"back.out(2.5)"}, @tdw); tl.to("#rk-pr", {y:-90, duration:0.45, ease:"back.out(2.5)"}, @tdw);
rise("#rk-dl", @tdw); pop("#rk-st", @tdw2, {from:{rotation:-20, scale:1.8}, to:{}});
""", tmet=tmet + 0.1, tmet2=tmet + 0.4, tls=tls, tls2=tls + 0.5, tdw0=tdw - 0.3, tdw=tdw, tdw2=tdw + 0.35))

# 9 COMETS — comet rides its orbit (MotionPath, autoRotate) shedding dust; pie wedge inks to 80 %
s = "comets"; twh = aw(s, "where does"); tsci = aw(s, "scientists"); t80 = aw(s, "eighty percent"); tcm = aw(s, "comets")
ORB = "M900,370 A380,150 0 1 1 140,370 A380,150 0 1 1 900,370"
PR = 95; PCX, PCY = 560, 760
a80 = 0.8 * 2 * _m.pi
WEDGE = f"M{PCX},{PCY-PR/2} A{PR/2},{PR/2} 0 1 1 {PCX + PR/2*_m.sin(a80):.1f},{PCY - PR/2*_m.cos(a80):.1f}"
rs = _r.Random(9)
trail = "".join(f'<circle class="cm-d" cx="{520 + 380*_m.cos(a) + rs.uniform(-10,10):.0f}" cy="{370 + 150*_m.sin(a) + rs.uniform(-10,10):.0f}" r="{rs.uniform(3,6):.1f}" fill="{DUST}"/>' for a in [_m.pi*(-0.5 + i*0.06) for i in range(-6, 7)])
scenes[s] = scene_file(s, f"""
#cm-svg {{ position:absolute; left:0; top:0; }}
#cm-lab {{ position:absolute; left:700px; top:650px; }}
#cm-lab .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <svg id="cm-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="cm-orb" d="{ORB}" stroke="{C['pencil']}" stroke-width="4" fill="none" stroke-dasharray="10 12"/>
    <circle id="cm-sun" cx="185" cy="370" r="34" fill="#FFC23A" stroke="{K}" stroke-width="5"/>
    {trail}
    <g id="cm-earth"><circle cx="520" cy="220" r="26" fill="{SEA}" stroke="{K}" stroke-width="5"/><path d="M505,212 Q515,200 528,210 Q524,224 510,222 Z" fill="{LAND}" stroke="{K}" stroke-width="2"/></g>
    <text x="556" y="234" font-family="Gochi Hand" font-size="40" fill="{K}">Earth</text>
    <g id="cm-com" opacity="0"><path d="M-10,-14 L-120,-4 L-110,4 L-120,12 L-10,14 Z" fill="#BFE3F7" stroke="{K}" stroke-width="3" stroke-linejoin="round" opacity=".9"/>
      <circle r="18" fill="#FFFFFF" stroke="{K}" stroke-width="5"/></g>
    <circle cx="{PCX}" cy="{PCY}" r="{PR}" fill="#FFFFFF" stroke="{K}" stroke-width="6" id="cm-pie" opacity="0"/>
    <path id="cm-w" d="{WEDGE}" stroke="{C['hi']}" stroke-width="{PR}" fill="none"/>
    <circle cx="{PCX}" cy="{PCY}" r="{PR}" fill="none" stroke="{K}" stroke-width="6" id="cm-pie2" opacity="0"/>
  </svg>
  <div id="cm-lab"><div class="big">≈ 80%</div><div style="font-size:52px">comets</div><div style="font-size:38px;color:{C['muted']}">rest: asteroids</div></div>
  {tape("cm-tp", "where from?", 110, 150, -4, 54)}
""", J("""
rise("#cm-tp", @twh); ink("#cm-orb", 0.1, 0.8);
tl.set("#cm-com", {opacity:1}, 0.5); along("#cm-com", "#cm-orb", 0.5, @lap, {ease:"none", rotate:true});
tl.fromTo(".cm-d", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, stagger:0.05, ease:"back.out(3)"}, @tdust);
pop("#cm-pie", @tsci); tl.set("#cm-pie2", {opacity:1}, @tsci);
ink("#cm-w", @t80, 0.7, {ease:"power2.out"});
pop("#cm-lab .big", @t80b); rise("#cm-lab div:nth-child(2)", @tcm); rise("#cm-lab div:nth-child(3)", @tcm2);
""", twh=twh - 0.1, lap=round(SC[s]["slot"] - 0.8, 3), tdust=1.6, tsci=tsci, t80=t80 - 0.1, t80b=t80 + 0.2, tcm=tcm - 0.1, tcm2=tcm + 0.4))

# 10 ROOF — cutaway house, rain runs into the gutter, lens shows glinting space grains; tape pins Paris, Oslo
s = "roof"; ttw = aw(s, "twist"); tres = aw(s, "researchers"); thun = aw(s, "hundreds"); trg = aw(s, "rooftop gutters"); tpar = aw(s, "Paris"); tosl = aw(s, "Oslo")
rs = _r.Random(14)
peb = "".join(f'<ellipse cx="{820+rs.uniform(-140,140):.0f}" cy="{420+rs.uniform(-40,120):.0f}" rx="{rs.uniform(6,14):.0f}" ry="{rs.uniform(4,9):.0f}" fill="#9C8F80" stroke="{K}" stroke-width="2"/>' for _ in range(22))
sg = []
while len(sg) < 26:
    x, y = 820 + rs.uniform(-140, 140), 400 + rs.uniform(-50, 140)
    if (x-820)**2 + (y-400)**2 < 150**2 and y > 345: sg.append((x, y))
spher = "".join(f'<g class="rf-g"><circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#3A2616" stroke="{K}" stroke-width="2"/><circle cx="{x-2:.0f}" cy="{y-2:.0f}" r="2.4" fill="#FFFFFF"/></g>' for x, y in sg)
RAIN = "M300,330 L520,470 L640,540"
scenes[s] = scene_file(s, f"""
#rf-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <svg id="rf-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <clipPath id="rf-lc"><circle cx="820" cy="420" r="160"/></clipPath>
    <path id="rf-wall" d="M140,560 L140,820 L600,820 L600,560" fill="#FFFFFF" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    <path d="M260,820 L260,700 L340,700 L340,820 M430,630 L520,630 L520,700 L430,700 Z" stroke="{K}" stroke-width="5" fill="#BFE3F7" stroke-linejoin="round"/>
    <path id="rf-roof" d="M100,570 L370,330 L640,560 Z" fill="#E9806E" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    <path d="M190,490 L560,490 M260,430 L480,430" stroke="{K}" stroke-width="3" opacity=".5"/>
    <path id="rf-gut" d="M610,550 L612,590 Q640,604 668,590 L670,550" fill="#DDE3EA" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
    <path id="rf-rain" d="{RAIN}" stroke="none" fill="none"/>
    {"".join(f'<g id="rf-r{i}" opacity="0"><path d="M0,-12 Q7,0 0,8 Q-7,0 0,-12 Z" fill="{SEA}" stroke="{C["blue"]}" stroke-width="3"/></g>' for i in range(4))}
    <path id="rf-cut" d="M640,575 C700,560 720,500 690,470" stroke="{C['red']}" stroke-width="5" fill="none" stroke-dasharray="12 10" stroke-linecap="round"/>
    <g id="rf-lens" opacity="0"><circle cx="820" cy="420" r="160" fill="#8C7356"/>
      <g clip-path="url(#rf-lc)"><path d="M660,340 Q820,310 980,350 L980,600 L660,600 Z" fill="#6E5A44"/>{peb}{spher}</g></g>
    <path id="rf-ring" d="M820,260 A160,160 0 1 1 819.9,260" stroke="{K}" stroke-width="12" fill="none"/>
  </svg>
  {stamp("rf-st", "TWIST!", 120, 170, -8, 76)}
  {tape("rf-h", "hundreds of space grains!", 480, 610, 3, 42)}
  {tape("rf-p", "Paris", 450, 860, -5, 54, "rgba(191,227,247,.95)")}
  {tape("rf-o", "Oslo", 760, 860, 4, 54, "rgba(255,201,194,.95)")}
""", J("""
pop("#rf-st", @ttw, {from:{rotation:-20, scale:1.8}, to:{}});
for (let i=0;i<4;i++) { const t = @trn + i*0.35; tl.set("#rf-r"+i, {opacity:1}, t); along("#rf-r"+i, "#rf-rain", t, 0.6, {ease:"power1.in"}); tl.set("#rf-r"+i, {opacity:0}, t + 0.6); }
ink("#rf-cut", @tres, 0.4); ink("#rf-ring", @tres2, 0.5); tl.to("#rf-lens", {opacity:1, duration:0.3}, @tres2);
tl.fromTo(".rf-g", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, stagger:0.03, ease:"back.out(3)"}, @thun);
rise("#rf-h", @thun2);
tl.fromTo("#rf-gut", {scale:1}, {scale:1.15, transformOrigin:"50% 50%", duration:0.15, yoyo:true, repeat:1}, @trg);
pop("#rf-p", @tpar, {from:{y:-60}, to:{}}); pop("#rf-o", @tosl, {from:{y:-60}, to:{}});
""", ttw=ttw - 0.1, trn=0.3, tres=tres, tres2=tres + 0.3, thun=thun, thun2=thun + 0.6, trg=trg, tpar=tpar - 0.05, tosl=tosl - 0.05))

# 11 OUTRO — red "?" morphs into a dust sparkle (hook callback); specks drift down; Stay curious (Max centre: keep y < 620)
s = "outro"; t52 = aw(s, "five thousand"); tfal = aw(s, "falling"); tsc = aw(s, "stay curious"); d = SC[s]["slot"]
QM = "M470,230 Q470,150 540,150 Q610,150 610,215 Q610,262 545,290 L545,350"
SPK = "M545,150 L572,250 L660,280 L572,310 L545,410 L518,310 L430,280 L518,250 Z"
rs = _r.Random(41)
specks = "".join(f'<circle class="ou-sp" data-x="{rs.uniform(60,1020):.0f}" data-v="{rs.uniform(70,140):.0f}" data-y="{rs.uniform(-40,600):.0f}" cx="0" cy="0" r="{rs.uniform(3,7):.1f}" fill="{DUST}"/>' for _ in range(40))
scenes[s] = scene_file(s, f"""
#ou-chip {{ position:absolute; left:0; right:0; top:470px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" class="abs" style="left:0;top:0" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <g id="ou-sps" opacity="0">{specks}</g>
    <path id="ou-qk" d="{QM}" stroke="{K}" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-q" d="{QM}" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="ou-qd" cx="545" cy="420" r="20" fill="{C['red']}" stroke="{K}" stroke-width="7"/>
  </svg>
  <div id="ou-chip"><span class="chip">≈ 5,200 tons / year</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", SIM + J("""
pop("#ou-svg", 0.05, {from:{scale:0.8}, to:{}});
morph("#ou-qk", "@spk", @t52, 0.55, {ease:"back.out(1.4)"}); morph("#ou-q", "@spk", @t52, 0.55, {ease:"back.out(1.4)"});
tl.to("#ou-q", {stroke:"@dust", fill:"@hi", duration:0.3}, @t52b); tl.to("#ou-qk", {strokeWidth:24, duration:0.3}, @t52b);
tl.to("#ou-qd", {opacity:0, scale:0, transformOrigin:"50% 50%", duration:0.2}, @t52);
pop("#ou-chip", @t52c, {from:{rotation:-10}, to:{rotation:-2}});
const SP = Array.from(document.querySelectorAll(".ou-sp"));
sim(@d, t => { const k = Math.max(0, t - @tfal); SP.forEach(e => { const y = ((+e.dataset.y + 40 + k*(+e.dataset.v)) % 660) - 40; e.setAttribute("cx", e.dataset.x); e.setAttribute("cy", y.toFixed(1)); }); });
tl.to("#ou-sps", {opacity:1, duration:0.3}, @tfal);
tl.to("#ou-qk, #ou-q, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
tl.to("#ou-sps", {opacity:0.35, duration:0.3}, @tsc0);
pop("#ou-c", @tsc1);
""", spk=SPK, dust=DUST, hi=C['hi'], t52=t52 - 0.05, t52b=t52 + 0.25, t52c=t52 + 0.5, d=d, tfal=tfal - 0.2, tsc0=tsc - 0.45, tsc1=tsc - 0.2), fade=False)
# === GESTURES ===
think(g("hook", "how much"), SC["guess"]["start"] + 0.2)
point(g("guess", "bucketful"), 2.6)
wave(g("intro", "I'm Max"))
point(g("snow", "Antarctica"), 1.3)
point(g("grains", "microscope"), 1.2)
wow(g("answer", "five thousand"), 1.5)
point(g("day", "ten kilograms"), 1.2)
wow(g("rocks", "dust wins"), 1.2)
think(SC["comets"]["start"] + 0.05, g("comets", "scientists"))
point(g("comets", "eighty percent"), 1.2)
wow(g("roof", "hundreds"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "tiny bits"), 0.35), ("ping.mp3", A("hook", "every year") + 0.1, 0.35),
        ("pop.mp3", A("guess", "bucketful"), 0.5), ("pop.mp3", A("guess", "hundred tons"), 0.5), ("pop.mp3", A("guess", "thousands"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("snow", "Antarctica"), 0.55),
        ("whoosh-short.mp3", A("grains", "microscope") - 0.3, 0.35), ("riser.mp3", A("answer", "the answer") - 0.2, 0.22),
        ("impact-bass-1.mp3", A("answer", "five thousand") + 1.2, 0.4), ("click.mp3", A("day", "ten kilograms") + 0.7, 0.5),
        ("impact-bass-2.mp3", A("rocks", "dust wins"), 0.4), ("pop.mp3", A("comets", "eighty percent") + 0.2, 0.5),
        ("pop.mp3", A("roof", "Paris"), 0.45), ("pop.mp3", A("roof", "Oslo"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
