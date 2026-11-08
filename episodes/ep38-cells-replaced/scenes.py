# MAX WISE ep38 — How many of your cells die and get replaced every single day?
# Sources: Sender & Milo 2021, Nature Medicine "The distribution of cellular turnover in the human body" (via Scientific American
# "Our bodies replace billions of cells every day" and the Weizmann Institute): ~330 billion cells/day, ~1% of ~30 trillion;
# ~9 in 10 by number are blood cells, most of the rest gut lining cells (< 1 week); red blood cells up to ~120 days;
# a bit under 100 g of cells per day; fat cells ~10 years, some muscle cells decades.
# Maths: 330e9/86400 = 3.82 million per second; x ~70 s = 267 million (> 200 million in this video); 330e9/30e12 = 1.1%.
# Kit: 3D hook (toon cell cluster); ink (intro, second, who, gut, myth, outro), morph (day), along (red, gut).
# === SCENES ===
import math
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
CELL = "#F7B3C2"; NUC = "#8E6CC9"; NEW = "#A8E6B0"; TAPE = "#BFE3F7"; RBC = "#E0483C"; RBC_L = "#F7B0A8"
SW = f'stroke="{K}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'

def poly(cx, cy, r_out, r_in=None, n=16):
    pts = []
    for k in range(n):
        a = -math.pi / 2 + 2 * math.pi * k / n
        r = r_out if (r_in is None or k % 2 == 0) else r_in
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"

def circ(cx, cy, r):  # single sub-path circle for ink
    return f"M{cx},{cy-r} A{r},{r} 0 1 1 {cx-0.01:.2f},{cy-r} Z"

# grid of 100 cells shared by total + day
GX0, GY0, GS, GR = 279, 330, 58, 22
PICK = (4, 6)
def grid(prefix, pick_path=False):
    s = ""
    for r in range(10):
        for c in range(10):
            x, y = GX0 + c * GS, GY0 + r * GS
            if pick_path and (r, c) == PICK:
                continue
            s += (f'<g class="{prefix}-d"><circle cx="{x}" cy="{y}" r="{GR}" fill="{CELL}" stroke="{K}" stroke-width="3.5"/>'
                  f'<circle cx="{x+4}" cy="{y-3}" r="7" fill="{NUC}"/></g>')
    return s

# 1 HOOK — 3D toon cluster of cells; one cell shrinks away, a fresh one grows in its place
s = "hook"; thm = aw(s, "how many"); tdie = aw(s, "die"); trep = aw(s, "replaced"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:72px; }}
#hk-box {{ position:absolute; left:250px; top:390px; width:600px; height:560px; }}
#hk-cv {{ position:absolute; left:0; top:0; width:600px; height:560px; }}
.hk-lb {{ position:absolute; {GH} font-size:52px; opacity:0; white-space:nowrap; }}
#hk-bye {{ color:{C['pencil']}; }}
#hk-new {{ color:#2E8B57; }}
""", f"""
  <div id="hk-q" class="h1">How many of your cells <span class="hl">die</span> and get replaced every day?</div>
  <div id="hk-box"><canvas id="hk-cv" width="600" height="560"></canvas>
    <div id="hk-bye" class="hk-lb">bye…</div><div id="hk-new" class="hk-lb">new!</div></div>
""", J("""
const S = T3.stage("#hk-cv", 600, 560, 35); S.cam.position.set(0, 0.3, 7.6); S.cam.lookAt(0, 0, 0);
const P = [[0,0,0.3],[1.1,0.3,0],[-1.1,0.25,0.1],[0.5,1.05,-0.2],[-0.55,1.0,0],[0.6,-0.95,0.1],[-0.6,-0.9,-0.1],[0,0.2,-1.0],
           [1.45,-0.6,-0.5],[-1.45,-0.5,-0.4],[0.95,0.45,0.95],[-0.85,-0.2,1.0],[0.15,-0.45,1.1]];
const clu = new THREE.Group(); S.scene.add(clu);
const geo = new THREE.SphereGeometry(0.62, 32, 20), ngeo = new THREE.SphereGeometry(0.2, 16, 10);
const mk = (p, col) => { const g = T3.inked(geo, col, 0.06); g.position.set(p[0], p[1], p[2]);
  const dir = new THREE.Vector3(p[0], p[1], p[2] + 0.6).normalize();
  const n = new THREE.Mesh(ngeo, T3.toon(0x8E6CC9)); n.position.copy(dir.multiplyScalar(0.5)); g.add(n); clu.add(g); return g; };
