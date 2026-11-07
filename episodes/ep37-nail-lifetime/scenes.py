# MAX WISE ep37 — How long would your fingernails grow if you never cut them?
# Sources: Yaemsiri et al. 2010 J Eur Acad Dermatol Venereol (PubMed 19744178): fingernails 3.47 mm/month, toenails 1.62 mm/month,
# little fingernail slower than the others. Cleveland Clinic "Nail anatomy": fingernails ~3 mm/month, toenails ~1.5 mm/month.
# Maths: 3.47 x 12 = 41.6 mm/yr (~4 cm); ~0.11 mm/day (~1 sheet of paper); x 80 yr = 3.33 m; x 10 nails = 33.3 m (~10 stories); 1.62/3.47 = 0.47.
# Kit: 2D only. ink (hook, intro, room, real, outro), morph (hook, life, real), along (life).
# === SCENES ===
import math
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#F6D2B0"; NAIL = "#F9C9D4"; TAPE = "#BFE3F7"; PAPER = "#FFFFFF"
SW = f'stroke="{K}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'

def finger_tip(x0, x1, ytop, ybot):
    r = (x1 - x0) / 2
    return f"M{x0},{ybot} L{x0},{ytop+r} Q{x0},{ytop} {x0+r},{ytop} Q{x1},{ytop} {x1},{ytop+r} L{x1},{ybot}"

def ruler_v(rid, x, ybase, px, n, unit, every=1, cls=""):
    # vertical ruler body + ticks + labels (left side ticks); returns svg string
    top = ybase - px * n
    s = f'<g id="{rid}"{cls}>'
    for k in range(0, n * 2 + 1):
        y = ybase - px * k / 2
        ln = 34 if k % 2 == 0 else 18
        s += f'<path d="M{x},{y:.0f} L{x+ln},{y:.0f}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>'
        if k % 2 == 0 and (k // 2) % every == 0:
            s += f'<text x="{x+44}" y="{y+13:.0f}" font-family="Patrick Hand" font-size="38" fill="{K}">{k//2}</text>'
    s += f'<text x="{x+40}" y="{top-24:.0f}" font-family="Gochi Hand" font-size="40" fill="{C["blue"]}">{unit}</text></g>'
    return s

# 1 HOOK — a hand inks itself, scissors get crossed out, nails morph into long curly claws
s = "hook"; tnc = aw(s, "never cut"); thl = aw(s, "how long"); twi = aw(s, "what if")
fingers = [(500, 470, 70), (580, 430, 70), (660, 440, 70), (738, 490, 62)]
fh = "".join(f'<path class="hk-hand" d="{finger_tip(cx-w/2, cx+w/2, ty, 712)}" fill="{SKIN}" {SW}/>' for cx, ty, w in fingers)
palm = f'<path class="hk-hand" d="M466,700 L466,870 Q472,935 545,942 L700,942 Q772,935 772,870 L772,700 Z" fill="{SKIN}" {SW}/>'
thumb = f'<path class="hk-hand" d="M468,820 Q402,792 392,722 Q388,676 424,676 Q458,680 470,734" fill="{SKIN}" {SW}/>'
nails = ""; longs = ""
for i, (cx, ty, w) in enumerate(fingers):
    nw = w * 0.31
    nails += f'<path id="hk-n{i}" class="hk-n" d="M{cx-nw:.0f},{ty+52} L{cx-nw:.0f},{ty+24} Q{cx},{ty+4} {cx+nw:.0f},{ty+24} L{cx+nw:.0f},{ty+52} Q{cx},{ty+60} {cx-nw:.0f},{ty+52} Z" fill="{NAIL}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>'
    longs += f'<path id="hk-L{i}" d="M{cx-nw:.0f},{ty+52} L{cx-nw:.0f},{ty-50} Q{cx-nw+8:.0f},{ty-165} {cx+68:.0f},{ty-150} Q{cx+22:.0f},{ty-110} {cx+nw:.0f},{ty-46} L{cx+nw:.0f},{ty+52} Q{cx},{ty+60} {cx-nw:.0f},{ty+52} Z" fill="none" stroke="none"/>'
scis = (f'<g id="hk-sc"><circle cx="880" cy="780" r="26" fill="none" {SW}/><circle cx="952" cy="792" r="26" fill="none" {SW}/>'
        f'<path d="M898,760 L1000,640" {SW} fill="none"/><path d="M940,770 L890,630" {SW} fill="none"/></g>')
scenes[s] = scene_file(s, f"""
#hk-t {{ top:150px; font-size:76px; }}
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-hl {{ position:absolute; left:820px; top:420px; {GH} font-size:64px; color:{C['red']}; opacity:0; }}
.hk-hand {{ fill-opacity:0; }}
""", f"""
  <div id="hk-t" class="h1">Never <span class="hl">cut</span> your nails?</div>
  <svg id="hk-svg" width="{W}" height="980" data-layout-ignore>
    {longs}{thumb}{palm}{fh}{nails}
    <g id="hk-scw" opacity="0">{scis}</g>
    <path id="hk-x1" d="M845,620 L1020,820" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path id="hk-x2" d="M1020,620 L845,820" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="hk-hl">How long?!</div>
""", J("""
ink(".hk-hand", 0.05, 0.45, {stagger:0.08});
tl.fromTo(".hk-hand", {fillOpacity:0}, {fillOpacity:1, duration:0.3}, 0.6);
tl.fromTo(".hk-n", {opacity:0}, {opacity:1, duration:0.25, stagger:0.06}, 0.8);
rise("#hk-t", @tw);
pop("#hk-scw", @tsc, {from:{rotation:-20}, to:{rotation:0}});
ink("#hk-x1", @tnc, 0.2); ink("#hk-x2", @tnc2, 0.2);
for (let i=0;i<4;i++) morph("#hk-n"+i, "#hk-L"+i, @tm+i*0.08, 0.7, {ease:"back.out(1.4)"});
pop("#hk-hl", @thl, {from:{rotation:20}, to:{rotation:8}});
""", tw=twi - 0.1, tsc=twi + 0.1, tnc=tnc, tnc2=tnc + 0.2, tm=thl - 0.4, thl=thl))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "a pencil"); t2 = aw(s, "tall as you"); t3 = aw(s, "taller than")
notes = [("a", "A pencil?", -6, 95, "#FFE27A"), ("b", "As tall<br>as you?", 4, 400, TAPE), ("c", "Taller than<br>a room?", -3, 705, "#F7C6C6")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:285px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;{GH}font-size:56px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.4, t2=t2 - 0.4, t3=t3 - 0.15))

