# MAX WISE ep48 — Is a bolt of lightning hotter than the Sun?
# Kit: ink / along helpers + one three.js scene (the Sun).
# Sources: NWS "Lightning temperature" (air heated to ~50,000 °F, 5x the Sun's surface), NWS Melbourne "What is lightning"
# (whole flash usually < half a second), NWS "How thunder is created" (rapid expansion/contraction = thunder; ~5 s per mile).
# Calc: 50000 / 10000 = 5; 15 s / 5 = 3 miles.
# === SCENES ===
import math as _m
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SUN = "#FFD54A"; SUN2 = "#F5A623"; BOLT = "#FFE14D"; SKY = "#BFE3F7"; CLOUD = "#D9DDE3"
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
BOLTP = "M20,-170 L-55,10 L5,10 L-35,170 L70,-30 L10,-30 L55,-170 Z"
def bolt(cls, x, y, s, idn=""):
    i = f' id="{idn}"' if idn else ""
    return f'<g{i} transform="translate({x},{y}) scale({s})"><path class="{cls}" d="{BOLTP}" fill="{BOLT}" stroke="{K}" stroke-width="{6/s:.2f}" stroke-linejoin="round"/></g>'
CLOUDP = "M-150,40 C-200,40 -200,-30 -140,-30 C-140,-90 -60,-100 -30,-60 C0,-110 90,-100 90,-40 C150,-50 170,40 110,40 Z"
def cloud(cls, x, y, s):
    return f'<g transform="translate({x},{y}) scale({s})"><path class="{cls}" d="{CLOUDP}" fill="{CLOUD}" stroke="{K}" stroke-width="{6/s:.2f}" stroke-linejoin="round"/></g>'
def sun2d(cls, x, y, r):
    ry = "".join(f'<path class="{cls}" d="M{x+(r+10)*_m.cos(k*_m.pi/6):.0f},{y+(r+10)*_m.sin(k*_m.pi/6):.0f} L{x+(r+30)*_m.cos(k*_m.pi/6):.0f},{y+(r+30)*_m.sin(k*_m.pi/6):.0f}" stroke="{SUN2}" stroke-width="7" stroke-linecap="round"/>' for k in range(12))
    return f'{ry}<path class="{cls}" d="M{x+r},{y} A{r},{r} 0 1 0 {x-r},{y} A{r},{r} 0 1 0 {x+r-0.1:.1f},{y-0.5}" fill="{SUN}" stroke="{K}" stroke-width="6"/>'

# thermometer on the right edge (the ruler that never leaves): 0 at y=860, 50,000 at y=280
TX, TY0, TY1 = 945, 860, 280
def ty(v): return TY0 - (TY0 - TY1) * v / 50000
def therm(p, lab10=True):
    ticks = "".join(f'<path d="M{TX-34},{ty(v):.0f} L{TX-22},{ty(v):.0f}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for v in range(0, 50001, 10000))
    return (f'<rect x="{TX-20}" y="{TY1-30}" width="40" height="{TY0-TY1+60}" rx="20" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>'
            f'<rect id="{p}-fill" x="{TX-11}" y="{TY1}" width="22" height="{TY0-TY1+40}" fill="{C["red"]}"/>'
            f'<circle cx="{TX}" cy="{TY0+45}" r="38" fill="{C["red"]}" stroke="{K}" stroke-width="6"/>{ticks}')

# 1 HOOK — storm cloud and bolt ink themselves, sun on the other side
s = "hook"; tst = aw(s, "stormy"); tbo = aw(s, "bolt of lightning"); tsu = aw(s, "the sun")
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:76px; }}
#hk-vs {{ position:absolute; left:470px; top:560px; {GH} font-size:90px; opacity:0; }}
#hk-qm {{ position:absolute; left:490px; top:330px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-q" class="h1" style="opacity:0">Is <span class="hl">lightning</span> hotter than the <span class="hl">Sun</span>?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {cloud("hk-c", 260, 430, 1.1)}
    {bolt("hk-b", 250, 640, 0.95)}
    {sun2d("hk-s", 820, 600, 120)}
  </svg>
  <div id="hk-vs">vs</div>
  <div id="hk-qm">?</div>
