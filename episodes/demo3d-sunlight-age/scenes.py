# MAX WISE demo3d — When you see sunlight, how old is it?
# Trial episode for the new kit: GSAP DrawSVG / MorphSVG / MotionPath helpers (ink, morph, along) and three.js scenes (T3, drive).
# === SCENES ===
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling)"""
    for k, v in kw.items(): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src

# shared 3D sun builder (lumpy toon sphere, seeded so every render is identical)
SUN_JS = """
function lumpySun(R, seed, phiStart, phiLen) {
  const geo = new THREE.SphereGeometry(R, 64, 40, phiStart||0, phiLen||Math.PI*2);
  const rnd = T3.seeded(seed); const bumps = Array.from({length:10}, () => [rnd()*6.283, rnd()*3.14, 0.004+rnd()*0.008]);
  const p = geo.attributes.position, v = new THREE.Vector3();
  for (let i=0;i<p.count;i++) { v.fromBufferAttribute(p,i); const th=Math.acos(v.y/R), ph=Math.atan2(v.z,v.x); let k=1;
    for (const [a,b,h] of bumps) k += h*Math.cos(3*(ph-a))*Math.sin(2*(th-b)); v.multiplyScalar(k); p.setXYZ(i,v.x,v.y,v.z); }
  geo.computeVertexNormals(); return geo;
}
"""

# 1 HOOK — 3D sun, rays draw themselves
s = "hook"; tsun = aw(s, "sunshine"); thow = aw(s, "how old"); d = SC[s]["slot"]
rays = "".join(f'<path class="hk-ray" d="M{350+250*__import__("math").cos(a):.1f},{350+250*__import__("math").sin(a):.1f} L{350+330*__import__("math").cos(a):.1f},{350+330*__import__("math").sin(a):.1f}" {WS.replace("5", "9", 1)}/>' for a in [i*0.5236 for i in range(12)])
scenes[s] = scene_file(s, f"""
#hk-box {{ position:absolute; left:190px; top:110px; width:700px; height:700px; }}
#hk-cv {{ position:absolute; left:0; top:0; width:700px; height:700px; }}
#hk-rays {{ position:absolute; left:0; top:0; }}
#hk-q {{ top:790px; font-size:84px; }}
""", f"""
  <div id="hk-box"><canvas id="hk-cv" width="700" height="700"></canvas>
    <svg id="hk-rays" width="700" height="700" viewBox="0 0 700 700" data-layout-ignore>{rays}</svg></div>
  <div id="hk-q" class="h1">How <span class="hl">old</span> is sunlight?</div>
""", SUN_JS + J("""
const S = T3.stage("#hk-cv", 700, 700, 30); S.cam.position.set(0, 0.6, 11.5); S.cam.lookAt(0, 0, 0);
const sun = T3.inked(lumpySun(2, 7), 0xFFC23A, 0.045); S.scene.add(sun);
// a few darker sunspots so the turning reads
const rnd = T3.seeded(3);
for (let i=0;i<6;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.16+rnd()*0.1, 16, 10), T3.toon(0xF29A2E));
  m.position.setFromSphericalCoords(1.93, 0.8+rnd()*1.5, rnd()*6.283); m.scale.set(1,1,0.35); m.lookAt(0,0,0); sun.add(m); }
