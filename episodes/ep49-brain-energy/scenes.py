# MAX WISE ep49 — Your brain is tiny. So how much of your energy does it eat?
# Kit: ink / along helpers; no three.js (doodle brain fits better).
# Sources: Quanta Magazine "How much energy does it take to think?" (2025): brain ≈2% of body weight, ≈20% of energy,
#   effortful tasks ≈5% more than resting, infants closer to 50%. Scientific American "Why does the brain need so much power?":
#   up to 20% of energy, about two-thirds fuels neuron signaling.
# Calc: 70 kg * 0.02 = 1.4 kg; 20/2 = 10; 2000 kcal * 0.2 = 400 kcal.
# === SCENES ===
import math as _m
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
PINK = "#F7B6C8"; ZAP = "#F2B807"; GREEN = "#9BD27A"
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
BRAIN = "M-90,10 C-110,-30 -80,-70 -45,-65 C-35,-95 10,-100 25,-75 C55,-95 100,-70 90,-35 C115,-15 105,30 75,40 C70,70 30,80 10,60 C-10,80 -50,75 -55,50 C-85,55 -100,35 -90,10 Z"
FOLDS = ["M-60,-25 C-40,-45 -20,-20 0,-38", "M-62,18 C-40,2 -20,28 2,10 C22,-6 42,20 64,4", "M10,-62 C2,-42 14,-26 8,-8", "M30,-30 C50,-40 66,-22 80,-30", "M-30,40 C-15,30 0,50 20,38"]
def brain(cls, x, y, s, idn=""):
    i = f' id="{idn}"' if idn else ""
    sw = 5 / s
    f = "".join(f'<path class="{cls}" d="{d}" stroke="{K}" stroke-width="{sw*0.8:.2f}" fill="none" stroke-linecap="round"/>' for d in FOLDS)
    return f'<g{i} transform="translate({x},{y}) scale({s})"><path class="{cls}" d="{BRAIN}" fill="{PINK}" stroke="{K}" stroke-width="{sw:.2f}" stroke-linejoin="round"/>{f}</g>'
def battery(x, y, w, h, pre, n=5, filled=5):
    seg = ""
    gap = 8; sw = (w - gap * (n + 1)) / n
    for i in range(n):
        seg += f'<rect id="{pre}-s{i}" x="{x+gap+i*(sw+gap):.1f}" y="{y+gap}" width="{sw:.1f}" height="{h-2*gap}" rx="6" fill="{GREEN if i < filled else "#FFFFFF"}" stroke="{K}" stroke-width="3"/>'
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>'
            f'<rect x="{x+w}" y="{y+h*0.3:.0f}" width="18" height="{h*0.4:.0f}" rx="4" fill="{K}"/>' + seg)

# 1 HOOK — brain and battery ink themselves
s = "hook"; tbr = aw(s, "your brain"); tsm = aw(s, "pretty small"); ten = aw(s, "energy"); teat = aw(s, "does it eat")
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:76px; }}
#hk-qm {{ position:absolute; left:500px; top:610px; {GH} font-size:140px; color:{C['red']}; opacity:0; }}
#hk-l1 {{ position:absolute; left:120px; top:720px; width:360px; text-align:center; {GH} font-size:52px; opacity:0; }}
#hk-l2 {{ position:absolute; left:620px; top:720px; width:360px; text-align:center; {GH} font-size:52px; opacity:0; }}
#hk-bat {{ opacity:0; }}
""", f"""
  <div id="hk-q" class="h1" style="opacity:0">How much <span class="hl">energy</span> does your brain eat?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {brain("hk-b", 300, 560, 1.6)}
    <g id="hk-bat">{battery(660, 500, 250, 120, "hk")}</g>
    <path id="hk-ar" d="M650,470 Q540,400 450,470" stroke="{C['blue']}" stroke-width="6" stroke-dasharray="14 12" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="hk-qm">?</div>
  <div id="hk-l1">your brain</div><div id="hk-l2">your energy</div>
