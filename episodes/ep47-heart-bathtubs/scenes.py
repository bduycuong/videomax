# MAX WISE ep47 — How many bathtubs of blood does your heart pump in one day?
# Kit: ink / along helpers; no three.js (pure doodles).
# Source: Cleveland Clinic "Facts about the heart" (5.7 L per minute, ~100,000 beats/day, ~96,000 km vessels ≈ twice around Earth, two clasped hands).
# Calc: 5.7*1440 = 8208 ≈ 8,200 L; /150 = 54.7 ≈ 55 tubs; *365.25*80 ≈ 240 million L; /2.5 million = 96 pools ("nearly 100").
# === SCENES ===
import math as _m
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
PINK = "#F7A1A1"; BLOOD = "#E0483C"; WATER = "#BFE3F7"
WSF = WS.replace('fill="none" ', '')
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
HEART = "M0,60 C-90,0 -110,-70 -55,-90 C-25,-100 -5,-80 0,-60 C5,-80 25,-100 55,-90 C110,-70 90,0 0,60 Z"
def heart(cls, x, y, s, idn=""):
    i = f' id="{idn}"' if idn else ""
    return f'<g{i} transform="translate({x},{y}) scale({s})"><path class="{cls}" d="{HEART}" fill="{PINK}" stroke="{K}" stroke-width="{5/s:.2f}" stroke-linejoin="round"/></g>'
TUB = "M-50,-14 L50,-14 C50,14 34,26 0,26 C-34,26 -50,14 -50,-14 Z"
def tub_outline(cls, x, y, s, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})"{extra}>'
            f'<path class="{cls}" d="{TUB}" fill="#FFFFFF" stroke="{K}" stroke-width="{5/s:.2f}" stroke-linejoin="round"/>'
            f'<path class="{cls}" d="M-40,26 L-44,36 M40,26 L44,36" stroke="{K}" stroke-width="{5/s:.2f}" stroke-linecap="round" fill="none"/>'
            f'<path class="{cls}" d="M40,-14 L40,-40 L28,-40" stroke="{K}" stroke-width="{5/s:.2f}" stroke-linecap="round" fill="none"/></g>')

# 1 HOOK — heart and bathtub ink themselves
s = "hook"; thp = aw(s, "heart pump"); tbt = aw(s, "bathtubs"); tod = aw(s, "one day")
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:76px; }}
#hk-qm {{ position:absolute; left:500px; top:640px; {GH} font-size:140px; color:{C['red']}; opacity:0; }}
#hk-l1 {{ position:absolute; left:160px; top:780px; width:300px; text-align:center; {GH} font-size:52px; opacity:0; }}
#hk-l2 {{ position:absolute; left:640px; top:780px; width:300px; text-align:center; {GH} font-size:52px; opacity:0; }}
""", f"""
  <div id="hk-q" class="h1" style="opacity:0">How many <span class="hl">bathtubs</span> of blood a day?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {heart("hk-h", 310, 590, 1.7)}
    {tub_outline("hk-t", 790, 600, 2.2)}
    <path id="hk-ar" d="M440,560 Q560,470 660,540" stroke="{C['blue']}" stroke-width="6" stroke-dasharray="14 12" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="hk-qm">?</div>
  <div id="hk-l1">your heart</div><div id="hk-l2">bathtub</div>
