# MAX WISE ep30 — More stars in the universe than grains of sand on Earth? (a debate, not settled fact)
# Sources: Universe Today (beaches ~5 sextillion grains; stars >= 10 sextillion = 1e11 galaxies x 1e11 stars),
# The Naked Scientists / M. Merrifield (1e4 grains per metre -> 1e12 per m3; Sahara 1e7 km2 x 1 cm = 1e11 m3 -> 1e23 grains;
# faint small galaxies push stars ~x10 to 1e23). Maths: 1e22 / 5e21 = 2.
# Kit: three.js pull-back (galaxy), ink (intro, stars, grain, desert, outro), along (grain), morph (recount).
# === SCENES ===
import math, random
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
NIGHT = "#1F2747"; STAR = "#FFE27A"; SAND = "#E9C77B"; SANDD = "#C9A055"
def star_pts(cx, cy, r, r2=None):
    r2 = r2 or r * 0.45
    return " ".join(f"{cx + (r if i % 2 == 0 else r2) * math.sin(math.pi * i / 5):.1f},{cy - (r if i % 2 == 0 else r2) * math.cos(math.pi * i / 5):.1f}" for i in range(10))

# 1 HOOK — night card with twinkling stars vs a sand card where grains really fall and pile up
s = "hook"; tsh = aw(s, "cosmic showdown"); tst = aw(s, "more stars"); tsa = aw(s, "grains of sand")
rnd = random.Random(30); sv = ""; sj = ""
for i in range(26):
    x, y = rnd.uniform(30, 410), rnd.uniform(30, 430); r = rnd.uniform(7, 16)
    sv += f'<polygon id="hk-s{i}" points="{star_pts(x, y, r)}" fill="{STAR}" opacity="0"/>'
    t0 = tst - 0.3 + i * 0.05
    sj += f'tl.fromTo("#hk-s{i}", {{opacity:0, scale:0, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.25, ease:"back.out(3)"}}, {t0:.3f});'
    sj += f'tl.to("#hk-s{i}", {{opacity:0.35, duration:0.3, yoyo:true, repeat:3}}, {t0 + 0.6 + rnd.uniform(0, 0.8):.3f});'
gv = ""; gj = ""
for i in range(60):
    # final spot inside a pile (triangle) at the bottom of the sand card (card is 440 x 470)
    while True:
        px, py = rnd.uniform(40, 380), rnd.uniform(300, 450)
        if py >= 450 - (180 - abs(px - 210)) * 0.85: break
    x0 = 210 + rnd.uniform(-20, 20); t0 = tsa - 0.6 + i * 0.045; d = rnd.uniform(0.5, 0.8)
    col = SAND if i % 3 else SANDD
    gv += f'<circle id="hk-g{i}" cx="0" cy="0" r="{rnd.uniform(6, 9):.1f}" fill="{col}" stroke="{K}" stroke-width="2" opacity="0"/>'
    gj += f'tl.fromTo("#hk-g{i}", {{x:{x0:.0f}, y:-10, opacity:1}}, {{x:{px:.0f}, y:{py:.0f}, opacity:1, duration:{d:.2f}, ease:"power2.in", immediateRender:false}}, {t0:.3f});'
scenes[s] = scene_file(s, f"""
#hk-t {{ top:150px; font-size:70px; line-height:1.08; }}
#hk-n {{ position:absolute; left:50px; top:390px; width:420px; height:470px; background:{NIGHT}; border:5px solid {K}; {SKETCH} overflow:hidden; opacity:0; }}
#hk-d {{ position:absolute; left:610px; top:390px; width:420px; height:470px; background:#FFF6DC; border:5px solid {K}; {SKETCH} overflow:hidden; opacity:0; }}
#hk-vs {{ position:absolute; left:470px; top:560px; width:140px; text-align:center; {GH} font-size:84px; color:{C['red']}; opacity:0; }}
.hk-lab {{ position:absolute; left:0; right:0; bottom:14px; text-align:center; {GH} font-size:52px; }}
""", f"""
  <div id="hk-t" class="h1">More <span class="hl">stars</span> in the universe… or <span class="hl">grains of sand</span> on Earth?</div>
  <div id="hk-n"><svg width="420" height="470" data-layout-ignore>{sv}</svg><div class="hk-lab" style="color:{STAR}">STARS</div></div>
  <div id="hk-d"><svg width="420" height="470" style="overflow:hidden" data-layout-ignore>{gv}</svg><div class="hk-lab">SAND</div></div>
  <div id="hk-vs">VS</div>
""", J("""
pop("#hk-t", @t0, {from:{scale:1.2}, to:{}});
pop("#hk-n", @tn, {from:{rotation:-8}, to:{rotation:-2}});
pop("#hk-d", @td, {from:{rotation:8}, to:{rotation:2}});
""" + sj + gj + """
pop("#hk-vs", @tv, {from:{scale:3, rotation:-30}, to:{rotation:-8}});
""", t0=0.05, tn=tst - 0.4, td=tsa - 0.7, tv=tsa + 0.6))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "stars"); t2 = aw(s, "sand"); t3 = aw(s, "a tie")
notes = [("a", "Stars?", -6, 110, STAR), ("b", "Sand?", 4, 405, SAND), ("c", "A tie?", -3, 700, "#BFE3F7")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:70px;line-height:260px;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.15, t2=t2 - 0.15, t3=t3 - 0.15))

