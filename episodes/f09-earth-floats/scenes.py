# Why doesn't Earth fall? Doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.sticky {{ position:absolute; width:230px; padding:14px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; t6 = aw(s, "six trillion"); tn = aw(s, "Nothing holds"); tf = aw(s, "doesn't it fall")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:76px; }", f"""
  <div id="hk-t" class="h1">Why doesn't Earth <span class="hl">fall</span>?</div>
  {tag('hk-m', '6 × 10²⁴ kg', 60, 270)}
  <div id="hk-n" class="note">no rope, no stand…</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-m", {t6:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#hk-n", {tn:.2f});
""")

s = "intro"; tw = aw(s, "Max Wise"); tk = aw(s, "keeps our planet")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">what keeps it <span class="hl">up there</span>?</div>
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tk:.2f});
""")

s = "nodown"; tu = aw(s, "no up"); th = aw(s, "something heavy"); ts = aw(s, "is the Sun"); tm = aw(s, "three hundred thirty thousand")
scenes[s] = scene_file(s, OV, f"""
  {chip('nd-c', 'NO UP, NO DOWN')}
  <div id="nd-x" class="abs" style="left:70px;top:270px;font-family:'Gochi Hand',cursive;font-size:84px;color:{C['red']};transform:rotate(-6deg);text-shadow:4px 4px 0 #FFFFFF;opacity:0"><s>down</s></div>
  {tag('nd-s', 'Sun = 330,000 Earths', 470, 780)}
  <div id="nd-n" class="note">fall = move toward <span class="hl">heavy</span></div>
""", f"""
pop("#nd-c", {tu:.2f}); pop("#nd-x", {tu+0.4:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-6}}}}); rise("#nd-n", {th:.2f});
tl.to("#nd-x", {{opacity:0, duration:0.2}}, {ts-0.3:.2f}); pop("#nd-s", {tm:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}});
""")

s = "newton"; tg = aw(s, "gravity is"); ta = aw(s, "an apple"); tmo = aw(s, "the Moon")
scenes[s] = scene_file(s, OV, f"""
  {chip('nw-c', 'ISAAC NEWTON')}
  {tag('nw-t', 'gravity = a pull', 560, 790)}
  <div id="nw-n" class="note">apple, Moon, <span class="hl">planets</span></div>
""", f"""
pop("#nw-c", 0.05); pop("#nw-t", {tg:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#nw-n", {tmo:.2f});
""")

s = "einstein"; te = aw(s, "Albert Einstein"); tb = aw(s, "bend space"); td = aw(s, "a dent")
scenes[s] = scene_file(s, OV, f"""
  {chip('es-c', '1915 · EINSTEIN')}
  {tag('es-t', 'mass bends space', 60, 780)}
  <div id="es-n" class="note">like a <span class="hl">dent</span></div>
""", f"""
pop("#es-c", {te-0.6:.2f}); pop("#es-t", {tb:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#es-n", {td:.2f});
""")

s = "sheet"; tw_ = aw(s, "stretchy sheet"); tdp = aw(s, "deep dip"); tr = aw(s, "rolls down")
scenes[s] = scene_file(s, OV, f"""
  {chip('sh-c', 'THE STRETCHY SHEET')}
  {tag('sh-t', 'heavy ball = Sun', 600, 290)}
  <div id="sh-n" class="note">marble rolls <span class="hl">in</span></div>
""", f"""
pop("#sh-c", {tw_-0.3:.2f}); pop("#sh-t", {tdp:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#sh-n", {tr:.2f});
""")

s = "sideways"; tp = aw(s, "sideways push"); tc = aw(s, "keeps circling")
scenes[s] = scene_file(s, OV, f"""
  {chip('sw-c', 'ADD A SIDEWAYS PUSH')}
  <div id="sw-a" class="abs" style="left:640px;top:280px;font-family:'Gochi Hand',cursive;font-size:96px;color:{C['red']};transform:rotate(-8deg);text-shadow:4px 4px 0 #FFFFFF;opacity:0">WHOOSH!</div>
  <div id="sw-n" class="note">it <span class="hl">circles</span> instead</div>
""", f"""
pop("#sw-c", 0.05); pop("#sw-a", {tp:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#sw-n", {tc:.2f});
""")

s = "speed"; tr2 = aw(s, "races sideways"); t30 = aw(s, "thirty kilometers"); tal = aw(s, "always falling"); tmi = aw(s, "always missing")
scenes[s] = scene_file(s, OV, f"""
  {chip('sp-c', 'EARTH DOES THIS')}
  {tag('sp-t', '≈ 30 km every second', 500, 790)}
  <div id="sp-n" class="note">always falling… <span class="hl">always missing</span></div>
""", f"""
pop("#sp-c", 0.05); pop("#sp-t", {t30:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#sp-n", {tmi-0.8:.2f});
""")

s = "proof"; tb2 = aw(s, "really bent"); tec = aw(s, "solar eclipse"); tsb = aw(s, "starlight bend")
scenes[s] = scene_file(s, OV, f"""
  {chip('pf-c', '1919 · ECLIPSE TEST')}
  {tag('pf-t', 'starlight bends!', 60, 790)}
  <div id="pf-n" class="note">space <span class="hl">is</span> bent</div>
""", f"""
pop("#pf-c", {tec-0.3:.2f}); pop("#pf-t", {tsb:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#pf-n", {tsb+0.6:.2f});
""")

s = "outro"; tfl = aw(s, "isn't floating"); tfa = aw(s, "falling around"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'FALLING… FOREVER')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tfa:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "So why"), g("hook", "fall"))
wave(g("intro", "I'm Max"))
point(g("nodown", "no up"), 1.2)
wow(g("nodown", "three hundred thirty thousand"), 1.2)
point(g("newton", "gravity is"), 1.2)
point(g("einstein", "bend space"), 1.2)
point(g("sheet", "deep dip"), 1.2)
wow(g("sideways", "keeps circling"), 1.0)
point(g("speed", "thirty kilometers"), 1.2)
wow(g("proof", "starlight bend"), 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "doesn't it fall"), 0.35), ("pop.mp3", A("hook", "six trillion"), 0.45), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click.mp3", A("nodown", "no up"), 0.4), ("impact-bass-1.mp3", A("nodown", "three hundred thirty thousand"), 0.35),
        ("pop.mp3", A("newton", "gravity is"), 0.45), ("pop.mp3", A("einstein", "bend space"), 0.45), ("click-soft.mp3", A("sheet", "deep dip"), 0.5),
        ("whoosh-short.mp3", A("sideways", "sideways push"), 0.45), ("pop.mp3", A("speed", "thirty kilometers"), 0.45),
        ("ping.mp3", A("proof", "starlight bend"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
