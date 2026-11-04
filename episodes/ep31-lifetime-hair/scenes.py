# MAX WISE ep31 — How many hairs will you lose in your lifetime?
# Sources: AAD (aad.org/hair-shedding): 50-100 hairs/day is normal shedding; MedlinePlus (003246): ~100,000 scalp hairs;
# Cleveland Clinic (Hair Follicle): growth phase 2-7 years, then rest, shed, regrow.
# Maths: 75 x 365 = 27,375/yr; x 80 = 2,190,000 (50/day -> 1.46 M, 100/day -> 2.92 M); 2.19 M / 100,000 = 21.9 -> ~20 times.
# Kit: 2D only. ink (hook, intro, cycle, recycled, outro), along (cycle, life), morph (life).
# === SCENES ===
import math, random
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
HAIR = "#6B4226"; SKIN = "#F6D2B0"; BRUSH = "#8FC1E3"; TAPE = "#BFE3F7"

def wavy(x, y, a, b, n=3, rot=0.0):
    # one wavy hair as a single sub-path (quadratic + smooth t segments)
    s = f"M{x:.0f},{y:.0f} q{a:.0f},{-b:.0f} {2*a:.0f},0" + "".join(f" t{2*a:.0f},0" for _ in range(n - 1))
    return s

def hair_piece(pid, col=HAIR, w=4):
    # a short loose hair drawn around 0,0 (for falling)
    return f'<path id="{pid}" d="M-22,0 q11,-10 22,0 t22,0" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" opacity="0"/>'

def mini_head(cx, cy, r, hid=""):
    i = f' id="{hid}"' if hid else ""
    return (f'<g{i}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{SKIN}" stroke="{K}" stroke-width="3"/>'
            f'<path d="M{cx-r*1.05:.1f},{cy+r*0.1:.1f} Q{cx-r*1.1:.1f},{cy-r*1.25:.1f} {cx:.1f},{cy-r*1.2:.1f} Q{cx+r*1.1:.1f},{cy-r*1.25:.1f} {cx+r*1.05:.1f},{cy+r*0.1:.1f} Q{cx+r*0.6:.1f},{cy-r*0.55:.1f} {cx:.1f},{cy-r*0.5:.1f} Q{cx-r*0.6:.1f},{cy-r*0.55:.1f} {cx-r*1.05:.1f},{cy+r*0.1:.1f} Z" fill="{HAIR}" stroke="{K}" stroke-width="3"/>'
            f'<circle cx="{cx-r*0.35:.1f}" cy="{cy+r*0.1:.1f}" r="{max(2,r*0.09):.1f}" fill="{K}"/><circle cx="{cx+r*0.35:.1f}" cy="{cy+r*0.1:.1f}" r="{max(2,r*0.09):.1f}" fill="{K}"/>'
            f'<path d="M{cx-r*0.3:.1f},{cy+r*0.45:.1f} Q{cx:.1f},{cy+r*0.65:.1f} {cx+r*0.3:.1f},{cy+r*0.45:.1f}" fill="none" stroke="{K}" stroke-width="3" stroke-linecap="round"/></g>')

# 1 HOOK — paddle brush inks itself, tangled hairs ink on, then hairs really fall and pile on a floor line
s = "hook"; tbr = aw(s, "hairbrush"); thm = aw(s, "how many"); tlf = aw(s, "whole lifetime")
brush = ["M410,600 Q410,470 640,470 Q870,470 870,600", "M870,600 Q870,730 640,730 Q410,730 410,600",
         "M430,640 L200,800", "M200,800 Q180,830 210,845", "M210,845 L455,690"]