""", J("""
rise("#hk-q", @tq);
ink(".hk-h", @th, 0.8); tl.fromTo("#hk-l1", {opacity:0}, {opacity:1, duration:0.2}, @th2);
ink(".hk-t", @tb, 0.8, {stagger:0.15}); tl.fromTo("#hk-l2", {opacity:0}, {opacity:1, duration:0.2}, @tb2);
ink("#hk-ar", @ta, 0.5); pop("#hk-qm", @tod, {from:{rotation:-25, scale:2}, to:{rotation:-6}});
""", tq=max(0.0, tbt - 1.2), th=max(0.1, tbt - 0.8), th2=tbt - 0.2, tb=tbt, tb2=tbt + 0.6, ta=thp, tod=tod - 0.1))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "one bathtub"); t2 = aw(s, "ten"); t3 = aw(s, "more than fifty")
notes = [("a", "1?", -6, 110, C['hi'], 110), ("b", "10?", 4, 405, "#BFE3F7", 110), ("c", "50+?", -3, 700, "#FFC9C2", 110)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:280px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding-top:70px;opacity:0">{txt}</div>' for k, txt, r, x, bg, fs in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  <div class="h2" style="top:690px">bathtubs per day</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.1))

# 3 INTRO — logo + heart ink (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tfp = aw(s, "follow the pump")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {heart("in-h", 540, 545, 0.65)}
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Follow the pump!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tfp); ink(".in-h", @th, 0.6);
""", tmw=tmw, tu=tmw + 0.3, tfp=tfp - 0.2, th=tfp + 0.1))

# 4 SQUEEZE — heart beats, drops ride along an artery, counter to 100,000
s = "squeeze"; tsq = aw(s, "squeezes"); tgl = aw(s, "small gulp"); t100 = aw(s, "one hundred thousand"); tad = aw(s, "a day")
ART = "M610,430 C760,380 820,560 990,560"
drops = "".join(f'<g id="sq-d{i}" opacity="0"><path d="M0,-20 Q16,0 0,14 Q-16,0 0,-20 Z" fill="{BLOOD}" stroke="{K}" stroke-width="3"/></g>' for i in range(5))
scenes[s] = scene_file(s, f"""
#sq-title {{ top:150px; font-size:74px; }}
#sq-bd {{ position:absolute; left:50px; top:250px; {GH} font-size:64px; color:{C['red']}; opacity:0; transform:rotate(-10deg); }}
#sq-cnt {{ position:absolute; left:0; right:0; top:730px; text-align:center; opacity:0; }}
#sq-cnt .big {{ font-size:120px; color:{C['red']}; }}
""", f"""
  <div id="sq-title" class="h1">One <span class="hl">squeeze</span> = one gulp</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <path id="sq-art" d="{ART}" stroke="{BLOOD}" stroke-width="30" fill="none" stroke-linecap="round" opacity="0.35"/>
    <path id="sq-artk" d="{ART}" stroke="{K}" stroke-width="4" fill="none" stroke-dasharray="10 10"/>
    {drops}
    <g id="sq-hw" transform="translate(470,470)"><g id="sq-h"><path d="{HEART}" transform="scale(2.1)" fill="{PINK}" stroke="{K}" stroke-width="2.6" stroke-linejoin="round"/>
      <path d="M-50,-60 Q-70,-30 -55,0" transform="scale(2.1)" stroke="#FFFFFF" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.7"/></g></g>
  </svg>
  <div id="sq-bd">BA‑DUM!</div>
  <div id="sq-cnt"><span id="sq-n" class="big">0</span><div style="font-size:52px">squeezes a day</div></div>
""", J("""
rise("#sq-title", 0.0); ink("#sq-artk", 0.2, 0.6);
tl.fromTo("#sq-h", {scale:1, svgOrigin:"0 0"}, {scale:0.86, duration:0.16, yoyo:true, repeat:13, repeatDelay:0.27, ease:"power2.inOut", svgOrigin:"0 0"}, @tsq);
tl.fromTo("#sq-bd", {opacity:0, scale:0.6}, {opacity:1, scale:1, duration:0.2, ease:"back.out(2)"}, @tsq);
for (let i=0;i<5;i++) { tl.set("#sq-d"+i, {opacity:1, x:610, y:430}, @tgl + i*0.85); along("#sq-d"+i, "#sq-art", @tgl + i*0.85, 1.3, {ease:"power1.in"}); tl.set("#sq-d"+i, {opacity:0}, @tgl + i*0.85 + 1.3); }
pop("#sq-cnt", @tc); count("#sq-n", 0, 100000, @tc, @dc, fmtInt);
tl.fromTo("#sq-n", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1}, @te);
""", tsq=tsq - 0.1, tgl=tgl - 0.1, tc=t100 - 0.6, dc=0.9, te=t100 + 0.4))