# 3 INTRO — logo + a scoreboard inks itself (keep y < 620: Max is centre stage)
s = "intro"; tmw = aw(s, "Max Wise"); tcb = aw(s, "count both")
frame = ["M250,20 Q540,12 830,20", "M830,20 Q838,80 830,140", "M830,140 Q540,148 250,140", "M250,140 Q242,80 250,20", "M540,24 L540,136"]
fh = "".join(f'<path class="in-f" d="{d}" {WS} stroke-width="7"/>' for d in frame)
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:390px; font-size:60px; }}
#in-sc {{ position:absolute; left:0; top:470px; }}
.in-x {{ position:absolute; top:490px; width:290px; text-align:center; {GH} font-size:50px; line-height:1.1; opacity:0; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Count both sides!</span></div>
  <svg id="in-sc" width="{W}" height="160" data-layout-ignore>{fh}</svg>
  <div id="in-xa" class="in-x" style="left:250px">STARS<br><span class="blue">0</span></div>
  <div id="in-xb" class="in-x" style="left:540px">SAND<br><span class="red">0</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tc); ink(".in-f", @tc, 0.35, {stagger:0.08});
pop("#in-xa", @tx); pop("#in-xb", @tx2);
""", tmw=tmw, tu=tmw + 0.3, tc=tcb - 0.3, tx=tcb + 0.2, tx2=tcb + 0.35))

# 4 GALAXY — 3D: a spiral galaxy of points, the camera pulls back until many galaxies fill the dark
s = "galaxy"; tr1 = aw(s, "round one"); tbs = aw(s, "hundred billion stars"); tbg = aw(s, "hundred billion galaxies"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#gx-card {{ position:absolute; left:60px; top:240px; width:960px; height:610px; background:{NIGHT}; border:5px solid {K}; {SKETCH} overflow:hidden; }}
#gx-cv {{ position:absolute; left:0; top:0; width:960px; height:610px; }}
#gx-r {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
.gx-l {{ position:absolute; left:0; right:0; text-align:center; {GH} font-size:54px; color:#fff; opacity:0; }}
.gx-l b {{ color:{STAR}; font-weight:normal; }}
""", f"""
  <div id="gx-r"><span class="chip">Round 1: STARS</span></div>
  <div id="gx-card"><canvas id="gx-cv" width="960" height="610"></canvas>
    <div id="gx-a" class="gx-l" style="top:16px">≈ <b>100,000,000,000</b> stars per galaxy</div>
    <div id="gx-b" class="gx-l" style="top:528px">× <b>100,000,000,000</b> galaxies</div></div>
""", J("""
const S = T3.stage("#gx-cv", 960, 610, 50);
const R = T3.seeded(30);
function spiral(n, sc, cx, cy, cz, rx, ry, arr, col, c1, c2) {
  for (let i = 0; i < n; i++) {
    const r = Math.pow(R(), 0.7) * sc, arm = i % 2, a = r / sc * 4.2 + arm * Math.PI + (R() - 0.5) * 0.7;
    let x = Math.cos(a) * r, y = (R() - 0.5) * 0.08 * sc, z = Math.sin(a) * r;
    const y2 = y * Math.cos(rx) - z * Math.sin(rx), z2 = y * Math.sin(rx) + z * Math.cos(rx); y = y2; z = z2;
    const x3 = x * Math.cos(ry) + z * Math.sin(ry), z3 = -x * Math.sin(ry) + z * Math.cos(ry);
    arr.push(cx + x3, cy + y, cz + z3);
    const k = r / sc; col.push(c1[0] * (1 - k) + c2[0] * k, c1[1] * (1 - k) + c2[1] * k, c1[2] * (1 - k) + c2[2] * k);
  } }
const p1 = [], c1 = []; spiral(3200, 1, 0, 0, 0, 0, 0, p1, c1, [1, 0.95, 0.75], [0.55, 0.7, 1]);
const g1 = new THREE.BufferGeometry(); g1.setAttribute("position", new THREE.Float32BufferAttribute(p1, 3)); g1.setAttribute("color", new THREE.Float32BufferAttribute(c1, 3));
const home = new THREE.Points(g1, new THREE.PointsMaterial({size:2.2, sizeAttenuation:false, vertexColors:true})); S.scene.add(home);
const p2 = [], c2 = [];
for (let k = 0; k < 90; k++) { const rr = 6 + R() * 50, th = R() * Math.PI * 2, ph = (R() - 0.5) * 2.4;
  spiral(50, 0.6 + R() * 0.9, Math.cos(th) * Math.cos(ph) * rr, Math.sin(ph) * rr * 0.8, Math.sin(th) * Math.cos(ph) * rr, R() * 3, R() * 3, p2, c2, [1, 0.9, 0.7], [0.6, 0.75, 1]); }
const g2 = new THREE.BufferGeometry(); g2.setAttribute("position", new THREE.Float32BufferAttribute(p2, 3)); g2.setAttribute("color", new THREE.Float32BufferAttribute(c2, 3));
const m2 = new THREE.PointsMaterial({size:2.6, sizeAttenuation:false, vertexColors:true, transparent:true, opacity:0});
const others = new THREE.Points(g2, m2); S.scene.add(others);
const sm = (a, b, t) => { const k = Math.min(1, Math.max(0, (t - a) / (b - a))); return k * k * (3 - 2 * k); };
drive(@d, t => {
  const e = sm(0.2, @tpe, t), dist = 1.6 * Math.pow(18, e);
  S.cam.position.set(0, dist * 0.55, dist); S.cam.lookAt(0, 0, 0);
  home.rotation.y = 0.25 * t; m2.opacity = sm(@tgo, @tgo + 1.0, t);
  S.render(); });
pop("#gx-r .chip", @tr, {from:{rotation:-10}, to:{rotation:-2}});
pop("#gx-a", @ta); pop("#gx-b", @tb);
""", d=d, tpe=d - 0.5, tgo=tbg - 0.6, tr=tr1, ta=tbs, tb=tbg))

