# MAX WISE ep34 — Why is the ocean salty, but rivers aren't?
# Kit: ink / morph / along helpers + seeded simulations (rain, salt pile-up, vent plume); 2D only.
# Sources: USGS FAQ "Why is the ocean salty?" and USGS Water Science School "Why is the ocean salty?"
# (rain + CO2 -> weak carbonic acid weathers rock; ions run off via streams and rivers; rivers carry too little to taste and keep flowing;
#  evaporation leaves salt behind for hundreds of millions of years; hydrothermal vents add minerals; ~35 g per liter;
#  sodium + chloride > 90 % of ions; spread over land > 500 ft thick ~ a 40-story office building).
# Maths: 35 g / ~17 g per tablespoon of table salt ~ 2 tablespoons; 500 ft / 40 stories = 12.5 ft per floor.
# === SCENES ===
import math as _m
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SEA = "#BFE3F7"; DEEP = "#9CCFEA"; LAND = "#DDEBC8"; SAND = "#E9D3AE"; ROCK = "#CFC6BA"; MIN = ["#E0483C", "#2F5DA8", "#F2B33D", "#7A9E4E", "#8E6BBF"]
SIM = """
const sim = (dur, fn) => { const st={t:0}; tl.fromTo(st, {t:0}, {t:dur, duration:dur, ease:"none", onUpdate:()=>fn(st.t)}, 0); fn(0); };
const clamp = v => Math.max(0, Math.min(1, v));
const $ = id => document.getElementById(id);
"""
def rnd(seed):
    import random as _r
    return _r.Random(seed)

def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.9)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 26px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff;white-space:nowrap">{txt}</span></div>')
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
def crystal(idn, x, y, s=16, rot=0, extra=""):
    return f'<rect id="{idn}" x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s}" height="{s}" rx="2" fill="#FFFFFF" stroke="{K}" stroke-width="3" transform="rotate({rot} {x} {y})" {extra}/>'
DROP = "M0,-24 Q16,2 0,13 Q-16,2 0,-24 Z"
def waves(x0, x1, y, amp=14, step=70):
    d = f"M{x0},{y}"; x = x0; up = True
    while x < x1:
        nx = min(x + step, x1); d += f" Q{(x + nx) / 2:.0f},{y - amp if up else y + amp} {nx},{y}"; x = nx; up = not up
    return d

# 1 HOOK — a river inks itself from a hill into the sea; a drop rides along it; "fresh" vs "salty"; big "?"
s = "hook"; tsp = aw(s, "a salty"); twh = aw(s, "why is"); tsa = aw(s, "salty", 2); tri = aw(s, "rivers"); tar = aw(s, "aren't")
RIV = "M905,560 C860,640 760,600 760,680 C760,740 690,750 640,808"
salt = "".join(crystal(f"hk-c{i}", x, y, 18, r, 'class="hk-c"') for i, (x, y, r) in enumerate([(470, 880, 12), (560, 920, -20), (690, 870, 30), (800, 930, 8), (900, 880, -14), (1000, 925, 22), (620, 945, 40), (960, 845, -5)]))
scenes[s] = scene_file(s, f"""
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#hk-q {{ top:260px; font-size:86px; line-height:1.08; opacity:0; }}
#hk-qm {{ position:absolute; left:150px; top:480px; {GH} font-size:230px; line-height:1; color:{C['red']}; opacity:0; }}
#hk-hill, #hk-sea {{ opacity:0; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="hk-hill" d="M600,640 Q720,470 860,520 Q960,460 1080,540 L1080,640 Z" fill="{LAND}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    <g id="hk-sea"><path d="{waves(380, 1080, 810)} L1080,975 L380,975 Z" fill="{SEA}" stroke="none"/>
      <path d="{waves(380, 1080, 810)}" stroke="{C['blue']}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
    <path id="hk-riv" d="{RIV}" stroke="{C['blue']}" stroke-width="24" fill="none" stroke-linecap="round"/>
    <path id="hk-rin" d="{RIV}" stroke="{SEA}" stroke-width="10" fill="none" stroke-linecap="round"/>
    {salt}
    <g id="hk-dr" opacity="0"><path d="{DROP}" fill="#FFFFFF" stroke="{C['blue']}" stroke-width="5" stroke-linejoin="round"/></g>
  </svg>
  <div id="hk-tag"><span class="chip" style="background:#FFFFFF;transform:rotate(-3deg)">a salty puzzle</span></div>
  <div id="hk-q" class="h1">Why is the ocean <span class="hl">salty</span>,<br>but rivers aren't?</div>
  {tape("hk-fr", "fresh", 820, 650, 4, 50, "rgba(191,227,247,.95)")}
  {tape("hk-sl", "salty", 540, 860, -4, 54)}
  <div id="hk-qm">?</div>
""", J("""
tl.set("#hk-tag", {opacity:1}, @ts); pop("#hk-tag .chip", @ts, {from:{rotation:-14}, to:{rotation:-3}});
tl.fromTo("#hk-hill", {opacity:0, y:30}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, 0.1);
tl.fromTo("#hk-sea", {opacity:0, y:40}, {opacity:1, y:0, duration:0.45, ease:"power3.out"}, 0.2);
ink("#hk-riv", 0.4, 1.0); ink("#hk-rin", 0.5, 1.0);
tl.set("#hk-q", {opacity:1}, @tw); rise("#hk-q", @tw);
tl.set("#hk-dr", {opacity:1}, 1.4); along("#hk-dr", "#hk-riv", 1.4, 1.2, {ease:"power1.in"}); tl.to("#hk-dr", {opacity:0, duration:0.15}, 2.55);
pop(".hk-c", @tsa, {from:{scale:0, transformOrigin:"50% 50%"}, to:{stagger:0.05}});
tl.set("#hk-sl", {opacity:1}, @tsa); pop("#hk-sl span", @tsa, {from:{rotation:-16}, to:{rotation:-4}});
tl.set("#hk-fr", {opacity:1}, @tr); pop("#hk-fr span", @tr, {from:{rotation:16}, to:{rotation:4}});
tl.set("#hk-qm", {opacity:1}, @ta); pop("#hk-qm", @ta, {from:{rotation:-30, scale:1.8}, to:{rotation:8}});
""", ts=tsp, tw=twh - 0.1, tsa=tsa - 0.05, tr=tri - 0.05, ta=tar + 0.1))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "salty fish"); t2 = aw(s, "salt mines"); t3 = aw(s, "rocks on")
notes = [("a", "Salty fish?", -6, 110, SEA), ("b", "Salt mines?", 4, 405, "#E6E6E6"), ("c", "Rocks on land?", -3, 700, C['hi'])]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:80px 14px 0;box-sizing:border-box;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg);
tl.set("#gs-a", {opacity:1}, @t1); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
tl.set("#gs-b", {opacity:1}, @t2); pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}});
tl.set("#gs-c", {opacity:1}, @t3); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3 - 0.25))