const cells = P.map(p => mk(p, 0xF7B3C2));
const fresh = mk(P[10], 0xA8E6B0); const fresh2 = mk(P[3], 0xA8E6B0);
const grey = new THREE.Color(0xA0A0A0), pink = new THREE.Color(0xF7B3C2);
const cl = (t, a, b) => Math.min(1, Math.max(0, (t - a) / (b - a)));
const bk = gsap.parseEase("back.out(2)"), pin = gsap.parseEase("power2.in");
const v = new THREE.Vector3(); const byeEl = document.querySelector("#hk-bye"), newEl = document.querySelector("#hk-new");
drive(@d, t => {
  clu.rotation.y = 0.35 * Math.sin(t * 0.55); clu.rotation.x = 0.12;
  clu.scale.setScalar(0.7 + 0.3 * bk(cl(t, 0, 0.5)));
  const dying = cells[10]; dying.userData.body.material.color.copy(pink).lerp(grey, cl(t, @td0, @td1));
  dying.scale.setScalar(1 - pin(cl(t, @td1, @td2)) + 1e-4);
  fresh.scale.setScalar(bk(cl(t, @tr0, @tr1)) + 1e-4);
  const d2 = cells[3]; d2.userData.body.material.color.copy(pink).lerp(grey, cl(t, @te0, @te1)); d2.scale.setScalar(1 - pin(cl(t, @te1, @te2)) + 1e-4);
  fresh2.scale.setScalar(bk(cl(t, @tf0, @tf1)) + 1e-4);
  clu.updateMatrixWorld(true); dying.getWorldPosition(v); v.project(S.cam);
  const x = (v.x + 1) / 2 * 600, y = (1 - v.y) / 2 * 560;
  byeEl.style.left = (x + 40) + "px"; byeEl.style.top = (y - 120) + "px"; newEl.style.left = (x + 40) + "px"; newEl.style.top = (y - 120) + "px";
  S.render(); });
rise("#hk-q", @tq);
tl.fromTo("#hk-bye", {opacity:0}, {opacity:1, duration:0.15}, @td0); tl.to("#hk-bye", {opacity:0, duration:0.15}, @tr0);
pop("#hk-new", @tr0, {from:{rotation:-15}, to:{rotation:-4}});
""", d=d, tq=thm - 0.15, td0=tdie - 0.1, td1=tdie + 0.25, td2=tdie + 0.7, tr0=trep - 0.05, tr1=trep + 0.5,
     te0=trep + 1.1, te1=trep + 1.4, te2=trep + 1.8, tf0=trep + 2.0, tf1=trep + 2.5))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "few thousand"); t2 = aw(s, "few million"); t3 = aw(s, "or billions")
notes = [("a", "Thousands?", -6, 95, "#FFE27A"), ("b", "Millions?", 4, 400, TAPE), ("c", "Billions?", -3, 705, "#F7C6C6")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:285px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;{GH}font-size:50px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.3, t2=t2 - 0.3, t3=t3 - 0.1))

# 3 INTRO — logo + underline + chip + tally marks that ink themselves (keep y < 620: Max is centre stage)
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "count them")
tal = ""
for grp in range(2):
    bx = 330 + grp * 230
    for k in range(4):
        tal += f'<path class="in-tk" d="M{bx+k*34},500 L{bx+k*34+4},590" stroke="{K}" stroke-width="7" stroke-linecap="round" fill="none"/>'
    tal += f'<path class="in-tk" d="M{bx-16},575 L{bx+124},515" stroke="{C["red"]}" stroke-width="7" stroke-linecap="round" fill="none"/>'
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ position:absolute; left:0; right:0; top:390px; text-align:center; opacity:0; }}
#in-sub .chip {{ font-size:56px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {tal}
  </svg>
  <div id="in-sub"><span class="chip">Let's count them up!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
pop("#in-sub", @tc, {from:{rotation:-8}, to:{rotation:-2}});
ink(".in-tk", @tk, 0.12, {stagger:0.08});
""", tmw=tmw, tu=tmw + 0.3, tc=tct - 0.2, tk=tct + 0.1))

# 4 TOTAL — countable units: a 10 x 10 grid of cell dots
s = "total"; tbd = aw(s, "your body"); t30 = aw(s, "thirty trillion")
scenes[s] = scene_file(s, f"""
#to-t {{ top:150px; font-size:74px; opacity:0; }}
#to-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="to-t" class="h1">≈ <span class="hl">30 trillion</span> cells</div>
  <svg id="to-svg" width="{W}" height="960" data-layout-ignore>{grid("to")}</svg>
""", J("""
tl.fromTo(".to-d", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, ease:"back.out(2)", stagger:{grid:[10,10], from:"center", amount:1.3}}, @tg);
rise("#to-t", @t30);
""", tg=tbd, t30=t30 - 0.1))