# 3 INTRO — logo + underline + chip + a ruler that inks itself (keep y < 620: Max is centre stage)
s = "intro"; tmw = aw(s, "Max Wise"); tgr = aw(s, "grab a ruler")
rticks = "".join(f'<path class="in-tk" d="M{300+k*24},500 L{300+k*24},{530 if k%5 else 548}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(1, 20))
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ position:absolute; left:0; right:0; top:390px; text-align:center; }}
#in-sub .chip {{ font-size:56px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <rect id="in-rb" x="300" y="500" width="480" height="80" rx="8" fill="{C['hi']}" fill-opacity="0" {SW}/>
    {rticks}
  </svg>
  <div id="in-sub"><span class="chip">Let's grab a ruler!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
pop("#in-sub", @tc, {from:{rotation:-8}, to:{rotation:-2}});
ink("#in-rb", @tr, 0.5); tl.to("#in-rb", {fillOpacity:1, duration:0.3}, @tr2);
ink(".in-tk", @tr2, 0.15, {stagger:0.03});
""", tmw=tmw, tu=tmw + 0.3, tc=tgr - 0.2, tr=tgr, tr2=tgr + 0.4))

# 4 DAY — fingertip, magnifier pushes in on the nail edge: a 0.1 mm sliver; a sheet of paper drops beside it
s = "day"; tfn = aw(s, "your fingernails"); tte = aw(s, "a tenth"); tev = aw(s, "every day"); tsp = aw(s, "sheet of paper")
MX, MY, MR = 660, 570, 250
mticks = "".join(f'<path d="M{480+k*60},700 L{480+k*60},{730 if k%2 else 745}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(0, 8))
scenes[s] = scene_file(s, f"""
#dy-t {{ top:150px; font-size:76px; opacity:0; }}
#dy-svg {{ position:absolute; left:0; top:0; }}
#dy-p {{ position:absolute; left:410px; top:850px; width:500px; text-align:center; opacity:0; }}
#dy-p .pill {{ font-size:46px; }}
""", f"""
  <div id="dy-t" class="h1">≈ <span class="hl">0.1 mm</span> a day</div>
  <svg id="dy-svg" width="{W}" height="980" data-layout-ignore>
    <defs><clipPath id="dy-clip"><circle cx="{MX}" cy="{MY}" r="{MR}"/></clipPath>
      <pattern id="dy-h" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="14" height="14" fill="{C['hi']}"/><path d="M0,0 L0,14" stroke="{C['red']}" stroke-width="4"/></pattern></defs>
    <g id="dy-fing">
      <path d="{finger_tip(170, 290, 400, 760)}" fill="{SKIN}" {SW}/>
      <path d="M196,470 L196,430 Q230,404 264,430 L264,470 Q230,480 196,470 Z" fill="{NAIL}" stroke="{K}" stroke-width="4"/>
      <circle cx="230" cy="420" r="34" fill="none" stroke="{C['blue']}" stroke-width="5" stroke-dasharray="8 8"/></g>
    <g id="dy-mag">
      <path d="M262,400 L{MX-MR+30},{MY-160}" stroke="{C['blue']}" stroke-width="4" stroke-dasharray="10 10" fill="none"/>
      <path d="M262,440 L{MX-MR+30},{MY+160}" stroke="{C['blue']}" stroke-width="4" stroke-dasharray="10 10" fill="none"/>
      <circle cx="{MX}" cy="{MY}" r="{MR}" fill="#fff"/>
      <g clip-path="url(#dy-clip)">
        <rect x="380" y="430" width="220" height="230" fill="{NAIL}" stroke="{K}" stroke-width="5"/>
        <rect id="dy-g" x="600" y="430" width="60" height="230" fill="url(#dy-h)" stroke="{K}" stroke-width="5"/>
        <rect id="dy-pp" x="720" y="430" width="60" height="230" fill="{PAPER}" stroke="{C['blue']}" stroke-width="5"/>
        <path d="M420,700 L900,700" stroke="{K}" stroke-width="5"/>{mticks}
        <text x="600" y="790" text-anchor="middle" font-family="Patrick Hand" font-size="36" fill="{K}">0</text>
        <text x="672" y="790" text-anchor="middle" font-family="Patrick Hand" font-size="36" fill="{C['red']}">0.1</text>
        <text id="dy-1d" x="630" y="410" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{C['red']}">1 day</text>
        <text id="dy-pl" x="750" y="410" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{C['blue']}">paper</text>
      </g>
      <circle cx="{MX}" cy="{MY}" r="{MR}" fill="none" stroke="{K}" stroke-width="9"/>
    </g>
  </svg>
  <div id="dy-p"><span class="pill">≈ 1 sheet of paper</span></div>
