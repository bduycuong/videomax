# MAX WISE ep33 — Why do your ears pop on a plane?
# Kit: ink / morph / along helpers; 2D only (no three.js). Sources: Mayo Clinic "Airplane ear" (middle-ear vs cabin pressure mismatch,
# Eustachian tube to back of nose/throat opens on swallow/yawn, tips incl. gentle Valsalva, babies bottle/pacifier, see a doctor if it lasts),
# Medscape "Eustachian Tube Function" (adult tube ~36 mm, closed at rest, descent can lock it shut), SKYbrary "Cabin Altitude" (<= 8,000 ft).
# Maths: 8,000 ft = 2,438 m -> p/p0 = 0.743 -> about a quarter less air pressure; 36 mm ~ 3.5 cm.
# === SCENES ===
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#FCE3D2"; PINK = "#F7C6CF"; AIR = "#BFE3F7"; DRUM = "#E88A9A"; LIGHT = "#FFF3EC"

D_FLAT = "M490,390 Q490,450 490,510"
D_OUT = "M490,390 Q410,450 490,510"
D_IN = "M490,390 Q570,450 490,510"
TUBE = "M640,560 C680,680 760,760 830,840"

def plane(idn, scale=1.0):
    return (f'<g id="{idn}" opacity="0"><g transform="scale({scale})">'
            f'<path d="M-95,0 Q-90,-24 -40,-24 L70,-22 Q100,-18 104,0 Q100,18 70,20 L-40,22 Q-90,24 -95,0 Z" fill="#FFFFFF" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M-80,-18 L-98,-62 L-66,-62 L-44,-22" fill="{C["hi"]}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M-10,6 L-40,58 L-6,58 L30,8" fill="{C["hi"]}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
            f'<circle cx="20" cy="-6" r="6" fill="{AIR}" stroke="{K}" stroke-width="3"/><circle cx="44" cy="-6" r="6" fill="{AIR}" stroke="{K}" stroke-width="3"/>'
            f'<circle cx="68" cy="-6" r="6" fill="{AIR}" stroke="{K}" stroke-width="3"/></g></g>')