""", J("""
rise("#hk-q", @tq);
ink(".hk-b", @tb, 0.9, {stagger:0.08}); tl.fromTo("#hk-l1", {opacity:0}, {opacity:1, duration:0.2}, @tb2);
pop("#hk-bat", @ten); tl.fromTo("#hk-l2", {opacity:0}, {opacity:1, duration:0.2}, @ten2);
ink("#hk-ar", @ta, 0.5); pop("#hk-qm", @tq2, {from:{rotation:-25, scale:2}, to:{rotation:-6}});
""", tq=0.0, tb=tbr - 0.1, tb2=tbr + 0.6, ten=ten - 0.1, ten2=ten + 0.3, ta=teat - 0.2, tq2=teat + 0.3))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "two percent"); t2 = aw(s, "ten percent"); t3 = aw(s, "or twenty percent")
notes = [("a", "2%?", -6, 110, C['hi']), ("b", "10%?", 4, 405, "#BFE3F7"), ("c", "20%?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:280px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:104px;line-height:1.05;padding-top:70px;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  <div class="h2" style="top:690px">of your body's energy</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 + 0.1))

# 3 INTRO — logo + brain on a little scale (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tsc = aw(s, "on a scale")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:380px; font-size:62px; opacity:0; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {brain("in-b", 540, 520, 0.5)}
    <path class="in-s" d="M470,560 L610,560 L590,600 L490,600 Z" fill="none" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Brain on the scale!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tsc); ink(".in-s", @ts, 0.4); ink(".in-b", @tb, 0.6, {stagger:0.05});
""", tmw=tmw, tu=tmw + 0.3, tsc=tsc - 0.6, ts=tsc - 0.3, tb=tsc))

