# MAX WISE ep43 — If you jumped into a hole through the Earth, how long would you fall?
# Kit: ink / morph / along helpers + one three.js scene (hook: cut-away toon Earth with a tunnel, a ball drops in).
# Source: Klotz 2015, Am. J. Phys. 83, 231 (arXiv 1308.1342): uniform Earth 42 min 12 s; PREM (seismic) 38 min 11 s;
#  gravity peaks ~1.09 g near the core-mantle boundary, then falls ~linearly to 0 at the centre. Air drag ignored.
# Maths: 38 min 11 s / 2 = 19 min 5 s ~ 19 min each way.
# === SCENES ===
import math as _m, random as _r
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
CRUST = "#A9744B"; MANT = "#F2A65A"; OCORE = "#F7D154"; ICORE = "#FFF2B0"; SEA = "#BFE3F7"; LAND = "#9BD08F"
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
def circ(cx, cy, r):  # one sub-path circle, starts at top, clockwise
    return f"M{cx},{cy-r} A{r},{r} 0 1 1 {cx-0.1:.1f},{cy-r}"
def earth2d(p, cx, cy, r, layers=True):
    """flat cut-away Earth: crust ring, mantle, outer + inner core"""
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CRUST}"/><circle cx="{cx}" cy="{cy}" r="{r*0.94:.0f}" fill="{MANT}"/>'
    if layers: out += f'<circle cx="{cx}" cy="{cy}" r="{r*0.546:.0f}" fill="{OCORE}"/><circle cx="{cx}" cy="{cy}" r="{r*0.19:.0f}" fill="{ICORE}"/>'
    return out + f'<path id="{p}-rim" d="{circ(cx, cy, r)}" stroke="{K}" stroke-width="7" fill="none"/>'