""", J("""
pop("#dy-fing", @tf, {from:{scale:0.6, transformOrigin:"50% 50%"}, to:{}});
tl.fromTo("#dy-mag", {opacity:0, scale:0.15, svgOrigin:"230 420"}, {opacity:1, scale:1, svgOrigin:"230 420", duration:0.6, ease:"power3.out"}, @tm);
tl.fromTo("#dy-g", {scaleX:0, svgOrigin:"600 545"}, {scaleX:1, svgOrigin:"600 545", duration:0.6, ease:"power2.out"}, @tg);
tl.fromTo("#dy-1d", {opacity:0}, {opacity:1, duration:0.2}, @tg2);
rise("#dy-t", @tg);
tl.fromTo("#dy-pp", {y:-420, opacity:0}, {y:0, opacity:1, duration:0.5, ease:"bounce.out"}, @tp);
tl.fromTo("#dy-pl", {opacity:0}, {opacity:1, duration:0.2}, @tp2);
pop("#dy-p", @tp2);
""", tf=tfn - 0.05, tm=tfn + 0.6, tg=tte - 0.05, tg2=tte + 0.4, tp=tsp - 0.6, tp2=tsp - 0.1))

# 5 MONTH — 30 slivers drop and stack against a 0-4 mm ruler; day counter to 30
s = "month"; tmo = aw(s, "a month"); t35 = aw(s, "three and a")
RB, PX = 880, 110
sh = 110 * 3.5 / 30
sl = "".join(f'<rect class="mo-s" x="600" y="{RB-(i+1)*sh:.2f}" width="200" height="{sh:.2f}" fill="{NAIL if i%2 else "#F4B3C2"}" stroke="{K}" stroke-width="1.5" opacity="0"/>' for i in range(30))
ticks = "".join(f'<path d="M{560-(30 if k%2==0 else 16)},{RB-PX*k/2:.0f} L560,{RB-PX*k/2:.0f}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{506}" y="{RB-PX*k/2+12:.0f}" text-anchor="end" font-family="Patrick Hand" font-size="36" fill="{K}">{k//2}</text>' if k % 2 == 0 else "") for k in range(0, 9))
st = (t35 - 0.4 - (tmo - 0.1)) / 30
scenes[s] = scene_file(s, f"""
#mo-t {{ top:150px; font-size:74px; }}
#mo-svg {{ position:absolute; left:0; top:0; }}
#mo-c {{ position:absolute; left:820px; top:440px; width:230px; text-align:center; {GH} font-size:52px; line-height:1; }}
#mo-c span {{ font-size:96px; color:{C['blue']}; }}
#mo-a {{ position:absolute; left:790px; top:640px; width:280px; text-align:center; white-space:nowrap; opacity:0; }}
#mo-a .pill {{ font-size:54px; color:{C['red']}; }}
""", f"""
  <div id="mo-t" class="h1">One <span class="hl">month</span> of days</div>
  <svg id="mo-svg" width="{W}" height="960" data-layout-ignore>
    <path d="M560,{RB} L560,{RB-PX*4-30}" {SW} fill="none"/>{ticks}
    <text x="470" y="{RB-PX*4-50}" font-family="Gochi Hand" font-size="40" fill="{C['blue']}">mm</text>
    <path d="M580,{RB+2} L820,{RB+2}" {SW} fill="none"/>
    {sl}
    <path id="mo-br" d="M818,{RB} Q850,{RB} 850,{RB-30} L850,{RB-PX*3.5+30:.0f} Q850,{RB-PX*3.5:.0f} 818,{RB-PX*3.5:.0f}" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="mo-c">day<br><span id="mo-n">0</span></div>
  <div id="mo-a"><span class="pill">≈ 3.5 mm</span></div>
