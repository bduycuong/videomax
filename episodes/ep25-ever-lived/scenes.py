# MAX WISE ep25 — How many humans have ever lived on Earth?
# Kit: ink / along helpers; 2D only (no three.js today). Source: PRB, "How Many People Have Ever Lived on Earth?" (2022).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKY = "#BFE3F7"; LIVE = "#E8574A"

def stick(x, y, s, cls, color=None, sw=5, head_fill="none", extra=""):
    """stick person standing with feet at (x, y), height ~ 100*s; every stroke its own <path> so ink() draws it cleanly"""
    col = color or K
    hr = 13 * s; hy = y - 100 * s + hr
    st = f'stroke="{col}" stroke-width="{sw}" fill="none" stroke-linecap="round" class="{cls}" {extra}'
    return (f'<circle cx="{x:.1f}" cy="{hy:.1f}" r="{hr:.1f}" stroke="{col}" stroke-width="{sw}" fill="{head_fill}" class="{cls}" {extra}/>'
            f'<path d="M{x:.1f},{hy + hr:.1f} L{x:.1f},{y - 38*s:.1f}" {st}/>'
            f'<path d="M{x - 22*s:.1f},{y - 70*s:.1f} L{x:.1f},{y - 60*s:.1f} L{x + 22*s:.1f},{y - 70*s:.1f}" {st}/>'
            f'<path d="M{x - 18*s:.1f},{y:.1f} L{x:.1f},{y - 38*s:.1f} L{x + 18*s:.1f},{y:.1f}" {st}/>')

# 1 HOOK — a row of stick people inks itself in; a big question mark
s = "hook"; thu = aw(s, "humans"); tea = aw(s, "earth"); tev = aw(s, "everyone ever")
row = "".join(stick(120 + i * 105, 620, 1.6, "hk-p", sw=6) for i in range(9))
scenes[s] = scene_file(s, f"""
#hk-t {{ top:160px; font-size:84px; line-height:1.05; }}
#hk-svg {{ position:absolute; left:0; top:180px; }}
#hk-q {{ position:absolute; left:0; right:0; top:820px; text-align:center; opacity:0; }}
""", f"""
  <div id="hk-t" class="h1">How many <span class="hl">ever</span> lived?</div>
  <svg id="hk-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <path id="hk-gr" d="M60,630 Q540,615 1020,632" stroke="{C['pencil']}" stroke-width="5" fill="none" stroke-linecap="round"/>
    {row}
  </svg>
  <div id="hk-q"><span class="chip" style="font-size:58px">everyone, ever</span></div>
""", J("""
pop("#hk-t", @t0, {from:{scale:1.4}, to:{}});
ink("#hk-gr", @t1, 0.5);
ink(".hk-p", @t2, 0.25, {stagger:0.03});
tl.set("#hk-q", {opacity:1}, @tev); pop("#hk-q .chip", @tev, {from:{rotation:-12}, to:{rotation:-3}});
""", t0=max(0.05, thu - 0.5), t1=thu, t2=thu + 0.3, tev=tev - 0.1))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "ten billion"); t2 = aw(s, "fifty billion"); t3 = aw(s, "or more")
notes = [("a", "10 billion?", -6, 110, C['hi']), ("b", "50 billion?", 4, 405, SKY), ("c", "more than 100 billion?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:60px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.1, t2=t2 - 0.1, t3=t3 - 0.1))

# 3 INTRO — logo + tally marks ink themselves
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "count")
tally = "".join(f'<path class="in-tl" d="M{x},20 L{x + 6},120" stroke="{C["blue"]}" stroke-width="8" fill="none" stroke-linecap="round"/>' for g0 in (330, 590) for x in range(g0, g0 + 160, 38))
tally += "".join(f'<path class="in-tl" d="M{g0 - 20},100 L{g0 + 170},40" stroke="{C["red"]}" stroke-width="8" fill="none" stroke-linecap="round"/>' for g0 in (330, 590))
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:62px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Count everyone!</span></div>
  <svg class="abs" style="left:0;top:500px" width="{W}" height="150" data-layout-ignore>{tally}</svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tc); ink(".in-tl", @tc, 0.12, {stagger:0.07});