""", J("""
ink(".hk-c", @tc, 0.6); rise("#hk-q", @tq);
ink(".hk-b", @tb, 0.5); tl.fromTo("#hk-b", {opacity:1}, {opacity:0.2, duration:0.06, yoyo:true, repeat:3}, @tb2);
ink(".hk-s", @ts, 0.7, {stagger:0.02}); pop("#hk-vs", @ts);
pop("#hk-qm", @tqm, {from:{rotation:-25, scale:2}, to:{rotation:-6}});
""", tc=max(0.05, tst - 0.2), tq=tbo - 0.6, tb=tbo - 0.1, tb2=tbo + 0.45, ts=tsu - 0.3, tqm=tsu + 0.4))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "cooler"); t2 = aw(s, "about the same"); t3 = aw(s, "way hotter")
notes = [("a", "cooler", -6, 110, C['hi']), ("b", "same", 4, 405, SKY), ("c", "WAY hotter", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:280px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:74px;line-height:1.05;padding-top:80px;opacity:0">{txt}?</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  <div class="h2" style="top:690px">lightning vs the Sun</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.1))

# 3 INTRO — logo + small thermometer inks (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tth = aw(s, "giant thermometer")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-t" d="M520,600 L520,500 A20,20 0 0 1 560,500 L560,600" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path class="in-t" d="M540,560 L540,605" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Grab a thermometer!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tth); ink(".in-t", @tt, 0.5, {stagger:0.2});
""", tmw=tmw, tu=tmw + 0.3, tth=tth - 0.3, tt=tth))

# 4 SUN — 3D sun (one three.js scene) + thermometer rises to 10,000 °F
s = "sun"; tfs = aw(s, "first the sun"); tsf = aw(s, "glowing surface"); t10 = aw(s, "ten thousand degrees"); tfm = aw(s, "first mark"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#sn-title {{ top:150px; font-size:72px; }}
#sn-cv {{ position:absolute; left:10px; top:260px; width:760px; height:560px; }}
#sn-lab {{ position:absolute; left:480px; top:840px; width:400px; text-align:right; opacity:0; }}
#sn-lab .big {{ font-size:72px; color:{C['red']}; }}
""", f"""
  <div id="sn-title" class="h1">The <span class="hl">Sun's</span> surface</div>
  <canvas id="sn-cv" width="760" height="560"></canvas>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>{therm("sn")}
    <path id="sn-ar" d="M{TX-40},{ty(10000):.0f} Q{TX-90},{ty(10000)+20:.0f} {TX-110},{ty(10000)+95:.0f}" stroke="{K}" stroke-width="5" stroke-linecap="round"/></svg>
  <div id="sn-lab"><span class="big">10,000°F</span></div>
""", J("""
const S = T3.stage("#sn-cv", 760, 560, 34);
const sun = T3.inked(new THREE.SphereGeometry(1.3, 48, 32), 0xFFD54A, 0.05); S.scene.add(sun);
const rnd = T3.seeded(7);
for (let i=0;i<26;i++) { const sp = new THREE.Mesh(new THREE.SphereGeometry(0.08+rnd()*0.1, 10, 8), T3.toon(0xF5A623));
  const th = rnd()*Math.PI*2, ph = Math.acos(2*rnd()-1); sp.position.set(1.27*Math.sin(ph)*Math.cos(th), 1.27*Math.cos(ph), 1.27*Math.sin(ph)*Math.sin(th)); sun.add(sp); }
const rays = new THREE.Group(); S.scene.add(rays);
for (let k=0;k<12;k++) { const c = T3.inked(new THREE.ConeGeometry(0.16, 0.5, 8), 0xF5A623, 0.02); const a = k*Math.PI/6;
  c.position.set(1.75*Math.cos(a), 1.75*Math.sin(a), 0); c.rotation.z = a - Math.PI/2; rays.add(c); }
drive(@d, t => {
  const s0 = t < 0.6 ? 0.4 + 0.6*gsap.parseEase("back.out(2)")(t/0.6) : 1; sun.scale.setScalar(s0); rays.scale.setScalar(s0);
  sun.rotation.y = t*0.35; rays.rotation.z = -t*0.25;
  S.cam.position.set(0, 0.2, 6.4 - 0.5*Math.min(1, t/@d)); S.cam.lookAt(0, 0, 0); S.render();
});
rise("#sn-title", @tt);
tl.fromTo("#sn-fill", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:@f10, duration:1.0, ease:"power2.out"}, @t10);
ink("#sn-ar", @t10b, 0.3); pop("#sn-lab", @t10b);
tl.fromTo("#sn-lab", {scale:1}, {scale:1.12, duration:0.15, yoyo:true, repeat:1}, @tfm);
""", d=d, tt=tfs - 0.2, t10=t10 - 0.6, f10=(TY0 + 40 - ty(10000)) / (TY0 - TY1 + 40), t10b=t10 + 0.2, tfm=tfm))

# 5 BOLT — bolt inks from a cloud, thermometer shoots from 10,000 to 50,000
s = "bolt"; tlb = aw(s, "lightning bolt"); tss = aw(s, "split second"); t50 = aw(s, "fifty thousand degrees")
F10 = (TY0 + 40 - ty(10000)) / (TY0 - TY1 + 40)
scenes[s] = scene_file(s, f"""
#bl-title {{ top:150px; font-size:72px; }}
#bl-lab {{ position:absolute; left:440px; top:{ty(50000)-10:.0f}px; width:430px; text-align:right; opacity:0; }}
#bl-lab .big {{ font-size:78px; color:{C['red']}; }}
#bl-cnt {{ position:absolute; left:440px; top:700px; width:430px; text-align:right; opacity:0; }}
#bl-cnt .big {{ font-size:72px; }}
#bl-zap {{ position:absolute; left:470px; top:440px; {GH} font-size:96px; color:{C['red']}; opacity:0; transform:rotate(-10deg); }}
#bl-flash {{ position:absolute; left:0; top:0; width:{W}px; height:1920px; background:#FFFFFF; opacity:0; }}
""", f"""
  <div id="bl-title" class="h1">Now… <span class="hl">lightning!</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {cloud("bl-c", 260, 330, 1.15)}
    {bolt("bl-b", 250, 580, 1.15)}
    {therm("bl")}
    <path d="M{TX-34},{ty(10000):.0f} L{TX-80},{ty(10000):.0f}" stroke="{K}" stroke-width="4" stroke-dasharray="8 8"/>
    <text x="{TX-90}" y="{ty(10000)+12:.0f}" text-anchor="end" font-family="Patrick Hand" font-size="38" fill="{K}">Sun 10,000°F</text>
  </svg>
  <div id="bl-zap">ZAP!</div>
  <div id="bl-lab"><span class="big"><span id="bl-n">10,000</span>°F</span></div>
  <div id="bl-flash"></div>