""", J("""
rise("#mo-t", 0.0);
tl.fromTo(".mo-s", {y:-520, opacity:1}, {y:0, opacity:1, duration:0.32, ease:"power2.in", stagger:@st, immediateRender:false}, @ts);
count("#mo-n", 0, 30, @ts, @dc, v => String(Math.round(v)));
ink("#mo-br", @tb, 0.4); pop("#mo-a", @t35, {from:{rotation:-14}, to:{rotation:-4}});
""", st=round(st, 4), ts=tmo - 0.1, dc=t35 - 0.4 - (tmo - 0.1) + 0.3, tb=t35 - 0.3, t35=t35))

# 6 YEAR — the ruler that never leaves (right edge); the nail grows 4 cm while months tick to 12
s = "year"; twy = aw(s, "whole year"); t4 = aw(s, "four centimeters")
YB, YPX, RX = 850, 100, 900
fing = f'<path d="{finger_tip(640, 760, 840, 990)}" fill="{SKIN}" {SW}/>'
scenes[s] = scene_file(s, f"""
#yr-t {{ top:150px; font-size:74px; }}
#yr-svg {{ position:absolute; left:0; top:0; }}
#yr-c {{ position:absolute; left:420px; top:330px; width:200px; text-align:center; {GH} font-size:48px; line-height:1; }}
#yr-c span {{ font-size:96px; color:{C['blue']}; }}
#yr-a {{ position:absolute; left:400px; top:600px; width:250px; text-align:center; opacity:0; }}
#yr-a .pill {{ font-size:66px; color:{C['red']}; }}
""", f"""
  <div id="yr-t" class="h1">One whole <span class="hl">year</span></div>
  <svg id="yr-svg" width="{W}" height="1000" data-layout-ignore>
    <rect x="{RX-14}" y="{YB-YPX*5-70}" width="170" height="{YPX*5+90}" rx="10" fill="{C['hi']}" {SW}/>
    {ruler_v("yr-r", RX, YB, YPX, 5, "cm")}
    {fing}
    <rect id="yr-n" x="668" y="{YB-400}" width="64" height="410" rx="22" fill="{NAIL}" stroke="{K}" stroke-width="5"/>
    <path id="yr-ld" d="M740,{YB-400} L{RX-4},{YB-400}" stroke="{C['red']}" stroke-width="5" stroke-dasharray="12 10" fill="none" opacity="0"/>
  </svg>
  <div id="yr-c">month<br><span id="yr-m">0</span></div>
  <div id="yr-a"><span class="pill">≈ 4 cm</span></div>
""", J("""
rise("#yr-t", 0.0);
tl.fromTo("#yr-n", {scaleY:0.03, svgOrigin:"700 @yb"}, {scaleY:1, svgOrigin:"700 @yb", duration:@dg, ease:"none"}, @tg);
count("#yr-m", 0, 12, @tg, @dg, v => String(Math.round(v)));
tl.to("#yr-ld", {opacity:1, duration:0.2}, @t4); pop("#yr-a", @t4, {from:{rotation:-14}, to:{rotation:-4}});
""", yb=YB, tg=twy - 0.2, dg=t4 - twy + 0.2, t4=t4))

# 7 LIFE — same ruler relabels cm -> m; marker rides a 0-80 year line; nail stub morphs into a 3.3 m nail
s = "life"; tnv = aw(s, "never cut"); t80 = aw(s, "eighty years"); t33 = aw(s, "three point three")
MPX = 125; TOP33 = YB - 3.3 * MPX
scenes[s] = scene_file(s, f"""
#lf-svg {{ position:absolute; left:0; top:0; }}
#lf-a {{ position:absolute; left:380px; top:520px; width:290px; text-align:center; white-space:nowrap; opacity:0; }}
#lf-a .big {{ font-size:84px; color:{C['red']}; }}
#lf-zo {{ position:absolute; left:620px; top:330px; {GH} font-size:48px; color:{C['blue']}; opacity:0; transform:rotate(-6deg); }}
""", f"""
  <svg id="lf-svg" width="{W}" height="1000" data-layout-ignore>
    <rect x="{RX-14}" y="{YB-YPX*5-70}" width="170" height="{YPX*5+90}" rx="10" fill="{C['hi']}" {SW}/>
    {ruler_v("lf-cm", RX, YB, YPX, 5, "cm")}
    {ruler_v("lf-m", RX, YB, MPX, 4, "m", cls=' opacity="0"')}
    {fing}
    <path id="lf-n" d="M668,{YB+10} L668,{YB-378} Q668,{YB-400} 700,{YB-400} Q732,{YB-400} 732,{YB-378} L732,{YB+10} Z" fill="{NAIL}" stroke="{K}" stroke-width="5"/>
    <path id="lf-stub" d="M668,{YB+10} L668,{YB-2} Q668,{YB-6} 700,{YB-6} Q732,{YB-6} 732,{YB-2} L732,{YB+10} Z" fill="none" stroke="none"/>
    <path id="lf-tall" d="M668,{YB+10} L668,{TOP33+22:.0f} Q668,{TOP33:.0f} 700,{TOP33:.0f} Q732,{TOP33:.0f} 732,{TOP33+22:.0f} L732,{YB+10} Z" fill="none" stroke="none"/>
    <path id="lf-ld" d="M740,{TOP33:.0f} L{RX-4},{TOP33:.0f}" stroke="{C['red']}" stroke-width="5" stroke-dasharray="12 10" fill="none" opacity="0"/>
    <path id="lf-tline" d="M150,170 L850,170" {SW} fill="none"/>
    <path d="M150,150 L150,190 M850,150 L850,190" {SW} fill="none"/>
    <text x="150" y="240" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">0</text>
    <text x="850" y="240" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">80 years</text>
    <path id="lf-tp" d="M150,140 L850,140" fill="none" stroke="none"/>
    <g id="lf-mk"><path d="M-18,-24 L18,-24 L0,8 Z" fill="{C['red']}" stroke="{K}" stroke-width="3"/></g>
  </svg>
  <div id="lf-zo">zoom out…</div>
  <div id="lf-a"><div class="big">≈ 3.3 m</div><div style="font-size:42px">per nail!</div></div>