# 1 HOOK — 3D cut-away Earth, tunnel through the middle, a ball drops in
s = "hook"; thole = aw(s, "hole"); tjmp = aw(s, "jumping in"); thw = aw(s, "how long"); toth = aw(s, "other side"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q0 {{ top:160px; font-size:76px; }}
#hk-q {{ top:150px; font-size:80px; }}
#hk-cv {{ position:absolute; left:40px; top:420px; width:1000px; height:540px; }}
#hk-qm {{ position:absolute; left:860px; top:430px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="hk-q0" class="h1">Dig a <span class="hl">hole</span> straight through Earth…</div>
  <div id="hk-q" class="h1" style="opacity:0">How long would you <span class="hl">fall</span>?</div>
  <canvas id="hk-cv" width="1000" height="540"></canvas>
  <div id="hk-qm">?</div>
""", J("""
const S = T3.stage("#hk-cv", 1000, 540, 34);
const R = 1.75, PC = 1.98, PS = PC + Math.PI/4, PL = 1.5*Math.PI;
const shell = (r, col) => { const m = new THREE.Mesh(new THREE.SphereGeometry(r, 64, 40, PS, PL), T3.toon(col, {side:THREE.DoubleSide})); S.scene.add(m); return m; };
const world = new THREE.Group(); S.scene.add(world);
const parts = [shell(R, 0x4F9BE0), shell(R*0.94, 0xF2A65A), shell(R*0.546, 0xF7D154)];
parts.forEach(p => { S.scene.remove(p); world.add(p); });
const ic = T3.inked(new THREE.SphereGeometry(R*0.19, 32, 20), 0xFFF2B0, 0.06); world.add(ic);
const rnd = T3.seeded(3);
for (let i=0;i<12;i++) { const th = 0.5+rnd()*2.1, ph = PS + 0.2 + rnd()*(PL-0.4), sz = R*(0.18+rnd()*0.14);
  const m = new THREE.Mesh(new THREE.SphereGeometry(sz, 18, 12), T3.toon(0x7CC46A)); m.position.setFromSphericalCoords(R*0.97, th, ph); m.scale.set(1,1,0.25); m.lookAt(0,0,0); world.add(m); }
const tun = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, R*2.08, 20), new THREE.MeshBasicMaterial({color:0x262A3B})); world.add(tun);
const ball = T3.inked(new THREE.SphereGeometry(0.11, 20, 14), 0xE0483C, 0.12); world.add(ball);
S.cam.position.set(0, 0, 8); 
drive(@d, t => {
  const s = t < 0.6 ? 0.6 + 0.4*gsap.parseEase("back.out(2)")(t/0.6) : 1; world.scale.setScalar(s);
  const a = -0.35 + 0.5*Math.min(1, t/@d); S.cam.position.set(6.4*Math.sin(a + 0.42), 1.8, 6.4*Math.cos(a + 0.42)); S.cam.lookAt(0, -0.05, 0);
  const k = Math.max(0, t - @tj); const y = k <= 0 ? R + 0.55 : Math.max(-R*0.2, R + 0.55 - 0.5*1.1*k*k);
  ball.position.set(0, y, 0); ball.visible = t > @tb; S.render();
});
tl.to("#hk-q0", {opacity:0, y:-20, duration:0.25}, @tq0);
rise("#hk-q", @tq);
pop("#hk-qm", @toth, {from:{rotation:-20}, to:{rotation:8}});
""", d=d, tj=tjmp, tb=thole, tq0=thw - 0.4, tq=thw - 0.15, toth=toth))

# 2 GUESS — sticky notes; clocks ink themselves
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "few minutes"); t2 = aw(s, "few hours"); t3 = aw(s, "whole day")
notes = [("a", "minutes?", -6, 110, C['hi'], 64), ("b", "hours?", 4, 405, "#BFE3F7", 70), ("c", "a whole day?", -3, 700, "#FFC9C2", 58)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:340px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding:40px 16px 0">{txt}</div>' for k, txt, r, x, bg, fs in notes)
def clock(cx, cy, cls, ang):
    hx, hy = cx + 34*_m.sin(_m.radians(ang)), cy - 34*_m.cos(_m.radians(ang))
    return (f'<path class="{cls}" d="{circ(cx, cy, 52)}" {WS}/><path class="{cls}" d="M{cx},{cy} L{cx},{cy-40}" {WS}/>'
            f'<path class="{cls}" d="M{cx},{cy} L{hx:.0f},{hy:.0f}" stroke="{C["red"]}" stroke-width="5" fill="none" stroke-linecap="round"/>')
doodles = (f'<svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>' + clock(248, 600, "gs-da", 60) + clock(545, 610, "gs-db", 150)
           + clock(838, 610, "gs-dc", 300) + '</svg>')
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  {doodles}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
ink(".gs-da", @ta, 0.3, {stagger:0.1}); ink(".gs-db", @tb, 0.3, {stagger:0.1}); ink(".gs-dc", @tc, 0.3, {stagger:0.1});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.1, ta=t1 + 0.25, tb=t2 + 0.25, tc=t3 + 0.2))

# 3 INTRO — logo, underline, shovel + hole ink themselves (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tjp = aw(s, "jump in"); tpp = aw(s, "on paper")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-sh" d="M120,470 L210,580" stroke="{K}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path class="in-sh" d="M196,560 L246,540 L262,600 Q236,620 214,606 Z" stroke="{K}" stroke-width="6" fill="#DDE3EA" stroke-linejoin="round"/>
    <path class="in-sh" d="M100,470 L140,470" stroke="{K}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path class="in-hl" d="M800,560 C800,530 980,530 980,560 C980,590 800,590 800,560 Z" stroke="{K}" stroke-width="7" fill="{K}"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's jump in… on paper!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tjp); ink(".in-sh", @tjp2, 0.35, {stagger:0.15}); ink(".in-hl", @tpp, 0.4);
""", tmw=tmw, tu=tmw + 0.3, tjp=tjp - 0.15, tjp2=tjp + 0.1, tpp=tpp))