""", J("""
rise("#bl-title", 0.0); ink(".bl-c", 0.1, 0.5);
tl.set("#bl-fill", {scaleY:@f10, transformOrigin:"50% 100%"}, 0);
ink(".bl-b", @tb, 0.35); tl.fromTo("#bl-flash", {opacity:0}, {opacity:0.7, duration:0.05, yoyo:true, repeat:1}, @tb2);
pop("#bl-zap", @tb2, {from:{scale:1.8, rotation:-25}, to:{rotation:-10}});
tl.fromTo("#bl-fill", {scaleY:@f10, transformOrigin:"50% 100%"}, {scaleY:1, duration:@df, ease:"power2.inOut", transformOrigin:"50% 100%"}, @tf);
pop("#bl-lab", @tf); count("#bl-n", 10000, 50000, @tf, @df, fmtInt);
tl.fromTo("#bl-lab", {scale:1}, {scale:1.12, duration:0.15, yoyo:true, repeat:1}, @te);
""", f10=F10, tb=tlb - 0.2, tb2=tlb + 0.2, tf=tss, df=t50 + 0.6 - tss, te=t50 + 0.7))

# 6 TIMES — countable units: five suns stack up to one bolt
s = "times"; tdv = aw(s, "divided by"); tfv = aw(s, "is five"); t5x = aw(s, "five times hotter")
SX, BX, YB, U = 330, 760, 840, 104
suns = "".join(f'<g class="tm-s" opacity="0"><circle cx="{SX}" cy="{YB - U*i - U/2:.0f}" r="{U/2-6:.0f}" fill="{SUN}" stroke="{K}" stroke-width="5"/>'
               f'<text x="{SX}" y="{YB - U*i - U/2 + 14:.0f}" text-anchor="middle" font-family="Patrick Hand" font-size="40" fill="{K}">{i+1}</text></g>' for i in range(5))
scenes[s] = scene_file(s, f"""
#tm-eq {{ top:150px; font-size:62px; }}
#tm-l1 {{ position:absolute; left:{SX-200}px; top:{YB+10}px; width:400px; text-align:center; font-size:40px; }}
#tm-l2 {{ position:absolute; left:{BX-200}px; top:{YB+10}px; width:400px; text-align:center; font-size:40px; }}
#tm-x {{ position:absolute; left:490px; top:420px; opacity:0; }}
""", f"""
  <div id="tm-eq" class="h1" style="opacity:0">50,000 ÷ 10,000 = <span class="hl">5</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path d="M120,{YB} L1000,{YB}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
    {suns}
    <rect id="tm-bar" x="{BX-55}" y="{YB-5*U}" width="110" height="{5*U}" fill="{BOLT}" stroke="{K}" stroke-width="6"/>
    {bolt("tm-bi", BX, YB - 2.5*U, 1.0)}
  </svg>
  <div id="tm-l1">Sun surface</div><div id="tm-l2">lightning</div>
  <div id="tm-x"><span class="pill red" style="font-size:64px">5×</span></div>
