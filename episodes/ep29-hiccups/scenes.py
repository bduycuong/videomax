# MAX WISE ep29 — Why do we hiccup?
# Kit: ink / morph / along helpers; 2D only (no three.js). Sources: Mayo Clinic (hiccups: diaphragm spasm, vocal cords close -> "hic", triggers, >48 h see a doctor),
# UCL news Nov 2019 / EurekAlert release (fetal hiccups from ~9 weeks, preterm ~1% of time ~15 min/day, 3 brainwaves per hiccup), Straus et al. 2003 BioEssays (gill hypothesis, one idea only).
# Maths: 1% of 1440 min = 14.4 min ~ 15 min/day; 48 h = 2 days.
# === SCENES ===
import random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#FCE3D2"; PINK = "#F7C6CF"; AIR = "#BFE3F7"; AIRD = "#7FC3EA"; DIA = C['red']; CORD = "#E88A9A"

def mirror(d):
    """mirror an absolute M/Q/L path around x=540"""
    import re
    return re.sub(r"(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)", lambda m: f"{1080 - float(m.group(1)):.0f},{m.group(2)}", d)

LUNG_L = "M520,300 Q420,290 360,360 Q310,450 330,560 Q380,590 440,575 Q510,560 520,500 Z"
DOME = "M270,700 C380,560 700,560 810,700"
FLAT = "M270,700 C380,690 700,690 810,700"
def chest(p, dashed=True):
    """cutaway torso: dashed cut outline, windpipe, lungs group #p-lungs, diaphragm #p-dia (dome)"""
    dash = ' stroke-dasharray="18 12"' if dashed else ""
    return (f'<path id="{p}-torso" d="M330,190 Q300,260 260,330 Q230,560 262,820 L818,820 Q850,560 820,330 Q780,260 750,190" fill="{SKIN}" stroke="{K}" stroke-width="6"{dash} stroke-linecap="round"/>'
            f'<path class="{p}-tr" d="M522,130 L522,300" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path class="{p}-tr" d="M558,130 L558,300" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<g id="{p}-lungs"><path d="{LUNG_L}" fill="{PINK}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="{mirror(LUNG_L)}" fill="{PINK}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M420,400 Q440,450 420,500 M660,400 Q640,450 660,500" stroke="#E79AA8" stroke-width="5" fill="none" stroke-linecap="round"/></g>'
            f'<path id="{p}-dia" d="{DOME}" stroke="{DIA}" stroke-width="16" fill="none" stroke-linecap="round"/>')

def airdot(idn):
    return f'<circle id="{idn}" cx="0" cy="0" r="11" fill="{AIR}" stroke="{C["blue"]}" stroke-width="4" opacity="0"/>'

# 1 HOOK — a giant HIC! bursts in, a doodle face jolts; the question rises
s = "hook"; th = aw(s, "hic"); tso = aw(s, "sound"); twh = aw(s, "so why"); thc = aw(s, "hiccup")
burst = "".join(f'<path class="hk-b" d="M{540 + 260*dx:.0f},{250 + 120*dy:.0f} L{540 + 330*dx:.0f},{250 + 150*dy:.0f}" stroke="{C["red"]}" stroke-width="8" stroke-linecap="round" fill="none"/>'
                for dx, dy in ((-1, -0.6), (-1.05, 0.2), (-0.9, 0.9), (1, -0.6), (1.05, 0.2), (0.9, 0.9)))
scenes[s] = scene_file(s, f"""
#hk-hic {{ position:absolute; left:0; right:0; top:150px; text-align:center; {GH} font-size:210px; line-height:1; color:{C['red']}; opacity:0; }}
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-q {{ top:440px; font-size:92px; opacity:0; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {burst}
    <g id="hk-face">
      <circle cx="540" cy="760" r="120" fill="{SKIN}" stroke="{K}" stroke-width="7"/>
      <path d="M485,740 Q500,728 515,740 M565,740 Q580,728 595,740" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
      <ellipse cx="540" cy="800" rx="22" ry="16" fill="{K}"/>
      <path d="M470,660 L455,640 M610,660 L625,640" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
    </g>
  </svg>
  <div id="hk-hic">HIC!</div>
  <div id="hk-q" class="h1">Why do we <span class="hl">hiccup?</span></div>
""", J("""
tl.set("#hk-hic", {opacity:1}, @th); pop("#hk-hic", @th, {from:{scale:2.2, rotation:-14}, to:{rotation:-5, duration:0.35}});
ink(".hk-b", @th2, 0.25, {stagger:0.03});
pop("#hk-face", 0.05, {from:{transformOrigin:"50% 50%"}});
tl.fromTo("#hk-face", {y:0}, {y:-46, duration:0.09, yoyo:true, repeat:1, ease:"power2.out"}, @th);
tl.fromTo("#hk-face", {y:0}, {y:-46, duration:0.09, yoyo:true, repeat:1, ease:"power2.out", immediateRender:false}, @thc);
tl.fromTo("#hk-hic", {rotation:-5}, {rotation:3, duration:0.06, yoyo:true, repeat:3, immediateRender:false}, @thc);
tl.set("#hk-q", {opacity:1}, @tw); rise("#hk-q", @tw);
""", th=th, th2=th + 0.1, thc=thc + 0.15, tw=twh - 0.1))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "swallowed air"); t2 = aw(s, "twitchy muscle"); t3 = aw(s, "your baby")
notes = [("a", "Swallowed air?", -6, 110, AIR), ("b", "A twitchy muscle?", 4, 405, C['hi']), ("c", "Baby days?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:54px;line-height:1.05;padding:70px 14px 0;box-sizing:border-box">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3 - 0.2))