# 5 DAY — same grid; one dot (1%) turns red, bursts and comes back as a fresh cell
s = "day"; t1p = aw(s, "one percent"); trp = aw(s, "replaced"); t330 = aw(s, "three hundred")
px, py = GX0 + PICK[1] * GS, GY0 + PICK[0] * GS
scenes[s] = scene_file(s, f"""
#dy-t {{ top:150px; font-size:74px; }}
#dy-svg {{ position:absolute; left:0; top:0; }}
#dy-pc {{ position:absolute; left:850px; top:{py-48}px; background:#FFFDF6; padding:0 8px; {GH} font-size:64px; color:{C['red']}; opacity:0; }}
#dy-a {{ position:absolute; left:400px; right:30px; top:878px; text-align:center; opacity:0; }}
#dy-a .pill {{ font-size:58px; color:{C['red']}; }}
""", f"""
  <div id="dy-t" class="h1">Every day: <span class="hl">1%</span></div>
  <svg id="dy-svg" width="{W}" height="960" data-layout-ignore>{grid("dy", True)}
    <path id="dy-c" d="{poly(px, py, GR)}" fill="{CELL}" stroke="{K}" stroke-width="3.5" stroke-linejoin="round"/>
    <path id="dy-splat" d="{poly(px, py, 40, 14)}" fill="none" stroke="none"/>
    <path id="dy-round" d="{poly(px, py, GR)}" fill="none" stroke="none"/>
    <path id="dy-ring" d="{circ(px, py, 40)}" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="dy-pc">1%</div>
  <div id="dy-a"><span class="pill">≈ 330 billion cells</span></div>
""", J("""
tl.fromTo("#dy-ring", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
tl.to("#dy-c", {fill:"@red", duration:0.2}, @t1);
ink("#dy-ring", @t1, 0.4); pop("#dy-pc", @t1b, {from:{rotation:15}, to:{rotation:-6}});
morph("#dy-c", "#dy-splat", @tr, 0.25, {ease:"power2.out"});
tl.to("#dy-c", {opacity:0, duration:0.15}, @tr2);
tl.set("#dy-c", {fill:"@new"}, @tr3); tl.to("#dy-c", {opacity:1, duration:0.15}, @tr3);
morph("#dy-c", "#dy-round", @tr3, 0.45, {ease:"back.out(2)"});
pop("#dy-a", @t330, {from:{rotation:-10}, to:{rotation:-2}});
""", red=C['red'], new=NEW, t1=t1p - 0.1, t1b=t1p + 0.2, tr=trp - 0.05, tr2=trp + 0.2, tr3=trp + 0.45, t330=t330 - 0.1))

# 6 SECOND — stopwatch inks itself; the hand sweeps one second while a counter runs to 3.8 million
s = "second"; t38 = aw(s, "three point"); tdv = aw(s, "during this"); t200 = aw(s, "two hundred"); d = SC[s]["slot"]
SX, SY, SR = 290, 500, 150
sticks = "".join(f'<path class="se-tk" d="M{SX+(SR-14)*math.sin(a):.1f},{SY-(SR-14)*math.cos(a):.1f} L{SX+(SR-(36 if k%3==0 else 26))*math.sin(a):.1f},{SY-(SR-(36 if k%3==0 else 26))*math.cos(a):.1f}" stroke="{K}" stroke-width="5" stroke-linecap="round" fill="none"/>'
                 for k, a in enumerate([i * math.pi / 6 for i in range(12)]))