""", J("""
tl.fromTo("#tm-bar", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.7, ease:"power2.out"}, 0.1);
ink(".tm-bi", 0.6, 0.4);
rise("#tm-eq", @teq);
tl.fromTo(".tm-s", {opacity:0, y:-60}, {opacity:1, y:0, duration:0.25, stagger:@stg, ease:"back.out(2)"}, @ts);
pop("#tm-x", @t5x, {from:{scale:2, rotation:-20}, to:{rotation:-6}});
""", teq=tdv - 0.6, ts=tdv + 0.2, stg=(tfv - tdv) / 5, t5x=t5x - 0.1))

# 7 FAST — a stopwatch ruler: 0 to 1 second, the flash fits in the first half
s = "fast"; tdl = aw(s, "doesn't last"); tlf = aw(s, "lightning flash"); thf = aw(s, "half a second")
RX0, RX1, RY = 140, 960, 560
def rx(v): return RX0 + (RX1 - RX0) * v
ticks = "".join(f'<path d="M{rx(k/10):.0f},{RY-(30 if k % 5 == 0 else 16)} L{rx(k/10):.0f},{RY}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(11))
labs = "".join(f'<text x="{rx(v):.0f}" y="{RY+50}" text-anchor="middle" font-family="Patrick Hand" font-size="40" fill="{K}">{t}</text>' for v, t in [(0, "0"), (0.5, "½ s"), (1, "1 s")])
scenes[s] = scene_file(s, f"""
#fs-title {{ top:150px; font-size:72px; }}
#fs-lab {{ position:absolute; left:{rx(0)}px; top:{RY+90}px; width:700px; white-space:nowrap; opacity:0; }}
""", f"""
  <div id="fs-title" class="h1">But it's <span class="hl">fast!</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <rect id="fs-band" x="{rx(0)}" y="{RY-120}" width="{rx(0.5)-rx(0):.0f}" height="120" fill="{C['hi']}" opacity="0.8"/>
    <path id="fs-rul" d="M{RX0},{RY} L{RX1},{RY}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>{ticks}{labs}
    {bolt("fs-b", (rx(0)+rx(0.5))/2, RY-230, 0.6, "fs-bg")}
  </svg>
  <div id="fs-lab"><span class="chip" style="font-size:50px">less than ½ second</span></div>
