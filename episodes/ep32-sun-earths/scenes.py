# MAX WISE ep32 — How many Earths could fit inside the Sun?
# Sources: NASA Science "Sun: Facts" (1.3 million Earths fill the Sun's volume; >330,000 Earths to match its mass; 99.8 % of solar system mass),
# NASA NSSDC Sun Fact Sheet (radius 695,700 km vs 6,371 km -> 109.2; volume ratio 1,304,000; mass ratio 332,900).
# Maths: 109^2 = 11,881 (almost 12,000); 109^3 = 1,295,029 (about 1.3 million). Door 2 m / 109 = 18 mm ~ a nickel (21 mm).
# Kit: three.js (hook), along (across), ink (intro, volume, door, outro), morph (squish).
# === SCENES ===
import math, random
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SUNC = "#FFC23A"; SUND = "#F29A2E"; EAR = "#4F9BE0"
def circ_d(x, y, r):
    return f"M{x + r:.1f},{y:.1f} A{r:.1f},{r:.1f} 0 1 1 {x - r:.1f},{y:.1f} A{r:.1f},{r:.1f} 0 1 1 {x + r:.1f},{y:.1f}"

SUN_JS = """
function lumpySun(R, seed) {
  const geo = new THREE.SphereGeometry(R, 64, 40);
  const rnd = T3.seeded(seed); const bumps = Array.from({length:10}, () => [rnd()*6.283, rnd()*3.14, 0.004+rnd()*0.008]);
  const p = geo.attributes.position, v = new THREE.Vector3();
  for (let i=0;i<p.count;i++) { v.fromBufferAttribute(p,i); const th=Math.acos(v.y/R), ph=Math.atan2(v.z,v.x); let k=1;
    for (const [a,b,h] of bumps) k += h*Math.cos(3*(ph-a))*Math.sin(2*(th-b)); v.multiplyScalar(k); p.setXYZ(i,v.x,v.y,v.z); }
  geo.computeVertexNormals(); return geo;
}
"""

# 1 HOOK — 3D Sun turning, a tiny Earth beside it, camera pulls back; the "Earth" tag follows the planet
s = "hook"; thm = aw(s, "how many"); tea = aw(s, "Earths"); tin = aw(s, "inside the"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q {{ top:140px; font-size:78px; }}
#hk-cv {{ position:absolute; left:40px; top:330px; width:1000px; height:620px; }}
#hk-e {{ position:absolute; left:0; top:0; {GH} font-size:46px; color:{C['blue']}; opacity:0; white-space:nowrap; }}
""", f"""
  <div id="hk-q" class="h1">How many <span class="hl">Earths</span> could fit <span class="red">inside the Sun</span>?</div>
  <canvas id="hk-cv" width="1000" height="620"></canvas>
  <div id="hk-e">&larr; Earth</div>
""", SUN_JS + J("""
const S = T3.stage("#hk-cv", 1000, 620, 32);
const sun = T3.inked(lumpySun(2, 7), 0xFFC23A, 0.04); sun.position.set(-0.7, 0, 0); S.scene.add(sun);
const rnd = T3.seeded(3);
for (let i=0;i<6;i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.16+rnd()*0.1, 16, 10), T3.toon(0xF29A2E));
  m.position.setFromSphericalCoords(1.93, 0.8+rnd()*1.5, rnd()*6.283); m.scale.set(1,1,0.35); m.lookAt(0,0,0); sun.add(m); }