bh = "".join(f'<path class="hk-b" d="{d}" {WS} stroke-width="7"/>' for d in brush)
bris = "".join(f'<circle cx="{500+ (i%8)*40 + (20 if (i//8)%2 else 0)}" cy="{530+(i//8)*40}" r="6" fill="{K}"/>' for i in range(40) if 470 < 500 + (i % 8) * 40 + (20 if (i // 8) % 2 else 0) < 820)
rnd = random.Random(31); hairs = ""
for i in range(9):
    x = rnd.uniform(440, 640); y = rnd.uniform(520, 690); a = rnd.uniform(18, 30); b = rnd.uniform(10, 22)
    hairs += f'<path class="hk-h" d="{wavy(x, y, a, b, rnd.randint(3, 4))}" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>'
fall = ""; fj = ""
for i in range(22):
    fall += hair_piece(f"hk-f{i}")
    x0 = rnd.uniform(500, 820); x1 = x0 + rnd.uniform(-60, 60); y1 = rnd.uniform(872, 895); r0 = rnd.uniform(-40, 40); r1 = rnd.uniform(-25, 25)
    t0 = tlf - 1.2 + i * 0.09; d = rnd.uniform(0.55, 0.8)
    fj += f'tl.fromTo("#hk-f{i}", {{x:{x0:.0f}, y:700, rotation:{r0:.0f}, opacity:1}}, {{x:{x1:.0f}, y:{y1:.0f}, rotation:{r1:.0f}, opacity:1, duration:{d:.2f}, ease:"bounce.out", immediateRender:false}}, {t0:.3f});'
scenes[s] = scene_file(s, f"""
#hk-t {{ top:150px; font-size:72px; line-height:1.06; }}
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-bf {{ opacity:0; }}
#hk-sw {{ position:absolute; left:640px; top:420px; {GH} font-size:56px; color:{C['red']}; transform:rotate(8deg); opacity:0; }}
""", f"""
  <div id="hk-t" class="h1">How many <span class="hl">hairs</span> will you lose in your <span class="hl">lifetime</span>?</div>
  <svg id="hk-svg" width="{W}" height="960" data-layout-ignore>
    <path id="hk-bf" d="M410,600 Q410,470 640,470 Q870,470 870,600 Q870,730 640,730 Q410,730 410,600 Z" fill="{BRUSH}"/>
    <g id="hk-bri" opacity="0">{bris}</g>
    {bh}{hairs}
    <path id="hk-fl" d="M430,900 L1010,900" {WS} stroke-width="5"/>
    {fall}
  </svg>
  <div id="hk-sw">swish…</div>
""", J("""
ink(".hk-b", @tb, 0.35, {stagger:0.1});
tl.fromTo("#hk-bf", {opacity:0}, {opacity:0.9, duration:0.3}, @tb2); tl.fromTo("#hk-bri", {opacity:0}, {opacity:1, duration:0.3}, @tb2);
ink(".hk-h", @th, 0.4, {stagger:0.08});
rise("#hk-t", @tt);
ink("#hk-fl", @tf, 0.4);
""" + fj + """
pop("#hk-sw", @tsw, {from:{rotation:20}, to:{rotation:8}});
""", tb=0.05, tb2=0.5, th=tbr - 0.1, tt=thm - 0.2, tf=tlf - 1.4, tsw=tlf - 0.6))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "ten thousand"); t2 = aw(s, "two million"); t3 = aw(s, "a billion")
notes = [("a", "10,000?", -6, 95, "#FFE27A"), ("b", "2 million?", 4, 400, TAPE), ("c", "1 billion?", -3, 705, "#F7C6C6")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:285px;height:260px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:62px;line-height:260px;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.15, t2=t2 - 0.15, t3=t3 - 0.15))

# 3 INTRO — logo + underline ink + chip (keep y < 620: Max is centre stage)
s = "intro"; tmw = aw(s, "Max Wise"); tch = aw(s, "count the hairs")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ position:absolute; left:0; right:0; top:420px; text-align:center; }}
#in-sub .chip {{ font-size:56px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="in-h1" d="{wavy(140, 40, 14, 9, 4)}" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>
    <path id="in-h2" d="{wavy(830, 40, 14, 9, 4)}" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/></svg>
  <div id="in-sub"><span class="chip">Count the hairs in your brush!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
