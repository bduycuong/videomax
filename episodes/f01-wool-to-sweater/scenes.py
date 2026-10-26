# Wool → sweater: doodle overlays on real footage. Footage panel sits at x 20–1060, y 230–898.
# === SCENES ===
PX, PY, PW, PH = 20, 230, 1040, 668
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.sticky {{ position:absolute; width:220px; padding:14px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} }}
"""
def chip(txt): return f'<div class="top"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def arrow(i, d, color=None): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color or C["red"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

s = "hook"; t1 = aw(s, "fluffy"); t2 = aw(s, "smelly"); t3 = aw(s, "cozy sweater")
scenes[s] = scene_file(s, OV + f"#hk-t {{ top:96px; font-size:80px; }}", f"""
  <div id="hk-t" class="h1">From <span class="hl">sheep</span> to <span class="hl">sweater</span>?</div>
  <div id="hk-a" class="sticky" style="left:60px;top:280px;background:{C['hi']};transform:rotate(-6deg)">fluffy</div>
  <div id="hk-b" class="sticky" style="left:800px;top:300px;background:#C9E8C2;transform:rotate(5deg)">smelly!</div>
  {tag('hk-c', 'cozy sweater?', 620, 790)}
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:5}}}});
pop("#hk-c", {t3:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

s = "intro"; tm = aw(s, "I'm Max"); tw = aw(s, "Max Wise"); tf = aw(s, "follow the wool")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-f', 'let&#39;s follow the wool →', 430, 905, 'font-size:50px')}
  {arrow('in-p', 'M80,800 Q300,640 520,760 T980,640')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-f", {tf:.2f}); tl.set("#in-p", {{opacity:1}}, 0); draw("#in-p", {tf+0.2:.2f}, 0.8);
""")

s = "shear"; ts = aw(s, "step one"); tp = aw(s, "one big piece"); th = aw(s, "doesn't hurt")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="sh-c"><span class="chip">STEP 1 · SHEARING</span></div>
  {tag('sh-p', 'one big piece', 640, 300)}
  <div id="sh-n" class="note">doesn't hurt the sheep <span class="blue">✓</span></div>
""", f"""
pop("#sh-c", {ts:.2f}); pop("#sh-p", {tp:.2f}, {{from:{{rotation:8}}, to:{{rotation:-2}}}}); rise("#sh-n", {th:.2f});
""")

s = "raw"; tg = aw(s, "greasy"); tl_ = aw(s, "lanolin"); tsw = aw(s, "sweat"); tdu = aw(s, "dust"); tso = aw(s, "soil"); tse = aw(s, "seeds")
items = [("rw-1", "lanolin (wax)", tl_), ("rw-2", "sweat", tsw), ("rw-3", "dust", tdu), ("rw-4", "soil", tso), ("rw-5", "seeds", tse)]
lst = "".join(f'<div id="{i}" style="font-size:40px;line-height:1.25">• {t}</div>' for i, t, _ in items)
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="rw-c"><span class="chip">RAW WOOL = <span class="red">greasy!</span></span></div>
  <div id="rw-card" class="card" style="left:690px;top:270px;width:340px;padding:18px 24px;font-family:'Gochi Hand',cursive">
    <div style="font-size:42px;margin-bottom:6px" class="red">stuck in it:</div>{lst}</div>
""", f"""
pop("#rw-c", {tg:.2f}); rise("#rw-card", {tl_-0.3:.2f});
{"".join(f'tl.fromTo("#{i}", {{opacity:0, x:-20}}, {{opacity:1, x:0, duration:0.2}}, {t:.2f});' for i, _, t in items)}
""")

s = "scour"; tso_ = aw(s, "sorted"); twa = aw(s, "washed"); tri = aw(s, "rinsed"); tsq = aw(s, "squeezed"); tdr = aw(s, "dried")
steps = [("sc-1", "sort", tso_), ("sc-2", "wash", twa), ("sc-3", "rinse", tri), ("sc-4", "squeeze", tsq), ("sc-5", "dry", tdr)]
row = "".join(tag(i, t, 40 + k * 205, 820, "font-size:40px;padding:0 16px") for k, (i, t, _) in enumerate(steps))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="sc-c"><span class="chip">STEP 2 · WASHING</span></div>
  {row}
  <div id="sc-n" class="note">warm soapy tanks <span class="blue">~~~</span></div>
""", f"""
pop("#sc-c", 0.05); rise("#sc-n", {twa+0.3:.2f});
{"".join(f'pop("#{i}", {t:.2f}, {{from:{{rotation:-12}}, to:{{rotation:{(-1)**k*3}}}}});' for k, (i, _, t) in enumerate(steps))}
""")

s = "lanolin"; tw_ = aw(s, "isn't wasted"); tl2 = aw(s, "into lanolin"); tsk = aw(s, "skin creams")
jar = f'''<svg id="ln-jar" class="abs" style="left:770px;top:400px" width="230" height="260" viewBox="0 0 230 260" data-layout-ignore>
  <rect x="40" y="20" width="150" height="40" rx="10" fill="{C['hi']}" {WS.replace('fill="none" ', '')}/>
  <path d="M30,70 Q115,60 200,70 L196,236 Q115,248 34,236 Z" fill="#FFFFFF" {WS.replace('fill="none" ', '')}/>
  <rect x="58" y="120" width="114" height="64" rx="8" fill="{C['hi']}" stroke="{K}" stroke-width="4"/>
  <text x="115" y="162" text-anchor="middle" font-family="Gochi Hand" font-size="30" fill="{K}">lanolin</text></svg>'''
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="ln-c"><span class="chip">BONUS: <span class="red">not wasted!</span></span></div>
  {jar}
  <div id="ln-n" class="note">→ <span class="hl">skin creams</span></div>
""", f"""
pop("#ln-c", {tw_:.2f}); pop("#ln-jar", {tl2:.2f}, {{from:{{rotation:-15}}, to:{{rotation:0}}}}); rise("#ln-n", {tsk:.2f});
""")

s = "open"; ttg = aw(s, "tangled mess"); tdm = aw(s, "spinning drums"); tap = aw(s, "pulls the clumps")
scribble = "M700,330 " + " ".join(f"Q{720+(i*37)%180},{300+(i*53)%160} {730+(i*61)%170},{320+(i*29)%150}" for i in range(14))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="op-c"><span class="chip">STEP 3 · OPENING</span></div>
  {arrow('op-s', scribble, K)}
  {tag('op-t', 'tangled mess', 700, 500)}
  <div id="op-n" class="note">spinning drums <span class="red">pull it apart</span></div>
""", f"""
pop("#op-c", 0.05); tl.set("#op-s", {{opacity:1}}, 0); draw("#op-s", {ttg:.2f}, 0.6); pop("#op-t", {ttg+0.3:.2f});
rise("#op-n", {tdm:.2f}); tl.to("#op-s, #op-t", {{opacity:0, duration:0.3}}, {tap:.2f});
""")