const earth = T3.inked(new THREE.SphereGeometry(0.09, 24, 16), 0x4F9BE0, 0.12); earth.position.set(2.6, 0.7, 0.4); S.scene.add(earth);
const el = document.getElementById("hk-e"); const v = new THREE.Vector3();
drive(@d, t => {
  const k = Math.min(1, t / @d), e = k*k*(3-2*k);
  S.cam.position.set(0.3, 0.3 + 0.3*e, 6.2 + 3.4*e); S.cam.lookAt(0.3, 0, 0);
  sun.rotation.y = 0.35*t; earth.rotation.y = t; S.render();
  S.cam.updateMatrixWorld(); v.copy(earth.position).project(S.cam);
  el.style.left = (40 + (v.x+1)*500 + 22).toFixed(1) + "px"; el.style.top = (330 + (1-v.y)*310 - 30).toFixed(1) + "px";
});
pop("#hk-q", 0.05, {from:{scale:1.15}, to:{}});
tl.fromTo("#hk-e", {opacity:0}, {opacity:1, duration:0.3}, @te);
tl.fromTo("#hk-q .red", {color:"#262A3B"}, {color:"#E0483C", duration:0.3}, @ti);
""", d=d, te=tea, ti=tin))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "a hundred"); t2 = aw(s, "a thousand"); t3 = aw(s, "a million")
notes = [("a", "100?", -6, 110, C['hi']), ("b", "1,000?", 4, 405, "#BFE3F7"), ("c", "1,000,000?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{70 if len(txt) < 8 else 44}px;line-height:260px;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.1, t2=t2 - 0.1, t3=t3 - 0.1))

# 3 INTRO — logo, a Sun outline inks with rays (keep y < 620: Max is centre stage)
s = "intro"; tmw = aw(s, "Max Wise"); tpk = aw(s, "pack the")
rays = "".join(f'<path class="in-r" d="M{860 + 78 * math.cos(a):.1f},{520 + 78 * math.sin(a):.1f} L{860 + 108 * math.cos(a):.1f},{520 + 108 * math.sin(a):.1f}" {WS} stroke-width="6"/>' for a in [i * math.pi / 4 for i in range(8)])
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; left:60px; right:330px; font-size:64px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="640" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <circle id="in-sf" cx="860" cy="520" r="62" fill="{SUNC}" opacity="0"/>
    <path id="in-so" d="{circ_d(860, 520, 62)}" {WS} stroke-width="6"/>
    {rays}
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's pack the Sun!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tp); ink("#in-so", @tp, 0.5); tl.fromTo("#in-sf", {opacity:0}, {opacity:1, duration:0.3}, @tp2);
ink(".in-r", @tp2, 0.25, {stagger:0.05});
""", tmw=tmw, tu=tmw + 0.3, tp=tpk - 0.3, tp2=tpk + 0.15))

# shared Sun disc for across / slice
CX, CY, R = 600, 560, 300; EP = 2 * R / 109
SUN_DISC = f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="{SUNC}" stroke="{K}" stroke-width="6"/>'