# 5 STARS — 100 billion x 100 billion = 10 sextillion; 1 and 22 zeros pop one by one
s = "stars"; tmu = aw(s, "multiply them"); tts = aw(s, "ten sextillion"); t22 = aw(s, "twenty two zeros"); ton = aw(s, "a one with")
digits = "1" + "0" * 22
groups = []; rev = digits[::-1]
for i in range(0, len(rev), 3): groups.append(rev[i:i + 3][::-1])
groups = groups[::-1]
dh = ""; k = 0
for gi, gr in enumerate(groups):
    for ch in gr:
        dh += f'<span id="st-d{k}" class="st-d{" red" if k == 0 else ""}">{ch}</span>'; k += 1
    if gi < len(groups) - 1: dh += '<span class="st-d">,</span>'
scenes[s] = scene_file(s, f"""
#st-m {{ position:absolute; left:0; right:0; top:180px; text-align:center; {GH} font-size:64px; }}
#st-big {{ position:absolute; left:0; right:0; top:330px; text-align:center; }}
#st-big .big {{ font-size:100px; }}
#st-row {{ position:absolute; left:40px; right:40px; top:600px; text-align:center; {GH} font-size:64px; letter-spacing:1px; }}
.st-d {{ display:inline-block; opacity:0; }}
.st-c {{ display:inline-block; }}
#st-br {{ position:absolute; left:0; top:690px; }}
#st-z {{ position:absolute; left:0; right:0; top:770px; text-align:center; {GH} font-size:56px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="st-m">100,000,000,000 <span class="red">×</span> 100,000,000,000</div>
  <div id="st-big"><div class="big">= ≈ <span class="hl">10 sextillion</span> stars</div></div>
  <div id="st-row">{dh}</div>
  <svg id="st-br" width="{W}" height="80" data-layout-ignore><path id="st-bp" d="M150,10 Q150,40 300,40 L520,40 Q540,40 545,70 Q550,40 570,40 L960,40 Q1000,40 1000,10" {WS} stroke-width="6" stroke="{C['blue']}"/></svg>
  <div id="st-z">1 with 22 zeros!</div>
""", J("""
rise("#st-m", @tm); pop("#st-big", @tt, {from:{scale:1.5}, to:{}});
tl.fromTo("#st-d0", {opacity:0, scale:2}, {opacity:1, scale:1, duration:0.25, ease:"back.out(2)"}, @to);
tl.fromTo(".st-d:not(#st-d0)", {opacity:0, y:-30}, {opacity:1, y:0, duration:0.15, stagger:0.045, ease:"back.out(2)"}, @to2);
ink("#st-bp", @tz, 0.5); pop("#st-z", @tz2);
""", tm=tmu - 0.1, tt=tts - 0.1, to=ton - 0.1, to2=ton + 0.15, tz=t22 - 0.2, tz2=t22 + 0.2))

