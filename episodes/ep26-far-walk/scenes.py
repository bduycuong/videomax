# MAX WISE ep26 — How far will you walk in your lifetime?
# Kit: ink / along helpers; 2D only (no three.js today). Source: Althoff et al., Nature 2017 (Stanford, 717,527 phone users,
# world average 4,961 steps/day), via Live Science. Earth equator ~40,075 km. Maths in storyboard.md.
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKY = "#BFE3F7"; GRN = "#9BD08F"; PINK = "#FFC9C2"; TAN = "#F2D2A9"

SOLE = "M0,-40 C22,-40 26,-10 20,15 C15,40 -15,40 -20,15 C-26,-10 -22,-40 0,-40"
def foot(x, y, rot, cls, s=1.0, fill=TAN, sw=4, gid=""):
    toes = "".join(f'<circle cx="{tx}" cy="{ty}" r="{tr}" fill="{fill}" stroke="{K}" stroke-width="{sw-1}"/>' for tx, ty, tr in [(-12, -52, 6), (0, -56, 6.5), (11, -53, 5.5), (19, -46, 4.5)])
    o, c = (f'<g id="{gid}">', '</g>') if gid else ("", "")
    return o + (f'<g class="{cls}" transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f}) scale({s})">'
            f'<path d="{SOLE}" fill="{fill}" stroke="{K}" stroke-width="{sw}" stroke-linejoin="round"/>{toes}</g>') + c

def stick(x, y, s, cls, color=None, sw=5, head_fill="none"):
    col = color or K
    hr = 13 * s; hy = y - 100 * s + hr
    st = f'stroke="{col}" stroke-width="{sw}" fill="none" stroke-linecap="round" class="{cls}"'
    return (f'<circle cx="{x:.1f}" cy="{hy:.1f}" r="{hr:.1f}" stroke="{col}" stroke-width="{sw}" fill="{head_fill}" class="{cls}"/>'
            f'<path d="M{x:.1f},{hy + hr:.1f} L{x:.1f},{y - 38*s:.1f}" {st}/>'
            f'<path d="M{x - 22*s:.1f},{y - 70*s:.1f} L{x:.1f},{y - 60*s:.1f} L{x + 22*s:.1f},{y - 70*s:.1f}" {st}/>'
            f'<path d="M{x - 18*s:.1f},{y:.1f} L{x:.1f},{y - 38*s:.1f} L{x + 18*s:.1f},{y:.1f}" {st}/>')

def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(u**3*a + 3*u*u*t*b + 3*u*t*t*c + t**3*d for a, b, c, d in zip(p0, p1, p2, p3))

# 1 HOOK — a winding road inks itself; footprints walk it; a walker travels along
s = "hook"; twk = aw(s, "walk"); tev = aw(s, "every step"); tla = aw(s, "your last"); d1 = SC[s]["slot"]
RD = [(120, 640), (420, 760), (520, 300), (960, 420)]
fp = ""
for i in range(12):
    t = 0.04 + i * 0.08; x, y = bez(*RD, t); x2, y2 = bez(*RD, t + 0.01)
    ang = math.degrees(math.atan2(y2 - y, x2 - x)) + 90; off = 22 if i % 2 else -22
    nx, ny = -math.sin(math.radians(ang - 90)), math.cos(math.radians(ang - 90))
    fp += foot(x + nx * off, y + ny * off, ang, "hk-f", s=0.5)