# 4 ACROSS — an Earth rides across the diameter, leaving a row of true-scale dots; counter to 109
s = "across"; tlu = aw(s, "line up"); tmd = aw(s, "middle of"); t109 = aw(s, "one hundred nine")
row = "".join(f'<circle cx="{CX - R + EP / 2 + i * EP:.2f}" cy="{CY}" r="{EP * 0.42:.2f}" fill="{EAR}"/>' for i in range(109))
scenes[s] = scene_file(s, f"""
#ac-t {{ top:140px; font-size:64px; }}
#ac-svg {{ position:absolute; left:0; top:0; }}
#ac-n {{ position:absolute; left:420px; right:40px; top:880px; text-align:center; {GH} font-size:62px; }}
#ac-tag {{ position:absolute; left:660px; top:222px; {GH} font-size:44px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="ac-t" class="h1">Line up Earths <span class="hl">across</span></div>
  <svg id="ac-svg" width="{W}" height="960" data-layout-ignore>
    <defs><clipPath id="ac-cl"><rect id="ac-cr" x="{CX - R}" y="{CY - 10}" width="0" height="20"/></clipPath></defs>
    {SUN_DISC}
    <path id="ac-dia" d="M{CX - R},{CY} L{CX + R},{CY}" stroke="{K}" stroke-width="3" fill="none" stroke-dasharray="10 8"/>
    <g clip-path="url(#ac-cl)">{row}</g>
    <path id="ac-path" d="M{CX - R + 8},{CY - 30} L{CX + R - 8},{CY - 30}" fill="none" stroke="none"/>
    <g id="ac-e" opacity="0"><circle cx="0" cy="0" r="16" fill="{EAR}" stroke="{K}" stroke-width="4"/><path d="M0,16 L0,26" stroke="{K}" stroke-width="3"/></g>
    <path id="ac-br" d="M{CX - R},{CY + 60} Q{CX - R},{CY + 90} {CX - 40},{CY + 90} Q{CX},{CY + 90} {CX},{CY + 120} Q{CX},{CY + 90} {CX + 40},{CY + 90} Q{CX + R},{CY + 90} {CX + R},{CY + 60}" {WS} stroke="{C['red']}"/>
  </svg>
  <div id="ac-tag">1 dot = 1 Earth</div>
  <div id="ac-n">about <span id="ac-c" class="red">0</span> Earths across</div>
""", J("""
rise("#ac-t", 0.0); rise("#ac-n", 0.3);
ink("#ac-dia", @tl, 0.6);
tl.set("#ac-e", {opacity:1}, @tm); along("#ac-e", "#ac-path", @tm, @dd, {ease:"power1.inOut"});
tl.fromTo("#ac-cr", {attr:{width:0}}, {attr:{width:@w}, duration:@dd, ease:"power1.inOut"}, @tm);
count("#ac-c", 0, 109, @tm, @dd, fmtInt);
pop("#ac-tag", @tm2);
ink("#ac-br", @t9, 0.5); pop("#ac-n", @t9, {from:{scale:1.25}, to:{}});
""", tl=tlu - 0.1, tm=tmd - 0.2, dd=max(1.2, t109 + 0.6 - (tmd - 0.2)), w=2 * R, tm2=tmd + 0.4, t9=t109))

# 5 SLICE — the disc fills top to bottom with a true-scale dot pattern (109 across); 109 x 109 = almost 12,000
s = "slice"; tnl = aw(s, "not a"); tfs = aw(s, "flat slice"); tx = aw(s, "times one"); t12 = aw(s, "twelve thousand")
scenes[s] = scene_file(s, f"""
#sl-t {{ top:140px; font-size:64px; }}
#sl-svg {{ position:absolute; left:0; top:0; }}
#sl-eq {{ position:absolute; left:420px; right:30px; top:870px; text-align:center; {GH} font-size:60px; opacity:0; }}
#sl-res {{ position:absolute; left:380px; top:470px; width:440px; text-align:center; opacity:0; }}
#sl-res .chip {{ font-size:58px; background:#FFFFFF; }}
""", f"""
  <div id="sl-t" class="h1">The Sun is <span class="red">not a line</span>!</div>
  <svg id="sl-svg" width="{W}" height="960" data-layout-ignore>
    <defs><pattern id="sl-pat" x="{CX - R}" y="{CY - R}" width="{EP:.3f}" height="{EP:.3f}" patternUnits="userSpaceOnUse">
      <circle cx="{EP / 2:.3f}" cy="{EP / 2:.3f}" r="{EP * 0.3:.3f}" fill="{C['blue']}"/></pattern>
      <clipPath id="sl-cl"><rect id="sl-cr" x="{CX - R}" y="{CY - R}" width="{2 * R}" height="0"/></clipPath></defs>
    {SUN_DISC}
    <circle cx="{CX}" cy="{CY}" r="{R - 3}" fill="url(#sl-pat)" clip-path="url(#sl-cl)"/>
    <path id="sl-row" d="M{CX - R},{CY} L{CX + R},{CY}" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="sl-eq"><span class="red">109</span> &times; <span class="blue">109</span></div>
  <div id="sl-res"><span class="chip">almost 12,000!</span></div>
""", J("""
rise("#sl-t", 0.0); ink("#sl-row", 0.15, 0.5);
tl.fromTo("#sl-cr", {attr:{height:0}}, {attr:{height:@h}, duration:@df, ease:"power1.inOut"}, @tf);
pop("#sl-eq", @tx);
pop("#sl-res", @t12, {from:{scale:1.6, rotation:-10}, to:{rotation:-3}});
""", h=2 * R, tf=tfs - 0.1, df=max(1.0, t12 - tfs - 0.3), tx=tx - 0.4, t12=t12 - 0.15))

