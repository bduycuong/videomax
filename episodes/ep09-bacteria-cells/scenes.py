# MAX WISE ep09 — Are you more bacteria than human?  Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"

def bug(x, y, rot=0, s=1.0, pid=""):
    """bacterium capsule doodle"""
    i = f' id="{pid}"' if pid else ""
    return (f'<g{i}><g transform="translate({x:.0f},{y:.0f}) rotate({rot:.0f}) scale({s})"><rect x="-22" y="-11" width="44" height="22" rx="11" fill="{PINK}" stroke="{C["red"]}" stroke-width="4"/>'
            f'<path d="M22,0 Q32,-6 38,2" stroke="{C["red"]}" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="-6" cy="-2" r="3" fill="{C["red"]}"/></g></g>')

def cell(x, y, s=1.0, pid=""):
    """human cell doodle"""
    i = f' id="{pid}"' if pid else ""
    return (f'<g{i}><g transform="translate({x:.0f},{y:.0f}) scale({s})"><path d="M-24,0 Q-24,-23 0,-24 Q25,-22 24,0 Q23,24 0,24 Q-25,23 -24,0 Z" fill="{SKY}" stroke="{C["blue"]}" stroke-width="4"/>'
            f'<circle cx="3" cy="-2" r="8" fill="{C["blue"]}"/></g></g>')