# 4 WEIGHT — countable units: 50 blocks = 70 kg, one pink block = the brain (2%)
s = "weight"; t70 = aw(s, "seventy kilograms"); t14 = aw(s, "one point four"); t2p = aw(s, "two percent")
cols = 10; bx0, by0, bw, bh = 150, 290, 80, 70
blocks = ""
for i in range(50):
    x = bx0 + (i % cols) * (bw + 8); y = by0 + (i // cols) * (bh + 8)
    blocks += f'<rect class="wt-bl" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="8" fill="{"#FFFFFF" if i else PINK}" stroke="{K}" stroke-width="4" opacity="0"/>'
scenes[s] = scene_file(s, f"""
#wt-title {{ top:150px; font-size:72px; }}
#wt-br {{ opacity:0; }}
#wt-a {{ position:absolute; left:120px; top:700px; opacity:0; }}
#wt-b {{ position:absolute; left:470px; top:700px; opacity:0; }}
#wt-c {{ position:absolute; left:440px; top:800px; right:40px; text-align:center; opacity:0; }}
#wt-c .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="wt-title" class="h1">Weigh it: <span class="hl">body vs brain</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    {blocks}
    {brain("wt-bc", bx0 + bw/2, by0 + bh/2, 0.33, idn="wt-br")}
    <path id="wt-ar" d="M{bx0+bw/2},{by0-10} C{bx0+60},{by0-60} {bx0+160},{by0-60} {bx0+220},{by0-40}" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="wt-a"><span class="chip">body 70 kg</span></div>
  <div id="wt-b"><span class="pill red" style="font-size:46px">brain ≈ 1.4 kg</span></div>
  <div id="wt-c"><span class="big">2%</span><span style="font-size:48px"> of you</span></div>
""", J("""
rise("#wt-title", 0.0);
tl.fromTo(".wt-bl", {opacity:0, scale:0.6, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.12, stagger:0.025, ease:"back.out(2)"}, @t70);
pop("#wt-a", @t70b);
tl.fromTo("#wt-br", {opacity:0}, {opacity:1, duration:0.2}, @t14);
tl.to(".wt-bl", {opacity:0.35, duration:0.3}, @t14);
ink("#wt-ar", @t14, 0.4); pop("#wt-b", @t14b);
pop("#wt-c", @t2p, {from:{scale:1.8}, to:{}});
""", t70=t70 - 0.3, t70b=t70 + 0.6, t14=t14 - 0.1, t14b=t14 + 0.2, t2p=t2p - 0.1))

# 5 ENERGY — battery of five 20% cells; one cell's sparks ride along a wire into the brain
s = "energy"; tbu = aw(s, "burns about"); t20 = aw(s, "twenty percent"); tfi = aw(s, "one fifth")
WIRE = "M540,560 C540,660 420,700 300,620"
sparks = "".join(f'<g id="en-z{i}" opacity="0"><path d="M-10,-16 L6,-2 L-4,0 L10,16 L-8,2 L2,0 Z" fill="{ZAP}" stroke="{K}" stroke-width="2.5"/></g>' for i in range(5))
scenes[s] = scene_file(s, f"""
#en-title {{ top:150px; font-size:72px; }}
#en-big {{ position:absolute; left:440px; right:40px; top:730px; text-align:center; opacity:0; }}
#en-big .big {{ font-size:120px; color:{C['red']}; }}
""", f"""
  <div id="en-title" class="h1">Your energy <span class="hl">battery</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {battery(150, 330, 780, 150, "en")}
    <text x="150" y="315" font-family="Patrick Hand" font-size="38" fill="{K}">20%</text>
    <text x="305" y="315" font-family="Patrick Hand" font-size="38" fill="{K}">20%</text>
    <text x="460" y="315" font-family="Patrick Hand" font-size="38" fill="{K}">20%</text>
    <text x="615" y="315" font-family="Patrick Hand" font-size="38" fill="{K}">20%</text>
    <text x="770" y="315" font-family="Patrick Hand" font-size="38" fill="{K}">20%</text>
    <path id="en-w" d="{WIRE}" stroke="{K}" stroke-width="5" stroke-dasharray="12 10" fill="none" stroke-linecap="round"/>
    {brain("en-bc", 230, 620, 0.85, idn="en-b")}
    {sparks}
  </svg>
  <div id="en-big"><span class="big">≈ 20%</span></div>
  {stamp("en-st", "1/5 of the battery!", 470, 560, -6, 52)}
""", J("""
rise("#en-title", 0.0); ink("#en-w", @tw, 0.6);
tl.fromTo("#en-s4", {fill:"#9BD27A"}, {fill:"#F2B807", duration:0.3, yoyo:true, repeat:3}, @t20); tl.to("#en-s4", {fill:"#FFFFFF", duration:0.4}, @t20 + 1.3);
for (let i=0;i<5;i++) { tl.set("#en-z"+i, {opacity:1}, @tz + i*0.35); along("#en-z"+i, "#en-w", @tz + i*0.35, 0.9, {ease:"power1.in"}); tl.set("#en-z"+i, {opacity:0}, @tz + i*0.35 + 0.9); }
tl.fromTo("#en-b", {scale:0.85, svgOrigin:"230 620"}, {scale:0.95, duration:0.15, yoyo:true, repeat:5, svgOrigin:"230 620"}, @tz + 0.9);
pop("#en-big", @t20b);
pop("#en-st", @tfi, {from:{rotation:-25, scale:1.8}, to:{rotation:-6}});
""", tw=tbu - 0.4, t20=t20 - 0.1, tz=tbu, t20b=t20 - 0.1, tfi=tfi - 0.1))

# 6 TEN — one 2% block stacks up ten times to reach the 20% bar (one object, many states)
s = "ten"; tdv = aw(s, "divided by two"); tisten = aw(s, "is ten"); tfs = aw(s, "fair share")
BH = 48
stack = "".join(f'<rect class="tn-k" x="600" y="{800 - (i+1)*BH}" width="200" height="{BH-4}" rx="6" fill="{PINK}" stroke="{K}" stroke-width="4" opacity="0"/>' for i in range(10))
scenes[s] = scene_file(s, f"""
#tn-eq {{ top:160px; font-size:84px; opacity:0; }}
#tn-l1 {{ position:absolute; left:150px; top:810px; width:260px; text-align:center; font-size:44px; }}
#tn-l2 {{ position:absolute; left:600px; top:810px; width:200px; text-align:center; font-size:44px; }}
""", f"""
  <div id="tn-eq" class="h1">20 ÷ 2 = <span class="hl">10</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <path d="M100,800 L980,800" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
    <rect x="180" y="{800-BH}" width="200" height="{BH-4}" rx="6" fill="{PINK}" stroke="{K}" stroke-width="4"/>
    <path id="tn-cap" d="M590,{800-10*BH-10} L810,{800-10*BH-10}" stroke="{C['red']}" stroke-width="6" stroke-dasharray="14 10" fill="none"/>
    {stack}
  </svg>
  <div id="tn-l1">its weight: 2%</div><div id="tn-l2">its energy: 20%</div>
  {stamp("tn-st", "10×", 830, 360, -8, 90)}
""", J("""
ink("#tn-cap", 0.1, 0.5); pop("#tn-eq", @tdv);
tl.fromTo(".tn-k", {opacity:0, y:-60}, {opacity:1, y:0, duration:0.2, stagger:@stg, ease:"bounce.out"}, @tdv2);
pop("#tn-st", @tten, {from:{rotation:-30, scale:2}, to:{rotation:-8}});
tl.fromTo("#tn-st", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1}, @tfs);
""", tdv=tdv - 0.5, tdv2=tdv, stg=max(0.08, (tisten + 0.6 - tdv) / 10), tten=tisten + 0.3, tfs=tfs))

# 7 FOOD — 2,000 calories as 10 lunch-box blocks; two slide up to the brain, counter to 400
s = "food"; t2k = aw(s, "two thousand calories"); t400 = aw(s, "four hundred"); tst = aw(s, "straight to")
fb = "".join(f'<g class="fd-b" id="fd-b{i}"><rect x="{120 + i*86}" y="560" width="76" height="110" rx="10" fill="{"#FFD27A" if i < 8 else "#FFB27A"}" stroke="{K}" stroke-width="4"/>'
             f'<text x="{158 + i*86}" y="628" text-anchor="middle" font-family="Patrick Hand" font-size="30" fill="{K}">200</text></g>' for i in range(10))
scenes[s] = scene_file(s, f"""
#fd-title {{ top:150px; font-size:72px; opacity:0; }}
#fd-br {{ opacity:0; }}
#fd-cnt {{ position:absolute; left:440px; right:40px; top:760px; text-align:center; opacity:0; }}
#fd-cnt .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="fd-title" class="h1"><span class="hl">2,000</span> calories a day</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <path d="M100,690 L1000,690" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
    {fb}
    {brain("fd-bc", 870, 360, 0.9, idn="fd-br")}
  </svg>
  <div id="fd-cnt"><span class="big"><span id="fd-n">0</span></span><span style="font-size:48px"> to the brain</span></div>
""", J("""
rise("#fd-title", @t2k);
tl.fromTo(".fd-b", {opacity:0, y:40}, {opacity:1, y:0, duration:0.2, stagger:0.06, ease:"back.out(2)"}, @t2k2);
tl.fromTo("#fd-br", {opacity:0}, {opacity:1, duration:0.3}, @t2k2);
tl.to("#fd-b8", {x:50, y:-200, scale:0.4, rotation:-10, duration:0.6, ease:"power2.inOut"}, @tmv); tl.to("#fd-b8", {opacity:0, duration:0.15}, @tmv + 0.6);
tl.to("#fd-b9", {x:-30, y:-200, scale:0.4, rotation:8, duration:0.6, ease:"power2.inOut"}, @tmv + 0.2); tl.to("#fd-b9", {opacity:0, duration:0.15}, @tmv + 0.8);
pop("#fd-cnt", @t400); count("#fd-n", 0, 400, @t400, 0.8, fmtInt);
tl.fromTo("#fd-br", {scale:1, svgOrigin:"870 360"}, {scale:1.1, duration:0.15, yoyo:true, repeat:3, svgOrigin:"870 360"}, @tst);
""", t2k=t2k - 0.3, t2k2=t2k + 0.2, tmv=t400 - 0.3, t400=t400 - 0.1, tst=tst))

# 8 SIGNALS — pie inks two thirds; sparks run along a nerve cell
s = "signals"; twh = aw(s, "where does"); t23 = aw(s, "two thirds"); tsig = aw(s, "tiny signals"); tfire = aw(s, "fire")
PX, PY, PR = 300, 520, 150
circ = 2 * _m.pi * (PR / 2)
NERVE = "M520,600 C600,520 680,640 760,560 C820,500 880,560 960,520"
nz = "".join(f'<g id="sg-z{i}" opacity="0"><circle r="13" fill="{ZAP}" stroke="{K}" stroke-width="3"/></g>' for i in range(4))
scenes[s] = scene_file(s, f"""
#sg-title {{ top:150px; font-size:72px; }}
#sg-23 {{ position:absolute; left:160px; top:720px; width:280px; text-align:center; opacity:0; }}
#sg-23 .big {{ font-size:96px; color:{C['red']}; }}
#sg-lab {{ position:absolute; left:520px; top:640px; width:460px; text-align:center; {GH} font-size:48px; opacity:0; }}
#sg-bz {{ position:absolute; left:700px; top:380px; {GH} font-size:72px; color:{C['red']}; opacity:0; transform:rotate(-8deg); }}
""", f"""
  <div id="sg-title" class="h1">Where does it <span class="hl">go?</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <circle cx="{PX}" cy="{PY}" r="{PR}" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>
    <circle id="sg-pie" cx="{PX}" cy="{PY}" r="{PR/2}" fill="none" stroke="{ZAP}" stroke-width="{PR}" stroke-dasharray="{circ*2/3:.1f} {circ:.1f}" transform="rotate(-90 {PX} {PY})" opacity="0"/>
    <circle cx="{PX}" cy="{PY}" r="{PR}" fill="none" stroke="{K}" stroke-width="6"/>
    <path id="sg-n" d="{NERVE}" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <circle cx="520" cy="600" r="34" fill="{PINK}" stroke="{K}" stroke-width="5"/>
    <path d="M500,575 L470,545 M515,568 L510,530 M540,575 L565,545" stroke="{K}" stroke-width="5" stroke-linecap="round" fill="none"/>
    {nz}
  </svg>
  <div id="sg-23"><span class="big">≈ 2/3</span></div>
  <div id="sg-lab">nerve cell signals</div>
  <div id="sg-bz">ZAP!</div>
""", J("""
rise("#sg-title", @twh);
tl.fromTo("#sg-pie", {opacity:1, strokeDashoffset:@circ}, {strokeDashoffset:0, duration:0.01}, @t23);
tl.fromTo("#sg-pie", {attr:{"stroke-dasharray":"0 @circ"}}, {attr:{"stroke-dasharray":"@arc @circ"}, duration:0.9, ease:"power2.out"}, @t23);
pop("#sg-23", @t23b);
ink("#sg-n", @tn, 0.6); pop("#sg-lab", @tsig);
for (let i=0;i<4;i++) { tl.set("#sg-z"+i, {opacity:1}, @tz + i*0.4); along("#sg-z"+i, "#sg-n", @tz + i*0.4, 0.8, {ease:"none"}); tl.set("#sg-z"+i, {opacity:0}, @tz + i*0.4 + 0.8); }
pop("#sg-bz", @tfire, {from:{scale:2, rotation:-20}, to:{rotation:-8}});
""", twh=twh - 0.1, circ=circ, arc=circ * 2 / 3, t23=t23 - 0.1, t23b=t23 + 0.6, tn=t23 + 0.3, tsig=tsig - 0.1, tz=tsig, tfire=tfire - 0.1))

# 9 TWIST — myth crossed out; resting vs hard-thinking bars (100 vs 105)
s = "twist"; ttw = aw(s, "the twist"); thard = aw(s, "really hard"); t5 = aw(s, "five percent"); trs = aw(s, "resting")
scenes[s] = scene_file(s, f"""
#tw-title {{ top:150px; font-size:72px; }}
#tw-myth {{ position:absolute; left:0; right:0; top:270px; text-align:center; {GH} font-size:60px; color:{C['pencil']}; opacity:0; }}
#tw-l1 {{ position:absolute; left:180px; top:810px; width:240px; text-align:center; font-size:42px; opacity:0; }}
#tw-l2 {{ position:absolute; left:560px; top:810px; width:300px; text-align:center; font-size:42px; opacity:0; }}
#tw-5 {{ position:absolute; left:560px; top:350px; width:300px; text-align:center; opacity:0; }}
""", f"""
  <div id="tw-title" class="h1">Here's the <span class="hl">twist</span></div>
  <div id="tw-myth">hard thinking = huge energy?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <path id="tw-x" d="M190,300 C400,290 700,320 900,295" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path d="M120,800 L960,800" stroke="{K}" stroke-width="6" stroke-linecap="round"/>
    <rect id="tw-b1" x="200" y="480" width="200" height="320" rx="8" fill="#BFE3F7" stroke="{K}" stroke-width="5" opacity="0"/>
    <rect id="tw-b2" x="610" y="464" width="200" height="336" rx="8" fill="#BFE3F7" stroke="{K}" stroke-width="5" opacity="0"/>
    <rect id="tw-b2t" x="610" y="464" width="200" height="16" fill="{C['red']}" stroke="{K}" stroke-width="3" opacity="0"/>
  </svg>
  <div id="tw-l1">resting</div><div id="tw-l2">thinking hard</div>
  <div id="tw-5"><span class="pill red" style="font-size:56px">only +5%</span></div>
""", J("""
rise("#tw-title", 0.0); pop("#tw-myth", @tm);
ink("#tw-x", @tx, 0.4);
tl.fromTo("#tw-b2", {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.5, ease:"back.out(1.6)"}, @thard);
pop("#tw-l2", @thard);
pop("#tw-5", @t5); tl.fromTo("#tw-b2t", {opacity:0}, {opacity:1, duration:0.2, yoyo:true, repeat:3}, @t5);
tl.fromTo("#tw-b1", {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.5, ease:"back.out(1.6)"}, @trs);
pop("#tw-l1", @trs);
""", tm=ttw, tx=thard - 0.4, thard=thard, t5=t5 - 0.1, trs=trs - 0.3))

# 10 BABY — baby head doodle, energy pie fills to about half
s = "baby"; tbb = aw(s, "in babies"); thalf = aw(s, "close to half")
BX, BY = 560, 520
scenes[s] = scene_file(s, f"""
#bb-title {{ top:150px; font-size:72px; }}
#bb-big {{ position:absolute; left:440px; right:40px; top:790px; text-align:center; opacity:0; }}
#bb-big .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="bb-title" class="h1">And in <span class="hl">babies</span>…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <circle class="bb-h" cx="{BX}" cy="{BY}" r="220" fill="#FFE6D2" stroke="{K}" stroke-width="6"/>
    <path class="bb-h" d="M{BX-20},{BY-218} C{BX-40},{BY-260} {BX+20},{BY-270} {BX+10},{BY-240}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <circle cx="{BX-70}" cy="{BY+40}" r="12" fill="{K}"/><circle cx="{BX+70}" cy="{BY+40}" r="12" fill="{K}"/>
    <path class="bb-h" d="M{BX-30},{BY+110} Q{BX},{BY+135} {BX+30},{BY+110}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g id="bb-br" opacity="0">{brain("bb-b", BX, BY-80, 0.95)}</g>
    <circle id="bb-pie" cx="{BX+250}" cy="{BY-180}" r="45" fill="none" stroke="{ZAP}" stroke-width="90" stroke-dasharray="0 283" transform="rotate(-90 {BX+250} {BY-180})"/>
    <circle cx="{BX+250}" cy="{BY-180}" r="90" fill="none" stroke="{K}" stroke-width="5"/>
  </svg>
  <div id="bb-big"><span class="big">≈ 50%</span></div>
""", J("""
rise("#bb-title", 0.0); ink(".bb-h", 0.1, 0.7, {stagger:0.1});
tl.fromTo("#bb-br", {opacity:0}, {opacity:1, duration:0.3}, @tbb);
tl.fromTo("#bb-pie", {attr:{"stroke-dasharray":"0 283"}}, {attr:{"stroke-dasharray":"138 283"}, duration:0.9, ease:"power2.out"}, @th);
pop("#bb-big", @th2, {from:{scale:1.8}, to:{}});
""", tbb=tbb, th=thalf - 0.3, th2=thalf))

# 11 OUTRO — recap, brain + battery, Stay curious (Max centre: keep y < 620)
s = "outro"; t20 = aw(s, "twenty percent"); t2 = aw(s, "for an organ"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#ou-b {{ position:absolute; left:0; right:0; top:270px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:62px">≈ 20% of your energy</span></div>
  <div id="ou-b"><span class="pill red" style="font-size:50px">for 2% of your weight</span></div>
  <svg id="ou-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    {brain("ou-br", 540, 480, 0.9)}
  </svg>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-a", @ta); ink(".ou-br", @ta2, 0.7, {stagger:0.06}); pop("#ou-b", @tb);
tl.to("#ou-a, #ou-b, #ou-svg", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tout);
pop("#ou-c", @tsc);
""", ta=t20 - 0.2, ta2=t20, tb=t2 - 0.1, tout=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "two percent"), 2.4)
wave(g("intro", "I'm Max"))
point(g("weight", "one point four"), 1.2)
wow(g("energy", "twenty percent"), 1.3)
point(g("ten", "is ten"), 1.2)
point(g("food", "four hundred"), 1.2)
point(g("signals", "two thirds"), 1.2)
wow(g("twist", "five percent"), 1.3)
wow(g("baby", "close to half"), 1.3)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "does it eat"), 0.35), ("pop.mp3", A("guess", "two percent"), 0.5), ("pop.mp3", A("guess", "ten percent"), 0.5),
        ("pop.mp3", A("guess", "or twenty percent"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("pop.mp3", A("weight", "two percent"), 0.5), ("riser.mp3", A("energy", "burns about"), 0.3),
        ("impact-bass-1.mp3", A("energy", "one fifth"), 0.45), ("impact-bass-2.mp3", A("ten", "is ten") + 0.3, 0.45),
        ("click-soft.mp3", A("food", "four hundred"), 0.6), ("sparkle.mp3", A("signals", "fire"), 0.4),
        ("click.mp3", A("twist", "really hard") - 0.4, 0.5), ("pop.mp3", A("baby", "close to half"), 0.55), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