def ear(p, drum=D_FLAT, tube=False, cut=True):
    """cutaway ear: dashed cut, outer ear + canal, eardrum #p-drum, air pocket #p-pkt, bones, cochlea; optional tube + throat"""
    dash = ' stroke-dasharray="18 12"' if cut else ""
    out = (f'<path id="{p}-cut" d="M200,260 Q560,230 960,262 L968,930 L430,930 Q360,760 200,640 Z" fill="{SKIN}" stroke="{K}" stroke-width="6"{dash} stroke-linejoin="round"/>'
           f'<path d="M190,300 Q70,320 72,450 Q76,580 190,610 Q150,520 160,450 Q150,370 190,300 Z" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
           f'<rect x="170" y="400" width="320" height="100" fill="{LIGHT}"/>'
           f'<path d="M170,400 L490,400 M170,500 L490,500" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
           f'<path id="{p}-pkt" d="M490,360 Q600,320 690,380 Q730,450 690,530 Q600,580 490,540 Z" fill="{AIR}" stroke="{C["blue"]}" stroke-width="6" stroke-linejoin="round"/>'
           f'<path d="M500,450 L555,425 L600,455 L645,435" stroke="{C["muted"]}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M800,450 m-40,0 a40,40 0 1,1 80,0 a30,30 0 1,1 -60,0 a18,18 0 1,1 36,0" stroke="{C["muted"]}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    if tube:
        out += (f'<rect x="830" y="600" width="120" height="320" fill="{PINK}" opacity=".7"/>'
                f'<path d="M830,600 L830,920 M950,600 L950,920" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>'
                f'<path id="{p}-tw" d="{TUBE}" stroke="{K}" stroke-width="56" fill="none" stroke-linecap="round" opacity=".9"/>'
                f'<path id="{p}-tin" d="{TUBE}" stroke="{PINK}" stroke-width="44" fill="none" stroke-linecap="round"/>'
                f'<path id="{p}-core" d="{TUBE}" stroke="{AIR}" stroke-width="0" fill="none" stroke-linecap="round"/>'
                f'<path id="{p}-seam" d="{TUBE}" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    out += f'<path id="{p}-drum" d="{drum}" stroke="{DRUM}" stroke-width="14" fill="none" stroke-linecap="round"/>'
    return out

def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.9)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 26px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff">{txt}</span></div>')

# 1 HOOK — a plane climbs along a dashed path; a doodle ear with a "?"; the question rises
s = "hook"; tqq = aw(s, "quick question"); twh = aw(s, "why do"); tpo = aw(s, "pop"); tpl = aw(s, "plane")
scenes[s] = scene_file(s, f"""
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-q {{ top:170px; font-size:96px; line-height:1.1; opacity:0; }}
#hk-qm {{ position:absolute; left:250px; top:470px; {GH} font-size:150px; color:{C['red']}; opacity:0; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="hk-route" d="M440,880 C620,860 760,760 1000,520" fill="none" stroke="none"/>
    <path id="hk-trail" d="M440,880 C620,860 760,760 1000,520" stroke="{C['pencil']}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="6 18"/>
    <g id="hk-ear" opacity="0"><path d="M190,520 Q90,530 92,650 Q96,770 190,800 Q150,720 160,650 Q150,580 190,520 Z" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
      <path d="M150,600 Q120,650 150,700" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/></g>
    {plane("hk-pl", 1.1)}
  </svg>
  <div id="hk-q" class="h1">Why do your ears<br><span class="hl">pop</span> on a plane?</div>
  <div id="hk-qm">?</div>
""", J("""
tl.set("#hk-q", {opacity:1}, @tw); rise("#hk-q", @tw);
tl.fromTo("#hk-ear", {opacity:0, scale:0.5, svgOrigin:"150 660"}, {opacity:1, scale:1, svgOrigin:"150 660", duration:0.4, ease:"back.out(2)"}, 0.1);
tl.set("#hk-pl", {opacity:1}, 0.1);
ink("#hk-trail", 0.1, @dd, {ease:"none"});
along("#hk-pl", "#hk-route", 0.1, @dd, {ease:"sine.inOut", rotate:true});
tl.set("#hk-qm", {opacity:1}, @tp); pop("#hk-qm", @tp, {from:{rotation:-30, scale:1.8}, to:{rotation:8}});
tl.fromTo("#hk-ear", {x:0}, {x:8, duration:0.05, yoyo:true, repeat:5, immediateRender:false}, @tp);
""", tw=twh - 0.1, tp=tpo, dd=tpl + 0.6))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "engines"); t2 = aw(s, "cold"); t3 = aw(s, "air itself")
notes = [("a", "The engines?", -6, 110, "#E6E6E6"), ("b", "The cold?", 4, 405, AIR), ("c", "The air?", -3, 700, C['hi'])]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:80px 14px 0;box-sizing:border-box;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg);
tl.set("#gs-a", {opacity:1}, @t1); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
tl.set("#gs-b", {opacity:1}, @t2); pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}});
tl.set("#gs-c", {opacity:1}, @t3); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3 - 0.2))

# 3 INTRO — logo + underline + a magnifying glass inks itself
s = "intro"; tmw = aw(s, "max wise"); tpk = aw(s, "peek inside")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:395px; font-size:62px; opacity:0; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">A peek inside your ear</span></div>
  <svg class="abs" style="left:0;top:470px" width="{W}" height="150" data-layout-ignore>
    <circle class="in-mg" cx="520" cy="68" r="52" fill="none" stroke="{K}" stroke-width="8"/>
    <path class="in-mg" d="M558,106 L610,140" stroke="{K}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path class="in-mg" d="M495,48 Q505,36 520,34" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
tl.set("#in-sub", {opacity:1}, @ts); rise("#in-sub", @ts);
ink(".in-mg", @ts, 0.5, {stagger:0.12});
""", tmw=tmw, tu=tmw + 0.3, ts=tpk - 0.4))

# 4 POCKET — dashed cutaway ear; eardrum + air pocket get tape labels with leader lines
s = "pocket"; ted = aw(s, "eardrum"); tpa = aw(s, "pocket of"); tme = aw(s, "middle ear")
scenes[s] = scene_file(s, f"""
#pk-svg {{ position:absolute; left:0; top:0; }}
#pk-c {{ position:absolute; left:120px; top:150px; opacity:0; }}
#pk-air {{ position:absolute; left:545px; top:600px; {GH} font-size:56px; color:{C['blue']}; opacity:0; }}
""", f"""
  <svg id="pk-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="pk-ear">{ear("pk")}</g>
    <path id="pk-l1" d="M486,392 L420,330" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path id="pk-l2" d="M620,360 L700,300" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="pk-c"><span class="chip" style="background:#FFFFFF;font-size:42px;transform:rotate(-4deg)">cutaway</span></div>
  {tape("pk-t1", "eardrum", 230, 270, -4, 46, "rgba(232,138,154,.85)")}
  {tape("pk-t2", "middle ear", 640, 245, 3, 50)}
  <div id="pk-air">just air!</div>