# 4 MYTH — pencil "42 min" note, pale uniform Earth, red strike
s = "myth"; tot = aw(s, "old textbooks"); t42 = aw(s, "forty two"); tpr = aw(s, "pretended"); tsm = aw(s, "same all the way")
rs = _r.Random(4)
dots = "".join(f'<circle cx="{700+rr*_m.cos(a):.0f}" cy="{700+rr*_m.sin(a):.0f}" r="3" fill="{C["pencil"]}"/>' for a, rr in [(rs.uniform(0, 6.283), 140*_m.sqrt(rs.random())) for _ in range(70)])
scenes[s] = scene_file(s, f"""
#my-title {{ top:150px; font-size:76px; }}
#my-note {{ position:absolute; left:120px; top:300px; width:500px; height:230px; background:#FFFFFF; border:4px solid {K}; {SKETCH} transform:rotate(-3deg); text-align:center; }}
#my-note .big {{ font-size:120px; color:{C['pencil']}; line-height:230px; }}
""", f"""
  <div id="my-title" class="h1">The <span class="hl">old</span> textbook answer</div>
  <div id="my-note" style="opacity:0"><span class="big">≈ 42 min</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <g id="my-earth" opacity="0"><circle cx="700" cy="700" r="150" fill="#E6E2DA" stroke="{K}" stroke-width="6"/>{dots}</g>
    <path id="my-x" d="M110,470 C260,380 460,420 640,360" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("my-tp", "same all the way through?", 420, 560, 3, 44)}
""", J("""
rise("#my-title", @tot); pop("#my-note", @t42, {from:{rotation:-14}, to:{rotation:-3}});
pop("#my-earth", @tpr); rise("#my-tp", @tsm);
ink("#my-x", @tx, 0.35, {ease:"power2.out"});
""", tot=tot - 0.1, t42=t42 - 0.1, tpr=tpr, tsm=tsm, tx=tsm + 0.6))

# 5 LAYERS — cut-away Earth rings ink in, density stipple, tape labels
s = "layers"; tis = aw(s, "isn't"); tdi = aw(s, "deep inside"); tir = aw(s, "heavy iron"); tde = aw(s, "denser"); tsu = aw(s, "surface")
CX, CY, R = 560, 590, 290
rs = _r.Random(5)
def stip(n, r0, r1, cls):
    return "".join(f'<circle class="{cls}" cx="{CX+rr*_m.cos(a):.0f}" cy="{CY+rr*_m.sin(a):.0f}" r="3" fill="{K}" opacity=".55"/>' for a, rr in [(rs.uniform(0, 6.283), _m.sqrt(rs.uniform(r0*r0, r1*r1))) for _ in range(n)])
scenes[s] = scene_file(s, f"""
#ly-title {{ top:150px; font-size:80px; }}
""", f"""
  <div id="ly-title" class="h1">It <span class="hl">isn't!</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <circle id="ly-c0" cx="{CX}" cy="{CY}" r="{R}" fill="{CRUST}" opacity="0"/>
    <circle id="ly-c1" cx="{CX}" cy="{CY}" r="{R*0.94:.0f}" fill="{MANT}" opacity="0"/>
    <circle id="ly-c2" cx="{CX}" cy="{CY}" r="{R*0.546:.0f}" fill="{OCORE}" opacity="0"/>
    <circle id="ly-c3" cx="{CX}" cy="{CY}" r="{R*0.19:.0f}" fill="{ICORE}" opacity="0"/>
    <g id="ly-st" opacity="0">{stip(40, R*0.6, R*0.92, "ly-s")}{stip(120, R*0.2, R*0.53, "ly-s")}{stip(50, 0, R*0.18, "ly-s")}</g>
    <path class="ly-r" d="{circ(CX, CY, R)}" stroke="{K}" stroke-width="7" fill="none"/>
    <path class="ly-r" d="{circ(CX, CY, round(R*0.94))}" stroke="{K}" stroke-width="3" fill="none"/>
    <path class="ly-r" d="{circ(CX, CY, round(R*0.546))}" stroke="{K}" stroke-width="5" fill="none"/>
    <path class="ly-r" d="{circ(CX, CY, round(R*0.19))}" stroke="{K}" stroke-width="5" fill="none"/>
    <path id="ly-l1" d="M780,330 L720,390" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path id="ly-l2" d="M830,720 L650,640" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("ly-tm", "rocky mantle", 700, 260, 4, 46)}
  {tape("ly-tc", "heavy iron core", 680, 720, -3, 46, "rgba(255,201,194,.95)")}
  {stamp("ly-sd", "much denser!", 30, 300, -8, 52)}
""", J("""
rise("#ly-title", @tis);
tl.to("#ly-c0", {opacity:1, duration:0.3}, @tdi); tl.to("#ly-c1", {opacity:1, duration:0.3}, @tdi1);
tl.to("#ly-c2", {opacity:1, duration:0.3}, @tir); tl.to("#ly-c3", {opacity:1, duration:0.3}, @tir1);
ink(".ly-r", @tdi, 1.0, {stagger:0.25});
ink("#ly-l2", @tir, 0.3); rise("#ly-tc", @tir);
tl.to("#ly-st", {opacity:1, duration:0.4}, @tde);
pop("#ly-sd", @tde, {from:{rotation:-20, scale:1.6}, to:{}});
ink("#ly-l1", @tsu, 0.3); rise("#ly-tm", @tsu);
""", tis=tis - 0.1, tdi=tdi - 0.1, tdi1=tdi + 0.3, tir=tir - 0.1, tir1=tir + 0.3, tde=tde - 0.1, tsu=tsu - 0.4))