ink("#in-h1, #in-h2", @tu2, 0.4);
pop("#in-sub", @tc, {from:{rotation:-8}, to:{rotation:-2}});
""", tmw=tmw, tu=tmw + 0.3, tu2=tmw + 0.6, tc=tch - 0.2))

# 4 HEAD — 100 dots pop onto the scalp; counter to 100,000; 1 dot = 1,000 hairs
s = "head"; tsc = aw(s, "your scalp"); tht = aw(s, "hundred thousand"); ted = aw(s, "each dot")
HX, HY, HR = 640, 640, 230
pts = []
for row in range(12):
    for col in range(16):
        x = HX - 300 + col * 40 + (20 if row % 2 else 0); y = HY - 270 + row * 30
        dx, dy = (x - HX) / (HR * 1.12), (y - (HY - 10)) / (HR * 1.18)
        if dx * dx + dy * dy <= 1 and y < HY - 40 + abs(x - HX) * 0.35: pts.append((x, y))
pts.sort(key=lambda p: (p[1], p[0]))
step = len(pts) / 100.0
pts = [pts[int(i * step)] for i in range(100)]
dots = "".join(f'<circle class="hd-d" cx="{x}" cy="{y}" r="9" fill="{HAIR}" stroke="{K}" stroke-width="2" opacity="0"/>' for x, y in pts)
scenes[s] = scene_file(s, f"""
#hd-t {{ top:150px; font-size:70px; }}
#hd-svg {{ position:absolute; left:0; top:0; }}
#hd-tape {{ position:absolute; left:60px; top:420px; padding:6px 22px; background:{TAPE}; {GH} font-size:46px; transform:rotate(-6deg); opacity:0; }}
""", f"""
  <div id="hd-t" class="h1"><span id="hd-cnt" class="hl">0</span> hairs</div>
  <svg id="hd-svg" width="{W}" height="960" data-layout-ignore>
    <circle id="hd-face" cx="{HX}" cy="{HY}" r="{HR}" fill="{SKIN}" stroke="{K}" stroke-width="6" opacity="0"/>
    <g id="hd-fc" opacity="0"><circle cx="{HX-75}" cy="{HY+40}" r="14" fill="{K}"/><circle cx="{HX+75}" cy="{HY+40}" r="14" fill="{K}"/>
      <path d="M{HX-60},{HY+120} Q{HX},{HY+165} {HX+60},{HY+120}" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round"/></g>
    {dots}
  </svg>
  <div id="hd-tape">1 dot = 1,000 hairs</div>
""", J("""
rise("#hd-t", 0.0);
pop("#hd-face", @tf, {from:{scale:0.6, transformOrigin:"50% 50%"}, to:{}}); tl.fromTo("#hd-fc", {opacity:0}, {opacity:1, duration:0.3}, @tf2);
tl.fromTo(".hd-d", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, stagger:0.018, ease:"back.out(3)"}, @td);
count("#hd-cnt", 0, 100000, @td, 1.9, fmtInt);
pop("#hd-tape", @tt, {from:{rotation:-20}, to:{rotation:-6}});
""", tf=tsc - 0.2, tf2=tsc + 0.1, td=tht - 0.5, tt=ted - 0.1))

# 5 CYCLE — a cycle circle inks itself, a marker rides along it; a follicle grows a hair, drops it, grows a new one
s = "cycle"; tgr = aw(s, "grows for"); t27 = aw(s, "two to seven"); trs = aw(s, "it rests"); tfo = aw(s, "falls out"); tbn = aw(s, "brand new")
CX, CY, CR = 540, 560, 255
arcs = [f"M{CX},{CY-CR} A{CR},{CR} 0 0,1 {CX+CR},{CY}", f"M{CX+CR},{CY} A{CR},{CR} 0 0,1 {CX},{CY+CR}",
        f"M{CX},{CY+CR} A{CR},{CR} 0 0,1 {CX-CR},{CY}", f"M{CX-CR},{CY} A{CR},{CR} 0 0,1 {CX},{CY-CR}"]
ah = "".join(f'<path class="cy-a" d="{d}" {WS} stroke-width="6"/>' for d in arcs)
heads = [(CX + CR, CY, 0), (CX, CY + CR, 90), (CX - CR, CY, 180), (CX, CY - CR, 270)]
arr = "".join(f'<path class="cy-ar" d="M-14,-14 L4,0 L-14,14" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" transform="translate({x},{y}) rotate({r+90})" opacity="0"/>' for x, y, r in heads)
scenes[s] = scene_file(s, f"""
#cy-svg {{ position:absolute; left:0; top:0; }}
.cy-l {{ position:absolute; {GH} font-size:50px; line-height:1.0; opacity:0; }}
.cy-l small {{ font-size:40px; color:{C['blue']}; }}
""", f"""
  <svg id="cy-svg" width="{W}" height="960" data-layout-ignore>
    {ah}{arr}
    <path id="cy-loop" d="M{CX},{CY-CR} A{CR},{CR} 0 1,1 {CX-0.1},{CY-CR}" fill="none" stroke="none"/>
    <path id="cy-skin" d="M{CX-120},{CY+70} Q{CX},{CY+60} {CX+120},{CY+70}" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path id="cy-root" d="M{CX-18},{CY+70} Q{CX-26},{CY+120} {CX},{CY+130} Q{CX+26},{CY+120} {CX+18},{CY+70}" fill="{SKIN}" stroke="{K}" stroke-width="5"/>
    <path id="cy-hair" d="M{CX},{CY+80} Q{CX-30},{CY} {CX},{CY-60} Q{CX+30},{CY-120} {CX},{CY-170}" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>
    <path id="cy-new" d="M{CX},{CY+80} Q{CX-30},{CY} {CX},{CY-60} Q{CX+30},{CY-120} {CX},{CY-170}" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>
    <circle id="cy-m" cx="0" cy="0" r="18" fill="{C['hi']}" stroke="{K}" stroke-width="4" opacity="0"/>
  </svg>
  <div id="cy-g" class="cy-l" style="left:800px;top:300px">GROW<br><small>2–7 years</small></div>
  <div id="cy-r" class="cy-l" style="left:810px;top:790px">REST</div>
  <div id="cy-f" class="cy-l" style="left:50px;top:790px;width:240px;text-align:right">FALL<br>OUT</div>
  <div id="cy-n" class="cy-l" style="left:40px;top:300px;width:250px;text-align:right;color:{C['red']}">NEW<br>HAIR!</div>