scenes[s] = scene_file(s, f"""
#se-t {{ top:150px; font-size:76px; }}
#se-svg {{ position:absolute; left:0; top:0; }}
#se-c {{ position:absolute; left:480px; right:20px; top:400px; text-align:center; opacity:0; }}
#se-n {{ {GH} font-size:104px; color:{C['blue']}; line-height:1; white-space:nowrap; }}
#se-u {{ font-size:48px; }}
#se-a {{ position:absolute; left:60px; right:60px; top:735px; text-align:center; opacity:0; }}
#se-a .pill {{ font-size:54px; color:{C['red']}; }}
""", f"""
  <div id="se-t" class="h1">Every <span class="hl">second</span></div>
  <svg id="se-svg" width="{W}" height="960" data-layout-ignore>
    <path id="se-btn" d="M{SX-22},{SY-SR-34} L{SX+22},{SY-SR-34} M{SX},{SY-SR-34} L{SX},{SY-SR}" {SW} fill="none"/>
    <circle cx="{SX}" cy="{SY}" r="{SR}" fill="#fff" id="se-face" opacity="0"/>
    <path id="se-rim" d="{circ(SX, SY, SR)}" {SW} stroke-width="8" fill="none"/>
    {sticks}
    <g id="se-hand"><path d="M{SX},{SY+18} L{SX},{SY-SR+34}" stroke="{C['red']}" stroke-width="8" stroke-linecap="round"/></g>
    <circle cx="{SX}" cy="{SY}" r="10" fill="{K}"/>
  </svg>
  <div id="se-c"><div id="se-n">0</div><div id="se-u">cells / second</div></div>
  <div id="se-a"><span class="pill">&gt; 200 million in this video!</span></div>
""", J("""
rise("#se-t", 0.0);
tl.to("#se-face", {opacity:1, duration:0.2}, 0.05);
ink("#se-rim", 0.05, 0.45); ink("#se-btn", 0.3, 0.2); ink(".se-tk", 0.3, 0.1, {stagger:0.02});
tl.fromTo("#se-hand", {rotation:0, svgOrigin:"@sx @sy"}, {rotation:360, svgOrigin:"@sx @sy", duration:1, ease:"none", repeat:@nrep}, @th);
pop("#se-c", @th);
count("#se-n", 0, 3800000, @th, 1.0, v => v > 3799000 ? "3.8 million" : Math.round(v).toLocaleString("en-US"));
pop("#se-a", @t200, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#se-a", {scale:1}, {scale:1.08, duration:0.14, yoyo:true, repeat:1}, @t200b);
""", sx=SX, sy=SY, th=t38 - 0.1, nrep=max(0, int(d - t38 - 0.6)), t200=t200 - 0.2, t200b=t200 + 0.6))

# 7 WHO — ten coloured-pencil cells: nine red blood discs + one gut cell
s = "who"; tbl = aw(s, "blood cells"); t9 = aw(s, "nine out"); t10 = aw(s, "every ten")
cells = ""
for i in range(10):
    x = 125 + i * 92
    if i < 9:
        cells += (f'<g class="wh-c"><circle cx="{x}" cy="470" r="38" fill="url(#wh-h)" stroke="{K}" stroke-width="4"/>'
                  f'<ellipse cx="{x}" cy="470" rx="16" ry="13" fill="{RBC_L}" stroke="#B83228" stroke-width="2.5"/></g>')
    else:
        cells += (f'<g id="wh-g"><rect x="{x-34}" y="424" width="68" height="92" rx="14" fill="url(#wh-b)" stroke="{K}" stroke-width="4"/>'
                  f'<circle cx="{x}" cy="490" r="11" fill="{NUC}"/></g>')
scenes[s] = scene_file(s, f"""
#wh-t {{ top:150px; font-size:76px; }}
#wh-svg {{ position:absolute; left:0; top:0; }}
#wh-9 {{ position:absolute; left:120px; width:740px; top:620px; text-align:center; opacity:0; }}
#wh-9 .big {{ font-size:96px; color:{C['red']}; }}
#wh-o {{ position:absolute; left:880px; width:180px; top:550px; text-align:center; {GH} font-size:42px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="wh-t" class="h1">Mostly <span class="hl">blood</span> cells</div>
  <svg id="wh-svg" width="{W}" height="960" data-layout-ignore>
    <defs><pattern id="wh-h" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="12" height="12" fill="#F27C70"/><path d="M0,0 L0,12" stroke="{RBC}" stroke-width="5"/></pattern>
      <pattern id="wh-b" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-40)"><rect width="12" height="12" fill="{TAPE}"/><path d="M0,0 L0,12" stroke="{C['blue']}" stroke-width="3"/></pattern></defs>
    {cells}
    <path id="wh-br" d="M90,540 Q90,575 130,575 L440,575 Q480,575 480,605 Q480,575 520,575 L830,575 Q870,575 870,540" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="wh-9"><div class="big">9 in 10</div></div>
  <div id="wh-o">the rest</div>
""", J("""
rise("#wh-t", 0.0);
tl.fromTo(".wh-c", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.28, ease:"back.out(2)", stagger:0.07}, @tb);
tl.fromTo("#wh-br", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
ink("#wh-br", @t9, 0.5); pop("#wh-9", @t9b, {from:{scale:1.5}, to:{}});
pop("#wh-g", @t10, {from:{rotation:20, transformOrigin:"50% 50%"}, to:{rotation:0}}); rise("#wh-o", @t10b);
""", tb=tbl - 0.2, t9=t9 - 0.15, t9b=t9 + 0.2, t10=t10 - 0.1, t10b=t10 + 0.2))

