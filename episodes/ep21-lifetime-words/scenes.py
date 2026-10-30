# MAX WISE ep21 — How many words will you speak in your lifetime?
# Kit: ink / morph / along helpers; no 3D (no natural 3D hero in this topic).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"

# 1 HOOK — speech bubbles ink themselves around the page
s = "hook"; tf = aw(s, "friends"); tfa = aw(s, "family"); tp = aw(s, "pets"); tq = aw(s, "how many")
def bubble(i, x, y, w, h, txt, fill, tail):
    tx, ty = tail
    return (f'<g id="hk-b{i}"><path class="hk-bo{i}" d="M{x+30},{y} L{x+w-30},{y} Q{x+w},{y} {x+w},{y+30} L{x+w},{y+h-30} Q{x+w},{y+h} {x+w-30},{y+h} '
            f'L{x+w*0.45},{y+h} L{tx},{ty} L{x+w*0.3},{y+h} L{x+30},{y+h} Q{x},{y+h} {x},{y+h-30} L{x},{y+30} Q{x},{y} {x+30},{y} Z" fill="{fill}" {WS.replace("fill=\"none\" ", "")}/>'
            f'<text x="{x+w/2}" y="{y+h/2+18}" text-anchor="middle" style="{GH}font-size:54px" fill="{K}">{txt}</text></g>')