# 6 GRAVITY — graph: depth vs gravity, curve inks itself, ball rides along it
s = "gravity"; twp = aw(s, "weird part"); tfa = aw(s, "as you fall"); tst = aw(s, "stronger"); t9 = aw(s, "nine percent"); tcore = aw(s, "near the core")
GX0, GX1, GY0, GY1 = 170, 960, 760, 300  # x: surface -> centre, y: 0 -> 1.2 g
def gx(dkm): return GX0 + (GX1 - GX0) * dkm / 6371
def gy(g): return GY0 - (GY0 - GY1) * g / 1.2
pts = [(0, 1.0), (700, 1.0), (1500, 1.005), (2300, 1.04), (2891, 1.09)]
pts += [(2891 + (6371 - 2891) * i / 8, 1.09 * (1 - i / 8)) for i in range(1, 9)]
CUR = "M" + " L".join(f"{gx(dk):.1f},{gy(g):.1f}" for dk, g in pts)
CUR0 = f"M{gx(0):.1f},{gy(1):.1f} L{gx(2891):.1f},{gy(1.09):.1f}"
scenes[s] = scene_file(s, f"""
#gv-title {{ top:150px; font-size:74px; }}
#gv-pk {{ position:absolute; left:{gx(2891)-130:.0f}px; top:{gy(1.09)-130:.0f}px; }}
""", f"""
  <div id="gv-title" class="h1">The <span class="hl">weird</span> part</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="gv-ax" d="M{GX0},{GY1-30} L{GX0},{GY0} L{GX1+20},{GY0}" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="gv-1g" d="M{GX0},{gy(1):.0f} L{GX1},{gy(1):.0f}" stroke="{C['pencil']}" stroke-width="3" stroke-dasharray="10 10" fill="none" opacity="0"/>
    <text x="{GX0-14}" y="{gy(1)+12:.0f}" text-anchor="end" font-family="Patrick Hand" font-size="38" fill="{K}">1 g</text>
    <text x="{GX0-14}" y="{GY0+12}" text-anchor="end" font-family="Patrick Hand" font-size="38" fill="{K}">0</text>
    <path d="M{gx(2891):.0f},{GY0} L{gx(2891):.0f},{GY0-14}" stroke="{K}" stroke-width="4"/>
    <text x="{GX0+10}" y="{GY0+50}" font-family="Gochi Hand" font-size="40" fill="{C['muted']}">surface</text>
    <text x="{gx(2891):.0f}" y="{GY0+50}" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{C['muted']}">core</text>
    <text x="{GX1}" y="{GY0+50}" text-anchor="end" font-family="Gochi Hand" font-size="40" fill="{C['muted']}">center</text>
    <text x="{GX0+16}" y="{GY1-10}" font-family="Gochi Hand" font-size="42" fill="{C['blue']}">gravity</text>
    <path id="gv-cur" d="{CUR}" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="gv-p0" d="{CUR0}" stroke="none" fill="none"/>
    <g id="gv-ball" opacity="0"><circle r="20" fill="{C['red']}" stroke="{K}" stroke-width="5"/><circle cx="-6" cy="-6" r="5" fill="#FFFFFF"/></g>
  </svg>
  <div id="gv-pk" style="opacity:0"><span class="pill" style="font-size:56px">≈ 9% stronger!</span></div>
""", J("""
rise("#gv-title", @twp); ink("#gv-ax", @tax, 0.5); tl.to("#gv-1g", {opacity:1, duration:0.3}, @tax2);
ink("#gv-cur", @tfa, @dc, {ease:"power1.inOut"});
tl.set("#gv-ball", {opacity:1, x:@bx, y:@by}, @tfa);
along("#gv-ball", "#gv-p0", @tfa, @db, {ease:"power1.inOut"});
pop("#gv-pk", @t9, {from:{rotation:-12}, to:{rotation:-3}});
tl.fromTo("#gv-ball", {scale:1}, {scale:1.4, transformOrigin:"50% 50%", duration:0.15, yoyo:true, repeat:1}, @tcore);
""", twp=twp - 0.1, tax=0.2, tax2=0.6, tfa=tfa, dc=round(tst + 0.6 - tfa, 3), bx=round(gx(0), 1), by=round(gy(1), 1), db=round(t9 - tfa, 3), t9=t9, tcore=tcore))

