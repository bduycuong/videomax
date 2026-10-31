# MAX WISE ep23 — Why do your fingers wrinkle in water?
# Kit: ink / morph / along helpers; one three.js scene (a treaded tire rolling on a wet road).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#FFD9B8"; WATER = "#BFE3F7"

def wavy(x0, x1, y, n, a):
    """wavy line with n humps from x0 to x1 (same start point as the flat line)"""
    step = (x1 - x0) / (2 * n); d = f"M{x0},{y}"
    for i in range(2 * n):
        d += f" Q{x0 + step*(i+0.5):.0f},{y - a if i % 2 == 0 else y + a} {x0 + step*(i+1):.0f},{y}"
    return d
def flat(x0, x1, y, n):
    step = (x1 - x0) / (2 * n); d = f"M{x0},{y}"
    for i in range(2 * n):
        d += f" Q{x0 + step*(i+0.5):.0f},{y} {x0 + step*(i+1):.0f},{y}"
    return d

# 1 HOOK — fingertip in the bath; flat lines morph into wrinkles; a raisin pops beside it
s = "hook"; tb = aw(s, "bath"); tw = aw(s, "wrinkle"); tr = aw(s, "raisins"); tq = aw(s, "but why")
lines = [(370, 530, 330, 3), (360, 540, 390, 3), (360, 540, 450, 3), (370, 530, 510, 3)]
fl = "".join(f'<path id="hk-w{i}" d="{flat(*l)}" stroke="{C["pencil"]}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".35"/>' for i, l in enumerate(lines))
wv = "".join(f'<path id="hk-v{i}" d="{wavy(*l, 14)}" fill="none" stroke="none"/>' for i, l in enumerate(lines))
scenes[s] = scene_file(s, f"""
#hk-svg {{ position:absolute; left:0; top:140px; }}
#hk-q {{ top:780px; font-size:84px; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="640" viewBox="0 0 {W} 640" data-layout-ignore>
    <path id="hk-tub" d="M80,520 L1000,520 L960,630 L120,630 Z" fill="{WATER}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path id="hk-fin" d="M330,600 L330,320 Q330,230 450,230 Q570,230 570,320 L570,600" fill="{SKIN}" stroke="{K}" stroke-width="7"/>
    <path d="M90,540 Q160,525 230,540 Q300,555 370,540" stroke="#FFFFFF" stroke-width="8" fill="none" stroke-linecap="round"/>
    {fl}{wv}
    <g id="hk-rai"><ellipse cx="800" cy="360" rx="100" ry="80" fill="#7A3E5C" stroke="{K}" stroke-width="7"/>
      <path d="M730,330 Q760,350 740,380 M790,300 Q810,340 790,390 M840,320 Q860,360 850,410" stroke="#4A2236" stroke-width="6" fill="none" stroke-linecap="round"/></g>
  </svg>
  <div id="hk-q" class="h1"><span class="hl">But why?</span></div>
""", J("""
pop("#hk-tub", @tb, {from:{scaleY:0.6}, to:{}});
tl.fromTo("#hk-fin", {y:200, opacity:0}, {y:0, opacity:1, duration:0.5, ease:"back.out(1.6)"}, @tb2);
tl.fromTo("[id^=hk-w]", {opacity:0}, {opacity:0.35, duration:0.3}, @tb3);
""" + "".join(f'morph("#hk-w{i}", "#hk-v{i}", @tw + {i*0.08:.2f}, 0.6);' for i in range(4)) + """
tl.to("[id^=hk-w]", {opacity:1, stroke:"#262A3B", duration:0.4}, @tw);
pop("#hk-rai", @tr, {from:{rotation:-20, transformOrigin:"50% 50%"}, to:{rotation:0}});
pop("#hk-q", @tq, {from:{scale:1.5}, to:{}});
""", tb=tb - 0.6, tb2=tb - 0.2, tb3=tb + 0.3, tw=tw - 0.2, tr=tr - 0.1, tq=tq - 0.05))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "your skin drinks"); t2 = aw(s, "gets tired"); t3 = aw(s, "or your")
notes = [("a", "skin drinks water?", -6, 110, C['hi']), ("b", "skin gets tired?", 4, 405, "#BFE3F7"), ("c", "nerves on purpose?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:60px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.1, t2=t2 - 0.5, t3=t3 - 0.1))

# 3 INTRO — logo + bubbles ink themselves
s = "intro"; tmw = aw(s, "Max Wise"); tbt = aw(s, "bottom")
bub = "".join(f'<circle class="in-bb" cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{C["blue"]}" stroke-width="5"/>' for x, y, r in [(200, 90, 26), (280, 40, 16), (820, 80, 30), (900, 30, 14), (760, 30, 10)])
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:62px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <svg class="abs" style="left:0;top:480px" width="{W}" height="140" data-layout-ignore>{bub}</svg>
  <div id="in-sub" class="h1"><span class="hl">Bottom of the bath!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tb); ink(".in-bb", @tb, 0.3, {stagger:0.08});
""", tmw=tmw, tu=tmw + 0.3, tb=tbt - 0.5))

# 4 MYTH — sponge swells with drops; the popular idea crossed out
s = "myth"; tsoak = aw(s, "soaks up"); tsw = aw(s, "swells"); tnq = aw(s, "not quite")
drops = "".join(f'<path class="my-dr" d="M{x},{y} Q{x+16},{y+30} {x},{y+40} Q{x-16},{y+30} {x},{y} Z" fill="{WATER}" stroke="{K}" stroke-width="4"/>' for x, y in [(420, 20), (540, 0), (660, 30)])
scenes[s] = scene_file(s, f"""
#my-svg {{ position:absolute; left:0; top:160px; }}
#my-t {{ position:absolute; left:0; right:0; top:610px; text-align:center; {GH} font-size:64px; color:{C['pencil']}; }}
#my-nq {{ position:absolute; left:0; right:0; top:730px; text-align:center; opacity:0; }}
""", f"""
  <svg id="my-svg" width="{W}" height="460" viewBox="0 0 {W} 460" data-layout-ignore>
    {drops}
    <g id="my-sp"><rect x="370" y="140" width="340" height="230" rx="30" fill="#FFE27A" stroke="{K}" stroke-width="7"/>
      <circle cx="450" cy="210" r="16" fill="#E6C34A"/><circle cx="560" cy="270" r="22" fill="#E6C34A"/><circle cx="640" cy="200" r="12" fill="#E6C34A"/><circle cx="470" cy="310" r="12" fill="#E6C34A"/></g>
  </svg>
  <div id="my-t">"skin soaks up water"</div>
  <svg class="abs" style="left:0;top:600px" width="{W}" height="100" data-layout-ignore>
    <path id="my-x" d="M150,60 L930,40" stroke="{C['red']}" stroke-width="10" stroke-linecap="round" fill="none"/></svg>
  <div id="my-nq"><span class="chip" style="background:#FFC9C2">not quite!</span></div>
""", J("""
pop("#my-sp", 0.2, {from:{rotation:-8, transformOrigin:"50% 50%"}, to:{rotation:0}});
tl.fromTo(".my-dr", {y:-60, opacity:0}, {y:110, opacity:1, duration:0.5, ease:"power2.in", stagger:0.15}, @tso);
tl.to("#my-sp", {scale:1.18, svgOrigin:"540 255", duration:0.6, ease:"back.out(2)"}, @tsw);
rise("#my-t", @tso);
ink("#my-x", @tnq, 0.3); tl.set("#my-nq", {opacity:1}, @tnq2); pop("#my-nq .chip", @tnq2, {from:{rotation:-14}, to:{rotation:-4}});
""", tso=tsoak - 0.3, tsw=tsw - 0.2, tnq=tnq - 0.2, tnq2=tnq + 0.1))

# 5 NERVES — two finger cards: healthy nerve → wrinkles; damaged nerve → smooth
s = "nerves"; t30 = aw(s, "nineteen thirties"); tdam = aw(s, "damaged nerves"); tnot = aw(s, "not wrinkle")
def finger(px, cls):
    return (f'<path d="M{px},560 L{px},170 Q{px},90 {px+90},90 Q{px+180},90 {px+180},170 L{px+180},560" fill="{SKIN}" stroke="{K}" stroke-width="7"/>'
            f'<path id="{cls}-n" d="M{px+90},560 L{px+90},150" stroke="#E6B800" stroke-width="10" fill="none" stroke-linecap="round"/>')
wr = "".join(f'<path class="nv-wr" d="{wavy(150, 290, y, 3, 12)}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>' for y in (150, 200, 250))
scenes[s] = scene_file(s, f"""
#nv-y {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#nv-svg {{ position:absolute; left:0; top:250px; }}
.nv-l {{ position:absolute; top:262px; width:360px; text-align:center; {GH} font-size:48px; opacity:0; }}
#nv-l1 {{ left:440px; }} #nv-l2 {{ left:600px; color:{C['red']}; }}
""", f"""
  <div id="nv-y"><span class="chip">1930s</span></div>
  <svg id="nv-svg" width="{W}" height="600" viewBox="0 0 {W} 600" data-layout-ignore>
    <g id="nv-f1" transform="translate(-20,0)">{finger(130, "nv1")}{wr}</g>
    <g id="nv-f2">{finger(690, "nv2")}
      <path id="nv-cut" d="M740,330 L820,410 M820,330 L740,410" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/></g>
  </svg>
  <div id="nv-l1" class="nv-l" style="left:20px">wrinkles</div>
  <div id="nv-l2" class="nv-l">stays smooth!</div>
""", J("""
pop("#nv-y .chip", @t30, {from:{rotation:-14}, to:{rotation:-3}});
pop("#nv-f1", @tf, {from:{x:-60}, to:{}}); pop("#nv-f2", @tf, {from:{x:60}, to:{}});
ink("#nv1-n", @tn1, 0.5); ink("#nv2-n", @tn1, 0.5);
ink(".nv-wr", @tn2, 0.25, {stagger:0.12}); tl.to("#nv-l1", {opacity:1, duration:0.2}, @tn2);
ink("#nv-cut", @tdam, 0.35);
tl.to("#nv2-n", {opacity:0.25, duration:0.3}, @tdam2);
tl.set("#nv-l2", {opacity:1}, @tnot); pop("#nv-l2", @tnot);
""", t30=t30, tf=t30 + 0.4, tn1=t30 + 0.8, tn2=t30 + 1.4, tdam=tdam - 0.1, tdam2=tdam + 0.3, tnot=tnot - 0.2))

# 6 VESSELS — fingertip cutaway: a signal runs along the nerve, vessels squeeze thinner
s = "vessels"; tch = aw(s, "in charge"); tsq = aw(s, "squeezes"); tves = aw(s, "blood vessels")
vs = "".join(f'<rect class="vs-v" x="{220 + i*150}" y="420" width="70" height="300" rx="35" fill="#F28B82" stroke="{K}" stroke-width="5"/>' for i in range(5))
scenes[s] = scene_file(s, f"""
#vs-svg {{ position:absolute; left:0; top:120px; }}
#vs-chip {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#vs-sq {{ position:absolute; left:640px; top:860px; {GH} font-size:62px; color:{C['red']}; opacity:0; }}
""", f"""
  <svg id="vs-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    <path d="M120,760 L120,360 Q120,180 540,180 Q960,180 960,360 L960,760" fill="{SKIN}" stroke="{K}" stroke-width="7"/>
    <path id="vs-nerve" d="M60,740 C160,640 140,330 540,300 C760,285 860,330 900,360" stroke="#E6B800" stroke-width="12" fill="none" stroke-linecap="round"/>
    {vs}
    <g id="vs-sig"><circle r="20" fill="#FFF3A0" stroke="{K}" stroke-width="4"/><path d="M-8,-4 L2,-4 L-4,8 L8,-2 L-2,-2 L4,-12" stroke="{K}" stroke-width="3" fill="none"/></g>
  </svg>
  <div id="vs-chip"><span class="chip">nervous system: in charge</span></div>
  <div id="vs-sq">squeeze!</div>
""", J("""
ink("#vs-nerve", 0.1, 0.8);
tl.fromTo(".vs-v", {opacity:0, scaleY:0.3, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.3, ease:"back.out(2)", stagger:0.08}, @tv0);
tl.set("#vs-chip", {opacity:1}, @tch); pop("#vs-chip .chip", @tch);
tl.fromTo("#vs-sig", {opacity:0}, {opacity:1, duration:0.1}, @ts0);
along("#vs-sig", "#vs-nerve", @ts0, 1.4, {ease:"power1.in"});
tl.to(".vs-v", {scaleX:0.45, transformOrigin:"50% 50%", duration:0.6, ease:"back.out(1.6)", stagger:0.06}, @tsq);
tl.set("#vs-sq", {opacity:1}, @tsq); pop("#vs-sq", @tsq, {from:{rotation:-12, scale:1.8}, to:{rotation:-5}});
""", tv0=0.6, tch=tch - 0.4, ts0=tsq - 1.5, tsq=tsq - 0.1))

# 7 FOLD — padding shrinks; one skin line morphs from flat to ridges and valleys
s = "fold"; tpad = aw(s, "soft padding"); tshr = aw(s, "shrinks"); trv = aw(s, "ridges and valleys")
scenes[s] = scene_file(s, f"""
#fd-svg {{ position:absolute; left:0; top:160px; }}
.fd-lab {{ position:absolute; {GH} font-size:46px; padding:0 18px; background:#FFF3C4; border:3px solid {K}; transform:rotate(-3deg); opacity:0; }}
#fd-l1 {{ left:150px; top:200px; }} #fd-l2 {{ left:640px; top:200px; background:{WATER}; }}
#fd-pl {{ position:absolute; left:0; right:0; top:700px; text-align:center; opacity:0; }}
""", f"""
  <svg id="fd-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <rect id="fd-pad" x="100" y="300" width="880" height="230" fill="#FFE9D6" stroke="{K}" stroke-width="5" stroke-dasharray="14 10"/>
    <path d="M100,300 L100,560 L980,560 L980,300" stroke="{K}" stroke-width="0" fill="none"/>
    <path id="fd-skin" d="{flat(100, 980, 300, 5)}" stroke="{K}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path id="fd-wv" d="{wavy(100, 980, 300, 5, 70)}" fill="none" stroke="none"/>
    <path id="fd-ld1" d="M250,130 L188,240" stroke="{K}" stroke-width="4" fill="none"/>
    <path id="fd-ld2" d="M740,130 L716,330" stroke="{K}" stroke-width="4" fill="none"/>
  </svg>
  <div id="fd-l1" class="fd-lab">ridge</div>
  <div id="fd-l2" class="fd-lab">valley</div>
  <div id="fd-pl"><span class="chip" style="background:#FFE9D6">padding shrinks a little</span></div>
""", J("""
ink("#fd-skin", 0.05, 0.6);
tl.fromTo("#fd-pad", {opacity:0}, {opacity:1, duration:0.3}, @tp);
tl.to("#fd-pad", {scaleY:0.82, svgOrigin:"540 530", duration:0.7, ease:"power2.inOut"}, @ts);
tl.set("#fd-pl", {opacity:1}, @ts); pop("#fd-pl .chip", @ts);
morph("#fd-skin", "#fd-wv", @tm, 0.8, {ease:"back.out(1.4)"});
tl.to("#fd-l1", {opacity:1, duration:0.2}, @trv); ink("#fd-ld1", @trv, 0.3);
tl.to("#fd-l2", {opacity:1, duration:0.2}, @trv2); ink("#fd-ld2", @trv2, 0.3);
""", tp=tpad - 0.2, ts=tshr - 0.2, tm=tshr + 0.3, trv=trv - 0.1, trv2=trv + 0.6))

# 8 TIRE — three.js: a treaded tire rolls on a wet road; drops fling off behind it
s = "tire"; ttr = aw(s, "tread on"); tch2 = aw(s, "channels water"); tgrip = aw(s, "wet road"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#tr-cv {{ position:absolute; left:40px; top:140px; width:1000px; height:680px; }}
#tr-c1 {{ position:absolute; left:620px; top:170px; opacity:0; }}
#tr-c2 {{ position:absolute; left:470px; top:830px; opacity:0; }}
""", f"""
  <canvas id="tr-cv" width="1000" height="680"></canvas>
  <div id="tr-c1"><span class="chip">tread</span></div>
  <div id="tr-c2"><span class="chip" style="background:{WATER}">grip on wet roads</span></div>
""", J("""
const S = T3.stage("#tr-cv", 1000, 680, 30);
const tire = new THREE.Group(); S.scene.add(tire);
tire.add(T3.inked(new THREE.TorusGeometry(1.7, 0.62, 24, 72), 0x3A3F4F, 0.03));
const hub = T3.inked(new THREE.CylinderGeometry(1.05, 1.05, 0.5, 40), 0xD8DCE6, 0.04); hub.rotation.x = Math.PI/2; tire.add(hub);
for (let i = 0; i < 28; i++) { const a = i / 28 * Math.PI * 2;
  const b = new THREE.Mesh(new THREE.BoxGeometry(0.28, 0.16, 0.9), T3.toon(0x23262F));
  b.position.set(Math.cos(a) * 2.32, Math.sin(a) * 2.32, 0); b.rotation.z = a; b.rotation.y = (i % 2 ? 0.35 : -0.35); tire.add(b); }
tire.position.y = 0.3;
const road = new THREE.Mesh(new THREE.BoxGeometry(14, 0.2, 4), T3.toon(0x8EC5E8)); road.position.y = -2.15; S.scene.add(road);
const R = T3.seeded(23); const drops = [];
for (let i = 0; i < 26; i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.1 + 0.06*R(), 10, 8), new THREE.MeshBasicMaterial({color:0x2F8FD8}));
  m.userData = {ph: R(), vx: 1.5 + 2*R(), vy: 2 + 2*R(), z: (R() - 0.5) * 1.6}; S.scene.add(m); drops.push(m); }
S.cam.position.set(2.5, 1.6, 10.5); S.cam.lookAt(0, -0.2, 0);
drive(@d, t => { tire.rotation.z = -1.6 * t;
  const on = Math.min(1, Math.max(0, (t - @tw) / 0.4));
  drops.forEach(m => { const u = ((t * 0.9 + m.userData.ph) % 1); const tt = u * 0.9;
    m.position.set(-1.8 - m.userData.vx * tt, -2.0 + m.userData.vy * tt - 4.9 * tt * tt, m.userData.z);
    m.visible = on > 0 && m.position.y > -2.1; m.scale.setScalar(on || 0.001); });
  S.render(); });
tl.set("#tr-c1", {opacity:1}, @tt); pop("#tr-c1 .chip", @tt, {from:{rotation:-12}, to:{rotation:-4}});
tl.set("#tr-c2", {opacity:1}, @tg); pop("#tr-c2 .chip", @tg, {from:{rotation:10}, to:{rotation:3}});
""", d=d, tw=tch2 - 0.2, tt=ttr - 0.1, tg=tgrip - 0.3))

# 9 TEST — 2013 chip, 30 min timer, marbles hop from box A to box B (seeded)
s = "test"; t13 = aw(s, "two thousand thirteen"); t30m = aw(s, "thirty minutes"); tmar = aw(s, "wet marbles")
rnd = random.Random(13)
mars = ""
for i in range(8):
    x, y = 210 + (i % 4) * 46 + rnd.uniform(-4, 4), 560 - (i // 4) * 44
    mars += f'<circle class="ts-m" id="ts-m{i}" cx="{x:.0f}" cy="{y:.0f}" r="20" fill="{["#7DB6E8","#F28B82","#9BD08F","#FFE27A"][i%4]}" stroke="{K}" stroke-width="4"/>'
scenes[s] = scene_file(s, f"""
#ts-y {{ position:absolute; left:110px; top:150px; }}
#ts-svg {{ position:absolute; left:0; top:140px; }}
#ts-t {{ position:absolute; left:600px; top:150px; {GH} font-size:52px; opacity:0; }}
""", f"""
  <div id="ts-y"><span class="chip">2013 test</span></div>
  <div id="ts-t"><span class="chip" style="background:{WATER}">soak: 30 min</span></div>
  <svg id="ts-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <g transform="translate(860,330)"><circle r="0" fill="none"/></g>
    <path id="ts-ba" d="M170,480 L170,600 L410,600 L410,480" stroke="{K}" stroke-width="7" fill="#FFF3DD" stroke-linejoin="round"/>
    <path id="ts-bb" d="M670,480 L670,600 L910,600 L910,480" stroke="{K}" stroke-width="7" fill="#FFF3DD" stroke-linejoin="round"/>
    <text x="290" y="660" text-anchor="middle" style="{GH}font-size:40px" fill="{C['muted']}">box A</text>
    <text x="790" y="660" text-anchor="middle" style="{GH}font-size:40px" fill="{C['muted']}">box B</text>
    {mars}
    <path id="ts-arc" d="M300,440 Q540,200 780,440" stroke="{C['pencil']}" stroke-width="5" stroke-dasharray="12 10" fill="none"/>
  </svg>
""", J("""
pop("#ts-y .chip", @t13, {from:{rotation:-12}, to:{rotation:-3}});
tl.set("#ts-t", {opacity:1}, @t30); pop("#ts-t .chip", @t30, {from:{rotation:10}, to:{rotation:3}});
ink("#ts-ba", @tbx, 0.4); ink("#ts-bb", @tbx2, 0.4);
tl.fromTo(".ts-m", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, ease:"back.out(2)", stagger:0.04}, @tbx2);
ink("#ts-arc", @tm0, 0.4);
for (let i = 0; i < 8; i++) { const t = @tm + i * 0.28;
  tl.to("#ts-m" + i, {x:500, duration:0.45, ease:"none"}, t);
  tl.to("#ts-m" + i, {y:-220, duration:0.225, ease:"power1.out", yoyo:true, repeat:1}, t); }
""", t13=t13 - 0.1, t30=t30m - 0.2, tbx=t13 + 0.6, tbx2=t13 + 0.9, tm0=tmar - 0.5, tm=tmar - 0.2))

# 10 RESULT — time bars: wet (smooth vs wrinkly, ≈12% faster) and dry (equal)
s = "result"; t12 = aw(s, "twelve percent"); tdry = aw(s, "dry objects"); tnd = aw(s, "no difference")
L = 520; Lw = round(L * 0.88)
scenes[s] = scene_file(s, f"""
#rs-svg {{ position:absolute; left:0; top:140px; }}
#rs-n {{ position:absolute; left:630px; top:300px; width:430px; text-align:center; opacity:0; }}
#rs-n .big {{ font-size:76px; color:{C['red']}; }}
#rs-nd {{ position:absolute; left:600px; top:640px; width:440px; text-align:center; opacity:0; }}
""", f"""
  <svg id="rs-svg" width="{W}" height="740" viewBox="0 0 {W} 740" data-layout-ignore>
    <text x="80" y="40" style="{GH}font-size:50px" fill="{C['blue']}">wet marbles</text>
    <text x="80" y="110" style="{GH}font-size:38px" fill="{K}">smooth</text>
    <rect id="rs-w1" x="80" y="125" width="{L}" height="56" fill="#E8E2D6" stroke="{K}" stroke-width="5"/>
    <text x="80" y="235" style="{GH}font-size:38px" fill="{K}">wrinkly</text>
    <rect id="rs-w2" x="80" y="250" width="{Lw}" height="56" fill="{SKIN}" stroke="{K}" stroke-width="5"/>
    <text x="80" y="420" style="{GH}font-size:50px" fill="{C['muted']}">dry objects</text>
    <text x="80" y="490" style="{GH}font-size:38px" fill="{K}">smooth</text>
    <rect id="rs-d1" x="80" y="505" width="{L}" height="56" fill="#E8E2D6" stroke="{K}" stroke-width="5"/>
    <text x="80" y="615" style="{GH}font-size:38px" fill="{K}">wrinkly</text>
    <rect id="rs-d2" x="80" y="630" width="{L}" height="56" fill="{SKIN}" stroke="{K}" stroke-width="5"/>
    <text x="{80+L}" y="110" text-anchor="end" style="{GH}font-size:32px" fill="{C['muted']}">time taken</text>
  </svg>
  <div id="rs-n"><span class="big">≈ 12% faster</span></div>
  <div id="rs-nd"><span class="chip" style="background:#FFFFFF">no difference</span></div>
""", J("""
tl.fromTo("#rs-w1,#rs-w2", {scaleX:0}, {scaleX:1, svgOrigin:"80 0", duration:0.8, ease:"power2.out", stagger:0.15}, 0.2);
tl.set("#rs-n", {opacity:1}, @t12); pop("#rs-n .big", @t12);
tl.fromTo("#rs-d1,#rs-d2", {scaleX:0}, {scaleX:1, svgOrigin:"80 0", duration:0.8, ease:"power2.out"}, @td);
tl.set("#rs-nd", {opacity:1}, @tnd); pop("#rs-nd .chip", @tnd, {from:{rotation:-10}, to:{rotation:-3}});
""", t12=t12 - 0.1, td=tdry - 0.4, tnd=tnd - 0.2))

# 11 DEBATE — shaded "maybe" band with question marks
s = "debate"; tne = aw(s, "not every"); tdb = aw(s, "debate goes")
qs = "".join(f'<text class="db-q" x="{x}" y="{y}" style="{GH}font-size:{fs}px" fill="{C["blue"]}">?</text>' for x, y, fs in [(170, 220, 110), (820, 200, 130), (520, 120, 90), (330, 610, 80), (760, 610, 100)])
scenes[s] = scene_file(s, f"""
#db-svg {{ position:absolute; left:0; top:150px; }}
#db-c {{ position:absolute; left:0; right:0; top:600px; text-align:center; opacity:0; }}
""", f"""
  <svg id="db-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <rect id="db-band" x="140" y="250" width="800" height="150" fill="#FFE27A" fill-opacity=".55" stroke="{K}" stroke-width="5" stroke-dasharray="16 10"/>
    <text x="540" y="345" text-anchor="middle" style="{GH}font-size:70px" fill="{K}">better grip?  maybe</text>
    {qs}
  </svg>
  <div id="db-c"><span class="chip" style="background:#FFFFFF">later studies: mixed</span></div>
""", J("""
tl.fromTo("#db-band", {opacity:0}, {opacity:1, duration:0.4}, 0.1);
tl.fromTo("#db-svg text:not(.db-q)", {opacity:0}, {opacity:1, duration:0.3}, 0.4);
tl.set("#db-c", {opacity:1}, @tne); pop("#db-c .chip", @tne, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo(".db-q", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.3, ease:"back.out(2.4)", stagger:0.12}, @tdb);
""", tne=tne, tdb=tdb - 0.4))

# 12 OUTRO — callback: rain tires for your fingers (Max centre stage, keep y < 620)
s = "outro"; trt = aw(s, "rain tires"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:170px; text-align:center; }}
#ou-sc {{ top:400px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:54px;background:{WATER}">rain tires for your fingers?</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a .chip", @ta, {from:{rotation:-10}, to:{rotation:-3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", ta=trt - 0.3, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "but why"), SC["guess"]["start"] + 0.2)
point(g("guess", "your skin drinks"), 3.0)
wave(g("intro", "I'm Max"))
think(g("myth", "most people"), g("myth", "not quite"))
wow(g("nerves", "not wrinkle"), 1.2)
point(g("vessels", "squeezes"), 1.2)
point(g("fold", "ridges and"), 1.2)
point(g("tire", "wet road"), 1.2)
point(g("test", "wet marbles"), 1.4)
wow(g("result", "twelve percent"), 1.2)
think(g("debate", "not every"), SC["outro"]["start"])
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "raisins"), 0.5), ("sparkle.mp3", A("hook", "wrinkle"), 0.35),
        ("pop.mp3", A("guess", "your skin drinks"), 0.45), ("pop.mp3", A("guess", "gets tired") - 0.4, 0.45), ("pop.mp3", A("guess", "or your"), 0.5),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("myth", "not quite"), 0.45),
        ("impact-bass-1.mp3", A("nerves", "not wrinkle"), 0.4), ("riser.mp3", A("vessels", "squeezes") - 1.4, 0.3),
        ("click-soft.mp3", A("fold", "ridges and"), 0.45), ("whoosh-short.mp3", A("tire", "channels water"), 0.4),
        ("click.mp3", A("test", "wet marbles"), 0.4), ("ping.mp3", A("result", "twelve percent"), 0.45),
        ("pop.mp3", A("debate", "debate goes"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