""", J("""
ink(".cy-a", @ta, 0.35, {stagger:0.12}); tl.fromTo(".cy-ar", {opacity:0}, {opacity:1, duration:0.2, stagger:0.12}, @ta2);
ink("#cy-hair", @tg, 1.2);
tl.set("#cy-m", {opacity:1}, @tg); along("#cy-m", "#cy-loop", @tg, @dl, {ease:"none"});
pop("#cy-g", @t27); pop("#cy-r", @tr);
tl.to("#cy-hair", {x:120, y:170, rotation:70, opacity:0, transformOrigin:"50% 100%", duration:0.7, ease:"power2.in"}, @tf);
pop("#cy-f", @tf);
ink("#cy-new", @tn, 1.0); pop("#cy-n", @tn2, {from:{scale:1.6}, to:{}});
""", ta=0.0, ta2=0.6, tg=tgr - 0.1, dl=tbn + 0.4 - (tgr - 0.1), t27=t27 - 0.1, tr=trs - 0.1, tf=tfo - 0.1, tn=tbn - 0.3, tn2=tbn))

# 6 DAILY — honest band 50-100 on a hairs-per-day axis; hairs really fall into a pile
s = "daily"; tsn = aw(s, "totally normal"); t50 = aw(s, "fifty to"); tad = aw(s, "a day")
AX0, AX1, AY = 140, 960, 330
def xv(v): return AX0 + (AX1 - AX0) * v / 150
ticks = "".join(f'<path d="M{xv(v):.0f},{AY-10} L{xv(v):.0f},{AY+10}" stroke="{K}" stroke-width="4"/><text x="{xv(v):.0f}" y="{AY+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{v}</text>' for v in (0, 50, 100, 150))
rnd = random.Random(6); fall = ""; fj = ""
for i in range(30):
    fall += hair_piece(f"dl-f{i}")
    x0 = rnd.uniform(480, 960); x1 = 720 + rnd.gauss(0, 90); y1 = 835 - max(0, 60 - abs(x1 - 720) * 0.4) * rnd.uniform(0.3, 1.0)
    t0 = tsn - 0.6 + i * 0.13; d = rnd.uniform(0.7, 1.0)
    fj += f'tl.fromTo("#dl-f{i}", {{x:{x0:.0f}, y:420, rotation:{rnd.uniform(-60,60):.0f}, opacity:1}}, {{x:{x1:.0f}, y:{y1:.0f}, rotation:{rnd.uniform(-30,30):.0f}, opacity:1, duration:{d:.2f}, ease:"power1.in", immediateRender:false}}, {t0:.3f});'
scenes[s] = scene_file(s, f"""
#dl-t {{ top:150px; font-size:70px; }}
#dl-svg {{ position:absolute; left:0; top:0; }}
#dl-lab {{ position:absolute; left:0; right:0; top:420px; text-align:center; {GH} font-size:52px; opacity:0; }}
""", f"""
  <div id="dl-t" class="h1">Shedding is <span class="hl">normal</span></div>
  <svg id="dl-svg" width="{W}" height="960" data-layout-ignore>
    <rect id="dl-band" x="{xv(50):.0f}" y="{AY-34}" width="{xv(100)-xv(50):.0f}" height="68" fill="{C['hi']}" stroke="{K}" stroke-width="4" opacity="0"/>
    <path id="dl-ax" d="M{AX0-20},{AY} L{AX1+30},{AY}" {WS} stroke-width="5"/>{ticks}
    <path d="M440,840 L1010,840" {WS} stroke-width="5"/>
    {fall}
  </svg>
  <div id="dl-lab"><span class="red">50 – 100</span> hairs a day</div>