# 3 INTRO — logo + a stopwatch inks itself (slow motion)
s = "intro"; tmw = aw(s, "max wise"); tsl = aw(s, "slow one")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:395px; font-size:62px; opacity:0; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Hiccup in slow motion</span></div>
  <svg class="abs" style="left:0;top:470px" width="{W}" height="150" data-layout-ignore>
    <circle class="in-sw" cx="540" cy="82" r="58" fill="none" stroke="{K}" stroke-width="7"/>
    <path class="in-sw" d="M528,14 L552,14" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="in-sw" d="M540,14 L540,24" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <g id="in-hand"><path d="M540,82 L540,40" stroke="{C['red']}" stroke-width="6" stroke-linecap="round"/></g>
  </svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
tl.set("#in-sub", {opacity:1}, @ts); rise("#in-sub", @ts);
ink(".in-sw", @ts, 0.5, {stagger:0.1});
tl.fromTo("#in-hand", {rotation:0, svgOrigin:"540 82"}, {rotation:90, svgOrigin:"540 82", duration:1.2, ease:"power1.out"}, @ts2);
""", tmw=tmw, tu=tmw + 0.3, ts=tsl - 0.3, ts2=tsl + 0.2))

# 4 MUSCLE — cutaway torso; diaphragm inks as a dome, morphs flat as the lungs fill, back to a dome
s = "muscle"; tlu = aw(s, "lungs"); tdo = aw(s, "dome"); tdi = aw(s, "diaphragm"); tfl = aw(s, "flattens"); tpa = aw(s, "pulls air")
arrows = "".join(f'<path class="mu-ar" d="M{540 + dx},70 L{540 + dx},{150 + dy}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round"/>' for dx, dy in ((-70, 0), (0, 40), (70, 0)))
scenes[s] = scene_file(s, f"""
#mu-svg {{ position:absolute; left:0; top:0; }}
#mu-cl {{ position:absolute; left:770px; top:250px; opacity:0; }}
#mu-cd {{ position:absolute; left:560px; top:770px; opacity:0; }}
#mu-cut {{ position:absolute; left:70px; top:160px; opacity:0; }}
#mu-lungs {{ opacity:0; }}
""", f"""
  <svg id="mu-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {chest("mu")}
    {arrows}
    <path id="mu-ll" d="M700,400 L790,300" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path id="mu-ld" d="M690,640 L720,775" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="mu-cut"><span class="chip" style="background:#FFFFFF;font-size:42px;transform:rotate(-4deg)">cutaway</span></div>
  <div id="mu-cl"><span class="chip" style="background:{PINK};font-size:46px">lungs</span></div>
  <div id="mu-cd"><span class="chip" style="background:{C['hi']};font-size:54px">diaphragm</span></div>
""", J("""
ink("#mu-torso", 0.05, 0.7); ink(".mu-tr", 0.3, 0.4);
tl.set("#mu-cut", {opacity:1}, 0.3); pop("#mu-cut .chip", 0.3);
tl.fromTo("#mu-lungs", {opacity:0, scale:0.6, svgOrigin:"540 440"}, {opacity:1, scale:1, svgOrigin:"540 440", duration:0.4, ease:"back.out(2)"}, @tl);
ink("#mu-ll", @tl2, 0.25); tl.set("#mu-cl", {opacity:1}, @tl2); pop("#mu-cl .chip", @tl2);
ink("#mu-dia", @td, 0.7);
ink("#mu-ld", @tdi, 0.25); tl.set("#mu-cd", {opacity:1}, @tdi); pop("#mu-cd .chip", @tdi, {from:{rotation:-10}, to:{rotation:-3}});
morph("#mu-dia", "@flat", @tf, 0.7, {ease:"power2.inOut"});
tl.to("#mu-lungs", {scaleY:1.1, scaleX:1.04, svgOrigin:"540 300", duration:0.7, ease:"power2.inOut"}, @tf);
ink(".mu-ar", @tp, 0.45, {stagger:0.08});
morph("#mu-dia", "@dome", @tb, 0.6, {ease:"power2.inOut"});
tl.to("#mu-lungs", {scaleY:1, scaleX:1, svgOrigin:"540 300", duration:0.6, ease:"power2.inOut"}, @tb);
""", tl=tlu - 0.1, tl2=tlu + 0.3, td=tdo - 0.1, tdi=tdi, tf=tfl - 0.2, tp=tpa - 0.2, tb=tpa + 0.9, flat=FLAT, dome=DOME))

# 5 SPASM — the diaphragm snaps flat on its own; seeded air dots race down both airways
s = "spasm"; thc = aw(s, "hiccup"); tje = aw(s, "jerks"); tow = aw(s, "on its"); tai = aw(s, "air rushes")
rnd = random.Random(29)
NDOT = 14
dots = "".join(airdot(f"sp-d{i}") for i in range(NDOT))
starts = sorted(rnd.uniform(0, 0.75) for _ in range(NDOT))
jolts = "".join(f'<path class="sp-j" d="M{x},620 L{x + 26*sg},640 L{x},662 L{x + 26*sg},684 L{x},706" stroke="{C["red"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0"/>' for x, sg in ((215, 1), (865, -1)))
scenes[s] = scene_file(s, f"""
#sp-svg {{ position:absolute; left:0; top:0; }}
#sp-c {{ position:absolute; left:60px; top:160px; opacity:0; }}
#sp-own {{ position:absolute; left:600px; top:850px; opacity:0; }}
""", f"""
  <svg id="sp-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="sp-all">{chest("sp", dashed=True)}{jolts}</g>
    <path id="sp-rl" d="M540,90 L540,300 Q470,330 430,450" fill="none" stroke="none"/>
    <path id="sp-rr" d="M540,90 L540,300 Q610,330 650,450" fill="none" stroke="none"/>
    {dots}
  </svg>
  <div id="sp-c"><span class="chip" style="background:#FFC9C2;font-size:58px;transform:rotate(-4deg)">SPASM!</span></div>
  <div id="sp-own"><span class="chip" style="background:#FFFFFF;font-size:46px">all on its own</span></div>
