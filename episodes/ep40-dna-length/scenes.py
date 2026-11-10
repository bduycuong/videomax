# MAX WISE ep40 — If you unrolled all the DNA in your body, how far would it reach?
# Sources: NIH genome.gov Human Genome Project FAQ (~3 billion base pairs); BioNumbers 100667 (0.34 nm rise per base pair, B-DNA);
# Sender, Fuchs & Milo 2016, PLoS Biology "Revised estimates for the number of human and bacteria cells in the body"
# (~30 trillion cells; almost 90% enucleated, mostly red blood cells and platelets; ~3 trillion nucleated cells);
# NASA Pluto facts (Pluto ~5.9 billion km from the Sun, 39 AU; 1 AU ~150 million km).
# Maths: 6.2e9 bp x 0.34 nm = 2.1 m per cell (~2 m); 3e12 x 2 m = 6e12 m = 6 billion km; / 150 million km = 40; / 5.9 billion km = 1.02.
# Kit: 3D hook (toon double helix); ink (intro, letters, cell, myth, blood, pluto, outro), morph (intro, cell), along (sun).
# === SCENES ===
import math
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
TAPE = "#BFE3F7"; RBC = "#E0483C"; RBC_L = "#F7B0A8"; NUC = "#8E6CC9"; CELL = "#F7B3C2"
BASES = {"A": "#E0483C", "T": "#2F5DA8", "C": "#3A9A5B", "G": "#C08B17"}
SW = f'stroke="{K}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'

def circ(cx, cy, r):  # single sub-path circle for ink
    return f"M{cx},{cy-r} A{r},{r} 0 1 1 {cx-0.01:.2f},{cy-r} Z"

def wave_path(x0, x1, y, amp, period, phase=0.0, step=6):
    pts = []
    x = x0
    while x <= x1:
        pts.append((x, y + amp * math.sin(2 * math.pi * (x - x0) / period + phase)))
        x += step
    return "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)

# 1 HOOK — 3D toon double helix turning, camera pulls back
s = "hook"; tun = aw(s, "unrolled"); thf = aw(s, "how far"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:74px; opacity:0; }}
#hk-cv {{ position:absolute; left:300px; top:350px; width:600px; height:600px; }}
#hk-lab {{ position:absolute; left:250px; top:470px; {GH} font-size:56px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="hk-q" class="h1">If you <span class="hl">unrolled</span> all your DNA, how far would it reach?</div>
  <canvas id="hk-cv" width="600" height="600"></canvas>
  <div id="hk-lab">DNA</div>
""", J("""
const S = T3.stage("#hk-cv", 600, 600, 35); S.cam.position.set(0, 0, 10); S.cam.lookAt(0, 0, 0);
const hel = new THREE.Group(); S.scene.add(hel);
const R = 1.0, Y0 = -2.5, Y1 = 2.5, TURNS = 2.1, N = 160;
const strand = (ph) => { const pts = []; for (let i=0;i<=N;i++) { const k = i/N, a = ph + k*TURNS*6.2832; pts.push(new THREE.Vector3(R*Math.cos(a), Y0 + (Y1-Y0)*k, R*Math.sin(a))); }
  return new THREE.CatmullRomCurve3(pts); };
const cA = strand(0), cB = strand(2.4);
hel.add(T3.inked(new THREE.TubeGeometry(cA, 240, 0.13, 10, false), 0x2F5DA8, 0.03));
hel.add(T3.inked(new THREE.TubeGeometry(cB, 240, 0.13, 10, false), 0xE0483C, 0.03));
const cols = [0xE0483C, 0x2F5DA8, 0x3A9A5B, 0xE0A21B]; const rnd = T3.seeded(5); const up = new THREE.Vector3(0, 1, 0);
for (let j=1;j<26;j++) { const k = j/26; const p = cA.getPointAt(k), q = cB.getPointAt(k);
  // use matching parameter so rungs are horizontal
  const a1 = k*TURNS*6.2832, y = Y0 + (Y1-Y0)*k; const P = new THREE.Vector3(R*Math.cos(a1), y, R*Math.sin(a1)), Q = new THREE.Vector3(R*Math.cos(a1+2.4), y, R*Math.sin(a1+2.4));
  const len = P.distanceTo(Q); const c = T3.inked(new THREE.CylinderGeometry(0.07, 0.07, len, 8), cols[Math.floor(rnd()*4)], 0.12);
  c.position.copy(P).add(Q).multiplyScalar(0.5); c.quaternion.setFromUnitVectors(up, Q.clone().sub(P).normalize()); hel.add(c); }