""", J("""
tl.fromTo("#lf-mk", {x:150, y:140}, {x:150, y:140, duration:0.01}, 0);
ink("#lf-tline", 0.05, 0.4);
pop("#lf-zo", @tz, {from:{rotation:10}, to:{rotation:-6}}); tl.to("#lf-zo", {opacity:0, duration:0.2}, @tz2);
tl.to("#lf-cm", {opacity:0, duration:0.3}, @tz); tl.to("#lf-m", {opacity:1, duration:0.3}, @tz1);
morph("#lf-n", "#lf-stub", @tz, 0.5, {ease:"power3.inOut"});
along("#lf-mk", "#lf-tp", @t8, @da, {ease:"power1.inOut"});
morph("#lf-n", "#lf-tall", @t8, @da, {ease:"power1.inOut"});
tl.to("#lf-ld", {opacity:1, duration:0.2}, @t33);
pop("#lf-a", @t33, {from:{scale:1.6}, to:{}});
""", tz=tnv - 0.1, tz1=tnv + 0.1, tz2=tnv + 0.9, t8=t80 - 0.2, da=t33 - t80 + 0.2, t33=t33))

# 8 ROOM — cross-section of a room; the nail inks up from the floor and pokes through the ceiling
s = "room"; tce = aw(s, "ceiling"); tnr = aw(s, "normal room")
FL, MPXR = 900, 170; CE = FL - 2.5 * MPXR; NT = FL - 3.3 * MPXR
scenes[s] = scene_file(s, f"""
#rm-t {{ top:150px; font-size:74px; }}
#rm-svg {{ position:absolute; left:0; top:0; }}
#rm-cr {{ position:absolute; left:560px; top:{NT-40:.0f}px; {GH} font-size:62px; color:{C['red']}; opacity:0; }}
#rm-lb {{ position:absolute; left:880px; top:{CE+90:.0f}px; {GH} font-size:40px; color:{C['blue']}; line-height:1; opacity:0; }}
""", f"""
  <div id="rm-t" class="h1">Taller than the <span class="hl">ceiling</span>!</div>
  <svg id="rm-svg" width="{W}" height="1000" data-layout-ignore>
    <path class="rm-w" d="M430,{FL} L1010,{FL}" {SW} fill="none" stroke-width="7"/>
    <path class="rm-w" d="M440,{FL} L440,{CE:.0f}" {SW} fill="none"/>
    <path class="rm-w" d="M440,{CE:.0f} L1000,{CE:.0f}" {SW} fill="none" stroke-width="7"/>
    <path class="rm-w" d="M1000,{CE:.0f} L1000,{FL}" {SW} fill="none"/>
    <path class="rm-w" d="M480,{FL} L480,{FL-200} L590,{FL-200} L590,{FL}" {SW} fill="none"/>
    <g id="rm-p" opacity="0"><circle cx="700" cy="{FL-262}" r="26" fill="#fff" {SW}/>
      <path d="M700,{FL-236} L700,{FL-120} M700,{FL-120} L672,{FL} M700,{FL-120} L728,{FL} M700,{FL-200} L668,{FL-140} M700,{FL-200} L736,{FL-150}" {SW} fill="none"/></g>
    <path id="rm-no" d="M840,{FL} L840,{NT+40:.0f} Q840,{NT:.0f} 870,{NT-10:.0f}" stroke="{K}" stroke-width="40" fill="none" stroke-linecap="round"/>
    <path id="rm-ni" d="M840,{FL} L840,{NT+40:.0f} Q840,{NT:.0f} 870,{NT-10:.0f}" stroke="{NAIL}" stroke-width="30" fill="none" stroke-linecap="round"/>
    <path class="rm-c" d="M800,{CE:.0f} L780,{CE-26:.0f} L792,{CE-48:.0f}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path class="rm-c" d="M880,{CE:.0f} L902,{CE-22:.0f} L894,{CE-50:.0f}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path class="rm-c" d="M820,{CE:.0f} L810,{CE+24:.0f}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="rm-cr">CRUNCH!</div>
  <div id="rm-lb">your<br>nail</div>