# 6 GRAIN — a 1 m ruler; a grain rides along while the counter climbs to 10,000; then a cube = 1 trillion grains
s = "grain"; tr2 = aw(s, "round two"); ttt = aw(s, "ten thousand"); tom = aw(s, "one metre"); tcm = aw(s, "cubic metre"); ttr = aw(s, "trillion")
ticks = "".join(f'<path d="M{100+i*88},{80 if i%5 else 60} L{100+i*88},110" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(11))
cube = ["M640,640 L860,640", "M860,640 L860,860", "M860,860 L640,860", "M640,860 L640,640", "M640,640 L720,570", "M860,640 L940,570", "M720,570 L940,570", "M940,570 L940,790", "M860,860 L940,790"]
ch = "".join(f'<path class="gr-c" d="{d}" {WS} stroke-width="6"/>' for d in cube)
dots = "".join(f'<circle cx="{660+ (i%9)*24}" cy="{660+(i//9)*24}" r="5" fill="{SAND}" stroke="{K}" stroke-width="1.5"/>' for i in range(81))
scenes[s] = scene_file(s, f"""
#gr-r {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#gr-svg {{ position:absolute; left:0; top:250px; }}
#gr-n {{ position:absolute; left:0; right:0; top:420px; text-align:center; {GH} font-size:64px; }}
#gr-cl {{ position:absolute; left:90px; top:640px; width:500px; {GH} font-size:58px; line-height:1.1; opacity:0; }}
#gr-dots {{ opacity:0; }}
""", f"""
  <div id="gr-r"><span class="chip" style="background:{SAND}">Round 2: SAND</span></div>
  <svg id="gr-svg" width="{W}" height="700" viewBox="0 250 {W} 700" data-layout-ignore>
    <g transform="translate(0,250)">
    <path id="gr-ru" d="M90,60 L1000,60 L1000,112 L90,112 Z" fill="#FFF6DC" stroke="{K}" stroke-width="5" stroke-linejoin="round" opacity="0"/>
    {ticks}
    <path id="gr-path" d="M100,40 L980,40" fill="none" stroke="none"/>
    <circle id="gr-g" cx="0" cy="0" r="12" fill="{SAND}" stroke="{K}" stroke-width="3" opacity="0"/>
    <text x="100" y="150" font-family="Patrick Hand" font-size="34" text-anchor="middle" fill="{K}">0</text>
    <text x="980" y="150" font-family="Patrick Hand" font-size="34" text-anchor="middle" fill="{K}">1 m</text>
    </g>
    <g id="gr-dots">{dots}</g>
    {ch}
  </svg>
  <div id="gr-n"><span id="gr-cnt" class="red">0</span> grains in a line 1 m long</div>
  <div id="gr-cl">1 m³ ≈<br><span class="hl">1 trillion</span><br>grains</div>
""", J("""
pop("#gr-r .chip", @tr, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#gr-ru", {opacity:0}, {opacity:1, duration:0.3}, @tr2);
tl.set("#gr-g", {opacity:1}, @tt); along("#gr-g", "#gr-path", @tt, @dd, {ease:"power1.inOut"});
count("#gr-cnt", 0, 10000, @tt, @dd, fmtInt);
ink(".gr-c", @tc, 0.3, {stagger:0.07});
tl.fromTo("#gr-dots", {opacity:0}, {opacity:1, duration:0.4}, @tc2);
pop("#gr-cl", @ttr, {from:{rotation:-6}, to:{}});
""", tr=tr2, tr2=tr2 + 0.3, tt=ttt - 0.1, dd=tom + 0.4 - ttt, tc=tcm - 0.3, tc2=tcm + 0.4, ttr=ttr - 0.2))

# 7 BEACH — bar match: stars 10 sextillion vs beaches 5 sextillion; 2 : 1
s = "beach"; tes = aw(s, "one estimate"); tbe = aw(s, "every beach"); t5 = aw(s, "five sextillion"); tsw = aw(s, "stars win"); t21 = aw(s, "two to one")
BB = 900; HS = 520
scenes[s] = scene_file(s, f"""
#bc-t {{ top:150px; font-size:66px; }}
.bc-bar {{ position:absolute; width:200px; bottom:{1920-BB}px; border:5px solid {K}; {SKETCH} transform-origin:50% 100%; }}
#bc-s {{ left:440px; height:{HS}px; background:{NIGHT}; }}
#bc-b {{ left:760px; height:{HS//2}px; background:{SAND}; transform:scaleY(0); }}
.bc-l {{ position:absolute; width:300px; text-align:center; {GH} font-size:46px; line-height:1.05; }}
#bc-tape {{ position:absolute; left:120px; top:300px; padding:6px 20px; background:#BFE3F7; {GH} font-size:44px; transform:rotate(-7deg); opacity:0; }}
#bc-w {{ position:absolute; left:80px; top:470px; width:330px; text-align:center; opacity:0; }}
#bc-w .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="bc-t" class="h1">Stars <span class="red">vs</span> every beach</div>
  <div id="bc-tape">one estimate</div>
  <div id="bc-s" class="bc-bar"></div><div id="bc-b" class="bc-bar"></div>
  <div id="bc-ls" class="bc-l" style="left:390px;top:{BB-HS-120}px">STARS<br>10 sextillion</div>
  <div id="bc-lb" class="bc-l" style="left:710px;top:{BB-HS//2-120}px;opacity:0">BEACHES<br>5 sextillion</div>
  <div id="bc-w"><div class="big">2 : 1</div><span class="chip" style="font-size:42px">stars win!</span></div>
""", J("""
rise("#bc-t", 0.0); rise("#bc-s", 0.1); rise("#bc-ls", 0.15);
pop("#bc-tape", @te, {from:{rotation:-20}, to:{rotation:-7}});
tl.fromTo("#bc-b", {scaleY:0}, {scaleY:1, duration:0.9, ease:"back.out(1.4)"}, @tb);
pop("#bc-lb", @t5);
pop("#bc-w", @tw, {from:{scale:2, rotation:-20}, to:{rotation:-4}});
tl.fromTo("#bc-s", {scaleY:1}, {scaleY:1.05, duration:0.15, yoyo:true, repeat:1}, @t21);
""", te=tes, tb=tbe, t5=t5 - 0.1, tw=tsw - 0.1, t21=t21))

# 8 DESERT — Sahara outline inks; a hatched 1 cm slab; ~100 sextillion; a dune with a growing depth arrow
s = "desert"; tde = aw(s, "about deserts"); tsh = aw(s, "Sahara"); t1c = aw(s, "one centimetre"); t100 = aw(s, "hundred sextillion"); tdp = aw(s, "much deeper")
sah = ["M160,250 Q260,200 380,215 Q470,190 560,220 Q680,205 760,240", "M760,240 Q800,300 770,370 Q700,420 560,410", "M560,410 Q430,430 300,405 Q190,390 150,330 Q140,280 160,250"]
sh = "".join(f'<path class="ds-o" d="{d}" {WS} stroke-width="7"/>' for d in sah)
scenes[s] = scene_file(s, f"""
#ds-t {{ top:150px; font-size:66px; }}
#ds-svg {{ position:absolute; left:40px; top:200px; }}
#ds-lab {{ position:absolute; left:60px; top:530px; width:960px; text-align:center; {GH} font-size:52px; opacity:0; }}
#ds-n {{ position:absolute; left:400px; top:660px; width:620px; text-align:center; opacity:0; }}
#ds-n .big {{ font-size:84px; }}
#ds-dp {{ position:absolute; left:800px; top:830px; {GH} font-size:52px; color:{C['red']}; transform:rotate(-8deg); opacity:0; }}
""", f"""
  <div id="ds-t" class="h1">But what about <span class="hl">deserts</span>?</div>
  <svg id="ds-svg" width="1000" height="800" viewBox="0 120 1000 800" data-layout-ignore>
    <path id="ds-fill" d="M160,250 Q260,200 380,215 Q470,190 560,220 Q680,205 760,240 Q800,300 770,370 Q700,420 560,410 Q430,430 300,405 Q190,390 150,330 Q140,280 160,250 Z" fill="{SAND}" opacity="0"/>
    {sh}
    <text id="ds-sn" x="460" y="330" text-anchor="middle" font-family="Gochi Hand" font-size="56" fill="{K}" opacity="0">SAHARA</text>
    <g id="ds-slab" opacity="0">
      <path d="M120,560 L360,560 L360,590 L120,590 Z" fill="{SAND}" stroke="{K}" stroke-width="4"/>
      {''.join(f'<path d="M{130+i*20},588 L{146+i*20},562" stroke="{SANDD}" stroke-width="3"/>' for i in range(11))}
      <path d="M380,560 L400,560 M390,560 L390,590 M380,590 L400,590" stroke="{C['red']}" stroke-width="4" stroke-linecap="round"/>
    </g>
    <path id="ds-dune" d="M420,850 Q600,640 780,700 Q880,730 960,850" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round" opacity="0"/>
    <path id="ds-ar" d="M900,700 L900,880 M885,862 L900,882 L915,862" fill="none" stroke="{C['red']}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="ds-lab">just <span class="red">1 cm</span> deep</div>
  <div id="ds-n"><div class="big">≈ <span class="hl">100 sextillion</span></div><div style="font-size:46px">grains</div></div>
  <div id="ds-dp">deeper!</div>
""", J("""
pop("#ds-t", 0.0);
ink(".ds-o", @ts, 0.45, {stagger:0.15}); tl.fromTo("#ds-fill", {opacity:0}, {opacity:0.7, duration:0.4}, @ts2); pop("#ds-sn", @ts2);
tl.fromTo("#ds-slab", {opacity:0, x:-40}, {opacity:1, x:0, duration:0.35, ease:"back.out(2)"}, @t1); rise("#ds-lab", @t1);
pop("#ds-n", @t100, {from:{scale:1.5}, to:{}});
tl.to("#ds-svg, #ds-lab", {y:-40, duration:0.4}, @tdp0);
tl.fromTo("#ds-dune", {opacity:0}, {opacity:1, duration:0.2}, @tdp0); ink("#ds-dune", @tdp0, 0.5);
ink("#ds-ar", @tdp, 0.6); pop("#ds-dp", @tdp2);
""", ts=tsh - 0.2, ts2=tsh + 0.4, t1=t1c - 0.1, t100=t100 - 0.3, tdp0=tdp - 0.9, tdp=tdp - 0.3, tdp2=tdp + 0.2))

# 9 RECOUNT — the stars bar morphs from 10 to 100 sextillion while faint galaxies pop around
s = "recount"; tfb = aw(s, "fire back"); tfa = aw(s, "faint little"); tps = aw(s, "push the"); t1h = aw(s, "hundred sextillion")
rnd = random.Random(9); fg = ""
spots = [(150, 300), (300, 260), (230, 420), (400, 380), (140, 560), (330, 560), (220, 700), (420, 690), (480, 250), (120, 800)]
for i, (x, y) in enumerate(spots):
    fg += f'<g id="rc-g{i}" opacity="0">' + "".join(f'<circle cx="{x + rnd.gauss(0, 14):.0f}" cy="{y + rnd.gauss(0, 7):.0f}" r="2.6" fill="{C["blue"]}"/>' for _ in range(16)) + '</g>'
scenes[s] = scene_file(s, f"""
#rc-t {{ top:150px; font-size:66px; }}
#rc-svg {{ position:absolute; left:0; top:0; }}
#rc-l {{ position:absolute; left:560px; top:230px; width:420px; text-align:center; {GH} font-size:50px; line-height:1.05; }}
""", f"""
  <div id="rc-t" class="h1">Astronomers <span class="hl">fire back</span>!</div>
  <svg id="rc-svg" width="{W}" height="960" data-layout-ignore>
    {fg}
    <path id="rc-bar" d="M670,900 L670,700 Q770,690 870,700 L870,900 Z" fill="{NIGHT}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
    <path id="rc-tall" d="M670,900 L670,360 Q770,350 870,360 L870,900 Z" fill="none" stroke="none"/>
  </svg>
  <div id="rc-l">STARS<br><span id="rc-n" class="red">10 sextillion</span></div>
""", J("""
rise("#rc-t", 0.0);
tl.fromTo("#rc-l", {y:430}, {y:430, duration:0.01}, 0);
""" + "".join(f'tl.fromTo("#rc-g{i}", {{opacity:0, scale:0.3, transformOrigin:"50% 50%"}}, {{opacity:0.75, scale:1, duration:0.3, ease:"back.out(2)"}}, @tf+{i*0.12:.2f});' for i in range(len(spots))) + """
morph("#rc-bar", "#rc-tall", @tp, 1.2, {ease:"back.out(1.2)"});
tl.to("#rc-l", {y:0, duration:1.2, ease:"back.out(1.2)"}, @tp);
tl.set("#rc-n", {textContent:"100 sextillion"}, @th);
pop("#rc-n", @th, {from:{scale:1.6}, to:{}});
""", tf=tfa - 0.1, tp=tps - 0.2, th=t1h - 0.1))

# 10 VERDICT — honest ranges on a sextillion axis
s = "verdict"; tdc = aw(s, "depends what"); tob = aw(s, "only beaches"); tsw = aw(s, "stars win"); ted = aw(s, "every desert"); tsm = aw(s, "sand might")
AX0, AX1, AY = 130, 960, 470
def xp(v): return AX0 + (AX1 - AX0) * math.log10(v / 1) / math.log10(200)   # log axis 1..200 sextillion
labs = "".join(f'<path d="M{xp(v):.0f},{AY-12} L{xp(v):.0f},{AY+12}" stroke="{K}" stroke-width="4"/><text x="{xp(v):.0f}" y="{AY+56}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{v}</text>' for v in (5, 10, 100))
scenes[s] = scene_file(s, f"""
#vd-t {{ top:150px; font-size:66px; }}
#vd-svg {{ position:absolute; left:0; top:0; }}
#vd-a {{ position:absolute; left:440px; top:720px; width:560px; opacity:0; }}
#vd-b {{ position:absolute; left:440px; top:830px; width:560px; opacity:0; }}
.vd-c {{ {GH} font-size:46px; }}
""", f"""
  <div id="vd-t" class="h1">It depends what you <span class="hl">count</span></div>
  <svg id="vd-svg" width="{W}" height="960" data-layout-ignore>
    <path id="vd-ax" d="M{AX0},{AY} L{AX1+40},{AY}" {WS} stroke-width="5"/>{labs}
    <text x="{AX1+20}" y="{AY+100}" text-anchor="end" font-family="Patrick Hand" font-size="32" fill="{C['muted']}">sextillion</text>
    <g id="vd-s" opacity="0"><rect x="{xp(10):.0f}" y="{AY-150}" width="{xp(100)-xp(10):.0f}" height="46" fill="{NIGHT}" opacity=".85" stroke="{K}" stroke-width="4"/>
      <text x="{xp(10)-14:.0f}" y="{AY-114}" text-anchor="end" font-family="Gochi Hand" font-size="42" fill="{K}">stars</text></g>
    <g id="vd-d" opacity="0"><rect x="{xp(5):.0f}" y="{AY-82}" width="{xp(100)-xp(5):.0f}" height="46" fill="{SAND}" stroke="{K}" stroke-width="4"/>
      <path d="M{xp(100):.0f},{AY-59} L{xp(190):.0f},{AY-59} M{xp(190)-16:.0f},{AY-73} L{xp(190):.0f},{AY-59} L{xp(190)-16:.0f},{AY-45}" stroke="{SANDD}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="10 8"/>
      <text x="{xp(5)-14:.0f}" y="{AY-46}" text-anchor="end" font-family="Gochi Hand" font-size="42" fill="{K}">sand</text>
      <text x="{xp(190):.0f}" y="{AY-90}" text-anchor="middle" font-family="Gochi Hand" font-size="52" fill="{C['red']}">?</text></g>
  </svg>
  <div id="vd-a"><span class="pill vd-c">only beaches → <span class="blue">STARS</span></span></div>
  <div id="vd-b"><span class="pill vd-c" style="color:{C['red']}">every desert → <span>SAND?</span></span></div>
""", J("""
rise("#vd-t", 0.0); tl.fromTo("#vd-svg", {opacity:0}, {opacity:1, duration:0.3}, 0.2);
tl.fromTo("#vd-s", {opacity:0, x:-30}, {opacity:1, x:0, duration:0.35}, @tdc);
tl.fromTo("#vd-d", {opacity:0, x:-30}, {opacity:1, x:0, duration:0.35}, @tdc2);
pop("#vd-a", @tob); pop("#vd-b", @ted);
""", tdc=tdc, tdc2=tdc + 0.4, tob=tob - 0.1, ted=ted - 0.1))

# 11 OUTRO — vote boxes + Stay curious (Max centre: keep content above y ~840)
s = "outro"; tcf = aw(s, "close fight"); tso = aw(s, "stars or"); tvo = aw(s, "vote in"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:76px; }}
.ou-box {{ position:absolute; top:300px; width:340px; height:220px; border:5px solid {K}; {SKETCH} text-align:center; {GH} font-size:60px; opacity:0; }}
#ou-v {{ position:absolute; left:0; right:0; top:580px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:300px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">Still a <span class="hl">close fight</span>!</div>
  <div id="ou-s" class="ou-box" style="left:150px;background:{NIGHT};color:{STAR}">
    <svg width="90" height="90" style="margin-top:18px" data-layout-ignore><polygon points="{star_pts(45, 48, 40)}" fill="{STAR}" stroke="{K}" stroke-width="3"/></svg><div>STARS</div></div>
  <div id="ou-d" class="ou-box" style="left:590px;background:{SAND}">
    <svg width="120" height="90" style="margin-top:18px" data-layout-ignore><path d="M10,80 Q60,10 110,80 Z" fill="{SANDD}" stroke="{K}" stroke-width="3"/></svg><div>SAND</div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore>
    <path id="ou-ck1" d="M200,330 L230,365 L290,300" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-ck2" d="M640,330 L670,365 L730,300" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <div id="ou-v"><span class="chip">Vote in the comments!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-a", @tc);