const sm = (a, b, t) => { const k = Math.min(1, Math.max(0, (t-a)/(b-a))); return k*k*(3-2*k); };
const bk = gsap.parseEase("back.out(1.7)");
drive(@d, t => {
  hel.rotation.y = 0.9*t; hel.rotation.z = -0.3;
  hel.scale.setScalar(0.5 + 0.5*bk(Math.min(1, t/0.6)));
  hel.scale.y *= 1 + 0.2*sm(@tu, @tu2, t);
  const e = sm(@tu, @d, t); S.cam.position.set(0, 0.2*e, 10 + 2.5*e); S.cam.lookAt(0, 0, 0);
  S.render(); });
rise("#hk-q", @tq); pop("#hk-lab", @tl, {from:{rotation:-15}, to:{rotation:-6}});
""", d=d, tu=tun, tu2=tun + 1.2, tq=0.2, tl=aw(s, "DNA") - 0.05))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "the moon"); t2 = aw(s, "the sun"); t3 = aw(s, "all the way")
notes = [("a", "To the Moon?", -6, 95, "#FFE27A"), ("b", "To the Sun?", 4, 400, TAPE), ("c", "All the way to Pluto?", -3, 705, "#F7C6C6")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:285px;height:280px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;{GH}font-size:54px;line-height:1.05;padding:0 16px;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px;opacity:0">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.3, t2=t2 - 0.3, t3=t3 - 0.1))

# 3 INTRO — logo + underline; a wavy strand inks itself, then straightens (morph). Max centre: keep y < 620
s = "intro"; tmw = aw(s, "Max Wise"); tun = aw(s, "unroll")
WV = wave_path(150, 930, 540, 34, 120, step=10)
ST = "M" + " L".join(f"{x},{540}" for x in range(150, 931, 10))
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; opacity:0; }}
#in-sub {{ position:absolute; left:0; right:0; top:390px; text-align:center; opacity:0; }}
#in-sub .chip {{ font-size:56px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="in-dna" d="{WV}" stroke="{C['blue']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="in-str" d="{ST}" fill="none" stroke="none"/>
  </svg>
  <div id="in-sub"><span class="chip">Let's unroll it!</span></div>
""", J("""
tl.fromTo("#in-ul, #in-dna", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
pop("#in-sub", @tc, {from:{rotation:-8}, to:{rotation:-2}});
ink("#in-dna", @tc, 0.5);
morph("#in-dna", "#in-str", @tm, 0.7, {ease:"back.out(1.4)"});
""", tmw=tmw, tu=tmw + 0.3, tc=tun - 0.2, tm=tun + 0.5))

# 4 LETTERS — typewriter tapes of A T C G; three billion, two copies, six billion
s = "letters"; tdna = aw(s, "DNA recipe"); t3b = aw(s, "three billion"); t2c = aw(s, "two copies"); t6b = aw(s, "six billion")
SEQ = "ATGCCGTTAGCATGGACTTCAGGTACCA"
def tape(tid, top, seq):
    cells = "".join(f'<span style="color:{BASES[ch]}">{ch}</span>' for ch in seq)
    return (f'<div id="{tid}" class="abs" style="left:150px;top:{top}px;width:860px;height:96px;overflow:hidden;background:#FFFFFF;'
            f'border:4px solid {K};border-left:none;opacity:0"><div style="white-space:nowrap;font-family:Courier New,monospace;font-weight:bold;'
            f'font-size:64px;line-height:92px;letter-spacing:6px;padding-left:18px">{cells}</div></div>')