""", J("""
rise("#rm-t", 0.0); ink(".rm-w", 0.0, 0.3, {stagger:0.05});
tl.fromTo("#rm-p", {opacity:0}, {opacity:1, duration:0.2}, 0.3);
ink("#rm-no, #rm-ni", @tn, @dn, {ease:"power1.in"});
ink(".rm-c", @tc, 0.15, {stagger:0.05});
pop("#rm-cr", @tc, {from:{scale:2, rotation:-20}, to:{rotation:-8}});
rise("#rm-lb", @tl);
""", tn=0.35, dn=tce + 0.1 - 0.35, tc=tce + 0.15, tl=tnr - 0.2))

# 9 TEN — ten nail bars line up, then slide into the ten floors of a tower
s = "ten"; ttf = aw(s, "ten fingers"); tad = aw(s, "add them"); t33 = aw(s, "thirty three"); tts = aw(s, "ten story")
bars = "".join(f'<rect id="tn-b{i}" class="tn-b" x="{455+i*56}" y="330" width="38" height="300" rx="14" fill="{NAIL}" stroke="{K}" stroke-width="4" opacity="0"/>' for i in range(10))
wins = "".join(f'<rect class="tn-w" x="{680+j*95}" y="{860-(i+1)*55+12}" width="46" height="28" fill="{TAPE}" stroke="{K}" stroke-width="3" opacity="0"/>' for i in range(10) for j in range(3))
scenes[s] = scene_file(s, f"""
#tn-t {{ top:150px; font-size:74px; }}
#tn-svg {{ position:absolute; left:0; top:0; }}
#tn-x {{ position:absolute; left:440px; top:680px; width:600px; text-align:center; {GH} font-size:100px; color:{C['red']}; opacity:0; }}
#tn-a {{ position:absolute; left:392px; top:360px; width:240px; text-align:center; white-space:nowrap; opacity:0; }}
#tn-a .big {{ font-size:68px; color:{C['red']}; }}
#tn-f {{ position:absolute; left:396px; top:580px; width:236px; text-align:center; white-space:nowrap; opacity:0; }}
#tn-f .pill {{ font-size:42px; padding:2px 16px; }}
""", f"""
  <div id="tn-t" class="h1"><span class="hl">10</span> fingers × 3.3 m</div>
  <svg id="tn-svg" width="{W}" height="1000" data-layout-ignore>
    {bars}{wins}
    <path id="tn-roof" d="M626,{860-10*55-8} L994,{860-10*55-8}" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="tn-gr" d="M610,862 L1010,862" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="tn-x">× 10</div>
  <div id="tn-a"><div class="big">≈ 33 m</div></div>
  <div id="tn-f"><span class="pill">10 floors!</span></div>
