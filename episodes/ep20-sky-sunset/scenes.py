# MAX WISE ep20 — Why is the sky blue, but sunsets orange-red?
# Kit: ink/morph/along (DrawSVG, MorphSVG, MotionPath) + one three.js scene (sunset geometry).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling)"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src

# 1 HOOK — one sky card: the sun slides down its arc and the sky turns from blue to orange
s = "hook"; tblue = aw(s, "bright blue"); tsun = aw(s, "sunset"); twhy = aw(s, "so why"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-sky {{ position:absolute; left:140px; top:150px; width:800px; height:560px; background:#9ED3F5; border:6px solid {K}; {SKETCH} overflow:hidden; }}
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-q {{ top:760px; font-size:82px; }}
""", f"""
  <div id="hk-sky"><svg id="hk-svg" width="800" height="560" viewBox="0 0 800 560" data-layout-ignore>
    <path id="hk-arc" d="M170,130 Q470,40 640,470" fill="none" stroke="none"/>
    <g id="hk-sun" transform="translate(170,130)"><circle id="hk-sunc" r="62" fill="#FFD84A" stroke="{K}" stroke-width="6"/>
      <path d="M-34,-6 Q-26,-14 -18,-6 M18,-6 Q26,-14 34,-6 M-20,18 Q0,34 20,18" {WS}/></g>
    <path id="hk-hill" d="M-10,470 Q150,400 330,455 T700,440 L810,450 L810,570 L-10,570 Z" fill="#8CC67A" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
  </svg></div>
  <div id="hk-q" class="h1">Why <span class="blue">blue</span>, then <span class="red">red</span>?</div>
""", J("""
pop("#hk-sky", 0.05, {from:{rotation:-4}, to:{rotation:-1}});
tl.fromTo("#hk-sun", {scale:0.7}, {scale:1, duration:0.4, ease:"back.out(2)"}, @tb);
along("#hk-sun", "#hk-arc", @tmove, 1.4, {ease:"power1.inOut"});
tl.to("#hk-sky", {backgroundColor:"#F7A063", duration:1.2, ease:"power1.inOut"}, @tmove);
tl.to("#hk-sunc", {attr:{fill:"#F0563E"}, duration:1.2}, @tmove);
tl.to("#hk-hill", {attr:{fill:"#5E7F55"}, duration:1.2}, @tmove);
rise("#hk-q", @twhy);
""", tb=tblue, tmove=tsun - 0.8, twhy=twhy))

# 2 GUESS — three sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "dust"); t2 = aw(s, "the sun"); t3 = aw(s, "or the air")
notes = [("a", "dust?", -6, 110, C['hi']), ("b", "the Sun cooling down?", 4, 405, "#BFE3F7"), ("c", "the air itself?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;font-family:Gochi Hand,cursive;font-size:58px;line-height:1.05;padding:56px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1, t2=t2, t3=t3))

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tsb = aw(s, "split")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="300" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="in-b1" d="M180,230 L540,230" stroke="#F2C21B" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path id="in-b2" d="M540,230 L900,190" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path id="in-b3" d="M540,230 L900,230" stroke="#3FA34D" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path id="in-b4" d="M540,230 L900,270" stroke="{C['blue']}" stroke-width="10" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's split a sunbeam!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tsb); ink("#in-b1", @tsb, 0.4); ink("#in-b2,#in-b3,#in-b4", @tb, 0.4, {stagger:0.08});
""", tmw=tmw, tu=tmw + 0.3, tsb=tsb - 0.4, tb=tsb + 0.05))

# 4 WHITE — a prism splits the white beam; each colour ray draws on its own word
s = "white"; tlook = aw(s, "looks white"); tmix = aw(s, "every color")
cols = [("red", C['red']), ("orange", "#F28C28"), ("yellow", "#F2C21B"), ("green", "#3FA34D"), ("blue", C['blue']), ("violet", "#8A4FC8")]
ys = [190, 260, 330, 400, 470, 540]
rays = "".join(f'<path id="wh-r{i}" d="M560,330 L880,{y}" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/>' for i, ((n, c), y) in enumerate(zip(cols, ys)))
labs = "".join(f'<div id="wh-l{i}" class="abs" style="left:{40+895}px;top:{240+y-30}px;font-size:44px;color:{c}">{n}</div>' for i, ((n, c), y) in enumerate(zip(cols, ys)))
tcols = [aw(s, n) for n, _ in cols]
scenes[s] = scene_file(s, f"""
#wh-title {{ top:150px; font-size:72px; }}
#wh-svg {{ position:absolute; left:40px; top:240px; }}
#wh-wl {{ position:absolute; left:80px; top:500px; font-size:44px; }}
""", f"""
  <div id="wh-title" class="h1">White light = <span class="hl">every color</span></div>
  <svg id="wh-svg" width="1000" height="620" viewBox="0 0 1000 620" data-layout-ignore>
    <path id="wh-bo" d="M20,330 L480,330" stroke="{K}" stroke-width="26" fill="none" stroke-linecap="round"/>
    <path id="wh-bi" d="M20,330 L480,330" stroke="#FFFBEA" stroke-width="15" fill="none" stroke-linecap="round"/>
    {rays}
    <path id="wh-pr" d="M520,120 L680,450 L360,450 Z" fill="#E6F3FB" fill-opacity=".85" {WS.replace('fill="none" ', '')}/>
  </svg>
  <div id="wh-wl">white light</div>
  {labs}
""", J("""
rise("#wh-title", @tt);
ink("#wh-pr", 0.1, 0.6); tl.set("#wh-pr", {fillOpacity:0.85}, 0);
ink("#wh-bo,#wh-bi", @tlook, 0.5); rise("#wh-wl", @tlook);
""", tt=tmix - 0.3, tlook=tlook - 0.1) + "".join(f'ink("#wh-r{i}", {t - 0.05:.3f}, 0.35); rise("#wh-l{i}", {t:.3f}, 0.25);\n' for i, t in enumerate(tcols)))

# 5 SCATTER — molecules pop in; a white ray hits one and bounces off in every direction (seeded)
s = "scatter"; ttiny = aw(s, "tiny"); tn = aw(s, "nitrogen"); to = aw(s, "oxygen"); thit = aw(s, "hits them"); tbo = aw(s, "bounces")
rnd = random.Random(20); mols = []
while len(mols) < 13:
    x, y = rnd.uniform(130, 950), rnd.uniform(90, 600)
    if math.hypot(x - 540, y - 360) < 120: continue
    if all(math.hypot(x - a, y - b) > 120 for a, b, _, _ in mols): mols.append((x, y, rnd.uniform(0, 180), rnd.random() < 0.78))
def mol(x, y, a, nit, mid=""):
    c = "#7DB6E8" if nit else "#F28B82"
    return (f'<g class="sc-m" {mid} transform="translate({x:.0f},{y:.0f}) rotate({a:.0f})"><circle cx="-17" cy="0" r="22" fill="{c}" stroke="{K}" stroke-width="5"/>'
            f'<circle cx="17" cy="0" r="22" fill="{c}" stroke="{K}" stroke-width="5"/></g>')
mh = "".join(mol(*m) for m in mols) + mol(540, 360, 20, True, 'id="sc-hero"')
burst = "".join(f'<path class="sc-b" d="M{540+48*math.cos(a):.0f},{360+48*math.sin(a):.0f} L{540+150*math.cos(a):.0f},{360+150*math.sin(a):.0f}" stroke="#E5A800" stroke-width="9" fill="none" stroke-linecap="round" stroke-dasharray="20 12"/>' for a in [i * math.pi / 5 + 0.2 for i in range(10)])
scenes[s] = scene_file(s, f"""
#sc-svg {{ position:absolute; left:0; top:170px; }}
#sc-n {{ position:absolute; left:120px; top:150px; }}
#sc-o {{ position:absolute; left:640px; top:150px; }}
#sc-pop {{ position:absolute; left:700px; top:300px; font-family:'Gochi Hand',cursive; font-size:96px; color:{C['red']}; transform:rotate(-8deg); }}
.sc-m {{ transform-box:fill-box; }}
""", f"""
  <svg id="sc-svg" width="{W}" height="720" viewBox="0 0 {W} 720" data-layout-ignore>
    {mh}
    <path id="sc-ray" d="M0,360 L488,360" stroke="#E5A800" stroke-width="12" fill="none" stroke-linecap="round"/>
    {burst}
  </svg>
  <div id="sc-n"><span class="chip" style="background:#BFE3F7">nitrogen</span></div>
  <div id="sc-o"><span class="chip" style="background:#FFC9C2">oxygen</span></div>
  <div id="sc-pop">boing!</div>
""", J("""
tl.fromTo(".sc-m", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2.2)", stagger:0.04}, @tt);
pop("#sc-n .chip", @tn, {from:{rotation:-10}, to:{rotation:-3}}); pop("#sc-o .chip", @to, {from:{rotation:10}, to:{rotation:3}});
ink("#sc-ray", @thit, 0.5);
tl.fromTo("#sc-hero", {rotation:20}, {rotation:60, duration:0.4, ease:"back.out(3)", svgOrigin:"540 360"}, @tbo);
ink(".sc-b", @tbo, 0.35, {stagger:0.03});
pop("#sc-pop", @tbo2, {from:{rotation:-20}, to:{rotation:-8}});
""", tt=ttiny - 0.1, tn=tn, to=to, thit=thit - 0.4, tbo=tbo, tbo2=tbo + 0.3))

# 6 FOUR — countable bounces: blue gets knocked off four times, red once
s = "four"; tsame = aw(s, "the same"); tbl = aw(s, "blue light"); t4 = aw(s, "four times"); tred = aw(s, "than red")
def kicks(y, n, color, cls):
    out = ""
    for i in range(n):
        x = 300 + i * 150; a = -1 if i % 2 == 0 else 1
        out += f'<path class="{cls}" d="M{x},{y} L{x+50},{y+a*120}" stroke="{color}" stroke-width="9" fill="none" stroke-linecap="round" stroke-dasharray="16 10"/>'
    return out
scenes[s] = scene_file(s, f"""
#fo-title {{ top:150px; font-size:74px; }}
#fo-svg {{ position:absolute; left:0; top:250px; }}
#fo-4 {{ position:absolute; left:860px; top:300px; font-family:'Gochi Hand',cursive; font-size:120px; color:{C['blue']}; }}
#fo-1 {{ position:absolute; left:860px; top:600px; font-family:'Gochi Hand',cursive; font-size:120px; color:{C['red']}; }}
""", f"""
  <div id="fo-title" class="h1">Not <span class="hl">fair!</span></div>
  <svg id="fo-svg" width="{W}" height="640" viewBox="0 0 {W} 640" data-layout-ignore>
    <path id="fo-bl" d="M90,150 L820,150" stroke="{C['blue']}" stroke-width="14" fill="none" stroke-linecap="round"/>
    {kicks(150, 4, C['blue'], "fo-kb")}
    <path id="fo-rd" d="M90,450 L820,450" stroke="{C['red']}" stroke-width="14" fill="none" stroke-linecap="round"/>
    {kicks(450, 1, C['red'], "fo-kr")}
  </svg>
  <div id="fo-4">4×</div>
  <div id="fo-1">1×</div>
""", J("""
pop("#fo-title", @ts, {from:{rotation:-8}, to:{}});
ink("#fo-bl", @tbl, 0.5); ink("#fo-rd", @tbl2, 0.5);
ink(".fo-kb", @t4, 0.25, {stagger:0.18}); pop("#fo-4", @t4b);
ink(".fo-kr", @tred, 0.3); pop("#fo-1", @tred2);
""", ts=tsame - 0.2, tbl=tbl, tbl2=tbl + 0.3, t4=t4 - 0.3, t4b=t4 + 0.4, tred=tred, tred2=tred + 0.3))

# 7 BLUE — sky dome: blue light reaches the eye from every direction, then the dome glows
s = "blue"; tall = aw(s, "all over"); tev = aw(s, "every direction"); tglow = aw(s, "glows blue")
pts = [(540 + 400 * math.cos(a), 640 - 400 * math.sin(a)) for a in [math.pi * (0.1 + 0.8 * i / 8) for i in range(9)]]
eye = (540, 600)
lines = "".join(f'<path class="bl-ln" d="M{x:.0f},{y:.0f} L{eye[0]},{eye[1]-22}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="14 12"/>' for x, y in pts)
dots = "".join(f'<circle class="bl-d" cx="{x:.0f}" cy="{y:.0f}" r="16" fill="#5E9CE6" stroke="{K}" stroke-width="4"/>' for x, y in pts)
scenes[s] = scene_file(s, f"""
#bl-svg {{ position:absolute; left:0; top:170px; }}
#bl-lab {{ position:absolute; left:0; right:0; top:830px; text-align:center; }}
""", f"""
  <svg id="bl-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <path id="bl-dome" d="M110,640 A430,430 0 0 1 970,640 Z" fill="#9ED3F5" fill-opacity="0" stroke="{K}" stroke-width="6"/>
    {lines}{dots}
    <g id="bl-guy"><circle cx="540" cy="575" r="30" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>
      <circle cx="540" cy="568" r="8" fill="{K}"/><path d="M540,605 L540,640" {WS}/></g>
  </svg>
  <div id="bl-lab"><span class="chip" style="background:#BFE3F7">blue from everywhere</span></div>
""", J("""
ink("#bl-dome", 0.05, 0.7); pop("#bl-guy", 0.3);
tl.fromTo(".bl-d", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, ease:"back.out(2)", stagger:0.06}, @tall);
ink(".bl-ln", @tev, 0.4, {stagger:0.05});
tl.to("#bl-dome", {attr:{"fill-opacity":0.9}, duration:0.8}, @tglow);
pop("#bl-lab .chip", @tglow2, {from:{rotation:-8}, to:{rotation:-2}});
""", tall=tall - 0.3, tev=tev - 0.3, tglow=tglow - 0.5, tglow2=tglow))

# 8 VIOLET — myth crossed out: "violet sky?" struck through
s = "violet"; tv = aw(s, "violet"); tless = aw(s, "less of"); teye = aw(s, "eyes prefer")
scenes[s] = scene_file(s, f"""
#vi-q {{ position:absolute; left:0; right:0; top:160px; text-align:center; font-family:'Gochi Hand',cursive; font-size:100px; color:#8A4FC8; }}
#vi-svg {{ position:absolute; left:0; top:300px; }}
#vi-l1 {{ position:absolute; left:205px; top:820px; font-size:44px; color:#8A4FC8; }}
#vi-l2 {{ position:absolute; left:395px; top:820px; font-size:44px; color:{C['blue']}; }}
#vi-sun {{ position:absolute; left:200px; top:330px; font-size:42px; color:{C['muted']}; }}
#vi-eye {{ position:absolute; left:640px; top:740px; }}
""", f"""
  <div id="vi-q">violet sky?</div>
  <svg id="vi-svg" width="{W}" height="560" viewBox="0 0 {W} 560" data-layout-ignore>
    <path id="vi-x" d="M300,-60 Q540,-110 790,-80" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <rect id="vi-b1" x="210" y="380" width="120" height="120" fill="#B48CE0" stroke="{K}" stroke-width="5"/>
    <rect id="vi-b2" x="400" y="160" width="120" height="340" fill="#5E9CE6" stroke="{K}" stroke-width="5"/>
    <path d="M180,500 L560,500" {WS}/>
    <path id="vi-e" d="M650,330 Q780,230 910,330 Q780,430 650,330 Z" fill="#FFFFFF" {WS.replace('fill="none" ', '')}/>
    <circle id="vi-ei" cx="780" cy="330" r="42" fill="#5E9CE6" stroke="{K}" stroke-width="5"/>
  </svg>
  <div id="vi-sun">in sunlight:</div>
  <div id="vi-l1">violet</div><div id="vi-l2">blue</div>
  <div id="vi-eye"><span class="chip" style="background:#BFE3F7">eyes prefer blue</span></div>
""", J("""
pop("#vi-q", @tv, {from:{rotation:-6}, to:{}});
rise("#vi-sun", @tl0);
tl.fromTo("#vi-b1", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.4, ease:"back.out(1.6)"}, @tl1);
tl.fromTo("#vi-b2", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.5, ease:"back.out(1.6)"}, @tl2);
rise("#vi-l1", @tl1); rise("#vi-l2", @tl2);
ink("#vi-e", @te, 0.45); pop("#vi-ei", @te2, {from:{transformOrigin:"50% 50%"}});
pop("#vi-eye .chip", @teye, {from:{rotation:8}, to:{rotation:3}});
ink("#vi-x", @tx, 0.4);
""", tv=tv - 0.1, tl0=tless - 0.6, tl1=tless - 0.4, tl2=tless, te=teye - 0.5, te2=teye - 0.1, teye=teye + 0.2, tx=teye + 0.6))

# 9 SUNSET — 3D: Earth with a thin air shell; noon ray is short, sunset ray grazes a long way through the air
s = "sunset"; tsun = aw(s, "at sunset"); tlow = aw(s, "low on"); t38 = aw(s, "thirty eight"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#ss-cv {{ position:absolute; left:40px; top:150px; width:1000px; height:700px; }}
#ss-noon {{ position:absolute; opacity:0; }}
#ss-set {{ position:absolute; opacity:0; }}
#ss-lab {{ position:absolute; left:0; right:0; top:830px; text-align:center; }}
#ss-lab .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <canvas id="ss-cv" width="1000" height="700"></canvas>
  <div id="ss-noon"><span class="chip" style="font-size:44px">noon: short</span></div>
  <div id="ss-set"><span class="chip" style="font-size:44px;background:#FFC9C2">sunset: long</span></div>
  <div id="ss-lab"><span class="big">≈ 38× more air</span></div>
""", J("""
const S = T3.stage("#ss-cv", 1000, 700, 30);
const earth = T3.inked(new THREE.SphereGeometry(2, 48, 32), 0x4F9BE0, 0.04); S.scene.add(earth);
const land = new THREE.Mesh(new THREE.SphereGeometry(2.01, 48, 32, 0.2, 1.4, 0.15, 1.0), T3.toon(0x7CC46A)); earth.add(land);
const air = new THREE.Mesh(new THREE.SphereGeometry(2.3, 48, 32), new THREE.MeshBasicMaterial({color:0x9FD4F5, transparent:true, opacity:0.35, depthWrite:false})); S.scene.add(air);
const rim = new THREE.Mesh(new THREE.TorusGeometry(2.3, 0.012, 8, 120), new THREE.MeshBasicMaterial({color:0x262A3B})); S.scene.add(rim);
const guy = T3.inked(new THREE.ConeGeometry(0.09, 0.26, 16), 0xE0483C, 0.03); guy.position.set(0, 2.12, 0.0); S.scene.add(guy);
function ray(color, L, px, py, rotZ) {
  const geo = new THREE.CylinderGeometry(0.05, 0.05, L, 12); geo.translate(0, L/2, 0);
  const pivot = new THREE.Group(); pivot.position.set(px, py, 0); pivot.rotation.z = rotZ;
  const m = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({color})); pivot.add(m); S.scene.add(pivot); pivot.scale.y = 0.0001; return pivot; }
const noon = ray(0xF2C21B, 2.0, 0, 4.25, Math.PI);
const dusk = ray(0xF28C28, 5.4, 5.4, 2.2, Math.PI/2);
const cam = t => { const k = Math.min(1, t/1.5), e = k*k*(3-2*k); S.cam.position.set(1.8 + 0.4*Math.sin(t*0.4), 1.6 + 0.4*e, 14.5 - 1.5*e); S.cam.lookAt(1.6, 1.3, 0); };
cam(@d); S.cam.updateMatrixWorld();
const pr = (x, y, z) => { const q = new THREE.Vector3(x, y, z).project(S.cam); return [40 + (q.x+1)*500, 150 + (1-q.y)*350]; };
const a = pr(0.15, 3.7, 0), b = pr(3.4, 2.2, 0);
gsap.set("#ss-noon", {left: a[0] + 20, top: a[1] - 40}); gsap.set("#ss-set", {left: Math.min(b[0] - 140, 760), top: b[1] - 120});
const sm = t => Math.min(1, Math.max(0, t));
drive(@d, t => { cam(t); earth.rotation.y = 0.15*t;
  noon.scale.y = Math.max(0.0001, sm((t - 0.3)/0.6)); dusk.scale.y = Math.max(0.0001, sm((t - @tdusk)/0.9));
  S.render(); });
tl.set("#ss-noon", {opacity:1}, 0.6); pop("#ss-noon .chip", 0.6, {from:{rotation:-8}, to:{rotation:-2}});
tl.set("#ss-set", {opacity:1}, @tset); pop("#ss-set .chip", @tset, {from:{rotation:8}, to:{rotation:3}});
pop("#ss-lab", @t38);
""", d=d, tdusk=tsun, tset=tlow, t38=t38 - 0.1))

# 10 LOST — one long beam drawn segment by segment, white fading to red; blue dots peel off (seeded)
s = "lost"; tlong = aw(s, "long path"); tsc = aw(s, "scattered away"); tonly = aw(s, "only the")
segcols = ["#FFF3C4", "#FFE7A3", "#FFD27F", "#FDBA62", "#F9A04E", "#F28C28", "#EE7232", "#E8583A", "#E0483C"]
x0, x1, by = 70, 900, 470
sw = (x1 - x0) / len(segcols)
segs = "".join(f'<path class="lo-s" d="M{x0+i*sw:.0f},{by} L{x0+(i+1)*sw:.0f},{by}" stroke="{c}" stroke-width="30" fill="none" stroke-linecap="butt"/>' for i, c in enumerate(segcols))
rnd = random.Random(7)
bdots = []
for i in range(16):
    x = x0 + 40 + i * (x1 - x0 - 120) / 15
    dy = rnd.choice([-1, 1]) * rnd.uniform(140, 260); dx = rnd.uniform(-60, 60)
    bdots.append((x, dx, dy))
dh = "".join(f'<circle class="lo-d" id="lo-d{i}" cx="{x:.0f}" cy="{by}" r="15" fill="#5E9CE6" stroke="{K}" stroke-width="4"/>' for i, (x, dx, dy) in enumerate(bdots))
scenes[s] = scene_file(s, f"""
#lo-title {{ top:150px; font-size:74px; }}
#lo-svg {{ position:absolute; left:0; top:0; }}
#lo-lab {{ position:absolute; left:0; right:0; top:640px; text-align:center; }}
""", f"""
  <div id="lo-title" class="h1">The <span class="hl">long</span> way</div>
  <svg id="lo-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="lo-ol" d="M{x0},{by-19} L{x1},{by-19} M{x0},{by+19} L{x1},{by+19}" stroke="{K}" stroke-width="5" fill="none"/>
    {segs}{dh}
    <g id="lo-eye"><path d="M930,{by} Q975,{by-40} 1020,{by} Q975,{by+40} 930,{by} Z" fill="#FFFFFF" {WS.replace('fill="none" ', '')}/>
      <circle cx="975" cy="{by}" r="14" fill="{C['red']}" stroke="{K}" stroke-width="4"/></g>
  </svg>
  <div id="lo-lab"><span class="chip" style="background:#FFC9C2">only orange + red get through</span></div>
""", J("""
rise("#lo-title", @tt);
tl.fromTo("#lo-ol", {opacity:0}, {opacity:1, duration:0.3}, @tl0);
ink(".lo-s", @tl0, 0.18, {stagger:0.16});
tl.fromTo(".lo-d", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, stagger:0.05}, @tl1);
""", tt=tlong - 0.8, tl0=tlong - 0.4, tl1=tlong + 0.2) + "".join(
    f'tl.to("#lo-d{i}", {{x:{dx:.0f}, y:{dy:.0f}, opacity:0, duration:0.9, ease:"power2.out"}}, {tsc - 0.2 + i*0.07:.3f});\n' for i, (x, dx, dy) in enumerate(bdots)) + J("""