COMP = {"A": "T", "T": "A", "C": "G", "G": "C"}
scenes[s] = scene_file(s, f"""
#lt-t {{ top:150px; font-size:76px; opacity:0; }}
#lt-svg {{ position:absolute; left:0; top:0; }}
#lt-x2 {{ position:absolute; left:20px; top:385px; {GH} font-size:64px; color:{C['red']}; opacity:0; }}
#lt-a {{ position:absolute; left:120px; right:60px; top:620px; text-align:center; opacity:0; }}
#lt-a .big {{ font-size:96px; }}
#lt-b {{ position:absolute; left:120px; right:60px; top:620px; text-align:center; opacity:0; }}
#lt-b .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="lt-t" class="h1">Your <span class="hl">DNA recipe</span></div>
  {tape("lt-k1", 300, SEQ)}{tape("lt-k2", 430, "".join(COMP[c] for c in SEQ))}
  <svg id="lt-svg" width="{W}" height="960" data-layout-ignore>
    <path id="lt-br" d="M140,300 Q110,300 110,340 L110,420 Q110,463 86,463 Q110,463 110,500 L110,580 Q110,620 140,620" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="lt-x2">×2</div>
  <div id="lt-a"><span class="big">≈ <span class="blue">3 billion</span> letters</span></div>
  <div id="lt-b"><span class="big">≈ 6 billion letters</span></div>
""", J("""
tl.fromTo("#lt-br", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
rise("#lt-t", @tt);
tl.fromTo("#lt-k1", {opacity:1, clipPath:"inset(0 100% 0 0)"}, {opacity:1, clipPath:"inset(0 0% 0 0)", duration:1.4, ease:"steps(28)"}, @tk);
pop("#lt-a", @t3);
tl.fromTo("#lt-k2", {opacity:0, x:300}, {opacity:1, x:0, duration:0.45, ease:"back.out(1.6)"}, @t2);
ink("#lt-br", @t2b, 0.45); pop("#lt-x2", @t2c, {from:{rotation:-20, scale:1.6}, to:{rotation:-6}});
tl.to("#lt-a", {opacity:0, y:-20, duration:0.2}, @t6a);
pop("#lt-b", @t6, {from:{scale:1.5}, to:{}});
""", tt=tdna - 0.2, tk=tdna + 0.2, t3=t3b - 0.1, t2=t2c - 0.3, t2b=t2c + 0.1, t2c=t2c + 0.3, t6a=t6b - 0.3, t6=t6b - 0.1))

# 5 CELL — a third of a nanometer per letter; a 2 m tape; the line morphs into a tangle inside a tiny nucleus
s = "cell"; t13 = aw(s, "a third"); tline = aw(s, "line them"); t2m = aw(s, "two meters"); tnuc = aw(s, "nucleus"); tsee = aw(s, "too small")
NPT = 90
LINE = "M" + " L".join(f"{110 + 860*i/(NPT-1):.1f},560" for i in range(NPT))
NX, NY, NR = 640, 760, 92
tang = []
for i in range(NPT):
    a = i / (NPT - 1) * 2 * math.pi * 7
    r = 62 * (0.35 + 0.65 * abs(math.sin(i * 0.37 + 0.6)))
    tang.append((NX + r * math.cos(a + 0.4 * math.sin(i * 0.21)), NY + r * math.sin(a * 1.08)))
TANG = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in tang)
bases3 = "".join(f'<g><circle cx="{360 + k*180}" cy="330" r="62" fill="{col}" stroke="{K}" stroke-width="5"/>'
                 f'<text x="{360 + k*180}" y="352" text-anchor="middle" font-family="Gochi Hand" font-size="64" fill="#fff">{ch}</text></g>'
                 for k, (ch, col) in enumerate([("A", BASES["A"]), ("T", BASES["T"]), ("G", BASES["G"])]))