""", J("""
rise("#dl-t", 0.0); ink("#dl-ax", 0.2, 0.5);
tl.fromTo("#dl-band", {opacity:0, scaleX:0, transformOrigin:"50% 50%"}, {opacity:0.9, scaleX:1, duration:0.5, ease:"back.out(1.6)"}, @tb);
pop("#dl-lab", @tl);
""" + fj, tb=t50 - 0.1, tl=tad - 0.3))

# 7 YEAR — 365 calendar squares fill while a counter climbs to 27,000
s = "year"; t75 = aw(s, "seventy five"); toy = aw(s, "one year"); t27 = aw(s, "twenty seven thousand")
sq = ""
for i in range(365):
    r, c = divmod(i, 25)
    sq += f'<rect class="yr-s" x="{118 + c*34}" y="{370 + r*32}" width="28" height="26" rx="4" fill="{HAIR}" opacity="0"/>'
grid = "".join(f'<rect x="{118 + (i%25)*34}" y="{370 + (i//25)*32}" width="28" height="26" rx="4" fill="none" stroke="{C["muted"]}" stroke-width="2"/>' for i in range(365))
scenes[s] = scene_file(s, f"""
#yr-t {{ top:150px; font-size:64px; }}
#yr-n {{ position:absolute; left:0; right:0; top:255px; text-align:center; {GH} font-size:66px; opacity:0; }}
#yr-svg {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="yr-t" class="h1"><span class="red">75</span> a day × <span class="hl">1 year</span></div>
  <div id="yr-n">≈ <span id="yr-c" class="hl">0</span> hairs</div>
  <svg id="yr-svg" width="{W}" height="960" data-layout-ignore><g id="yr-g" opacity="0">{grid}</g>{sq}</svg>