bh = bubble(1, 90, 60, 330, 140, "hi there!", C['hi'], (200, 260)) + bubble(2, 560, 120, 400, 140, "blah blah", "#BFE3F7", (650, 320)) + bubble(3, 250, 380, 380, 140, "good boy!", "#FFC9C2", (360, 580))
scenes[s] = scene_file(s, f"""
#hk-svg {{ position:absolute; left:0; top:140px; }}
#hk-q {{ top:780px; font-size:68px; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>{bh}</svg>
  <div id="hk-q" class="h1">How many words in a <span class="hl">lifetime</span>?</div>
""", J("""
pop("#hk-b1", @t1, {from:{rotation:-8, transformOrigin:"50% 100%"}, to:{rotation:0}});
pop("#hk-b2", @t2, {from:{rotation:8, transformOrigin:"50% 100%"}, to:{rotation:0}});
pop("#hk-b3", @t3, {from:{rotation:-8, transformOrigin:"50% 100%"}, to:{rotation:0}});
rise("#hk-q", @tq);
""", t1=tf - 0.1, t2=tfa - 0.1, t3=tp - 0.1, tq=tq))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "a million"); t2 = aw(s, "a hundred"); t3 = aw(s, "or even")
notes = [("a", "1 million?", -6, 110, C['hi']), ("b", "100 million?", 4, 405, "#BFE3F7"), ("c", "even more?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:62px;line-height:1.05;padding:70px 18px 0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1, t2=t2, t3=t3))

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tc = aw(s, "count")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:410px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="300" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {"".join(f'<path class="in-tl" d="M{300+i*60},{200} L{300+i*60},{270}" {WS}/>' for i in range(4))}
    <path class="in-tl" d="M280,250 L520,220" {WS}/>
    {"".join(f'<path class="in-tl2" d="M{600+i*60},{200} L{600+i*60},{270}" {WS}/>' for i in range(3))}
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count every word!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tc0); ink(".in-tl", @tc, 0.15, {stagger:0.1}); ink(".in-tl2", @tc2, 0.15, {stagger:0.1});
""", tmw=tmw, tu=tmw + 0.3, tc0=tc - 0.5, tc=tc - 0.1, tc2=tc + 0.45))

# 4 MYTH — the popular numbers in pencil, a magnifier draws itself on "check"
s = "myth"; tw = aw(s, "women say"); t20 = aw(s, "twenty thousand"); tm = aw(s, "and men"); t7 = aw(s, "seven thousand"); tch = aw(s, "check")
scenes[s] = scene_file(s, f"""
#my-title {{ top:150px; font-size:70px; color:{C['muted']}; }}
#my-a {{ position:absolute; left:110px; top:290px; width:400px; height:300px; }}
#my-b {{ position:absolute; left:570px; top:290px; width:400px; height:300px; }}
#my-a div, #my-b div {{ position:absolute; left:0; right:0; text-align:center; {GH} }}
.my-who {{ top:30px; font-size:56px; }}
.my-n {{ top:110px; font-size:96px; color:{C['pencil']}; }}
.my-d {{ top:220px; font-size:40px; color:{C['muted']}; }}
#my-svg {{ position:absolute; left:380px; top:600px; }}
""", f"""
  <div id="my-title" class="h1">"Everyone knows..."</div>
  <div id="my-a" class="card"><div class="my-who">women</div><div class="my-n">20,000</div><div class="my-d">words a day?</div></div>
  <div id="my-b" class="card"><div class="my-who">men</div><div class="my-n">7,000</div><div class="my-d">words a day?</div></div>
  <svg id="my-svg" width="320" height="300" viewBox="0 0 320 300" data-layout-ignore>
    <circle id="my-glass" cx="130" cy="120" r="90" fill="#E6F3FB" fill-opacity=".6" stroke="{K}" stroke-width="9"/>
    <path id="my-handle" d="M196,186 L290,280" stroke="{K}" stroke-width="22" fill="none" stroke-linecap="round"/>
  </svg>
""", J("""
rise("#my-title", @tt);
pop("#my-a", @ta, {from:{rotation:-10}, to:{rotation:-3}}); pop("#my-b", @tb, {from:{rotation:10}, to:{rotation:3}});
tl.fromTo("#my-a .my-n", {scale:0.6}, {scale:1, duration:0.3, ease:"back.out(2)"}, @t20);
tl.fromTo("#my-b .my-n", {scale:0.6}, {scale:1, duration:0.3, ease:"back.out(2)"}, @t7);
ink("#my-glass", @tch, 0.5); ink("#my-handle", @tch2, 0.25);
tl.fromTo("#my-svg", {rotation:-10}, {rotation:6, duration:0.6, yoyo:true, repeat:1, ease:"sine.inOut", transformOrigin:"40% 40%"}, @tch3);
""", tt=tw - 0.6, ta=tw, tb=tm, t20=t20, t7=t7, tch=tch - 0.6, tch2=tch - 0.1, tch3=tch + 0.2))

# 5 STUDY — 400 students as a dot grid, then a timeline with a 30 s blip every 12.5 min
s = "study"; trec = aw(s, "tiny recorders"); t400 = aw(s, "four hundred"); t125 = aw(s, "twelve and a half"); t30 = aw(s, "thirty seconds")
dots = "".join(f'<circle class="st-d" cx="{30+i%20*42}" cy="{30+i//20*20}" r="7" fill="{C["blue"] if (i*7)%3 else C["red"]}"/>' for i in range(400))
blips = "".join(f'<rect class="st-bl" x="{60+i*190}" y="40" width="30" height="80" fill="{C["red"]}" stroke="{K}" stroke-width="4"/>' for i in range(5))
gaps = "".join(f'<path class="st-gp" d="M{95+i*190},150 Q{170+i*190},185 {245+i*190},150" stroke="{C["blue"]}" stroke-width="5" fill="none" stroke-linecap="round"/>' for i in range(4))
scenes[s] = scene_file(s, f"""
#st-grid {{ position:absolute; left:110px; top:160px; }}
#st-n {{ position:absolute; left:0; right:0; top:590px; text-align:center; }}
#st-tl {{ position:absolute; left:70px; top:680px; }}
#st-l30 {{ position:absolute; left:110px; top:640px; font-size:40px; color:{C['red']}; }}
#st-l125 {{ position:absolute; left:450px; top:870px; font-size:40px; color:{C['blue']}; }}
""", f"""
  <svg id="st-grid" width="860" height="420" viewBox="0 0 860 420" data-layout-ignore>{dots}</svg>
  <div id="st-n"><span class="chip">almost 400 students</span></div>
  <svg id="st-tl" width="960" height="200" viewBox="0 0 960 200" data-layout-ignore>
    <path id="st-line" d="M20,80 L940,80" {WS}/>{blips}{gaps}</svg>
  <div id="st-l30" class="abs">30 s on</div>
  <div id="st-l125" class="abs">every 12.5 min</div>
""", J("""
tl.fromTo(".st-d", {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.15, stagger:{each:0.003, from:"random"}}, @tg);
pop("#st-n .chip", @t400, {from:{rotation:-8}, to:{rotation:-2}});
ink("#st-line", @tl0, 0.6);
ink(".st-gp", @t125, 0.25, {stagger:0.12}); rise("#st-l125", @t125);
tl.fromTo(".st-bl", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.2, ease:"back.out(2)", stagger:0.1}, @t30); rise("#st-l30", @t30);
""", tg=trec - 0.2, t400=t400, tl0=t125 - 0.6, t125=t125, t30=t30 - 0.2))

# 6 RESULT — myth crossed out: both say about 16,000
s = "result"; tres = aw(s, "the result"); twm = aw(s, "women and"); t16 = aw(s, "sixteen thousand"); tbust = aw(s, "myth busted")
scenes[s] = scene_file(s, f"""
#rs-svg {{ position:absolute; left:0; top:150px; }}
#rs-o1 {{ position:absolute; left:170px; top:180px; {GH} font-size:64px; color:{C['pencil']}; }}
#rs-o2 {{ position:absolute; left:690px; top:180px; {GH} font-size:64px; color:{C['pencil']}; }}
#rs-l1 {{ position:absolute; left:180px; top:770px; font-size:48px; }}
#rs-l2 {{ position:absolute; left:720px; top:770px; font-size:48px; }}
#rs-n {{ position:absolute; left:0; right:0; top:320px; text-align:center; }}
#rs-n .big {{ font-size:110px; color:{C['red']}; }}
#rs-st {{ position:absolute; left:300px; top:560px; {GH} font-size:90px; color:{C['red']}; border:7px solid {C['red']}; padding:0 26px; {SKETCH} background:rgba(255,253,246,.9); }}
""", f"""
  <svg id="rs-svg" width="{W}" height="620" viewBox="0 0 {W} 620" data-layout-ignore>
    <path id="rs-x1" d="M150,72 L420,52" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path id="rs-x2" d="M670,72 L900,52" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <rect id="rs-b1" x="190" y="390" width="200" height="210" fill="#FFC9C2" stroke="{K}" stroke-width="5"/>
    <rect id="rs-b2" x="690" y="390" width="200" height="210" fill="#BFE3F7" stroke="{K}" stroke-width="5"/>
  </svg>
  <div id="rs-o1">20,000?</div><div id="rs-o2">7,000?</div>
  <div id="rs-n"><span class="big">≈ 16,000</span><div style="font-size:46px">words a day, each</div></div>
  <div id="rs-l1">women</div><div id="rs-l2">men</div>
  <div id="rs-st">MYTH BUSTED</div>