s = "card"; tc = aw(s, "carding"); tt = aw(s, "wire teeth"); tsw_ = aw(s, "same way"); tsl = aw(s, "sliver")
comb = f'''<svg id="cd-comb" class="abs" style="left:740px;top:290px" width="280" height="150" viewBox="0 0 280 150" data-layout-ignore>
  <rect x="10" y="10" width="260" height="40" rx="10" fill="#FFFFFF" {WS.replace('fill="none" ', '')}/>
  {"".join(f'<path d="M{24+i*20},50 L{24+i*20},120" stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for i in range(12))}</svg>'''
lines = "".join(f'<path id="cd-l{i}" d="M440,{930+i*16} L1020,{930+i*16}" stroke="{C["blue"]}" stroke-width="5" stroke-linecap="round" fill="none"/>' for i in range(4))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="cd-c"><span class="chip">STEP 4 · CARDING</span></div>
  {comb}
  <svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore>{lines}</svg>
  {tag('cd-s', 'sliver', 470, 760)}
""", f"""
pop("#cd-c", {tc:.2f}); pop("#cd-comb", {tt:.2f}, {{from:{{rotation:-10}}, to:{{rotation:0}}}});
{"".join(f'tl.set("#cd-l{i}", {{opacity:1}}, 0); draw("#cd-l{i}", {tsw_:.2f}+{i}*0.12, 0.5);' for i in range(4))}
pop("#cd-s", {tsl:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}});
""")

s = "comb"; tcb = aw(s, "combed again"); tsh = aw(s, "short fibers"); tlo = aw(s, "long ones"); tne = aw(s, "neater fibers")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="cb-c"><span class="chip">STEP 5 · COMBING</span></div>
  {tag('cb-s', 'short fibers', 80, 300)}
  {arrow('cb-x', 'M70,300 L370,372 M370,296 L74,374')}
  {tag('cb-l', 'long + straight <span class="blue">✓</span>', 660, 300)}
  <div id="cb-n" class="note">neater fibers → <span class="hl">smoother yarn</span></div>
""", f"""
pop("#cb-c", {tcb:.2f}); pop("#cb-s", {tsh:.2f}); tl.set("#cb-x", {{opacity:1}}, 0); draw("#cb-x", {tsh+0.6:.2f}, 0.35);
pop("#cb-l", {tlo:.2f}); rise("#cb-n", {tne:.2f});
""")