# 3 INTRO — logo + underline; a raindrop inks itself (Max centre stage: keep y < 620)
s = "intro"; tmw = aw(s, "max wise"); tfo = aw(s, "let's follow"); trd = aw(s, "raindrop")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:395px; font-size:62px; opacity:0; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Follow one raindrop</span></div>
  <svg class="abs" style="left:0;top:480px" width="{W}" height="140" data-layout-ignore>
    <path id="in-dr" d="M540,8 Q590,80 540,124 Q490,80 540,8 Z" fill="none" stroke="{C['blue']}" stroke-width="8" stroke-linejoin="round"/>
    <path id="in-dh" d="M522,82 Q524,100 538,108" fill="none" stroke="{C['blue']}" stroke-width="5" stroke-linecap="round"/>
  </svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
tl.set("#in-sub", {opacity:1}, @ts); rise("#in-sub", @ts);
ink("#in-dr", @td, 0.6); ink("#in-dh", @td2, 0.25);
tl.fromTo("#in-dr", {attr:{fill:"rgba(191,227,247,0)"}}, {attr:{fill:"rgba(191,227,247,1)"}, duration:0.3}, @td3);
""", tmw=tmw, tu=tmw + 0.3, ts=tfo - 0.1, td=trd - 0.2, td2=trd + 0.35, td3=trd + 0.4))

# 4 RAIN — seeded rain falls from a cloud; CO2 bubbles join; drops turn "acid" green; tape: rain + CO2 = weak acid
s = "rain"; tca = aw(s, "carbon dioxide"); tai = aw(s, "air"); tac = aw(s, "acidic")
R = rnd(4); ND = 26
drops = "".join(f'<g transform="translate(0,0)" id="rn-d{i}"><path class="rn-dp" d="{DROP}" fill="{SEA}" stroke="{C["blue"]}" stroke-width="4" stroke-linejoin="round"/></g>' for i in range(ND))
DX = [round(R.uniform(330, 990)) for _ in range(ND)]; DP = [round(R.random(), 3) for _ in range(ND)]; DV = [round(R.uniform(0.85, 1.15), 3) for _ in range(ND)]
CO = [(380, 470), (560, 430), (760, 480), (930, 440), (470, 600), (840, 620)]
bub = "".join(f'<g id="rn-b{i}" opacity="0"><circle cx="{x}" cy="{y}" r="40" fill="#FFFFFF" stroke="{C["muted"]}" stroke-width="4" stroke-dasharray="8 6"/>'
              f'<text x="{x}" y="{y + 12}" text-anchor="middle" style="{GH}font-size:34px" fill="{C["muted"]}">CO<tspan font-size="22" dy="8">2</tspan></text></g>' for i, (x, y) in enumerate(CO))
CLOUD = "M300,330 Q250,330 252,285 Q256,240 310,244 Q320,180 400,186 Q440,140 510,160 Q570,120 640,160 Q720,140 760,200 Q840,190 850,250 Q900,260 892,300 Q886,334 840,332 Z"
scenes[s] = scene_file(s, f"""
#rn-svg {{ position:absolute; left:0; top:0; }}
#rn-air {{ opacity:0; }}
""", f"""
  <svg id="rn-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <defs><clipPath id="rn-clip"><rect x="250" y="370" width="830" height="490"/></clipPath></defs>
    <g clip-path="url(#rn-clip)">{drops}</g>
    {bub}
    <path id="rn-cl" transform="translate(-40,40)" d="{CLOUD}" fill="#FFFFFF" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path transform="translate(-40,40)" d="M360,290 Q420,300 470,282 M600,296 Q660,306 720,288" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("rn-air", "CO<sub style='font-size:28px'>2</sub> from the air", 640, 140, 3, 44, "rgba(255,255,255,.95)")}
  {tape("rn-ac", "rain + CO<sub style='font-size:30px'>2</sub> = weak acid", 430, 790, -3, 50)}
""", SIM + J("""
const DX=@dx, DP=@dp, DV=@dv;
sim(@dur, t => { for (let i=0;i<DX.length;i++) { const ph=(t*0.9*DV[i]+DP[i])%1; const y=370+ph*520; const x=DX[i]-ph*30;
  $("rn-d"+i).setAttribute("transform", `translate(${x.toFixed(1)},${y.toFixed(1)})`); } });
tl.fromTo("#rn-cl", {scale:0.6, opacity:0, svgOrigin:"530 290"}, {scale:1, opacity:1, svgOrigin:"530 290", duration:0.4, ease:"back.out(2)"}, 0.0);
""", dx=DX, dp=DP, dv=DV, dur=SC[s]["slot"])
  + "".join(f'tl.fromTo("#rn-b{i}", {{opacity:0, scale:0.3, svgOrigin:"{x} {y}"}}, {{opacity:1, scale:1, svgOrigin:"{x} {y}", duration:0.3, ease:"back.out(2)"}}, {tca - 0.1 + i * 0.1:.3f});\n'
            f'tl.to("#rn-b{i}", {{y:40, duration:1.6, ease:"sine.inOut", yoyo:true, repeat:1}}, {tca + 0.3 + i * 0.1:.3f});\n' for i, (x, y) in enumerate(CO))
  + J("""