tticks = "".join(f'<path class="ce-tk" d="M{110 + k*86},{600} L{110 + k*86},{600 + (34 if k % 5 == 0 else 20)}" stroke="{K}" stroke-width="4" stroke-linecap="round" fill="none"/>' for k in range(11))
scenes[s] = scene_file(s, f"""
#ce-svg {{ position:absolute; left:0; top:0; }}
#ce-13 {{ position:absolute; left:400px; top:160px; {GH} font-size:62px; color:{C['red']}; opacity:0; }}
#ce-2m {{ position:absolute; left:0; right:0; top:440px; text-align:center; opacity:0; }}
#ce-2m .big {{ font-size:96px; color:{C['red']}; }}
#ce-nl {{ position:absolute; left:770px; top:650px; {GH} font-size:50px; color:{NUC}; opacity:0; }}
#ce-see {{ position:absolute; left:430px; right:40px; top:880px; text-align:center; opacity:0; }}
#ce-see .pill {{ font-size:50px; color:{C['blue']}; }}
""", f"""
  <svg id="ce-svg" width="{W}" height="960" data-layout-ignore>
    <g id="ce-bases">{bases3}
      <path id="ce-brk" d="M360,420 L360,440 L540,440 L540,420" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
    <g id="ce-tape" opacity="0"><rect x="100" y="590" width="880" height="56" rx="6" fill="#FFE27A" stroke="{K}" stroke-width="4"/>{tticks}</g>
    <path id="ce-nuc" d="{circ(NX, NY, NR)}" fill="#EDE3FA" stroke="{NUC}" stroke-width="7" opacity="0"/>
    <path id="ce-line" d="{LINE}" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ce-tang" d="{TANG}" fill="none" stroke="none"/>
  </svg>
  <div id="ce-13">≈ 1/3 nm</div>
  <div id="ce-2m"><span class="big">≈ 2 m per cell</span></div>
  <div id="ce-nl">nucleus</div>
  <div id="ce-see"><span class="pill">too small to see!</span></div>
""", J("""
tl.fromTo("#ce-line, #ce-brk", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
tl.fromTo("#ce-bases g", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2)", stagger:0.12}, 0.05);
ink("#ce-brk", @t13, 0.4); pop("#ce-13", @t13b);
tl.to("#ce-bases, #ce-13", {opacity:0, y:-30, duration:0.3, ease:"power2.in"}, @tl0);
tl.fromTo("#ce-tape", {opacity:0, scaleX:0, svgOrigin:"100 600"}, {opacity:1, scaleX:1, svgOrigin:"100 600", duration:0.6, ease:"power2.out"}, @tl1);
ink("#ce-line", @tl1, 1.1);
pop("#ce-2m", @t2m);
tl.to("#ce-tape, #ce-2m", {opacity:0, duration:0.3}, @tn0);
tl.fromTo("#ce-nuc", {opacity:0, scale:0.3, svgOrigin:"@nx @ny"}, {opacity:1, scale:1, svgOrigin:"@nx @ny", duration:0.4, ease:"back.out(2)"}, @tn0);
morph("#ce-line", "#ce-tang", @tn0, 0.9, {ease:"power2.inOut"});
tl.to("#ce-line", {attr:{"stroke-width":3}, duration:0.9}, @tn0);
rise("#ce-nl", @tn); pop("#ce-see", @tsee, {from:{rotation:-10}, to:{rotation:-3}});
""", t13=t13, t13b=t13 + 0.3, tl0=tline - 0.35, tl1=tline, t2m=t2m - 0.1, tn0=tnuc - 0.6, tn=tnuc, tsee=tsee - 0.1, nx=NX, ny=NY))

