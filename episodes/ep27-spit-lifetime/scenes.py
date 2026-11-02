# MAX WISE ep27 — How much spit will you make in your lifetime?
# Kit: ink / along helpers; 2D only (no three.js). Sources: Cleveland Clinic (salivary glands), Britannica (salivary glands), Cambridge MRCS revision guide.
# Maths: 1 L/day x 365 = 365 L/yr = 2.4 tubs (150 L); x 80 yr = 29,200 L ~ 30,000 L ~ 195 tubs; low end 0.5 L/day -> ~97 tubs. Olympic pool 50x25x2 m = 2,500,000 L.
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SPIT = "#BFE3F7"; GLAND = "#F2B705"; SKIN = "#FCE3D2"; PINK = "#F7C6CF"; WATER = "#7FC3EA"

def drop(idn, cls=""):
    """a water drop drawn around 0,0 (tip up)"""
    c = f' class="{cls}"' if cls else ""
    return (f'<g id="{idn}"{c}><path d="M0,-34 Q24,-4 22,12 A22,22 0 0 1 -22,12 Q-24,-4 0,-34 Z" fill="{SPIT}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M-9,4 Q-10,12 -4,18" stroke="#FFFFFF" stroke-width="5" fill="none" stroke-linecap="round"/></g>')

def tub(p, cx, cy, w=260, water=True):
    """bathtub doodle centred at cx,cy; water rect id p-w (scaleY from the bottom)"""
    h = w * 0.42; x0, x1 = cx - w / 2, cx + w / 2; y0 = cy - h / 2; y1 = cy + h / 2
    body = f"M{x0:.0f},{y0:.0f} L{x1:.0f},{y0:.0f} L{x1 - w*0.08:.0f},{y1:.0f} Q{cx:.0f},{y1 + h*0.25:.0f} {x0 + w*0.08:.0f},{y1:.0f} Z"
    out = f'<clipPath id="{p}-cl"><path d="{body}"/></clipPath>'
    if water:
        out += f'<g clip-path="url(#{p}-cl)"><rect id="{p}-w" x="{x0:.0f}" y="{y0 + h*0.12:.0f}" width="{w}" height="{h*1.2:.0f}" fill="{WATER}"/></g>'
    out += (f'<path d="{body}" fill="none" stroke="{K}" stroke-width="{max(3, w/40):.0f}" stroke-linejoin="round"/>'
            f'<path d="M{x0 - w*0.04:.0f},{y0:.0f} L{x1 + w*0.04:.0f},{y0:.0f}" stroke="{K}" stroke-width="{max(3, w/30):.0f}" stroke-linecap="round"/>'
            f'<circle cx="{x0 + w*0.16:.0f}" cy="{y1 + h*0.12:.0f}" r="{max(2, w/28):.0f}" fill="{K}"/><circle cx="{x1 - w*0.16:.0f}" cy="{y1 + h*0.12:.0f}" r="{max(2, w/28):.0f}" fill="{K}"/>')
    return out, (y1 + h * 0.2)