""", J("""
rise("#yr-t", @tt);
tl.fromTo("#yr-g", {opacity:0}, {opacity:1, duration:0.3}, @tg);
rise("#yr-n", @tc);
tl.fromTo(".yr-s", {opacity:0}, {opacity:1, duration:0.05, stagger:@st}, @tc);
count("#yr-c", 0, 27000, @tc, @dc, fmtInt);
tl.fromTo("#yr-n", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1}, @tz);
""", tt=t75 - 0.3, tg=t75 + 0.2, tc=toy - 0.1, st=round((t27 + 0.3 - toy) / 365, 4), dc=t27 + 0.4 - toy, tz=t27 + 0.4))

# 8 LIFE — 0-80 ruler, bag rides along; small bag morphs into a huge bag; about 2,000,000; error bar 1.5-3 million
s = "life"; t80 = aw(s, "eighty years"); t2m = aw(s, "two million"); t15 = aw(s, "one and a half"); t3m = aw(s, "three million")
RX0, RX1, RY = 130, 950, 250
rt = "".join(f'<path d="M{RX0 + (RX1-RX0)*k/8:.0f},{RY-16 if k%4 else RY-26} L{RX0 + (RX1-RX0)*k/8:.0f},{RY+4}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for k in range(9))
def bag(cx, base, sc):
    return (f"M{cx},{base} C{cx-80*sc:.0f},{base} {cx-90*sc:.0f},{base-110*sc:.0f} {cx-40*sc:.0f},{base-160*sc:.0f} "
            f"L{cx-50*sc:.0f},{base-190*sc:.0f} L{cx+50*sc:.0f},{base-190*sc:.0f} L{cx+40*sc:.0f},{base-160*sc:.0f} "
            f"C{cx+90*sc:.0f},{base-110*sc:.0f} {cx+80*sc:.0f},{base} {cx},{base} Z")
EX0, EX1, EY = 110, 470, 640
ex2 = EX0 + (EX1 - EX0) * (2.19 - 1.5) / 1.5
scenes[s] = scene_file(s, f"""
#lf-svg {{ position:absolute; left:0; top:0; }}
#lf-n {{ position:absolute; left:0; right:0; top:330px; text-align:center; opacity:0; }}
#lf-n .big {{ font-size:110px; }}
.lf-e {{ position:absolute; top:680px; width:200px; text-align:center; {GH} font-size:40px; line-height:1; opacity:0; }}
""", f"""
  <svg id="lf-svg" width="{W}" height="960" data-layout-ignore>
    <path id="lf-ru" d="M{RX0-20},{RY} L{RX1+20},{RY}" {WS} stroke-width="5"/>{rt}
    <text x="{RX0}" y="{RY+46}" text-anchor="middle" font-family="Patrick Hand" font-size="36" fill="{K}">0</text>
    <text x="{RX1}" y="{RY+46}" text-anchor="middle" font-family="Patrick Hand" font-size="36" fill="{K}">80 years</text>
    <path id="lf-rp" d="M{RX0},{RY-40} L{RX1},{RY-40}" fill="none" stroke="none"/>
    <g id="lf-mk"><path d="M-16,-22 L16,-22 L0,8 Z" fill="{C['red']}" stroke="{K}" stroke-width="3"/></g>
    <path id="lf-bag" d="{bag(760, 880, 0.55)}" fill="{HAIR}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
    <path id="lf-big" d="{bag(760, 880, 1.75)}" fill="none" stroke="none"/>
    <g id="lf-eb" opacity="0">
      <rect x="{EX0}" y="{EY-18}" width="{EX1-EX0}" height="36" fill="{C['hi']}" opacity=".7"/>
      <path d="M{EX0},{EY} L{EX1},{EY} M{EX0},{EY-26} L{EX0},{EY+26} M{EX1},{EY-26} L{EX1},{EY+26}" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <circle cx="{ex2:.0f}" cy="{EY}" r="12" fill="{C['red']}" stroke="{K}" stroke-width="3"/></g>
  </svg>
  <div id="lf-n"><div class="big">≈ <span class="hl">2,000,000</span></div><div style="font-size:46px">hairs</div></div>
  <div id="lf-ea" class="lf-e" style="left:{EX0-100}px">1.5<br>million</div>
  <div id="lf-eb2" class="lf-e" style="left:{EX1-100}px">3<br>million</div>
""", J("""
ink("#lf-ru", 0.0, 0.5);
tl.fromTo("#lf-mk", {x:@rx0, y:@ry, opacity:1}, {x:@rx0, y:@ry, duration:0.01}, 0);
along("#lf-mk", "#lf-rp", @t8, 1.4, {ease:"power1.inOut"});
morph("#lf-bag", "#lf-big", @t8b, 1.6, {ease:"back.out(1.3)"});
pop("#lf-n", @t2, {from:{scale:1.6}, to:{}});
tl.fromTo("#lf-eb", {opacity:0, scaleX:0, transformOrigin:"0% 50%"}, {opacity:1, scaleX:1, duration:0.5}, @t15);
pop("#lf-ea", @t15); pop("#lf-eb2", @t3);
""", rx0=RX0, ry=RY - 40, t8=t80 - 0.6, t8b=t80 - 0.2, t2=t2m - 0.2, t15=t15 - 0.1, t3=t3m - 0.1))

# 9 TWIST — one big head (about 100,000 at once) shrinks into a grid; 20 heads pop; counter x 20
s = "twist"; tht = aw(s, "hundred thousand"); trp = aw(s, "replaced"); t20 = aw(s, "twenty times")
cells = [(190 + (i % 5) * 175, 400 + (i // 5) * 135) for i in range(20)]
mh = "".join(mini_head(x, y, 44, f"tw-h{i}") for i, (x, y) in enumerate(cells))
scenes[s] = scene_file(s, f"""
#tw-t {{ top:150px; font-size:62px; line-height:1.05; }}
#tw-svg {{ position:absolute; left:0; top:0; }}
#tw-x {{ position:absolute; left:560px; top:880px; {GH} font-size:0px; }}
#tw-st {{ position:absolute; left:420px; top:250px; width:620px; text-align:center; opacity:0; }}
#tw-st .big {{ font-size:72px; color:{C['red']}; }}
""", f"""
  <div id="tw-t" class="h1">Only ≈ <span class="hl">100,000</span> at once</div>
  <svg id="tw-svg" width="{W}" height="960" data-layout-ignore>
    <g id="tw-big">{mini_head(540, 600, 190)}</g>
    {mh}
  </svg>
  <div id="tw-st"><div class="big">≈ 20 times!</div></div>