# 7 CENTER — ball floats at the centre; big gravity arrow morphs into a dot; 0 g, weightless, top speed
s = "center"; tvc = aw(s, "very center"); tze = aw(s, "zero"); tfl = aw(s, "float"); twl = aw(s, "weightless"); tts = aw(s, "top speed"); d = SC[s]["slot"]
CX, CY, R = 560, 560, 300
ARR = "M560,380 L560,500 L530,470 M560,500 L590,470"
DOT = "M560,452 L560,456 L558,454 M560,456 L562,454"
scenes[s] = scene_file(s, f"""
#ce-title {{ top:150px; font-size:74px; }}
""", f"""
  <div id="ce-title" class="h1">At the <span class="hl">very center</span>…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {earth2d("ce", CX, CY, R)}
    <path d="M{CX},{CY-R} L{CX},{CY+R}" stroke="{K}" stroke-width="22" opacity=".85"/>
    <path id="ce-arr" d="{ARR}" stroke="{C['blue']}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <g id="ce-ball"><circle cx="{CX}" cy="{CY}" r="26" fill="{C['red']}" stroke="{K}" stroke-width="5"/><circle cx="{CX-8}" cy="{CY-8}" r="6" fill="#FFFFFF"/></g>
    {"".join(f'<path class="ce-sp" d="M{CX+40+i*6},{CY-30+i*22} L{CX+110+i*14},{CY-30+i*22}" stroke="{K}" stroke-width="5" stroke-linecap="round" fill="none"/>' for i in range(3))}
    {"".join(f'<path class="ce-sp" d="M{CX-40-i*6},{CY-30+i*22} L{CX-110-i*14},{CY-30+i*22}" stroke="{K}" stroke-width="5" stroke-linecap="round" fill="none"/>' for i in range(3))}
  </svg>
  {stamp("ce-z", "g = 0", 760, 270, 8, 70, C['blue'])}
  {tape("ce-w", "weightless!", 640, 820, -4, 52)}
  {stamp("ce-t", "top speed!", 40, 770, -6, 50)}
""", SIM + J("""
rise("#ce-title", @tvc);
morph("#ce-arr", "@dot", @tze, 0.6, {ease:"power2.in"}); tl.to("#ce-arr", {opacity:0, duration:0.2}, @tze2);
pop("#ce-z", @tze, {from:{rotation:-20, scale:1.6}, to:{}});
sim(@d, t => { const k = Math.max(0, t - @tfl); const y = 14*Math.sin(k*3.2)*Math.min(1, k); gsap.set("#ce-ball", {y, rotation: 30*Math.sin(k*1.7)*Math.min(1,k), svgOrigin:"@cx @cy"}); });
rise("#ce-w", @twl);
ink(".ce-sp", @tts, 0.25, {stagger:0.05}); pop("#ce-t", @tts, {from:{rotation:-20, scale:1.6}, to:{}});
""", dot=DOT, tvc=tvc - 0.4, tze=tze - 0.1, tze2=tze + 0.5, d=d, tfl=tfl, cx=CX, cy=CY, twl=twl, tts=tts - 0.05))