# 6 VOLUME — slice ellipses ink top to bottom into a sphere; 109 x 109 x 109; about 1.3 million
s = "volume"; tst = aw(s, "stack those"); ta = aw(s, "One hundred nine"); tb = aw(s, "times one hundred", 1); tc = aw(s, "times one hundred", 2); t13 = aw(s, "one point three")
VX, VY, VR = 600, 610, 270; NS = 9
sl = ""
for k in range(NS):
    y = VY - VR + (k + 0.5) * 2 * VR / NS; rx = VR * math.sqrt(1 - ((y - VY) / VR) ** 2); ry = rx * 0.2
    sl += f'<path class="vo-s" d="M{VX + rx:.1f},{y:.1f} A{rx:.1f},{ry:.1f} 0 1 1 {VX - rx:.1f},{y:.1f} A{rx:.1f},{ry:.1f} 0 1 1 {VX + rx:.1f},{y:.1f}" fill="#BFE3F7" fill-opacity="0.55" stroke="{C["blue"]}" stroke-width="4"/>'
scenes[s] = scene_file(s, f"""
#vo-t {{ top:140px; font-size:62px; }}
#vo-eq {{ position:absolute; left:0; right:0; top:240px; text-align:center; {GH} font-size:62px; }}
#vo-eq span {{ display:inline-block; opacity:0; }}
#vo-svg {{ position:absolute; left:0; top:0; }}
#vo-res {{ position:absolute; left:330px; top:520px; width:540px; text-align:center; opacity:0; }}
#vo-res .big {{ font-size:96px; color:{C['red']}; }}
#vo-res .pill {{ font-size:48px; }}
""", f"""
  <div id="vo-t" class="h1">Stack the slices!</div>
  <div id="vo-eq"><span id="vo-a" class="red">109</span> <span id="vo-b">&times; 109</span> <span id="vo-c">&times; 109</span></div>
  <svg id="vo-svg" width="{W}" height="960" data-layout-ignore>
    <defs><radialGradient id="vo-g" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="{SUND}"/></radialGradient></defs>
    <circle id="vo-ball" cx="{VX}" cy="{VY}" r="{VR}" fill="url(#vo-g)" opacity="0"/>
    {sl}
    <path id="vo-o" d="{circ_d(VX, VY, VR)}" {WS} stroke-width="6"/>
  </svg>
  <div id="vo-res"><div class="big">&asymp; 1.3 million</div><span class="pill">Earths!</span></div>
""", J("""
rise("#vo-t", 0.0);
ink(".vo-s", @ts, 0.3, {stagger:@sg});
ink("#vo-o", @to, 0.7); tl.fromTo("#vo-ball", {opacity:0}, {opacity:1, duration:0.6}, @to);
tl.to(".vo-s", {opacity:0.25, duration:0.5}, @to);
pop("#vo-a", @ta); pop("#vo-b", @tb); pop("#vo-c", @tc);
pop("#vo-res", @t13, {from:{scale:1.6}, to:{}});
tl.fromTo("#vo-ball", {scale:1, transformOrigin:"50% 50%"}, {scale:1.04, duration:0.15, yoyo:true, repeat:1}, @t13);
""", ts=tst - 0.1, sg=0.12, to=tst + 0.1 + NS * 0.12, ta=ta - 0.1, tb=tb - 0.05, tc=tc - 0.05, t13=t13 - 0.15))