""", J("""
rise("#fs-title", @tt); ink("#fs-rul", 0.1, 0.5);
tl.fromTo("#fs-band", {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:0.6, ease:"power2.out"}, @tb);
ink(".fs-b", @tlf, 0.3);
tl.fromTo("#fs-bg", {opacity:1}, {opacity:0.1, duration:0.07, yoyo:true, repeat:5}, @tlf2);
pop("#fs-lab", @thf);
""", tt=max(0.0, tdl - 0.4), tb=tlf - 0.1, tlf=tlf, tlf2=tlf + 0.4, thf=thf - 0.2))

# 8 THUNDER — cutaway of the air: dots burst outward then snap back, BOOM
s = "thunder"; tbo = aw(s, "burst outward"); tsh = aw(s, "shrink back"); tpp = aw(s, "push and pull"); tth = aw(s, "thunder")
CX, CY = 600, 540
rnd = __import__("random").Random(5)
dots = ""
for i in range(46):
    a = rnd.random() * 2 * _m.pi; r = 70 + rnd.random() * 180
    dots += f'<circle class="th-d" cx="{CX + r*_m.cos(a):.0f}" cy="{CY + r*_m.sin(a)*0.9:.0f}" r="9" fill="{SKY}" stroke="{K}" stroke-width="3"/>'
rings = "".join(f'<circle class="th-r" cx="{CX}" cy="{CY}" r="{120 + 60*i}" fill="none" stroke="{C["blue"]}" stroke-width="6" stroke-dasharray="18 14" opacity="0"/>' for i in range(3))
scenes[s] = scene_file(s, f"""
#th-title {{ top:150px; font-size:70px; }}
#th-boom {{ position:absolute; left:640px; top:250px; {GH} font-size:120px; color:{C['red']}; opacity:0; transform:rotate(-8deg); }}
#th-l1 {{ position:absolute; left:440px; top:850px; width:600px; text-align:center; font-size:44px; opacity:0; }}
""", f"""
  <div id="th-title" class="h1">Where <span class="hl">thunder</span> comes from</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {rings}{dots}
    {bolt("th-b", CX, CY, 1.3)}
  </svg>
  <div id="th-boom">BOOM!</div>
  <div id="th-l1">hot air bursts out, then shrinks back</div>
""", J("""
rise("#th-title", 0.0); ink(".th-b", 0.1, 0.4);
tl.fromTo(".th-d", {scale:1, svgOrigin:"@cx @cy"}, {scale:1.55, svgOrigin:"@cx @cy", duration:0.5, ease:"power3.out"}, @tbo);
tl.to(".th-d", {scale:1.0, svgOrigin:"@cx @cy", duration:0.6, ease:"power2.inOut"}, @tsh);
pop("#th-l1", @tbo);
tl.fromTo(".th-r", {opacity:0.9, scale:0.5, svgOrigin:"@cx @cy"}, {opacity:0, scale:1.6, svgOrigin:"@cx @cy", duration:1.0, stagger:0.25, ease:"power1.out"}, @tth);
pop("#th-boom", @tth, {from:{scale:2.2, rotation:-25}, to:{rotation:-8}});
tl.fromTo(".th-b", {x:0}, {x:6, duration:0.05, yoyo:true, repeat:7}, @tth);
""", cx=CX, cy=CY, tbo=tbo - 0.1, tsh=tsh - 0.1, tth=tth - 0.15))

# 9 COUNT — flash-to-bang track: sound wave rides along, 5 s per mile
s = "count"; ttr = aw(s, "a trick"); tcs = aw(s, "count the seconds"); tdf = aw(s, "divide by five"); t15 = aw(s, "fifteen seconds"); t3m = aw(s, "three miles")
KX0, KX1, KY = 470, 990, 520
def kx(sec): return KX0 + (KX1 - KX0) * sec / 15
kt = "".join(f'<path d="M{kx(k):.0f},{KY-(30 if k % 5 == 0 else 14)} L{kx(k):.0f},{KY}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(16))
km = "".join(f'<g class="ct-m" opacity="0"><text x="{kx(5*m):.0f}" y="{KY+60}" text-anchor="middle" font-family="Patrick Hand" font-size="42" fill="{C["blue"]}">{m} mi</text></g>' for m in (1, 2, 3))
scenes[s] = scene_file(s, f"""
#ct-title {{ top:150px; font-size:66px; }}
#ct-sec {{ position:absolute; left:440px; top:300px; width:600px; text-align:center; opacity:0; }}
#ct-sec .big {{ font-size:84px; }}
#ct-eq {{ position:absolute; left:420px; top:700px; width:620px; text-align:center; opacity:0; }}
#ct-eq .big {{ font-size:80px; color:{C['red']}; }}
""", f"""
  <div id="ct-title" class="h1">Flash… then <span class="hl">boom</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {cloud("ct-c", 250, 380, 0.75)}
    {bolt("ct-b", 240, 540, 0.6)}
    <path id="ct-trk" d="M{KX0},{KY} L{KX1},{KY}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>{kt}{km}
    <g id="ct-w" opacity="0"><path d="M-14,-26 Q4,0 -14,26 M0,-38 Q24,0 0,38" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
  </svg>
  <div id="ct-sec"><span class="big"><span id="ct-n">0</span> s</span></div>
  <div id="ct-eq"><span class="big">15 ÷ 5 = 3 miles</span></div>