# 6 MYTH — pencil "x 37 trillion cells?" struck by a red pen
s = "myth"; tmp = aw(s, "many people"); t37 = aw(s, "thirty seven"); tnq = aw(s, "not quite")
scenes[s] = scene_file(s, f"""
#my-l {{ top:170px; font-size:56px; color:{C['pencil']}; opacity:0; }}
#my-m {{ position:absolute; left:0; right:0; top:330px; text-align:center; {GH} font-size:100px; color:{C['pencil']}; line-height:1.05; opacity:0; }}
#my-svg {{ position:absolute; left:0; top:0; }}
#my-nq {{ position:absolute; left:0; right:0; top:640px; text-align:center; {GH} font-size:110px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="my-l" class="h1">the popular math…</div>
  <div id="my-m">× 37 trillion<br>cells?</div>
  <svg id="my-svg" width="{W}" height="960" data-layout-ignore>
    <path id="my-x1" d="M170,330 L910,560" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".8"/>
    <path id="my-x2" d="M900,330 L180,560" stroke="{C['red']}" stroke-width="9" opacity=".8" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="my-nq">NOT QUITE!</div>
""", J("""
tl.fromTo("#my-x1, #my-x2", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
rise("#my-l", @tl); rise("#my-m", @tm);
ink("#my-x1", @tx, 0.25); ink("#my-x2", @tx2, 0.25);
pop("#my-nq", @tn, {from:{scale:2, rotation:-20}, to:{rotation:-6}});
""", tl=tmp - 0.1, tm=t37 - 0.2, tx=tnq - 0.4, tx2=tnq - 0.15, tn=tnq))

# 7 BLOOD — ten coloured-pencil cells: nine red blood discs (no nucleus) + one cell with a nucleus
s = "blood"; t30 = aw(s, "thirty trillion"); t9 = aw(s, "nine in"); tnn = aw(s, "have no"); trb = aw(s, "red blood"); tnd = aw(s, "no DNA")
cells = ""
for i in range(10):
    x = 125 + i * 92
    if i < 9:
        cells += (f'<g class="bl-c"><circle cx="{x}" cy="470" r="38" fill="url(#bl-h)" stroke="{K}" stroke-width="4"/>'
                  f'<ellipse cx="{x}" cy="470" rx="16" ry="13" fill="{RBC_L}" stroke="#B83228" stroke-width="2.5"/></g>')
    else:
        cells += (f'<g id="bl-g"><circle cx="{x}" cy="470" r="40" fill="url(#bl-b)" stroke="{K}" stroke-width="4"/>'
                  f'<circle cx="{x}" cy="470" r="17" fill="{NUC}" stroke="{K}" stroke-width="3"/></g>')
scenes[s] = scene_file(s, f"""
#bl-t {{ top:150px; font-size:80px; opacity:0; }}
#bl-svg {{ position:absolute; left:0; top:0; }}
#bl-9 {{ position:absolute; left:90px; width:780px; top:620px; text-align:center; opacity:0; }}
#bl-9 .big {{ font-size:80px; color:{C['red']}; }}
#bl-rb {{ position:absolute; left:90px; width:780px; top:715px; text-align:center; font-size:46px; color:{C['muted']}; opacity:0; }}
#bl-has {{ position:absolute; left:900px; width:160px; top:310px; text-align:center; {GH} font-size:44px; color:{NUC}; opacity:0; }}
#bl-st {{ position:absolute; left:300px; top:290px; padding:0 26px; border:6px solid {C['red']}; border-radius:14px; {GH} font-size:72px; color:{C['red']}; background:rgba(255,253,246,.82); opacity:0; }}
""", f"""
  <div id="bl-t" class="h1">≈ <span class="hl">30 trillion</span> cells</div>
  <svg id="bl-svg" width="{W}" height="960" data-layout-ignore>
    <defs><pattern id="bl-h" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="12" height="12" fill="#F27C70"/><path d="M0,0 L0,12" stroke="{RBC}" stroke-width="5"/></pattern>
      <pattern id="bl-b" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-40)"><rect width="12" height="12" fill="{CELL}"/><path d="M0,0 L0,12" stroke="#E68AA0" stroke-width="3"/></pattern></defs>
    {cells}
    <path id="bl-br" d="M90,540 Q90,575 130,575 L440,575 Q480,575 480,605 Q480,575 520,575 L830,575 Q870,575 870,540" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="bl-9"><div class="big">9 in 10: no nucleus</div></div>
  <div id="bl-rb">mostly red blood cells</div>
  <div id="bl-has">has DNA</div>
  <div id="bl-st">NO DNA</div>
""", J("""
tl.fromTo("#bl-br", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
rise("#bl-t", @t30);
tl.fromTo(".bl-c, #bl-g", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.28, ease:"back.out(2)", stagger:0.07}, @tc);
ink("#bl-br", @t9, 0.5); pop("#bl-9", @t9b, {from:{scale:1.4}, to:{}});
rise("#bl-rb", @trb);
pop("#bl-has", @thas, {from:{rotation:15}, to:{rotation:4}});
pop("#bl-st", @tnd, {from:{scale:2.2, rotation:-25}, to:{rotation:-8}});
""", t30=t30 - 0.2, tc=t30 + 0.3, t9=t9 - 0.15, t9b=t9 + 0.2, trb=trb - 0.2, thas=tnn + 0.6, tnd=tnd - 0.5))