""", tmw=tmw, tu=tmw + 0.3, tc=tct - 0.3))

# 4 START — timeline; a little walker travels from 190,000 years ago to today
s = "start"; t190 = aw(s, "one hundred ninety"); tmh = aw(s, "modern humans"); d4 = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#st-svg {{ position:absolute; left:0; top:200px; }}
#st-c {{ position:absolute; left:0; right:0; top:170px; text-align:center; opacity:0; }}
.st-l {{ position:absolute; {GH} font-size:46px; opacity:0; }}
#st-l1 {{ left:60px; top:640px; width:360px; }} #st-l2 {{ left:860px; top:640px; }}
""", f"""
  <div id="st-c"><span class="chip">the count starts here</span></div>
  <svg id="st-svg" width="{W}" height="500" viewBox="0 0 {W} 500" data-layout-ignore>
    <path id="st-line" d="M110,360 L960,360" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="st-ar" d="M930,335 L965,360 L930,385" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="st-t1" d="M110,330 L110,390" stroke="{C['red']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="st-t2" d="M900,330 L900,390" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="st-walk" d="M110,350 L900,350" fill="none" stroke="none"/>
    <path id="st-trail" d="M110,350 L900,350" stroke="{C['hi']}" stroke-width="22" fill="none" stroke-linecap="round" opacity=".8"/>
    <g id="st-man">{stick(0, 0, 1.3, "st-mp", sw=6, head_fill="#FFFFFF")}</g>
  </svg>
  <div id="st-l1" class="st-l" style="color:{C['red']}">190,000 years ago</div>
  <div id="st-l2" class="st-l" style="color:{C['blue']}">today</div>
""", J("""
ink("#st-line", 0.1, 0.6); ink("#st-ar", 0.6, 0.2); ink("#st-t2", 0.7, 0.2);
tl.to("#st-l2", {opacity:1, duration:0.2}, 0.8);
ink("#st-t1", @t190, 0.3); tl.set("#st-l1", {opacity:1}, @t190); pop("#st-l1", @t190);
tl.set("#st-c", {opacity:1}, @t190b); pop("#st-c .chip", @t190b, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo("#st-man", {opacity:0}, {opacity:1, duration:0.2}, @tmh);
along("#st-man", "#st-walk", @tmh, @dw, {ease:"power1.inOut"});
tl.fromTo("#st-trail", {drawSVG:"0%"}, {drawSVG:"100%", duration:@dw, ease:"power1.inOut"}, @tmh);
""", t190=t190 - 0.1, t190b=t190 + 0.6, tmh=tmh - 0.2, dw=max(1.2, d4 - (tmh - 0.2) - 0.6)))

# 5 TINY — Earth with a handful of dots: 10,000 years ago, about 5 million people
s = "tiny"; t10 = aw(s, "ten thousand"); tfa = aw(s, "farming"); t5 = aw(s, "five million")
rnd = random.Random(5); dots = ""
for i in range(14):
    a = rnd.uniform(0, 2 * math.pi); r = 200 * math.sqrt(rnd.uniform(0.05, 0.85))
    dots += f'<circle class="tn-d" cx="{540 + r*math.cos(a):.0f}" cy="{330 + r*math.sin(a):.0f}" r="9" fill="{LIVE}" stroke="{K}" stroke-width="3"/>'
scenes[s] = scene_file(s, f"""
#tn-y {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#tn-svg {{ position:absolute; left:0; top:200px; }}
#tn-f {{ position:absolute; left:760px; top:300px; opacity:0; }}
#tn-n {{ position:absolute; left:0; right:0; top:790px; text-align:center; opacity:0; padding-left:200px; }}
#tn-n .big {{ font-size:70px; }}
""", f"""
  <div id="tn-y"><span class="chip">10,000 years ago</span></div>
  <svg id="tn-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <circle id="tn-e" cx="540" cy="330" r="240" fill="{SKY}" stroke="{K}" stroke-width="7"/>
    <path d="M400,200 Q470,150 540,200 Q590,250 520,300 Q450,330 420,280 Z" fill="#9BD08F" stroke="{K}" stroke-width="5"/>
    <path d="M590,360 Q680,330 700,400 Q690,470 610,470 Q560,430 590,360 Z" fill="#9BD08F" stroke="{K}" stroke-width="5"/>
    {dots}
  </svg>
  <div id="tn-f"><span class="chip" style="background:#FFF3C4">farming begins</span></div>
  <div id="tn-n"><span class="big">about <span class="hl">5 million</span> people</span></div>
""", J("""
pop("#tn-y .chip", @t10, {from:{rotation:-12}, to:{rotation:-3}});
tl.fromTo("#tn-svg", {opacity:0, scale:0.7, transformOrigin:"50% 55%"}, {opacity:1, scale:1, duration:0.5, ease:"back.out(1.6)"}, @te);
tl.set("#tn-f", {opacity:1}, @tfa); pop("#tn-f .chip", @tfa, {from:{rotation:12}, to:{rotation:4}});
tl.fromTo(".tn-d", {opacity:0, scale:0, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, ease:"back.out(3)", stagger:0.05}, @td);
tl.set("#tn-n", {opacity:1}, @t5); pop("#tn-n .big", @t5);
""", t10=t10 - 0.1, te=t10 + 0.2, tfa=tfa - 0.1, td=t5 - 0.9, t5=t5 - 0.1))