pop("#ou-s", @ts, {from:{rotation:-12}, to:{rotation:-3}}); pop("#ou-d", @td, {from:{rotation:12}, to:{rotation:3}});
pop("#ou-v", @tv); ink("#ou-ck1", @tv2, 0.3); ink("#ou-ck2", @tv3, 0.3);
tl.to("#ou-a, #ou-s, #ou-d, #ou-v, #ou-ck1, #ou-ck2", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
pop("#ou-c", @tsc);
""", tc=tcf - 0.4, ts=tso - 0.1, td=tso + 0.3, tv=tvo - 0.1, tv2=tvo + 0.3, tv3=tvo + 0.6, tx=tsc - 0.3, tsc=tsc))

# === GESTURES ===
think(g("hook", "are there"), SC["guess"]["start"] + 0.2)
point(g("guess", "stars"), 2.2)
wave(g("intro", "I'm Max"))
point(g("galaxy", "hundred billion stars"), 1.2)
wow(g("stars", "ten sextillion"), 1.4)
point(g("grain", "ten thousand"), 1.2)
point(g("beach", "five sextillion"), 1.0)
wow(g("beach", "two to one"), 1.0)
think(g("desert", "but what"), g("desert", "Sahara"))
wow(g("desert", "hundred sextillion"), 1.4)
point(g("recount", "push the"), 1.4)
think(g("verdict", "depends what"), g("verdict", "only beaches"))
point(g("verdict", "every desert"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "more stars"), 0.35), ("impact-bass-1.mp3", A("hook", "grains of sand") + 0.6, 0.45),
        ("pop.mp3", A("guess", "stars"), 0.5), ("pop.mp3", A("guess", "sand"), 0.5), ("pop.mp3", A("guess", "a tie"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("riser.mp3", A("galaxy", "and there") - 0.4, 0.3),
        ("ping.mp3", A("stars", "ten sextillion"), 0.4), ("click-soft.mp3", A("grain", "ten thousand"), 0.5),
        ("impact-bass-2.mp3", A("beach", "stars win"), 0.45), ("pop.mp3", A("desert", "hundred sextillion"), 0.5),
        ("whoosh-short.mp3", A("recount", "push the"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