# 5 MINUTE — three soda bottles fill: 1, 2, almost 3
s = "minute"; tmin = aw(s, "every minute"); t57 = aw(s, "five point seven"); t3b = aw(s, "three big soda")
BOT = "M-42,-120 L-42,-150 Q-42,-160 -30,-165 L-20,-200 L-20,-230 L20,-230 L20,-200 L30,-165 Q42,-160 42,-150 L42,150 Q42,170 22,170 L-22,170 Q-42,170 -42,150 Z"
bots = ""
for i, x in enumerate([260, 540, 820]):
    lvl = 1.0 if i < 2 else 0.85
    hgt = 300 * lvl
    bots += (f'<g transform="translate({x},560)"><clipPath id="mn-c{i}"><path d="{BOT}"/></clipPath>'
             f'<rect id="mn-f{i}" x="-50" y="{170-hgt:.0f}" width="100" height="{hgt:.0f}" fill="{BLOOD}" clip-path="url(#mn-c{i})"/>'
             f'<path d="{BOT}" fill="none" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
             f'<rect x="-42" y="-40" width="84" height="50" fill="#FFFFFF" stroke="{K}" stroke-width="4" opacity="0.9"/></g>')
scenes[s] = scene_file(s, f"""
#mn-title {{ top:150px; font-size:74px; }}
#mn-lab {{ position:absolute; left:0; right:0; top:770px; text-align:center; opacity:0; {GH} font-size:64px; }}
""", f"""
  <div id="mn-title" class="h1" style="opacity:0">Every minute: <span class="hl">5.7 L</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>{bots}</svg>
  <div id="mn-lab">almost <span class="red">3</span> big soda bottles</div>
""", J("""
rise("#mn-title", @t57);
tl.fromTo("#mn-f0", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.7, ease:"power1.inOut"}, @tf);
tl.fromTo("#mn-f1", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.7, ease:"power1.inOut"}, @tf + 0.7);
tl.fromTo("#mn-f2", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.6, ease:"power1.out"}, @tf + 1.4);
pop("#mn-lab", @t3b);
""", t57=t57 - 0.3, tf=t57 + 0.2, t3b=t3b - 0.2))