""", J("""
tl.fromTo("#rs-o1,#rs-o2", {opacity:0}, {opacity:1, duration:0.3}, 0.05);
tl.fromTo("#rs-b1,#rs-b2", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.6, ease:"back.out(1.4)"}, @twm);
rise("#rs-l1", @twm); rise("#rs-l2", @twm);
pop("#rs-n", @t16);
ink("#rs-x1", @tb, 0.3); ink("#rs-x2", @tb2, 0.3);
pop("#rs-st", @tst, {from:{rotation:-25, scale:2}, to:{rotation:-8}});
""", twm=twm - 0.1, t16=t16 - 0.1, tb=tbust - 0.3, tb2=tbust - 0.1, tst=tbust + 0.1))

# 7 HOUR — a sun-to-moon arc; a dot travels it while the hour counter ticks
s = "hour"; t16h = aw(s, "sixteen waking"); t1k = aw(s, "one thousand"); d = SC[s]["slot"]
scenes[s] = scene_file(s, f"""
#hr-svg {{ position:absolute; left:40px; top:170px; }}
#hr-h {{ position:absolute; left:0; right:0; top:560px; text-align:center; {GH} font-size:64px; }}
#hr-n {{ position:absolute; left:0; right:0; top:700px; text-align:center; }}
#hr-n .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <svg id="hr-svg" width="1000" height="560" viewBox="0 0 1000 560" data-layout-ignore>
    <path id="hr-arc" d="M120,470 Q500,-120 880,470" stroke="{C['pencil']}" stroke-width="6" fill="none" stroke-dasharray="14 12"/>
    <g transform="translate(120,470)"><circle r="44" fill="#FFD84A" stroke="{K}" stroke-width="5"/></g>
    <g transform="translate(880,470)"><path d="M-10,-44 A44,44 0 1 0 30,30 A36,36 0 1 1 -10,-44 Z" fill="#E6E2F5" stroke="{K}" stroke-width="5"/></g>
    <g id="hr-dot" transform="translate(120,470)"><circle r="26" fill="#FFFFFF" stroke="{K}" stroke-width="5"/><text y="12" text-anchor="middle" style="{GH}font-size:30px" fill="{K}">blah</text></g>
  </svg>
  <div id="hr-h"><span id="hr-c">0</span> waking hours</div>
  <div id="hr-n"><span class="big">≈ 1,000</span><div style="font-size:50px">words every hour</div></div>