tl.set("#rn-air", {opacity:1}, @ta); pop("#rn-air span", @ta, {from:{rotation:12}, to:{rotation:3}});
tl.to(".rn-dp", {attr:{fill:"#D8EDA0"}, stroke:"#6E9A2E", duration:0.4}, @tc);
tl.to("[id^=rn-b]", {opacity:0, scale:0.2, duration:0.3, ease:"power2.in"}, @tc);
tl.set("#rn-ac", {opacity:1}, @tc2); pop("#rn-ac span", @tc2, {from:{rotation:-14, scale:1.4}, to:{rotation:-3}});
""", ta=tai - 0.3, tc=aw(s, "which makes") - 0.1, tc2=aw(s, "which makes")))

# 5 ROCK — acid drops hit a hatched boulder; it morphs smaller (nibbled); mineral bits break off and dissolve
s = "rock"; twa = aw(s, "weak acid"); tni = aw(s, "nibbles"); tti = aw(s, "tiny bits"); tmi = aw(s, "minerals"); tdi = aw(s, "dissolve")
CX, CY, RX, RY_ = 560, 600, 230, 175
R = rnd(11); NP = 16; base = [R.uniform(0.9, 1.06) for _ in range(NP)]
def rock(bites, shrink=1.0):
    pts = []
    for i in range(NP):
        a = -_m.pi / 2 + i * 2 * _m.pi / NP; r = base[i] * shrink * bites.get(i, 1.0)
        y = CY + _m.sin(a) * RY_ * r
        pts.append((CX + _m.cos(a) * RX * r, min(y, CY + RY_ * 0.92)))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
R0 = rock({}); R1 = rock({1: 0.78, 2: 0.7, 3: 0.82, 14: 0.85}); R2 = rock({0: 0.86, 1: 0.66, 2: 0.58, 3: 0.7, 4: 0.85, 13: 0.84, 14: 0.72, 15: 0.8}, 0.93)
AD = [(470, 0.3), (590, 0.55), (680, 0.8), (520, 1.05), (640, 1.3)]
acid = "".join(f'<g id="rk-a{i}" transform="translate({x},180)" opacity="0"><path d="{DROP}" fill="#D8EDA0" stroke="#6E9A2E" stroke-width="4" stroke-linejoin="round"/></g>' for i, (x, _) in enumerate(AD))
BITS = [(640, 450), (700, 480), (590, 440), (740, 530), (480, 450), (660, 470), (720, 505), (610, 455), (530, 445), (690, 460)]
bits = "".join(f'<circle id="rk-b{i}" cx="{x}" cy="{y}" r="13" fill="{MIN[i % 5]}" stroke="{K}" stroke-width="3" opacity="0"/>' for i, (x, y) in enumerate(BITS))
scenes[s] = scene_file(s, f"""
#rk-svg {{ position:absolute; left:0; top:0; }}
#rk-wa {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#rk-nom {{ position:absolute; left:790px; top:300px; {GH} font-size:72px; color:{C['red']}; opacity:0; }}
#rk-rock {{ opacity:0; }}
""", f"""
  <svg id="rk-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <defs><pattern id="rk-h" width="18" height="18" patternUnits="userSpaceOnUse" patternTransform="rotate(40)">
      <rect width="18" height="18" fill="{ROCK}"/><path d="M0,0 L0,18" stroke="#A89E90" stroke-width="5"/></pattern></defs>
    <path id="rk-pud" d="M330,800 Q560,760 1010,800 Q1030,850 1000,870 Q600,900 360,866 Q320,840 330,800 Z" fill="{SEA}" stroke="{C['blue']}" stroke-width="5"/>
    <path id="rk-rock" d="{R0}" fill="url(#rk-h)" stroke="{K}" stroke-width="8" stroke-linejoin="round"/>
    {acid}{bits}
  </svg>
  <div id="rk-wa"><span class="chip" style="background:#D8EDA0;transform:rotate(-2deg)">weak acid</span></div>
  <div id="rk-nom">nom nom</div>
  {tape("rk-mt", "minerals", 790, 470, 4, 50)}
""", J("""
tl.fromTo("#rk-rock", {opacity:0, y:40}, {opacity:1, y:0, duration:0.35, ease:"back.out(1.6)"}, 0.0);
tl.set("#rk-wa", {opacity:1}, @tw); pop("#rk-wa .chip", @tw);
""", tw=twa - 0.1)
  + "".join(f'tl.set("#rk-a{i}", {{opacity:1}}, {t:.2f}); tl.fromTo("#rk-a{i}", {{y:0}}, {{y:{CY - RY_ - 175 + 20 + (abs(x - CX) // 8)}, duration:0.45, ease:"power2.in", immediateRender:false}}, {t:.2f}); tl.to("#rk-a{i}", {{opacity:0, scaleX:1.8, scaleY:0.3, duration:0.15}}, {t + 0.45:.2f});\n' for i, (x, t) in enumerate(AD))
  + J("""