drive(@d, t => { sun.rotation.y = 0.35*t; sun.rotation.z = 0.08*Math.sin(t*0.9); const s = t<0.5 ? 0.6+0.4*gsap.parseEase("back.out(2)")(t/0.5) : 1; sun.scale.setScalar(s); S.render(); });
ink(".hk-ray", @tsun, 0.5, {stagger:0.05});
tl.to("#hk-rays", {rotation:12, transformOrigin:"50% 50%", duration:@d, ease:"none"}, 0);
rise("#hk-q", @thow);
""", d=d, tsun=tsun - 0.15, thow=thow - 0.1))

# 2 GUESS — sticky notes, pyramid drawn on the last one
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "brand new"); t2 = aw(s, "a few"); t3 = aw(s, "older than")
notes = [("a", "brand new?", -6, 110, C['hi']), ("b", "a few minutes?", 4, 405, "#BFE3F7"), ("c", "older than the pyramids?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;font-family:Gochi Hand,cursive;font-size:54px;line-height:1.05;padding:46px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  <svg class="abs" style="left:790px;top:582px" width="110" height="72" viewBox="0 0 160 110" data-layout-ignore>
    <path id="gs-pyr" d="M10,100 L80,12 L150,100 Z M80,12 L96,100 M40,62 L120,62" {WS}/></svg>
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink("#gs-pyr", @tp, 0.7);
""", tg=tg, t1=t1, t2=t2, t3=t3, tp=t3 + 0.35))

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tsb = aw(s, "sunbeam")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="300" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="in-beam" d="M150,250 C260,170 330,290 440,215 S640,170 720,235 S860,250 930,205" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-dasharray="2 18"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's chase a sunbeam!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tsb); ink("#in-beam", @tb, 0.7);
""", tmw=tmw, tu=tmw + 0.3, tsb=tsb - 0.5, tb=tsb))

# 4 DISTANCE — 3D pull-back from the Sun to a tiny Earth
s = "distance"; t93 = aw(s, "ninety three"); tmil = aw(s, "million"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#ds-cv {{ position:absolute; left:40px; top:150px; width:1000px; height:620px; }}
#ds-line {{ position:absolute; left:40px; top:150px; }}
#ds-lab {{ position:absolute; left:0; right:0; top:780px; text-align:center; }}
#ds-lab .big {{ font-size:104px; color:{C['red']}; }}
#ds-e {{ position:absolute; font-size:44px; }}
""", f"""
  <canvas id="ds-cv" width="1000" height="620"></canvas>
  <svg id="ds-line" width="1000" height="620" viewBox="0 0 1000 620" data-layout-ignore>
    <path id="ds-p" d="M0,0 L1,1" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="18 14"/></svg>
  <div id="ds-e" style="left:820px;top:420px;opacity:0">Earth</div>
  <div id="ds-lab"><span class="big">≈ 93,000,000 miles</span><div style="font-size:46px">(about 150 million km)</div></div>
""", SUN_JS + J("""
const S = T3.stage("#ds-cv", 1000, 620, 32);
const sun = T3.inked(lumpySun(1.8, 7), 0xFFC23A, 0.04); sun.position.set(-3.2, 0, 0); S.scene.add(sun);
const earth = T3.inked(new THREE.SphereGeometry(0.32, 32, 20), 0x4F9BE0, 0.09); earth.position.set(4.1, -0.1, 0); S.scene.add(earth);
const land = new THREE.Mesh(new THREE.SphereGeometry(0.325, 32, 20, 0, 1.6, 0.6, 1.2), T3.toon(0x7CC46A)); earth.add(land);
const A = new THREE.Vector3(-3.2, 0, 0), B = new THREE.Vector3(0.45, 0, 0);
const cam = (k) => { const e = k*k*(3-2*k); S.cam.position.set(-3.2 + 3.65*e, 0.2 + 0.3*e, 4.6 + 10.4*e); S.cam.lookAt(-3.2 + 3.65*e, 0, 0); };
// measure the final framing once, to place the dashed line between the two bodies
cam(1); S.cam.updateMatrixWorld(); const pr = (v) => { const q = v.clone().project(S.cam); return [(q.x+1)*500, (1-q.y)*310]; };
const a = pr(new THREE.Vector3(-1.3, 0, 0)), b = pr(new THREE.Vector3(3.7, -0.1, 0)), eL = pr(new THREE.Vector3(4.1, 0.6, 0));
gsap.set("#ds-e", {left: 40 + eL[0] - 60, top: 150 + eL[1] - 70});
document.getElementById("ds-p").setAttribute("d", `M${a[0].toFixed(1)},${a[1].toFixed(1)} L${b[0].toFixed(1)},${b[1].toFixed(1)}`);
drive(@d, t => { cam(Math.min(1, Math.max(0, (t-0.2)/@pull))); sun.rotation.y = 0.3*t; earth.rotation.y = 0.8*t; S.render(); });
ink("#ds-p", @t93, 0.9); pop("#ds-e", @te);
pop("#ds-lab", @tmil);
""", d=d, pull=max(0.8, t93 - 0.3), t93=t93, te=t93 + 0.7, tmil=tmil - 0.1))