""", J("""
tl.fromTo("#sp-all", {opacity:0}, {opacity:1, duration:0.25}, 0.0);
tl.set("#sp-c", {opacity:1}, @th); pop("#sp-c .chip", @th, {from:{rotation:-16, scale:1.4}, to:{rotation:-4}});
morph("#sp-dia", "@flat", @tj, 0.08, {ease:"power4.out"});
tl.to("#sp-lungs", {scaleY:1.12, scaleX:1.05, svgOrigin:"540 300", duration:0.1, ease:"power4.out"}, @tj);
tl.to(".sp-j", {opacity:1, duration:0.05}, @tj); tl.to(".sp-j", {opacity:0, duration:0.2}, @tj2);
tl.fromTo("#sp-all", {x:0}, {x:10, duration:0.05, yoyo:true, repeat:5, immediateRender:false}, @tj);
tl.set("#sp-own", {opacity:1}, @to); pop("#sp-own .chip", @to, {from:{rotation:8}, to:{rotation:2}});
""", th=thc - 0.1, tj=tje, tj2=tje + 0.6, to=tow - 0.1, flat=FLAT) + "".join(
    f'tl.set("#sp-d{i}", {{opacity:1}}, {tai - 0.1 + st:.3f}); along("#sp-d{i}", "#sp-r{"l" if i % 2 else "r"}", {tai - 0.1 + st:.3f}, 0.45, {{ease:"power2.in"}}); tl.to("#sp-d{i}", {{opacity:0, duration:0.15}}, {tai + 0.35 + st:.3f});\n'
    for i, st in enumerate(starts)))

# 6 SNAP — side view of the windpipe; the vocal cords morph shut, air piles up on top: HIC!
s = "snap"; tsp = aw(s, "split second"); tla = aw(s, "later"); tvc = aw(s, "vocal cords"); tsh = aw(s, "slam shut"); thi = aw(s, "hic")
OPEN_L = "M470,400 Q492,432 500,480"; SHUT_L = "M470,420 Q505,416 540,422"
OPEN_R = "M610,400 Q588,432 580,480"; SHUT_R = "M610,420 Q575,416 540,422"
early = "".join(airdot(f"sn-e{i}") + f'<path id="sn-pe{i}" d="M{540 + (i % 3 - 1) * 18},120 L{540 + (i % 3 - 1) * 18},860" fill="none" stroke="none"/>' for i in range(6))
late = "".join(airdot(f"sn-l{i}") + f'<path id="sn-pl{i}" d="M{540 + (i % 3 - 1) * 26},120 L{540 + (i % 3 - 1) * 26},{392 - (i // 3) * 26}" fill="none" stroke="none"/>' for i in range(6))
hburst = "".join(f'<path class="sn-b" d="M{x1},{y1} L{x2},{y2}" stroke="{C["red"]}" stroke-width="8" stroke-linecap="round" fill="none"/>' for x1, y1, x2, y2 in ((640, 420, 600, 380), (650, 470, 600, 470), (640, 520, 600, 560)))
scenes[s] = scene_file(s, f"""
#sn-svg {{ position:absolute; left:0; top:0; }}
#sn-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#sn-v {{ position:absolute; left:700px; top:380px; opacity:0; }}
#sn-hic {{ position:absolute; left:660px; top:540px; {GH} font-size:180px; line-height:1; color:{C['red']}; opacity:0; }}
#sn-w {{ position:absolute; left:120px; top:640px; opacity:0; }}
""", f"""
  <svg id="sn-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="sn-tube">
      <rect x="470" y="250" width="140" height="590" fill="#FFF3F0"/>
      <path class="sn-wl" d="M470,250 L470,840" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
      <path class="sn-wl" d="M610,250 L610,840" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
      <path id="sn-fl" d="{OPEN_L}" stroke="{CORD}" stroke-width="18" fill="none" stroke-linecap="round"/>
      <path id="sn-fr" d="{OPEN_R}" stroke="{CORD}" stroke-width="18" fill="none" stroke-linecap="round"/>
    </g>
    <path id="sn-lv" d="M600,440 L700,420" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    {early}{late}{hburst}
  </svg>
  <div id="sn-c"><span class="chip" style="background:#FFFFFF;font-size:58px">a split second later…</span></div>
  <div id="sn-v"><span class="chip" style="background:{CORD};font-size:50px">vocal cords</span></div>
  <div id="sn-w"><span class="chip" style="background:{AIR};font-size:42px;transform:rotate(-3deg)">windpipe</span></div>
  <div id="sn-hic">HIC!</div>