""", J("""
rise("#tw-t", @tt); pop("#tw-big", @tb, {from:{scale:0.5, transformOrigin:"50% 50%"}, to:{}});
tl.to("#tw-big", {opacity:0, scale:0.25, transformOrigin:"50% 50%", duration:0.4, ease:"power2.in"}, @tr);
tl.to("#tw-t", {opacity:0, y:-20, duration:0.3}, @tr);
""" + "".join(f'tl.fromTo("#tw-h{i}", {{opacity:0, scale:0, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.25, ease:"back.out(3)"}}, @tr2+{i*0.07:.2f});' for i in range(20)) + """
pop("#tw-st", @t2, {from:{scale:2, rotation:-12}, to:{rotation:-4}});
""", tt=tht - 0.8, tb=tht - 0.4, tr=trp - 0.5, tr2=trp - 0.2, t2=t20 - 0.1))

# 10 RECYCLED — three recycling arrows ink around a head and spin; stamp; dermatologist pill
s = "recycled"; trc = aw(s, "recycled"); tlw = aw(s, "losing way"); tdm = aw(s, "see a dermatologist")
RC, RCY, RR = 640, 570, 225
rec = ""
for k in range(3):
    a0 = math.radians(-80 + k * 120); a1 = math.radians(-80 + k * 120 + 95)
    x0, y0 = RC + RR * math.cos(a0), RCY + RR * math.sin(a0); x1, y1 = RC + RR * math.cos(a1), RCY + RR * math.sin(a1)
    rec += f'<path class="rc-a" d="M{x0:.0f},{y0:.0f} A{RR},{RR} 0 0,1 {x1:.0f},{y1:.0f}" fill="none" stroke="{C["blue"]}" stroke-width="12" stroke-linecap="round"/>'
    ang = a1 + math.pi / 2
    tx, ty = math.cos(ang), math.sin(ang); nx, ny = -ty, tx
    tipx, tipy = x1 + tx * 18, y1 + ty * 18
    rec += f'<path class="rc-a" d="M{x1 - tx*12 + nx*24:.0f},{y1 - ty*12 + ny*24:.0f} L{tipx:.0f},{tipy:.0f} L{x1 - tx*12 - nx*24:.0f},{y1 - ty*12 - ny*24:.0f}" fill="none" stroke="{C["blue"]}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
scenes[s] = scene_file(s, f"""
#rc-svg {{ position:absolute; left:0; top:0; }}
#rc-st {{ position:absolute; left:420px; top:150px; width:600px; text-align:center; {GH} font-size:96px; color:{C['red']}; border:7px solid {C['red']}; {SKETCH} opacity:0; }}
#rc-p {{ position:absolute; left:420px; top:830px; width:600px; text-align:center; opacity:0; }}
#rc-p .pill {{ font-size:40px; line-height:1.1; }}
""", f"""
  <svg id="rc-svg" width="{W}" height="960" data-layout-ignore>
    <g id="rc-rot">{rec}</g>
    <g id="rc-hd">{mini_head(RC, RCY + 20, 120)}</g>
  </svg>
  <div id="rc-st">RECYCLED!</div>
  <div id="rc-p"><span class="pill">Losing way more than usual?<br><span class="red">See a dermatologist.</span></span></div>
