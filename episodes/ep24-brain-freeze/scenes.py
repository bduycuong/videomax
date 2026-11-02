# MAX WISE ep24 — Why does ice cream give you brain freeze?
# Kit: ink / along / morph helpers; 2D only (no three.js). Source: APS / Experimental Biology 2012 (Serrador et al.), via ScienceDaily.
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
ICE = "#BFE3F7"; BLOOD = "#E8574A"; NERVE = "#F2B705"; SKIN = "#FCE3D2"; PINK = "#F7C6CF"

def head(p):
    """side-view head facing right, inside a 1080x760 svg; palate arc and tongue get ids with prefix p"""
    return (f'<path id="{p}-hd" d="M600,740 L600,640 Q360,620 340,380 Q330,110 560,90 Q760,80 790,260 L840,380 L800,400 L812,452 Q790,468 802,500 Q812,560 740,585 L700,640 L700,740" fill="{SKIN}" stroke="{K}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<ellipse cx="530" cy="260" rx="160" ry="115" fill="{PINK}" stroke="{K}" stroke-width="5" stroke-dasharray="14 9"/>'
            f'<path d="M430,250 Q470,200 520,250 Q560,300 610,240" stroke="#D88C9A" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<circle cx="725" cy="300" r="12" fill="{K}"/>'
            f'<path id="{p}-pal" d="M600,452 Q700,410 806,452" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path id="{p}-tg" d="M600,500 Q700,520 795,490" stroke="#D45C6E" stroke-width="14" fill="none" stroke-linecap="round"/>')