# 8 RED — a red blood cell rolls along a 120-day track while a day counter runs
s = "red"; trb = aw(s, "red blood"); t120 = aw(s, "one hundred"); tdays = aw(s, "days")
TY = 640
scenes[s] = scene_file(s, f"""
#rd-t {{ top:150px; font-size:76px; opacity:0; }}
#rd-svg {{ position:absolute; left:0; top:0; }}
#rd-c {{ position:absolute; left:0; right:0; top:360px; text-align:center; {GH} font-size:56px; line-height:1; }}
#rd-c span {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="rd-t" class="h1">Up to <span class="hl">120 days</span></div>
  <svg id="rd-svg" width="{W}" height="960" data-layout-ignore>
    <path id="rd-ln" d="M110,{TY} L970,{TY}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {''.join(f'<path class="rd-tk" d="M{110+k*86},{TY} L{110+k*86},{TY+(26 if k%5==0 else 14)}" stroke="{K}" stroke-width="4" stroke-linecap="round" fill="none"/>' for k in range(11))}
    <text x="110" y="{TY+80}" text-anchor="middle" font-family="Gochi Hand" font-size="44" fill="#2E8B57">new</text>
    <text x="960" y="{TY+80}" text-anchor="middle" font-family="Gochi Hand" font-size="44" fill="{C['pencil']}">worn out</text>
    <path id="rd-p" d="M110,{TY-46} L960,{TY-46}" fill="none" stroke="none"/>
    <g id="rd-cell"><g id="rd-roll"><circle cx="0" cy="0" r="44" id="rd-body" fill="{RBC}" stroke="{K}" stroke-width="4"/>
      <ellipse cx="0" cy="0" rx="19" ry="15" id="rd-in" fill="{RBC_L}" stroke="#B83228" stroke-width="3"/>
      <path d="M-30,-10 Q-26,-26 -10,-32" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/></g></g>
  </svg>
  <div id="rd-c">day<br><span id="rd-n">0</span></div>
""", J("""
tl.fromTo("#rd-cell", {x:110, y:@ty0}, {x:110, y:@ty0, duration:0.01}, 0);
ink("#rd-ln", 0.0, 0.4); ink(".rd-tk", 0.2, 0.08, {stagger:0.03});
tl.fromTo("#rd-roll", {scale:0.2, opacity:0, svgOrigin:"0 0"}, {scale:1, opacity:1, svgOrigin:"0 0", duration:0.3, ease:"back.out(2)"}, @tc);
along("#rd-cell", "#rd-p", @ta, @da, {ease:"power1.inOut"});
tl.fromTo("#rd-roll", {rotation:0, svgOrigin:"0 0"}, {rotation:660, svgOrigin:"0 0", duration:@da, ease:"power1.inOut"}, @ta);
count("#rd-n", 0, 120, @ta, @da, v => String(Math.round(v)));
tl.to("#rd-body", {fill:"#A89A9A", duration:0.5}, @tg); tl.to("#rd-in", {fill:"#D8CFCF", duration:0.5}, @tg);
rise("#rd-t", @t120);
""", ty0=TY - 46, tc=trb - 0.1, ta=trb + 0.3, da=tdays - trb, tg=tdays - 0.2, t120=t120 - 0.1))

# 9 GUT — cutaway of gut lining: villi ink on, little cells ride up each villus and fall off the tip
s = "gut"; tgt = aw(s, "your gut"); twr = aw(s, "wear out"); tls = aw(s, "less than"); d = SC[s]["slot"]
VB, VT, VW = 800, 480, 64
vx = [250, 450, 650, 850]
od = f"M110,{VB}"
for cx in vx:
    od += f" L{cx-VW},{VB} L{cx-VW},{VT+VW} Q{cx-VW},{VT} {cx},{VT} Q{cx+VW},{VT} {cx+VW},{VT+VW} L{cx+VW},{VB}"