def balance_svg(pid, w=760):
    """balance: #pid-beam rotates about svgOrigin 380 150; left pan blue (human), right pan red (bacteria)"""
    lp = "".join(cell(170 + (k % 4) * 34 - 50, 250 - (k // 4) * 30, 0.62) for k in range(10))
    rp = "".join(bug(590 + (k % 4) * 34 - 50, 250 - (k // 4) * 26, (k * 37) % 60 - 30, 0.62) for k in range(13))
    return f'''<svg id="{pid}" width="{w}" height="{w*0.6:.0f}" viewBox="0 0 760 456" style="overflow:visible" data-layout-ignore>
  <path d="M380,150 L380,420 M290,428 Q380,420 470,429" {WS}/>
  <g id="{pid}-beam">
    <path d="M110,150 Q380,142 650,151" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M110,150 L60,280 M110,150 L160,280 M650,150 L600,280 M650,150 L700,280" stroke="{K}" stroke-width="3"/>
    <path d="M40,280 Q110,320 180,280 Z" fill="#fff" {WSF}/><path d="M580,280 Q650,320 720,280 Z" fill="#fff" {WSF}/>
    {lp}{rp}
    <text x="110" y="360" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{C['blue']}">human</text>
    <text x="650" y="360" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{C['red']}">bacteria</text></g>
  <circle cx="380" cy="150" r="12" fill="{K}"/></svg>'''

# 1 HOOK — more bacteria than human?
s = "hook"; tpl = aw(s, "people love"); tmb = aw(s, "more bacteria"); ttr = aw(s, "is that true")
rb = random.Random(3)
bugs_h = "".join(bug(rb.uniform(-60, 60), rb.uniform(-170, 190), rb.uniform(0, 180), 0.8, f"hk-b{k}") for k in range(16))
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:84px; }}
#hk-body {{ position:absolute; left:360px; top:450px; }}
#hk-qm {{ position:absolute; left:720px; top:520px; font-size:150px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">More <span class="hl">bacteria</span><br>than human?</div>
  <svg id="hk-body" width="360" height="500" viewBox="-180 -230 360 500" data-layout-ignore>
    <circle cx="0" cy="-185" r="42" fill="#fff" {WSF}/>
    <path d="M-60,-130 Q0,-140 60,-130 L95,40 L60,48 L52,-40 L50,250 L10,250 L0,90 L-10,250 L-50,250 L-52,-40 L-60,48 L-95,40 Z" fill="#fff" {WSF}/>
    {bugs_h}</svg>
  <div id="hk-qm" class="big">?!</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tpl:.2f}); pop("#hk-body", {tpl+0.3:.2f});
for (let k=0;k<16;k++) tl.fromTo("#hk-b"+k, {{opacity:0, scale:0.2, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.2, ease:"back.out(2)"}}, {tmb:.2f}+k*0.06);
pop("#hk-qm", {ttr:.2f}, {{from:{{rotation:20}}, to:{{rotation:6}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t10 = aw(s, "ten bacteria"); t11 = aw(s, "one for one"); twf = aw(s, "way fewer")
notes = [("ten", "10 : 1?", -6, 110, C['hi']), ("one", "1 : 1?", 4, 405, "#BFE3F7"), ("few", "Way<br>fewer?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:62px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
  <div id="gs-sub" class="h2" style="top:700px">bacteria : human cells</div>
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-ten", {t10:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); rise("#gs-sub", {t10+0.4:.2f});
pop("#gs-one", {t11:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-few", {twf:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "let's count")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count cells!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tct:.2f});
""")

# 4 MYTH — the 1972 guess
s = "myth"; t101 = aw(s, "ten to one"); trg = aw(s, "rough guess"); t72 = aw(s, "nineteen seventy two"); tnb = aw(s, "nobody really"); tdc = aw(s, "decades")
scenes[s] = scene_file(s, f"""
#my-num {{ position:absolute; left:0; right:0; top:260px; text-align:center; font-size:250px; color:{C['pencil']}; }}
#my-tag {{ position:absolute; left:620px; top:560px; width:340px; height:180px; background:{C['hi']}; border:4px solid {K}; {SKETCH} transform:rotate(5deg); text-align:center; font-family:'Gochi Hand',cursive; font-size:54px; line-height:1.1; padding-top:12px; }}
#my-stamp {{ position:absolute; left:120px; top:770px; width:840px; text-align:center; }}
#my-stamp span {{ font-size:58px; color:{C['red']}; }}
""", f"""
  <div id="my-title" class="h1" style="top:150px;font-size:72px">The famous <span class="hl">10 to 1</span></div>
  <div id="my-num" class="big">10 : 1</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore><path id="my-q" d="M200,560 Q240,520 280,560 Q320,600 360,560" stroke="{C['pencil']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="my-tag">a rough guess<br>from 1972</div>
  <div id="my-stamp"><span class="pill">unchecked for decades</span></div>
""", f"""
rise("#my-title", 0.0);
tl.fromTo("#my-num", {{opacity:0, clipPath:"inset(0 100% 0 0)"}}, {{opacity:1, clipPath:"inset(0 0% 0 0)", duration:0.7, ease:"power1.inOut"}}, {t101:.2f});
draw("#my-q", {trg:.2f}, 0.4);
pop("#my-tag", {t72-0.2:.2f}, {{from:{{rotation:-15}}, to:{{rotation:5}}}});
tl.fromTo("#my-stamp span", {{opacity:0, scale:2.2, rotation:-14}}, {{opacity:1, scale:1, rotation:-4, duration:0.25, ease:"power3.in"}}, {tdc-0.3:.2f});
""")

# 5 HUMAN — 30 trillion human cells, 1 dot = 1 trillion
s = "human"; t16 = aw(s, "twenty sixteen"); trc = aw(s, "recounted"); tad = aw(s, "a typical adult"); t30 = aw(s, "thirty trillion")
grid = "".join(cell(250 + (k % 6) * 116, 330 + (k // 6) * 100, 1.3, f"hu-c{k}") for k in range(30))
scenes[s] = scene_file(s, f"""
#hu-yr {{ position:absolute; left:670px; top:150px; font-size:52px; transform:rotate(5deg); }}
#hu-key {{ position:absolute; left:110px; top:160px; font-size:46px; }}
#hu-num {{ position:absolute; left:400px; top:830px; width:640px; text-align:center; font-size:70px; white-space:nowrap; }}
""", f"""
  <div id="hu-yr" class="pill">2016 recount</div>
  <div id="hu-key" class="abs"><svg width="60" height="56" viewBox="-30 -28 60 56" style="vertical-align:middle" data-layout-ignore>{cell(0, 0, 1)}</svg> = 1 trillion cells</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore>{grid}</svg>
  <div id="hu-num" class="big"><span id="hu-n" class="blue">0</span> trillion <span class="hl">human</span></div>
""", f"""
pop("#hu-yr", {t16:.2f}, {{from:{{rotation:20}}, to:{{rotation:5}}}}); rise("#hu-key", {trc:.2f});
for (let k=0;k<30;k++) tl.fromTo("#hu-c"+k, {{opacity:0, scale:0.2, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.18, ease:"back.out(2)"}}, {tad:.2f}+k*0.07);
rise("#hu-num", {tad:.2f}); count("#hu-n", 0, 30, {tad:.2f}, {t30-tad+0.4:.2f}, v => String(Math.round(v)));
""")

# 6 BLOOD — red blood cells flowing (cutaway vein)
s = "blood"; trb = aw(s, "red blood cells"); tzp = aw(s, "zipping")
rr = random.Random(11)
discs = "".join(f'<g id="bl-d{k}"><ellipse cx="0" cy="0" rx="34" ry="24" fill="{C["red"]}" stroke="{K}" stroke-width="3"/><ellipse cx="0" cy="0" rx="14" ry="9" fill="#F28B80"/></g>' for k in range(14))
starts = [(rr.uniform(0, 1), rr.uniform(-70, 70)) for _ in range(14)]
scenes[s] = scene_file(s, f"""
#bl-lab {{ position:absolute; left:120px; top:780px; width:840px; text-align:center; }}
#bl-lab span {{ font-size:60px; }}
""", f"""
  <div id="bl-title" class="h1" style="top:150px;font-size:72px">Mostly <span class="hl">red blood cells</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore>
    <path d="M60,380 Q540,350 1020,380 M60,600 Q540,630 1020,600" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M60,380 Q540,350 1020,380 L1020,600 Q540,630 60,600 Z" fill="#FFE8E4" stroke="none"/>
    <path d="M60,380 Q540,350 1020,380 M60,600 Q540,630 1020,600" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M110,380 Q90,490 110,600" stroke="{K}" stroke-width="4" fill="none" stroke-dasharray="10 8"/>
    <g id="bl-flow">{discs}</g></svg>
  <div id="bl-lab"><span class="pill red">tiny, and everywhere</span></div>
""", f"""
rise("#bl-title", {trb-0.6:.2f});
const st = {json.dumps(starts)}; const o = {{p:0}};
const place = () => {{ for (let k=0;k<14;k++) {{ const u=((st[k][0]+o.p)%1); document.querySelector("#bl-d"+k).setAttribute("transform", `translate(${{120+u*880}},${{490+st[k][1]}}) rotate(${{u*720+k*40}})`); }} }}; place();
tl.fromTo("#bl-flow", {{opacity:0}}, {{opacity:1, duration:0.3}}, {trb:.2f});
tl.to(o, {{p:0.6, duration:{tzp-trb:.2f}, ease:"none", onUpdate:place}}, {trb:.2f});
tl.to(o, {{p:2.2, duration:{SC[s]['slot']-tzp:.2f}, ease:"power1.in", onUpdate:place}}, {tzp:.2f});
pop("#bl-lab span", {tzp:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 7 BUGS — 38 trillion bacteria, same key
s = "bugs"; tbq = aw(s, "and the bacteria"); t38 = aw(s, "thirty eight"); tgut = aw(s, "mostly living")
gb = "".join(bug(200 + (k % 8) * 96, 330 + (k // 8) * 96, (k * 47) % 70 - 35, 1.3, f"bg-b{k}") for k in range(38))
scenes[s] = scene_file(s, f"""
#bg-key {{ position:absolute; left:110px; top:160px; font-size:46px; }}
#bg-num {{ position:absolute; left:400px; top:830px; width:640px; text-align:center; font-size:70px; white-space:nowrap; }}
#bg-gut {{ position:absolute; left:590px; white-space:nowrap; top:150px; font-size:50px; transform:rotate(5deg); }}
""", f"""
  <div id="bg-key" class="abs"><svg width="80" height="40" viewBox="-40 -20 80 40" style="vertical-align:middle" data-layout-ignore>{bug(0, 0, 0, 1)}</svg> = 1 trillion bacteria</div>
  <div id="bg-gut" class="pill red">mostly in the gut</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore>{gb}</svg>
  <div id="bg-num" class="big"><span id="bg-n" class="red">0</span> trillion <span class="hl">bacteria</span></div>
""", f"""
rise("#bg-key", {tbq:.2f});
for (let k=0;k<38;k++) tl.fromTo("#bg-b"+k, {{opacity:0}}, {{opacity:1, duration:0.12}}, {t38-0.5:.2f}+k*0.035);
rise("#bg-num", {t38-0.5:.2f}); count("#bg-n", 0, 38, {t38-0.5:.2f}, 1.4, v => String(Math.round(v)));
pop("#bg-gut", {tgut:.2f}, {{from:{{rotation:20}}, to:{{rotation:5}}}});
""")

# 8 RATIO — balance nearly level; 10:1 struck, 1.3:1
s = "ratio"; trr = aw(s, "real ratio"); t11 = aw(s, "one to one"); t13 = aw(s, "one point three")
scenes[s] = scene_file(s, f"""
#ra-bal {{ position:absolute; left:160px; top:400px; }}
#ra-old {{ position:absolute; left:140px; top:180px; width:360px; text-align:center; font-size:110px; color:{C['pencil']}; }}
#ra-new {{ position:absolute; left:520px; top:180px; width:440px; text-align:center; font-size:110px; }}
""", f"""
  <div id="ra-old" class="big">10 : 1</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="400" data-layout-ignore><path id="ra-x" d="M150,300 Q330,230 500,190" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/></svg>
  <div id="ra-new" class="big"><span class="hl">≈ 1.3 : 1</span></div>
  <div id="ra-bal">{balance_svg('ra-b', 760)}</div>
""", f"""
rise("#ra-old", 0.0); pop("#ra-bal", {trr-0.2:.2f});
tl.set("#ra-b-beam", {{rotation:0, svgOrigin:"380 150"}}, 0);
tl.fromTo("#ra-b-beam", {{rotation:-14}}, {{rotation:4, duration:1.2, ease:"elastic.out(1,0.4)"}}, {trr:.2f});
draw("#ra-x", {t11:.2f}, 0.3);
pop("#ra-new", {t13:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 9 WEIGHT — less than half a pound
s = "weight"; tsm = aw(s, "so small"); tall = aw(s, "all of them"); thp = aw(s, "half a pound")
small = "".join(bug(-40 + (k % 4) * 28, -30 + (k // 4) * 22, k * 40, 0.55) for k in range(12))
scenes[s] = scene_file(s, f"""
#wt-sc {{ position:absolute; left:300px; top:270px; }}
#wt-lab {{ position:absolute; left:440px; top:810px; width:560px; text-align:center; }}
#wt-lab span {{ font-size:72px; }}
""", f"""
  <div id="wt-title" class="h1" style="top:150px;font-size:72px">All bacteria, <span class="hl">weighed</span></div>
  <svg id="wt-sc" width="480" height="520" viewBox="0 0 240 260" style="overflow:visible" data-layout-ignore>
    <g id="wt-bag"><path d="M80,40 Q120,22 160,40 Q178,92 160,110 Q120,120 80,110 Q62,92 80,40 Z" fill="#fff" {WSF}/>
      <path d="M96,34 Q120,14 144,34" {WS}/><g transform="translate(120,78)">{small}</g></g>
    <path d="M50,116 L190,116" stroke="{K}" stroke-width="8" stroke-linecap="round"/>
    <path d="M30,130 Q120,124 210,131 L204,250 Q120,254 36,249 Z" fill="#fff" {WSF}/>
    <circle cx="120" cy="190" r="44" fill="#FFFDF6" stroke="{K}" stroke-width="4"/>
    {''.join(f'<path d="M120,150 L120,158" transform="rotate({-90+i*30} 120 190)" stroke="{K}" stroke-width="3"/>' for i in range(7))}
    <g id="wt-needle"><path d="M120,190 L120,154" stroke="{C['red']}" stroke-width="5" stroke-linecap="round"/></g>
    <circle cx="120" cy="190" r="5" fill="{K}"/></svg>
  <div id="wt-lab"><span class="pill red">&lt; ½ pound</span></div>
""", f"""
rise("#wt-title", 0.0); pop("#wt-sc", 0.1); tl.set("#wt-needle", {{rotation:-90, svgOrigin:"120 190"}}, 0);
tl.fromTo("#wt-bag", {{y:-160, opacity:0}}, {{y:0, opacity:1, duration:0.45, ease:"bounce.out"}}, {tall-0.3:.2f});
tl.to("#wt-needle", {{rotation:-40, duration:0.6, ease:"elastic.out(1,0.5)"}}, {tall+0.1:.2f});
pop("#wt-lab span", {thp:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 10 FLUSH — one bathroom trip tips the balance
s = "flush"; tfp = aw(s, "funny part"); tcl = aw(s, "so close"); tbt = aw(s, "bathroom"); tth = aw(s, "toward human")
scenes[s] = scene_file(s, f"""
#fl-bal {{ position:absolute; left:160px; top:400px; }}
#fl-pf {{ position:absolute; left:0; right:0; top:200px; text-align:center; font-size:150px; color:{C['blue']}; opacity:0; }}
""", f"""
  <div id="fl-title" class="h1" style="top:150px;font-size:72px">Here's the <span class="hl">funny part</span></div>
  <div id="fl-pf" class="big">FLUSH!</div>
  <div id="fl-bal">{balance_svg('fl-b', 760)}</div>
""", f"""
rise("#fl-title", {tfp-0.3:.2f}); pop("#fl-bal", 0.1);
tl.set("#fl-b-beam", {{rotation:4, svgOrigin:"380 150"}}, 0);
tl.to("#fl-b-beam", {{rotation:2, duration:0.15, yoyo:true, repeat:5, ease:"sine.inOut"}}, {tcl:.2f});
tl.to("#fl-title", {{opacity:0, duration:0.2}}, {tbt-0.3:.2f});
tl.fromTo("#fl-pf", {{opacity:0, scale:0.4, rotation:-14}}, {{opacity:1, scale:1, rotation:-4, duration:0.3, ease:"back.out(2.5)"}}, {tbt:.2f});
tl.to("#fl-b-beam", {{rotation:-9, duration:0.8, ease:"elastic.out(1,0.5)"}}, {tth-0.2:.2f});
""")

# 11 OUTRO
s = "outro"; tnm = aw(s, "not mostly"); thh = aw(s, "you're roughly"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:80px; }}
#ou-b {{ position:absolute; left:0; right:0; top:330px; text-align:center; }}
#ou-b .big {{ font-size:84px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">Not mostly bacteria…</div>
  <div id="ou-b"><div class="big"><span class="blue">human</span> <span class="hl">½ + ½</span> <span class="red">bacteria</span></div></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
rise("#ou-a", {tnm:.2f}); pop("#ou-b", {thh:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "is that true"), SC["guess"]["start"] + 0.2)
point(g("guess", "ten bacteria"), 3.6)
wave(g("intro", "I'm Max"))
point(g("myth", "ten to one"), 1.2)
think(g("myth", "nobody really"), g("myth", "decades") + 0.8)
point(g("human", "thirty trillion"), 1.4)
point(g("blood", "red blood"), 1.2)
wow(g("bugs", "thirty eight"), 1.4)
point(g("ratio", "one point three"), 1.4)
point(g("weight", "half a pound"), 1.2)
wow(g("flush", "bathroom"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "more bacteria"), 0.45), ("ping.mp3", A("hook", "is that true"), 0.35),
        ("pop.mp3", A("guess", "ten bacteria"), 0.5), ("pop.mp3", A("guess", "one for one"), 0.5), ("pop.mp3", A("guess", "way fewer"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("impact-bass-2.mp3", A("myth", "decades") - 0.05, 0.4),
        ("click-soft.mp3", A("human", "thirty trillion"), 0.55), ("riser.mp3", A("bugs", "thirty eight") - 0.6, 0.3),
        ("click.mp3", A("ratio", "one to one"), 0.5), ("pop.mp3", A("ratio", "one point three"), 0.5),
        ("click-soft.mp3", A("weight", "all of them"), 0.5), ("impact-bass-1.mp3", A("flush", "bathroom"), 0.45),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