# 5 SPEED — a light dot laps a doodle Earth seven times
s = "speed"; tfast = aw(s, "fastest"); t186 = aw(s, "one hundred eighty"); tsec = aw(s, "every second"); t7 = aw(s, "seven laps"); ttick = aw(s, "one tick")
scenes[s] = scene_file(s, f"""
#sp-title {{ top:150px; font-size:76px; }}
#sp-svg {{ position:absolute; left:240px; top:250px; }}
#sp-lab {{ position:absolute; left:0; right:0; top:780px; text-align:center; }}
#sp-lab .big {{ font-size:84px; color:{C['red']}; }}
#sp-lap {{ position:absolute; left:440px; top:460px; width:200px; text-align:center; font-family:'Gochi Hand',cursive; font-size:120px; color:{C['red']}; -webkit-text-stroke:3px #fff; paint-order:stroke; opacity:0; }}
""", f"""
  <div id="sp-title" class="h1">Light is <span class="hl">fast</span></div>
  <svg id="sp-svg" width="600" height="520" viewBox="0 0 600 520" data-layout-ignore>
    <path id="sp-orb" d="M300,40 A230,230 0 1 1 299.9,40" stroke="{C['pencil']}" stroke-width="4" fill="none" stroke-dasharray="10 12"/>
    <circle cx="300" cy="270" r="150" fill="#BFE3F7" stroke="{K}" stroke-width="6"/>
    <path d="M200,220 Q240,170 290,200 Q300,250 250,270 Q210,280 200,220 Z M320,300 Q380,280 400,330 Q380,380 330,370 Z" fill="#9BD08F" stroke="{K}" stroke-width="4"/>
    <g id="sp-dot" opacity="0"><circle r="34" fill="#FFD646" opacity=".35"/><circle r="20" fill="{C['hi']}" stroke="{K}" stroke-width="5"/></g>
  </svg>
  <div id="sp-lap">0</div>
  <div id="sp-lab"><span class="big">186,000 miles</span><div style="font-size:50px">every second</div></div>
""", J("""
rise("#sp-title", @tf);
pop("#sp-lab .big", @t186); rise("#sp-lab div", @tsec);
tl.set("#sp-dot", {opacity:1}, @t7);
along("#sp-dot", "#sp-orb", @t7, @lap, {ease:"none", repeat:6});
tl.to("#sp-lap", {opacity:1, duration:0.15}, @t7);
count("#sp-lap", 0, 7, @t7, @run, v => String(Math.min(7, Math.floor(v + 0.15))) + "x");
tl.to("#sp-dot", {opacity:0, duration:0.2}, @tend);
tl.fromTo("#sp-lap", {scale:1}, {scale:1.25, duration:0.15, yoyo:true, repeat:1}, @ttick);
""", tf=tfast - 0.2, t186=t186, tsec=tsec, t7=t7 - 0.1, lap=round((ttick - t7 + 0.3) / 7, 3), run=round(ttick - t7 + 0.3, 3), tend=ttick + 0.35, ttick=ttick))