od += f" L970,{VB}"
fd = od + f" L970,{VB+50} L110,{VB+50} Z"
vpaths = "".join(f'<path id="gu-p{k}" d="M{cx},{VB+20} L{cx},{VT+20} Q{cx+10},{VT-60} {cx+70},{VT-110}" fill="none" stroke="none"/>' for k, cx in enumerate(vx))
gcells = "".join(f'<g id="gu-c{k}{j}" opacity="0"><circle cx="0" cy="0" r="17" fill="{TAPE}" stroke="{K}" stroke-width="3.5"/><circle cx="3" cy="-2" r="5" fill="{NUC}"/></g>' for k in range(4) for j in range(2))
scenes[s] = scene_file(s, f"""
#gu-t {{ top:150px; font-size:76px; }}
#gu-svg {{ position:absolute; left:0; top:0; }}
#gu-tape {{ position:absolute; left:610px; top:870px; padding:4px 26px; background:{TAPE}; opacity:0; {GH} font-size:44px; transform:rotate(-3deg); border-left:3px dashed {C['blue']}; border-right:3px dashed {C['blue']}; }}
#gu-a {{ position:absolute; left:0; right:0; top:262px; text-align:center; opacity:0; }}
#gu-a .pill {{ font-size:58px; color:{C['red']}; }}
""", f"""
  <div id="gu-t" class="h1">The rest: your <span class="hl">gut</span></div>
  <svg id="gu-svg" width="{W}" height="960" data-layout-ignore>
    <path id="gu-fill" d="{fd}" fill="#F9C9D4" stroke="none" opacity="0"/>
    {vpaths}{gcells}
    <path id="gu-ol" d="{od}" {SW} stroke-width="6" fill="none"/>
    <path id="gu-cut" d="M110,{VB+50} L970,{VB+50}" stroke="{C['blue']}" stroke-width="4" stroke-dasharray="14 10" fill="none"/>
  </svg>
  <div id="gu-tape">gut lining</div>
  <div id="gu-a"><span class="pill">&lt; 1 week</span></div>
""", J("""
rise("#gu-t", 0.0);
ink("#gu-ol", 0.05, 0.8); tl.to("#gu-fill", {opacity:1, duration:0.4}, 0.6); tl.fromTo("#gu-cut", {opacity:0}, {opacity:1, duration:0.3}, 0.6);
for (let k=0;k<4;k++) for (let j=0;j<2;j++) {
  const id = "#gu-c"+k+j, t0 = 0.6 + k*0.18 + j*1.45;
  tl.set(id, {opacity:1}, t0);
  along(id, "#gu-p"+k, t0, 1.6, {ease:"power1.in"});
  tl.to(id, {opacity:0, duration:0.25}, t0+1.35);
}
rise("#gu-tape", @tgt);
pop("#gu-a", @tls, {from:{rotation:-12}, to:{rotation:-3}});
""", tgt=tgt, tls=tls - 0.1))

# 10 MASS — balance scale: a pile of cells (< 100 g) tips the beam, two eggs drop on the other pan, PLONK
s = "mass"; tad = aw(s, "add it"); t100 = aw(s, "one hundred"); tegg = aw(s, "two eggs"); tw = aw(s, "the weight")
PVX, PVY, L = 540, 420, 280
dy = L * math.sin(math.radians(10))
def pan(pid, cx, inner=""):
    return (f'<g id="{pid}"><path d="M{cx},{PVY} L{cx-70},{PVY+150} M{cx},{PVY} L{cx+70},{PVY+150}" stroke="{K}" stroke-width="3.5" fill="none"/>'
            f'{inner}<path d="M{cx-95},{PVY+150} Q{cx},{PVY+215} {cx+95},{PVY+150} Z" fill="#FFFFFF" {SW}/></g>')
pile = "".join(f'<g class="ms-pc"><circle cx="{x}" cy="{y}" r="17" fill="{CELL}" stroke="{K}" stroke-width="3"/><circle cx="{x+3}" cy="{y-2}" r="5" fill="{NUC}"/></g>'
               for x, y in [(218, 552), (252, 552), (286, 552), (322, 552), (236, 524), (270, 522), (304, 524), (254, 496), (288, 496), (271, 470)])
eggs = (f'<g id="ms-eggs"><ellipse cx="785" cy="526" rx="30" ry="38" fill="#FFF3DC" {SW}/><ellipse cx="855" cy="526" rx="30" ry="38" fill="#FFF3DC" {SW}/>'
        f'<path d="M772,508 Q776,498 784,494 M842,508 Q846,498 854,494" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/></g>')