morph("#rk-rock", "@r1", @tn, 0.45, {ease:"back.out(1.5)"});
tl.set("#rk-nom", {opacity:1}, @tn); pop("#rk-nom", @tn, {from:{rotation:-20, scale:1.6}, to:{rotation:-6}});
tl.fromTo("#rk-rock", {x:0}, {x:7, duration:0.05, yoyo:true, repeat:5, immediateRender:false}, @tn);
pop("[id^=rk-b]", @tt, {from:{scale:0, transformOrigin:"50% 50%"}, to:{stagger:0.06}});
tl.set("#rk-mt", {opacity:1}, @tm); pop("#rk-mt span", @tm, {from:{rotation:14}, to:{rotation:4}});
morph("#rk-rock", "@r2", @td, 0.5, {ease:"power2.inOut"});
""", r1=R1, r2=R2, tn=tni - 0.1, tt=tti - 0.1, tm=tmi - 0.1, td=tdi - 0.2)
  + "".join(f'tl.to("#rk-b{i}", {{x:{(i * 47) % 260 - 120 + (CX - x) * 0.2:.0f}, y:{820 - y + (i % 3) * 14}, scale:0.45, opacity:0.55, duration:0.9, ease:"power1.in"}}, {tdi - 0.1 + i * 0.05:.3f});\n' for i, (x, y) in enumerate(BITS)))

# 6 RIVER — streams ink in from the hills, join a river to the sea; mineral dots ride along; a spoon with just a pinch
s = "river"; tst = aw(s, "streams"); tri = aw(s, "then rivers") + 0.2; tca = aw(s, "rivers carry"); tpi = aw(s, "pinch"); tta = aw(s, "taste"); tkf = aw(s, "keep flowing")
STR = ["M170,440 Q330,480 560,560", "M320,440 Q430,490 560,560", "M470,440 Q520,500 560,560"]
RV = "M560,560 C660,630 600,720 760,760 C860,785 900,840 1000,890"
NDOT = 8
dots = "".join(f'<circle id="rv-d{i}" cx="0" cy="0" r="11" fill="{MIN[i % 5]}" stroke="{K}" stroke-width="3" opacity="0"/>' for i in range(NDOT))
scenes[s] = scene_file(s, f"""
#rv-svg {{ position:absolute; left:0; top:0; }}
#rv-mt, #rv-sea, #rv-sp, #rv-rv, #rv-rvi {{ opacity:0; }}
#rv-pc {{ position:absolute; left:640px; top:150px; opacity:0; }}
#rv-kf {{ position:absolute; left:420px; top:830px; opacity:0; }}
""", f"""
  <svg id="rv-svg" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <path id="rv-mt" d="M70,450 L200,250 L280,330 L380,190 L540,450 Z" fill="{LAND}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    <path id="rv-sea" d="M780,975 Q820,880 1080,830 L1080,975 Z" fill="{SEA}" stroke="{C['blue']}" stroke-width="6" stroke-linejoin="round"/>
    {''.join(f'<path id="rv-st{i}" d="{d}" stroke="{C["blue"]}" stroke-width="10" fill="none" stroke-linecap="round"/>' for i, d in enumerate(STR))}
    <path id="rv-rv" d="{RV}" stroke="{C['blue']}" stroke-width="30" fill="none" stroke-linecap="round"/>
    <path id="rv-rvi" d="{RV}" stroke="{SEA}" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="26 22"/>
    {dots}
    <g id="rv-sp"><path d="M850,268 L1020,200" stroke="{K}" stroke-width="16" stroke-linecap="round"/>
      <ellipse cx="770" cy="290" rx="100" ry="46" fill="#FFFFFF" stroke="{K}" stroke-width="7"/>
      {crystal("rv-c0", 760, 286, 14, 20)}{crystal("rv-c1", 780, 292, 12, -10)}{crystal("rv-c2", 770, 276, 10, 35)}</g>
  </svg>
  <div id="rv-pc"><span class="chip" style="background:#FFFFFF;transform:rotate(-3deg)">just a pinch</span></div>
  {tape("rv-ta", "too little to taste", 640, 380, 3, 46)}
  <div id="rv-kf"><span class="chip" style="background:{SEA};font-size:46px;transform:rotate(-2deg)">and it keeps flowing</span></div>
""", J("""
tl.fromTo("#rv-mt", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, 0.0);
tl.fromTo("#rv-sea", {opacity:0, x:60}, {opacity:1, x:0, duration:0.4, ease:"power3.out"}, 0.15);
ink("[id^=rv-st]", @ts, 0.6, {stagger:0.15});
tl.set("#rv-rv, #rv-rvi", {opacity:1}, @tr); ink("#rv-rv", @tr, 0.8);
tl.fromTo("#rv-rvi", {strokeDashoffset:0}, {strokeDashoffset:-480, duration:@fl, ease:"none"}, @tr);
tl.fromTo("#rv-sp", {opacity:0, scale:0.5, svgOrigin:"850 260"}, {opacity:1, scale:1, svgOrigin:"850 260", duration:0.35, ease:"back.out(2)"}, @tp0);
tl.set("#rv-pc", {opacity:1}, @tp); pop("#rv-pc .chip", @tp, {from:{rotation:-12}, to:{rotation:-3}});
tl.set("#rv-ta", {opacity:1}, @tt); pop("#rv-ta span", @tt, {from:{rotation:14}, to:{rotation:3}});
tl.set("#rv-kf", {opacity:1}, @tk); pop("#rv-kf .chip", @tk, {from:{rotation:-10}, to:{rotation:-2}});
""", ts=tst - 0.2, tr=tri - 0.2, fl=SC[s]["slot"] - tri, tp0=tpi - 0.5, tp=tpi - 0.05, tt=tta - 0.3, tk=tkf - 0.3)
  + "".join(f'tl.set("#rv-d{i}", {{opacity:1}}, {tca - 0.2 + i * 0.25:.3f}); along("#rv-d{i}", "#rv-rv", {tca - 0.2 + i * 0.25:.3f}, 1.7, {{ease:"none", repeat:2}});\n' for i in range(NDOT)))

# 7 OCEAN — dead end tank: salt crystals flow in and pile on the floor (seeded); vapour rises to the sun; water leaves, salt stays
s = "ocean"; tde = aw(s, "dead end"); tsu = aw(s, "the sun"); tva = aw(s, "vapor"); tsb = aw(s, "stays behind"); thu = aw(s, "hundreds"); tpu = aw(s, "piles up")
NC, COLS = 105, 21
R = rnd(21); slots = []
for row in range(NC // COLS):
    cs = list(range(COLS)); R.shuffle(cs); slots += [(452 + c * 27 + R.uniform(-3, 3), 858 - row * 22) for c in cs]
SX = [round(x, 1) for x, _ in slots]; SY = [round(y, 1) for _, y in slots]; SR = [R.randint(-30, 30) for _ in range(NC)]
cry = "".join(f'<rect id="oc-k{i}" x="-9" y="-9" width="18" height="18" rx="2" fill="#FFFFFF" stroke="{K}" stroke-width="3" opacity="0"/>' for i in range(NC))
WATER = "M424,472 L1016,472 L1016,820 Q1016,876 960,876 L480,876 Q424,876 424,820 Z"
vap = "".join(f'<g transform="translate({x},455)"><g id="oc-v{i}" opacity="0"><path d="M0,0 Q14,-22 0,-44 Q-14,-66 0,-88" stroke="{C["pencil"]}" stroke-width="6" fill="none" stroke-linecap="round"/></g></g>' for i, x in enumerate((800, 860, 920, 980)))
scenes[s] = scene_file(s, f"""
#oc-svg {{ position:absolute; left:0; top:0; }}
#oc-tank, #oc-sun {{ opacity:0; }}
""", f"""
  <svg id="oc-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="oc-sun"><circle cx="910" cy="230" r="62" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>
      {''.join(f'<path d="M{910 + 80 * _m.cos(a):.0f},{230 + 80 * _m.sin(a):.0f} L{910 + 108 * _m.cos(a):.0f},{230 + 108 * _m.sin(a):.0f}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>' for a in [k * _m.pi / 4 for k in range(8)])}</g>
    <g id="oc-tank">
      <path d="{WATER}" fill="{SEA}"/>
      <path d="{waves(424, 1016, 472, 10, 74)}" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <path d="M150,340 Q330,330 440,488" stroke="{C['blue']}" stroke-width="30" fill="none" stroke-linecap="round"/>
      <path d="M150,340 Q330,330 440,488" stroke="{SEA}" stroke-width="14" fill="none" stroke-linecap="round"/>
      <path d="M420,430 L420,820 Q420,880 480,880 L960,880 Q1020,880 1020,820 L1020,430" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    {vap}{cry}
  </svg>
  {stamp("oc-de", "DEAD END", 110, 160, -8, 64)}
  {tape("oc-wl", "water leaves", 470, 380, -3, 44, "rgba(255,255,255,.95)")}
  {tape("oc-ss", "salt stays", 600, 600, 3, 54)}
  {tape("oc-yr", "100s of millions of years", 100, 255, -2, 44, "rgba(191,227,247,.95)")}