s = "draft"; tsp = aw(s, "now spinning"); tdf = aw(s, "different speeds"); tth = aw(s, "thinner and thinner")
rolls = "".join(f'<g id="df-r{i}"><circle cx="{120+i*170}" cy="46" r="38" fill="#FFFFFF" {WS.replace(chr(102)+"ill=\"none\" ", "")}/><text x="{120+i*170}" y="122" text-anchor="middle" font-family="Gochi Hand" font-size="30" fill="{K}">{lab}</text></g>' for i, lab in enumerate(["slow", "faster", "fastest"]))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="df-c"><span class="chip">STEP 6 · SPINNING</span></div>
  <svg class="abs" style="left:420px;top:905px" width="640" height="140" data-layout-ignore>
    <path id="df-th" d="M10,46 L120,46 L290,46 L460,46 L620,46" stroke="{C['red']}" stroke-width="16" fill="none" stroke-linecap="round" style="opacity:0"/>
    {rolls}</svg>
""", f"""
pop("#df-c", {tsp:.2f}); {"".join(f'pop("#df-r{i}", {tdf:.2f}+{i}*0.15);' for i in range(3))}
tl.to("#df-th", {{opacity:1, duration:0.2}}, {tth-0.2:.2f}); tl.fromTo("#df-th", {{strokeWidth:16}}, {{strokeWidth:5, duration:1.0}}, {tth:.2f});
""")

s = "twist"; ttw = aw(s, "adds twist"); tst = aw(s, "strong yarn")
spiral = "M440,960 " + " ".join(f"Q{460+i*40},{930 if i%2 else 990} {480+i*40},960" for i in range(14))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="tw-c"><span class="chip"><span class="red">TWIST!</span></span></div>
  {arrow('tw-s', spiral, C['blue'])}
  {tag('tw-y', 'strong yarn', 700, 300)}
""", f"""
pop("#tw-c", {ttw:.2f}, {{from:{{rotation:-30}}, to:{{rotation:-4}}}}); tl.set("#tw-s", {{opacity:1}}, 0); draw("#tw-s", {ttw+0.2:.2f}, 1.0);
pop("#tw-y", {tst:.2f});
""")

s = "fabric"; tco = aw(s, "coats are woven"); tsw2 = aw(s, "sweaters are knitted")
weave = "".join(f'<path d="M{20+i*24},8 L{20+i*24},84" stroke="{K}" stroke-width="5"/>' for i in range(8)) + "".join(f'<path d="M10,{20+j*22} ' + " ".join(f'Q{22+i*24},{(12 if (i+j)%2 else 28)+j*22} {34+i*24},{20+j*22}' for i in range(8)) + f'" stroke="{C["red"]}" stroke-width="5" fill="none"/>' for j in range(3))
knit = "".join(f'<path d="M{18+i*30},{20+j*30} q15,-18 30,0 q-6,24 -15,26 q-9,-2 -15,-26" stroke="{C["blue"]}" stroke-width="5" fill="none"/>' for i in range(6) for j in range(2))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="fb-c"><span class="chip">STEP 7 · FABRIC</span></div>
  <div id="fb-w" class="card" style="left:430px;top:900px;width:290px;height:120px"><svg class="abs" style="left:10px;top:14px" width="150" height="92" viewBox="0 0 210 96">{weave}</svg>
    <div class="abs" style="left:172px;top:26px;font-family:'Gochi Hand',cursive;font-size:36px;line-height:1">woven<br><span style="font-size:26px">coats</span></div></div>
  <div id="fb-k" class="card" style="left:745px;top:900px;width:290px;height:120px"><svg class="abs" style="left:8px;top:22px" width="150" height="72" viewBox="0 0 200 90">{knit}</svg>
    <div class="abs" style="left:166px;top:26px;font-family:'Gochi Hand',cursive;font-size:36px;line-height:1">knitted<br><span style="font-size:26px">sweaters</span></div></div>