scenes[s] = scene_file(s, f"""
#ms-t {{ top:150px; font-size:72px; opacity:0; }}
#ms-svg {{ position:absolute; left:0; top:0; }}
#ms-g {{ position:absolute; left:150px; width:250px; top:{PVY+235}px; text-align:center; opacity:0; }}
#ms-g .pill {{ font-size:54px; color:{C['red']}; }}
#ms-e {{ position:absolute; left:690px; width:260px; top:{PVY+235}px; text-align:center; {GH} font-size:50px; color:{C['blue']}; opacity:0; }}
#ms-pl {{ position:absolute; left:830px; top:330px; {GH} font-size:62px; color:{C['red']}; opacity:0; }}
""", f"""
  <div id="ms-t" class="h1">A bit under <span class="hl">100 g</span> a day</div>
  <svg id="ms-svg" width="{W}" height="960" data-layout-ignore>
    <path d="M{PVX},{PVY} L{PVX},860 M{PVX-110},860 L{PVX+110},860" {SW} stroke-width="8" fill="none"/>
    <path d="M{PVX-34},{PVY+10} L{PVX},{PVY-30} L{PVX+34},{PVY+10} Z" fill="{C['hi']}" {SW}/>
    <g id="ms-beam"><path d="M{PVX-L-20},{PVY} L{PVX+L+20},{PVY}" stroke="{K}" stroke-width="10" stroke-linecap="round" fill="none"/></g>
    {pan("ms-lp", PVX-L, pile)}
    {pan("ms-rp", PVX+L, eggs)}
    <circle cx="{PVX}" cy="{PVY}" r="10" fill="{K}"/>
  </svg>
  <div id="ms-g"><span class="pill">&lt; 100 g</span></div>
  <div id="ms-e">2 eggs</div>
  <div id="ms-pl">PLONK!</div>
""", J("""
tl.fromTo("#ms-eggs", {y:-560, opacity:0}, {y:-560, opacity:0, duration:0.01}, 0);
tl.fromTo(".ms-pc", {opacity:0, y:-140}, {opacity:1, y:0, duration:0.3, ease:"bounce.out", stagger:0.07}, @tp);
tl.to("#ms-beam", {rotation:-10, svgOrigin:"@px @py", duration:0.5, ease:"back.out(1.6)"}, @tt);
tl.to("#ms-lp", {y:@dy, duration:0.5, ease:"back.out(1.6)"}, @tt); tl.to("#ms-rp", {y:-@dy, duration:0.5, ease:"back.out(1.6)"}, @tt);
rise("#ms-t", @t100); pop("#ms-g", @t100b);
tl.to("#ms-eggs", {y:0, opacity:1, duration:0.4, ease:"power2.in"}, @te);
tl.to("#ms-beam", {rotation:0, svgOrigin:"@px @py", duration:0.6, ease:"elastic.out(1,0.5)"}, @tl);
tl.to("#ms-lp, #ms-rp", {y:0, duration:0.6, ease:"elastic.out(1,0.5)"}, @tl);
pop("#ms-pl", @tl, {from:{scale:2, rotation:-20}, to:{rotation:-8}}); rise("#ms-e", @tl2);
""", px=PVX, py=PVY, dy=round(dy, 1), tp=tad, tt=tad + 0.8, t100=t100 - 0.1, t100b=t100 + 0.4, te=tegg - 0.6, tl=tegg - 0.2, tl2=tegg + 0.1))

# 11 MYTH — pencil myth struck by red pen; then honest bars: fat about ten years, some muscle cells decades
s = "myth"; tps = aw(s, "people say"); t7 = aw(s, "seven years"); tnq = aw(s, "not quite"); tft = aw(s, "fat cells"); t10y = aw(s, "ten years")
tmu = aw(s, "muscle cells"); tdc = aw(s, "decades")
BX = 430; YPX = 18  # px per year
scenes[s] = scene_file(s, f"""
#my-m {{ top:160px; {GH} font-size:66px; color:{C['pencil']}; line-height:1.08; opacity:0; }}
#my-svg {{ position:absolute; left:0; top:0; }}
#my-nq {{ position:absolute; left:600px; top:350px; {GH} font-size:70px; color:{C['red']}; opacity:0; white-space:nowrap; }}
.my-lb {{ position:absolute; left:40px; width:370px; text-align:right; {GH} font-size:50px; line-height:1; opacity:0; }}
#my-f {{ top:530px; }} #my-mu {{ top:680px; }}
.my-v {{ position:absolute; {GH} font-size:52px; opacity:0; white-space:nowrap; }}
#my-fv {{ left:{BX + 10*YPX + 22}px; top:530px; color:{C['blue']}; }}
#my-dv {{ left:{BX + 10}px; top:790px; color:{C['red']}; }}
""", f"""
  <div id="my-m" class="h1">"Every cell is replaced<br>every 7 years"</div>
  <svg id="my-svg" width="{W}" height="960" data-layout-ignore>
    <defs><pattern id="my-hf" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="14" height="14" fill="{C['hi']}"/><path d="M0,0 L0,14" stroke="#E0B800" stroke-width="5"/></pattern>
      <pattern id="my-hm" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="14" height="14" fill="#F7C6C6"/><path d="M0,0 L0,14" stroke="{C['red']}" stroke-width="4"/></pattern>
      <linearGradient id="my-fade" x1="0" x2="1"><stop offset="0" stop-color="#F7C6C6" stop-opacity="1"/><stop offset="1" stop-color="#F7C6C6" stop-opacity="0"/></linearGradient></defs>
    <path id="my-x" d="M120,215 L960,250 M140,320 L940,280" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <rect id="my-fb" x="{BX}" y="530" width="{10*YPX}" height="64" rx="8" fill="url(#my-hf)" {SW}/>
    <rect id="my-mb" x="{BX}" y="690" width="{20*YPX}" height="64" rx="8" fill="url(#my-hm)" {SW}/>
    <rect id="my-band" x="{BX + 20*YPX}" y="690" width="{1050 - BX - 20*YPX}" height="64" fill="url(#my-fade)"/>
    <path id="my-ar" d="M{BX + 20*YPX},780 L1030,780 M1006,762 L1030,780 L1006,798" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="16 12"/>
  </svg>
  <div id="my-nq">NOT QUITE!</div>
  <div id="my-f" class="my-lb">fat cells</div>
  <div id="my-mu" class="my-lb">some muscle<br>cells</div>
  <div id="my-fv" class="my-v">≈ 10 years</div>
  <div id="my-dv" class="my-v">decades!</div>
""", J("""
tl.fromTo("#my-x", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
rise("#my-m", @tm);
ink("#my-x", @tx, 0.35); pop("#my-nq", @tx2, {from:{scale:2, rotation:-20}, to:{rotation:-8}});
rise("#my-f", @tf);
tl.fromTo("#my-fb", {scaleX:0, svgOrigin:"@bx 0"}, {scaleX:1, svgOrigin:"@bx 0", duration:0.5, ease:"power2.out"}, @tf2);
pop("#my-fv", @t10);
rise("#my-mu", @tmu);
tl.fromTo("#my-mb", {scaleX:0, svgOrigin:"@bx 0"}, {scaleX:1, svgOrigin:"@bx 0", duration:0.6, ease:"power2.out"}, @tmu2);
tl.fromTo("#my-band", {opacity:0}, {opacity:1, duration:0.4}, @tdc0);
tl.fromTo("#my-ar", {opacity:0}, {opacity:1, duration:0.2}, @tdc0);
pop("#my-dv", @tdc, {from:{rotation:10}, to:{rotation:-3}});
""", tm=tps - 0.1, tx=tnq - 0.15, tx2=tnq + 0.1, tf=tft - 0.15, tf2=tft + 0.1, t10=t10y - 0.1, tmu=tmu - 0.3, tmu2=tmu,
     tdc0=tdc - 0.5, tdc=tdc - 0.1, bx=BX))