""", J("""
tl.fromTo("#sn-tube", {opacity:0}, {opacity:1, duration:0.2}, 0.0); ink(".sn-wl", 0.0, 0.5);
tl.set("#sn-w", {opacity:1}, 0.3); pop("#sn-w .chip", 0.3);
tl.set("#sn-c", {opacity:1}, @tc); pop("#sn-c .chip", @tc, {from:{rotation:-8}, to:{rotation:-2}});
ink("#sn-lv", @tv, 0.25); tl.set("#sn-v", {opacity:1}, @tv); pop("#sn-v .chip", @tv, {from:{rotation:10}, to:{rotation:3}});
morph("#sn-fl", "@shutl", @ts, 0.12, {ease:"power4.in"}); morph("#sn-fr", "@shutr", @ts, 0.12, {ease:"power4.in"});
tl.fromTo("#sn-tube", {y:0}, {y:8, duration:0.05, yoyo:true, repeat:3, immediateRender:false}, @ts2);
tl.set("#sn-hic", {opacity:1}, @th); pop("#sn-hic", @th, {from:{scale:2.2, rotation:-18}, to:{rotation:-8, duration:0.3}});
ink(".sn-b", @th, 0.2, {stagger:0.04});
""", tc=tsp - 0.1, tv=tvc - 0.1, ts=tsh - 0.1, ts2=tsh + 0.02, th=thi - 0.05, shutl=SHUT_L, shutr=SHUT_R)
  + "".join(f'tl.set("#sn-e{i}", {{opacity:1}}, {tla - 0.4 + i * 0.22:.3f}); along("#sn-e{i}", "#sn-pe{i}", {tla - 0.4 + i * 0.22:.3f}, 0.7, {{ease:"power1.in"}}); tl.set("#sn-e{i}", {{opacity:0}}, {tla + 0.3 + i * 0.22:.3f});\n' for i in range(6))
  + "".join(f'tl.set("#sn-l{i}", {{opacity:1}}, {tsh + 0.05 + i * 0.12:.3f}); along("#sn-l{i}", "#sn-pl{i}", {tsh + 0.05 + i * 0.12:.3f}, 0.4, {{ease:"power2.in"}});\n' for i in range(6)))

# 7 WOMB — womb inks, a curled baby jolts with tiny hics; a weeks ruler, marker slides to 9
s = "womb"; tws = aw(s, "weirder"); tba = aw(s, "babies"); twm = aw(s, "womb"); t9 = aw(s, "nine weeks")
WX = lambda w: 140 + w * 20
rt = "".join(f'<path d="M{WX(w)},730 L{WX(w)},{770 if w % 10 == 0 else 756}" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for w in range(0, 41, 5))
rl = "".join(f'<text x="{WX(w)}" y="815" text-anchor="middle" style="{GH}font-size:42px" fill="{K}">{w}</text>' for w in range(0, 41, 10))
scenes[s] = scene_file(s, f"""
#wb-svg {{ position:absolute; left:0; top:0; }}
#wb-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#wb-n {{ position:absolute; left:370px; top:608px; opacity:0; }}
#wb-baby, #wb-fill, #wb-rul {{ opacity:0; }}
""", f"""
  <svg id="wb-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <ellipse id="wb-fill" cx="540" cy="410" rx="240" ry="180" fill="#FDE3E8"/>
    <path class="wb-w" d="M540,230 Q780,230 780,410 Q780,590 540,590" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="wb-w" d="M540,590 Q300,590 300,410 Q300,230 540,230" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <g id="wb-baby">
      <path d="M560,400 Q450,430 465,500 Q490,545 580,530 Q645,515 640,450 Z" fill="{SKIN}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
      <circle cx="590" cy="360" r="58" fill="{SKIN}" stroke="{K}" stroke-width="6"/>
      <path d="M598,352 Q610,346 620,354" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    </g>
    <text id="wb-h1" x="790" y="260" style="{GH}font-size:52px" fill="{C['red']}" opacity="0">hic</text>
    <text id="wb-h2" x="380" y="320" style="{GH}font-size:44px" fill="{C['red']}" opacity="0">hic</text>
    <g id="wb-rul"><rect x="120" y="690" width="840" height="40" rx="6" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>{rt}{rl}
      <text x="960" y="870" text-anchor="end" style="{GH}font-size:40px" fill="{C['muted']}">weeks</text></g>
    <g id="wb-mk" opacity="0"><path d="M{WX(0)},686 L{WX(0) - 22},646 L{WX(0) + 22},646 Z" fill="{C['red']}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/></g>
  </svg>
  <div id="wb-c"><span class="chip" style="background:#FFFFFF;font-size:56px">weirder still…</span></div>
  <div id="wb-n"><span class="chip" style="background:{C['hi']};font-size:54px">from about 9 weeks</span></div>