""", J("""
tl.fromTo("#pk-ear", {opacity:0}, {opacity:1, duration:0.3}, 0.0);
ink("#pk-cut", 0.0, 0.7);
tl.set("#pk-c", {opacity:1}, 0.3); pop("#pk-c .chip", 0.3);
tl.fromTo("#pk-drum", {scaleY:0.2, svgOrigin:"490 450"}, {scaleY:1, svgOrigin:"490 450", duration:0.35, ease:"back.out(2)"}, @te);
ink("#pk-l1", @te, 0.25); tl.set("#pk-t1", {opacity:1}, @te); pop("#pk-t1 span", @te, {from:{rotation:-14}, to:{rotation:-4}});
tl.fromTo("#pk-pkt", {scale:0.92, svgOrigin:"600 450"}, {scale:1.06, svgOrigin:"600 450", duration:0.3, yoyo:true, repeat:1, immediateRender:false}, @tp);
tl.set("#pk-air", {opacity:1}, @tp2); pop("#pk-air", @tp2, {from:{rotation:-10}, to:{rotation:-3}});
ink("#pk-l2", @tm, 0.25); tl.set("#pk-t2", {opacity:1}, @tm); pop("#pk-t2 span", @tm, {from:{rotation:12}, to:{rotation:3}});
""", te=ted - 0.1, tp=tpa - 0.1, tp2=tpa + 0.3, tm=tme - 0.1))

# 5 CLIMB — altitude ruler 0..8,000 ft, plane marker rises; 12 air dots, 3 fade = a quarter less
s = "climb"; tdr = aw(s, "drops"); tcl = aw(s, "climb"); tmt = aw(s, "mountain"); t8k = aw(s, "eight thousand"); tq = aw(s, "quarter")
RY = lambda ft: 860 - ft * 0.075
ticks = "".join(f'<path d="M900,{RY(f):.0f} L{935 if f % 4000 == 0 else 925},{RY(f):.0f}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for f in range(0, 8001, 1000))
tlab = "".join(f'<text x="885" y="{RY(f) + 14:.0f}" text-anchor="end" style="{GH}font-size:40px" fill="{K}">{f:,}</text>' for f in (0, 4000, 8000))
DOTS = [(150, 330), (300, 280), (470, 340), (180, 480), (350, 450), (520, 520), (680, 430), (240, 640), (430, 650), (600, 700), (760, 620), (330, 800)]
FADE = (1, 6, 9)
dots = "".join(f'<circle id="cb-d{i}" cx="{x}" cy="{y}" r="26" fill="{AIR}" stroke="{C["blue"]}" stroke-width="5"/>' for i, (x, y) in enumerate(DOTS))
scenes[s] = scene_file(s, f"""
#cb-svg {{ position:absolute; left:0; top:0; }}
#cb-c {{ position:absolute; left:110px; top:150px; opacity:0; }}
#cb-8 {{ position:absolute; left:640px; top:160px; opacity:0; }}
#cb-q {{ position:absolute; left:430px; top:860px; opacity:0; }}
#cb-rul, #cb-mt, #cb-dots {{ opacity:0; }}
""", f"""
  <svg id="cb-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="cb-mt" d="M120,860 L380,520 L460,600 L640,{RY(8000):.0f} L860,860 Z" fill="#E4EED8" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
    <path id="cb-sn" d="M590,330 L640,{RY(8000):.0f} L690,330 L660,320 L640,340 L615,318 Z" fill="#FFFFFF" stroke="{K}" stroke-width="4" stroke-linejoin="round" opacity="0"/>
    <path id="cb-dl" d="M640,{RY(8000):.0f} L790,{RY(8000):.0f}" stroke="{C['red']}" stroke-width="4" stroke-dasharray="10 10" fill="none"/>
    <g id="cb-rul"><path d="M900,{RY(0):.0f} L900,{RY(8000) - 20:.0f}" stroke="{K}" stroke-width="7" stroke-linecap="round"/>{ticks}{tlab}
      <text x="1000" y="{RY(0) + 60:.0f}" text-anchor="end" style="{GH}font-size:38px" fill="{C['muted']}">feet</text></g>
    <g id="cb-dots">{dots}</g>
    <g id="cb-mk" opacity="0"><path d="M945,{RY(0):.0f} L985,{RY(0) - 22:.0f} L985,{RY(0) + 22:.0f} Z" fill="{C['red']}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/></g>
  </svg>
  <div id="cb-c"><span class="chip" style="background:#FFFFFF;font-size:50px;transform:rotate(-3deg)">higher = less air</span></div>
  <div id="cb-8"><span class="chip" style="background:{C['hi']};font-size:56px">8,000 ft</span></div>
  <div id="cb-q"><span class="chip" style="background:#FFC9C2;font-size:52px">about 1/4 less air</span></div>
