# MAX WISE ep28 — How much dead skin will you shed in your lifetime?
# Kit: ink / morph / along helpers; 2D only (no three.js). Sources: BBC Science Focus Q&A (0.03-0.09 g/h, ~35 kg/life),
# Live Science (ACS figure; 2009 dust study ~40 % of house dust from outdoors), Cleveland Clinic (new outer skin about every 30 days).
# Maths: 0.06 g/h x 24 = 1.44 g/day ~ 1.5 g; x 365 = 526 g/yr ~ half a kilo; x 80 yr = 42 kg ~ 40 kg (range 21-63 kg).
# Myth: 2,880 kg = 3 kg whole skin x 12 x 80 (wrong: only the outer layer flakes off).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#FCE3D2"; FLAKE = "#F3D3B8"; SACK = "#D9B98C"; LIVE = "#F7C6CF"; SOIL = "#B9895A"; DUST = "#C9C4BC"; BREAD = "#E9B66B"

def flake_pts(rnd, r):
    n = rnd.randint(5, 7)
    return " ".join(f"{math.cos(2*math.pi*i/n + rnd.uniform(-.3, .3)) * r * rnd.uniform(.6, 1):.1f},{math.sin(2*math.pi*i/n + rnd.uniform(-.3, .3)) * r * rnd.uniform(.4, .8):.1f}" for i in range(n))

def sack(p, cx, by, s, label="", fs=0, hidden=False):
    """burlap sack doodle, bottom centre at cx,by, height ~s. ids p-b (body), p-t (tie), p-f (tuft)"""
    f = lambda a, b: f"{cx + a*s:.1f},{by - b*s:.1f}"
    body = f"M{f(-.18,.86)} Q{f(-.52,.62)} {f(-.48,.26)} Q{f(-.44,0)} {f(0,0)} Q{f(.44,0)} {f(.48,.26)} Q{f(.52,.62)} {f(.18,.86)} Z"
    tie = f"M{f(-.21,.85)} Q{f(0,.78)} {f(.21,.85)}"
    tuft = f"M{f(-.16,.87)} L{f(-.27,1.02)} L{f(-.08,.96)} L{f(0,1.07)} L{f(.08,.96)} L{f(.27,1.02)} L{f(.16,.87)} Z"
    op = ' opacity="0"' if hidden else ""
    sw = max(3, s / 40)
    out = (f'<path id="{p}-f" d="{tuft}" fill="{SACK}" stroke="{K}" stroke-width="{sw:.1f}" stroke-linejoin="round"{op}/>'
           f'<path id="{p}-b" d="{body}" fill="{SACK}" stroke="{K}" stroke-width="{sw:.1f}" stroke-linejoin="round"{op}/>'
           f'<path id="{p}-t" d="{tie}" fill="none" stroke="{C["red"]}" stroke-width="{sw*1.4:.1f}" stroke-linecap="round"{op}/>')
    if not hidden:
        out += "".join(f'<path d="M{f(a,b)} l{s*.05:.1f},{s*.03:.1f}" stroke="{K}" stroke-width="{max(2, s/80):.1f}" stroke-linecap="round" opacity=".5"/>' for a, b in ((-.25,.35), (.2,.5), (.05,.18), (-.1,.62)))
    if label:
        out += f'<text id="{p}-l" x="{cx}" y="{by - .3*s:.0f}" text-anchor="middle" style="{GH}font-size:{fs}px" fill="{K}">{label}</text>'
    return out

# 1 HOOK — a forearm inks itself; seeded flakes really fall, sway and pile on the floor
s = "hook"; tq = aw(s, "how much"); tfl = aw(s, "tiny flakes"); tds = aw(s, "dead skin"); twl = aw(s, "whole life")
rnd = random.Random(28); fl = ""; fj = ""
for i in range(34):
    x0 = rnd.uniform(200, 760); x1 = x0 + rnd.uniform(-60, 90); y1 = rnd.uniform(505, 528)
    t0 = tfl + i * 0.085; d = rnd.uniform(1.3, 1.9); rot = rnd.uniform(-200, 200)
    fl += f'<polygon class="hk-f" id="hk-f{i}" points="{flake_pts(rnd, rnd.uniform(9, 15))}" fill="{FLAKE}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round" opacity="0"/>'
    fj += (f'tl.fromTo("#hk-f{i}", {{y:{rnd.uniform(215, 235):.0f}, rotation:0, opacity:0, transformOrigin:"50% 50%"}}, {{y:{y1:.0f}, rotation:{rot:.0f}, opacity:1, transformOrigin:"50% 50%", duration:{d:.2f}, ease:"power1.in"}}, {t0:.3f});'
           f'tl.fromTo("#hk-f{i}", {{x:{x0:.0f}}}, {{x:{x1:.0f}, duration:{d:.2f}, ease:"sine.inOut"}}, {t0:.3f});')
