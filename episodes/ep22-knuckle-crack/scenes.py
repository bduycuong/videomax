# MAX WISE ep22 — What actually makes the "pop" when you crack your knuckles?
# Kit: ink / morph / along helpers; one three.js scene (bones sliding apart inside the joint capsule).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#FFD9B8"; BONE = "#FFF6E0"; FLUID = "#BFE3F7"

# 1 HOOK — a doodle finger draws itself, bends, POP!
s = "hook"; tpull = aw(s, "pull"); tbend = aw(s, "bend"); tpop = aw(s, "pop"); tq = aw(s, "what is")
scenes[s] = scene_file(s, f"""
#hk-svg {{ position:absolute; left:0; top:150px; }}
#hk-pop {{ position:absolute; left:600px; top:250px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
#hk-q {{ top:760px; font-size:70px; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="600" viewBox="0 0 {W} 600" data-layout-ignore>
    <path id="hk-palm" d="M120,560 L120,330 Q120,290 160,290 L340,290 L340,372 L420,372 L420,560 Z" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linecap="round"/>
    <g transform="translate(330,290)"><g id="hk-fin">
      <path d="M0,0 L220,0 Q262,0 262,40 Q262,80 220,80 L0,80" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
      <path d="M120,18 Q128,40 120,62 M140,18 Q148,40 140,62" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
      <path d="M215,14 Q240,14 240,40" stroke="{K}" stroke-width="4" fill="none"/>
    </g></g>
    <path id="hk-burst" d="M600,170 L640,120 M660,200 L730,180 M590,110 L590,50 M540,140 L500,100" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="hk-pop">POP!</div>
  <div id="hk-q" class="h1">What makes that <span class="hl">crack</span>?</div>
""", J("""
pop("#hk-palm", 0.05, {from:{scale:0.8}, to:{}});
tl.fromTo("#hk-fin", {opacity:0}, {opacity:1, duration:0.3}, @tp);
tl.to("#hk-fin", {rotation:8, svgOrigin:"0 40", duration:0.3, ease:"power2.out"}, @tp2);
tl.to("#hk-fin", {rotation:-28, svgOrigin:"0 40", duration:0.3, ease:"back.out(2)"}, @tb);
tl.set("#hk-pop", {opacity:1}, @tpop); pop("#hk-pop", @tpop, {from:{rotation:-20, scale:2}, to:{rotation:-8}});
ink("#hk-burst", @tpop, 0.25);
rise("#hk-q", @tq);
""", tp=0.3, tp2=tpull, tb=tbend, tpop=tpop - 0.05, tq=tq - 0.2))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "bones rubbing"); t2 = aw(s, "a bubble bursting"); t3 = aw(s, "or a")
notes = [("a", "bones rubbing?", -6, 110, C['hi']), ("b", "bubble bursting?", 4, 405, "#BFE3F7"), ("c", "bubble being born?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:60px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.1, t2=t2 - 0.1, t3=t3 - 0.1))

# 3 INTRO — logo + magnifier inks itself
s = "intro"; tmw = aw(s, "Max Wise"); tin = aw(s, "inside")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
#in-svg {{ position:absolute; left:400px; top:500px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Inside a knuckle!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @ti);
""", tmw=tmw, tu=tmw + 0.3, ti=tin - 0.3))

# 4 JOINT — cutaway: two bones, capsule, fluid; tape labels with leader lines
s = "joint"; tb = aw(s, "two finger bones"); tc = aw(s, "tiny capsule"); tf = aw(s, "slippery")
scenes[s] = scene_file(s, f"""
#jt-svg {{ position:absolute; left:0; top:150px; }}
.jt-lab {{ position:absolute; {GH} font-size:46px; padding:0 18px; background:#FFF3C4; border:3px solid {K}; transform:rotate(-3deg); opacity:0; }}
#jt-l1 {{ left:90px; top:200px; }} #jt-l2 {{ left:720px; top:200px; background:#FFC9C2; }} #jt-l3 {{ left:600px; top:760px; background:{FLUID}; }}
""", f"""
  <svg id="jt-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    <path id="jt-cut" d="M60,60 L1020,60" stroke="{C['pencil']}" stroke-width="5" stroke-dasharray="18 14" fill="none"/>
    <path id="jt-fl" d="M440,250 Q540,190 640,250 L640,450 Q540,510 440,450 Z" fill="{FLUID}" stroke="none" opacity="0"/>
    <path id="jt-b1" d="M100,280 L430,270 Q500,300 500,350 Q500,400 430,430 L100,420 Q70,350 100,280 Z" fill="{BONE}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path id="jt-b2" d="M980,280 L650,270 Q580,290 585,350 Q580,410 650,430 L980,420 Q1010,350 980,280 Z" fill="{BONE}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path id="jt-cap" d="M400,240 Q540,150 680,240 L680,460 Q540,550 400,460 Z" fill="none" stroke="{C['red']}" stroke-width="7" stroke-linejoin="round"/>
    <path id="jt-ld1" d="M260,110 L260,300" stroke="{K}" stroke-width="4" fill="none"/>
    <path id="jt-ld2" d="M820,110 L660,215" stroke="{K}" stroke-width="4" fill="none"/>
    <path id="jt-ld3" d="M700,610 L560,420" stroke="{K}" stroke-width="4" fill="none"/>
  </svg>
  <div id="jt-l1" class="jt-lab">bone</div>
  <div id="jt-l2" class="jt-lab">capsule</div>
  <div id="jt-l3" class="jt-lab">joint fluid</div>
""", J("""
ink("#jt-cut", 0.05, 0.5);
pop("#jt-b1", @tb, {from:{x:-60}, to:{}}); pop("#jt-b2", @tb2, {from:{x:60}, to:{}});
tl.to("#jt-l1", {opacity:1, duration:0.2}, @tb3); ink("#jt-ld1", @tb3, 0.3);
ink("#jt-cap", @tc, 0.8);
tl.to("#jt-l2", {opacity:1, duration:0.2}, @tc2); ink("#jt-ld2", @tc2, 0.3);
tl.to("#jt-fl", {opacity:0.9, duration:0.6}, @tf);
tl.to("#jt-l3", {opacity:1, duration:0.2}, @tf2); ink("#jt-ld3", @tf2, 0.3);
""", tb=tb - 0.2, tb2=tb + 0.1, tb3=tb + 0.4, tc=tc - 0.2, tc2=tc + 0.5, tf=tf - 0.2, tf2=tf + 0.3))

# 5 PULL — three.js: bones slide apart inside a see-through fluid capsule; pressure gauge drops
s = "pull"; tsl = aw(s, "slide apart"); tdr = aw(s, "drops fast"); tsp = aw(s, "the space"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#pl-cv {{ position:absolute; left:40px; top:140px; width:1000px; height:560px; }}
#pl-g {{ position:absolute; left:560px; top:700px; }}
#pl-gl {{ position:absolute; left:440px; top:900px; width:400px; text-align:center; {GH} font-size:46px; opacity:0; }}
#pl-arr {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:54px; opacity:0; }}
""", f"""
  <canvas id="pl-cv" width="1000" height="560"></canvas>
  <div id="pl-arr"><span class="chip">&larr; pull &rarr;</span></div>
  <svg id="pl-g" width="320" height="200" viewBox="0 0 320 200" data-layout-ignore>
    <path id="pl-dial" d="M30,180 A130,130 0 0 1 290,180" fill="#FFFFFF" stroke="{K}" stroke-width="7"/>
    <path d="M60,150 L76,160 M160,62 L160,80 M260,150 L244,160" stroke="{K}" stroke-width="5"/>
    <g id="pl-nd"><path d="M160,180 L250,110" stroke="{C['red']}" stroke-width="9" stroke-linecap="round"/></g>
    <circle cx="160" cy="180" r="12" fill="{K}"/>
  </svg>
  <div id="pl-gl">pressure drops</div>
""", J("""
const S = T3.stage("#pl-cv", 1000, 560, 30);
const bone = x => { const g = T3.inked(new THREE.CapsuleGeometry(0.55, 2.4, 8, 24), 0xFFF0D0, 0.05); g.rotation.z = Math.PI/2; g.position.x = x; S.scene.add(g); return g; };
const b1 = bone(-1.75), b2 = bone(1.75);
const fl = new THREE.Mesh(new THREE.SphereGeometry(1, 40, 24), new THREE.MeshBasicMaterial({color:0x9FD4F5, transparent:true, opacity:0.45, depthWrite:false}));
fl.scale.set(1.0, 0.85, 0.85); S.scene.add(fl);
const ring = new THREE.Mesh(new THREE.TorusGeometry(1, 0.02, 8, 80), new THREE.MeshBasicMaterial({color:0xE0483C})); ring.rotation.y = Math.PI/2; ring.scale.set(0.85, 0.85, 0.85); S.scene.add(ring);
const sm = k => { k = Math.min(1, Math.max(0, k)); return k*k*(3-2*k); };
drive(@d, t => { const g = 0.45 * sm((t - @ts)/1.2);
  b1.position.x = -1.75 - g; b2.position.x = 1.75 + g; fl.scale.x = 1.0 + g*0.9;
  S.cam.position.set(9.6*Math.sin(0.12 + 0.03*t), 1.5, 9.6*Math.cos(0.12 + 0.03*t)); S.cam.lookAt(0, 0, 0); S.render(); });
tl.set("#pl-arr", {opacity:1}, @ts); pop("#pl-arr .chip", @ts);
tl.to("#pl-nd", {rotation:-110, svgOrigin:"160 180", duration:0.6, ease:"back.out(1.5)"}, @tdr);
tl.to("#pl-gl", {opacity:1, duration:0.2}, @tdr);
""", d=d, ts=tsl - 0.2, tdr=tdr - 0.3))

# 6 CAVITY — the gap morphs into a gas bubble; a suction cup pops off a window
s = "cavity"; tgas = aw(s, "gas pocket"); tsuc = aw(s, "suction cup"); tpo = aw(s, "popping off")
scenes[s] = scene_file(s, f"""
#cv-svg {{ position:absolute; left:0; top:150px; }}
#cv-l {{ position:absolute; left:110px; top:640px; width:420px; text-align:center; opacity:0; }}
#cv-pop {{ position:absolute; left:700px; top:160px; {GH} font-size:90px; color:{C['red']}; opacity:0; }}
""", f"""
  <svg id="cv-svg" width="{W}" height="720" viewBox="0 0 {W} 720" data-layout-ignore>
    <path d="M40,200 L220,195 Q260,230 260,290 Q260,350 220,385 L40,380 Z" fill="{BONE}" stroke="{K}" stroke-width="6"/>
    <path d="M520,200 L340,195 Q300,230 300,290 Q300,350 340,385 L520,380 Z" fill="{BONE}" stroke="{K}" stroke-width="6"/>
    <path id="cv-gap" d="M270,240 L290,240 L290,340 L270,340 Z" fill="#FFFFFF" stroke="{K}" stroke-width="4"/>
    <path id="cv-bub" d="M280,215 C325,215 345,255 345,290 C345,325 325,365 280,365 C235,365 215,325 215,290 C215,255 235,215 280,215 Z" fill="none" stroke="none"/>
    <path id="cv-win" d="M640,80 L1000,80 L1000,560 L640,560 Z" fill="#E6F3FB" stroke="{K}" stroke-width="7"/>
    <path d="M680,130 L740,110 M680,180 L790,140" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round"/>
    <g id="cv-cup"><path d="M650,240 Q760,240 760,320 Q760,400 650,400 Z" fill="#F28B82" stroke="{K}" stroke-width="6"/>
      <path d="M760,300 L860,300 L860,340 L760,340 Z" fill="#F28B82" stroke="{K}" stroke-width="6"/></g>
    <path id="cv-lines" d="M640,250 L600,230 M640,320 L590,320 M640,390 L600,410" stroke="{C['red']}" stroke-width="7" stroke-linecap="round"/>
  </svg>
  <div id="cv-l"><span class="chip" style="background:#FFFFFF">gas pocket!</span></div>
  <div id="cv-pop">POP!</div>
""", J("""
tl.fromTo("#cv-gap", {scaleX:1}, {scaleX:1.6, svgOrigin:"280 290", duration:0.8, ease:"power1.inOut"}, 0.2);
morph("#cv-gap", "#cv-bub", @tg, 0.35, {ease:"back.out(2.4)"});
tl.to("#cv-gap", {attr:{fill:"#FFFFFF"}, duration:0.1}, @tg);
tl.set("#cv-l", {opacity:1}, @tg); pop("#cv-l .chip", @tg);
pop("#cv-win", @tsu, {from:{scale:0.8}, to:{}}); pop("#cv-cup", @tsu2, {from:{x:60}, to:{}});
tl.to("#cv-cup", {x:-170, rotation:-25, svgOrigin:"760 320", duration:0.3, ease:"back.out(2)"}, @tpo);
tl.set("#cv-pop", {opacity:1}, @tpo); pop("#cv-pop", @tpo, {from:{scale:2, rotation:12}, to:{rotation:6}});
ink("#cv-lines", @tpo, 0.2);
""", tg=tgas - 0.15, tsu=tsuc - 0.5, tsu2=tsuc - 0.2, tpo=tpo - 0.1))

# 7 MRI — scanner ring with 2015 chip; a timeline ruler 0 → 1 s, the flash before 1/3 s
s = "mri"; t15 = aw(s, "two thousand fifteen"); tmri = aw(s, "MRI scanner"); tthird = aw(s, "third of a")
ticks = "".join(f'<path d="M{140+i*80},{560} L{140+i*80},{545 if i%5 else 525}" stroke="{K}" stroke-width="4"/>' for i in range(11))
scenes[s] = scene_file(s, f"""
#mr-svg {{ position:absolute; left:0; top:140px; }}
#mr-y {{ position:absolute; left:700px; top:190px; }}
#mr-t {{ position:absolute; left:0; right:0; top:780px; text-align:center; opacity:0; }}
#mr-t .big {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <svg id="mr-svg" width="{W}" height="640" viewBox="0 0 {W} 640" data-layout-ignore>
    <circle id="mr-ring" cx="400" cy="230" r="170" fill="none" stroke="{K}" stroke-width="40" stroke-opacity=".15"/>
    <circle id="mr-ring2" cx="400" cy="230" r="170" fill="none" stroke="{K}" stroke-width="7"/>
    <circle cx="400" cy="230" r="110" fill="none" stroke="{K}" stroke-width="5"/>
    <path id="mr-bed" d="M140,330 L660,330 L660,360 L140,360 Z" fill="#BFE3F7" stroke="{K}" stroke-width="5"/>
    <path id="mr-axis" d="M140,560 L940,560" stroke="{K}" stroke-width="6" fill="none"/>
    {ticks}
    <text x="140" y="615" text-anchor="middle" style="{GH}font-size:40px" fill="{K}">0</text>
    <text x="940" y="615" text-anchor="middle" style="{GH}font-size:40px" fill="{K}">1 s</text>
    <path id="mr-bar" d="M140,500 L400,500" stroke="{C['red']}" stroke-width="26" stroke-linecap="round" fill="none"/>
    <path id="mr-third" d="M407,470 L407,580" stroke="{C['blue']}" stroke-width="6" stroke-dasharray="10 8"/>
    <text id="mr-tl" x="407" y="455" text-anchor="middle" style="{GH}font-size:40px" fill="{C['blue']}">1/3 s</text>
  </svg>
  <div id="mr-y"><span class="chip">2015</span></div>
  <div id="mr-t"><span class="big">less than 1/3 second</span></div>
""", J("""
ink("#mr-ring2", 0.05, 0.7); tl.fromTo("#mr-ring", {opacity:0}, {opacity:1, duration:0.5}, 0.3);
pop("#mr-y", @t15, {from:{rotation:-15}, to:{rotation:-4}});
pop("#mr-bed", @tm, {from:{x:-80}, to:{}});
ink("#mr-axis", @ta, 0.5);
tl.fromTo("#mr-third,#mr-tl", {opacity:0}, {opacity:1, duration:0.3}, @tth0);
ink("#mr-bar", @tth, 0.5, {ease:"power2.out"});
tl.set("#mr-t", {opacity:1}, @tth2); pop("#mr-t .big", @tth2);
""", t15=t15, tm=tmri - 0.3, ta=tmri + 0.3, tth0=tthird - 1.0, tth=tthird - 0.6, tth2=tthird))

# 8 DEBATE — two cards on a see-saw that wobbles
s = "debate"; t18 = aw(s, "two thousand eighteen"); tpc = aw(s, "partly collapsing"); targ = aw(s, "still argue")
scenes[s] = scene_file(s, f"""
#db-ss {{ position:absolute; left:40px; top:150px; width:1000px; height:700px; }}
.db-c {{ position:absolute; top:150px; width:380px; height:270px; text-align:center; {GH} font-size:46px; line-height:1.1; padding-top:22px; }}
.db-c b {{ display:block; font-size:70px; color:{C['red']}; }}
#db-a {{ left:50px; }} #db-b {{ left:570px; }}
#db-q {{ position:absolute; left:440px; top:120px; {GH} font-size:150px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="db-ss">
    <svg class="abs" style="left:0;top:0" width="1000" height="700" viewBox="0 0 1000 700" data-layout-ignore>
      <path d="M440,640 L500,520 L560,640 Z" fill="{C['hi']}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/></svg>
    <div id="db-arm" class="abs" style="left:0;top:0;width:1000px;height:520px">
      <svg class="abs" style="left:0;top:0" width="1000" height="520" viewBox="0 0 1000 520" data-layout-ignore>
        <path id="db-plank" d="M30,500 L970,500" stroke="#8B5A2B" stroke-width="18" stroke-linecap="round" fill="none"/></svg>
      <div id="db-a" class="db-c card"><b>2015</b>pocket opens</div>
      <div id="db-b" class="db-c card" style="background:#FFF3DD"><b>2018</b>bubble partly collapses</div>
    </div>
  </div>
  <div id="db-q">?</div>
""", J("""
ink("#db-plank", 0.05, 0.5);
pop("#db-a", 0.3, {from:{rotation:-10}, to:{rotation:-2}});
pop("#db-b", @t18, {from:{rotation:10}, to:{rotation:2}});
tl.to("#db-arm", {rotation:-6, transformOrigin:"500px 500px", duration:0.5, ease:"back.out(2)"}, 0.5);
tl.to("#db-arm", {rotation:6, transformOrigin:"500px 500px", duration:0.6, ease:"back.out(2)"}, @tpc);
tl.to("#db-arm", {rotation:-3, transformOrigin:"500px 500px", duration:0.5, ease:"sine.inOut", yoyo:true, repeat:3}, @ta);
tl.set("#db-q", {opacity:1}, @ta); pop("#db-q", @ta, {from:{scale:2}, to:{}});
""", t18=t18 - 0.1, tpc=tpc - 0.3, ta=targ - 0.2))

# 9 WAIT — clock face: a dot travels the arc to 20 minutes while the bubble shrinks
s = "wait"; t20 = aw(s, "twenty minutes"); tagain = aw(s, "won't crack")
# arc from 12 o'clock clockwise to 4 o'clock (20 min of a 60-min face), centre 300,330 r 230
a1 = math.radians(-90 + 120)
ax, ay = 300 + 230 * math.cos(a1), 330 + 230 * math.sin(a1)
nums = "".join(f'<text x="{300 + 185*math.cos(math.radians(-90+i*30)):.0f}" y="{330 + 185*math.sin(math.radians(-90+i*30)) + 14:.0f}" text-anchor="middle" style="{GH}font-size:38px" fill="{C["muted"]}">{i*5}</text>' for i in range(0, 12, 2))
scenes[s] = scene_file(s, f"""
#wt-svg {{ position:absolute; left:0; top:130px; }}
#wt-n {{ position:absolute; left:600px; top:250px; width:440px; text-align:center; opacity:0; }}
#wt-n .big {{ font-size:90px; color:{C['red']}; }}
#wt-no {{ position:absolute; left:600px; top:560px; width:440px; text-align:center; opacity:0; }}
""", f"""
  <svg id="wt-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <circle cx="300" cy="330" r="260" fill="#FFFFFF" stroke="{K}" stroke-width="8"/>
    {nums}
    <path id="wt-arc" d="M300,100 A230,230 0 0 1 {ax:.1f},{ay:.1f}" stroke="{C['red']}" stroke-width="14" fill="none" stroke-linecap="round"/>
    <g id="wt-dot" transform="translate(300,100)"><circle r="22" fill="{FLUID}" stroke="{K}" stroke-width="5"/></g>
    <circle cx="300" cy="330" r="12" fill="{K}"/>
    <circle id="wt-bub" cx="300" cy="330" r="80" fill="{FLUID}" fill-opacity=".6" stroke="{K}" stroke-width="5"/>
  </svg>
  <div id="wt-n"><span class="big">up to 20 min</span></div>
  <div id="wt-no"><span class="chip" style="background:#FFC9C2">no crack yet!</span></div>
""", J("""
tl.fromTo("#wt-bub", {scale:0}, {scale:1, svgOrigin:"300 330", duration:0.4, ease:"back.out(2)"}, 0.2);
ink("#wt-arc", @t0, @run, {ease:"none"});
along("#wt-dot", "#wt-arc", @t0, @run, {ease:"none"});
tl.to("#wt-bub", {scale:0.35, svgOrigin:"300 330", duration:@run, ease:"none"}, @t0);
tl.set("#wt-n", {opacity:1}, @t20); pop("#wt-n .big", @t20);
tl.set("#wt-no", {opacity:1}, @tag); pop("#wt-no .chip", @tag, {from:{rotation:-12}, to:{rotation:-4}});
""", t0=t20 - 1.2, run=2.0, t20=t20, tag=tagain - 0.2))

# 10 MYTH — left vs right hand, 60 years; "arthritis?" struck out on both
s = "myth"; tar = aw(s, "and arthritis"); tleft = aw(s, "left hand's"); t60 = aw(s, "sixty years"); tnei = aw(s, "neither hand")
scenes[s] = scene_file(s, f"""
#mt-q {{ top:150px; font-size:72px; }}
.mt-h {{ position:absolute; top:290px; width:400px; height:430px; text-align:center; {GH} }}
#mt-l {{ left:110px; }} #mt-r {{ left:570px; }}
.mt-h .who {{ font-size:54px; margin-top:20px; }}
.mt-h .tal {{ font-size:46px; color:{C['blue']}; height:70px; }}
.mt-h .ar {{ position:absolute; left:0; right:0; top:300px; font-size:56px; color:{C['pencil']}; }}
#mt-60 {{ position:absolute; left:0; right:0; top:750px; text-align:center; opacity:0; }}
.mt-x {{ position:absolute; top:330px; }}
""", f"""
  <div id="mt-q" class="h1">Arthritis?</div>
  <div id="mt-l" class="mt-h card"><div class="who">left hand</div>
    <svg width="400" height="170" viewBox="0 0 400 170" data-layout-ignore>
      <path d="M80,160 L80,60 M130,160 L130,30 M180,160 L180,20 M230,160 L230,35 M280,160 L280,80" stroke="{K}" stroke-width="22" stroke-linecap="round"/>
      <text id="mt-cr" x="330" y="60" style="{GH}font-size:40px" fill="{C['red']}" opacity="0">crack!</text></svg>
    <div class="ar">arthritis?</div></div>
  <div id="mt-r" class="mt-h card"><div class="who">right hand</div>
    <svg width="400" height="170" viewBox="0 0 400 170" data-layout-ignore>
      <path d="M120,160 L120,80 M170,160 L170,35 M220,160 L220,20 M270,160 L270,30 M320,160 L320,60" stroke="{K}" stroke-width="22" stroke-linecap="round"/></svg>
    <div class="ar">arthritis?</div></div>
  <svg class="mt-x abs" style="left:110px;top:560px" width="900" height="120" viewBox="0 0 900 120" data-layout-ignore>
    <path id="mt-x1" d="M80,60 L330,40" stroke="{C['red']}" stroke-width="10" stroke-linecap="round" fill="none"/>
    <path id="mt-x2" d="M540,60 L790,40" stroke="{C['red']}" stroke-width="10" stroke-linecap="round" fill="none"/></svg>
  <div id="mt-60"><span class="chip">about 60 years</span></div>
""", J("""
rise("#mt-q", @tq);
pop("#mt-l", @tl0, {from:{rotation:-10}, to:{rotation:-2}}); pop("#mt-r", @tl1, {from:{rotation:10}, to:{rotation:2}});
tl.fromTo("#mt-cr", {opacity:0}, {opacity:1, duration:0.1, yoyo:true, repeat:5}, @tl0);
tl.set("#mt-60", {opacity:1}, @t60); pop("#mt-60 .chip", @t60, {from:{rotation:-10}, to:{rotation:-3}});
ink("#mt-x1", @tn, 0.3); ink("#mt-x2", @tn2, 0.3);
""", tq=tar - 0.2, tl0=tleft - 0.3, tl1=tleft + 0.2, t60=t60, tn=tnei, tn2=tnei + 0.35))

# 11 OUTRO — recap chip (Max centre stage, keep y < 620)
s = "outro"; tgp = aw(s, "gas pocket"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:170px; text-align:center; }}
#ou-sc {{ top:400px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:56px">POP = a gas pocket</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a .chip", @ta, {from:{rotation:-10}, to:{rotation:-3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", ta=tgp - 0.2, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "what is"), SC["guess"]["start"] + 0.2)
point(g("guess", "bones rubbing"), 2.8)
wave(g("intro", "I'm Max"))
point(g("joint", "tiny capsule"), 1.2)
point(g("pull", "drops fast"), 1.2)
wow(g("cavity", "popping off"), 1.2)
point(g("mri", "third of"), 1.2)
think(g("debate", "still argue"), SC["wait"]["start"])
point(g("wait", "twenty minutes"), 1.2)
wow(g("myth", "neither hand"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "pop"), 0.55), ("pop.mp3", A("guess", "bones rubbing"), 0.45), ("pop.mp3", A("guess", "a bubble bursting"), 0.45),
        ("pop.mp3", A("guess", "or a"), 0.5), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("joint", "tiny capsule"), 0.45),
        ("riser.mp3", A("pull", "slide apart") - 0.3, 0.3), ("impact-bass-1.mp3", A("pull", "drops fast"), 0.45),
        ("pop.mp3", A("cavity", "gas pocket"), 0.6), ("pop.mp3", A("cavity", "popping off"), 0.55),
        ("ping.mp3", A("mri", "third of"), 0.4), ("click.mp3", A("debate", "two thousand eighteen"), 0.4),
        ("click-soft.mp3", A("wait", "twenty minutes"), 0.45), ("impact-bass-2.mp3", A("myth", "neither hand"), 0.45),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