""", J("""
ink("#hr-arc", 0.05, 0.7);
rise("#hr-h", @th);
along("#hr-dot", "#hr-arc", @th, @run, {ease:"none"});
count("#hr-c", 0, 16, @th, @run, v => String(Math.round(v)));
pop("#hr-n", @t1k);
""", th=t16h - 0.2, run=1.6, t1k=t1k - 0.1))

# 8 YEAR — a 12-month calendar fills in tally ticks; total pops
s = "year"; t1y = aw(s, "one year"); t6 = aw(s, "six million")
cells = ""
for i in range(12):
    x, y = 130 + (i % 4) * 210, 170 + (i // 4) * 150
    cells += f'<rect class="yr-c" x="{x}" y="{y}" width="190" height="130" rx="10" fill="#FFFFFF" stroke="{K}" stroke-width="4"/>'
    cells += f'<path class="yr-k" d="M{x+30},{y+95} L{x+80},{y+35} M{x+80},{y+95} L{x+130},{y+35} M{x+130},{y+95} L{x+165},{y+50}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round"/>'
mons = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
ml = "".join(f'<text x="{130+(i%4)*210+12}" y="{170+(i//4)*150+32}" style="{GH}font-size:28px" fill="{C["muted"]}">{m}</text>' for i, m in enumerate(mons))
scenes[s] = scene_file(s, f"""
#yr-svg {{ position:absolute; left:0; top:0; }}
#yr-n {{ position:absolute; left:0; right:0; top:660px; text-align:center; }}
#yr-n .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <svg id="yr-svg" width="{W}" height="660" viewBox="0 0 {W} 660" data-layout-ignore>{cells}{ml}</svg>
  <div id="yr-n"><span class="big">almost 6,000,000</span><div style="font-size:50px">words in a year</div></div>
""", J("""
tl.fromTo(".yr-c", {opacity:0, scale:0.5, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.2, ease:"back.out(2)", stagger:0.05}, 0.05);
ink(".yr-k", @tk, 0.12, {stagger:0.1});
pop("#yr-n", @t6);
""", tk=t1y - 0.2, t6=t6 - 0.2))

# 9 LIFE — a tower of 70 year-bricks grows beside a ruler; counter to about 400 million
s = "life"; t70 = aw(s, "seventy years"); t400 = aw(s, "four hundred")
bricks = "".join(f'<rect class="lf-b" x="{360 + (i % 2) * 6}" y="{770 - (i+1)*9}" width="190" height="8" fill="{["#FFE27A","#BFE3F7","#FFC9C2"][i%3]}" stroke="{K}" stroke-width="2"/>' for i in range(70))
ruler = "".join(f'<path d="M300,{770 - i*90} L{270 if i%2==0 else 282},{770 - i*90}" {WS}/><text x="232" y="{770 - i*90 + 12}" text-anchor="end" style="{GH}font-size:32px" fill="{K}">{i*10}</text>' for i in range(8))
scenes[s] = scene_file(s, f"""
#lf-svg {{ position:absolute; left:0; top:120px; }}
#lf-yl {{ position:absolute; left:140px; top:140px; font-size:40px; color:{C['muted']}; }}
#lf-n {{ position:absolute; left:590px; top:380px; width:460px; text-align:center; }}
#lf-n .big {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <svg id="lf-svg" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>
    <path id="lf-ax" d="M300,780 L300,120" {WS}/>{ruler}{bricks}</svg>
  <div id="lf-yl">years</div>
  <div id="lf-n"><span class="big">≈ 400 million</span><div style="font-size:50px">words</div></div>
