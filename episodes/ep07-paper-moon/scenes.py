# MAX WISE ep07 — Fold paper 42 times: does it reach the Moon?  Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
def moon_svg(pid, r=80):
    return f'''<svg id="{pid}" width="{2*r+20}" height="{2*r+20}" viewBox="-10 -10 {2*r+20} {2*r+20}" style="overflow:visible" data-layout-ignore>
  <circle cx="{r}" cy="{r}" r="{r}" fill="#ECE8DA" {WSF}/>
  <circle cx="{r*0.65:.0f}" cy="{r*0.7:.0f}" r="{r*0.2:.0f}" fill="none" stroke="{C['pencil']}" stroke-width="4"/>
  <circle cx="{r*1.3:.0f}" cy="{r*1.1:.0f}" r="{r*0.26:.0f}" fill="none" stroke="{C['pencil']}" stroke-width="4"/>
  <circle cx="{r*0.8:.0f}" cy="{r*1.45:.0f}" r="{r*0.12:.0f}" fill="none" stroke="{C['pencil']}" stroke-width="4"/></svg>'''

def sheet_svg(pid, w=260):
    return f'''<svg id="{pid}" width="{w}" height="{w*1.3:.0f}" viewBox="0 0 100 130" data-layout-ignore>
  <path d="M8,6 Q50,3 92,7 L90,124 Q50,127 9,123 Z" fill="#fff" stroke="{K}" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M20,30 L80,30 M20,48 L80,48 M20,66 L80,66 M20,84 L70,84" stroke="{C['rule']}" stroke-width="3"/>
  <path d="M50,8 L50,122" stroke="{C['red']}" stroke-width="3" stroke-dasharray="6 5"/></svg>'''

def stack_html(pid, x, bottom, w, h, label, lab_left=True):
    lines = "".join(f'<div style="height:2px;background:{C["pencil"]};margin-top:{max(3, h/18):.0f}px"></div>' for _ in range(int(min(16, h/8))))
    return (f'<div id="{pid}" class="abs" style="left:{x}px;top:{bottom-h}px;width:{w}px;height:{h}px;background:#fff;border:4px solid {K};{SKETCH}overflow:hidden;transform-origin:50% 100%">{lines}</div>')

# 1 HOOK
s = "hook"; tf = aw(s, "fold a sheet"); t42 = aw(s, "forty two"); trm = aw(s, "reach the moon")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:86px; }}
#hk-sh {{ position:absolute; left:200px; top:520px; }}
#hk-mn {{ position:absolute; left:700px; top:500px; }}
#hk-q2 {{ position:absolute; left:500px; top:740px; width:520px; text-align:center; font-size:72px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">Fold paper in half<br><span class="hl">42 times</span>…</div>
  <div id="hk-sh">{sheet_svg('hk-s', 210)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore><path id="hk-ar" d="M440,640 Q560,520 690,580" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="16 12"/></svg>
  <div id="hk-mn">{moon_svg('hk-m', 95)}</div>
  <div id="hk-q2" class="big">…to the Moon?!</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tf-0.05:.2f}); pop("#hk-sh", {tf+0.3:.2f});