# 6 BIRTHS — seeded baby dots drop into a big jar and pile up (simulate)
s = "births"; tba = aw(s, "babies"); tgn = aw(s, "thousands of"); d6 = SC[s]["slot"]
rnd = random.Random(25); drops = ""; N6 = 70
cols = 12
for i in range(N6):
    cx = 330 + (i % cols) * 38 + (19 if (i // cols) % 2 else 0) + rnd.uniform(-3, 3)
    cy = 640 - (i // cols) * 34
    drops += f'<circle class="bt-d" cx="{min(cx, 770):.0f}" cy="{cy:.0f}" r="16" fill="{["#F2B8A0","#FFE27A","#BFE3F7","#C9E7B8"][i % 4]}" stroke="{K}" stroke-width="3"/>'
scenes[s] = scene_file(s, f"""
#bt-svg {{ position:absolute; left:0; top:150px; }}
#bt-c {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#bt-g {{ position:absolute; left:0; right:0; top:860px; text-align:center; opacity:0; }}
""", f"""
  <div id="bt-c"><span class="chip">every birth counts</span></div>
  <svg id="bt-svg" width="{W}" height="720" viewBox="0 0 {W} 720" data-layout-ignore>
    {drops}
    <path id="bt-jar" d="M300,180 L300,660 Q300,690 330,690 L770,690 Q800,690 800,660 L800,180" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="bt-rim" d="M270,180 L830,180" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="bt-g"><span class="chip" style="background:#FFF3C4">generation after generation</span></div>
""", J("""
ink("#bt-jar", 0.05, 0.6); ink("#bt-rim", 0.5, 0.25);
tl.set("#bt-c", {opacity:1}, @tba); pop("#bt-c .chip", @tba, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo(".bt-d", {opacity:0, y:-560}, {opacity:1, y:0, duration:0.45, ease:"bounce.out", stagger:@stg}, @tba2);
tl.set("#bt-g", {opacity:1}, @tgn); pop("#bt-g .chip", @tgn, {from:{rotation:10}, to:{rotation:3}});
""", tba=tba - 0.1, tba2=tba + 0.1, stg=max(0.03, (d6 - tba - 1.2) / N6), tgn=tgn - 0.8))

# 7 TOTAL — the jar again, full; a counter climbs to about 117 billion
s = "total"; tad = aw(s, "add up"); t117 = aw(s, "one hundred seventeen")
full = "".join(f'<circle cx="{330 + (i % 12) * 38 + (19 if (i // 12) % 2 else 0):.0f}" cy="{640 - (i // 12) * 34}" r="16" fill="{["#F2B8A0","#FFE27A","#BFE3F7","#C9E7B8"][i % 4]}" stroke="{K}" stroke-width="3"/>' for i in range(168))
scenes[s] = scene_file(s, f"""
#tt-svg {{ position:absolute; left:140px; top:130px; }}
#tt-n {{ position:absolute; left:0; right:0; top:800px; text-align:center; font-size:96px; }}
#tt-svg circle {{ opacity:0; }}
""", f"""
  <svg id="tt-svg" width="800" height="650" viewBox="0 0 {W} 720" data-layout-ignore>
    {full}
    <path d="M300,180 L300,660 Q300,690 330,690 L770,690 Q800,690 800,660 L800,180" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M270,180 L830,180" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="tt-n" class="big"><span id="tt-v" class="hl">0</span></div>
""", J("""
tl.to("#tt-svg circle", {opacity:1, duration:0.1, stagger:{each:@ea, from:"start"}}, @tad);
count("#tt-v", 0, 117, @tad, @dc, v => "about " + Math.round(v) + " billion");
pop("#tt-n", @t117, {from:{scale:1.3}, to:{}});
""", tad=tad - 0.1, ea=max(0.004, (t117 - tad + 0.3) / 168), dc=max(0.8, t117 - tad + 0.4), t117=t117 + 0.4))

# 8 RANGE — honest estimate: a shaded band and an error bar around 117 billion
s = "range"; tom = aw(s, "other methods"); tro = aw(s, "rough estimate")
xs = "".join(f'<path class="rg-x" d="M{x-14},{y-14} L{x+14},{y+14} M{x+14},{y-14} L{x-14},{y+14}" stroke="{C["blue"]}" stroke-width="6" fill="none" stroke-linecap="round"/>' for x, y in [(330, 300), (470, 250), (640, 310), (760, 260)])
scenes[s] = scene_file(s, f"""
#rg-svg {{ position:absolute; left:0; top:200px; }}
#rg-n {{ position:absolute; left:0; right:0; top:170px; text-align:center; }}
#rg-n .big {{ font-size:96px; }}
#rg-c {{ position:absolute; left:0; right:0; top:760px; text-align:center; opacity:0; }}
""", f"""
  <div id="rg-n"><span class="big">about 117 billion</span></div>
  <svg id="rg-svg" width="{W}" height="520" viewBox="0 0 {W} 520" data-layout-ignore>
    <rect id="rg-band" x="250" y="190" width="580" height="180" fill="{C['hi']}" fill-opacity=".5" stroke="{K}" stroke-width="5" stroke-dasharray="16 10"/>
    <path id="rg-bar" d="M250,280 L830,280" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="rg-c1" d="M250,240 L250,320" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="rg-c2" d="M830,240 L830,320" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <circle id="rg-dot" cx="560" cy="280" r="24" fill="{LIVE}" stroke="{K}" stroke-width="5"/>
    {xs}
    <text x="540" y="450" text-anchor="middle" style="{GH}font-size:48px" fill="{C['muted']}">other methods</text>
  </svg>
  <div id="rg-c"><span class="chip" style="background:#FFFFFF;font-size:60px">rough estimate</span></div>
""", J("""
pop("#rg-dot", 0.1); ink("#rg-bar", 0.3, 0.5); ink("#rg-c1", 0.7, 0.2); ink("#rg-c2", 0.7, 0.2);
tl.fromTo("#rg-band", {opacity:0}, {opacity:1, duration:0.4}, @tom);
tl.fromTo("#rg-svg text", {opacity:0}, {opacity:1, duration:0.3}, @tom);
ink(".rg-x", @tom2, 0.2, {stagger:0.15});
tl.set("#rg-c", {opacity:1}, @tro); pop("#rg-c .chip", @tro, {from:{rotation:-10}, to:{rotation:-3}});
""", tom=tom - 0.1, tom2=tom + 0.4, tro=tro - 0.2))

# 9 SHARE — 100 stick people; only 7 are coloured in (alive today)
s = "share"; t8 = aw(s, "eight billion"); t7 = aw(s, "seven percent")
rnd = random.Random(7); live = set(rnd.sample(range(100), 7))
grid = ""
for i in range(100):
    x = 300 + (i % 10) * 72; y = 340 + (i // 10) * 46
    if i in live: grid += f'<g class="sh-on" id="sh-on{i}">{stick(x, y, 0.36, "sh-lp", color=LIVE, sw=4, head_fill=LIVE)}</g>'
    else: grid += stick(x, y, 0.36, "sh-p", color=C["pencil"], sw=3)
scenes[s] = scene_file(s, f"""
#sh-svg {{ position:absolute; left:0; top:150px; }}
#sh-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#sh-n {{ position:absolute; left:0; right:0; top:260px; text-align:center; opacity:0; }}
#sh-n .big {{ color:{LIVE}; font-size:96px; }}
.sh-on {{ opacity:0; }}
""", f"""
  <div id="sh-a"><span class="chip" style="background:#FFC9C2">8 billion alive today</span></div>
  <div id="sh-n"><span class="big">only about 7%</span></div>
  <svg id="sh-svg" width="{W}" height="760" viewBox="0 0 {W} 760" data-layout-ignore>
    {grid}
  </svg>
""", J("""
ink(".sh-p", 0.1, 0.2, {stagger:0.008});
tl.set("#sh-a", {opacity:1}, @t8); pop("#sh-a .chip", @t8, {from:{rotation:-10}, to:{rotation:-3}});
tl.fromTo(".sh-on", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1.25, duration:0.3, ease:"back.out(3)", stagger:0.12}, @t8b);
tl.set("#sh-n", {opacity:1}, @t7); pop("#sh-n .big", @t7, {from:{scale:1.5}, to:{}});
""", t8=t8 - 0.1, t8b=t8 + 0.3, t7=t7 - 0.2))

# 10 BEFORE — one coloured person; fourteen pencil people ink in behind
s = "before"; tfo = aw(s, "fourteen"); tal = aw(s, "alive right")
ghosts = "".join(stick(150 + (i % 7) * 95, 470 + (i // 7) * 190, 1.4, "bf-g", color=C['pencil'], sw=5) for i in range(14))
scenes[s] = scene_file(s, f"""
#bf-svg {{ position:absolute; left:0; top:160px; }}
#bf-n {{ position:absolute; left:0; right:0; top:160px; text-align:center; opacity:0; }}
#bf-n .big {{ font-size:96px; }}
#bf-y {{ position:absolute; left:820px; top:750px; opacity:0; }}
""", f"""
  <div id="bf-n"><span class="big"><span class="hl">14</span> came before</span></div>
  <svg id="bf-svg" width="{W}" height="720" viewBox="0 0 {W} 720" data-layout-ignore>
    {ghosts}
    <g id="bf-me">{stick(930, 560, 2.2, "bf-mp", color=LIVE, sw=8, head_fill="#FFC9C2")}</g>
  </svg>
  <div id="bf-y"><span class="chip" style="background:#FFC9C2">alive now</span></div>
""", J("""
pop("#bf-me", @tal, {from:{y:40}, to:{}});
tl.set("#bf-y", {opacity:1}, @tal2); pop("#bf-y .chip", @tal2, {from:{rotation:10}, to:{rotation:3}});
ink(".bf-g", @tfo, 0.12, {stagger:0.012});
tl.set("#bf-n", {opacity:1}, @tfo); pop("#bf-n .big", @tfo);
""", tal=tal - 0.2, tal2=tal + 0.2, tfo=tfo - 0.2))

# 11 OUTRO — callback: more than 100 billion humans... and you (Max centre stage, keep y < 620)
s = "outro"; thb = aw(s, "hundred billion"); tom = aw(s, "one of them"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:160px; text-align:center; }}
#ou-b {{ position:absolute; left:0; right:0; top:280px; text-align:center; opacity:0; }}
#ou-sc {{ top:420px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:54px;background:{SKY}">100+ billion humans</span></div>
  <div id="ou-b"><span class="chip" style="font-size:54px;background:#FFC9C2">...and you!</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a .chip", @ta, {from:{rotation:-10}, to:{rotation:-3}});
tl.set("#ou-b", {opacity:1}, @tb); pop("#ou-b .chip", @tb, {from:{rotation:10}, to:{rotation:3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", ta=thb - 0.3, tb=tom - 0.2, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "ten billion"), 3.0)
wave(g("intro", "I'm Max"))
point(g("start", "modern humans"), 1.4)
point(g("tiny", "five million"), 1.2)
think(g("births", "but babies"), g("births", "thousands of"))
wow(g("total", "one hundred seventeen"), 1.4)
think(g("range", "other methods"), g("range", "rough estimate"))
wow(g("share", "seven percent"), 1.2)
point(g("before", "fourteen"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "everyone ever"), 0.35),
        ("pop.mp3", A("guess", "ten billion"), 0.45), ("pop.mp3", A("guess", "fifty billion"), 0.45), ("pop.mp3", A("guess", "or more"), 0.5),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("start", "one hundred ninety"), 0.45),
        ("ping.mp3", A("tiny", "five million"), 0.4), ("riser.mp3", A("total", "add up"), 0.3),
        ("impact-bass-1.mp3", A("total", "one hundred seventeen") + 0.4, 0.45), ("click-soft.mp3", A("range", "rough estimate"), 0.45),
        ("ping.mp3", A("share", "seven percent"), 0.45), ("pop.mp3", A("before", "fourteen"), 0.4),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