""", J("""
rise("#tn-t", @tt);
tl.fromTo(".tn-b", {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.25, stagger:0.06, ease:"back.out(2)"}, @tb);
pop("#tn-x", @tx);
tl.to("#tn-x", {opacity:0, duration:0.2}, @ta);
for (let i=0;i<10;i++) tl.to("#tn-b"+i, {attr:{x:640, y:860-(i+1)*55, width:340, height:52, rx:6}, duration:0.45, ease:"power3.inOut"}, @ta+i*0.09);
ink("#tn-gr", @ta, 0.3);
pop("#tn-a", @t33, {from:{scale:1.6}, to:{}});
ink("#tn-roof", @tr, 0.3);
tl.fromTo(".tn-w", {opacity:0}, {opacity:1, duration:0.1, stagger:0.02}, @tw);
pop("#tn-f", @ts, {from:{rotation:-14}, to:{rotation:-4}});
""", tt=ttf - 0.5, tb=ttf - 0.3, tx=ttf + 0.1, ta=tad - 0.1, t33=t33, tr=t33 + 0.4, tw=tts - 0.9, ts=tts))

# 10 PINKY — coloured-pencil speed bars: pinky slowest (snail), toenails about half
s = "pinky"; tnt = aw(s, "not every"); tlf = aw(s, "little finger"); tsl = aw(s, "the slowest"); tto = aw(s, "toenails"); thf = aw(s, "half as fast")
rows = [("index", 320, 520), ("middle", 420, 520), ("ring", 520, 520), ("pinky", 620, 430), ("toenail", 780, 250)]
bh = ""
for i, (lab, y, L) in enumerate(rows):
    col = C['red'] if lab == "pinky" else (C['blue'] if lab == "toenail" else K)
    bh += (f'<text x="395" y="{y+16}" text-anchor="end" font-family="Gochi Hand" font-size="50" fill="{col}">{lab}</text>'
           f'<rect id="pk-b{i}" x="420" y="{y-30}" width="{L}" height="60" rx="8" fill="url(#pk-h{1 if lab=="toenail" else 0})" stroke="{K}" stroke-width="4"/>')
snail = (f'<g id="pk-sn" opacity="0"><path d="M880,650 L990,650 Q1010,650 1004,628 L996,612" {SW} fill="#D8F0C8"/>'
         f'<circle cx="930" cy="612" r="38" fill="#F5D18A" {SW}/><path d="M930,612 m-6,0 a6,6 0 1,1 12,0 a14,14 0 1,1 -26,4 a22,22 0 1,1 40,-6" fill="none" stroke="{K}" stroke-width="4"/>'
         f'<path d="M996,612 L990,588 M1000,612 L1012,592" stroke="{K}" stroke-width="4" stroke-linecap="round"/></g>')
scenes[s] = scene_file(s, f"""
#pk-t {{ top:150px; font-size:70px; }}
#pk-svg {{ position:absolute; left:0; top:0; }}
#pk-sl {{ position:absolute; left:858px; top:664px; {GH} font-size:40px; color:{C['red']}; opacity:0; transform:rotate(-4deg); }}
#pk-hf {{ position:absolute; left:700px; top:740px; opacity:0; }}
#pk-hf .pill {{ font-size:52px; color:{C['blue']}; }}
""", f"""
  <div id="pk-t" class="h1">Not every nail keeps <span class="hl">pace</span></div>
  <svg id="pk-svg" width="{W}" height="1000" data-layout-ignore>
    <defs><pattern id="pk-h0" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><rect width="16" height="16" fill="{NAIL}"/><path d="M0,0 L0,16" stroke="#E58FA6" stroke-width="5"/></pattern>
      <pattern id="pk-h1" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><rect width="16" height="16" fill="{TAPE}"/><path d="M0,0 L0,16" stroke="{C['blue']}" stroke-width="4"/></pattern></defs>
    <path d="M90,726 L1000,726" stroke="{C['pencil']}" stroke-width="4" stroke-dasharray="14 12" fill="none"/>
    {bh}{snail}
    <rect id="pk-ring" x="408" y="578" width="{430+24}" height="84" rx="14" fill="none" stroke="{C['red']}" stroke-width="6" opacity="0"/>
  </svg>
  <div id="pk-sl">slowest!</div>
  <div id="pk-hf"><span class="pill">≈ ½ as fast</span></div>
""", J("""
rise("#pk-t", @tt);
for (let i=0;i<4;i++) tl.fromTo("#pk-b"+i, {scaleX:0, svgOrigin:"420 0"}, {scaleX:1, svgOrigin:"420 0", duration:0.7, ease:"power2.out"}, @tb+i*0.12);
tl.fromTo("#pk-ring", {opacity:0}, {opacity:1, duration:0.2}, @tl);
pop("#pk-sn", @tl, {from:{x:60}, to:{x:0}});
pop("#pk-sl", @ts, {from:{rotation:10}, to:{rotation:-4}});
tl.fromTo("#pk-b4", {scaleX:0, svgOrigin:"420 0"}, {scaleX:1, svgOrigin:"420 0", duration:0.7, ease:"power2.out"}, @tto);
pop("#pk-hf", @th, {from:{rotation:-14}, to:{rotation:-3}});
""", tt=0.0, tb=tnt + 0.2, tl=tlf - 0.1, ts=tsl, tto=tto - 0.1, th=thf - 0.2))

# 11 REAL — the long straight nail morphs into a spiral; crack lines; CRACK!
s = "real"; tcr = aw(s, "crack"); ttw = aw(s, "twist"); tcu = aw(s, "curl")
N = 60
straight = [(620, 880 - (880 - 300) * k / (N - 1)) for k in range(N)]
sp = []
for k in range(N):
    if k < 20: sp.append((620, 880 - (880 - 600) * k / 19))
    else:
        u = (k - 20) / (N - 21); a = math.pi + u * 2 * math.pi * 1.7; r = 130 - 105 * u
        sp.append((750 + r * math.cos(a), 600 + r * math.sin(a)))
def pth(pts): return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
scenes[s] = scene_file(s, f"""
#rl-t {{ top:150px; font-size:68px; line-height:1.05; }}
#rl-svg {{ position:absolute; left:0; top:0; }}
#rl-ck {{ position:absolute; left:700px; top:330px; {GH} font-size:72px; color:{C['red']}; opacity:0; }}
#rl-tw {{ position:absolute; left:860px; top:470px; {GH} font-size:54px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="rl-t" class="h1">Real nails <span class="hl">crack, twist</span><br>and curl</div>
  <svg id="rl-svg" width="{W}" height="1000" data-layout-ignore>
    <path id="rl-o" d="{pth(straight)}" stroke="{K}" stroke-width="44" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="rl-i" d="{pth(straight)}" stroke="{NAIL}" stroke-width="32" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="rl-s" d="{pth(sp)}" fill="none" stroke="none"/>
    <path d="{finger_tip(560, 680, 860, 990)}" fill="{SKIN}" {SW}/>
    <path d="M598,900 L598,880 Q620,866 642,880 L642,900" fill="{NAIL}" stroke="{K}" stroke-width="4"/>
    <path class="rl-c" d="M592,420 L612,432 L600,446 L626,458" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="rl-c" d="M648,360 L630,374 L644,386" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="rl-ck">CRACK!</div>
  <div id="rl-tw">twist…</div>