""", J("""
tl.set("#wb-c", {opacity:1}, @tw); pop("#wb-c .chip", @tw, {from:{rotation:-10}, to:{rotation:-3}});
ink(".wb-w", @tb, 0.6, {stagger:0.1}); tl.fromTo("#wb-fill", {opacity:0}, {opacity:1, duration:0.4}, @tb2);
tl.fromTo("#wb-baby", {opacity:0, scale:0.5, svgOrigin:"560 450"}, {opacity:1, scale:1, svgOrigin:"560 450", duration:0.4, ease:"back.out(2)"}, @tm);
tl.fromTo("#wb-baby", {y:0}, {y:-22, duration:0.08, yoyo:true, repeat:1, immediateRender:false}, @tm2); pop("#wb-h1", @tm2);
tl.fromTo("#wb-baby", {y:0}, {y:-22, duration:0.08, yoyo:true, repeat:1, immediateRender:false}, @tm3); pop("#wb-h2", @tm3);
tl.fromTo("#wb-rul", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"power3.out"}, @tr);
tl.fromTo("#wb-mk", {opacity:0}, {opacity:1, duration:0.15}, @tr2);
tl.to("#wb-mk", {x:@dx, duration:0.6, ease:"back.out(1.6)"}, @t9);
tl.set("#wb-n", {opacity:1}, @t9b); pop("#wb-n .chip", @t9b, {from:{rotation:-8}, to:{rotation:-2}});
""", tw=tws - 0.1, tb=tba - 0.3, tb2=tba + 0.2, tm=twm - 0.2, tm2=twm + 0.4, tm3=twm + 1.2, tr=twm + 0.3, tr2=twm + 0.6, t9=t9 - 0.3, t9b=t9 + 0.1, dx=WX(9) - WX(0)))

# 8 PREEMIE — 100 squares = all their time; one turns red = 1%; about 15 minutes a day
s = "preemie"; tpr = aw(s, "premature"); t1p = aw(s, "one percent"); t15 = aw(s, "fifteen minutes")
sq = "".join(f'<rect class="pr-s" id="pr-s{i}" x="{150 + (i % 10) * 50}" y="{300 + (i // 10) * 50}" width="42" height="42" rx="6" fill="#FFFFFF" stroke="{K}" stroke-width="3"/>' for i in range(100))
scenes[s] = scene_file(s, f"""
#pr-svg {{ position:absolute; left:0; top:0; }}
#pr-c {{ position:absolute; left:0; right:0; top:155px; text-align:center; opacity:0; }}
#pr-a {{ position:absolute; left:690px; top:360px; width:340px; opacity:0; }}
#pr-b {{ position:absolute; left:690px; top:560px; width:340px; opacity:0; }}
#pr-a .chip, #pr-b .chip {{ text-align:center; line-height:1.05; padding:10px 18px; }}
""", f"""
  <svg id="pr-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>{sq}
    <text x="400" y="845" text-anchor="middle" style="{GH}font-size:40px" fill="{C['muted']}">100 squares = all their time</text>
    <path id="pr-ar" d="M690,410 Q560,380 200,322" stroke="{C['red']}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="2 12"/>
  </svg>
  <div id="pr-c"><span class="chip" style="background:#FFFFFF;font-size:54px">premature babies</span></div>
  <div id="pr-a"><span class="chip" style="background:#FFC9C2;font-size:60px">1% of the time</span></div>
  <div id="pr-b"><span class="chip" style="background:{C['hi']};font-size:56px">about 15 minutes a day</span></div>
""", J("""
tl.set("#pr-c", {opacity:1}, @tp); pop("#pr-c .chip", @tp, {from:{rotation:-8}, to:{rotation:-2}});
tl.fromTo(".pr-s", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, stagger:0.012, ease:"back.out(2)"}, @tp2);
tl.to("#pr-s0", {attr:{fill:"@red"}, duration:0.15}, @t1);
tl.fromTo("#pr-s0", {scale:1, transformOrigin:"50% 50%"}, {scale:1.5, duration:0.18, yoyo:true, repeat:1, immediateRender:false}, @t1);
ink("#pr-ar", @t1b, 0.4);
tl.set("#pr-a", {opacity:1}, @t1b); pop("#pr-a .chip", @t1b, {from:{rotation:10}, to:{rotation:3}});
tl.set("#pr-b", {opacity:1}, @t15); pop("#pr-b .chip", @t15, {from:{rotation:-10}, to:{rotation:-3}});
""", tp=tpr - 0.1, tp2=tpr + 0.1, t1=t1p - 0.1, t1b=t1p + 0.2, t15=t15 - 0.1, red=C['red']))

# 9 BRAIN — 2019 study: each hiccup -> three brainwaves inked on an EEG strip; loop brain <-> breathing muscle
s = "brain"; t19 = aw(s, "twenty nineteen"); tnh = aw(s, "newborn hiccup"); t3 = aw(s, "three brainwaves"); tmb = aw(s, "maybe"); ttb = aw(s, "teach babies"); tbm = aw(s, "breathing muscles")
grid = "".join(f'<path d="M{x},310 L{x},510" stroke="{C["rule"]}" stroke-width="2"/>' for x in range(520, 1000, 40))
bumps = [("M560,420 Q585,330 610,420 Q625,470 640,420", 600), ("M680,420 Q705,330 730,420 Q745,470 760,420", 720), ("M800,420 Q840,365 880,420", 840)]
bh = "".join(f'<path class="br-bp" id="br-bp{i}" d="{d}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<text id="br-n{i}" x="{x}" y="350" text-anchor="middle" style="{GH}font-size:46px" fill="{C["red"]}" opacity="0">{i + 1}</text>' for i, (d, x) in enumerate(bumps))
segs = "".join(f'<path class="br-sg" d="{d}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round"/>' for d in ("M500,420 L560,420", "M640,420 L680,420", "M760,420 L800,420", "M880,420 L990,420"))
scenes[s] = scene_file(s, f"""
#br-svg {{ position:absolute; left:0; top:0; }}
#br-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#br-t {{ position:absolute; left:520px; top:540px; opacity:0; }}
#br-m {{ position:absolute; left:450px; top:690px; width:580px; opacity:0; }}
#br-m .chip {{ text-align:center; line-height:1.05; padding:8px 18px; }}
#br-strip, #br-dd {{ opacity:0; }}
""", f"""
  <svg id="br-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="br-head" d="M300,280 Q440,280 440,420 Q440,560 300,560 Q160,560 160,420 Q160,280 300,280 Z" fill="{SKIN}" stroke="{K}" stroke-width="7"/>
    <path id="br-br" d="M200,390 Q200,300 300,300 Q400,300 400,390 Q350,410 300,395 Q250,410 200,390 Z" fill="{PINK}" stroke="{K}" stroke-width="5" opacity="0"/>
    <path d="M250,460 Q262,450 274,460 M326,460 Q338,450 350,460 M285,505 Q300,515 315,505" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g id="br-strip"><rect x="480" y="300" width="530" height="220" rx="10" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>{grid}</g>
    <path id="br-wire" d="M400,360 Q450,330 480,370" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>
    {segs}{bh}
    <path id="br-dd" d="M200,820 Q300,730 400,820" stroke="{DIA}" stroke-width="14" fill="none" stroke-linecap="round"/>
    <path class="br-lp" d="M420,520 Q500,660 410,770" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="14 10"/>
    <path class="br-lp" d="M398,540 L420,520 L428,548" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="br-lp" d="M402,742 L410,770 L436,760" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="br-c"><span class="chip" style="background:#FFFFFF;font-size:54px">a 2019 study of newborns</span></div>
  <div id="br-t"><span class="chip" style="background:{AIR};font-size:46px;transform:rotate(-2deg)">3 brainwaves per hiccup</span></div>
  <div id="br-m"><span class="chip" style="background:{C['hi']};font-size:46px;transform:rotate(2deg)">maybe: learning to feel the breathing muscles</span></div>