""", J("""
pop("#rc-hd", 0.05, {from:{scale:0.6, transformOrigin:"50% 50%"}, to:{}});
ink(".rc-a", @ta, 0.35, {stagger:0.1});
tl.fromTo("#rc-rot", {rotation:0, svgOrigin:"@rc @rcy"}, {rotation:360, svgOrigin:"@rc @rcy", duration:@dr, ease:"none"}, @ta2);
pop("#rc-st", @ts, {from:{scale:2.4, rotation:-25}, to:{rotation:-6}});
rise("#rc-p", @tp);
""", ta=trc - 1.0, ta2=trc - 0.1, dr=SC[s]["slot"] - trc + 0.1, rc=RC, rcy=RCY, ts=trc - 0.05, tp=tlw - 0.1))

# 11 OUTRO — callback brush with a pile, check ink, Stay curious (Max centre: keep content above ~840)
s = "outro"; t2m = aw(s, "two million"); tnm = aw(s, "normal"); tsc = aw(s, "stay curious")
rnd = random.Random(11)
pile = "".join(f'<path class="ou-h" d="{wavy(rnd.uniform(330, 650), rnd.uniform(560, 620), rnd.uniform(14, 24), rnd.uniform(8, 16), 3)}" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round"/>' for _ in range(14))
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:68px; line-height:1.05; }}
#ou-svg {{ position:absolute; left:0; top:-70px; }}
#ou-n {{ position:absolute; left:0; right:0; top:575px; text-align:center; opacity:0; }}
#ou-c {{ position:absolute; left:0; right:0; top:300px; text-align:center; opacity:0; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">≈ <span class="hl">2 million</span> hairs in a lifetime</div>
  <svg id="ou-svg" width="{W}" height="760" data-layout-ignore>
    <g id="ou-br"><path d="M300,430 Q300,360 450,360 Q600,360 600,430 Q600,500 450,500 Q300,500 300,430 Z" fill="{BRUSH}" stroke="{K}" stroke-width="6"/>
    <path d="M600,450 L800,540 Q820,555 805,570 L590,480" fill="{BRUSH}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/></g>
    {pile}
    <path id="ou-ck" d="M860,600 L895,640 L970,560" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="ou-n"><span class="chip">totally normal!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-a", @ta); pop("#ou-br", @tb, {from:{rotation:-10}, to:{}});
ink(".ou-h", @tb2, 0.3, {stagger:0.06});
ink("#ou-ck", @tn, 0.35); pop("#ou-n", @tn2);
tl.to("#ou-a, #ou-svg, #ou-n", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
pop("#ou-c", @tsc);
""", ta=0.0, tb=t2m - 0.6, tb2=t2m - 0.2, tn=tnm - 0.3, tn2=tnm, tx=tsc - 0.3, tsc=tsc))

# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "ten thousand"), 2.2)
wave(g("intro", "I'm Max"))
point(g("head", "hundred thousand"), 1.4)
point(g("cycle", "grows for"), 1.2)
wow(g("cycle", "brand new"), 1.0)
point(g("daily", "fifty to"), 1.2)
point(g("year", "twenty seven thousand"), 1.2)
wow(g("life", "two million"), 1.4)
think(g("twist", "but you"), g("twist", "replaced"))
wow(g("twist", "twenty times"), 1.4)
point(g("recycled", "see a dermatologist"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "how many") - 0.3, 0.3), ("click-soft.mp3", A("hook", "whole lifetime"), 0.45),
        ("pop.mp3", A("guess", "ten thousand"), 0.5), ("pop.mp3", A("guess", "two million"), 0.5), ("pop.mp3", A("guess", "a billion"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("ping.mp3", A("head", "hundred thousand") + 1.4, 0.4),
        ("pop.mp3", A("cycle", "brand new"), 0.5), ("click.mp3", A("year", "twenty seven thousand"), 0.45),
        ("riser.mp3", A("life", "eighty years") - 0.5, 0.3), ("impact-bass-1.mp3", A("life", "two million"), 0.45),
        ("impact-bass-2.mp3", A("twist", "twenty times"), 0.45), ("ping.mp3", A("recycled", "recycled"), 0.4),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