""", J("""
rise("#rl-t", 0.0);
ink("#rl-o, #rl-i", 0.15, 0.7);
ink(".rl-c", @tc, 0.2, {stagger:0.1}); pop("#rl-ck", @tc, {from:{scale:2, rotation:-20}, to:{rotation:-8}});
tl.to(".rl-c, #rl-ck", {opacity:0, duration:0.2}, @tw0);
morph("#rl-o", "#rl-s", @tw, 1.1, {ease:"power2.inOut"}); morph("#rl-i", "#rl-s", @tw, 1.1, {ease:"power2.inOut"});
pop("#rl-tw", @tw, {from:{rotation:20}, to:{rotation:6}});
tl.fromTo("#rl-o, #rl-i", {rotation:0, svgOrigin:"620 880"}, {rotation:-6, svgOrigin:"620 880", duration:0.25, yoyo:true, repeat:3, ease:"sine.inOut"}, @tu);
""", tc=tcr - 0.05, tw0=ttw - 0.25, tw=ttw - 0.1, tu=tcu))

# 12 OUTRO — callback ruler + "over 3 m per nail!", Stay curious (Max centre: keep content above ~620)
s = "outro"; tov = aw(s, "over three"); tsc = aw(s, "stay curious")
oticks = "".join(f'<path class="ou-tk" d="M{170+k*37},470 L{170+k*37},{500 if k%5 else 516}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(1, 20))
scenes[s] = scene_file(s, f"""
#ou-a {{ top:170px; font-size:84px; line-height:1.05; }}
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:200px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">over <span class="hl">3 m</span><br>per nail!</div>
  <svg id="ou-svg" width="{W}" height="620" data-layout-ignore>
    <rect id="ou-rb" x="150" y="470" width="780" height="80" rx="8" fill="{C['hi']}" {SW}/>
    {oticks}
    <rect id="ou-nl" x="150" y="400" width="800" height="50" rx="24" fill="{NAIL}" stroke="{K}" stroke-width="5"/>
  </svg>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
ink("#ou-rb", 0.05, 0.5); ink(".ou-tk", 0.4, 0.12, {stagger:0.02});
tl.fromTo("#ou-nl", {scaleX:0, svgOrigin:"150 425"}, {scaleX:1, svgOrigin:"150 425", duration:1.2, ease:"power2.out"}, @tn);
pop("#ou-a", @ta, {from:{scale:1.5}, to:{}});
tl.to("#ou-a, #ou-svg", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
pop("#ou-c", @tsc);
""", tn=0.5, ta=tov - 0.1, tx=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "what if"), SC["guess"]["start"] + 0.2)
point(g("guess", "a pencil"), 2.6)
wave(g("intro", "I'm Max"))
point(g("day", "a tenth"), 1.4)
point(g("month", "three and a"), 1.2)
point(g("year", "four centimeters"), 1.2)
wow(g("life", "three point three"), 1.4)
wow(g("room", "ceiling"), 1.2)
point(g("ten", "thirty three"), 1.2)
wow(g("ten", "ten story"), 1.2)
point(g("pinky", "little finger"), 1.4)
point(g("pinky", "half as fast"), 1.2)
think(g("real", "in real"), g("real", "crack"))
wow(g("real", "crack"), 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("click.mp3", A("hook", "never cut") + 0.1, 0.45), ("ping.mp3", A("hook", "how long"), 0.4),
        ("pop.mp3", A("guess", "a pencil") - 0.4, 0.5), ("pop.mp3", A("guess", "tall as you") - 0.4, 0.5), ("pop.mp3", A("guess", "taller than") - 0.15, 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("day", "a tenth"), 0.55), ("pop.mp3", A("day", "sheet of paper") - 0.2, 0.45),
        ("click.mp3", A("month", "three and a"), 0.45), ("riser.mp3", A("life", "eighty years") - 0.4, 0.3),
        ("impact-bass-1.mp3", A("life", "three point three"), 0.45), ("impact-bass-2.mp3", A("room", "ceiling") + 0.15, 0.45),
        ("pop.mp3", A("ten", "thirty three"), 0.5), ("ping.mp3", A("pinky", "the slowest"), 0.4),
        ("click.mp3", A("real", "crack"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