""", J("""
tl.fromTo("#cb-dots", {opacity:0}, {opacity:1, duration:0.3}, 0.05);
tl.fromTo("#cb-rul", {opacity:0, x:40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, 0.2);
tl.set("#cb-mk", {opacity:1}, 0.4);
tl.set("#cb-c", {opacity:1}, @td); pop("#cb-c .chip", @td, {from:{rotation:-10}, to:{rotation:-3}});
tl.to("#cb-mk", {y:@dy, duration:@dur, ease:"power1.inOut"}, @tc);
tl.fromTo("#cb-mt", {opacity:0, y:40}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, @tm);
tl.fromTo("#cb-sn", {opacity:0}, {opacity:1, duration:0.3}, @tm2);
ink("#cb-dl", @t8, 0.4);
tl.set("#cb-8", {opacity:1}, @t8); pop("#cb-8 .chip", @t8, {from:{rotation:-10, scale:1.4}, to:{rotation:-2}});
""", td=tdr - 0.1, tc=tcl - 0.1, dur=t8k - tcl + 0.2, dy=RY(8000) - RY(0), tm=tmt - 0.3, tm2=tmt + 0.1, t8=t8k)
  + "".join(f'tl.to("#cb-d{i}", {{opacity:0, scale:0.2, svgOrigin:"{DOTS[i][0]} {DOTS[i][1]}", duration:0.3, ease:"power2.in"}}, {tq - 0.2 + k * 0.12:.3f});\n' for k, i in enumerate(FADE))
  + J("""tl.set("#cb-q", {opacity:1}, @tq); pop("#cb-q .chip", @tq, {from:{rotation:8}, to:{rotation:2}});""", tq=tq + 0.2))

# 6 BULGE — same ear; the eardrum morphs outward, push arrows, a balloon inflates
s = "bulge"; tpu = aw(s, "pushes outward"); tbu = aw(s, "bulges"); tba = aw(s, "balloon"); tst = aw(s, "stuffy")
arr = "".join(f'<path class="bg-ar" d="M650,{y} L540,{y} M560,{y - 16} L540,{y} L560,{y + 16}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' for y in (420, 455, 490))
scenes[s] = scene_file(s, f"""
#bg-svg {{ position:absolute; left:0; top:0; }}
#bg-o {{ position:absolute; left:110px; top:160px; opacity:0; }}
#bg-i {{ position:absolute; left:590px; top:160px; opacity:0; }}
#bg-s {{ position:absolute; left:470px; top:830px; opacity:0; }}
""", f"""
  <svg id="bg-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {ear("bg")}
    {arr}
    <g id="bg-bal" opacity="0">
      <path d="M850,740 Q852,790 830,830 Q812,860 838,900" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
      <g id="bg-bb"><ellipse cx="850" cy="660" rx="70" ry="82" fill="{C['red']}" stroke="{K}" stroke-width="6"/>
        <path d="M838,742 L862,742 L850,728 Z" fill="{C['red']}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>
        <path d="M815,620 Q825,600 845,594" stroke="#FFFFFF" stroke-width="7" fill="none" stroke-linecap="round"/></g>
    </g>
  </svg>
  <div id="bg-o"><span class="chip" style="background:#FFFFFF;font-size:44px;transform:rotate(-3deg)">less air out here</span></div>
  <div id="bg-i"><span class="chip" style="background:{AIR};font-size:44px;transform:rotate(2deg)">more air in here</span></div>
  <div id="bg-s"><span class="chip" style="background:{C['hi']};font-size:52px">full and stuffy</span></div>
""", J("""
tl.set("#bg-o", {opacity:1}, 0.2); pop("#bg-o .chip", 0.2);
tl.set("#bg-i", {opacity:1}, @tp); pop("#bg-i .chip", @tp, {from:{rotation:10}, to:{rotation:2}});
ink(".bg-ar", @tp, 0.35, {stagger:0.1});
tl.fromTo(".bg-ar", {x:0}, {x:-14, duration:0.3, yoyo:true, repeat:5, ease:"sine.inOut", immediateRender:false}, @tp2);
morph("#bg-drum", "@out", @tb, 0.6, {ease:"back.out(1.6)"});
tl.set("#bg-bal", {opacity:1}, @tba);
tl.fromTo("#bg-bb", {scale:0.3, svgOrigin:"850 742"}, {scale:1, svgOrigin:"850 742", duration:0.7, ease:"back.out(1.8)"}, @tba);
tl.set("#bg-s", {opacity:1}, @ts); pop("#bg-s .chip", @ts, {from:{rotation:-10}, to:{rotation:-2}});
""", tp=tpu - 0.1, tp2=tpu + 0.4, tb=tbu - 0.2, tba=tba - 0.3, ts=tst - 0.2, out=D_OUT))

# 7 TUBE — the escape hatch inks down to the throat; length ticks + 3.5 cm label; tape labels
s = "tube"; tes = aw(s, "escape hatch"); tsk = aw(s, "skinny tube"); t35 = aw(s, "three and"); tth = aw(s, "throat")
scenes[s] = scene_file(s, f"""
#tb-svg {{ position:absolute; left:0; top:0; }}
#tb-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#tb-cm {{ position:absolute; left:450px; top:770px; opacity:0; }}
#tb-thr, #tb-tk, #tb-tw, #tb-tin, #tb-seam {{ opacity:0; }}
""", f"""
  <svg id="tb-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {ear("tb", D_OUT, tube=True)}
    <path id="tb-ld" d="M650,640 L560,650" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <g id="tb-tk"><path d="M612,575 L668,545 M802,855 L858,825" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/></g>
  </svg>
  <div id="tb-c"><span class="chip" style="background:#FFFFFF;font-size:56px;transform:rotate(-2deg)">the escape hatch</span></div>
  {tape("tb-t1", "Eustachian tube", 170, 625, -3, 46)}
  <div id="tb-cm"><span class="chip" style="background:#FFC9C2;font-size:50px">about 3.5 cm</span></div>
  {tape("tb-thr", "throat", 820, 545, 4, 44, "rgba(247,198,207,.95)")}
""", J("""
tl.set("#tb-c", {opacity:1}, @te); pop("#tb-c .chip", @te, {from:{rotation:-10}, to:{rotation:-2}});
tl.set("#tb-tw, #tb-tin, #tb-seam", {opacity:1}, @tk);
ink("#tb-tw", @tk, 0.9); ink("#tb-tin", @tk, 0.9); ink("#tb-seam", @tk, 0.9);
ink("#tb-ld", @tk2, 0.25); tl.set("#tb-t1", {opacity:1}, @tk2); pop("#tb-t1 span", @tk2, {from:{rotation:-12}, to:{rotation:-3}});
tl.fromTo("#tb-tk", {opacity:0}, {opacity:1, duration:0.2}, @t3);
tl.set("#tb-cm", {opacity:1}, @t3); pop("#tb-cm .chip", @t3, {from:{rotation:10, scale:1.4}, to:{rotation:2}});
tl.set("#tb-thr", {opacity:1}, @tt); pop("#tb-thr span", @tt, {from:{rotation:14}, to:{rotation:4}});
""", te=tes - 0.1, tk=tsk - 0.2, tk2=tsk + 0.6, t3=t35 - 0.1, tt=tth - 0.2))

# 8 POP — tube shut; swallow/yawn opens it, air dots ride down the tube, eardrum morphs back flat: POP!
s = "pop"; tsh = aw(s, "stays shut"); tsw = aw(s, "swallow"); top_ = aw(s, "opens"); tru = aw(s, "rushes"); tev = aw(s, "evens out"); tpp = aw(s, "and pop") + 0.15
NDOT = 9
dots = "".join(f'<circle id="pp-d{i}" cx="0" cy="0" r="12" fill="#FFFFFF" stroke="{C["blue"]}" stroke-width="4" opacity="0"/>' for i in range(NDOT))
burst = "".join(f'<path class="pp-b" d="M{x1},{y1} L{x2},{y2}" stroke="{C["red"]}" stroke-width="8" stroke-linecap="round" fill="none"/>' for x1, y1, x2, y2 in ((100, 240, 60, 205), (90, 330, 45, 340), (470, 230, 510, 195), (480, 330, 525, 345)))
scenes[s] = scene_file(s, f"""
#pp-svg {{ position:absolute; left:0; top:0; }}
#pp-c1 {{ position:absolute; left:570px; top:160px; opacity:0; }}
#pp-c2 {{ position:absolute; left:570px; top:160px; opacity:0; }}
#pp-pop {{ position:absolute; left:110px; top:150px; {GH} font-size:200px; line-height:1; color:{C['red']}; opacity:0; }}
#pp-eq {{ position:absolute; left:130px; top:700px; opacity:0; }}
""", f"""
  <svg id="pp-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="pp-ear">{ear("pp", D_OUT, tube=True)}</g>
    <path id="pp-rt" d="{TUBE}" fill="none" stroke="none"/>
    {dots}{burst}
  </svg>
  <div id="pp-c1"><span class="chip" style="background:#FFFFFF;font-size:50px">usually shut</span></div>
  <div id="pp-c2"><span class="chip" style="background:{C['hi']};font-size:50px">swallow or yawn</span></div>
  <div id="pp-pop">POP!</div>
  <div id="pp-eq"><span class="chip" style="background:{AIR};font-size:48px;transform:rotate(-3deg)">pressure evens out</span></div>
""", J("""
tl.set("#pp-c1", {opacity:1}, @ts); pop("#pp-c1 .chip", @ts, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#pp-seam", {attr:{"stroke-width":4}}, {attr:{"stroke-width":9}, duration:0.2, yoyo:true, repeat:1, immediateRender:false}, @ts);
tl.to("#pp-c1", {opacity:0, y:-20, duration:0.2}, @tw0);
tl.set("#pp-c2", {opacity:1}, @tw); pop("#pp-c2 .chip", @tw, {from:{rotation:10}, to:{rotation:2}});
tl.to("#pp-seam", {opacity:0, duration:0.2}, @to);
tl.fromTo("#pp-core", {attr:{"stroke-width":0}}, {attr:{"stroke-width":26}, duration:0.35, ease:"back.out(2)"}, @to);
morph("#pp-drum", "@flat", @te, 0.4, {ease:"back.out(2)"});
tl.set("#pp-eq", {opacity:1}, @te); pop("#pp-eq .chip", @te, {from:{rotation:-10}, to:{rotation:-3}});
tl.set("#pp-pop", {opacity:1}, @tp); pop("#pp-pop", @tp, {from:{scale:2.2, rotation:-16}, to:{rotation:-6, duration:0.3}});
ink(".pp-b", @tp, 0.2, {stagger:0.03});
tl.fromTo("#pp-ear", {x:0}, {x:9, duration:0.05, yoyo:true, repeat:3, immediateRender:false}, @tp);
""", ts=tsh - 0.1, tw0=tsw - 0.4, tw=tsw - 0.15, to=top_ - 0.1, te=tev - 0.2, tp=tpp - 0.05, flat=D_FLAT)
  + "".join(f'tl.set("#pp-d{i}", {{opacity:1}}, {tru - 0.2 + i * 0.12:.3f}); along("#pp-d{i}", "#pp-rt", {tru - 0.2 + i * 0.12:.3f}, 0.7, {{ease:"power1.in"}}); tl.to("#pp-d{i}", {{opacity:0, duration:0.15}}, {tru + 0.45 + i * 0.12:.3f});\n' for i in range(NDOT)))

# 9 DOWN — plane glides down; outside air pushes the eardrum in; a red clamp squeezes the tube shut
s = "down"; tla = aw(s, "landing"); two = aw(s, "worse"); tpu = aw(s, "pushes"); tsq = aw(s, "squeezes")
arr = "".join(f'<path class="dn-ar" d="M250,{y} L380,{y} M360,{y - 16} L380,{y} L360,{y + 16}" stroke="{C["red"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' for y in (420, 455, 490))
scenes[s] = scene_file(s, f"""
#dn-svg {{ position:absolute; left:0; top:0; }}
#dn-c {{ position:absolute; left:110px; top:160px; opacity:0; }}
#dn-st {{ position:absolute; left:110px; top:700px; opacity:0; }}
#dn-st span {{ display:inline-block; {GH} font-size:52px; color:{C['red']}; border:5px solid {C['red']}; padding:0 18px; border-radius:10px; transform:rotate(-6deg); background:#FFFFFF; }}
#dn-cl {{ opacity:0; }}
""", f"""
  <svg id="dn-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g opacity=".95">{ear("dn", D_FLAT, tube=True, cut=False)}</g>
    {arr}
    <path id="dn-route" d="M640,150 C760,160 880,220 1010,320" fill="none" stroke="none"/>
    <path id="dn-trail" d="M640,150 C760,160 880,220 1010,320" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-dasharray="6 16" stroke-linecap="round"/>
    {plane("dn-pl", 0.7)}
    <g id="dn-cl"><path d="M680,700 L740,660" stroke="{C['red']}" stroke-width="14" stroke-linecap="round"/>
      <path d="M760,760 L820,720" stroke="{C['red']}" stroke-width="14" stroke-linecap="round"/></g>
  </svg>
  <div id="dn-c"><span class="chip" style="background:{C['hi']};font-size:50px;transform:rotate(-3deg)">landing: often worse</span></div>
  <div id="dn-st"><span>tube squeezed shut</span></div>
""", J("""
tl.set("#dn-pl", {opacity:1}, 0.05);
ink("#dn-trail", 0.05, @dd, {ease:"none"}); along("#dn-pl", "#dn-route", 0.05, @dd, {ease:"sine.inOut", rotate:true});
tl.set("#dn-c", {opacity:1}, @tw); pop("#dn-c .chip", @tw, {from:{rotation:-12}, to:{rotation:-3}});
ink(".dn-ar", @tp, 0.35, {stagger:0.1});
morph("#dn-drum", "@din", @tp2, 0.5, {ease:"back.out(1.6)"});
tl.fromTo("#dn-cl", {opacity:0, scale:1.6, svgOrigin:"750 710"}, {opacity:1, scale:1, svgOrigin:"750 710", duration:0.3, ease:"back.out(2)"}, @tq);
tl.to("#dn-seam", {attr:{"stroke-width":10}, duration:0.2}, @tq);
tl.set("#dn-st", {opacity:1}, @tq2); pop("#dn-st span", @tq2, {from:{rotation:-24, scale:1.7}, to:{rotation:-6}});
""", dd=two + 0.4, tw=tla - 0.1, tp=tpu - 0.2, tp2=tpu, tq=tsq - 0.1, tq2=tsq + 0.3, din=D_IN))

# 10 TIPS — a tip card with ticks; red card: pain sticks around -> see a doctor
s = "tips"; tgu = aw(s, "chew gum"); tpi = aw(s, "pinch"); tbb = aw(s, "feed babies"); tpa = aw(s, "if the"); tdc = aw(s, "doctor")
rows = [("r1", "chew gum, swallow, yawn", 300), ("r2", "pinch nose, blow gently", 420), ("r3", "feed babies on landing", 540)]
rh = "".join(f'<div id="tp-{k}" class="abs" style="left:150px;top:{y}px;opacity:0;font-family:\'Patrick Hand\',cursive;font-size:64px;line-height:1">'
             f'<span style="display:inline-block;width:62px;height:62px;border:5px solid {K};border-radius:8px;vertical-align:middle;margin-right:26px;background:#FFFFFF"></span>{txt}</div>' for k, txt, y in rows)
ticks = "".join(f'<path id="tp-k{i}" d="M168,{y + 30} L188,{y + 52} L232,{y - 4}" stroke="{C["red"]}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' for i, (_, _, y) in enumerate(rows))
scenes[s] = scene_file(s, f"""
#tp-svg {{ position:absolute; left:0; top:0; }}
#tp-card {{ position:absolute; left:100px; top:250px; width:880px; height:410px; background:#FFFFFF; border:5px solid {K}; {SKETCH} transform:rotate(-1deg); opacity:0; }}
#tp-h {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#tp-doc {{ position:absolute; left:420px; top:720px; width:600px; padding:14px 20px; text-align:center; background:#FFFFFF; border:5px solid {C['red']}; {SKETCH} {GH} font-size:54px; line-height:1.1; opacity:0; }}
""", f"""
  <div id="tp-h"><span class="chip" style="background:{C['hi']};font-size:58px;transform:rotate(-2deg)">tip card</span></div>
  <div id="tp-card"></div>
  {rh}
  <svg id="tp-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>{ticks}</svg>
  <div id="tp-doc">pain sticks around?<br><span class="red">see a doctor</span></div>
""", J("""
tl.set("#tp-h", {opacity:1}, 0.1); pop("#tp-h .chip", 0.1);
tl.fromTo("#tp-card", {opacity:0, y:40}, {opacity:1, y:0, duration:0.35, ease:"back.out(1.6)"}, 0.2);
tl.set("#tp-r1", {opacity:1}, @t1); rise("#tp-r1", @t1); ink("#tp-k0", @t1b, 0.3);
tl.set("#tp-r2", {opacity:1}, @t2); rise("#tp-r2", @t2); ink("#tp-k1", @t2b, 0.3);
tl.set("#tp-r3", {opacity:1}, @t3); rise("#tp-r3", @t3); ink("#tp-k2", @t3b, 0.3);
tl.set("#tp-doc", {opacity:1}, @td); pop("#tp-doc", @td, {from:{rotation:6}, to:{rotation:-1}});
tl.fromTo("#tp-doc", {scale:1}, {scale:1.06, duration:0.14, yoyo:true, repeat:1, immediateRender:false}, @tdd);
""", t1=tgu - 0.3, t1b=tgu + 0.8, t2=tpi - 0.2, t2b=tpi + 0.9, t3=tbb - 0.2, t3b=tbb + 0.7, td=tpa - 0.1, tdd=tdc))

# 11 OUTRO — callback: a tiny doodle door swings open, pop! (Max centre stage, keep y < 620)
s = "outro"; ttd = aw(s, "tiny door"); tba = aw(s, "balancing"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-r {{ position:absolute; left:0; right:0; top:480px; text-align:center; opacity:0; }}
#ou-p {{ position:absolute; left:640px; top:200px; {GH} font-size:110px; color:{C['red']}; opacity:0; }}
#ou-sc {{ top:470px; font-size:110px; opacity:0; }}
#ou-fr {{ opacity:0; }}
""", f"""
  <svg id="ou-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="ou-fr"><rect x="430" y="170" width="190" height="280" rx="8" fill="{AIR}" stroke="{K}" stroke-width="7"/>
      <circle cx="490" cy="270" r="9" fill="#FFFFFF"/><circle cx="560" cy="330" r="13" fill="#FFFFFF"/><circle cx="510" cy="380" r="7" fill="#FFFFFF"/></g>
    <g id="ou-door"><rect x="430" y="170" width="190" height="280" rx="8" fill="{C['hi']}" stroke="{K}" stroke-width="7"/>
      <circle cx="595" cy="315" r="10" fill="{K}"/></g>
  </svg>
  <div id="ou-p">pop!</div>
  <div id="ou-r"><span class="chip" style="background:#FFFFFF;font-size:52px">a tiny door that balances the air</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
tl.fromTo("#ou-fr", {opacity:0}, {opacity:1, duration:0.2}, 0.1);
tl.fromTo("#ou-door", {opacity:0, scale:0.6, svgOrigin:"525 310"}, {opacity:1, scale:1, svgOrigin:"525 310", duration:0.35, ease:"back.out(2)"}, 0.1);
tl.to("#ou-door", {scaleX:0.25, skewY:-8, svgOrigin:"430 310", duration:0.45, ease:"back.out(1.5)"}, @tt);
tl.set("#ou-p", {opacity:1}, @tt2); pop("#ou-p", @tt2, {from:{scale:2, rotation:-16}, to:{rotation:-6}});
tl.set("#ou-r", {opacity:1}, @tb); pop("#ou-r .chip", @tb, {from:{rotation:-6}, to:{rotation:-1}});
tl.to("#ou-r", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
tl.set("#ou-sc", {opacity:1}, @tsc); pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", tt=ttd - 0.1, tt2=ttd + 0.25, tb=ttd + 0.1, tx=tsc - 0.3, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "why do"), SC["guess"]["start"] + 0.2)
point(g("guess", "engines"), 2.4)
wave(g("intro", "I'm Max"))
point(g("pocket", "middle ear"), 1.2)
point(g("climb", "eight thousand"), 1.3)
wow(g("bulge", "balloon"), 1.0)
point(g("tube", "three and"), 1.3)
wow(g("pop", "and pop"), 1.0)
point(g("down", "squeezes"), 1.2)
point(g("tips", "doctor"), 1.3)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "quick question"), 0.3), ("pop.mp3", A("hook", "pop"), 0.5),
        ("pop.mp3", A("guess", "engines"), 0.45), ("pop.mp3", A("guess", "cold"), 0.45), ("pop.mp3", A("guess", "air itself"), 0.5),
        ("sparkle.mp3", A("intro", "max wise"), 0.4), ("click-soft.mp3", A("pocket", "eardrum"), 0.5),
        ("ping.mp3", A("climb", "eight thousand"), 0.4), ("riser.mp3", A("bulge", "pushes outward"), 0.25),
        ("click.mp3", A("tube", "three and"), 0.45), ("whoosh-short.mp3", A("pop", "rushes"), 0.3), ("pop.mp3", A("pop", "and pop"), 0.7),
        ("impact-bass-1.mp3", A("down", "squeezes"), 0.4), ("click-soft.mp3", A("tips", "chew gum"), 0.5),
        ("impact-bass-2.mp3", A("tips", "doctor"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