# 7 SQUISH — left jar: circles morph into hexagons (no gaps); right jar: round balls with red-hatched gaps
s = "squish"; tsc = aw(s, "small catch"); tsq = aw(s, "squish them"); tng = aw(s, "no gaps"); trb = aw(s, "round balls"); tfw = aw(s, "fewer would")
JW, JH, JT = 400, 470, 300; JA, JB = 90, 590
hs = 34; hw = math.sqrt(3) * hs; ri = hw / 2
cells_c, cells_h = "", ""; n = 0
for row in range(-1, 11):
    for col in range(-1, 8):
        x = col * hw + (hw / 2 if row % 2 else 0); y = row * 1.5 * hs
        if not (-hw < x < JW + hw and -hs < y < JH + hs): continue
        cells_c += f'<path id="sq-c{n}" class="sq-c" d="{circ_d(x, y, ri - 1)}" fill="{EAR}" stroke="{K}" stroke-width="2.5"/>'
        pts = [(x + hs * math.cos(math.radians(a)), y + hs * math.sin(math.radians(a))) for a in (0, 60, 120, 180, 240, 300)]
        pts = [(x + hs * math.cos(math.radians(a)), y + hs * math.sin(math.radians(a))) for a in (30, 90, 150, 210, 270, 330)]
        cells_h += f'<path id="sq-h{n}" d="M{pts[5][0]:.1f},{pts[5][1]:.1f} ' + " ".join(f"L{px:.1f},{py:.1f}" for px, py in pts) + ' Z" fill="none" stroke="none"/>'
        n += 1