# 1 HOOK — an open mouth inks itself; a drop drips along a path into a cup
s = "hook"; tsp = aw(s, "spit"); twl = aw(s, "whole life"); tev = aw(s, "every single"); tad = aw(s, "added up")
scenes[s] = scene_file(s, f"""
#hk-t {{ top:160px; font-size:88px; line-height:1.05; }}
#hk-svg {{ position:absolute; left:0; top:300px; }}
#hk-o {{ position:absolute; left:690px; top:640px; opacity:0; {GH} font-size:84px; color:{C['blue']}; }}
""", f"""
  <div id="hk-t" class="h1">A lifetime of <span class="hl">spit?</span></div>
  <svg id="hk-svg" width="{W}" height="640" viewBox="0 0 {W} 640" data-layout-ignore>
    <path class="hk-m" d="M300,150 Q540,40 780,150" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path class="hk-m" d="M300,150 Q540,330 780,150" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path id="hk-tg" d="M420,205 Q540,150 660,205 Q540,270 420,205 Z" fill="{PINK}" stroke="{K}" stroke-width="6" opacity="0"/>
    <path id="hk-route" d="M540,250 Q560,330 540,420 L540,500" fill="none" stroke="none"/>
    <path id="hk-trail" d="M540,250 Q560,330 540,420 L540,500" stroke="{SPIT}" stroke-width="10" stroke-dasharray="4 18" fill="none" stroke-linecap="round"/>
    <path class="hk-cup" d="M450,470 L470,620 L610,620 L630,470" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <rect id="hk-cw" x="462" y="560" width="156" height="56" fill="{SPIT}" opacity="0"/>
    {drop("hk-d")}
  </svg>
  <div id="hk-o">DRIP!</div>
""", J("""
ink(".hk-m", 0.05, 0.6, {stagger:0.15});
tl.fromTo("#hk-tg", {opacity:0}, {opacity:1, duration:0.3}, 0.6);
pop("#hk-t", @ts, {from:{scale:1.4}, to:{}});
ink(".hk-cup", @tw, 0.4);
tl.fromTo("#hk-d", {opacity:0}, {opacity:1, duration:0.2}, @te);
ink("#hk-trail", @te, 0.8);
along("#hk-d", "#hk-route", @te, 1.0, {ease:"power2.in"});
tl.fromTo("#hk-cw", {opacity:0}, {opacity:1, duration:0.3}, @te2);
tl.set("#hk-o", {opacity:1}, @te2); pop("#hk-o", @te2, {from:{rotation:-20, scale:1.6}, to:{rotation:-8}});
""", ts=tsp - 0.2, tw=twl - 0.3, te=tev - 0.2, te2=tev + 0.8))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "one bathtub"); t2 = aw(s, "a hundred"); t3 = aw(s, "two swimming")
notes = [("a", "1 bathtub?", -6, 110, SPIT), ("b", "100 bathtubs?", 4, 405, C['hi']), ("c", "2 swimming pools?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:60px;line-height:1.05;padding:70px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3 - 0.2))

# 3 INTRO — logo + a measuring jug inks itself
s = "intro"; tmw = aw(s, "Max Wise"); tme = aw(s, "measure every")
ticks = "".join(f'<path class="in-tk" d="M470,{60 + i*28} L{510 if i % 2 else 530},{60 + i*28}" stroke="{C["blue"]}" stroke-width="6" stroke-linecap="round"/>' for i in range(5))
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:62px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Every drop counts!</span></div>
  <svg class="abs" style="left:0;top:500px" width="{W}" height="230" data-layout-ignore>
    <path class="in-j" d="M450,30 L470,210 L610,210 L630,30" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="in-j" d="M630,70 Q690,80 680,140 Q672,180 618,175" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    {ticks}
  </svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tm); ink(".in-j", @tm, 0.4, {stagger:0.15}); ink(".in-tk", @tm2, 0.15, {stagger:0.07});
""", tmw=tmw, tu=tmw + 0.3, tm=tme - 0.4, tm2=tme))

# 4 GLANDS — front face cutaway; three pairs of glands pop, ducts ink to the mouth
s = "glands"; tth = aw(s, "three pairs"); tbg = aw(s, "big glands"); tmw = aw(s, "mouth wet")
GL = [("pa", 250, 330, 52, 78, "near the ears"), ("pa", 830, 330, 52, 78, ""), ("sm", 360, 560, 58, 36, "under the jaw"), ("sm", 720, 560, 58, 36, ""), ("sl", 470, 520, 40, 22, "under the tongue"), ("sl", 610, 520, 40, 22, "")]
gl = "".join(f'<ellipse class="gl-g gl-{k}" cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{GLAND}" stroke="{K}" stroke-width="5"/>' for k, x, y, rx, ry, _ in GL)
ducts = "".join(f'<path class="gl-du" d="M{x},{y} Q{(x + 540)/2:.0f},{(y + 460)/2 + 30:.0f} {540 + (40 if x > 540 else -40)},{462}" stroke="{C["blue"]}" stroke-width="5" stroke-dasharray="1 0" fill="none" stroke-linecap="round"/>' for k, x, y, *_ in GL)
scenes[s] = scene_file(s, f"""
#gl-svg {{ position:absolute; left:0; top:200px; }}
#gl-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#gl-w {{ position:absolute; left:0; right:0; top:840px; text-align:center; opacity:0; padding-left:300px; }}
""", f"""
  <div id="gl-c"><span class="chip" style="background:#FFF3C4">3 pairs of spit glands</span></div>
  <svg id="gl-svg" width="{W}" height="640" viewBox="0 0 {W} 640" data-layout-ignore>
    <path id="gl-face" d="M540,60 Q800,60 820,300 Q830,520 540,620 Q250,520 260,300 Q280,60 540,60 Z" fill="{SKIN}" stroke="{K}" stroke-width="8" stroke-linejoin="round"/>
    <circle cx="450" cy="260" r="14" fill="{K}"/><circle cx="630" cy="260" r="14" fill="{K}"/>
    <path d="M460,450 Q540,500 620,450 Q540,480 460,450 Z" fill="{PINK}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    {ducts}
    {gl}
  </svg>
  <div id="gl-w"><span class="chip" style="background:{SPIT}">keeps your mouth wet</span></div>
""", J("""
ink("#gl-face", 0.05, 0.7);
tl.set("#gl-c", {opacity:1}, @tt); pop("#gl-c .chip", @tt, {from:{rotation:-10}, to:{rotation:-3}});
pop(".gl-pa", @tt, {from:{transformOrigin:"50% 50%"}, to:{stagger:0.12}}); pop(".gl-sm", @tt2, {from:{transformOrigin:"50% 50%"}, to:{stagger:0.12}}); pop(".gl-sl", @tt3, {from:{transformOrigin:"50% 50%"}, to:{stagger:0.12}});
ink(".gl-du", @tm, 0.4, {stagger:0.06});
tl.set("#gl-w", {opacity:1}, @tm); pop("#gl-w .chip", @tm, {from:{rotation:8}, to:{rotation:2}});
""", tt=tth - 0.1, tt2=tth + 0.35, tt3=tbg, tm=tmw - 0.4))

# 5 DAY — honest range band on a litre scale; marker lands on one litre
s = "day"; th = aw(s, "half a"); toh = aw(s, "one and a half"); tol = aw(s, "one litre")
X = lambda l: 140 + l * 400
tk = "".join(f'<path d="M{X(v):.0f},470 L{X(v):.0f},{500 if v in (0, 1, 2) else 490}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for v in (0, .5, 1, 1.5, 2))
lb = "".join(f'<text x="{X(v):.0f}" y="560" text-anchor="middle" style="{GH}font-size:46px" fill="{K}">{t}</text>' for v, t in ((0, "0"), (.5, "0.5 L"), (1, "1 L"), (1.5, "1.5 L"), (2, "2 L")))
hatch = "".join(f'<path d="M{x},{380} L{x + 40},{450}" stroke="{C["blue"]}" stroke-width="4" opacity=".5"/>' for x in range(340, 740, 22))
scenes[s] = scene_file(s, f"""
#dy-svg {{ position:absolute; left:0; top:200px; }}
#dy-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#dy-a {{ position:absolute; left:0; right:0; top:820px; text-align:center; opacity:0; padding-left:240px; }}
#dy-band {{ opacity:0; }}
""", f"""
  <div id="dy-c"><span class="chip" style="background:#FFFFFF">spit per day</span></div>
  <svg id="dy-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <defs><clipPath id="dy-bc"><rect x="340" y="380" width="400" height="70"/></clipPath></defs>
    <g id="dy-band"><rect id="dy-br" x="340" y="380" width="400" height="70" rx="10" fill="{SPIT}" stroke="{K}" stroke-width="5"/><g clip-path="url(#dy-bc)">{hatch}</g></g>
    <path id="dy-ax" d="M120,470 L960,470" stroke="{K}" stroke-width="7" stroke-linecap="round"/>
    {tk}{lb}
    <g id="dy-mk"><path d="M540,370 L515,320 L565,320 Z" fill="{C['red']}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/></g>
    <g id="dy-bot" opacity="0">
      <path d="M515,80 L565,80 L565,110 Q600,130 600,170 L600,300 Q600,312 588,312 L492,312 Q480,312 480,300 L480,170 Q480,130 515,110 Z" fill="{SPIT}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
      <rect x="508" y="58" width="64" height="26" rx="6" fill="{C['blue']}" stroke="{K}" stroke-width="5"/>
      <text x="540" y="235" text-anchor="middle" style="{GH}font-size:52px" fill="{K}">1 L</text>
    </g>
  </svg>
  <div id="dy-a"><span class="chip" style="background:{C['hi']};font-size:60px">about 1 litre a day</span></div>
""", J("""
ink("#dy-ax", 0.05, 0.5);
tl.set("#dy-c", {opacity:1}, 0.3); pop("#dy-c .chip", 0.3, {from:{rotation:-10}, to:{rotation:-3}});
tl.set("#dy-band", {opacity:1}, @th);
tl.fromTo("#dy-band", {scaleX:0.02, svgOrigin:"340 415"}, {scaleX:0.5, svgOrigin:"340 415", duration:0.4, ease:"back.out(1.6)"}, @th);
tl.to("#dy-band", {scaleX:1, svgOrigin:"340 415", duration:0.6, ease:"back.out(1.4)"}, @to);
tl.fromTo("#dy-mk", {opacity:0, y:-120}, {opacity:1, y:0, duration:0.5, ease:"bounce.out"}, @tl);
tl.fromTo("#dy-bot", {opacity:0, scale:0.4, svgOrigin:"540 312"}, {opacity:1, scale:1, svgOrigin:"540 312", duration:0.5, ease:"back.out(2)"}, @tl2);
tl.set("#dy-a", {opacity:1}, @tl2); pop("#dy-a .chip", @tl2, {from:{rotation:8}, to:{rotation:2}});
""", th=th - 0.1, to=toh - 0.1, tl=tol - 0.6, tl2=tol - 0.2))

# 6 YEAR — 365 dots fill a calendar grid; a counter runs to 365 litres
s = "year"; toy = aw(s, "one year"); t365 = aw(s, "three hundred"); tend = aw(s, "sixty five")
dots = "".join(f'<circle class="yr-d" cx="{150 + (i % 25) * 32}" cy="{30 + (i // 25) * 34}" r="11" fill="{SPIT}" stroke="{K}" stroke-width="3"/>' for i in range(365))
scenes[s] = scene_file(s, f"""
#yr-n {{ position:absolute; left:0; right:0; top:160px; text-align:center; {GH} font-size:120px; line-height:1; }}
#yr-l {{ position:absolute; left:0; right:0; top:300px; text-align:center; }}
#yr-svg {{ position:absolute; left:0; top:380px; }}
""", f"""
  <div id="yr-n"><span id="yr-v" class="hl">0 L</span></div>
  <div id="yr-l"><span class="chip" style="background:#FFFFFF">1 year: 1 dot = 1 litre</span></div>
  <svg id="yr-svg" width="{W}" height="540" viewBox="0 0 {W} 540" data-layout-ignore>{dots}</svg>
""", J("""
pop("#yr-l .chip", @ty, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo(".yr-d", {opacity:0}, {opacity:1, duration:0.05, stagger:@st}, @ty);
count("#yr-v", 0, 365, @ty, @dd, v => Math.round(v) + " L");
pop("#yr-n", @te, {from:{scale:1.3}, to:{}});
""", ty=toy - 0.1, st=(tend + 0.2 - toy) / 365, dd=tend + 0.25 - toy, te=tend + 0.2))

# 7 TUBS — one bathtub = 150 L; two tubs fill and a third starts
s = "tubs"; tab = aw(s, "average bathtub"); t150 = aw(s, "one hundred fifty"); ttw = aw(s, "two tubs"); tey = aw(s, "every year")
tA, bA = tub("tb1", 220, 470); tB, _ = tub("tb2", 540, 470); tC, _ = tub("tb3", 860, 470)
scenes[s] = scene_file(s, f"""
#tb-svg {{ position:absolute; left:0; top:180px; }}
#tb-c {{ position:absolute; left:80px; top:350px; opacity:0; }}
#tb-y {{ position:absolute; left:0; right:0; top:870px; text-align:center; opacity:0; padding-left:240px; }}
#tb-g2, #tb-g3 {{ opacity:0; }}
""", f"""
  <svg id="tb-svg" width="{W}" height="640" viewBox="0 0 {W} 640" data-layout-ignore>
    <g id="tb-g1">{tA}</g><g id="tb-g2">{tB}</g><g id="tb-g3">{tC}</g>
    <text id="tb-sp" x="220" y="615" text-anchor="middle" style="{GH}font-size:56px" fill="{C['blue']}" opacity="0">SPLASH!</text>
  </svg>
  <div id="tb-c"><span class="chip" style="background:{C['hi']};font-size:60px">1 tub = 150 L</span></div>
  <div id="tb-y"><span class="chip" style="background:{SPIT};font-size:58px">more than 2 tubs a year!</span></div>
""", J("""
pop("#tb-g1", @ta, {from:{scale:0.3, svgOrigin:"220 470"}, to:{svgOrigin:"220 470"}});
tl.fromTo("#tb1-w", {scaleY:0, svgOrigin:"220 580"}, {scaleY:1, svgOrigin:"220 580", duration:1.0, ease:"power2.out"}, @ta2);
tl.set("#tb-c", {opacity:1}, @t15); pop("#tb-c .chip", @t15, {from:{rotation:-12}, to:{rotation:-3}});
tl.fromTo("#tb-sp", {opacity:0}, {opacity:1, duration:0.2}, @t15b);
tl.to("#tb-c", {opacity:0, duration:0.3}, @tw0);
tl.fromTo("#tb-g2", {opacity:0, y:-60}, {opacity:1, y:0, duration:0.4, ease:"back.out(2)"}, @tw0);
tl.fromTo("#tb2-w", {scaleY:0, svgOrigin:"540 580"}, {scaleY:1, svgOrigin:"540 580", duration:0.7, ease:"power2.out"}, @tw);
tl.fromTo("#tb-g3", {opacity:0, y:-60}, {opacity:1, y:0, duration:0.4, ease:"back.out(2)"}, @tw2);
tl.fromTo("#tb3-w", {scaleY:0, svgOrigin:"860 580"}, {scaleY:0.4, svgOrigin:"860 580", duration:0.6, ease:"power2.out"}, @tw3);
tl.set("#tb-y", {opacity:1}, @ty); pop("#tb-y .chip", @ty, {from:{rotation:8}, to:{rotation:2}});
""", ta=max(0.05, tab - 0.4), ta2=tab, t15=t150 - 0.1, t15b=t150 + 0.6, tw0=ttw - 1.0, tw=ttw - 0.5, tw2=ttw, tw3=ttw + 0.3, ty=ttw + 0.3))

# 8 LIFE — a year ruler 0..80 with a drop running along it; litres counter to 30,000
s = "life"; tey = aw(s, "eighty years"); tad = aw(s, "adds up"); t30 = aw(s, "thirty thousand")
RX = lambda y: 140 + y * 10
rt = "".join(f'<path d="M{RX(y)},{560} L{RX(y)},{600 if y % 20 == 0 else 585}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for y in range(0, 81, 10))
rl = "".join(f'<text x="{RX(y)}" y="650" text-anchor="middle" style="{GH}font-size:44px" fill="{K}">{y}</text>' for y in range(0, 81, 20))
scenes[s] = scene_file(s, f"""
#lf-n {{ position:absolute; left:0; right:0; top:260px; text-align:center; {GH} font-size:130px; line-height:1; }}
#lf-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#lf-svg {{ position:absolute; left:0; top:200px; }}
#lf-r {{ position:absolute; left:0; right:0; top:440px; text-align:center; opacity:0; }}
""", f"""
  <div id="lf-c"><span class="chip" style="background:#FFFFFF">about 80 years of spit</span></div>
  <div id="lf-n"><span id="lf-v" class="hl">0 L</span></div>
  <div id="lf-r"><span class="chip" style="background:{SPIT};font-size:54px">roughly</span></div>
  <svg id="lf-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <rect id="lf-rul" x="120" y="520" width="840" height="40" rx="6" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>
    {rt}{rl}
    <text x="940" y="695" text-anchor="end" style="{GH}font-size:40px" fill="{C['muted']}">years</text>
    <path id="lf-route" d="M140,490 L940,490" fill="none" stroke="none"/>
    <path id="lf-trail" d="M140,505 L940,505" stroke="{WATER}" stroke-width="12" fill="none" stroke-linecap="round"/>
    {drop("lf-d")}
  </svg>
""", J("""
tl.fromTo("#lf-rul", {opacity:0}, {opacity:1, duration:0.3}, 0.05);
tl.set("#lf-c", {opacity:1}, @te); pop("#lf-c .chip", @te, {from:{rotation:-10}, to:{rotation:-3}});
ink("#lf-trail", @te, @dd, {ease:"none"});
along("#lf-d", "#lf-route", @te, @dd, {ease:"none"});
count("#lf-v", 0, 30000, @te, @dd, v => fmtInt(Math.round(v/100)*100) + " L");
tl.set("#lf-r", {opacity:1}, @tr); pop("#lf-r .chip", @tr, {from:{rotation:10}, to:{rotation:3}});
pop("#lf-n", @t3, {from:{scale:1.25}, to:{}});
""", te=tey - 0.2, dd=t30 + 0.6 - (tey - 0.2), tr=t30 - 0.7, t3=t30 + 0.5))

# 9 PILE — 200 mini tubs fill the page; a bracket marks the low end (about 100)
s = "pile"; t200 = aw(s, "two hundred"); tlo = aw(s, "low end"); t100 = aw(s, "a hundred tubs")
mini = ""
for i in range(200):
    cx = 140 + (i % 20) * 42; cy = 360 + (i // 20) * 40
    mini += f'<path class="pl-t" d="M{cx-16},{cy-8} L{cx+16},{cy-8} L{cx+13},{cy+8} Q{cx},{cy+13} {cx-13},{cy+8} Z" fill="{WATER}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>'
scenes[s] = scene_file(s, f"""
#pl-n {{ position:absolute; left:0; right:0; top:165px; text-align:center; {GH} font-size:96px; line-height:1; opacity:0; }}
#pl-svg {{ position:absolute; left:0; top:0; }}
#pl-lo {{ position:absolute; left:420px; top:745px; opacity:0; }}
""", f"""
  <div id="pl-n"><span class="hl">about 200 bathtubs!</span></div>
  <svg id="pl-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {mini}
    <rect id="pl-br" x="108" y="336" width="864" height="196" rx="16" fill="none" stroke="{C['red']}" stroke-width="7" stroke-dasharray="18 10"/>
    <text x="640" y="900" text-anchor="middle" style="{GH}font-size:44px" fill="{C['muted']}">1 tub = 150 litres</text>
  </svg>
  <div id="pl-lo"><span class="chip" style="background:#FFC9C2;font-size:52px;transform:rotate(-3deg)">low end: about 100</span></div>
""", J("""
tl.fromTo(".pl-t", {opacity:0}, {opacity:1, duration:0.05, stagger:0.006}, @t2a);
tl.set("#pl-n", {opacity:1}, @t2); pop("#pl-n", @t2, {from:{scale:1.4}, to:{}});
ink("#pl-br", @tl, 0.7);
tl.to(".pl-t:nth-of-type(n+101)", {opacity:0.25, duration:0.4}, @tl);
tl.set("#pl-lo", {opacity:1}, @t1); pop("#pl-lo .chip", @t1, {from:{rotation:-14, scale:1.3}, to:{rotation:-3}});
""", t2a=max(0.05, t200 - 1.0), t2=t200 - 0.1, tl=tlo - 0.2, t1=t100 - 0.2))

# 10 MYTH — "2 swimming pools" crossed out; an Olympic pool dwarfs your lifetime of spit
s = "myth"; tsw = aw(s, "two swimming"); tol = aw(s, "Olympic pool"); tmi = aw(s, "half million"); tnc = aw(s, "not even close")
scenes[s] = scene_file(s, f"""
#my-p {{ position:absolute; left:0; right:0; top:165px; text-align:center; {GH} font-size:84px; color:{C['pencil']}; opacity:0; }}
#my-svg {{ position:absolute; left:0; top:150px; }}
#my-l {{ position:absolute; left:0; right:0; top:330px; text-align:center; opacity:0; }}
#my-y {{ position:absolute; left:640px; top:810px; opacity:0; }}
#my-nc {{ position:absolute; left:180px; top:520px; opacity:0; {GH} font-size:100px; color:{C['red']}; }}
""", f"""
  <div id="my-p">2 swimming pools?</div>
  <svg id="my-svg" width="{W}" height="810" viewBox="0 0 {W} 810" data-layout-ignore>
    <path id="my-st" d="M200,80 L880,50" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <g id="my-pool" opacity="0">
      <rect x="110" y="270" width="860" height="380" rx="14" fill="{WATER}" stroke="{K}" stroke-width="8"/>
      <path d="M110,390 L970,390 M110,510 L970,510" stroke="#FFFFFF" stroke-width="5" stroke-dasharray="20 14"/>
    </g>
    <rect id="my-sp" x="890" y="575" width="50" height="50" fill="{SPIT}" stroke="{K}" stroke-width="5" opacity="0"/>
    <path id="my-ar" d="M915,560 Q930,520 900,470" stroke="{K}" stroke-width="0" fill="none"/>
  </svg>
  <div id="my-l"><span class="chip" style="background:#FFFFFF;font-size:52px">1 Olympic pool = 2,500,000 L</span></div>
  <div id="my-y"><span class="chip" style="background:{C['hi']};font-size:42px">your lifetime</span></div>
  <div id="my-nc">NOT EVEN CLOSE!</div>
""", J("""
tl.set("#my-p", {opacity:1}, @ts); pop("#my-p", @ts, {from:{rotation:-6}, to:{}});
ink("#my-st", @ts2, 0.4);
tl.fromTo("#my-pool", {opacity:0, scale:0.6, svgOrigin:"540 460"}, {opacity:1, scale:1, svgOrigin:"540 460", duration:0.6, ease:"back.out(1.6)"}, @to);
tl.set("#my-l", {opacity:1}, @tm); pop("#my-l .chip", @tm, {from:{rotation:-10}, to:{rotation:-2}});
pop("#my-sp", @tm2, {from:{transformOrigin:"50% 50%", scale:3}, to:{}});
tl.set("#my-y", {opacity:1}, @tm2); pop("#my-y .chip", @tm2, {from:{rotation:8}, to:{rotation:-4}});
tl.set("#my-nc", {opacity:1}, @tn); pop("#my-nc", @tn, {from:{rotation:-20, scale:1.6}, to:{rotation:-6}});
""", ts=tsw - 0.2, ts2=tsw + 0.9, to=tol - 0.3, tm=tmi - 0.6, tm2=tmi + 0.5, tn=tnc - 0.1))

# 11 BONUS — spit at work: starch breaks into crumbs; a shield inks around a tooth
s = "bonus"; tbu = aw(s, "is busy"); tst = aw(s, "starch"); tte = aw(s, "protect your")
rnd = random.Random(27)
crumbs = "".join(f'<circle class="bn-cr" cx="{rnd.uniform(110, 450):.0f}" cy="{rnd.uniform(470, 640):.0f}" r="{rnd.uniform(7, 13):.0f}" fill="{C["hi"]}" stroke="{K}" stroke-width="3" opacity="0"/>' for _ in range(16))
scenes[s] = scene_file(s, f"""
#bn-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#bn-svg {{ position:absolute; left:0; top:180px; }}
#bn-a {{ position:absolute; left:110px; top:800px; opacity:0; }}
#bn-b {{ position:absolute; left:610px; top:800px; opacity:0; }}
""", f"""
  <div id="bn-c"><span class="chip" style="background:{SPIT};font-size:60px">spit is busy!</span></div>
  <svg id="bn-svg" width="{W}" height="680" viewBox="0 0 {W} 680" data-layout-ignore>
    <path id="bn-br" d="M140,500 L140,330 Q100,250 180,215 Q280,180 380,215 Q460,250 420,330 L420,500 Z" fill="#F4C27A" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path d="M170,330 Q170,250 280,245 Q390,250 390,330 L390,480 L170,480 Z" fill="#FFF0CC"/>
    {crumbs}
    <path id="bn-to" d="M700,300 Q700,220 780,230 Q820,240 860,230 Q940,220 940,300 Q940,380 905,420 L885,560 Q875,590 860,560 L835,460 Q820,440 805,460 L780,560 Q765,590 755,560 L735,420 Q700,380 700,300 Z" fill="#FFFFFF" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path class="bn-sh" d="M820,140 Q700,150 650,200" stroke="{C['blue']}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path class="bn-sh" d="M820,140 Q940,150 990,200" stroke="{C['blue']}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path class="bn-sh" d="M650,200 Q620,450 820,640" stroke="{C['blue']}" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path class="bn-sh" d="M990,200 Q1020,450 820,640" stroke="{C['blue']}" stroke-width="9" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="bn-a"><span class="chip" style="background:#FFF3C4;font-size:44px;transform:rotate(-3deg)">breaks down starch</span></div>
  <div id="bn-b"><span class="chip" style="background:#FFFFFF;font-size:44px;transform:rotate(3deg)">guards your teeth</span></div>
""", J("""
tl.set("#bn-c", {opacity:1}, @tb); pop("#bn-c .chip", @tb, {from:{rotation:-10}, to:{rotation:-3}});
ink("#bn-br", 0.1, 0.6); ink("#bn-to", 0.3, 0.6);
tl.fromTo(".bn-cr", {opacity:0, y:-80}, {opacity:1, y:0, duration:0.4, stagger:0.04, ease:"bounce.out"}, @ts);
tl.set("#bn-a", {opacity:1}, @ts); pop("#bn-a .chip", @ts, {from:{rotation:-14}, to:{rotation:-3}});
ink(".bn-sh", @tt, 0.5, {stagger:0.08});
tl.set("#bn-b", {opacity:1}, @tt); pop("#bn-b .chip", @tt, {from:{rotation:14}, to:{rotation:3}});
""", tb=tbu - 0.4, ts=tst - 0.3, tt=tte - 0.2))

# 12 OUTRO — callback: about 200 bathtubs in one lifetime (Max centre stage, keep y < 620)
s = "outro"; t2h = aw(s, "two hundred"); tli = aw(s, "one lifetime"); tsc = aw(s, "stay curious")
tO, _ = tub("ou", 540, 330, w=200)
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-sc {{ top:440px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:58px;background:{SPIT}">about 200 bathtubs per life</span></div>
  <svg id="ou-svg" width="{W}" height="440" viewBox="0 0 {W} 440" data-layout-ignore><g id="ou-g" opacity="0">{tO}</g></svg>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
tl.set("#ou-a", {opacity:1}, @t2); pop("#ou-a .chip", @t2, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo("#ou-g", {opacity:0, y:-40}, {opacity:1, y:0, duration:0.4, ease:"back.out(2)"}, @tl);
tl.fromTo("#ou-w", {scaleY:0, svgOrigin:"540 420"}, {scaleY:1, svgOrigin:"540 420", duration:0.8}, @tl);
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", t2=t2h - 0.3, tl=tli - 0.3, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "how much"), SC["guess"]["start"] + 0.2)
point(g("guess", "one bathtub"), 3.0)
wave(g("intro", "I'm Max"))
point(g("glands", "three pairs"), 1.2)
point(g("day", "one litre"), 1.2)
wow(g("year", "three hundred"), 1.2)
point(g("tubs", "one hundred fifty"), 1.2)
wow(g("life", "thirty thousand"), 1.4)
wow(g("pile", "two hundred"), 1.4)
think(g("myth", "some people"), g("myth", "but one"))
wow(g("myth", "not even close"), 1.2)
point(g("bonus", "protect your"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "spit"), 0.35), ("pop.mp3", A("hook", "added up"), 0.4),
        ("pop.mp3", A("guess", "one bathtub"), 0.45), ("pop.mp3", A("guess", "a hundred"), 0.45), ("pop.mp3", A("guess", "two swimming"), 0.5),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("ping.mp3", A("glands", "three pairs"), 0.4),
        ("click.mp3", A("day", "one litre"), 0.45), ("riser.mp3", A("year", "one year"), 0.3),
        ("ping.mp3", A("tubs", "one hundred fifty"), 0.4), ("impact-bass-1.mp3", A("life", "thirty thousand"), 0.45),
        ("sparkle.mp3", A("pile", "two hundred"), 0.4), ("click-soft.mp3", A("myth", "swimming pools") + 0.4, 0.45),
        ("impact-bass-2.mp3", A("myth", "not even close"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