""", f"""
pop("#fb-c", 0.05); rise("#fb-w", {tco:.2f}); rise("#fb-k", {tsw2:.2f});
""")

s = "finish"; tdy = aw(s, "dyed"); tco2 = aw(s, "color"); tsh2 = aw(s, "shape")
sw = "".join(f'<div id="fn-s{i}" class="abs" style="left:{700+i*100}px;top:290px;width:84px;height:84px;background:{c};border:4px solid {K};{SKETCH}"></div>' for i, c in enumerate(["#E0483C", "#2F5DA8", "#FFE27A"]))
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="fn-c"><span class="chip">STEP 8 · DYE + FINISH</span></div>
  {sw}
  <div id="fn-n" class="note">color · feel · <span class="hl">shape</span></div>
""", f"""
pop("#fn-c", {tdy-0.2:.2f}); {"".join(f'pop("#fn-s{i}", {tco2:.2f}+{i}*0.1, {{from:{{rotation:-30}}, to:{{rotation:{(-1)**i*6}}}}});' for i in range(3))}
rise("#fn-n", {tsh2-0.4:.2f});
""")

s = "outro"; tcu = aw(s, "cut"); tse = aw(s, "sewn"); tpr = aw(s, "pressed"); tfr = aw(s, "from sheep"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="ou-c"><span class="chip">DONE!</span></div>
  {tag('ou-1', 'cut', 470, 905)}{tag('ou-2', 'sew', 640, 905)}{tag('ou-3', 'press', 820, 905)}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">sheep → sweater</div></div>
""", f"""
pop("#ou-c", {tcu-0.2:.2f}); pop("#ou-1", {tcu:.2f}); pop("#ou-2", {tse:.2f}); pop("#ou-3", {tpr:.2f});
tl.to("#ou-1, #ou-2, #ou-3", {{opacity:0, duration:0.25}}, {tfr:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "ever wondered"), g("hook", "cozy sweater"))
wave(g("intro", "I'm Max"))
point(g("intro", "follow the wool"), 1.2)
point(g("shear", "step one"), 1.2)
wow(g("raw", "greasy"), 1.0)
point(g("scour", "washed"), 1.2)
wow(g("lanolin", "isn't wasted"), 1.2)
point(g("open", "spinning drums"), 1.2)
point(g("card", "wire teeth"), 1.2)
point(g("comb", "short fibers"), 1.2)
point(g("draft", "different speeds"), 1.2)
wow(g("twist", "adds twist"), 1.0)
point(g("fabric", "coats are woven"), 1.0)
point(g("fabric", "sweaters are knitted"), 1.0)
point(g("finish", "dyed"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "fluffy"), 0.45), ("pop.mp3", A("hook", "smelly"), 0.45), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("pop.mp3", A("shear", "step one"), 0.45), ("click-soft.mp3", A("raw", "lanolin"), 0.5), ("click.mp3", A("scour", "washed"), 0.35),
        ("sparkle.mp3", A("lanolin", "into lanolin"), 0.35), ("pop.mp3", A("card", "carding"), 0.45), ("ping.mp3", A("comb", "short fibers") + 0.6, 0.35),
        ("pop.mp3", A("draft", "now spinning"), 0.45), ("whoosh-short.mp3", A("twist", "adds twist"), 0.3), ("pop.mp3", A("fabric", "coats are woven"), 0.45),
        ("pop.mp3", A("finish", "color"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