# 12 OUTRO — callback: one red dot in a row of cells + "330 billion a day!", Stay curious (Max centre: keep content above ~620)
s = "outro"; t330 = aw(s, "three hundred"); tsc = aw(s, "stay curious")
odots = "".join(f'<g class="ou-d"><circle cx="{150+i*86}" cy="500" r="28" fill="{NEW if i==6 else CELL}" stroke="{K}" stroke-width="4"/><circle cx="{154+i*86}" cy="496" r="8" fill="{NUC}"/></g>' for i in range(10))
scenes[s] = scene_file(s, f"""
#ou-a {{ top:170px; font-size:84px; line-height:1.05; opacity:0; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">330 billion</span><br>new cells a day!</div>
  <svg id="ou-svg" width="{W}" height="620" data-layout-ignore>
    {odots}
    <path id="ou-ring" d="{circ(666, 500, 46)}" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
tl.fromTo("#ou-ring", {drawSVG:"0%"}, {drawSVG:"0%", duration:0.01}, 0);
tl.fromTo(".ou-d", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, ease:"back.out(2)", stagger:0.05}, 0.05);
ink("#ou-ring", @tr, 0.4);
pop("#ou-a", @ta, {from:{scale:1.5}, to:{}});
tl.to("#ou-a, #ou-svg", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
pop("#ou-c", @tsc);
""", tr=t330 + 0.2, ta=t330 - 0.1, tx=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "few thousand"), 2.6)
wave(g("intro", "I'm Max"))
point(g("total", "thirty trillion"), 1.2)
point(g("day", "one percent"), 1.2)
wow(g("day", "three hundred"), 1.4)
point(g("second", "three point"), 1.2)
wow(g("second", "two hundred"), 1.3)
point(g("who", "nine out"), 1.2)
point(g("red", "one hundred"), 1.2)
point(g("gut", "less than"), 1.1)
wow(g("mass", "two eggs"), 1.0)
think(g("myth", "people say"), g("myth", "not quite"))
point(g("myth", "decades"), 1.1)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "die"), 0.35), ("pop.mp3", A("hook", "replaced"), 0.45),
        ("pop.mp3", A("guess", "few thousand") - 0.3, 0.5), ("pop.mp3", A("guess", "few million") - 0.3, 0.5), ("pop.mp3", A("guess", "or billions") - 0.1, 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("day", "replaced"), 0.5),
        ("impact-bass-1.mp3", A("day", "three hundred"), 0.45), ("click.mp3", A("second", "three point"), 0.45),
        ("ping.mp3", A("who", "nine out"), 0.4), ("impact-bass-2.mp3", A("mass", "two eggs") - 0.2, 0.45),
        ("click.mp3", A("myth", "not quite"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