# 6 TRIP — division, counter, clock
s = "trip"; tdv = aw(s, "divide"); t500 = aw(s, "five hundred"); t8 = aw(s, "eight minutes"); t20 = aw(s, "twenty seconds")
ticks = "".join(f'<path class="tr-tk" d="M150,{22 if i%3==0 else 32} L150,{50}" transform="rotate({i*30} 150 150)" stroke="{K}" stroke-width="{6 if i%3==0 else 4}" stroke-linecap="round"/>' for i in range(12))
scenes[s] = scene_file(s, f"""
#tr-card {{ position:absolute; left:90px; top:170px; width:900px; height:190px; }}
#tr-eq {{ position:absolute; left:0; right:0; top:46px; text-align:center; font-family:'Gochi Hand',cursive; font-size:74px; }}
#tr-ans {{ position:absolute; left:0; right:0; top:400px; text-align:center; }}
#tr-n {{ font-size:130px; color:{C['red']}; }}
#tr-clk {{ position:absolute; left:400px; top:610px; }}
#tr-lab {{ position:absolute; left:720px; top:690px; }}
""", f"""
  <div id="tr-card" class="card"><div id="tr-eq"><span class="blue">93,000,000</span> ÷ <span class="blue">186,000</span></div></div>
  <div id="tr-ans"><span id="tr-n" class="big">0</span><span style="font-size:60px"> seconds</span></div>
  <svg id="tr-clk" width="300" height="300" viewBox="0 0 300 300" data-layout-ignore>
    <path id="tr-wedge" d="M150,150 L150,30 A120,120 0 0 1 150,30 Z" fill="{C['hi']}" opacity=".9"/>
    <circle id="tr-face" cx="150" cy="150" r="128" stroke="{K}" stroke-width="7" fill="none"/>{ticks}
    <g id="tr-hand"><path d="M150,150 L150,52" stroke="{C['red']}" stroke-width="9" stroke-linecap="round"/></g><circle cx="150" cy="150" r="10" fill="{K}"/></svg>
  <div id="tr-lab"><span class="pill" style="font-size:66px">8 min<br>20 s</span></div>
""", J("""
pop("#tr-card", @tdv, {from:{rotation:-6}, to:{rotation:-1}});
rise("#tr-ans", @tc0); count("#tr-n", 0, 499, @tc0, 1.0, v => "≈ " + fmtInt(Math.round(v/10)*10 > 495 ? 500 : Math.round(v/10)*10));
ink("#tr-face", @tclk, 0.6); ink(".tr-tk", @tclk2, 0.25, {stagger:0.03});
tl.set("#tr-hand", {rotation:0, svgOrigin:"150 150"}, 0); tl.fromTo("#tr-hand", {opacity:0}, {opacity:1, duration:0.1}, @tclk2);
const W = {a:0}; const wed = document.getElementById("tr-wedge");
tl.to(W, {a:50, duration:1.2, ease:"power1.inOut", onUpdate:() => { const r = W.a*Math.PI/180, x = 150 + 120*Math.sin(r), y = 150 - 120*Math.cos(r);
  wed.setAttribute("d", `M150,150 L150,30 A120,120 0 ${W.a>180?1:0} 1 ${x.toFixed(1)},${y.toFixed(1)} Z`); }}, @t8);
tl.to("#tr-hand", {rotation:50, duration:1.2, ease:"power1.inOut"}, @t8);
pop("#tr-lab .pill", @t20);
""", tdv=tdv - 0.2, tc0=t500 - 0.9, tclk=t8 - 0.9, tclk2=t8 - 0.4, t8=t8, t20=t20))

# 7 PAST — the Sun outline morphs into a photo frame
s = "past"; tnow = aw(s, "right now"); tago = aw(s, "eight minutes ago"); tnever = aw(s, "never")
scenes[s] = scene_file(s, f"""
#ps-svg {{ position:absolute; left:240px; top:170px; }}
#ps-now {{ position:absolute; left:0; right:0; top:640px; text-align:center; font-size:84px; color:{C['pencil']}; }}
#ps-stamp {{ position:absolute; left:0; right:0; top:760px; text-align:center; }}
#ps-stamp .chip {{ font-size:70px; }}
""", f"""
  <svg id="ps-svg" width="600" height="460" viewBox="0 0 600 460" data-layout-ignore>
    <path id="ps-frame" d="M300,40 C420,40 500,120 500,230 C500,340 420,420 300,420 C180,420 100,340 100,230 C100,120 180,40 300,40 Z" fill="#FFF3C4" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path id="ps-rect" d="M300,30 L560,30 L560,440 L40,440 L40,30 Z" fill="none" stroke="none"/>
    <g id="ps-sun" opacity="0"><circle cx="300" cy="215" r="80" fill="#FFC23A" stroke="{K}" stroke-width="6"/>
      <path d="M300,105 L300,80 M300,325 L300,350 M190,215 L165,215 M410,215 L435,215 M222,137 L205,120 M378,137 L395,120 M222,293 L205,310 M378,293 L395,310" stroke="{K}" stroke-width="6" stroke-linecap="round"/></g>
  </svg>
  <div id="ps-now">the Sun <span style="color:{K}">right now</span>?
    <svg class="abs" style="left:170px;top:20px" width="740" height="80" data-layout-ignore><path id="ps-x" d="M10,60 Q370,20 730,40" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/></svg></div>
  <div id="ps-stamp"><span class="chip">8 minutes ago</span></div>
""", J("""
pop("#ps-frame", 0.1, {from:{scale:0.6}, to:{}}); tl.set("#ps-frame", {transformOrigin:"50% 50%"}, 0);
rise("#ps-now", @tnever); ink("#ps-x", @tx, 0.45);
morph("#ps-frame", "#ps-rect", @tm, 0.7, {ease:"back.inOut(1.4)"});
tl.to("#ps-frame", {fill:"#FFFFFF", duration:0.4}, @tm);
tl.fromTo("#ps-sun", {opacity:0, scale:0.4, transformOrigin:"300px 215px"}, {opacity:1, scale:1, duration:0.4, ease:"back.out(2)"}, @tsun);
pop("#ps-stamp .chip", @tago, {from:{rotation:-14, scale:1.6}, to:{rotation:-4}});
""", tnever=tnever - 0.1, tx=tnow + 0.25, tm=tago - 1.0, tsun=tago - 0.4, tago=tago))