""", J("""
tl.set("#br-c", {opacity:1}, @tc); pop("#br-c .chip", @tc, {from:{rotation:-8}, to:{rotation:-2}});
ink("#br-head", 0.05, 0.6); tl.fromTo("#br-br", {opacity:0}, {opacity:1, duration:0.3}, 0.5);
tl.fromTo("#br-strip", {opacity:0, x:40}, {opacity:1, x:0, duration:0.35, ease:"power3.out"}, @tn);
ink("#br-wire", @tn2, 0.3); ink(".br-sg", @tn2, 0.2, {stagger:0.0});
tl.fromTo("#br-head", {y:0}, {y:-14, duration:0.08, yoyo:true, repeat:1, immediateRender:false}, @tn3);
ink("#br-bp0", @b0, 0.3); pop("#br-n0", @b0);
ink("#br-bp1", @b1, 0.3); pop("#br-n1", @b1);
ink("#br-bp2", @b2, 0.3); pop("#br-n2", @b2);
tl.set("#br-t", {opacity:1}, @tt); pop("#br-t .chip", @tt, {from:{rotation:-10}, to:{rotation:-2}});
tl.fromTo("#br-dd", {opacity:0}, {opacity:1, duration:0.3}, @tm); ink("#br-dd", @tm, 0.5);
ink(".br-lp", @tb, 0.5, {stagger:0.25});
tl.set("#br-m", {opacity:1}, @tbm); pop("#br-m .chip", @tbm, {from:{rotation:8}, to:{rotation:2}});
""", tc=t19 - 0.1, tn=tnh - 0.6, tn2=tnh - 0.3, tn3=tnh + 0.4, b0=t3 - 0.7, b1=t3 - 0.2, b2=t3 + 0.3, tt=t3 + 0.6, tm=tmb, tb=ttb, tbm=tbm - 0.6))

# 10 GILLS — one hypothesis: a tadpole swims along a wavy path, gills pulse; nobody knows for sure
s = "gills"; tid = aw(s, "another idea"); tlo = aw(s, "leftover"); tan = aw(s, "ancestors"); tgi = aw(s, "gills"); ttp = aw(s, "tadpoles"); tnk = aw(s, "nobody knows")
gslits = "".join(f'<path class="gi-sl" d="M{x},4 Q{x + 6},16 {x},28" stroke="{C["red"]}" stroke-width="5" fill="none" stroke-linecap="round"/>' for x in (-14, -2, 10))
scenes[s] = scene_file(s, f"""
#gi-svg {{ position:absolute; left:0; top:0; }}
#gi-tape {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#gi-tape span {{ display:inline-block; padding:6px 40px; background:rgba(255,201,194,.85); {GH} font-size:58px; transform:rotate(-3deg); border-left:6px dashed #fff; border-right:6px dashed #fff; }}
#gi-a {{ position:absolute; left:0; right:0; top:255px; text-align:center; opacity:0; }}
#gi-q {{ position:absolute; left:110px; top:370px; {GH} font-size:220px; line-height:1; color:{C['red']}; opacity:0; }}
#gi-n {{ position:absolute; left:440px; top:770px; opacity:0; }}
#gi-water {{ opacity:0; }}
""", f"""
  <svg id="gi-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="gi-water" d="M60,380 Q190,350 320,380 T580,380 T840,380 T1020,380 L1020,720 L60,720 Z" fill="#DDF0FA" stroke="{C['blue']}" stroke-width="5"/>
    <path id="gi-route" d="M120,600 C260,470 400,680 560,550 S820,450 960,560" fill="none" stroke="none"/>
    <path id="gi-trail" d="M120,600 C260,470 400,680 560,550 S820,450 960,560" stroke="{AIRD}" stroke-width="6" fill="none" stroke-linecap="round" stroke-dasharray="4 16"/>
    <g id="gi-tad" opacity="0">
      <g id="gi-tail"><path d="M-40,0 Q-80,-26 -125,-4 Q-82,22 -40,0 Z" fill="#5E6B3C" stroke="{K}" stroke-width="4" stroke-linejoin="round"/></g>
      <ellipse cx="0" cy="0" rx="52" ry="40" fill="#7E8C4E" stroke="{K}" stroke-width="5"/>
      <circle cx="26" cy="-14" r="11" fill="#FFFFFF" stroke="{K}" stroke-width="3"/><circle cx="29" cy="-14" r="5" fill="{K}"/>
      {gslits}
    </g>
  </svg>
  <div id="gi-tape"><span>one hypothesis</span></div>
  <div id="gi-a"><span class="chip" style="background:#FFFFFF;font-size:50px">a leftover from ancestors with gills?</span></div>
  <div id="gi-q">?</div>
  <div id="gi-n"><span class="chip" style="background:{C['hi']};font-size:52px">nobody knows for sure</span></div>