""", SIM + J("""
const SX=@sx, SY=@sy, SR=@sr, N=SX.length;
const T0 = k => 0.3 + 8.4*Math.pow(k/N, 0.62);
sim(@dur, t => { for (let k=0;k<N;k++) { const el=$("oc-k"+k); const p=(t-T0(k))/1.2;
  if (p<0) { el.setAttribute("opacity","0"); continue; } const q=clamp(p); const e=1-Math.pow(1-q,2);
  const x=440+(SX[k]-440)*e, y=490+(SY[k]-490)*Math.pow(q,1.3), r=SR[k]*q+q*200;
  el.setAttribute("opacity","1"); el.setAttribute("transform", `translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(0)})`); } });
tl.fromTo("#oc-tank", {opacity:0, y:40}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, 0.0);
tl.set("#oc-de", {opacity:1}, @td); pop("#oc-de span", @td, {from:{rotation:-26, scale:1.8}, to:{rotation:-8}});
tl.fromTo("#oc-sun", {opacity:0, scale:0.4, svgOrigin:"910 230"}, {opacity:1, scale:1, svgOrigin:"910 230", duration:0.4, ease:"back.out(2)"}, @tsu);
tl.to("#oc-sun", {rotation:30, svgOrigin:"910 230", duration:@sr2, ease:"none"}, @tsu2);
tl.set("#oc-wl", {opacity:1}, @tv); pop("#oc-wl span", @tv, {from:{rotation:-12}, to:{rotation:-3}});
tl.set("#oc-ss", {opacity:1}, @tsb); pop("#oc-ss span", @tsb, {from:{rotation:14, scale:1.4}, to:{rotation:3}});
tl.set("#oc-yr", {opacity:1}, @th); pop("#oc-yr span", @th, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#oc-tank", {scale:1, svgOrigin:"720 880"}, {scale:1.03, svgOrigin:"720 880", duration:0.15, yoyo:true, repeat:1, immediateRender:false}, @tp);
""", sx=SX, sy=SY, sr=SR, dur=SC[s]["slot"], td=tde - 0.15, tsu=tsu - 0.1, tsu2=tsu + 0.3, sr2=SC[s]["slot"] - tsu - 0.6, tv=tva - 0.2, tsb=tsb - 0.1, th=thu - 0.1, tp=tpu)
  + "".join(f'tl.fromTo("#oc-v{i}", {{opacity:1, y:0}}, {{opacity:0, y:-170, duration:1.3, ease:"power1.out", repeat:4, immediateRender:false}}, {tsu + 0.3 + i * 0.3:.3f});\n' for i in range(4)))

# 8 VENTS — cutaway sea floor: a hot vent chimney puffs mineral dots (seeded plume); tape labels
s = "vents"; tbo = aw(s, "bonus"); thv = aw(s, "hot vents"); tsf = aw(s, "sea floor"); tmi = aw(s, "more minerals")
R = rnd(8); NPL = 40
PL = [(round(R.random(), 3), round(R.random(), 3), MIN[R.randrange(5)] if R.random() < 0.55 else "#55555F") for _ in range(NPL)]
plume = "".join(f'<circle id="vt-p{i}" cx="0" cy="0" r="{8 + (i % 4) * 2}" fill="{c}" stroke="{K}" stroke-width="2" opacity="0"/>' for i, (_, _, c) in enumerate(PL))
FLOOR = "M64,700 Q200,660 330,690 Q450,720 600,690 Q700,672 820,690 Q920,705 1016,680 L1016,846 L64,846 Z"
stip = "".join(f'<circle cx="{R.randint(80, 1000)}" cy="{R.randint(730, 835)}" r="3" fill="#A88F6A"/>' for _ in range(60))
scenes[s] = scene_file(s, f"""
#vt-svg {{ position:absolute; left:0; top:0; }}
#vt-cut {{ opacity:0; }}
""", f"""
  <svg id="vt-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="vt-cut">
      <rect x="64" y="160" width="952" height="686" rx="24" fill="{DEEP}"/>
      <rect x="64" y="160" width="952" height="120" rx="24" fill="{SEA}"/>
      <path d="{FLOOR}" fill="{SAND}"/>{stip}
      <path d="M64,700 Q200,660 330,690 Q450,720 600,690 Q700,672 820,690 Q920,705 1016,680" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
      <path d="M300,692 L314,630 Q330,622 346,630 L360,700 Z" fill="#55555F" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M648,694 L672,500 Q700,486 728,500 L754,694 Z" fill="#55555F" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
      <ellipse cx="700" cy="498" rx="26" ry="9" fill="{C['red']}" stroke="{K}" stroke-width="4"/>
      <rect x="64" y="160" width="952" height="686" rx="24" fill="none" stroke="{K}" stroke-width="6" stroke-dasharray="20 12"/>
    </g>
    <path id="vt-ld" d="M760,560 L830,545" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    {plume}
  </svg>
  {stamp("vt-bo", "BONUS!", 110, 190, -8, 66)}
  {tape("vt-hv", "hot vent", 830, 515, 4, 48, "rgba(255,201,194,.95)")}
  {tape("vt-sf", "sea floor", 420, 760, -3, 46)}
  {tape("vt-mm", "more minerals!", 110, 360, -3, 50, "rgba(255,255,255,.95)")}
""", SIM + J("""
const PL=@pl, N=PL.length;
sim(@dur, t => { for (let k=0;k<N;k++) { const el=$("vt-p"+k); const t0=@t0+k*0.08; const p=(t-t0)/1.9;
  if (p<0||p>1) { el.setAttribute("opacity","0"); continue; }
  const x=700+(PL[k][0]-0.5)*260*p+Math.sin(p*7+PL[k][1]*6)*14, y=490-p*300;
  el.setAttribute("opacity", (1-p*p).toFixed(2)); el.setAttribute("transform", `translate(${x.toFixed(1)},${y.toFixed(1)})`); } });
tl.fromTo("#vt-cut", {opacity:0, scale:0.92, svgOrigin:"540 500"}, {opacity:1, scale:1, svgOrigin:"540 500", duration:0.35, ease:"back.out(1.6)"}, 0.0);
tl.set("#vt-bo", {opacity:1}, @tb); pop("#vt-bo span", @tb, {from:{rotation:-26, scale:1.8}, to:{rotation:-8}});
ink("#vt-ld", @th, 0.25); tl.set("#vt-hv", {opacity:1}, @th); pop("#vt-hv span", @th, {from:{rotation:14}, to:{rotation:4}});
tl.set("#vt-sf", {opacity:1}, @ts); pop("#vt-sf span", @ts, {from:{rotation:-12}, to:{rotation:-3}});
tl.set("#vt-mm", {opacity:1}, @tm); pop("#vt-mm span", @tm, {from:{rotation:-14, scale:1.4}, to:{rotation:-3}});
""", pl=[[a, b] for a, b, _ in PL], dur=SC[s]["slot"], t0=thv - 0.2, tb=tbo, th=thv - 0.1, ts=tsf - 0.1, tm=tmi - 0.2))

# 9 SPOON — 1 liter bottle; counter 0 -> 35 g with one crystal per gram; two tablespoons pop in; mostly sodium + chloride
s = "spoon"; tli = aw(s, "one liter"); tsw = aw(s, "sea water"); t35 = aw(s, "thirty five"); tgr = aw(s, "grams"); t2 = aw(s, "two tablespoons"); ttb = aw(s, "tablespoons")
tso = aw(s, "sodium"); tch = aw(s, "chloride"); tts = aw(s, "table salt")
R = rnd(35)
grams = "".join(crystal(f"sp-g{i}", 470 + (i % 5) * 34, 790 - (i // 5) * 46, 18, R.randint(-30, 30), 'class="sp-g" opacity="0"') for i in range(35))
def tbsp(idn, cy):
    heap = "".join(crystal(f"{idn}-c{j}", 735 + j * 16, cy - 10 - (j % 2) * 8, 13, R.randint(-30, 30)) for j in range(5))
    return (f'<g id="{idn}" opacity="0"><path d="M850,{cy - 6} L1030,{cy - 46}" stroke="{K}" stroke-width="14" stroke-linecap="round"/>'
            f'<ellipse cx="770" cy="{cy}" rx="86" ry="40" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>'
            f'<path d="M700,{cy - 4} Q770,{cy - 40} 840,{cy - 4} Z" fill="#FFFFFF" stroke="{C["pencil"]}" stroke-width="3"/>{heap}</g>')
BOT = "M505,250 L565,250 L565,320 Q640,340 640,400 L640,800 Q640,840 600,840 L470,840 Q430,840 430,800 L430,400 Q430,340 505,320 Z"
scenes[s] = scene_file(s, f"""
#sp-svg {{ position:absolute; left:0; top:0; }}
#sp-t {{ position:absolute; left:0; right:0; top:140px; text-align:center; opacity:0; }}
#sp-cnt {{ position:absolute; left:680px; top:250px; width:380px; {GH} font-size:120px; line-height:1; opacity:0; }}
#sp-2 {{ position:absolute; left:690px; top:610px; opacity:0; }}
#sp-na {{ position:absolute; left:660px; top:720px; width:400px; padding:10px 16px; background:#FFFFFF; border:4px solid {K}; {SKETCH} {GH} font-size:44px; line-height:1.15; text-align:center; opacity:0; }}
#sp-na span {{ display:inline-block; opacity:0; }}
#sp-bot, #sp-wat {{ opacity:0; }}
""", f"""
  <svg id="sp-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <defs><clipPath id="sp-clip"><path d="{BOT}"/></clipPath></defs>
    <g id="sp-wat" clip-path="url(#sp-clip)"><rect id="sp-wr" x="420" y="370" width="230" height="480" fill="{SEA}"/>
      <path d="{waves(420, 650, 372, 8, 46)}" stroke="{C['blue']}" stroke-width="4" fill="none"/></g>
    <path id="sp-bot" d="{BOT}" fill="none" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    {grams}
    {tbsp("sp-s1", 460)}{tbsp("sp-s2", 560)}
  </svg>
  <div id="sp-t"><span class="chip">1 liter of sea water</span></div>
  <div id="sp-cnt">≈ <span id="sp-n" class="red">0</span> g</div>
  <div id="sp-2"><span class="pill" style="font-size:50px">≈ 2 tablespoons</span></div>
  <div id="sp-na"><span id="sp-na1">mostly <b class="red">sodium</b></span><br><span id="sp-na2">+ <b class="blue">chloride</b></span><br><span id="sp-na3" class="hl">= table salt</span></div>
""", J("""
tl.set("#sp-t", {opacity:1}, @tl); pop("#sp-t .chip", @tl, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#sp-bot", {opacity:0, y:40}, {opacity:1, y:0, duration:0.35, ease:"back.out(1.6)"}, @tl);
tl.set("#sp-wat", {opacity:1}, @tw); tl.fromTo("#sp-wr", {y:470}, {y:0, duration:0.7, ease:"power2.out"}, @tw);
tl.set("#sp-cnt", {opacity:1}, @t3); pop("#sp-cnt", @t3);
count("#sp-n", 0, 35, @t3, @cd, v => String(Math.round(v)));
pop(".sp-g", @t3, {from:{scale:0, transformOrigin:"50% 50%"}, to:{stagger:@gs, duration:0.2}});
tl.set("#sp-s1", {opacity:1}, @ta); tl.fromTo("#sp-s1", {scale:0.3, svgOrigin:"850 460"}, {scale:1, svgOrigin:"850 460", duration:0.35, ease:"back.out(2.2)"}, @ta);
tl.set("#sp-s2", {opacity:1}, @tb); tl.fromTo("#sp-s2", {scale:0.3, svgOrigin:"850 560"}, {scale:1, svgOrigin:"850 560", duration:0.35, ease:"back.out(2.2)"}, @tb);
tl.set("#sp-2", {opacity:1}, @tb2); pop("#sp-2 .pill", @tb2, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#sp-na", {opacity:0, y:30}, {opacity:1, y:0, duration:0.3, ease:"back.out(1.6)"}, @tn);
tl.to("#sp-na1", {opacity:1, duration:0.2}, @tn); tl.to("#sp-na2", {opacity:1, duration:0.2}, @tc);
tl.set("#sp-na3", {opacity:1}, @tt); pop("#sp-na3", @tt, {from:{rotation:-8}, to:{}});
""", tl=tli - 0.1, tw=tsw - 0.1, t3=t35 - 0.05, cd=tgr - t35 + 0.4, gs=round((tgr - t35 + 0.2) / 35, 4), ta=t2 - 0.1, tb=ttb - 0.05, tb2=ttb + 0.4,
       tn=tso - 0.2, tc=tch - 0.1, tt=tts - 0.15))

# 10 LAYER — the salt slab grows over the land; a ruler counts 0..500 ft; a 40-story building fills floor by floor (same scale)
s = "layer"; tspr = aw(s, "spread all"); tla = aw(s, "the land"); t5 = aw(s, "five hundred"); tth = aw(s, "thick"); tta = aw(s, "as tall"); t40 = aw(s, "forty story"); tbu = aw(s, "building")
GY, TOP = 820, 320  # ground y; 500 ft -> y 320 (1 px per foot)
ticks = "".join(f'<path d="M712,{GY - f} L{742 if f % 100 == 0 else 730},{GY - f}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for f in range(0, 501, 50))
tlab = "".join(f'<text x="752" y="{GY - f + 12}" style="{GH}font-size:34px" fill="{K}">{f}</text>' for f in range(0, 501, 100))
floors = "".join(f'<rect class="ly-f" x="852" y="{GY - (k + 1) * 12.5 + 2:.1f}" width="146" height="8.5" fill="{C["hi"]}" stroke="{K}" stroke-width="1.5" opacity="0"/>' for k in range(40))
R = rnd(50)
slabdots = "".join(f'<rect x="{R.randint(440, 680)}" y="{R.randint(TOP + 10, GY - 10)}" width="10" height="10" fill="none" stroke="#9DB3C4" stroke-width="2" transform="rotate({R.randint(0, 80)})" transform-origin="center"/>' for _ in range(0))
scenes[s] = scene_file(s, f"""
#ly-svg {{ position:absolute; left:0; top:0; }}
#ly-t {{ position:absolute; left:0; right:0; top:140px; text-align:center; opacity:0; }}
#ly-big {{ position:absolute; left:70px; top:360px; width:350px; text-align:center; opacity:0; }}
#ly-big .big {{ font-size:104px; color:{C['red']}; }}
#ly-40 {{ position:absolute; left:820px; top:235px; opacity:0; }}
#ly-land, #ly-rul, #ly-bld {{ opacity:0; }}
""", f"""
  <svg id="ly-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <defs><pattern id="ly-h" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)">
      <rect width="22" height="22" fill="#FFFFFF"/><path d="M0,0 L0,22" stroke="#D6E4EE" stroke-width="6"/></pattern></defs>
    <g id="ly-land"><rect x="420" y="{GY}" width="620" height="34" fill="{SAND}" stroke="{K}" stroke-width="5"/>
      <path d="M540,{GY} L540,{GY - 46} L570,{GY - 72} L600,{GY - 46} L600,{GY} Z" fill="#FFC9C2" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>
      <path d="M650,{GY} L650,{GY - 30}" stroke="{K}" stroke-width="5"/><circle cx="650" cy="{GY - 46}" r="20" fill="{LAND}" stroke="{K}" stroke-width="4"/></g>
    <rect id="ly-slab" x="432" y="{TOP}" width="256" height="{GY - TOP}" fill="url(#ly-h)" stroke="{K}" stroke-width="6" opacity=".93"/>
    <g id="ly-rul"><path d="M712,{GY} L712,{TOP - 20}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>{ticks}{tlab}
      <text x="712" y="{GY + 74}" text-anchor="middle" style="{GH}font-size:36px" fill="{C['muted']}">feet</text></g>
    <path id="ly-mk" d="M696,{GY} L668,{GY - 16} L668,{GY + 16} Z" fill="{C['red']}" stroke="{K}" stroke-width="4" stroke-linejoin="round" opacity="0"/>
    <g id="ly-bld"><rect x="846" y="{TOP}" width="158" height="{GY - TOP}" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>
      <path d="M900,{TOP} L900,{TOP - 26} M950,{TOP} L950,{TOP - 40}" stroke="{K}" stroke-width="5" stroke-linecap="round"/></g>
    {floors}
  </svg>
  <div id="ly-t"><span class="chip" style="background:#FFFFFF;transform:rotate(-2deg)">all of it, spread over the land</span></div>
  <div id="ly-big"><div class="big">500+ ft</div><div style="{GH}font-size:52px">thick!</div></div>
  <div id="ly-40"><span class="chip" style="font-size:46px;transform:rotate(3deg)">40 stories</span></div>
""", J("""
tl.set("#ly-t", {opacity:1}, @ts); pop("#ly-t .chip", @ts, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#ly-land", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, @tl);
tl.fromTo("#ly-rul", {opacity:0, x:30}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, @tl2);
tl.fromTo("#ly-slab", {scaleY:0, svgOrigin:"560 @gy"}, {scaleY:1, svgOrigin:"560 @gy", duration:@sd, ease:"power2.inOut"}, @t5);
tl.set("#ly-mk", {opacity:1}, @t5); tl.to("#ly-mk", {y:-500, duration:@sd, ease:"power2.inOut"}, @t5);
tl.set("#ly-big", {opacity:1}, @t5b); pop("#ly-big", @t5b, {from:{rotation:-10, scale:1.5}, to:{rotation:-3}});
tl.fromTo("#ly-bld", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"back.out(1.6)"}, @tt);
tl.to(".ly-f", {opacity:1, duration:0.04, stagger:@fs}, @t4);
tl.set("#ly-40", {opacity:1}, @t4b); pop("#ly-40 .chip", @t4b, {from:{rotation:14, scale:1.4}, to:{rotation:3}});
""", ts=tspr - 0.05, tl=tla - 0.2, tl2=tla + 0.1, gy=GY, t5=t5 - 0.3, sd=tth - t5 + 0.5, t5b=t5 + 0.1, tt=tta - 0.1, t4=t40 - 0.1, fs=round((tbu - t40 + 0.2) / 40, 4), t4b=tbu))

# 11 OUTRO — callback: a river pours salt into a jar labelled OCEAN, which keeps it (Max centre stage: keep y < 620)
s = "outro"; tri = aw(s, "rivers deliver"); tde = aw(s, "deliver"); toc = aw(s, "the ocean"); tke = aw(s, "keeps"); tsc = aw(s, "stay curious")
ORV = "M90,230 C220,180 330,300 470,240 C560,200 620,190 700,215"
ND = 10
od = "".join(f'<rect id="ou-d{i}" x="-8" y="-8" width="16" height="16" rx="2" fill="#FFFFFF" stroke="{K}" stroke-width="3" opacity="0"/>' for i in range(ND))
scenes[s] = scene_file(s, f"""
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-sc {{ top:470px; font-size:110px; opacity:0; }}
#ou-jar, #ou-rv, #ou-rvi {{ opacity:0; }}
""", f"""
  <svg id="ou-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <defs><clipPath id="ou-clip"><path d="M690,200 L960,200 L960,420 Q960,450 930,450 L720,450 Q690,450 690,420 Z"/></clipPath></defs>
    <path id="ou-rv" d="{ORV}" stroke="{C['blue']}" stroke-width="28" fill="none" stroke-linecap="round"/>
    <path id="ou-rvi" d="{ORV}" stroke="{SEA}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <g id="ou-jar"><g clip-path="url(#ou-clip)"><rect x="690" y="250" width="270" height="200" fill="{SEA}"/>
      <rect id="ou-salt" x="690" y="400" width="270" height="60" fill="#FFFFFF" stroke="{K}" stroke-width="3"/></g>
      <path d="M690,190 L690,420 Q690,452 722,452 L928,452 Q960,452 960,420 L960,190" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
      <rect x="730" y="300" width="190" height="56" rx="6" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>
      <text x="825" y="341" text-anchor="middle" style="{GH}font-size:40px" fill="{K}">OCEAN</text></g>
    {od}
  </svg>
  {tape("ou-t1", "rivers deliver", 120, 300, -4, 50, "rgba(191,227,247,.95)")}
  {tape("ou-t2", "the ocean keeps it", 580, 475, 3, 46)}
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
tl.set("#ou-rv, #ou-rvi", {opacity:1}, 0.1); ink("#ou-rv", 0.1, 0.6); ink("#ou-rvi", 0.2, 0.6);
tl.fromTo("#ou-jar", {opacity:0, scale:0.6, svgOrigin:"825 450"}, {opacity:1, scale:1, svgOrigin:"825 450", duration:0.4, ease:"back.out(2)"}, 0.3);
tl.set("#ou-t1", {opacity:1}, @tr); pop("#ou-t1 span", @tr, {from:{rotation:-14}, to:{rotation:-4}});
tl.fromTo("#ou-salt", {y:50}, {y:0, duration:@sd, ease:"power1.inOut", immediateRender:false}, @td);
tl.set("#ou-t2", {opacity:1}, @tk); pop("#ou-t2 span", @tk, {from:{rotation:14}, to:{rotation:3}});
tl.to("#ou-t1, #ou-t2", {opacity:0, y:-20, duration:0.25, ease:"power2.in"}, @tx);
tl.set("#ou-sc", {opacity:1}, @tsc); pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", tr=tri - 0.05, td=tde, sd=tke - tde + 0.3, tk=toc - 0.1, tx=tsc - 0.3, tsc=tsc)
  + "".join(f'tl.set("#ou-d{i}", {{opacity:1}}, {tde - 0.1 + i * 0.2:.3f}); along("#ou-d{i}", "#ou-rv", {tde - 0.1 + i * 0.2:.3f}, 0.9, {{ease:"power1.in"}}); tl.to("#ou-d{i}", {{y:"+=120", opacity:0, duration:0.35, ease:"power2.in"}}, {tde + 0.8 + i * 0.2:.3f});\n' for i in range(ND)), fade=False)
# === GESTURES ===
think(g("hook", "why is"), SC["guess"]["start"] + 0.2)
point(g("guess", "salty fish"), 2.4)
wave(g("intro", "I'm Max"))
point(g("rain", "carbon dioxide"), 1.3)
point(g("rock", "nibbles"), 1.2)
point(g("river", "pinch"), 1.2)
wow(g("ocean", "piles up"), 1.0)
point(g("vents", "hot vents"), 1.3)
wow(g("spoon", "two tablespoons"), 1.2)
wow(g("layer", "forty story"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", SC["hook"]["start"] + aw("hook", "salty", 2), 0.45), ("ping.mp3", A("hook", "aren't") + 0.1, 0.35),
        ("pop.mp3", A("guess", "salty fish"), 0.45), ("pop.mp3", A("guess", "salt mines"), 0.45), ("pop.mp3", A("guess", "rocks on"), 0.5),
        ("sparkle.mp3", A("intro", "max wise"), 0.4), ("click-soft.mp3", A("rain", "acidic"), 0.5),
        ("click.mp3", A("rock", "nibbles"), 0.45), ("click-soft.mp3", A("river", "pinch"), 0.5),
        ("impact-bass-1.mp3", A("ocean", "dead end"), 0.4), ("pop.mp3", A("ocean", "stays behind"), 0.5),
        ("riser.mp3", A("vents", "hot vents"), 0.25), ("ping.mp3", A("spoon", "thirty five"), 0.4), ("pop.mp3", A("spoon", "tablespoons"), 0.55),
        ("impact-bass-2.mp3", A("layer", "five hundred"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