# 8 REAL — the multiplication, counter runs to 6 billion km
s = "real"; t3t = aw(s, "three trillion"); tx = aw(s, "times two"); t6 = aw(s, "six billion")
scenes[s] = scene_file(s, f"""
#re-card {{ position:absolute; left:80px; top:170px; width:920px; height:330px; opacity:0; }}
.re-row {{ position:absolute; left:0; right:0; text-align:center; {GH} font-size:76px; opacity:0; }}
#re-r1 {{ top:40px; }} #re-r2 {{ top:170px; }}
#re-svg {{ position:absolute; left:0; top:0; }}
#re-a {{ position:absolute; left:40px; right:40px; top:600px; text-align:center; opacity:0; }}
#re-n {{ {GH} font-size:120px; color:{C['red']}; white-space:nowrap; }}
""", f"""
  <div id="re-card" class="card">
    <div id="re-r1" class="re-row">≈ <span class="blue">3 trillion</span> cells</div>
    <div id="re-r2" class="re-row">× <span class="blue">2 m</span> each</div>
  </div>
  <svg id="re-svg" width="{W}" height="960" data-layout-ignore>
    <path id="re-ul" d="M150,560 Q540,548 930,562" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="re-a"><span id="re-n">0</span></div>
""", J("""
tl.fromTo("#re-ul", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
pop("#re-card", 0.05, {from:{rotation:-5}, to:{rotation:-1}});
rise("#re-r1", @t1); rise("#re-r2", @t2);
ink("#re-ul", @tu, 0.45);
tl.set("#re-a", {opacity:1}, @tc);
count("#re-n", 0, 6, @tc, @dc, v => "≈ " + (v > 5.97 ? "6" : v.toFixed(1)) + " billion km");
tl.fromTo("#re-n", {scale:1}, {scale:1.12, duration:0.15, yoyo:true, repeat:1, transformOrigin:"50% 50%"}, @t6);
""", t1=t3t - 0.1, t2=tx - 0.1, tu=tx + 0.6, tc=tx + 0.7, dc=round(t6 - tx - 0.6, 3), t6=t6 + 0.1))