""", J("""
tl.set("#gi-tape", {opacity:1}, @ti); pop("#gi-tape span", @ti, {from:{rotation:-12, scale:1.3}, to:{rotation:-3}});
tl.fromTo("#gi-water", {opacity:0}, {opacity:1, duration:0.4}, 0.1);
tl.set("#gi-a", {opacity:1}, @tl); pop("#gi-a .chip", @tl, {from:{rotation:8}, to:{rotation:1}});
tl.set("#gi-tad", {opacity:1}, @ta);
ink("#gi-trail", @ta, @dd, {ease:"none"});
along("#gi-tad", "#gi-route", @ta, @dd, {ease:"sine.inOut", rotate:true});
tl.fromTo("#gi-tail", {rotation:-14, svgOrigin:"-40 0"}, {rotation:14, svgOrigin:"-40 0", duration:0.18, yoyo:true, repeat:@rp, ease:"sine.inOut"}, @ta);
tl.fromTo(".gi-sl", {scaleY:1, transformOrigin:"50% 0%"}, {scaleY:1.6, duration:0.2, yoyo:true, repeat:5, ease:"sine.inOut", stagger:0.05}, @tg);
tl.set("#gi-q", {opacity:1}, @tn); pop("#gi-q", @tn, {from:{rotation:-20, scale:1.8}, to:{rotation:8}});
tl.set("#gi-n", {opacity:1}, @tn2); pop("#gi-n .chip", @tn2, {from:{rotation:-8}, to:{rotation:-2}});
""", ti=tid - 0.1, tl=tlo - 0.1, ta=tan - 0.3, dd=tnk - tan + 0.2, rp=int((tnk - tan + 0.6) / 0.18), tg=tgi - 0.1, tn=tnk - 0.1, tn2=tnk + 0.4))

# 11 TIPS — triggers on sticky notes; then remedies in pencil with a thin evidence meter; > 2 days: see a doctor
s = "tips"; tfz = aw(s, "fizzy drinks"); tef = aw(s, "eating fast"); tms = aw(s, "most stop"); thr = aw(s, "home remedies"); tth = aw(s, "thin"); t2d = aw(s, "two days"); tdoc = aw(s, "see a doctor")
bub = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["blue"]}" stroke-width="4"/>' for cx, cy, r in ((70, 236, 11), (130, 246, 8), (250, 240, 12), (310, 232, 9)))
scenes[s] = scene_file(s, f"""
#tp-svg {{ position:absolute; left:0; top:0; }}
#tp-hA {{ position:absolute; left:0; right:0; top:155px; text-align:center; opacity:0; }}
.tp-note {{ position:absolute; top:290px; width:380px; height:270px; border:4px solid {K}; {SKETCH} text-align:center; font-family:'Patrick Hand',cursive; font-size:70px; line-height:1.05; padding-top:56px; opacity:0; }}
#tp-n1 {{ left:120px; background:{AIR}; transform:rotate(-4deg); }}
#tp-n2 {{ left:580px; background:{C['hi']}; transform:rotate(3deg); }}
#tp-ms {{ position:absolute; left:0; right:0; top:630px; text-align:center; opacity:0; }}
#tp-hB {{ position:absolute; left:0; right:0; top:155px; text-align:center; {GH} font-size:84px; opacity:0; }}
.tp-r {{ position:absolute; left:250px; {GH} font-size:60px; color:{C['pencil']}; opacity:0; }}
#tp-ev {{ position:absolute; left:150px; top:500px; {GH} font-size:56px; opacity:0; }}
#tp-thin {{ position:absolute; left:760px; top:445px; {GH} font-size:64px; color:{C['red']}; border:5px solid {C['red']}; padding:0 18px; border-radius:10px; opacity:0; }}
#tp-doc {{ position:absolute; left:420px; top:680px; width:600px; padding:14px 20px; text-align:center; background:#FFFFFF; border:5px solid {C['red']}; {SKETCH} {GH} font-size:54px; line-height:1.1; opacity:0; }}
#tp-meter {{ opacity:0; }}
""", f"""
  <div id="tp-A">
    <div id="tp-hA"><span class="chip" style="background:#FFFFFF;font-size:54px">common triggers</span></div>
    <div id="tp-n1" class="tp-note">fizzy<br>drinks<svg class="abs" style="left:0;top:0" width="380" height="270" data-layout-ignore>{bub}</svg></div>
    <div id="tp-n2" class="tp-note">eating<br>too fast</div>
    <div id="tp-ms"><span class="chip" style="background:{C['hi']};font-size:54px">most stop in minutes</span></div>
  </div>
  <div id="tp-hB">home remedies?</div>
  <div class="tp-r" id="tp-r1" style="top:270px">spoon of sugar?</div>
  <div class="tp-r" id="tp-r2" style="top:345px">hold your breath?</div>
  <div class="tp-r" id="tp-r3" style="top:420px">a sudden fright?</div>
  <div id="tp-ev">evidence:</div>
  <svg id="tp-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="tp-meter"><rect x="400" y="515" width="340" height="56" rx="10" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>
      <rect id="tp-fill" x="406" y="521" width="34" height="44" rx="6" fill="{C['red']}"/></g>
  </svg>
  <div id="tp-thin">THIN</div>
  <div id="tp-doc">lasts over 2 days?<br><span class="red">see a doctor</span></div>