""", J("""
rise("#ct-title", 0.0); ink(".ct-c", 0.1, 0.5); ink(".ct-b", @ttr, 0.3);
ink("#ct-trk", @ttr, 0.5);
pop("#ct-sec", @tcs); tl.set("#ct-w", {opacity:1, x:@kx0, y:@ky}, @tcs);
along("#ct-w", "#ct-trk", @tcs, @dw, {ease:"none"}); count("#ct-n", 0, 15, @tcs, @dw, v => String(Math.round(v)));
tl.fromTo(".ct-m", {opacity:0, y:10}, {opacity:1, y:0, duration:0.25, stagger:@ms}, @tdf);
pop("#ct-eq", @t3m);
""", ttr=ttr - 0.1, tcs=tcs, kx0=KX0, ky=KY, dw=t15 + 0.6 - tcs, tdf=tdf - 0.2, ms=0.35, t3m=t3m - 0.4))

# 10 OUTRO — recap, bolt beats sun, go indoors, Stay curious (Max centre: keep y < 620)
s = "outro"; t5 = aw(s, "five times hotter"); tin = aw(s, "go indoors"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; }}
#ou-in {{ position:absolute; left:0; right:0; top:470px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:62px">Lightning ≈ 5× the Sun's surface</span></div>
  <svg id="ou-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    {bolt("ou-b", 380, 360, 0.75)}
    <text id="ou-gt" x="540" y="385" text-anchor="middle" font-family="Gochi Hand" font-size="96" fill="{K}" opacity="0">&gt;</text>
    {sun2d("ou-s", 700, 360, 70)}
  </svg>
  <div id="ou-in"><span class="pill red" style="font-size:54px">thunder roars → go indoors</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-a", @ta);
ink(".ou-b", @tb, 0.4); ink(".ou-s", @tb + 0.2, 0.5, {stagger:0.02}); pop("#ou-gt", @tb + 0.5);
tl.to("#ou-svg", {opacity:0, duration:0.2}, @tin - 0.4);
pop("#ou-in", @tin);
tl.to("#ou-a, #ou-in", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tout);
pop("#ou-c", @tsc);
""", ta=max(0.0, t5 - 1.2), tb=t5 - 0.2, tin=tin - 0.6, tout=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "cooler"), 2.4)
wave(g("intro", "I'm Max"))
point(g("sun", "ten thousand degrees"), 1.2)
wow(g("bolt", "fifty thousand degrees"), 1.3)
wow(g("times", "five times hotter"), 1.3)
point(g("fast", "half a second"), 1.2)
wow(g("thunder", "thunder"), 1.2)
point(g("count", "three miles"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("impact-bass-1.mp3", A("hook", "bolt of lightning"), 0.4), ("ping.mp3", A("hook", "the sun") + 0.4, 0.35),
        ("pop.mp3", A("guess", "cooler"), 0.5), ("pop.mp3", A("guess", "about the same"), 0.5), ("pop.mp3", A("guess", "way hotter"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("ping.mp3", A("sun", "ten thousand degrees") + 0.2, 0.4),
        ("impact-bass-2.mp3", A("bolt", "lightning bolt") + 0.2, 0.5), ("riser.mp3", A("bolt", "split second"), 0.3),
        ("pop.mp3", A("times", "five times hotter"), 0.55), ("click.mp3", A("fast", "half a second"), 0.5),
        ("impact-bass-1.mp3", A("thunder", "thunder") - 0.15, 0.55), ("click-soft.mp3", A("count", "count the seconds"), 0.5),
        ("ping.mp3", A("count", "three miles") - 0.4, 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