# 8 ANSWER — side-by-side: ball slides through the tunnel while a stopwatch counts to 38 minutes
s = "answer"; tre = aw(s, "real earthquake"); tma = aw(s, "math"); t38 = aw(s, "thirty eight"); tn1 = aw(s, "nineteen minutes down"); tn2 = aw(s, "nineteen minutes up")
CX, CY, R = 540, 450, 240
TUN = f"M{CX-R},{CY} L{CX+R},{CY}"
scenes[s] = scene_file(s, f"""
#an-cnt {{ position:absolute; left:0; right:0; top:730px; text-align:center; }}
#an-cnt .big {{ font-size:120px; color:{C['red']}; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {earth2d("an", CX, CY, R)}
    <path id="an-tun" d="{TUN}" stroke="{K}" stroke-width="22" fill="none" stroke-linecap="round"/>
    <path id="an-p" d="M{CX-R+10},{CY} L{CX+R-10},{CY}" stroke="none" fill="none"/>
    <g id="an-ball" opacity="0"><circle r="20" fill="{C['red']}" stroke="{K}" stroke-width="5"/><circle cx="-6" cy="-6" r="5" fill="#FFFFFF"/></g>
    <path id="an-mk" d="M{CX},{CY-40} L{CX},{CY+40}" stroke="{C['blue']}" stroke-width="6" stroke-dasharray="8 8" fill="none"/>
    <path id="an-a1" d="M{CX-R+30},{CY+80} Q{CX-R/2},{CY+120} {CX-20},{CY+80}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="an-a2" d="M{CX+20},{CY+80} Q{CX+R/2},{CY+120} {CX+R-30},{CY+80}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("an-tp", "real quake data", 330, 150, -3, 50)}
  {tape("an-d", "19 min down", 210, 620, -4, 46, "rgba(191,227,247,.95)")}
  {tape("an-u", "19 min up", 600, 620, 4, 46, "rgba(191,227,247,.95)")}
  <div id="an-cnt"><span id="an-n" class="big">0 min</span></div>
""", J("""
rise("#an-tp", @tre);
tl.set("#an-ball", {opacity:1, x:@bx, y:@cy}, @tma);
along("#an-ball", "#an-p", @tma, @db, {ease:"sine.inOut"});
rise("#an-cnt", @tma); count("#an-n", 0, 38, @tma, @db, v => "≈ " + Math.round(v) + " min");
tl.fromTo("#an-cnt", {scale:1}, {scale:1.12, duration:0.14, yoyo:true, repeat:1}, @t38b);
ink("#an-a1", @tn1, 0.4); rise("#an-d", @tn1); tl.fromTo("#an-mk", {opacity:0}, {opacity:1, duration:0.2}, @tn1);
ink("#an-a2", @tn2, 0.4); rise("#an-u", @tn2);
""", tre=tre - 0.2, bx=CX - R + 10, cy=CY, tma=tma - 0.2, db=round(t38 + 0.6 - (tma - 0.2), 3), t38b=t38 + 0.7, tn1=tn1, tn2=tn2))

# 9 TWIST — a hand misses; the ball swings back and forth forever (simulated)
s = "twist"; tgr = aw(s, "grabs"); tfb = aw(s, "fall all the way"); tbf = aw(s, "back and forth"); tfo = aw(s, "forever"); tna = aw(s, "no air"); d = SC[s]["slot"]
CX, CY, R = 540, 520, 260
HAND = f"M{CX+R+90},{CY-70} L{CX+R+30},{CY-40} Q{CX+R+10},{CY-30} {CX+R+20},{CY-10} L{CX+R+60},{CY-20} M{CX+R+30},{CY-40} L{CX+R+10},{CY-60} M{CX+R+40},{CY-50} L{CX+R+24},{CY-74}"
scenes[s] = scene_file(s, f"""
#tw-q {{ top:150px; font-size:70px; }}
""", f"""
  <div id="tw-q" class="h1">Nobody <span class="hl">grabs</span> you?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    {earth2d("tw", CX, CY, R)}
    <path d="M{CX-R-10},{CY} L{CX+R+10},{CY}" stroke="{K}" stroke-width="22" fill="none" stroke-linecap="round"/>
    <path id="tw-h" d="{HAND}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="tw-lp" d="M{CX-R+20},{CY-60} Q{CX},{CY-140} {CX+R-20},{CY-60}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path class="tw-lp" d="M{CX+R-20},{CY+60} Q{CX},{CY+140} {CX-R+20},{CY+60}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <g id="tw-ball"><circle cx="0" cy="0" r="22" fill="{C['red']}" stroke="{K}" stroke-width="5"/><circle cx="-6" cy="-6" r="5" fill="#FFFFFF"/></g>
  </svg>
  {stamp("tw-f", "forever!", 640, 830, -6, 60)}
  {tape("tw-a", "(if there were no air)", 120, 260, -3, 42)}
""", SIM + J("""
rise("#tw-q", 0.05); ink("#tw-h", @tgr, 0.4);
sim(@d, t => { const k = Math.max(0, t - @tfb); const x = @cx + (@r - 22)*Math.cos(k*2.4); gsap.set("#tw-ball", {x, y:@cy}); });
ink(".tw-lp", @tbf, 0.5, {stagger:0.3});
pop("#tw-f", @tfo, {from:{rotation:-20, scale:1.6}, to:{}});
rise("#tw-a", @tna);
""", tgr=tgr - 0.1, d=d, tfb=tfb - 0.2, cx=CX, r=R, cy=CY, tbf=tbf - 0.1, tfo=tfo - 0.05, tna=tna - 0.3))