# 8 INSIDE — 3D cutaway sun, seeded photon random walk from the core
s = "inside"; tdeep = aw(s, "deeper"); tcore = aw(s, "core"); tpin = aw(s, "bounced"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#ins-cv {{ position:absolute; left:90px; top:140px; width:900px; height:820px; }}
#ins-core {{ position:absolute; left:640px; top:190px; opacity:0; }}
#ins-pin {{ position:absolute; left:110px; top:180px; opacity:0; }}
""", f"""
  <canvas id="ins-cv" width="900" height="820"></canvas>
  <div id="ins-core"><span class="chip" style="font-size:52px">the core</span></div>
  <div id="ins-pin"><span class="pill" style="font-size:56px;color:{C['red']}">boing! boing!</span></div>
""", SUN_JS + J("""
const S = T3.stage("#ins-cv", 900, 820, 30);
const R = 2.3, phiM = 2.04, phiStart = phiM - 1.75*Math.PI, phiLen = 1.5*Math.PI;
const shell = new THREE.Group(); S.scene.add(shell);
const body = new THREE.Mesh(lumpySun(R, 7, phiStart, phiLen), T3.toon(0xFFC23A, {side:THREE.DoubleSide})); shell.add(body);
const hull = new THREE.Mesh(new THREE.SphereGeometry(R*1.035, 64, 40, phiStart, phiLen), new THREE.MeshBasicMaterial({color:0x262A3B, side:THREE.BackSide})); shell.add(hull);
// the two cut faces: rings for core / radiative zone / convective zone, drawn on a 2D canvas
const tc = document.createElement("canvas"); tc.width = tc.height = 512; const g = tc.getContext("2d");
[[256,"#FFD86B"],[200,"#FFB347"],[120,"#FF8A3D"],[62,"#FFF6D8"]].forEach(([r,c]) => { g.beginPath(); g.arc(256,256,r,0,6.284); g.fillStyle=c; g.fill(); g.lineWidth=7; g.strokeStyle="#262A3B"; g.stroke(); });
const tex = new THREE.CanvasTexture(tc); tex.colorSpace = THREE.SRGBColorSpace;
const dir = (ph) => new THREE.Vector3(-Math.cos(ph), 0, Math.sin(ph));
for (const ph of [phiStart, phiStart + phiLen]) {
  const m = new THREE.Mesh(new THREE.CircleGeometry(R*1.02, 64, -Math.PI/2, Math.PI), new THREE.MeshBasicMaterial({map:tex, side:THREE.DoubleSide}));
  m.rotation.y = Math.PI + ph; shell.add(m);
}
// seeded random walk on the first cut face, outward drift so it escapes
const rnd = T3.seeded(11), pts = []; let x = 0, y = 0;
while (pts.length < 420 && Math.hypot(x, y) < R*0.97) { pts.push([x, y]); const a = rnd()*6.283; x += 0.13*Math.cos(a) + 0.006*Math.sign(x||1); y += 0.13*Math.sin(a) + 0.004*Math.sign(y||1); }
pts.push([x, y]);
const dA = dir(phiStart + phiLen), off = dir(phiStart + phiLen + 0.25*Math.PI).multiplyScalar(0.03);
const pos = new Float32Array(pts.length*3); pts.forEach(([r, h], i) => { const r2 = Math.abs(r); const v = dA.clone().multiplyScalar(r2).add(new THREE.Vector3(0, h, 0)).add(off); pos.set([v.x, v.y, v.z], i*3); });
const cp = new THREE.CurvePath(); for (let i=1;i<pts.length;i++) cp.add(new THREE.LineCurve3(new THREE.Vector3(pos[i*3-3],pos[i*3-2],pos[i*3-1]), new THREE.Vector3(pos[i*3],pos[i*3+1],pos[i*3+2])));
const SEG = pts.length*3, RAD = 5; const lg = new THREE.TubeGeometry(cp, SEG, 0.03, RAD, false);
const walk = new THREE.Mesh(lg, new THREE.MeshBasicMaterial({color:0xE0483C})); shell.add(walk); lg.setDrawRange(0, 0);
const dot = new THREE.Mesh(new THREE.SphereGeometry(0.07, 16, 12), new THREE.MeshBasicMaterial({color:0xFFFFFF})); shell.add(dot); dot.visible = false;
const camDir = dir(phiM);
drive(@d, t => {
  const k = Math.min(1, t/1.2), e = k*k*(3-2*k);
  S.cam.position.copy(camDir.clone().multiplyScalar(12.5 - 2.6*e)).add(new THREE.Vector3(0, 3.4 - 0.8*e, 0)); S.cam.lookAt(0, -0.1, 0);
  shell.rotation.y = 0.18*Math.sin(t*0.6);
  const w = Math.min(1, Math.max(0, (t - @tw)/@wd)), n = Math.max(1, Math.floor(w*pts.length));
  lg.setDrawRange(0, t < @tw ? 0 : Math.floor(w*SEG)*RAD*6); dot.visible = t >= @tw; const p = pts[Math.min(n, pts.length) - 1];
  dot.position.copy(dA.clone().multiplyScalar(Math.abs(p[0])).add(new THREE.Vector3(0, p[1], 0)).add(off));
  S.render();
});
pop("#ins-core .chip", @tcore, {from:{rotation:8}, to:{rotation:3}}); tl.set("#ins-core", {opacity:1}, @tcore);
tl.set("#ins-pin", {opacity:1}, @tpin); pop("#ins-pin .pill", @tpin, {from:{rotation:-12}, to:{rotation:-5}});
""", d=d, tw=tpin - 0.2, wd=round(d - tpin - 0.2, 3), tcore=tcore - 0.1, tpin=tpin + 0.3))

# 9 ANCIENT — timeline, mammoth, pyramids near "today"
s = "ancient"; t40 = aw(s, "forty thousand"); tback = aw(s, "back then"); tmam = aw(s, "woolly mammoths"); tnasa = aw(s, "NASA")
mam = ("M70,170 C58,110 92,60 150,55 C200,50 240,68 256,100 C276,112 286,136 281,162 "
       "C278,186 287,205 301,210 C309,212 313,204 307,198 "
       "M262,150 C280,176 300,174 313,160 M234,104 C219,116 221,141 240,146 "
       "M70,170 C100,186 220,186 256,166 M90,178 L90,226 M120,182 L120,226 M205,182 L205,226 M236,175 L236,226 "
       "M68,140 C55,150 52,165 57,173 M110,70 L104,57 M140,60 L136,46 M172,57 L172,44 M252,121 L254,124")
scenes[s] = scene_file(s, f"""
#an-title {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#an-n {{ font-size:120px; color:{C['red']}; }}
#an-svg {{ position:absolute; left:0; top:300px; }}
#an-l1 {{ position:absolute; left:70px; top:640px; font-size:42px; }}
#an-l2 {{ position:absolute; left:905px; top:640px; font-size:42px; }}
#an-l3 {{ position:absolute; left:828px; top:466px; font-size:30px; color:{C['muted']}; }}
#an-src {{ position:absolute; right:90px; top:300px; font-size:34px; color:{C['muted']}; }}
""", f"""
  <div id="an-title"><span id="an-n" class="big">0</span><span style="font-size:60px"> years</span></div>
  <div id="an-src">NASA estimate · others say longer</div>
  <svg id="an-svg" width="{W}" height="380" viewBox="0 0 {W} 380" data-layout-ignore>
    <path id="an-line" d="M100,300 Q540,290 980,300" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="an-tick1" d="M100,280 L100,320 M980,280 L980,320 M880,285 L880,315" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
    <g transform="translate(70,40) scale(0.95)">{"".join(f'<path class="an-mam" d="M{seg.strip()}" {WS}/>' for seg in mam.split("M") if seg.strip())}</g>
    <path id="an-pyr" d="M840,270 L880,215 L920,270 Z" {WS}/>
    <circle id="an-ph" cx="0" cy="0" r="16" fill="{C['hi']}" stroke="{K}" stroke-width="5" opacity="0"/>
  </svg>
  <div id="an-l1">40,000 years ago</div>
  <div id="an-l2">today</div>
  <div id="an-l3">pyramids</div>
""", J("""
rise("#an-src", @tn);
rise("#an-title", @t40); count("#an-n", 0, 40000, @t40, 1.0, v => "≈ " + fmtInt(Math.round(v/1000)*1000));
ink("#an-line", @tline, 0.8); ink("#an-tick1", @tline2, 0.3); rise("#an-l1", @tline2); rise("#an-l2", @tline2);
ink(".an-mam", @tmam, 0.5, {stagger:0.08}); ink("#an-pyr", @tpyr, 0.5); rise("#an-l3", @tpyr);
tl.set("#an-ph", {opacity:1}, @tline2);
along("#an-ph", "#an-line", @tline2, @trun, {ease:"none"});
""", tn=tnasa, t40=t40 - 0.2, tline=t40 + 0.3, tline2=t40 + 1.0, tmam=tmam - 0.3, tpyr=tmam + 1.1, trun=round(SC[s]["slot"] - (t40 + 1.0) - 0.4, 3)))

# 10 OUTRO — recap chips (Max centre stage, keep y < 620)
s = "outro"; t8 = aw(s, "eight minutes"); tanc = aw(s, "ancient"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:170px; text-align:center; }}
#ou-b {{ position:absolute; left:0; right:0; top:285px; text-align:center; }}
#ou-sc {{ top:440px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:52px">light: 8 min</span></div>
  <div id="ou-b"><span class="chip" style="font-size:52px;background:#FFC9C2">energy: ≈ 40,000 yrs</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a .chip", @t8, {from:{rotation:-10}, to:{rotation:-3}}); pop("#ou-b .chip", @tanc, {from:{rotation:10}, to:{rotation:3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", t8=t8, tanc=tanc, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "how old"), SC["guess"]["start"] + 0.2)
point(g("guess", "brand new"), 2.6)
wave(g("intro", "I'm Max"))
point(g("distance", "ninety three"), 1.4)
wow(g("speed", "seven laps"), 1.4)
point(g("trip", "five hundred"), 1.2)
point(g("past", "eight minutes"), 1.2)
think(SC["inside"]["start"] + 0.05, g("inside", "core"))
wow(g("ancient", "forty thousand"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "sunshine"), 0.4), ("pop.mp3", A("guess", "brand new"), 0.5), ("pop.mp3", A("guess", "a few"), 0.5),
        ("pop.mp3", A("guess", "older than"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("riser.mp3", A("distance", "the sun") - 0.2, 0.25),
        ("click-soft.mp3", A("distance", "million"), 0.6), ("whoosh-short.mp3", A("speed", "seven laps"), 0.35),
        ("ping.mp3", A("speed", "one tick"), 0.4), ("impact-bass-1.mp3", A("trip", "five hundred") + 0.3, 0.45),
        ("click.mp3", A("past", "right now") + 0.25, 0.45), ("pop.mp3", A("past", "eight minutes"), 0.5),
        ("click-soft.mp3", A("inside", "bounced") + 0.3, 0.5), ("impact-bass-2.mp3", A("ancient", "forty thousand") + 0.8, 0.45),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