""", J("""
ink("#lf-ax", 0.05, 0.5); rise("#lf-yl", 0.3);
tl.fromTo(".lf-b", {opacity:0, x:-40}, {opacity:1, x:0, duration:0.12, stagger:@st}, @tb);
pop("#lf-n", @t400);
""", tb=0.5, st=round(max(0.02, (t70 + 0.6 - 0.5) / 70), 3), t400=t400 - 0.1))

# 10 BOOKS — one novel, then it morphs into a shelf; 40 book icons, 1 icon = 100 novels
s = "books"; tnov = aw(s, "thick novel"); t100k = aw(s, "one hundred thousand"); tfill = aw(s, "could fill"); t4k = aw(s, "four thousand")
rnd = random.Random(21)
icons = ""
for i in range(40):
    r, c = divmod(i, 10)
    x, y = 120 + c * 84 + rnd.uniform(-3, 3), 180 + r * 120
    icons += f'<rect class="bk-i" x="{x:.0f}" y="{y:.0f}" width="58" height="96" rx="5" fill="{["#F28B82","#7DB6E8","#FFE27A","#9BD08F"][i%4]}" stroke="{K}" stroke-width="4"/>'
shelves = "".join(f'<path class="bk-sh" d="M100,{280 + r*120} L980,{280 + r*120}" stroke="#8B5A2B" stroke-width="10" fill="none" stroke-linecap="round"/>' for r in range(4))
scenes[s] = scene_file(s, f"""
#bk-svg {{ position:absolute; left:0; top:0; }}
#bk-one {{ position:absolute; left:0; right:0; top:690px; text-align:center; }}
#bk-n {{ position:absolute; left:0; right:0; top:700px; text-align:center; opacity:0; }}
#bk-n .big {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <svg id="bk-svg" width="{W}" height="700" viewBox="0 0 {W} 700" data-layout-ignore>
    <path id="bk-book" d="M440,220 L640,220 L640,560 L440,560 Z" fill="#F28B82" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>
    <path id="bk-shelf" d="M100,160 L980,160 L980,660 L100,660 Z" fill="none" stroke="none"/>
    <path id="bk-sp" d="M470,300 L610,300 M470,340 L590,340" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    {shelves}{icons}
  </svg>
  <div id="bk-one"><span class="chip">1 novel ≈ 100,000 words</span></div>
  <div id="bk-n"><span class="big">≈ 4,000 novels</span><div style="font-size:42px">1 book = 100 novels</div></div>
""", J("""
pop("#bk-book", @tn, {from:{rotation:-10, transformOrigin:"50% 50%"}, to:{rotation:0}}); ink("#bk-sp", @tn2, 0.4);
pop("#bk-one .chip", @t100);
tl.to("#bk-sp", {opacity:0, duration:0.2}, @tm); tl.to("#bk-one", {opacity:0, duration:0.2}, @tm);
morph("#bk-book", "#bk-shelf", @tm, 0.6, {ease:"back.inOut(1.2)"}); tl.to("#bk-book", {attr:{fill:"#FFF3DD"}, duration:0.5}, @tm);
ink(".bk-sh", @tsh, 0.3, {stagger:0.08});
tl.fromTo(".bk-i", {opacity:0, y:-30}, {opacity:1, y:0, duration:0.15, ease:"back.out(2)", stagger:0.03}, @ti);
tl.set("#bk-n", {opacity:1}, @t4k); pop("#bk-n .big", @t4k); rise("#bk-n div", @t4k2);
""", tn=tnov - 0.2, tn2=tnov + 0.1, t100=t100k, tm=tfill - 0.9, tsh=tfill - 0.3, ti=tfill, t4k=t4k - 0.1, t4k2=t4k + 0.3))

# 11 OUTRO — recap chip (Max centre stage, keep y < 620)
s = "outro"; t400 = aw(s, "four hundred"); tcnt = aw(s, "make them"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:0; right:0; top:170px; text-align:center; }}
#ou-b {{ position:absolute; left:0; right:0; top:290px; text-align:center; }}
#ou-sc {{ top:430px; font-size:110px; }}
""", f"""
  <div id="ou-a"><span class="chip" style="font-size:56px">≈ 400 million words</span></div>
  <div id="ou-b"><span class="chip" style="font-size:52px;background:#FFC9C2">make them count</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
pop("#ou-a .chip", @ta, {from:{rotation:-10}, to:{rotation:-3}}); pop("#ou-b .chip", @tb, {from:{rotation:10}, to:{rotation:3}});
pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", ta=t400 - 0.1, tb=tcnt, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "a million"), 2.6)
wave(g("intro", "I'm Max"))
think(g("myth", "scientists"), SC["study"]["start"])
point(g("study", "four hundred"), 1.2)
wow(g("result", "myth busted"), 1.2)
point(g("hour", "one thousand"), 1.2)
point(g("year", "six million"), 1.2)
wow(g("life", "four hundred"), 1.4)
point(g("books", "four thousand"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "friends"), 0.45), ("pop.mp3", A("hook", "family"), 0.45), ("pop.mp3", A("hook", "pets"), 0.5),
        ("pop.mp3", A("guess", "a million"), 0.5), ("pop.mp3", A("guess", "a hundred"), 0.5), ("pop.mp3", A("guess", "or even"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("myth", "check"), 0.5),
        ("click.mp3", A("study", "thirty seconds"), 0.45), ("impact-bass-1.mp3", A("result", "myth busted") + 0.1, 0.5),
        ("ping.mp3", A("hour", "one thousand"), 0.4), ("click.mp3", A("year", "six million"), 0.45),
        ("impact-bass-2.mp3", A("life", "four hundred"), 0.45), ("pop.mp3", A("books", "four thousand"), 0.5),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