NCELL = n
balls = "".join(f'<circle cx="{ri + c * hw:.1f}" cy="{ri + r * hw:.1f}" r="{ri - 1:.1f}" fill="{EAR}" stroke="{K}" stroke-width="2.5"/>' for r in range(int(JH // hw) + 1) for c in range(int(JW // hw)))
scenes[s] = scene_file(s, f"""
#sq-t {{ top:140px; font-size:66px; }}
.sq-jar {{ position:absolute; top:{JT}px; width:{JW}px; height:{JH}px; border:5px solid {K}; {SKETCH} overflow:hidden; background:#FFFFFF; opacity:0; }}
#sq-b {{ background:repeating-linear-gradient(45deg, {C['red']} 0 3px, #FFFFFF 3px 11px); }}
.sq-l {{ position:absolute; top:{JT + JH + 20}px; width:{JW + 40}px; text-align:center; {GH} font-size:50px; opacity:0; }}
#sq-few {{ position:absolute; left:{JB + 30}px; top:{JT + 150}px; width:{JW - 60}px; text-align:center; opacity:0; }}
#sq-few .chip {{ background:#FFFFFF; color:{C['red']}; font-size:60px; }}
""", f"""
  <div id="sq-t" class="h1"><span class="hl">Small catch</span>&hellip;</div>
  <div id="sq-a" class="sq-jar" style="left:{JA}px"><svg width="{JW}" height="{JH}" data-layout-ignore>{cells_c}{cells_h}</svg></div>
  <div id="sq-b" class="sq-jar" style="left:{JB}px"><svg width="{JW}" height="{JH}" data-layout-ignore>{balls}</svg></div>
  <div id="sq-la" class="sq-l" style="left:{JA - 20}px">squished: <span class="blue">no gaps</span></div>
  <div id="sq-lb" class="sq-l" style="left:{JB - 20}px">round: <span class="red">gaps!</span></div>
  <div id="sq-few"><span class="chip">fewer fit</span></div>
""", J("""
rise("#sq-t", @tsc);
pop("#sq-a", @tsq0, {from:{rotation:-8}, to:{rotation:-1.5}});
""" + "".join(f'morph("#sq-c{i}", "#sq-h{i}", @tsq + {(i % 9) * 0.03:.2f}, 0.7, {{ease:"back.out(1.4)"}});' for i in range(NCELL)) + """
pop("#sq-la", @tng);
pop("#sq-b", @trb, {from:{rotation:8}, to:{rotation:1.5}}); pop("#sq-lb", @trb2);
pop("#sq-few", @tfw, {from:{scale:2, rotation:-20}, to:{rotation:-6}});
""", tsc=tsc - 0.1, tsq0=tsq - 0.6, tsq=tsq + 0.1, tng=tng - 0.1, trb=trb - 0.2, trb2=trb + 0.3, tfw=tfw - 0.1))

# 8 DOOR — a front door inks, a Sun as tall as the door, a true-scale Earth dot + magnified nickel callout
s = "door"; tpi = aw(s, "picture it"); tfd = aw(s, "front door"); tea = aw(s, "Earth would"); tni = aw(s, "nickel")
DT, DB = 330, 850; DH = DB - DT; SR = DH / 2; SX = 390 + SR; SY = DT + SR; ER = SR / 109
door = [f"M120,{DB} L120,{DT} L330,{DT} L330,{DB}", f"M145,{DB} L145,{DT + 25} L305,{DT + 25} L305,{DB}", f"M170,{DT + 70} L280,{DT + 70} L280,{DT + 230} L170,{DT + 230} Z", f"M60,{DB} L380,{DB}"]
dh = "".join(f'<path class="dr-d" d="{p}" {WS} stroke-width="6"/>' for p in door)
EX, EY = SX + SR + 50, SY + 120
scenes[s] = scene_file(s, f"""
#dr-t {{ top:140px; font-size:62px; }}
#dr-svg {{ position:absolute; left:0; top:0; }}
#dr-lab {{ position:absolute; left:640px; top:600px; width:420px; text-align:center; {GH} font-size:46px; line-height:1.05; opacity:0; }}
""", f"""
  <div id="dr-t" class="h1">If the Sun were a <span class="hl">front door</span>&hellip;</div>
  <svg id="dr-svg" width="{W}" height="960" data-layout-ignore>
    {dh}
    <circle id="dr-knob" cx="290" cy="{DT + 320}" r="10" fill="{K}" opacity="0"/>
    <circle id="dr-sun" cx="{SX}" cy="{SY}" r="{SR}" fill="{SUNC}" stroke="{K}" stroke-width="6" opacity="0"/>
    <circle id="dr-e" cx="{EX:.0f}" cy="{EY:.0f}" r="{max(ER, 2.4):.1f}" fill="{EAR}" opacity="0"/>
    <path id="dr-ld" d="M{EX:.0f},{EY - 8:.0f} L{EX - 20:.0f},{EY - 120:.0f}" {WS} stroke-width="4"/>
    <g id="dr-mag" opacity="0">
      <circle cx="{EX - 30:.0f}" cy="{EY - 220:.0f}" r="100" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>
      <circle cx="{EX - 30:.0f}" cy="{EY - 220:.0f}" r="80" fill="#C9CCD3" stroke="{K}" stroke-width="4"/>
      <circle cx="{EX - 30:.0f}" cy="{EY - 220:.0f}" r="70" fill="none" stroke="{C['muted']}" stroke-width="2"/>
      <circle id="dr-ee" cx="{EX - 30:.0f}" cy="{EY - 220:.0f}" r="66" fill="{EAR}" stroke="{K}" stroke-width="4" opacity="0"/>
      <path d="M{EX - 70:.0f},{EY - 250:.0f} Q{EX - 40:.0f},{EY - 270:.0f} {EX - 20:.0f},{EY - 240:.0f} Q{EX:.0f},{EY - 210:.0f} {EX - 30:.0f},{EY - 190:.0f}" fill="#7CC46A" stroke="none" id="dr-land" opacity="0"/>
    </g>
  </svg>
  <div id="dr-lab" style="left:{EX - 190:.0f}px;top:{EY - 470:.0f}px;width:320px">Earth &asymp;<br><span class="red">a nickel</span></div>
""", J("""
rise("#dr-t", @tp);
ink(".dr-d", @tf, 0.35, {stagger:0.1}); pop("#dr-knob", @tf2);
pop("#dr-sun", @tf2, {from:{scale:0.3}, to:{}});
pop("#dr-e", @te, {from:{scale:4}, to:{}}); ink("#dr-ld", @te2, 0.3);
pop("#dr-mag", @tn, {from:{scale:0.2}, to:{}});
tl.fromTo("#dr-ee, #dr-land", {opacity:0}, {opacity:1, duration:0.3}, @tn2);
pop("#dr-lab", @tn2);
""", tp=tpi - 0.1, tf=tfd - 0.6, tf2=tfd + 0.2, te=tea - 0.1, te2=tea + 0.2, tn=tni - 0.5, tn2=tni + 0.1))

# 9 MASS — balance: Sun vs a pile of Earths, levels at 330,000; then the solar-system mass bar is almost all Sun
s = "mass"; ttw = aw(s, "the twist"); thg = aw(s, "hot gas"); t33 = aw(s, "three hundred thirty"); tsl = aw(s, "Still"); tal = aw(s, "almost all")
rnd = random.Random(32); pile = ""
for i in range(40):
    while True:
        px, py = rnd.uniform(-110, 110), rnd.uniform(-130, 0)
        if py > -130 + abs(px) * 0.9: break
    pile += f'<circle class="ms-e" cx="{px:.0f}" cy="{py - 14:.0f}" r="13" fill="{EAR}" stroke="{K}" stroke-width="3" opacity="0"/>'
scenes[s] = scene_file(s, f"""
#ms-t {{ top:140px; font-size:66px; }}
#ms-svg {{ position:absolute; left:0; top:0; }}
#ms-n {{ position:absolute; left:560px; top:590px; width:500px; text-align:center; {GH} font-size:56px; opacity:0; }}
#ms-bar {{ position:absolute; left:80px; top:420px; width:920px; opacity:0; }}
#ms-bx {{ position:relative; height:150px; border:5px solid {K}; {SKETCH} overflow:hidden; background:{C['red']}; }}
#ms-fill {{ position:absolute; left:0; top:0; bottom:0; width:97%; background:{SUNC}; transform-origin:0 50%; }}
#ms-bx b {{ position:absolute; left:40px; top:30px; {GH} font-size:70px; font-weight:normal; }}
#ms-cap {{ margin-top:22px; text-align:center; {GH} font-size:52px; }}
#ms-oth {{ position:absolute; right:-10px; top:-80px; {GH} font-size:40px; color:{C['red']}; }}
""", f"""
  <div id="ms-t" class="h1">Here's the <span class="hl">twist</span>!</div>
  <svg id="ms-svg" width="{W}" height="960" data-layout-ignore>
    <g id="ms-scale">
      <path d="M600,840 L560,900 L640,900 Z" fill="#FFFFFF" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <g id="ms-beam">
        <path d="M300,840 L900,840" {WS} stroke-width="8"/>
        <g transform="translate(330,826)"><circle cx="0" cy="-100" r="100" fill="{SUNC}" stroke="{K}" stroke-width="5"/>
          <text x="0" y="-85" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{K}">Sun</text></g>
        <g id="ms-pile" transform="translate(810,826)">{pile}</g>
      </g>
    </g>
  </svg>
  <div id="ms-n">&asymp; <span class="red">330,000</span> Earths</div>
  <div id="ms-bar"><div id="ms-bx"><div id="ms-fill"></div><b>Sun</b><div id="ms-oth"></div></div>
    <div id="ms-cap">almost <span class="hl">all the mass</span> in our solar system</div></div>
""", J("""
rise("#ms-t", @tt);
tl.fromTo("#ms-beam", {rotation:-14, svgOrigin:"600 840"}, {rotation:-14, svgOrigin:"600 840", duration:0.01}, 0);
tl.fromTo("#ms-scale", {opacity:0, y:40}, {opacity:1, y:0, duration:0.4, ease:"back.out(1.6)"}, @tt2);
tl.fromTo(".ms-e", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, stagger:@sg, ease:"back.out(3)"}, @tg);
tl.to("#ms-beam", {rotation:0, svgOrigin:"600 840", duration:0.8, ease:"elastic.out(1,0.5)"}, @t33);
pop("#ms-n", @t33);
tl.to("#ms-scale, #ms-n", {opacity:0, y:-30, duration:0.3, ease:"power2.in"}, @ts);
tl.fromTo("#ms-bar", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35}, @ts2);
tl.fromTo("#ms-fill", {scaleX:0}, {scaleX:1, duration:0.9, ease:"power2.out"}, @ta);
""", tt=ttw - 0.1, tt2=ttw + 0.3, tg=thg, sg=max(0.02, (t33 - thg - 0.3) / 40), t33=t33, ts=tsl - 0.4, ts2=tsl - 0.05, ta=tal - 0.2))

# 10 OUTRO — callback: the "1,000,000?" note gets a red check; recap chip; Stay curious (Max centre: keep y < 620)
s = "outro"; t13 = aw(s, "one point three"); tfi = aw(s, "could fit"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-n {{ position:absolute; left:110px; top:170px; width:300px; height:240px; background:#FFC9C2; border:4px solid {K}; {SKETCH} transform:rotate(-4deg); text-align:center; {GH} font-size:54px; line-height:240px; opacity:0; }}
#ou-r {{ position:absolute; left:450px; top:200px; width:560px; text-align:center; opacity:0; }}
#ou-r .big {{ font-size:96px; color:{C['red']}; }}
#ou-r .pill {{ font-size:46px; margin-top:10px; }}
#ou-c {{ position:absolute; left:0; right:0; top:260px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-n">1,000,000?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="640" data-layout-ignore>
    <path id="ou-ck" d="M150,380 L215,450 L360,300" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <div id="ou-r"><div class="big">&asymp; 1.3 million</div><span class="pill">Earths inside the Sun</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-n", 0.1, {from:{rotation:-20}, to:{rotation:-4}});
pop("#ou-r", @t13, {from:{scale:1.4}, to:{}}); ink("#ou-ck", @tf, 0.45);
tl.to("#ou-n, #ou-r, #ou-ck", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
pop("#ou-c", @tsc);
""", t13=t13 - 0.1, tf=tfi, tx=tsc - 0.3, tsc=tsc))

# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "a hundred"), 2.2)
wave(g("intro", "I'm Max"))
point(g("across", "one hundred nine"), 1.2)
think(g("slice", "not a"), g("slice", "flat slice"))
point(g("slice", "twelve thousand"), 1.2)
wow(g("volume", "one point three"), 1.6)
think(g("squish", "small catch"), g("squish", "squish them"))
point(g("squish", "fewer would"), 1.0)
point(g("door", "nickel"), 1.2)
wow(g("mass", "three hundred thirty"), 1.2)
point(g("mass", "almost all"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "inside the"), 0.35),
        ("pop.mp3", A("guess", "a hundred"), 0.5), ("pop.mp3", A("guess", "a thousand"), 0.5), ("pop.mp3", A("guess", "a million"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("across", "middle of"), 0.5),
        ("ping.mp3", A("across", "one hundred nine"), 0.4), ("pop.mp3", A("slice", "twelve thousand"), 0.5),
        ("riser.mp3", A("volume", "stack those"), 0.3), ("impact-bass-1.mp3", A("volume", "one point three"), 0.45),
        ("pop.mp3", A("squish", "fewer would"), 0.5), ("pop.mp3", A("door", "nickel"), 0.5),
        ("impact-bass-2.mp3", A("mass", "three hundred thirty"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