# 10 OUTRO — red "?" morphs into a tick (hook callback); chip ≈ 38 minutes; Stay curious (Max centre: keep y < 620)
s = "outro"; t38 = aw(s, "thirty eight"); tcr = aw(s, "whole planet"); tsc = aw(s, "stay curious")
QM = "M470,230 Q470,150 540,150 Q610,150 610,215 Q610,262 545,290 L545,350"
TICK = "M440,250 Q470,280 500,320 Q520,345 530,350 Q580,250 650,160"
scenes[s] = scene_file(s, f"""
#ou-chip {{ position:absolute; left:0; right:0; top:440px; text-align:center; opacity:0; }}
#ou-chip .chip {{ font-size:60px; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <svg id="ou-svg" class="abs" style="left:0;top:0" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <path id="ou-qk" d="{QM}" stroke="{K}" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="ou-q" d="{QM}" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="ou-qd" cx="545" cy="410" r="20" fill="{C['red']}" stroke="{K}" stroke-width="7"/>
  </svg>
  <div id="ou-chip"><span class="chip">≈ 38 minutes!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-svg", 0.05, {from:{scale:0.8}, to:{}});
morph("#ou-qk", "@tick", @t38, 0.55, {ease:"back.out(1.4)"}); morph("#ou-q", "@tick", @t38, 0.55, {ease:"back.out(1.4)"});
tl.to("#ou-q", {stroke:"#3FA34D", duration:0.3}, @t38b);
tl.to("#ou-qd", {opacity:0, scale:0, transformOrigin:"50% 50%", duration:0.2}, @t38);
pop("#ou-chip", @t38c, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#ou-chip", {scale:1}, {scale:1.1, duration:0.14, yoyo:true, repeat:1}, @tcr);
tl.to("#ou-qk, #ou-q, #ou-chip", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tsc0);
pop("#ou-c", @tsc1);
""", tick=TICK, t38=t38 - 0.05, t38b=t38 + 0.25, t38c=t38 + 0.4, tcr=tcr, tsc0=tsc - 0.45, tsc1=tsc - 0.2), fade=False)
# === GESTURES ===
think(g("hook", "how long"), SC["guess"]["start"] + 0.2)
point(g("guess", "few minutes"), 2.6)
wave(g("intro", "I'm Max"))
point(g("myth", "forty two"), 1.2)
point(g("layers", "heavy iron"), 1.2)
wow(g("gravity", "nine percent"), 1.4)
think(SC["center"]["start"] + 0.05, g("center", "zero"))
wow(g("center", "top speed"), 1.2)
point(g("answer", "thirty eight"), 1.4)
wow(g("twist", "forever"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "jumping in"), 0.35), ("ping.mp3", A("hook", "other side") + 0.1, 0.35),
        ("pop.mp3", A("guess", "few minutes"), 0.5), ("pop.mp3", A("guess", "few hours"), 0.5), ("pop.mp3", A("guess", "whole day"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("myth", "same all the way") + 0.6, 0.5),
        ("impact-bass-2.mp3", A("layers", "denser"), 0.35), ("pop.mp3", A("gravity", "nine percent"), 0.5),
        ("click-soft.mp3", A("center", "zero"), 0.55), ("riser.mp3", A("answer", "math") - 0.2, 0.22),
        ("impact-bass-1.mp3", A("answer", "thirty eight") + 0.6, 0.4), ("pop.mp3", A("twist", "forever"), 0.5),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