scenes[s] = scene_file(s, f"""
#hk-t {{ top:150px; font-size:86px; line-height:1.05; }}
#hk-svg {{ position:absolute; left:0; top:180px; }}
#hk-c {{ position:absolute; left:0; right:0; top:900px; text-align:center; opacity:0; padding-left:300px; }}
.hk-f {{ opacity:0; }}
""", f"""
  <div id="hk-t" class="h1">How far will you <span class="hl">walk</span>?</div>
  <svg id="hk-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <path id="hk-road" d="M{RD[0][0]},{RD[0][1]} C{RD[1][0]},{RD[1][1]} {RD[2][0]},{RD[2][1]} {RD[3][0]},{RD[3][1]}" stroke="{C['pencil']}" stroke-width="70" fill="none" stroke-linecap="round" opacity=".25"/>
    <path id="hk-edge" d="M{RD[0][0]},{RD[0][1]} C{RD[1][0]},{RD[1][1]} {RD[2][0]},{RD[2][1]} {RD[3][0]},{RD[3][1]}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="20 16"/>
    {fp}
    <text id="hk-qm" x="960" y="330" text-anchor="middle" style="{GH}font-size:150px;opacity:0" fill="{C['red']}">?</text>
  </svg>
  <div id="hk-c"><span class="chip" style="font-size:52px">first step ... last step</span></div>
""", J("""
pop("#hk-t", @t0, {from:{scale:1.4}, to:{}});
ink("#hk-road", @t1, 0.9); ink("#hk-edge", @t1, 0.9);
tl.fromTo(".hk-f", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:0.5, duration:0.18, ease:"back.out(3)", stagger:@stg}, @tev);
tl.set("#hk-c", {opacity:1}, @tla); pop("#hk-c .chip", @tla, {from:{rotation:-10}, to:{rotation:-3}});
tl.to("#hk-qm", {opacity:1, duration:0.2}, @tq); pop("#hk-qm", @tq, {from:{scale:2, transformOrigin:"50% 50%"}, to:{}});
""", t0=max(0.05, twk - 0.6), t1=twk, tev=tev - 0.1, stg=max(0.08, (tla - tev) / 12), tla=tla - 0.1, tq=tla + 0.3))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "across your"); t2 = aw(s, "across an"); t3 = aw(s, "or all")
notes = [("a", "across your country?", -6, 110, C['hi']), ("b", "across an ocean?", 4, 405, SKY), ("c", "around the Earth?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:60px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.1, t2=t2 - 0.1, t3=t3 - 0.1))

# 3 INTRO — logo + a trail of footprint outlines inks across
s = "intro"; tmw = aw(s, "Max Wise"); tfo = aw(s, "follow")
trail = "".join(f'<path class="in-f" d="{SOLE}" transform="translate({150 + i*110},{70 + (24 if i % 2 else -24)}) rotate(90) scale(0.7)" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round"/>' for i in range(8))
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:62px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Follow the footsteps!</span></div>
  <svg class="abs" style="left:0;top:500px" width="{W}" height="150" data-layout-ignore>{trail}</svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tf); ink(".in-f", @tf, 0.2, {stagger:0.12});
""", tmw=tmw, tu=tmw + 0.3, tf=tfo - 0.3))

# 4 STEPS — a grid of doodle phones (the data), then a counter to about 5,000 steps a day
s = "steps"; tst = aw(s, "stanford"); tph = aw(s, "phone data"); t700 = aw(s, "seven hundred"); t5 = aw(s, "five thousand"); tav = aw(s, "on average")
ph = ""
for i in range(24):
    x = 150 + (i % 8) * 102; y = 300 + (i // 8) * 150
    ph += (f'<g class="st-p"><rect x="{x}" y="{y}" width="64" height="118" rx="12" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>'
           f'<rect x="{x+8}" y="{y+14}" width="48" height="80" rx="4" fill="{[SKY, C["hi"], GRN, PINK][i % 4]}"/>'
           f'<circle cx="{x+32}" cy="{y+105}" r="5" fill="{K}"/></g>')
scenes[s] = scene_file(s, f"""
#st-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#st-svg {{ position:absolute; left:0; top:0; }}
#st-n {{ position:absolute; left:0; right:0; top:180px; text-align:center; opacity:0; }}
#st-n .chip {{ background:{PINK}; font-size:56px; }}
#st-big {{ position:absolute; left:0; right:0; top:790px; text-align:center; font-size:68px; opacity:0; }}
.st-p {{ opacity:0; }}
""", f"""
  <div id="st-c"><span class="chip">a big Stanford study</span></div>
  <svg id="st-svg" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>{ph}</svg>
  <div id="st-n"><span class="chip">700,000+ people</span></div>
  <div id="st-big" class="big"><span id="st-v" class="hl">0</span></div>
""", J("""
tl.set("#st-c", {opacity:1}, @tst); pop("#st-c .chip", @tst, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo(".st-p", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.22, ease:"back.out(3)", stagger:0.04}, @tph);
tl.to("#st-c", {opacity:0, duration:0.15}, @t700a);
tl.set("#st-n", {opacity:1}, @t700); pop("#st-n .chip", @t700, {from:{rotation:10}, to:{rotation:2}});
tl.set("#st-big", {opacity:1}, @tav);
count("#st-v", 0, 5000, @tav, @dc, v => "about " + fmtInt(Math.round(v/10)*10) + " steps a day");
pop("#st-big", @t5, {from:{scale:1.3}, to:{}});
""", tst=tst - 0.1, tph=tph - 0.1, t700a=t700 - 0.25, t700=t700 - 0.1, tav=tav, dc=max(0.6, t5 - tav), t5=t5 + 0.1))

# 5 STRIDE — two footprints with a ruler between them, then a long ruler for one day
s = "stride"; tst = aw(s, "one step"); t70 = aw(s, "seventy"); t5k = aw(s, "so five"); t35 = aw(s, "three and")
ticks = "".join(f'<path class="sd-tk" d="M{300 + i*48},{430} L{300 + i*48},{430 + (34 if i % 5 == 0 else 20)}" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>' for i in range(11))
lticks = "".join(f'<path class="sd-lt" d="M{110 + i*86},{725} L{110 + i*86},{755}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>' for i in range(11))
scenes[s] = scene_file(s, f"""
#sd-svg {{ position:absolute; left:0; top:0; }}
#sd-70 {{ position:absolute; left:0; right:0; top:500px; text-align:center; opacity:0; }}
#sd-70 .big {{ font-size:90px; color:{C['blue']}; }}
#sd-5k {{ position:absolute; left:0; right:0; top:600px; text-align:center; opacity:0; }}
#sd-35 {{ position:absolute; left:0; right:0; top:800px; text-align:center; opacity:0; }}
#sd-35 .big {{ font-size:80px; }}
""", f"""
  <svg id="sd-svg" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {foot(270, 300, 90, "sd-f", s=1.5, gid="sd-f1")}
    {foot(810, 300, 90, "sd-f", s=1.5, gid="sd-f2")}
    <rect id="sd-ru" x="280" y="400" width="520" height="80" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>
    {ticks}
    <path id="sd-lr" d="M110,735 L970,735" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    {lticks}
  </svg>
  <div id="sd-70"><span class="big">70 cm</span></div>
  <div id="sd-5k"><span class="chip">5,000 steps</span></div>
  <div id="sd-35"><span class="big">about <span class="hl">3.5 km</span> a day</span></div>
""", J("""
pop("#sd-f1", @tst, {from:{transformOrigin:"50% 50%"}, to:{}});
pop("#sd-f2", @tst2, {from:{transformOrigin:"50% 50%"}, to:{}});
tl.fromTo("#sd-ru", {opacity:0, scaleX:0, transformOrigin:"0% 50%"}, {opacity:1, scaleX:1, duration:0.5, ease:"power2.out"}, @tru);
ink(".sd-tk", @tru2, 0.1, {stagger:0.04});
tl.set("#sd-70", {opacity:1}, @t70); pop("#sd-70 .big", @t70);
tl.set("#sd-5k", {opacity:1}, @t5k); pop("#sd-5k .chip", @t5k, {from:{rotation:-10}, to:{rotation:-3}});
ink("#sd-lr", @t5kb, @dl); ink(".sd-lt", @t5kb, 0.1, {stagger:@lst});
tl.set("#sd-35", {opacity:1}, @t35); pop("#sd-35 .big", @t35, {from:{scale:1.3}, to:{}});
""", tst=tst - 0.1, tst2=tst + 0.3, tru=t70 - 0.6, tru2=t70 - 0.3, t70=t70 - 0.1, t5k=t5k - 0.1, t5kb=t5k + 0.2,
    dl=max(0.6, t35 - t5k - 0.2), lst=max(0.04, (t35 - t5k - 0.3) / 11), t35=t35 - 0.1))

# 6 YEAR — 365 day squares fill one by one while the kilometres add up
s = "year"; ted = aw(s, "every day"); t13 = aw(s, "one thousand three"); d6 = SC[s]["slot"]
sq = "".join(f'<rect class="yr-d" x="{115 + (i % 25) * 34}" y="{330 + (i // 25) * 34}" width="28" height="28" rx="4" fill="{C["hi"] if (i // 25) % 2 == 0 else SKY}" stroke="{K}" stroke-width="2.5"/>' for i in range(365))
grid = "".join(f'<rect x="{115 + (i % 25) * 34}" y="{330 + (i // 25) * 34}" width="28" height="28" rx="4" fill="none" stroke="{C["rule"]}" stroke-width="2"/>' for i in range(365))
scenes[s] = scene_file(s, f"""
#yr-svg {{ position:absolute; left:0; top:0; }}
#yr-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
#yr-n {{ position:absolute; left:0; right:0; top:860px; text-align:center; font-size:80px; padding-left:260px; opacity:0; }}
.yr-d {{ opacity:0; }}
""", f"""
  <div id="yr-c"><span class="chip">every day for a year</span></div>
  <svg id="yr-svg" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>{grid}{sq}</svg>
  <div id="yr-n" class="big"><span id="yr-v" class="hl">0</span></div>
""", J("""
tl.set("#yr-c", {opacity:1}, @ted); pop("#yr-c .chip", @ted, {from:{rotation:-10}, to:{rotation:-3}});
tl.to(".yr-d", {opacity:1, duration:0.05, stagger:@ea}, @ted2);
tl.set("#yr-n", {opacity:1}, @ted2);
count("#yr-v", 0, 1300, @ted2, @dc, v => "about " + fmtInt(Math.round(v/10)*10) + " km");
pop("#yr-n", @t13, {from:{scale:1.3}, to:{}});
""", ted=ted - 0.1, ted2=ted + 0.2, ea=(t13 + 0.3 - ted) / 365, dc=max(0.6, t13 + 0.4 - ted), t13=t13 + 0.5))

# 7 LIFE — the same kilometres, now year after year: 80 segments fill along a road; an odometer climbs to 100,000 km
s = "life"; tke = aw(s, "keep it"); t80 = aw(s, "eighty years"); t100 = aw(s, "one hundred thousand"); d7 = SC[s]["slot"]
segs = "".join(f'<rect class="lf-s" x="{100 + (i % 20) * 44}" y="{320 + (i // 20) * 110}" width="38" height="60" rx="5" fill="{[C["hi"], SKY, GRN, PINK][i // 20]}" stroke="{K}" stroke-width="3"/>' for i in range(80))
rows = "".join(f'<path d="M100,{350 + r*110} L976,{350 + r*110}" stroke="{C["rule"]}" stroke-width="3" fill="none" stroke-dasharray="8 8"/>' for r in range(4))
scenes[s] = scene_file(s, f"""
#lf-svg {{ position:absolute; left:0; top:0; }}
#lf-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; opacity:0; }}
#lf-c .chip {{ background:{PINK}; }}
#lf-n {{ position:absolute; left:0; right:0; top:800px; text-align:center; font-size:92px; opacity:0; }}
#lf-k {{ position:absolute; left:100px; top:262px; {GH} font-size:40px; color:{C['muted']}; opacity:0; }}
.lf-s {{ opacity:0; }}
""", f"""
  <div id="lf-c"><span class="chip">about 80 years</span></div>
  <div id="lf-k">each box = a year of walking</div>
  <svg id="lf-svg" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>{rows}{segs}</svg>
  <div id="lf-n" class="big"><span id="lf-v" class="hl">0</span></div>
""", J("""
tl.to("#lf-k", {opacity:1, duration:0.25}, @tke);
tl.to(".lf-s", {opacity:1, duration:0.06, stagger:@ea}, @tke2);
tl.set("#lf-c", {opacity:1}, @t80); pop("#lf-c .chip", @t80, {from:{rotation:-10}, to:{rotation:-3}});
tl.set("#lf-n", {opacity:1}, @tke2);
count("#lf-v", 0, 100000, @tke2, @dc, v => "about " + fmtInt(Math.round(v/100)*100) + " km");
pop("#lf-n", @t100, {from:{scale:1.35}, to:{}});
""", tke=tke - 0.1, tke2=tke + 0.2, ea=(t100 + 0.3 - tke) / 80, t80=t80 - 0.1, dc=max(0.6, t100 + 0.5 - tke), t100=t100 + 0.6))

# 8 EARTH — a red trail spirals 2.5 times around a doodle Earth; a walker rides it
s = "earth"; t40 = aw(s, "forty thousand"); tmid = aw(s, "the middle"); tsf = aw(s, "so your"); t25 = aw(s, "two and"); d8 = SC[s]["slot"]
cx, cy = 540, 540
pts = []
N = 300
for i in range(N + 1):
    a = -math.pi / 2 + 2.5 * 2 * math.pi * i / N; r = 255 + 55 * i / N
    pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
spiral = "M" + " L".join(pts)
scenes[s] = scene_file(s, f"""
#ea-svg {{ position:absolute; left:0; top:0; }}
#ea-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#ea-c .chip {{ background:{SKY}; font-size:54px; }}
#ea-n {{ position:absolute; left:0; right:0; top:895px; text-align:center; opacity:0; padding-left:240px; }}
#ea-n .big {{ font-size:86px; color:{C['red']}; }}
""", f"""
  <div id="ea-c"><span class="chip">about 40,000 km around</span></div>
  <svg id="ea-svg" width="{W}" height="1000" viewBox="0 0 {W} 1000" data-layout-ignore>
    <circle id="ea-e" cx="{cx}" cy="{cy}" r="230" fill="{SKY}" stroke="{K}" stroke-width="7"/>
    <path d="M400,410 Q470,350 540,400 Q600,450 520,510 Q450,540 420,490 Z" fill="{GRN}" stroke="{K}" stroke-width="5"/>
    <path d="M590,560 Q690,520 710,600 Q700,680 610,680 Q560,640 590,560 Z" fill="{GRN}" stroke="{K}" stroke-width="5"/>
    <path d="M360,600 Q400,580 430,620 Q420,660 380,650 Z" fill="{GRN}" stroke="{K}" stroke-width="5"/>
    <path id="ea-eq" d="M310,540 Q540,600 770,540" stroke="{C['red']}" stroke-width="6" fill="none" stroke-dasharray="14 10" stroke-linecap="round"/>
    <path id="ea-sp" d="{spiral}" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <g id="ea-w"><circle r="20" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>{foot(0, 4, 0, "ea-wf", s=0.3)}</g>
  </svg>
  <div id="ea-n"><span class="big">about <span class="hl">2.5 times</span>!</span></div>
""", J("""
tl.fromTo("#ea-e", {scale:0.6, opacity:0, transformOrigin:"50% 50%"}, {scale:1, opacity:1, duration:0.5, ease:"back.out(1.6)"}, 0.05);
tl.set("#ea-c", {opacity:1}, @t40); pop("#ea-c .chip", @t40, {from:{rotation:-10}, to:{rotation:-3}});
ink("#ea-eq", @tmid, 0.5);
tl.fromTo("#ea-w", {opacity:0}, {opacity:1, duration:0.15}, @tsf);
ink("#ea-sp", @tsf, @dw, {ease:"none"});
along("#ea-w", "#ea-sp", @tsf, @dw, {ease:"none"});
tl.set("#ea-n", {opacity:1}, @t25); pop("#ea-n .big", @t25, {from:{scale:1.4}, to:{}});
""", t40=t40 - 0.1, tmid=tmid - 0.1, tsf=tsf - 0.2, dw=max(1.5, t25 + 0.5 - tsf), t25=t25 - 0.1))

# 9 MOON — Earth to Moon line; the first quarter glows: that is how far you walk
s = "moon"; tqu = aw(s, "quarter"); tmo = aw(s, "moon")
scenes[s] = scene_file(s, f"""
#mo-svg {{ position:absolute; left:0; top:0; }}
#mo-a {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
#mo-a .big {{ font-size:84px; }}
.mo-l {{ position:absolute; {GH} font-size:46px; }}
""", f"""
  <svg id="mo-svg" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <path id="mo-ln" d="M210,560 L870,560" stroke="{K}" stroke-width="6" fill="none" stroke-dasharray="18 14" stroke-linecap="round"/>
    <path id="mo-q" d="M210,560 L375,560" stroke="{C['hi']}" stroke-width="40" fill="none" stroke-linecap="round" opacity=".9"/>
    <path id="mo-qt" d="M375,520 L375,600" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <circle cx="140" cy="560" r="80" fill="{SKY}" stroke="{K}" stroke-width="6"/>
    <path d="M100,520 Q140,500 160,540 Q150,580 110,570 Z" fill="{GRN}" stroke="{K}" stroke-width="4"/>
    <g id="mo-m"><circle cx="920" cy="560" r="48" fill="#E7E3D8" stroke="{K}" stroke-width="6"/>
      <circle cx="905" cy="545" r="9" fill="none" stroke="{K}" stroke-width="3"/><circle cx="935" cy="575" r="6" fill="none" stroke="{K}" stroke-width="3"/></g>
  </svg>
  <div class="mo-l" style="left:80px;top:670px">Earth</div>
  <div id="mo-ml" class="mo-l" style="left:870px;top:640px;opacity:0">Moon</div>
  <div id="mo-a"><span class="big">about <span class="hl">1/4</span> of the way</span></div>
""", J("""
ink("#mo-ln", 0.05, 0.6); pop("#mo-m", 0.4, {from:{transformOrigin:"50% 50%"}, to:{}});
ink("#mo-q", @tq0, 0.6); ink("#mo-qt", @tq1, 0.2);
tl.set("#mo-a", {opacity:1}, @tqu); pop("#mo-a .big", @tqu, {from:{scale:1.3}, to:{}});
tl.to("#mo-ml", {opacity:1, duration:0.2}, @tmo); pop("#mo-m", @tmo, {from:{scale:1.3, transformOrigin:"50% 50%"}, to:{}});
""", tq0=max(0.5, tqu - 0.6), tq1=tqu, tqu=tqu - 0.1, tmo=tmo - 0.1))

# 10 RANGE — phone asleep on a desk (missed steps, zzz); honest band: real total probably higher
s = "range"; tms = aw(s, "miss steps"); tde = aw(s, "a desk"); trt = aw(s, "real total"); thi = aw(s, "even higher")
scenes[s] = scene_file(s, f"""
#rg-svg {{ position:absolute; left:0; top:0; }}
#rg-z {{ position:absolute; left:300px; top:330px; font-family:'Patrick Hand',cursive; font-size:84px; color:{C['blue']}; opacity:0; }}
#rg-c {{ position:absolute; left:80px; top:170px; opacity:0; }}
#rg-c .chip {{ background:#FFFFFF; font-size:50px; }}
#rg-b {{ position:absolute; left:610px; top:820px; width:360px; text-align:center; {GH} font-size:44px; }}
#rg-h {{ position:absolute; left:500px; top:170px; width:560px; white-space:nowrap; text-align:center; opacity:0; }}
#rg-h .chip {{ background:{C['hi']}; font-size:50px; }}
""", f"""
  <div id="rg-c"><span class="chip">steps missed!</span></div>
  <svg id="rg-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="rg-desk" d="M60,560 L520,560 M110,560 L110,780 M470,560 L470,780" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <g id="rg-ph"><rect x="200" y="505" width="190" height="46" rx="10" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>
      <rect x="214" y="513" width="150" height="30" rx="4" fill="{C['pencil']}" opacity=".5"/></g>
    <rect id="rg-bar" x="700" y="500" width="180" height="300" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>
    <rect id="rg-band" x="700" y="320" width="180" height="180" fill="{C['hi']}" fill-opacity=".35" stroke="{K}" stroke-width="5" stroke-dasharray="16 10"/>
    <path id="rg-ar" d="M790,480 L790,300" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path id="rg-ah" d="M760,330 L790,295 L820,330" stroke="{C['red']}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="rg-z">Zzz...</div>
  <div id="rg-b">about 100,000 km</div>
  <div id="rg-h"><span class="chip">probably even higher</span></div>
""", J("""
tl.fromTo("#rg-bar", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.5, ease:"power2.out"}, 0.05);
ink("#rg-desk", @tde0, 0.5); pop("#rg-ph", @tde, {from:{y:-60, transformOrigin:"50% 50%"}, to:{}});
tl.to("#rg-z", {opacity:1, duration:0.2}, @tz); tl.fromTo("#rg-z", {y:20}, {y:-20, duration:1.6, ease:"sine.inOut"}, @tz);
tl.set("#rg-c", {opacity:1}, @tms); pop("#rg-c .chip", @tms, {from:{rotation:-10}, to:{rotation:-4}});
tl.fromTo("#rg-band", {opacity:0}, {opacity:1, duration:0.4}, @trt);
ink("#rg-ar", @trt2, 0.4); ink("#rg-ah", @trt3, 0.2);
tl.set("#rg-h", {opacity:1}, @thi); pop("#rg-h .chip", @thi, {from:{rotation:10}, to:{rotation:3}});
""", tde0=max(0.2, tms - 0.6), tms=tms - 0.1, tde=tde - 0.2, tz=tde + 0.2, trt=trt - 0.2, trt2=trt + 0.2, trt3=trt + 0.6, thi=thi - 0.2))

# 11 OUTRO — callback: about 100,000 km, one small step at a time (Max centre stage, keep y < 620)
s = "outro"; tab = aw(s, "about one"); tst = aw(s, "one small"); tsc = aw(s, "stay curious")
of = "".join(foot(250 + i * 90, 560 + (16 if i % 2 else -16), 90, "ou-f", s=0.5) for i in range(7))
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; }}
#ou-sc {{ top:300px; font-size:110px; opacity:0; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
.ou-f {{ opacity:0; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:58px;background:{SKY}">about 100,000 km</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
  <svg id="ou-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>{of}</svg>
""", J("""
pop("#ou-a .chip", @ta, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo(".ou-f", {opacity:0}, {opacity:1, duration:0.15, stagger:0.2}, @tst);
tl.set("#ou-sc", {opacity:1}, @tsc); pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", ta=tab - 0.2, tst=tst - 0.1, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "how far"), SC["guess"]["start"] + 0.2)
point(g("guess", "across your"), 3.0)
wave(g("intro", "I'm Max"))
point(g("steps", "seven hundred"), 1.4)
point(g("stride", "seventy"), 1.2)
point(g("year", "one thousand three"), 1.2)
wow(g("life", "one hundred thousand"), 1.4)
wow(g("earth", "two and"), 1.4)
point(g("moon", "quarter"), 1.2)
think(g("range", "phones miss"), g("range", "real total"))
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "your last"), 0.35),
        ("pop.mp3", A("guess", "across your"), 0.45), ("pop.mp3", A("guess", "across an"), 0.45), ("pop.mp3", A("guess", "or all"), 0.5),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("steps", "seven hundred"), 0.45),
        ("ping.mp3", A("stride", "seventy"), 0.4), ("riser.mp3", A("life", "keep it"), 0.3),
        ("impact-bass-1.mp3", A("life", "one hundred thousand") + 0.5, 0.45), ("ping.mp3", A("earth", "two and"), 0.45),
        ("click-soft.mp3", A("moon", "quarter"), 0.45), ("pop.mp3", A("range", "even higher"), 0.4),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