# 6 DAY — clock spins, 1,440 minutes, counter to ≈ 8,200 L
s = "day"; t1440 = aw(s, "one thousand four hundred and forty"); tmu = aw(s, "multiply"); t82 = aw(s, "eight thousand two hundred")
ticks = "".join(f'<path d="M{540+170*_m.sin(a*_m.pi/6):.1f},{430-170*_m.cos(a*_m.pi/6):.1f} L{540+190*_m.sin(a*_m.pi/6):.1f},{430-190*_m.cos(a*_m.pi/6):.1f}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for a in range(12))
scenes[s] = scene_file(s, f"""
#dy-title {{ top:150px; font-size:74px; }}
#dy-ch {{ position:absolute; left:0; right:0; top:660px; text-align:center; opacity:0; }}
#dy-eq {{ position:absolute; left:0; right:0; top:770px; text-align:center; opacity:0; }}
#dy-eq .big {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="dy-title" class="h1">One whole <span class="hl">day</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="660" viewBox="0 0 {W} 660" data-layout-ignore>
    <circle cx="540" cy="430" r="200" fill="#FFFFFF" stroke="{K}" stroke-width="7"/>{ticks}
    <path id="dy-hh" d="M540,430 L540,330" stroke="{K}" stroke-width="10" stroke-linecap="round"/>
    <path id="dy-mh" d="M540,430 L540,265" stroke="{C['red']}" stroke-width="7" stroke-linecap="round"/>
    <circle cx="540" cy="430" r="12" fill="{K}"/>
  </svg>
  <div id="dy-ch"><span class="chip">1,440 minutes</span></div>
  <div id="dy-eq"><span class="big">≈ <span id="dy-n">0</span> L</span></div>
""", J("""
rise("#dy-title", 0.0);
tl.fromTo("#dy-mh", {rotation:0, svgOrigin:"540 430"}, {rotation:4320, duration:@dsp, ease:"power1.inOut"}, 0.2);
tl.fromTo("#dy-hh", {rotation:0, svgOrigin:"540 430"}, {rotation:360, duration:@dsp, ease:"power1.inOut"}, 0.2);
pop("#dy-ch", @t1440);
pop("#dy-eq", @tmu); count("#dy-n", 0, 8200, @tmu, @dc, fmtInt);
tl.fromTo("#dy-n", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1}, @te);
""", dsp=max(2.0, tmu - 0.2), t1440=t1440 - 0.1, tmu=tmu, dc=t82 + 0.9 - tmu, te=t82 + 1.0))

# 7 TUBS — 55 bathtubs fill one by one
s = "tubs"; t150 = aw(s, "one hundred and fifty"); tfl = aw(s, "fills about"); t55 = aw(s, "fifty five"); tev = aw(s, "every single day")
cols = 11; gx0, gy0, dx, dy = 95, 440, 89, 72
tg = ""
for i in range(55):
    x = gx0 + (i % cols) * dx; y = gy0 + (i // cols) * dy
    tg += (f'<g transform="translate({x},{y}) scale(0.72)"><clipPath id="tb-c{i}"><path d="{TUB}"/></clipPath>'
           f'<rect class="tb-w" x="-52" y="-14" width="104" height="42" fill="{BLOOD}" clip-path="url(#tb-c{i})"/>'
           f'<path d="{TUB}" fill="none" stroke="{K}" stroke-width="5" stroke-linejoin="round"/></g>')
scenes[s] = scene_file(s, f"""
#tb-title {{ top:150px; font-size:72px; }}
#tb-one {{ position:absolute; left:0; right:0; top:270px; text-align:center; opacity:0; {GH} font-size:56px; }}
#tb-cnt {{ position:absolute; left:420px; top:800px; opacity:0; }}
#tb-cnt .big {{ font-size:120px; color:{C['red']}; }}
""", f"""
  <div id="tb-title" class="h1">Fill the <span class="hl">bathtubs</span></div>
  <div id="tb-one">1 bathtub ≈ 150 L</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>{tg}</svg>
  <div id="tb-cnt"><span id="tb-n" class="big">0</span><span style="font-size:52px"> bathtubs</span></div>
  {stamp("tb-st", "EVERY DAY!", 370, 250, -6, 64)}
""", J("""
rise("#tb-title", 0.0); pop("#tb-one", @t150);
tl.fromTo(".tb-w", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.15, stagger:@stg}, @tf);
pop("#tb-cnt", @tf); count("#tb-n", 0, 55, @tf, @dc, v => String(Math.round(v)));
tl.to("#tb-one", {opacity:0, duration:0.15}, @tev - 0.15); pop("#tb-st", @tev, {from:{rotation:-25, scale:1.8}, to:{rotation:-8}});
""", t150=t150 - 0.2, tf=tfl - 0.1, stg=(t55 + 0.7 - tfl) / 55, dc=t55 + 0.8 - tfl, tev=tev - 0.1))

# 8 PIPES — Earth with a red vessel inking itself around it twice
s = "pipes"; tpu = aw(s, "pushes"); t96 = aw(s, "ninety six thousand"); tbv = aw(s, "blood vessels"); ttw = aw(s, "twice")
EX, EY = 600, 540
def loop(rx, ry, rot):
    a = rot * _m.pi / 180; pts = []
    for k in range(0, 73):
        th = k * 2 * _m.pi / 72
        x, y = rx * _m.cos(th), ry * _m.sin(th)
        pts.append((EX + x * _m.cos(a) - y * _m.sin(a), EY + x * _m.sin(a) + y * _m.cos(a)))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
scenes[s] = scene_file(s, f"""
#pp-title {{ top:150px; font-size:72px; }}
#pp-cnt {{ position:absolute; left:420px; right:30px; top:800px; text-align:center; opacity:0; }}
#pp-cnt .big {{ font-size:96px; color:{C['red']}; }}
#pp-tw {{ position:absolute; left:440px; top:250px; opacity:0; white-space:nowrap; }}
""", f"""
  <div id="pp-title" class="h1">All those <span class="hl">blood vessels</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <circle cx="{EX}" cy="{EY}" r="170" fill="{WATER}" stroke="{K}" stroke-width="7"/>
    <path d="M{EX-110},{EY-80} C{EX-60},{EY-120} {EX-10},{EY-70} {EX-30},{EY-20} C{EX-60},{EY+20} {EX-120},{EY} {EX-110},{EY-80} Z" fill="#B9DE9A" stroke="{K}" stroke-width="5"/>
    <path d="M{EX+40},{EY+20} C{EX+100},{EY} {EX+130},{EY+60} {EX+90},{EY+110} C{EX+50},{EY+130} {EX+20},{EY+70} {EX+40},{EY+20} Z" fill="#B9DE9A" stroke="{K}" stroke-width="5"/>
    <path id="pp-l1" d="{loop(270, 80, -14)}" stroke="{BLOOD}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="pp-l2" d="{loop(250, 110, 22)}" stroke="{BLOOD}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="pp-tw"><span class="pill red" style="font-size:52px">around Earth twice!</span></div>
  <div id="pp-cnt"><span class="big">≈ 96,000 km</span><div style="font-size:46px">of blood vessels</div></div>
""", J("""
rise("#pp-title", 0.0);
ink("#pp-l1", @ti1, @d1); pop("#pp-cnt", @t96);
ink("#pp-l2", @ti2, 1.0); pop("#pp-tw", @ttw, {from:{rotation:-15}, to:{rotation:-4}});
""", ti1=tpu - 0.1, d1=max(1.0, tbv - tpu), t96=t96 - 0.1, ti2=ttw - 1.0, ttw=ttw - 0.1))

# 9 LIFE — age ruler with a marker riding along; 10×10 pool grid fills to 96
s = "life"; t80 = aw(s, "eighty years"); t240 = aw(s, "two hundred and forty million"); tn100 = aw(s, "nearly one hundred")
RX0, RX1, RY = 120, 980, 320
def rx(a): return RX0 + (RX1 - RX0) * a / 80
rt = "".join(f'<path d="M{rx(a):.1f},{RY-(24 if a%20==0 else 12)} L{rx(a):.1f},{RY}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
             (f'<text x="{rx(a):.1f}" y="{RY+44}" text-anchor="middle" font-family="Patrick Hand" font-size="36" fill="{K}">{a}</text>' if a % 20 == 0 else "") for a in range(0, 81, 10))
pg = "".join(f'<rect class="lf-p" x="{150 + (i%10)*80}" y="{400 + (i//10)*38}" width="68" height="28" rx="4" fill="{BLOOD if i < 96 else "#FFFFFF"}" stroke="{K}" stroke-width="3"/>' for i in range(100))
pgo = "".join(f'<rect x="{150 + (i%10)*80}" y="{400 + (i//10)*38}" width="68" height="28" rx="4" fill="#FFFFFF" stroke="{K}" stroke-width="3"/>' for i in range(100))
scenes[s] = scene_file(s, f"""
#lf-title {{ top:150px; font-size:72px; }}
#lf-a {{ position:absolute; left:420px; right:30px; top:800px; text-align:center; opacity:0; }}
#lf-a .big {{ font-size:76px; color:{C['red']}; }}
#lf-b {{ position:absolute; left:420px; right:30px; top:890px; text-align:center; opacity:0; {GH} font-size:54px; }}
""", f"""
  <div id="lf-title" class="h1">Over <span class="hl">80 years</span>…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <path id="lf-rul" d="M{RX0},{RY} L{RX1},{RY}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>{rt}
    <g id="lf-m"><path d="M0,-6 L-16,-34 L16,-34 Z" fill="{C['red']}" stroke="{K}" stroke-width="3"/></g>
    {pgo}{pg}
  </svg>
  <div id="lf-a"><span class="big">≈ <span id="lf-n">0</span> million L</span></div>
  <div id="lf-b">nearly <span class="red">100</span> Olympic pools!</div>
""", J("""
rise("#lf-title", 0.0); tl.set("#lf-m", {x:@x0, y:@ry}, 0);
along("#lf-m", "#lf-rul", @tm, @dm, {ease:"none"});
tl.fromTo(".lf-p", {opacity:0}, {opacity:1, duration:0.05, stagger:@stg}, @tm);
pop("#lf-a", @tm2); count("#lf-n", 0, 240, @tm2, @dc, v => String(Math.round(v)));
pop("#lf-b", @tn);
""", x0=RX0, ry=RY, tm=t80 - 0.2, dm=tn100 + 0.3 - t80, stg=(tn100 + 0.3 - t80) / 100, tm2=t80 + 0.6, dc=t240 + 1.2 - (t80 + 0.6), tn=tn100 - 0.1))

# 10 OUTRO — recap chip, heart in two cupped hands, Stay curious (Max centre: keep y < 620)
s = "outro"; t55 = aw(s, "fifty five"); tch = aw(s, "clasped hands"); tsc = aw(s, "stay curious")
hands = (f'<path class="ou-hd" d="M380,430 C400,520 470,560 540,560 C610,560 680,520 700,430" {WS} stroke-width="7"/>'
         f'<path class="ou-hd" d="M380,430 L350,380 M410,470 L370,420 M700,430 L730,380 M670,470 L710,420" {WS} stroke-width="6"/>')
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:66px">≈ 55 bathtubs a day</span></div>
  <svg id="ou-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    {heart("ou-h", 540, 430, 1.0)}{hands}
  </svg>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-a", @ta);
ink(".ou-h", @th, 0.6); ink(".ou-hd", @tch, 0.7, {stagger:0.1});
tl.to("#ou-a, #ou-svg", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tout);
pop("#ou-c", @tsc);
""", ta=t55 - 0.2, th=t55 + 0.4, tch=tch - 0.6, tout=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "one bathtub"), 2.4)
wave(g("intro", "I'm Max"))
point(g("squeeze", "one hundred thousand"), 1.2)
point(g("minute", "five point seven"), 1.2)
wow(g("day", "eight thousand two hundred"), 1.3)
wow(g("tubs", "fifty five"), 1.3)
point(g("pipes", "ninety six thousand"), 1.2)
wow(g("life", "nearly one hundred"), 1.3)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "one day"), 0.35), ("pop.mp3", A("guess", "one bathtub"), 0.5), ("pop.mp3", A("guess", "ten"), 0.5),
        ("pop.mp3", A("guess", "more than fifty"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("impact-bass-1.mp3", A("squeeze", "squeezes"), 0.4), ("click-soft.mp3", A("squeeze", "one hundred thousand") + 0.4, 0.6),
        ("pop.mp3", A("minute", "three big soda"), 0.5), ("impact-bass-2.mp3", A("day", "eight thousand two hundred") + 0.9, 0.45),
        ("riser.mp3", A("tubs", "fills about"), 0.3), ("impact-bass-1.mp3", A("tubs", "every single day"), 0.45),
        ("ping.mp3", A("pipes", "twice"), 0.4), ("pop.mp3", A("life", "nearly one hundred"), 0.55), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