scenes[s] = scene_file(s, f"""
#hk-t {{ top:160px; font-size:84px; line-height:1.05; opacity:0; }}
#hk-svg {{ position:absolute; left:0; top:300px; }}
#hk-o {{ position:absolute; left:640px; top:745px; opacity:0; {GH} font-size:60px; color:{C['blue']}; transform:rotate(-6deg); }}
""", f"""
  <div id="hk-t" class="h1">How much <span class="hl">dead skin</span> will you shed?</div>
  <svg id="hk-svg" width="{W}" height="580" viewBox="0 0 {W} 580" data-layout-ignore>
    <path id="hk-fill" d="M110,112 Q420,82 760,102 Q900,72 950,140 Q960,200 860,230 L760,222 Q420,252 110,240 Z" fill="{SKIN}" opacity="0"/>
    <path class="hk-a" d="M110,112 Q420,82 760,102" {WS} stroke-width="8"/>
    <path class="hk-a" d="M110,240 Q420,252 760,222" {WS} stroke-width="8"/>
    <path class="hk-a" d="M760,102 Q900,72 950,140 Q960,200 860,230 L760,222" {WS} stroke-width="8"/>
    <path class="hk-a" d="M845,128 Q880,150 900,140" {WS} stroke-width="5"/>
    <path id="hk-floor" d="M130,535 Q540,525 950,538" {WS} stroke-width="7"/>
    {fl}
  </svg>
  <div id="hk-o">flake... flake...</div>
""", J("""
ink(".hk-a", 0.05, 0.7, {stagger:0.12});
tl.fromTo("#hk-fill", {opacity:0}, {opacity:1, duration:0.4}, 0.6);
ink("#hk-floor", @tf0, 0.5);
""" + fj + """
tl.set("#hk-o", {opacity:1}, @tfo); pop("#hk-o", @tfo, {from:{rotation:-16}, to:{rotation:-6}});
tl.set("#hk-t", {opacity:1}, @tq); pop("#hk-t", @tq, {from:{scale:1.3}, to:{}});
pop("#hk-t .hl", @td, {from:{scale:1.5}, to:{}});
""", tf0=tfl - 0.4, tfo=tfl + 1.4, tq=tq - 0.15, td=tds - 0.1))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "one kilo"); t2 = aw(s, "forty kilos"); t3 = aw(s, "three thousand")
notes = [("a", "1 kilo?", -6, 110, FLAKE), ("b", "40 kilos?", 4, 405, C['hi']), ("c", "3,000 kilos?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:62px;line-height:1.05;padding:95px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3 - 0.2))

# 3 INTRO — logo + a balance scale inks itself (keep y < 620: Max is centre stage)
s = "intro"; tmw = aw(s, "Max Wise"); twe = aw(s, "weigh every")
bal = [f"M540,18 L540,112", "M488,114 L592,114", "M392,30 L688,30", "M392,30 L362,82", "M392,30 L422,82", "M688,30 L658,82", "M688,30 L718,82",
       "M350,84 Q392,116 434,84", "M646,84 Q688,116 730,84"]
bh = "".join(f'<path class="in-j" d="{d}" {WS} stroke-width="7"/>' for d in bal)
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:395px; font-size:62px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Weigh every flake!</span></div>
  <svg class="abs" style="left:0;top:490px" width="{W}" height="130" data-layout-ignore>{bh}
    <polygon id="in-fk" points="380,70 398,64 410,74 392,80" fill="{FLAKE}" stroke="{K}" stroke-width="3" opacity="0"/></svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tw); ink(".in-j", @tw, 0.3, {stagger:0.06});
tl.fromTo("#in-fk", {opacity:0, y:-60}, {opacity:1, y:0, duration:0.4, ease:"bounce.out"}, @tw2);
""", tmw=tmw, tu=tmw + 0.3, tw=twe - 0.4, tw2=twe + 0.3))

# 4 LAYERS — skin block cutaway: flat dead bricks on top, round live cells below; a new cell rides up, old flakes peel off
s = "layers"; two = aw(s, "outer skin"); tfd = aw(s, "flat, dead"); tpu = aw(s, "push up"); tfa = aw(s, "flake away"); tem = aw(s, "every month")
bricks = ""
for r in range(3):
    for c in range(9):
        x = 150 + c * 94 + (47 if r % 2 else 0)
        if x + 86 > 945: continue
        bricks += f'<rect class="ly-br" x="{x}" y="{208 + r*30}" width="86" height="24" rx="6" fill="{FLAKE}" stroke="{K}" stroke-width="3.5"/>'
cells = "".join(f'<circle class="ly-c" cx="{185 + c*80 + (40 if r % 2 else 0)}" cy="{335 + r*64}" r="27" fill="{LIVE}" stroke="{K}" stroke-width="4"/>'
                for r in range(4) for c in range(10) if 185 + c*80 + (40 if r % 2 else 0) < 925)
routes = ["M330,210 Q360,120 470,90", "M520,210 Q580,110 700,70", "M760,210 Q840,130 960,110"]
peel = "".join(f'<path id="ly-r{i}" d="{d}" fill="none" stroke="none"/><g id="ly-p{i}" opacity="0"><rect x="-43" y="-12" width="86" height="24" rx="6" fill="{FLAKE}" stroke="{K}" stroke-width="3.5"/></g>' for i, d in enumerate(routes))
scenes[s] = scene_file(s, f"""
#ly-svg {{ position:absolute; left:0; top:200px; }}
#ly-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#ly-m {{ position:absolute; left:0; right:0; top:910px; text-align:center; opacity:0; padding-left:300px; }}
.ly-tape {{ position:absolute; opacity:0; padding:4px 18px; background:rgba(255,226,122,.85); border:3px solid {K}; {GH} font-size:42px; }}
""", f"""
  <div id="ly-c"><span class="chip" style="background:#FFFFFF">your outer skin, sliced open</span></div>
  <svg id="ly-svg" width="{W}" height="660" viewBox="0 0 {W} 660" data-layout-ignore>
    <path id="ly-cut" d="M130,195 L950,195 L950,600 L130,600 Z" fill="#FFF6EE" stroke="{K}" stroke-width="5" stroke-dasharray="16 10"/>
    {cells}{bricks}
    <path id="ly-up" d="M600,590 L600,240" fill="none" stroke="none"/>
    <path id="ly-arr" d="M600,580 L600,300 M576,328 L600,300 L624,328" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0"/>
    <g id="ly-new" opacity="0"><circle r="27" fill="#FFFFFF" stroke="{C['blue']}" stroke-width="6"/></g>
    {peel}
    <path id="ly-ld1" d="M880,150 Q900,180 870,215" {WS} stroke-width="4"/>
    <path id="ly-ld2" d="M880,640 Q900,600 860,560" {WS} stroke-width="4"/>
  </svg>
  <div id="ly-t1" class="ly-tape" style="left:600px;top:290px;transform:rotate(-2deg)">dead, flat cells</div>
  <div id="ly-t2" class="ly-tape" style="left:660px;top:815px;transform:rotate(2deg);background:rgba(247,198,207,.9)">new living cells</div>
  <div id="ly-m"><span class="chip" style="background:{C['hi']};font-size:54px">fresh layer about every month</span></div>
""", J("""
ink("#ly-cut", 0.05, 0.8);
tl.set("#ly-c", {opacity:1}, @tw); pop("#ly-c .chip", @tw, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo(".ly-c", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.25, stagger:0.012, ease:"back.out(2)"}, 0.3);
tl.fromTo(".ly-br", {opacity:0, y:-30}, {opacity:1, y:0, duration:0.25, stagger:0.03, ease:"back.out(2)"}, @tf);
tl.set("#ly-t1", {opacity:1}, @tf2); pop("#ly-t1", @tf2, {from:{rotation:-10}, to:{rotation:-2}}); ink("#ly-ld1", @tf2, 0.3);
tl.fromTo("#ly-arr", {opacity:0}, {opacity:1, duration:0.2}, @tp); ink("#ly-arr", @tp, 0.5);
tl.fromTo("#ly-new", {opacity:0}, {opacity:1, duration:0.15}, @tp);
along("#ly-new", "#ly-up", @tp, 1.2, {ease:"power2.out"});
tl.to("#ly-new circle", {attr:{r:24}, scaleY:0.5, transformOrigin:"50% 50%", duration:0.4}, @tp3);
tl.set("#ly-t2", {opacity:1}, @tp); pop("#ly-t2", @tp, {from:{rotation:10}, to:{rotation:2}}); ink("#ly-ld2", @tp, 0.3);
""" + "".join(f'tl.fromTo("#ly-p{i}", {{opacity:0}}, {{opacity:1, duration:0.1}}, @ta+{i*0.18:.2f}); along("#ly-p{i}", "#ly-r{i}", @ta+{i*0.18:.2f}, 1.1, {{ease:"power1.out", rotate:true}}); tl.to("#ly-p{i}", {{opacity:0, duration:0.4}}, @ta+{1.3 + i*0.18:.2f});' for i in range(3)) + """
tl.set("#ly-m", {opacity:1}, @tm); pop("#ly-m .chip", @tm, {from:{rotation:8}, to:{rotation:2}});
""", tw=two - 0.2, tf=tfd - 0.3, tf2=tfd + 0.2, tp=tpu - 0.4, tp3=tpu + 0.7, ta=tfa - 0.4, tm=tem - 0.5))

# 5 HOUR — honest range band on a gram axis; marker drops on 0.06 g; a one-hour clock ticks
s = "hour"; teh = aw(s, "each hour"); tth = aw(s, "between three"); tni = aw(s, "nine hundredths"); tsi = aw(s, "six hundredths")
X = lambda g: 140 + g * 8000
hatch = "".join(f'<path d="M{x},400 L{x + 40},470" stroke="{C["blue"]}" stroke-width="4" opacity=".5"/>' for x in range(380, 860, 22))
tk = "".join(f'<path d="M{X(v):.0f},490 L{X(v):.0f},515" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for v in (0, .03, .06, .09))
scenes[s] = scene_file(s, f"""
#hr-svg {{ position:absolute; left:0; top:200px; }}
#hr-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#hr-a {{ position:absolute; left:0; right:0; top:830px; text-align:center; opacity:0; padding-left:300px; }}
#hr-band {{ opacity:0; }}
""", f"""
  <div id="hr-c"><span class="chip" style="background:#FFFFFF">skin lost per hour</span></div>
  <svg id="hr-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <circle id="hr-clk" cx="540" cy="190" r="95" fill="#FFFFFF" stroke="{K}" stroke-width="7"/>
    <path id="hr-mh" d="M540,190 L540,112" stroke="{C['red']}" stroke-width="8" stroke-linecap="round"/>
    <path d="M540,190 L585,190" stroke="{K}" stroke-width="9" stroke-linecap="round"/>
    <circle cx="540" cy="190" r="9" fill="{K}"/>
    <defs><clipPath id="hr-bc"><rect x="380" y="400" width="480" height="70"/></clipPath></defs>
    <g id="hr-band"><rect x="380" y="400" width="480" height="70" rx="10" fill="{FLAKE}" stroke="{K}" stroke-width="5"/><g clip-path="url(#hr-bc)">{hatch}</g></g>
    <path id="hr-ax" d="M120,490 L960,490" stroke="{K}" stroke-width="7" stroke-linecap="round"/>
    {tk}
    <text id="hr-l3" x="{X(.03):.0f}" y="575" text-anchor="middle" style="{GH}font-size:48px" fill="{K}" opacity="0">0.03 g</text>
    <text id="hr-l9" x="{X(.09):.0f}" y="575" text-anchor="middle" style="{GH}font-size:48px" fill="{K}" opacity="0">0.09 g</text>
    <g id="hr-mk" opacity="0"><path d="M{X(.06):.0f},390 L{X(.06)-25:.0f},340 L{X(.06)+25:.0f},340 Z" fill="{C['red']}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/></g>
  </svg>
  <div id="hr-a"><span class="chip" style="background:{C['hi']};font-size:58px">about 0.06 g an hour</span></div>
""", J("""
ink("#hr-clk", 0.05, 0.6); ink("#hr-ax", 0.2, 0.5);
tl.fromTo("#hr-mh", {rotation:0, svgOrigin:"540 190"}, {rotation:360, svgOrigin:"540 190", duration:@dur, ease:"none"}, 0.3);
tl.set("#hr-c", {opacity:1}, @te); pop("#hr-c .chip", @te, {from:{rotation:-10}, to:{rotation:-3}});
tl.set("#hr-band", {opacity:1}, @t3);
tl.fromTo("#hr-band", {scaleX:0.03, svgOrigin:"380 435"}, {scaleX:0.15, svgOrigin:"380 435", duration:0.3, ease:"back.out(1.6)"}, @t3);
tl.fromTo("#hr-l3", {opacity:0}, {opacity:1, duration:0.2}, @t3);
tl.to("#hr-band", {scaleX:1, svgOrigin:"380 435", duration:0.6, ease:"back.out(1.4)"}, @t9);
tl.fromTo("#hr-l9", {opacity:0}, {opacity:1, duration:0.2}, @t9b);
tl.fromTo("#hr-mk", {opacity:0, y:-140}, {opacity:1, y:0, duration:0.5, ease:"bounce.out"}, @t6);
tl.set("#hr-a", {opacity:1}, @t6b); pop("#hr-a .chip", @t6b, {from:{rotation:8}, to:{rotation:2}});
""", dur=SC[s]["slot"] - 0.6, te=teh - 0.2, t3=tth + 0.2, t9=tni - 0.2, t9b=tni + 0.2, t6=tsi - 0.5, t6b=tsi - 0.45))

# 6 DAY — a clock hand sweeps twenty four hours, dropping one flake pile per hour; counter reaches 1.5 g
s = "day"; t24 = aw(s, "twenty four"); t15 = aw(s, "one and a half"); tpi = aw(s, "barely a pinch")
CX, CY, R = 580, 430, 235
piles = ""
for i in range(24):
    a = 2 * math.pi * i / 24; px = CX + 190 * math.sin(a); py = CY - 190 * math.cos(a)
    piles += f'<path class="dy-p" d="M{px-15:.0f},{py+8:.0f} Q{px:.0f},{py-16:.0f} {px+15:.0f},{py+8:.0f} Z" fill="{FLAKE}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
sw_d = max(1.0, t15 - t24 + 0.1)
scenes[s] = scene_file(s, f"""
#dy-svg {{ position:absolute; left:0; top:180px; }}
#dy-c {{ position:absolute; left:0; right:0; top:155px; text-align:center; opacity:0; }}
#dy-a {{ position:absolute; left:0; right:0; top:880px; text-align:center; opacity:0; padding-left:300px; }}
""", f"""
  <div id="dy-c"><span class="chip" style="background:#FFFFFF">24 hours = 24 little piles</span></div>
  <svg id="dy-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <circle id="dy-face" cx="{CX}" cy="{CY}" r="{R}" fill="#FFFFFF" stroke="{K}" stroke-width="8"/>
    {piles}
    <path id="dy-hand" d="M{CX},{CY} L{CX},{CY - 150}" stroke="{C['red']}" stroke-width="9" stroke-linecap="round"/>
    <circle cx="{CX}" cy="{CY}" r="10" fill="{K}"/>
    <rect x="{CX-120}" y="{CY+40}" width="240" height="90" rx="14" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>
    <text id="dy-v" x="{CX}" y="{CY+105}" text-anchor="middle" style="{GH}font-size:70px" fill="{K}">0.0 g</text>
  </svg>
  <div id="dy-a"><span class="chip" style="background:{FLAKE};font-size:54px">about 1.5 g: barely a pinch</span></div>
""", J("""
ink("#dy-face", 0.05, 0.6);
tl.set("#dy-c", {opacity:1}, @t24); pop("#dy-c .chip", @t24, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo("#dy-hand", {rotation:0, svgOrigin:"@cx @cy"}, {rotation:360, svgOrigin:"@cx @cy", duration:@sw, ease:"none"}, @t24);
tl.fromTo(".dy-p", {opacity:0, scale:0.2, transformOrigin:"50% 100%"}, {opacity:1, scale:1, duration:0.15, stagger:@st, ease:"back.out(2)"}, @t24);
count("#dy-v", 0, 1.5, @t24, @sw, v => v.toFixed(1) + " g");
tl.set("#dy-a", {opacity:1}, @tp); pop("#dy-a .chip", @tp, {from:{rotation:8}, to:{rotation:2}});
""", cx=CX, cy=CY, t24=t24 - 0.1, sw=sw_d, st=sw_d / 24, tp=t15 - 0.1))

# 7 YEAR — the hero sack: a tiny sack morphs into a fat one (about half a kilo); a loaf of bread inks beside it
s = "year"; toy = aw(s, "one year"); tpu = aw(s, "piles up"); thk = aw(s, "half a kilo"); tlb = aw(s, "loaf of")
scenes[s] = scene_file(s, f"""
#yr-svg {{ position:absolute; left:0; top:200px; }}
#yr-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#yr-l {{ opacity:0; }}
""", f"""
  <div id="yr-c"><span class="chip" style="background:#FFFFFF">1 year of flakes</span></div>
  <svg id="yr-svg" width="{W}" height="660" viewBox="0 0 {W} 660" data-layout-ignore>
    <g id="yr-g">{sack("yr", 430, 620, 150)}</g>
    {sack("yrB", 430, 620, 430, hidden=True)}
    <text id="yr-l" x="430" y="500" text-anchor="middle" style="{GH}font-size:62px" fill="{K}">about ½ kg</text>
    <text id="yr-eq" x="725" y="560" text-anchor="middle" style="{GH}font-size:90px" fill="{C['blue']}" opacity="0">≈</text>
    <path class="yr-br" d="M790,610 L790,520 Q780,470 830,465 Q880,440 930,465 Q985,470 975,520 L975,610 Z" fill="{BREAD}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    <path class="yr-br" d="M830,500 L860,540" {WS}/><path class="yr-br" d="M875,495 L905,535" {WS}/><path class="yr-br" d="M920,500 L950,540" {WS}/>
    <text id="yr-bt" x="882" y="655" text-anchor="middle" style="{GH}font-size:40px" fill="{C['muted']}" opacity="0">a loaf</text>
  </svg>
""", J("""
tl.set("#yr-c", {opacity:1}, @ty); pop("#yr-c .chip", @ty, {from:{rotation:-10}, to:{rotation:-3}});
pop("#yr-g", 0.1, {from:{scale:0.3, svgOrigin:"430 620"}, to:{svgOrigin:"430 620"}});
morph("#yr-b", "#yrB-b", @tp, 1.2, {ease:"back.out(1.3)"}); morph("#yr-t", "#yrB-t", @tp, 1.2, {ease:"back.out(1.3)"}); morph("#yr-f", "#yrB-f", @tp, 1.2, {ease:"back.out(1.3)"});
tl.to("#yr-g path[opacity]", {opacity:0, duration:0.2}, @tp);
tl.fromTo("#yr-l", {opacity:0, scale:0.5, svgOrigin:"430 480"}, {opacity:1, scale:1, svgOrigin:"430 480", duration:0.35, ease:"back.out(2)"}, @th);
tl.fromTo("#yr-eq", {opacity:0}, {opacity:1, duration:0.2}, @tl);
ink(".yr-br", @tl, 0.4, {stagger:0.1}); tl.fromTo("#yr-bt", {opacity:0}, {opacity:1, duration:0.3}, @tl2);
""", ty=toy - 0.2, tp=tpu - 0.3, th=thk - 0.1, tl=tlb - 0.6, tl2=tlb))

# 8 LIFE — sack on a platform scale; a marker rides the year ruler 0..80 while the sack label counts and the needle swings to 40
s = "life"; tst = aw(s, "stretch that"); tey = aw(s, "eighty years"); tsc = aw(s, "the scale"); t40 = aw(s, "forty kilos")
RX = lambda y: 140 + y * 10
rt = "".join(f'<path d="M{RX(y)},40 L{RX(y)},{80 if y % 40 == 0 else 66}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for y in range(0, 81, 10))
DCX, DCY, DR = 540, 560, 130
dt = "".join(f'<path d="M{DCX + (DR-12)*math.sin(math.radians(-120 + k*30)):.1f},{DCY - (DR-12)*math.cos(math.radians(-120 + k*30)):.1f} L{DCX + (DR-(34 if k == 4 else 26))*math.sin(math.radians(-120 + k*30)):.1f},{DCY - (DR-(34 if k == 4 else 26))*math.cos(math.radians(-120 + k*30)):.1f}" stroke="{C["red"] if k == 4 else K}" stroke-width="{7 if k == 4 else 5}" stroke-linecap="round"/>' for k in range(9))
scenes[s] = scene_file(s, f"""
#lf-svg {{ position:absolute; left:0; top:140px; }}
#lf-a {{ position:absolute; left:0; right:0; top:870px; text-align:center; opacity:0; padding-left:300px; }}
#lf-bo {{ position:absolute; left:790px; top:380px; opacity:0; {GH} font-size:72px; color:{C['red']}; }}
""", f"""
  <svg id="lf-svg" width="{W}" height="740" viewBox="0 0 {W} 740" data-layout-ignore>
    <rect id="lf-rul" x="120" y="20" width="840" height="40" rx="6" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>
    {rt}
    <text x="140" y="125" text-anchor="middle" style="{GH}font-size:44px" fill="{K}">0</text>
    <text x="940" y="125" text-anchor="end" style="{GH}font-size:44px" fill="{K}">80 years</text>
    <path id="lf-route" d="M140,10 L940,10" fill="none" stroke="none"/>
    <g id="lf-mk" opacity="0"><path d="M0,14 L-18,-18 L18,-18 Z" fill="{C['red']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></g>
    <g id="lf-sk">{sack("lf", 540, 372, 200, label="0 kg", fs=50)}</g>
    <path d="M300,380 L780,380" stroke="{K}" stroke-width="12" stroke-linecap="round"/>
    <path d="M540,380 L540,400" stroke="{K}" stroke-width="10"/>
    <rect id="lf-box" x="290" y="400" width="500" height="320" rx="24" fill="#FFFFFF" stroke="{K}" stroke-width="7"/>
    <circle cx="{DCX}" cy="{DCY}" r="{DR}" fill="#FFF6EE" stroke="{K}" stroke-width="6"/>
    {dt}
    <text x="{DCX}" y="{DCY + 80}" text-anchor="middle" style="{GH}font-size:40px" fill="{C['muted']}">kg</text>
    <path id="lf-nd" d="M{DCX},{DCY} L{DCX},{DCY - DR + 30}" stroke="{C['red']}" stroke-width="8" stroke-linecap="round"/>
    <circle cx="{DCX}" cy="{DCY}" r="11" fill="{K}"/>
  </svg>
  <div id="lf-bo">BOING!</div>
  <div id="lf-a"><span class="chip" style="background:{C['hi']};font-size:62px">about 40 kg!</span></div>
""", J("""
pop("#lf-sk", 0.05, {from:{scale:0.4, svgOrigin:"540 372"}, to:{svgOrigin:"540 372"}});
tl.fromTo("#lf-mk", {opacity:0}, {opacity:1, duration:0.15}, @te);
along("#lf-mk", "#lf-route", @te, @dd, {ease:"power1.inOut"});
count("#lf-l", 0, 40, @te, @dd, v => Math.round(v) + " kg");
tl.fromTo("#lf-nd", {rotation:-120, svgOrigin:"@dx @dy"}, {rotation:-8, svgOrigin:"@dx @dy", duration:@dd, ease:"power1.inOut"}, @te);
tl.to("#lf-nd", {rotation:0, svgOrigin:"@dx @dy", duration:0.6, ease:"elastic.out(1.2, 0.35)"}, @t4);
tl.to("#lf-sk", {scaleY:0.92, svgOrigin:"540 372", duration:0.12, yoyo:true, repeat:1}, @t4);
tl.set("#lf-bo", {opacity:1}, @t4); pop("#lf-bo", @t4, {from:{rotation:-20, scale:1.6}, to:{rotation:-8}});
tl.set("#lf-a", {opacity:1}, @t4b); pop("#lf-a .chip", @t4b, {from:{rotation:8, scale:1.4}, to:{rotation:2}});
""", dx=DCX, dy=DCY, te=tst - 0.1, dd=t40 - 0.1 - (tst - 0.1), t4=t40 - 0.1, t4b=t40 + 0.2))

# 9 COMPARE — an adult outline fills with coloured-pencil hatching up to the halfway line; the sack stands beside it
s = "compare"; tha = aw(s, "about half"); tad = aw(s, "grown adult")
body = ("M680,192 L680,222 Q600,226 590,262 L566,470 Q578,486 594,470 L620,300 L626,460 L640,700 L692,700 L700,480 L708,700 "
        "L760,700 L774,460 L780,300 L806,470 Q822,486 834,470 L810,262 Q800,226 720,222 L720,192 Z")
ph = "".join(f'<path d="M{x},700 L{x + 90},380" stroke="#D98E6A" stroke-width="7" stroke-linecap="round"/>' for x in range(470, 900, 18))
scenes[s] = scene_file(s, f"""
#cp-svg {{ position:absolute; left:0; top:150px; }}
#cp-c {{ position:absolute; left:70px; top:170px; opacity:0; }}
#cp-h {{ position:absolute; left:860px; top:500px; opacity:0; padding:4px 18px; background:rgba(255,226,122,.9); border:3px solid {K}; {GH} font-size:64px; transform:rotate(4deg); }}
""", f"""
  <div id="cp-c"><span class="chip" style="font-size:48px;background:#FFFFFF">half a grown adult</span></div>
  <svg id="cp-svg" width="{W}" height="720" viewBox="0 0 {W} 720" data-layout-ignore>
    <defs><clipPath id="cp-cl"><path d="{body}"/><circle cx="700" cy="130" r="62"/></clipPath></defs>
    <g clip-path="url(#cp-cl)"><g id="cp-fill">{ph}</g></g>
    <path id="cp-bd" d="{body}" fill="none" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <circle id="cp-hd" cx="700" cy="130" r="62" fill="none" stroke="{K}" stroke-width="7"/>
    <path id="cp-half" d="M540,380 L860,380" stroke="{C['red']}" stroke-width="6" stroke-dasharray="16 10" stroke-linecap="round"/>
    <g id="cp-sk">{sack("cp", 300, 690, 220, label="40 kg", fs=50)}</g>
  </svg>
  <div id="cp-h">½</div>
""", J("""
ink("#cp-bd", 0.05, 0.8); ink("#cp-hd", 0.1, 0.5);
pop("#cp-sk", 0.2, {from:{scale:0.4, svgOrigin:"300 690"}, to:{svgOrigin:"300 690"}});
tl.fromTo("#cp-fill", {y:330}, {y:0, duration:0.9, ease:"power2.out"}, @th);
ink("#cp-half", @th2, 0.4);
tl.set("#cp-h", {opacity:1}, @th2); pop("#cp-h", @th2, {from:{rotation:20}, to:{rotation:4}});
tl.set("#cp-c", {opacity:1}, @ta); pop("#cp-c .chip", @ta, {from:{rotation:-10}, to:{rotation:-3}});
""", th=tha - 0.2, th2=tha + 0.6, ta=tad - 0.4))

# 10 MYTH — pencil "almost 3,000 kg?" struck out; whole-skin slab crossed vs the thin outer layer peeling
s = "myth"; tsw = aw(s, "some websites"); tth = aw(s, "three thousand"); tas = aw(s, "that assumes"); tws = aw(s, "whole skin"); tem = aw(s, "every month"); tot = aw(s, "thin outer")
scenes[s] = scene_file(s, f"""
#my-p {{ position:absolute; left:0; right:0; top:165px; text-align:center; {GH} font-size:88px; color:{C['pencil']}; opacity:0; }}
#my-svg {{ position:absolute; left:0; top:150px; }}
#my-l1 {{ position:absolute; left:60px; top:745px; width:460px; white-space:nowrap; text-align:center; opacity:0; }}
#my-l2 {{ position:absolute; left:550px; top:745px; width:470px; white-space:nowrap; text-align:center; opacity:0; }}
""", f"""
  <div id="my-p">almost 3,000 kg?</div>
  <svg id="my-svg" width="{W}" height="580" viewBox="0 0 {W} 580" data-layout-ignore>
    <path id="my-st" d="M210,80 L870,55" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <g id="my-slab" opacity="0">
      <rect x="100" y="300" width="380" height="40" fill="{FLAKE}" stroke="{K}" stroke-width="5"/>
      <rect x="100" y="340" width="380" height="110" fill="{LIVE}" stroke="{K}" stroke-width="5"/>
      <rect x="100" y="450" width="380" height="110" fill="#F9E6C8" stroke="{K}" stroke-width="5"/>
    </g>
    <path class="my-x" d="M120,310 L460,550" stroke="{C['red']}" stroke-width="12" stroke-linecap="round"/>
    <path class="my-x" d="M460,310 L120,550" stroke="{C['red']}" stroke-width="12" stroke-linecap="round"/>
    <g id="my-blk" opacity="0">
      <rect x="600" y="340" width="380" height="110" fill="{LIVE}" stroke="{K}" stroke-width="5"/>
      <rect x="600" y="450" width="380" height="110" fill="#F9E6C8" stroke="{K}" stroke-width="5"/>
    </g>
    <g id="my-thin" opacity="0"><rect x="600" y="300" width="380" height="40" fill="{C['hi']}" stroke="{K}" stroke-width="5"/></g>
  </svg>
  <div id="my-l1"><span class="chip" style="background:#FFFFFF;font-size:38px">whole skin, every month?</span></div>
  <div id="my-l2"><span class="chip" style="background:{C['hi']};font-size:38px">only the thin outer layer</span></div>
""", J("""
tl.set("#my-p", {opacity:1}, @ts); pop("#my-p", @ts, {from:{rotation:-6}, to:{}});
ink("#my-st", @ta, 0.4);
tl.fromTo("#my-slab", {opacity:0, y:40}, {opacity:1, y:0, duration:0.4, ease:"back.out(2)"}, @tw);
tl.set("#my-l1", {opacity:1}, @tw); pop("#my-l1 .chip", @tw, {from:{rotation:-8}, to:{rotation:-2}});
ink(".my-x", @tm, 0.3, {stagger:0.15});
tl.fromTo("#my-blk", {opacity:0, y:40}, {opacity:1, y:0, duration:0.4, ease:"back.out(2)"}, @to0);
tl.fromTo("#my-thin", {opacity:0}, {opacity:1, duration:0.2}, @to0);
tl.to("#my-thin", {y:-55, rotation:-4, svgOrigin:"600 320", duration:0.6, ease:"back.out(1.8)"}, @to);
tl.set("#my-l2", {opacity:1}, @to); pop("#my-l2 .chip", @to, {from:{rotation:8}, to:{rotation:2}});
""", ts=tsw - 0.1, ta=tas - 0.2, tw=tws - 0.3, tm=tem - 0.1, to0=tot - 0.9, to=tot - 0.3))

# 11 DUST — stippled dust bunny sneezes; a donut ring inks 40 % "from outdoors"
s = "dust"; thd = aw(s, "house dust"); tnm = aw(s, "not mostly"); tfp = aw(s, "forty percent"); tou = aw(s, "from outdoors")
rnd = random.Random(11)
stip = ""
for _ in range(150):
    a = rnd.uniform(0, 2*math.pi); r = 80 * math.sqrt(rnd.uniform(0, 1))
    stip += f'<circle cx="{220 + r*math.cos(a):.0f}" cy="{470 + r*0.8*math.sin(a):.0f}" r="{rnd.uniform(3, 6):.1f}" fill="{rnd.choice([DUST, "#9E978C", SOIL])}"/>'
fuzz = "".join(f'<path class="du-fz" d="M{220 + 86*math.cos(a):.0f},{470 + 70*math.sin(a):.0f} l{14*math.cos(a + .6):.0f},{14*math.sin(a + .6):.0f}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for a in [i * 2 * math.pi / 18 for i in range(18)])
DX, DY, DRR = 640, 330, 175
ea = math.radians(144); ex = DX + DRR * math.sin(ea); ey = DY - DRR * math.cos(ea)
scenes[s] = scene_file(s, f"""
#du-svg {{ position:absolute; left:0; top:180px; }}
#du-c {{ position:absolute; left:0; right:0; top:155px; text-align:center; opacity:0; }}
#du-a {{ position:absolute; left:0; right:0; top:870px; text-align:center; opacity:0; padding-left:300px; }}
#du-ach {{ position:absolute; left:70px; top:470px; opacity:0; {GH} font-size:70px; color:{C['red']}; }}
#du-o {{ position:absolute; left:820px; top:420px; opacity:0; padding:4px 16px; background:rgba(185,137,90,.35); border:3px solid {K}; {GH} font-size:40px; transform:rotate(3deg); }}
""", f"""
  <div id="du-c"><span class="chip" style="background:#FFFFFF;border-color:{C['red']};color:{C['red']}">house dust is NOT mostly skin</span></div>
  <svg id="du-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <circle id="du-ring" cx="{DX}" cy="{DY}" r="{DRR}" fill="none" stroke="{DUST}" stroke-width="70" transform="rotate(-90 {DX} {DY})"/>
    <path id="du-arc" d="M{DX},{DY - DRR} A{DRR},{DRR} 0 0 1 {ex:.1f},{ey:.1f}" fill="none" stroke="{SOIL}" stroke-width="70"/>
    <text id="du-pc" x="{DX}" y="{DY + 22}" text-anchor="middle" style="{GH}font-size:76px" fill="{K}" opacity="0">40%</text>
    <g id="du-bun">{stip}{fuzz}
      <circle cx="195" cy="455" r="7" fill="{K}"/><circle cx="245" cy="455" r="7" fill="{K}"/></g>
  </svg>
  <div id="du-ach">ACHOO!</div>
  <div id="du-a"><span class="chip" style="background:{C['hi']};font-size:52px">about 40% from outdoors</span></div>
""", J("""
pop("#du-bun", 0.05, {from:{scale:0.3, svgOrigin:"220 470"}, to:{svgOrigin:"220 470"}});
ink("#du-ring", 0.2, 0.7);
tl.set("#du-ach", {opacity:1}, @th); pop("#du-ach", @th, {from:{rotation:-20, scale:1.6}, to:{rotation:-8}});
tl.to("#du-bun", {x:12, duration:0.06, yoyo:true, repeat:5}, @th);
tl.set("#du-c", {opacity:1}, @tn); pop("#du-c .chip", @tn, {from:{rotation:-10, scale:1.3}, to:{rotation:-2}});
tl.to("#du-ach", {opacity:0, duration:0.3}, @tn);
ink("#du-arc", @tf, 0.7);
tl.fromTo("#du-pc", {opacity:0}, {opacity:1, duration:0.2}, @tf2);
tl.set("#du-a", {opacity:1}, @to2); pop("#du-a .chip", @to2, {from:{rotation:8}, to:{rotation:2}});
""", th=thd - 0.4, tn=tnm - 0.3, tf=tfp - 0.4, tf2=tfp + 0.1, to=tou - 0.2, to2=tfp + 0.2))

# 12 OUTRO — callback: the sack, about 40 kg of you; a few flakes drift down (Max centre stage, keep y < 620)
s = "outro"; t40 = aw(s, "forty kilos"); tof = aw(s, "one flake"); tsc = aw(s, "stay curious")
od = ["M300,40 Q280,120 330,200", "M780,30 Q820,110 770,190", "M690,60 Q660,130 700,210"]
ofl = "".join(f'<path id="ou-r{i}" d="{d}" fill="none" stroke="none"/><polygon id="ou-f{i}" points="-12,-4 0,-9 13,-3 6,7 -8,6" fill="{FLAKE}" stroke="{K}" stroke-width="2.5" opacity="0"/>' for i, d in enumerate(od))
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#ou-svg {{ position:absolute; left:0; top:200px; }}
#ou-sc {{ top:460px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:58px;background:{FLAKE}">about 40 kg of you</span></div>
  <svg id="ou-svg" width="{W}" height="260" viewBox="0 0 {W} 260" data-layout-ignore>
    <g id="ou-g" opacity="0">{sack("ou", 540, 250, 200)}</g>{ofl}</svg>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
tl.set("#ou-a", {opacity:1}, @t4); pop("#ou-a .chip", @t4, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo("#ou-g", {opacity:0, y:-40}, {opacity:1, y:0, duration:0.4, ease:"back.out(2)"}, @t4);
""" + "".join(f'tl.fromTo("#ou-f{i}", {{opacity:0}}, {{opacity:1, duration:0.15}}, @tf+{i*0.25:.2f}); along("#ou-f{i}", "#ou-r{i}", @tf+{i*0.25:.2f}, 1.6, {{ease:"sine.inOut", rotate:true}});' for i in range(3)) + """
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", t4=t40 - 0.4, tf=tof - 0.3, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "how much"), SC["guess"]["start"] + 0.2)
point(g("guess", "one kilo"), 3.0)
wave(g("intro", "I'm Max"))
point(g("layers", "push up"), 1.2)
point(g("hour", "six hundredths"), 1.2)
point(g("day", "one and a half"), 1.2)
wow(g("year", "half a kilo"), 1.2)
wow(g("life", "forty kilos"), 1.4)
point(g("compare", "about half"), 1.2)
think(g("myth", "some websites"), g("myth", "that assumes"))
point(g("myth", "thin outer"), 1.2)
wow(g("dust", "forty percent"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "dead skin"), 0.35), ("pop.mp3", A("guess", "one kilo"), 0.45), ("pop.mp3", A("guess", "forty kilos"), 0.45),
        ("pop.mp3", A("guess", "three thousand"), 0.5), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("ping.mp3", A("layers", "push up"), 0.4),
        ("click.mp3", A("hour", "six hundredths"), 0.45), ("riser.mp3", A("day", "twenty four"), 0.3), ("ping.mp3", A("year", "half a kilo"), 0.4),
        ("impact-bass-1.mp3", A("life", "forty kilos"), 0.45), ("click-soft.mp3", A("myth", "that assumes"), 0.45),
        ("impact-bass-2.mp3", A("myth", "thin outer"), 0.4), ("pop.mp3", A("dust", "house dust"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