""", J("""
tl.set("#tp-hA", {opacity:1}, @tf0); pop("#tp-hA .chip", @tf0);
tl.set("#tp-n1", {opacity:1}, @tf); pop("#tp-n1", @tf, {from:{rotation:-20}, to:{rotation:-4}});
tl.set("#tp-n2", {opacity:1}, @te); pop("#tp-n2", @te, {from:{rotation:20}, to:{rotation:3}});
tl.set("#tp-ms", {opacity:1}, @tm); pop("#tp-ms .chip", @tm, {from:{rotation:-8}, to:{rotation:-2}});
tl.to("#tp-A", {opacity:0, y:-40, duration:0.3, ease:"power2.in"}, @tA);
tl.set("#tp-hB", {opacity:1}, @th); pop("#tp-hB", @th, {from:{rotation:-6}, to:{}});
rise("#tp-r1", @tr1); rise("#tp-r2", @tr2); rise("#tp-r3", @tr3);
tl.set("#tp-ev", {opacity:1}, @tev); rise("#tp-ev", @tev);
tl.fromTo("#tp-meter", {opacity:0}, {opacity:1, duration:0.25}, @tev);
tl.fromTo("#tp-fill", {scaleX:0, svgOrigin:"406 543"}, {scaleX:1, svgOrigin:"406 543", duration:0.4, ease:"power2.out"}, @tt);
tl.set("#tp-thin", {opacity:1}, @tt2); pop("#tp-thin", @tt2, {from:{rotation:-30, scale:1.8}, to:{rotation:-12}});
tl.set("#tp-doc", {opacity:1}, @t2); pop("#tp-doc", @t2, {from:{rotation:6}, to:{rotation:-1}});
tl.fromTo("#tp-doc", {scale:1}, {scale:1.06, duration:0.14, yoyo:true, repeat:1, immediateRender:false}, @td);
""", tf0=tfz - 0.3, tf=tfz - 0.1, te=tef - 0.2, tm=tms - 0.1, tA=thr - 0.45, th=thr - 0.1, tr1=thr + 0.3, tr2=thr + 0.55, tr3=thr + 0.8,
    tev=tth - 0.9, tt=tth - 0.4, tt2=tth, t2=t2d - 0.6, td=tdoc))

# 12 OUTRO — callback: jerk + slam = HIC! (Max centre stage, keep y < 620)
s = "outro"; tje = aw(s, "muscle jerk"); tsl = aw(s, "slam"); tbb = aw(s, "baby brain"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-eq {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:64px; }}
#ou-eq > span {{ display:inline-block; opacity:0; vertical-align:middle; }}
#ou-b {{ position:absolute; left:0; right:0; top:330px; text-align:center; opacity:0; }}
#ou-sc {{ top:400px; font-size:110px; opacity:0; }}
""", f"""
  <div id="ou-eq"><span id="ou-1"><span class="chip" style="background:{C['hi']};font-size:56px">muscle jerk</span></span>
    <span id="ou-p">+</span>
    <span id="ou-2"><span class="chip" style="background:{CORD};font-size:56px">slam</span></span>
    <span id="ou-e">=</span>
    <span id="ou-h" style="color:{C['red']};font-size:96px">HIC!</span></div>
  <div id="ou-b"><span class="chip" style="background:#FFFFFF;font-size:50px">…and maybe a baby brain workout</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-1", @tj, {from:{rotation:-10}, to:{}}); pop("#ou-p", @tj2);
pop("#ou-2", @ts, {from:{rotation:10}, to:{}}); pop("#ou-e", @ts2); pop("#ou-h", @ts3, {from:{scale:2, rotation:-16}, to:{rotation:-6}});
tl.set("#ou-b", {opacity:1}, @tb); pop("#ou-b .chip", @tb, {from:{rotation:-6}, to:{rotation:-1}});
tl.to("#ou-b", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
tl.set("#ou-sc", {opacity:1}, @tsc); pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", tj=tje - 0.1, tj2=tje + 0.4, ts=tsl - 0.1, ts2=tsl + 0.25, ts3=tsl + 0.45, tb=tbb - 0.6, tx=tsc - 0.3, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "so why"), SC["guess"]["start"] + 0.2)
point(g("guess", "swallowed air"), 2.6)
wave(g("intro", "I'm Max"))
point(g("muscle", "diaphragm"), 1.3)
wow(g("spasm", "jerks"), 1.0)
point(g("snap", "vocal cords"), 1.0)
wow(g("snap", "hic"), 0.9)
point(g("womb", "nine weeks"), 1.2)
point(g("preemie", "one percent"), 1.2)
wow(g("brain", "three brainwaves"), 1.2)
think(g("gills", "nobody knows"), SC["tips"]["start"] - 0.1)
point(g("tips", "two days"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "hic"), 0.6), ("pop.mp3", A("guess", "swallowed air"), 0.45), ("pop.mp3", A("guess", "twitchy muscle"), 0.45),
        ("pop.mp3", A("guess", "your baby"), 0.5), ("sparkle.mp3", A("intro", "max wise"), 0.4), ("click-soft.mp3", A("muscle", "flattens"), 0.5),
        ("impact-bass-1.mp3", A("spasm", "jerks"), 0.45), ("whoosh-short.mp3", A("spasm", "air rushes"), 0.3),
        ("click.mp3", A("snap", "slam shut"), 0.55), ("pop.mp3", A("snap", "hic"), 0.6), ("ping.mp3", A("womb", "nine weeks"), 0.4),
        ("ping.mp3", A("preemie", "one percent"), 0.4), ("sparkle.mp3", A("brain", "three brainwaves"), 0.4),
        ("click-soft.mp3", A("tips", "thin"), 0.5), ("impact-bass-2.mp3", A("tips", "two days"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