tl.fromTo("#hk-s", {{scaleX:1}}, {{scaleX:0.5, transformOrigin:"0% 50%", duration:0.25, yoyo:true, repeat:3, ease:"power2.inOut"}}, {t42:.2f});
draw("#hk-ar", {trm-0.2:.2f}, 0.4); pop("#hk-mn", {trm:.2f}); pop("#hk-q2", {trm+0.2:.2f}, {{from:{{rotation:6}}, to:{{rotation:-2}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "a house"); t2 = aw(s, "a mountain"); t3 = aw(s, "to the moon")
notes = [("house", "A house?", -6, 110, C['hi']), ("mount", "A<br>mountain?", 4, 405, "#BFE3F7"), ("moon", "The<br>Moon?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:50px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-house", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-mount", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-moon", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's fold")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Fold, step by step!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 THIN — a tenth of a millimeter
s = "thin"; tsh = aw(s, "a sheet"); tte = aw(s, "a tenth")
scenes[s] = scene_file(s, f"""
#th-svg {{ position:absolute; left:120px; top:280px; }}
#th-num {{ position:absolute; left:0; right:0; top:700px; text-align:center; font-size:130px; }}
""", f"""
  <div id="th-title" class="h1" style="top:150px;font-size:74px">Paper is <span class="hl">thin</span></div>
  <svg id="th-svg" width="840" height="380" viewBox="0 0 840 380" data-layout-ignore>
    <path id="th-edge" d="M40,190 Q300,186 520,191" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <g id="th-mag"><circle cx="640" cy="170" r="120" fill="#F4FAFD" stroke="{K}" stroke-width="7"/>
      <path d="M560,160 L720,160 L720,180 L560,180 Z" fill="#fff" stroke="{K}" stroke-width="4"/>
      <path d="M740,110 L740,230 M728,160 L752,160 M728,180 L752,180" stroke="{C['red']}" stroke-width="4" stroke-linecap="round"/>
      <path d="M545,255 L470,330" stroke="{K}" stroke-width="16" stroke-linecap="round"/></g></svg>
  <div id="th-num" class="big">≈ <span class="red">0.1</span> mm</div>
""", f"""
rise("#th-title", 0.0); draw("#th-edge", {tsh:.2f}, 0.4); pop("#th-mag", {tsh+0.5:.2f});
pop("#th-num", {tte:.2f});
""")

# 5 DOUBLE — 2, 4, 8 layers
s = "double"; tdb = aw(s, "doubles"); t2 = aw(s, "two layers"); t4 = aw(s, "then four"); t8 = aw(s, "then eight")
def layers(pid, n, x):
    hh = 26
    rows = "".join(f'<div style="height:{hh}px;margin-top:4px;background:#fff;border:3px solid {K};border-radius:6px"></div>' for _ in range(n))
    return (f'<div id="{pid}" class="abs" style="left:{x}px;top:{760-n*(hh+4)}px;width:220px;opacity:0">{rows}'
            f'<div class="big" style="text-align:center;font-size:72px;margin-top:14px">{n}</div></div>')
scenes[s] = scene_file(s, "", f"""
  <div id="db-title" class="h1" style="top:150px;font-size:74px">Each fold <span class="hl">doubles</span> it</div>
  {layers('db-2', 2, 120)}{layers('db-4', 4, 430)}{layers('db-8', 8, 740)}
  <div id="db-x1" class="abs big red" style="left:345px;top:560px;font-size:64px;opacity:0">×2</div>
  <div id="db-x2" class="abs big red" style="left:655px;top:560px;font-size:64px;opacity:0">×2</div>
""", f"""
rise("#db-title", {tdb-0.4:.2f}); pop("#db-2", {t2:.2f}); pop("#db-x1", {t4-0.15:.2f}); pop("#db-4", {t4:.2f});
pop("#db-x2", {t8-0.15:.2f}); pop("#db-8", {t8:.2f});
""")

# 6 TEN — hand width
s = "ten"; t10 = aw(s, "ten folds"); tcm = aw(s, "ten centimeters"); thd = aw(s, "your hand")
scenes[s] = scene_file(s, f"""
#te-hand {{ position:absolute; left:470px; top:300px; }}
#te-num {{ position:absolute; left:0; right:0; top:760px; text-align:center; font-size:90px; }}
""", f"""
  <div id="te-title" class="h1" style="top:150px;font-size:80px"><span class="hl">10 folds</span></div>
  {stack_html('te-st', 220, 680, 170, 340, '')}
  <svg id="te-hand" width="440" height="400" viewBox="0 0 220 200" data-layout-ignore>
    <path d="M40,190 L40,95 Q40,80 52,80 Q62,80 62,95 L62,40 Q62,26 74,26 Q86,26 86,40 L86,30 Q86,16 98,16 Q110,16 110,30 L110,38 Q110,24 122,24 Q134,24 134,38 L134,60 Q134,48 146,48 Q158,48 158,62 L158,140 Q158,190 110,190 Z" fill="#FFE8D6" {WSF}/>
    <path d="M62,95 L62,120 M86,40 L86,110 M110,38 L110,110 M134,60 L134,112" stroke="{K}" stroke-width="3" opacity=".5"/>
    <path id="te-ruler" d="M30,10 L30,195" stroke="{C['red']}" stroke-width="5" stroke-dasharray="10 8"/></svg>
  <div id="te-num" class="big">≈ <span class="red">10 cm</span> thick</div>
""", f"""
pop("#te-title", {t10:.2f}); tl.fromTo("#te-st", {{scaleY:0}}, {{scaleY:1, duration:0.6, ease:"power2.out"}}, {t10+0.2:.2f});
pop("#te-num", {tcm:.2f}); pop("#te-hand", {thd:.2f});
""")

# 7 TWENTY — taller than a building
s = "twenty"; t20 = aw(s, "twenty folds"); t100 = aw(s, "one hundred"); tbg = aw(s, "big building")
win = "".join(f'<rect x="{30+c*45}" y="{40+r*42}" width="22" height="24" fill="#BFE3F7" stroke="{K}" stroke-width="3"/>' for r in range(11) for c in range(3))
scenes[s] = scene_file(s, f"""
#tw-bld {{ position:absolute; left:560px; top:390px; }}
#tw-num {{ position:absolute; left:0; right:0; top:860px; text-align:center; font-size:84px; }}
#tw-num {{ left:420px; }}
""", f"""
  <div id="tw-title" class="h1" style="top:150px;font-size:80px"><span class="hl">20 folds</span></div>
  {stack_html('tw-st', 420, 840, 90, 560, '')}
  <svg id="tw-bld" width="180" height="450" viewBox="0 0 180 500" data-layout-ignore><path d="M10,495 L10,20 L170,20 L170,495" fill="#fff" {WSF}/>{win}</svg>
  <div id="tw-num" class="big">≈ <span class="red">100 m</span> tall!</div>
""", f"""
pop("#tw-title", {t20:.2f}); pop("#tw-bld", {t20+0.1:.2f});
tl.fromTo("#tw-st", {{scaleY:0}}, {{scaleY:1, duration:0.9, ease:"power2.out"}}, {t20+0.3:.2f});
pop("#tw-num", {t100:.2f}); tl.fromTo("#tw-st", {{x:0}}, {{x:6, duration:0.06, yoyo:true, repeat:5}}, {tbg:.2f});
""")

# 8 THIRTY — past the edge of space
s = "thirty"; t30 = aw(s, "thirty folds"); tov = aw(s, "over one hundred"); ted = aw(s, "edge of space")
stars = "".join(f'<path d="M{x},{y-10} L{x},{y+10} M{x-10},{y} L{x+10},{y}" stroke="{C["hi"]}" stroke-width="4" stroke-linecap="round"/>' for x, y in [(160, 220), (300, 330), (820, 250), (930, 400), (700, 200), (520, 290)])
scenes[s] = scene_file(s, f"""
#tt-sky {{ position:absolute; left:80px; top:150px; width:920px; height:700px; background:#2B3256; border:4px solid {K}; {SKETCH} overflow:hidden; }}
#tt-num {{ position:absolute; left:560px; top:320px; width:420px; text-align:center; font-size:86px; color:#fff; }}
#tt-lab {{ position:absolute; left:560px; top:520px; width:420px; text-align:center; font-size:44px; color:{C['hi']}; }}
#tt-t {{ position:absolute; left:120px; top:180px; font-family:'Gochi Hand',cursive; font-size:70px; color:#fff; }}
""", f"""
  <div id="tt-sky">
    <svg class="abs" style="left:-80px;top:-150px" width="{W}" height="960" data-layout-ignore>{stars}
      <path d="M-20,900 Q540,700 1100,900 L1100,1000 L-20,1000 Z" fill="#7FC8A9" stroke="{K}" stroke-width="5"/>
      <path id="tt-edge" d="M80,600 L1000,600" stroke="{C['hi']}" stroke-width="5" stroke-dasharray="18 12"/></svg>
  </div>
  <div id="tt-t"><span class="hl" style="color:{K}">30 folds</span></div>
  {stack_html('tt-st', 380, 820, 70, 520, '')}
  <div id="tt-num" class="big">&gt; 100 km</div>
  <div id="tt-lab">— edge of space —</div>
""", f"""
rise("#tt-sky", 0.0); pop("#tt-t", {t30:.2f});
tl.fromTo("#tt-st", {{scaleY:0}}, {{scaleY:1, duration:1.0, ease:"power2.out"}}, {t30+0.2:.2f});
pop("#tt-num", {tov:.2f}); draw("#tt-edge", {ted-0.2:.2f}, 0.5); rise("#tt-lab", {ted:.2f});
""")

# 9 MOON — 440,000 km vs 384,000 km
s = "moon"; t42 = aw(s, "forty two"); t440 = aw(s, "four hundred forty"); t384 = aw(s, "three hundred eighty"); tpast = aw(s, "shoot right past")
EX, MX = 250, 850; L440 = EX + (MX - EX) * 440 / 384
scenes[s] = scene_file(s, f"""
#mn-e {{ position:absolute; left:90px; top:470px; }}
#mn-m {{ position:absolute; left:{MX-50}px; top:535px; }}
#mn-l1 {{ position:absolute; left:250px; top:380px; width:{L440-EX:.0f}px; text-align:center; font-size:62px; color:{C['red']}; }}
#mn-l2 {{ position:absolute; left:250px; top:700px; width:600px; text-align:center; font-size:58px; color:{C['blue']}; }}
#mn-bar {{ position:absolute; left:{EX}px; top:470px; width:{L440-EX:.0f}px; height:44px; border:4px solid {C['red']}; {SKETCH} transform-origin:0 50%; }}
#mn-past {{ position:absolute; left:300px; right:0; top:775px; text-align:center; font-size:58px; }}
""", f"""
  <div id="mn-title" class="h1" style="top:150px;font-size:80px"><span class="hl">42 folds</span></div>
  <svg id="mn-e" width="170" height="170" viewBox="0 0 170 170" data-layout-ignore><circle cx="85" cy="85" r="78" fill="#BFE3F7" {WSF}/>
    <path d="M40,60 Q60,40 80,58 Q90,80 66,92 Q48,100 40,60 Z M100,100 Q130,90 140,116 Q120,140 100,124 Z" fill="#7FC8A9" stroke="{K}" stroke-width="4"/></svg>
  <div id="mn-m">{moon_svg('mn-mo', 50)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" data-layout-ignore>
    <path id="mn-d" d="M{EX},670 L{MX},670 M{EX},650 L{EX},690 M{MX},650 L{MX},690" stroke="{C['blue']}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>
  <div id="mn-bar" class="hatch-r"></div>
  <div id="mn-l1" class="big">≈ 440,000 km</div>
  <div id="mn-l2" class="big">Moon: ≈ 384,000 km</div>
  <div id="mn-past"><span class="pill red">right past the Moon!</span></div>
""", f"""
pop("#mn-title", {t42-0.2:.2f}); pop("#mn-e", 0.1);
tl.fromTo("#mn-bar", {{scaleX:0}}, {{scaleX:1, duration:1.2, ease:"power2.inOut"}}, {t440-0.2:.2f}); pop("#mn-l1", {t440+0.6:.2f});
pop("#mn-m", {t384-0.3:.2f}); draw("#mn-d", {t384:.2f}, 0.6); rise("#mn-l2", {t384+0.3:.2f});
pop("#mn-past span", {tpast:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 10 RECORD — 12 folds in 2001
s = "record"; tfb = aw(s, "fights back"); t12 = aw(s, "just twelve"); t01 = aw(s, "two thousand one"); tkm = aw(s, "over a kilometer")
scenes[s] = scene_file(s, f"""
#rc-crump {{ position:absolute; left:400px; top:270px; }}
#rc-12 {{ position:absolute; left:0; right:0; top:500px; text-align:center; font-size:110px; }}
#rc-yr {{ position:absolute; left:120px; top:660px; font-size:64px; transform:rotate(-4deg); }}
#rc-km {{ position:absolute; left:500px; top:660px; width:480px; text-align:center; font-size:56px; }}
""", f"""
  <div id="rc-title" class="h1" style="top:150px;font-size:74px">Real paper <span class="hl">fights back</span></div>
  <svg id="rc-crump" width="280" height="200" viewBox="0 0 140 100" data-layout-ignore>
    <path d="M14,70 L30,30 L52,46 L70,14 L92,40 L120,24 L128,66 L102,88 L70,74 L40,92 Z" fill="#fff" {WSF}/>
    <path d="M30,30 L40,92 M70,14 L70,74 M92,40 L102,88" stroke="{K}" stroke-width="3" opacity=".5"/></svg>
  <div id="rc-12" class="big">record: <span class="red">12</span> folds</div>
  <div id="rc-yr" class="chip">2001</div>
  <div id="rc-km" class="big">paper strip<br><span class="blue">&gt; 1 km</span> long</div>
""", f"""
rise("#rc-title", {tfb-0.5:.2f}); pop("#rc-crump", {tfb:.2f}, {{from:{{rotation:-30}}, to:{{rotation:0}}}});
pop("#rc-12", {t12:.2f}); pop("#rc-yr", {t01:.2f}, {{from:{{rotation:-15}}, to:{{rotation:-4}}}}); pop("#rc-km", {tkm:.2f});
""")

# 11 OUTRO
s = "outro"; tfy = aw(s, "forty two"); top_ = aw(s, "on paper"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:160px; font-size:84px; }}
#ou-b {{ top:370px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">42 folds</span> = the Moon</div>
  <div id="ou-b" class="h1">…at least on paper!</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tfy:.2f}); rise("#ou-b", {top_:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "here's"), g("hook", "reach the moon"))
point(g("guess", "a house"), 3.0)
wave(g("intro", "I'm Max"))
point(g("thin", "a tenth"), 1.2)
point(g("double", "two layers"), 2.2)
point(g("ten", "ten centimeters"), 1.2)
wow(g("twenty", "big building"), 1.2)
point(g("thirty", "edge of space"), 1.2)
wow(g("moon", "shoot right past"), 1.4)
think(g("record", "fights back"), g("record", "just twelve"))
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "reach the moon"), 0.35), ("pop.mp3", A("guess", "a house"), 0.5), ("pop.mp3", A("guess", "a mountain"), 0.5),
        ("pop.mp3", A("guess", "to the moon"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click-soft.mp3", A("double", "two layers"), 0.5), ("click-soft.mp3", A("double", "then four"), 0.5), ("click-soft.mp3", A("double", "then eight"), 0.5),
        ("impact-bass-1.mp3", A("thirty", "edge of space"), 0.4), ("impact-bass-2.mp3", A("moon", "shoot right past"), 0.45),
        ("pop.mp3", A("record", "just twelve"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