# 1 HOOK — ice cream cone inks itself; a face gets pain zigzags on the forehead
s = "hook"; tbf = aw(s, "brain freeze"); tfh = aw(s, "forehead"); tic = aw(s, "ice cream")
scenes[s] = scene_file(s, f"""
#hk-t {{ top:160px; font-size:90px; line-height:1.05; }}
#hk-svg {{ position:absolute; left:0; top:300px; }}
#hk-o {{ position:absolute; left:640px; top:300px; opacity:0; {GH} font-size:80px; color:{C['red']}; }}
""", f"""
  <div id="hk-t" class="h1"><span class="hl">Brain freeze?</span></div>
  <svg id="hk-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <circle id="hk-s1" cx="230" cy="190" r="85" fill="{PINK}" stroke="{K}" stroke-width="7"/>
    <circle id="hk-s2" cx="330" cy="170" r="80" fill="{ICE}" stroke="{K}" stroke-width="7"/>
    <path class="hk-c" d="M160,240 L280,560" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="hk-c" d="M280,560 L410,230" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="hk-c" d="M160,240 L410,230" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="hk-c" d="M200,300 L370,330 M220,380 L350,400" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <circle id="hk-f" cx="780" cy="330" r="190" fill="{SKIN}" stroke="{K}" stroke-width="8"/>
    <circle cx="720" cy="350" r="14" fill="{K}"/><circle cx="840" cy="350" r="14" fill="{K}"/>
    <path d="M720,440 Q780,410 840,440" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path class="hk-z" d="M680,240 L705,205 L730,240 L755,205 L780,240 L805,205 L830,240 L855,205 L880,240" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="hk-z" d="M700,280 L720,262 L740,280" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path class="hk-z" d="M820,280 L840,262 L860,280" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="hk-o">OUCH!</div>
""", J("""
ink(".hk-c", @tc, 0.35, {stagger:0.1});
pop("#hk-s1", @tc2); pop("#hk-s2", @tc3);
pop("#hk-t", @tbf, {from:{scale:1.4}, to:{}});
pop("#hk-f", @tf0);
ink(".hk-z", @tfh, 0.3, {stagger:0.08});
tl.set("#hk-o", {opacity:1}, @tfh2); pop("#hk-o", @tfh2, {from:{rotation:-20, scale:1.6}, to:{rotation:-8}});
""", tc=max(0.05, tic - 0.3), tc2=tic + 0.4, tc3=tic + 0.55, tbf=tbf - 0.1, tf0=tbf + 0.3, tfh=tfh - 0.6, tfh2=tfh - 0.1))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "brain freezing"); t2 = aw(s, "your nerves"); t3 = aw(s, "your blood")
notes = [("a", "brain freezing?", -6, 110, ICE), ("b", "nerves?", 4, 405, C['hi']), ("c", "blood?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:62px;line-height:1.05;padding:80px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3 - 0.2))

# 3 INTRO — logo + snowflake inks itself
s = "intro"; tmw = aw(s, "Max Wise"); tcb = aw(s, "cold bite")
flake = "".join(f'<path class="in-fl" d="M540,90 L{540 + 80*math.cos(a):.0f},{90 + 80*math.sin(a):.0f}" stroke="{C["blue"]}" stroke-width="8" fill="none" stroke-linecap="round"/>' for a in [i * math.pi / 3 for i in range(6)])
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:62px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Follow the cold!</span></div>
  <svg class="abs" style="left:0;top:500px" width="{W}" height="190" data-layout-ignore>{flake}</svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tc); ink(".in-fl", @tc, 0.2, {stagger:0.08});
""", tmw=tmw, tu=tmw + 0.3, tc=tcb - 0.5))

# 4 PALATE — side-view head; an ice cube travels along a path into the mouth and touches the palate
s = "palate"; tic = aw(s, "icy"); tpa = aw(s, "palate"); tro = aw(s, "roof of")
scenes[s] = scene_file(s, f"""
#pa-svg {{ position:absolute; left:0; top:200px; }}
#pa-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#pa-glow {{ opacity:0; }}
""", f"""
  <div id="pa-c"><span class="chip">roof of the mouth = palate</span></div>
  <svg id="pa-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    {head("pa")}
    <ellipse id="pa-glow" cx="705" cy="440" rx="110" ry="40" fill="{ICE}" opacity=".85"/>
    <path id="pa-route" d="M1020,700 Q980,520 760,470" fill="none" stroke="none"/>
    <path id="pa-trail" d="M1020,700 Q980,520 760,470" stroke="{ICE}" stroke-width="10" stroke-dasharray="4 18" fill="none" stroke-linecap="round"/>
    <g id="pa-cube"><rect x="-32" y="-32" width="64" height="64" rx="10" fill="{ICE}" stroke="{K}" stroke-width="5"/><path d="M-16,-14 L0,-22" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/></g>
  </svg>
""", J("""
ink("#pa-hd", 0.05, 0.8);
tl.fromTo("#pa-cube", {opacity:0}, {opacity:1, duration:0.2}, @ta);
ink("#pa-trail", @ta, 0.8);
along("#pa-cube", "#pa-route", @ta, 0.9, {ease:"power2.in"});
tl.fromTo("#pa-glow", {opacity:0}, {opacity:0.85, duration:0.3}, @tr);
tl.to("#pa-pal", {stroke:"@blue", duration:0.3}, @tr);
tl.set("#pa-c", {opacity:1}, @tp); pop("#pa-c .chip", @tp, {from:{rotation:-10}, to:{rotation:-3}});
""", ta=max(0.6, tic - 0.4), tr=tro - 0.1, tp=tro + 0.1, blue=C['blue']))

# 5 NERVES — same head; a yellow nerve bundle inks itself above the palate
s = "nerves"; tbn = aw(s, "bundle of"); tco = aw(s, "to cold")
nv = "".join(f'<path class="nv-n" d="M700,430 Q{700 + dx*0.4:.0f},{390} {700 + dx},{330 - abs(dx)*0.3:.0f}" stroke="{NERVE}" stroke-width="7" fill="none" stroke-linecap="round"/>' for dx in (-90, -45, 0, 45, 90))
sp = "".join(f'<path class="nv-s" d="M{x},{y} l14,-14 M{x},{y} l-14,-14 M{x},{y} l0,-20" stroke="{C["blue"]}" stroke-width="5" fill="none" stroke-linecap="round"/>' for x, y in [(610, 330), (700, 300), (790, 330)])
scenes[s] = scene_file(s, f"""
#nv-svg {{ position:absolute; left:0; top:200px; }}
#nv-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
""", f"""
  <div id="nv-c"><span class="chip" style="background:#FFF3C4">a bundle of nerves</span></div>
  <svg id="nv-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    {head("nv")}
    <ellipse cx="705" cy="440" rx="110" ry="40" fill="{ICE}" opacity=".85"/>
    {nv}
    <circle id="nv-k" cx="700" cy="425" r="20" fill="{NERVE}" stroke="{K}" stroke-width="5"/>
    {sp}
  </svg>
""", J("""
tl.set("#nv-pal", {stroke:"@blue"}, 0);
pop("#nv-k", @tb);
ink(".nv-n", @tb, 0.4, {stagger:0.08});
tl.set("#nv-c", {opacity:1}, @tb); pop("#nv-c .chip", @tb, {from:{rotation:-10}, to:{rotation:-3}});
ink(".nv-s", @tc, 0.2, {stagger:0.1});
""", tb=tbn - 0.1, tc=tco - 0.3, blue=C['blue']))

# 6 ARTERY — a blood vessel morphs from thin to wide
s = "artery"; tss = aw(s, "small study"); tbv = aw(s, "blood vessel"); twi = aw(s, "suddenly widen")
THIN = "M120,430 C400,410 680,450 960,430 L960,470 C680,490 400,450 120,470 Z"
WIDE = "M120,350 C400,320 680,370 960,350 L960,550 C680,580 400,530 120,550 Z"
scenes[s] = scene_file(s, f"""
#ar-svg {{ position:absolute; left:0; top:150px; }}
#ar-c {{ position:absolute; left:0; right:0; top:170px; text-align:center; opacity:0; }}
#ar-l {{ position:absolute; left:0; right:0; top:790px; text-align:center; opacity:0; padding-left:240px; }}
#ar-w {{ position:absolute; left:740px; top:330px; opacity:0; {GH} font-size:64px; color:{C['red']}; }}
""", f"""
  <div id="ar-c"><span class="chip" style="background:#FFFFFF">a small study</span></div>
  <svg id="ar-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    <path id="ar-v" d="{THIN}" fill="{BLOOD}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path class="ar-a" d="M540,330 L540,250 M515,275 L540,250 L565,275" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="ar-a" d="M540,570 L540,650 M515,625 L540,650 L565,625" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="ar-l"><span class="chip" style="background:#FFC9C2">blood vessel, front of the brain</span></div>
  <div id="ar-w">WHOOSH!</div>
""", J("""
tl.set("#ar-c", {opacity:1}, @ts); pop("#ar-c .chip", @ts, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo("#ar-v", {opacity:0}, {opacity:1, duration:0.3}, @tb);
tl.set("#ar-l", {opacity:1}, @tb); pop("#ar-l .chip", @tb, {from:{rotation:8}, to:{rotation:2}});
morph("#ar-v", "@wide", @tw, 0.7, {ease:"back.out(1.6)"});
ink(".ar-a", @tw, 0.3);
tl.set("#ar-w", {opacity:1}, @tw2); pop("#ar-w", @tw2, {from:{rotation:-15, scale:1.5}, to:{rotation:-6}});
""", ts=tss - 0.2, tb=tbv - 0.2, tw=twi - 0.1, tw2=twi + 0.3, wide=WIDE))

# 7 PRESSURE — blood dots stream through the wide vessel; a gauge needle swings up
s = "pressure"; twb = aw(s, "warm blood"); tpr = aw(s, "pressure"); d7 = SC[s]["slot"]
rnd = random.Random(24)
dots = "".join(f'<circle cx="{x:.0f}" cy="{rnd.uniform(395, 505):.0f}" r="{rnd.uniform(13, 20):.0f}" fill="#B8323A" stroke="{K}" stroke-width="3"/>' for x in range(-700, 960, 55))
scenes[s] = scene_file(s, f"""
#pr-svg {{ position:absolute; left:0; top:150px; }}
#pr-c {{ position:absolute; left:0; right:0; top:170px; text-align:center; opacity:0; }}
#pr-dots {{ opacity:0; }}
""", f"""
  <div id="pr-c"><span class="chip" style="background:#FFC9C2">more warm blood</span></div>
  <svg id="pr-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    <defs><clipPath id="pr-clip"><path d="{WIDE}"/></clipPath></defs>
    <path d="{WIDE}" fill="{BLOOD}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <g clip-path="url(#pr-clip)"><g id="pr-dots">{dots}</g></g>
    <path d="{WIDE}" fill="none" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <g transform="translate(780,700)">
      <path d="M-120,0 A120,120 0 0 1 120,0" stroke="{K}" stroke-width="7" fill="#FFFFFF"/>
      <path d="M60,-104 A120,120 0 0 1 120,0" stroke="{C['red']}" stroke-width="16" fill="none"/>
      <g id="pr-nd"><path d="M0,0 L0,-100" stroke="{K}" stroke-width="8" stroke-linecap="round"/></g>
      <circle r="14" fill="{K}"/>
    </g>
    <text x="780" y="750" text-anchor="middle" style="{GH}font-size:46px">pressure</text>
  </svg>
""", J("""
tl.fromTo("#pr-dots", {opacity:0}, {opacity:1, duration:0.3}, 0.1);
tl.fromTo("#pr-dots", {x:0}, {x:700, duration:@dd, ease:"none"}, 0.1);
tl.set("#pr-c", {opacity:1}, @tw); pop("#pr-c .chip", @tw, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo("#pr-nd", {rotation:-70, svgOrigin:"0 0"}, {rotation:-70, svgOrigin:"0 0", duration:0.01}, 0);
tl.to("#pr-nd", {rotation:55, svgOrigin:"0 0", duration:0.8, ease:"back.out(2)"}, @tp);
""", dd=max(1.0, d7 + 0.4), tw=twb - 0.2, tp=tpr - 0.2))

# 8 FOREHEAD — the mouth nerves are wired to the forehead: referred pain
s = "forehead"; twr = aw(s, "share wiring"); tup = aw(s, "up there"); trp = aw(s, "referred pain")
scenes[s] = scene_file(s, f"""
#fh-svg {{ position:absolute; left:0; top:200px; }}
#fh-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#fh-t {{ position:absolute; left:110px; top:780px; opacity:0; }}
""", f"""
  <div id="fh-c"><span class="chip" style="background:#FFF3C4">shared wiring</span></div>
  <svg id="fh-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    {head("fh")}
    <ellipse cx="705" cy="440" rx="110" ry="40" fill="{ICE}" opacity=".85"/>
    <circle cx="700" cy="425" r="20" fill="{NERVE}" stroke="{K}" stroke-width="5"/>
    <path id="fh-w" d="M700,425 Q640,330 700,260 Q740,215 770,200" stroke="{NERVE}" stroke-width="10" fill="none" stroke-linecap="round" stroke-dasharray="1 0"/>
    <path class="fh-z" d="M700,150 L720,120 L740,150 L760,120 L780,150 L800,120 L820,150" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path class="fh-z" d="M820,190 L860,180" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path class="fh-z" d="M815,225 L860,235" stroke="{C['red']}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="fh-t"><span class="chip" style="background:{ICE};font-size:62px;transform:rotate(-4deg)">referred pain</span></div>
""", J("""
tl.set("#fh-pal", {stroke:"@blue"}, 0);
ink("#fh-w", @tw, 0.9);
tl.set("#fh-c", {opacity:1}, @tw); pop("#fh-c .chip", @tw, {from:{rotation:-10}, to:{rotation:-3}});
ink(".fh-z", @tu, 0.25, {stagger:0.1});
tl.set("#fh-t", {opacity:1}, @tr); pop("#fh-t .chip", @tr, {from:{rotation:-14, scale:1.4}, to:{rotation:-4}});
""", tw=twr - 0.2, tu=tup - 0.4, tr=trp - 0.2, blue=C['blue']))

# 9 FADE — the vessel morphs back to thin; the pain bar drains
s = "fade"; tna = aw(s, "narrows"); tfa = aw(s, "fades"); tse = aw(s, "in seconds")
scenes[s] = scene_file(s, f"""
#fd-svg {{ position:absolute; left:0; top:150px; }}
#fd-c {{ position:absolute; left:0; right:0; top:170px; text-align:center; opacity:0; }}
#fd-pl {{ position:absolute; left:250px; top:690px; {GH} font-size:50px; }}
""", f"""
  <div id="fd-c"><span class="chip" style="background:{ICE}">gone in seconds</span></div>
  <svg id="fd-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    <path id="fd-v" d="{WIDE}" fill="{BLOOD}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <rect x="420" y="560" width="520" height="70" rx="14" fill="#FFFFFF" stroke="{K}" stroke-width="6"/>
    <rect id="fd-bar" x="430" y="570" width="500" height="50" rx="8" fill="{C['red']}"/>
  </svg>
  <div id="fd-pl">pain</div>
""", J("""
morph("#fd-v", "@thin", @tn, 0.8);
tl.fromTo("#fd-bar", {scaleX:1, svgOrigin:"430 595"}, {scaleX:0.03, svgOrigin:"430 595", duration:1.2, ease:"power2.inOut"}, @tf);
tl.set("#fd-c", {opacity:1}, @ts); pop("#fd-c .chip", @ts, {from:{rotation:-10}, to:{rotation:-3}});
""", tn=tna - 0.2, tf=tfa - 0.2, ts=tse - 0.2, thin=THIN))

# 10 TIP — tongue presses against the palate and warms it
s = "tip"; tqt = aw(s, "quick tip"); tto = aw(s, "your tongue"); twa = aw(s, "warm it")
scenes[s] = scene_file(s, f"""
#tp-svg {{ position:absolute; left:0; top:200px; }}
#tp-c {{ position:absolute; left:0; right:0; top:150px; text-align:center; opacity:0; }}
#tp-glow {{ opacity:0; }}
""", f"""
  <div id="tp-c"><span class="chip" style="background:#FFF3C4">tip: tongue to the roof</span></div>
  <svg id="tp-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    {head("tp")}
    <ellipse id="tp-cold" cx="705" cy="440" rx="110" ry="40" fill="{ICE}" opacity=".85"/>
    <ellipse id="tp-glow" cx="705" cy="440" rx="125" ry="50" fill="#FFB36B" opacity=".8"/>
  </svg>
""", J("""
tl.set("#tp-pal", {stroke:"@blue"}, 0);
tl.set("#tp-c", {opacity:1}, @tq); pop("#tp-c .chip", @tq, {from:{rotation:-10}, to:{rotation:-3}});
morph("#tp-tg", "M600,470 Q700,428 795,465", @tt, 0.5, {ease:"back.out(1.6)"});
tl.to("#tp-cold", {opacity:0, duration:0.6}, @tw);
tl.fromTo("#tp-glow", {opacity:0}, {opacity:0.8, duration:0.6}, @tw);
tl.to("#tp-pal", {stroke:"@red", duration:0.5}, @tw);
""", tq=tqt - 0.1, tt=tto - 0.1, tw=twa - 0.3, blue=C['blue'], red=C['red']))

# 11 OUTRO — callback: not freezing, warming you up (Max centre stage, keep y < 620)
s = "outro"; tnf = aw(s, "not freezing"); twu = aw(s, "warm you"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; }}
#ou-b {{ position:absolute; left:0; right:0; top:290px; text-align:center; opacity:0; }}
#ou-x {{ position:absolute; left:0; top:150px; }}
#ou-sc {{ top:420px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:54px;background:{ICE}">brain freezing</span></div>
  <svg id="ou-x" width="{W}" height="120" data-layout-ignore><path id="ou-st" d="M330,70 L750,45" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/></svg>
  <div id="ou-b"><span class="chip" style="font-size:54px;background:#FFC9C2">warming you up!</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a .chip", 0.1, {from:{rotation:-10}, to:{rotation:-3}});
ink("#ou-st", @tn, 0.4);
tl.set("#ou-b", {opacity:1}, @tw); pop("#ou-b .chip", @tw, {from:{rotation:10}, to:{rotation:3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", tn=tnf - 0.1, tw=twu - 0.5, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "why does"), SC["guess"]["start"] + 0.2)
point(g("guess", "brain freezing"), 3.0)
wave(g("intro", "I'm Max"))
point(g("palate", "palate"), 1.2)
point(g("nerves", "bundle of"), 1.2)
wow(g("artery", "suddenly widen"), 1.4)
point(g("pressure", "pressure"), 1.0)
think(g("forehead", "share wiring"), g("forehead", "up there"))
wow(g("forehead", "referred pain"), 1.2)
point(g("tip", "your tongue"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "brain freeze"), 0.35), ("impact-bass-1.mp3", A("hook", "forehead") - 0.1, 0.4),
        ("pop.mp3", A("guess", "brain freezing"), 0.45), ("pop.mp3", A("guess", "your nerves"), 0.45), ("pop.mp3", A("guess", "your blood"), 0.5),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("palate", "roof of"), 0.45),
        ("ping.mp3", A("nerves", "bundle of"), 0.4), ("riser.mp3", A("artery", "blood vessel"), 0.3),
        ("impact-bass-2.mp3", A("artery", "suddenly widen"), 0.45), ("click-soft.mp3", A("forehead", "referred pain"), 0.45),
        ("ping.mp3", A("tip", "your tongue"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