# 9 SUN — Earth to Sun, a DNA dot zips along the path, counter to 40
s = "sun"; tea = aw(s, "Earth"); t40 = aw(s, "forty times"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#su-t {{ top:150px; font-size:76px; opacity:0; }}
#su-svg {{ position:absolute; left:0; top:0; }}
#su-c {{ position:absolute; left:0; right:0; top:690px; text-align:center; opacity:0; }}
#su-n {{ {GH} font-size:130px; color:{C['red']}; }}
""", f"""
  <div id="su-t" class="h1">Earth → <span class="hl">Sun</span></div>
  <svg id="su-svg" width="{W}" height="960" data-layout-ignore>
    <circle cx="190" cy="500" r="62" fill="#BFE3F7" stroke="{K}" stroke-width="5"/>
    <path d="M150,480 Q175,450 205,470 Q210,500 180,510 Z M205,520 Q230,505 240,530 Q225,550 205,540 Z" fill="#9BD08F" stroke="{K}" stroke-width="3"/>
    <circle cx="880" cy="500" r="130" fill="#FFC23A" stroke="{K}" stroke-width="6"/>
    <path d="M880,345 L880,320 M880,655 L880,680 M725,500 L700,500 M1035,500 L1060,500" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
    <text x="190" y="610" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{K}">Earth</text>
    <path id="su-p" d="M262,500 L740,500" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-dasharray="14 12"/>
    <g id="su-dot" opacity="0"><circle r="24" fill="{C['hi']}" opacity=".5"/><circle r="13" fill="{C['blue']}" stroke="{K}" stroke-width="4"/></g>
  </svg>
  <div id="su-c"><span id="su-n">×0</span></div>
""", J("""
rise("#su-t", 0.05);
tl.set("#su-dot", {opacity:1}, @ta);
along("#su-dot", "#su-p", @ta, @lap, {ease:"none", repeat:@nrep});
tl.set("#su-c", {opacity:1}, @ta);
count("#su-n", 0, 40, @ta, @run, v => "×" + Math.round(v));
tl.fromTo("#su-n", {scale:1}, {scale:1.25, duration:0.15, yoyo:true, repeat:1, transformOrigin:"50% 50%"}, @t40);
""", ta=tea - 0.1, lap=0.12, nrep=int((t40 + 0.3 - tea) / 0.12), run=round(t40 + 0.2 - tea, 3), t40=t40 + 0.15))

# 10 PLUTO — solar-system map; the DNA strand inks itself from the Sun all the way to Pluto
s = "pluto"; tpl = aw(s, "Pluto"); tfs = aw(s, "from the")
def ax(au): return 150 + 800 * au / 39.5
planets = [(1, 9, "#4F9BE0"), (5.2, 22, "#E0A880"), (9.5, 19, "#E8D08A"), (19.2, 14, "#9ED8E0"), (30.1, 14, "#4F7BE0")]
pd = "".join(f'<circle class="pl-pl" cx="{ax(a):.1f}" cy="520" r="{r}" fill="{col}" stroke="{K}" stroke-width="3.5"/>' for a, r, col in planets)
DNA1 = wave_path(150, ax(39.5), 520, 26, 46, step=4)
DNA2 = wave_path(150, ax(39.5), 520, 26, 46, phase=math.pi, step=4)
scenes[s] = scene_file(s, f"""
#pl-svg {{ position:absolute; left:0; top:0; }}
#pl-t {{ top:150px; font-size:72px; opacity:0; }}
#pl-a {{ position:absolute; left:0; right:0; top:700px; text-align:center; opacity:0; }}
#pl-a .pill {{ font-size:58px; color:{C['red']}; }}
""", f"""
  <div id="pl-t" class="h1">all the way to <span class="hl">Pluto</span>!</div>
  <svg id="pl-svg" width="{W}" height="960" data-layout-ignore>
    <circle cx="20" cy="520" r="120" fill="#FFC23A" stroke="{K}" stroke-width="6"/>
    <text x="40" y="690" text-anchor="middle" font-family="Gochi Hand" font-size="46" fill="{K}">Sun</text>
    <path d="M150,520 L{ax(39.5):.1f},520" stroke="{C['pencil']}" stroke-width="3" stroke-dasharray="8 10" fill="none"/>
    {pd}
    <path id="pl-d1" d="{DNA1}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="pl-d2" d="{DNA2}" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <circle id="pl-p" cx="{ax(39.5):.1f}" cy="520" r="17" fill="#D9C7B0" stroke="{K}" stroke-width="5"/>
    <text id="pl-pt" x="{ax(39.5) - 10:.1f}" y="600" text-anchor="middle" font-family="Gochi Hand" font-size="50" fill="{K}">Pluto</text>
  </svg>
  <div id="pl-a"><span class="pill">your DNA ≈ Sun → Pluto</span></div>
""", J("""
tl.fromTo("#pl-d1, #pl-d2", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
rise("#pl-t", @tt);
ink("#pl-d1, #pl-d2", 0.1, @dd, {ease:"power1.inOut"});
tl.fromTo("#pl-p, #pl-pt", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2.5)"}, @tp);
pop("#pl-a", @ta, {from:{rotation:-10}, to:{rotation:-2}});
""", tt=tpl - 0.3, dd=round(tpl + 0.2, 3), tp=tpl - 0.1, ta=tfs - 0.1))

# 11 OUTRO — callback: tiny helix inks on + chip, then Stay curious (Max centre: keep content above ~620)
s = "outro"; trp = aw(s, "reach Pluto"); tfit = aw(s, "fits inside"); tsc = aw(s, "stay curious")
H1 = wave_path(200, 880, 480, 40, 136, step=6); H2 = wave_path(200, 880, 480, 40, 136, phase=math.pi, step=6)
rungs = "".join(f'<path class="ou-r" d="M{x},{480 + 40*math.sin(2*math.pi*(x-200)/136):.1f} L{x},{480 - 40*math.sin(2*math.pi*(x-200)/136):.1f}" stroke="{c}" stroke-width="6" stroke-linecap="round" fill="none"/>'
                for x, c in zip(range(220, 880, 34), [BASES[k] for k in "ATCGGACTTAGCATGCCGAT"]))
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:170px; text-align:center; opacity:0; }}
#ou-a .chip {{ font-size:66px; }}
#ou-b {{ position:absolute; left:0; right:0; top:290px; text-align:center; font-size:54px; color:{C['muted']}; opacity:0; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip">Your DNA → Pluto!</span></div>
  <div id="ou-b">…and it still fits inside you</div>
  <svg id="ou-svg" width="{W}" height="620" data-layout-ignore>
    {rungs}
    <path id="ou-h1" d="{H1}" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="ou-h2" d="{H2}" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
tl.fromTo("#ou-h1, #ou-h2", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
ink("#ou-h1, #ou-h2", 0.05, 0.9);
tl.fromTo(".ou-r", {opacity:0}, {opacity:1, duration:0.1, stagger:0.04}, 0.3);
pop("#ou-a", @ta, {from:{rotation:-10}, to:{rotation:-2}});
rise("#ou-b", @tb);
tl.to("#ou-a, #ou-b, #ou-svg", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
pop("#ou-c", @tsc);
""", ta=trp - 0.1, tb=tfit - 0.2, tx=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "the moon"), 2.6)
wave(g("intro", "I'm Max"))
point(g("letters", "three billion"), 1.2)
point(g("letters", "six billion"), 1.0)
point(g("cell", "a third"), 1.0)
wow(g("cell", "two meters"), 1.2)
point(g("cell", "nucleus"), 1.2)
think(g("myth", "many people"), g("myth", "not quite"))
point(g("blood", "nine in"), 1.2)
wow(g("blood", "no DNA"), 0.9)
wow(g("real", "six billion"), 1.3)
point(g("sun", "forty times"), 1.0)
wow(g("pluto", "Pluto"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "unrolled"), 0.35), ("pop.mp3", A("guess", "the moon") - 0.3, 0.5), ("pop.mp3", A("guess", "the sun") - 0.3, 0.5),
        ("pop.mp3", A("guess", "all the way") - 0.1, 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click-soft.mp3", A("letters", "DNA recipe") + 0.2, 0.5), ("pop.mp3", A("letters", "six billion"), 0.5),
        ("riser.mp3", A("cell", "line them"), 0.25), ("ping.mp3", A("cell", "two meters"), 0.4),
        ("click.mp3", A("myth", "not quite") - 0.4, 0.5), ("impact-bass-1.mp3", A("blood", "no DNA") - 0.4, 0.45),
        ("impact-bass-2.mp3", A("real", "six billion"), 0.45), ("whoosh-short.mp3", A("sun", "Earth"), 0.3),
        ("ping.mp3", A("pluto", "Pluto"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