pop("#lo-eye", @te, {from:{transformOrigin:"50% 50%"}});
pop("#lo-lab .chip", @tonly, {from:{rotation:-8}, to:{rotation:-2}});
""", te=tonly - 0.3, tonly=tonly))

# 11 OUTRO — callback to the hook: two mini sky cards (Max centre stage, keep y < 620)
s = "outro"; tday = aw(s, "blue by"); tred = aw(s, "red at"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:150px; top:150px; width:360px; height:220px; background:#9ED3F5; border:5px solid {K}; {SKETCH} }}
#ou-b {{ position:absolute; left:570px; top:150px; width:360px; height:220px; background:#F7A063; border:5px solid {K}; {SKETCH} }}
#ou-a div, #ou-b div {{ position:absolute; left:0; right:0; top:68px; text-align:center; font-family:'Gochi Hand',cursive; font-size:62px; }}
#ou-sc {{ top:430px; font-size:110px; }}
""", f"""
  <div id="ou-a"><div>day</div></div>
  <div id="ou-b"><div>sunset</div></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a", @ta, {from:{rotation:-10}, to:{rotation:-3}}); pop("#ou-b", @tb, {from:{rotation:10}, to:{rotation:3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", ta=tday - 0.2, tb=tred - 0.2, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "so why"), SC["guess"]["start"] + 0.2)
point(g("guess", "dust"), 2.6)
wave(g("intro", "I'm Max"))
point(g("white", "every color"), 1.4)
wow(g("scatter", "bounces"), 1.2)
point(g("four", "four times"), 1.4)
wow(g("blue", "glows blue"), 1.2)
think(g("violet", "violet"), g("violet", "eyes prefer"))
point(g("sunset", "thirty eight"), 1.4)
point(g("lost", "only the"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "bright blue"), 0.4), ("riser.mp3", A("hook", "sunset") - 0.8, 0.25),
        ("pop.mp3", A("guess", "dust"), 0.5), ("pop.mp3", A("guess", "the sun"), 0.5), ("pop.mp3", A("guess", "or the air"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("ping.mp3", A("white", "violet"), 0.35),
        ("pop.mp3", A("scatter", "tiny"), 0.4), ("impact-bass-1.mp3", A("scatter", "bounces"), 0.45),
        ("click.mp3", A("four", "four times") + 0.4, 0.5), ("sparkle.mp3", A("blue", "glows blue"), 0.4),
        ("click.mp3", A("violet", "eyes prefer") + 0.6, 0.45), ("impact-bass-2.mp3", A("sunset", "thirty eight"), 0.45),
        ("whoosh-short.mp3", A("lost", "scattered away"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
