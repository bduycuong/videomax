# Harlow monkeys: doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.sticky {{ position:absolute; width:230px; padding:14px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def arrow(i, d, color=None, w=7): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color or C["red"]}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/></svg>'


s = "hook"; t1 = aw(s, "feeds it"); t2 = aw(s, "hugs it")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:76px; }", f"""
  <div id="hk-t" class="h1">Milk or <span class="hl">hugs</span>?</div>
  <div id="hk-a" class="sticky" style="left:50px;top:290px;background:#C9E8C2;transform:rotate(-6deg)">feeds</div>
  <div id="hk-b" class="sticky" style="left:790px;top:300px;background:{C['hi']};transform:rotate(5deg)">hugs</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-b", {t2:.2f}, {{from:{{rotation:30}}, to:{{rotation:5}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tb = aw(s, "famous")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-f', 'a famous experiment', 520, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-f", {tb:.2f});
""")

s = "setup"; th = aw(s, "Harry Harlow"); tw_ = aw(s, "a wire mom"); tc = aw(s, "soft cloth mom")
scenes[s] = scene_file(s, OV, f"""
  {chip('su-c', '1950s · H. HARLOW')}
  <div id="su-w" class="sticky" style="left:60px;top:290px;background:#DDE3EA;transform:rotate(-4deg)">wire mom<br>+ milk</div>
  <div id="su-s" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">cloth mom<br>no milk</div>
  <div id="su-n" class="note">two <span class="hl">fake moms</span></div>
""", f"""
pop("#su-c", {th:.2f}); rise("#su-n", {th+1.2:.2f}); pop("#su-w", {tw_:.2f}); pop("#su-s", {tc:.2f});
""")

s = "predict"; te = aw(s, "many experts"); tf = aw(s, "whoever feeds them"); tr = aw(s, "wire mom should win")
scenes[s] = scene_file(s, OV, f"""
  {chip('pr-c', 'THE OLD IDEA')}
  {tag('pr-t', 'love = food?', 640, 300)}
  <div id="pr-n" class="note">wire mom <span class="hl">wins?</span></div>
""", f"""
pop("#pr-c", {te:.2f}); pop("#pr-t", {tf:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#pr-n", {tr:.2f});
""")

s = "result"; tn = aw(s, "Nope"); td = aw(s, "only to drink"); tcu = aw(s, "cuddled the soft")
scenes[s] = scene_file(s, OV, f"""
  {chip('rs-c', 'RESULT')}
  <div id="rs-x" class="abs" style="left:640px;top:280px;font-family:'Gochi Hand',cursive;font-size:110px;color:{C['red']};transform:rotate(-8deg);text-shadow:4px 4px 0 #FFFFFF;opacity:0">NOPE!</div>
  {tag('rs-d', 'wire = just a drink', 60, 760)}
  <div id="rs-n" class="note">rest of the day: <span class="hl">cloth mom</span></div>
""", f"""
pop("#rs-c", 0.05); pop("#rs-x", {tn:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); pop("#rs-d", {td:.2f}); rise("#rs-n", {tcu:.2f});
""")

s = "fear"; ts = aw(s, "scary toy"); tr2 = aw(s, "ran straight"); th2 = aw(s, "held on tight")
scenes[s] = scene_file(s, OV, f"""
  {chip('fr-c', 'FEAR TEST')}
  {tag('fr-t', 'scary toy!', 640, 300)}
  <div id="fr-n" class="note">run to the <span class="hl">soft mom</span></div>
""", f"""
pop("#fr-c", 0.05); pop("#fr-t", {ts:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#fr-n", {tr2:.2f});
""")

s = "comfort"; tfo = aw(s, "about food"); tto = aw(s, "comfort and touch")
scenes[s] = scene_file(s, OV, f"""
  {chip('cf-c', 'LOVE = ?')}
  <div id="cf-f" class="sticky" style="left:60px;top:290px;background:#DDE3EA;transform:rotate(-4deg)"><s>food</s></div>
  <div id="cf-t" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">touch</div>
""", f"""
pop("#cf-c", 0.05); pop("#cf-f", {tfo:.2f}); pop("#cf-t", {tto:.2f});
""")

s = "alone"; tdk = aw(s, "darkest part"); tal = aw(s, "completely alone"); tsh = aw(s, "curled up")
scenes[s] = scene_file(s, OV, f"""
  {chip('al-c', 'RAISED ALONE')}
  {tag('al-t', 'no mom, no friends', 60, 300)}
  <div id="al-n" class="note">curled up, <span class="red">shaking</span></div>
""", f"""
pop("#al-c", {tdk:.2f}); pop("#al-t", {tal:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#al-n", {tsh:.2f});
""")

s = "grown"; ta = aw(s, "As adults"); th3 = aw(s, "hid in corners"); tat = aw(s, "attacked others"); tne = aw(s, "neglected")
scenes[s] = scene_file(s, OV, f"""
  {chip('gr-c', 'AS ADULTS')}
  <div id="gr-n" class="note"><span id="gr-1" style="opacity:0">hid</span> · <span id="gr-2" style="opacity:0">fought</span> · <span id="gr-3" class="red" style="opacity:0">neglected</span></div>
""", f"""
pop("#gr-c", {ta:.2f}); pop("#gr-1", {th3:.2f}); pop("#gr-2", {tat:.2f}); pop("#gr-3", {tne:.2f});
""")

s = "recipe"; tl1 = aw(s, "lesson"); tt = aw(s, "touch"); tm = aw(s, "movement"); tp = aw(s, "and play")
scenes[s] = scene_file(s, OV, f"""
  {chip('rc-c', "HARLOW'S LESSON")}
  {tag('rc-1', 'touch', 450, 905)}{tag('rc-2', 'movement', 610, 905)}{tag('rc-3', 'play', 880, 905)}
""", f"""
pop("#rc-c", {tl1:.2f}); pop("#rc-1", {tt:.2f}); pop("#rc-2", {tm:.2f}); pop("#rc-3", {tp:.2f});
""")

s = "watson"; tb2 = aw(s, "parenting book"); tn2 = aw(s, "never to hug")
scenes[s] = scene_file(s, OV, f"""
  {chip('wt-c', 'OLD ADVICE · 1928')}
  {tag('wt-t', 'parenting book', 640, 300)}
  <div id="wt-n" class="note"><span class="red">"never hug or kiss"</span></div>
""", f"""
pop("#wt-c", 0.05); pop("#wt-t", {tb2:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#wt-n", {tn2:.2f});
""")

s = "ethics"; tcr = aw(s, "seen as cruel"); tla = aw(s, "lab animals")
scenes[s] = scene_file(s, OV, f"""
  {chip('et-c', 'TODAY')}
  {tag('et-t', 'seen as cruel', 640, 300)}
  <div id="et-n" class="note">better care for <span class="hl">lab animals</span></div>
""", f"""
pop("#et-c", 0.05); pop("#et-t", {tcr:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#et-n", {tla:.2f});
""")

s = "legacy"; trk = aw(s, "raise kids"); tsp = aw(s, "spoiling"); tne2 = aw(s, "a need")
scenes[s] = scene_file(s, OV, f"""
  {chip('lg-c', 'WHAT CHANGED')}
  {tag('lg-t', '<s>spoiling</s>', 60, 300)}
  <div id="lg-n" class="note">warmth = <span class="hl">a need</span></div>
""", f"""
pop("#lg-c", {trk:.2f}); pop("#lg-t", {tsp:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#lg-n", {tne2:.2f});
""")

s = "outro"; t1 = aw(s, "hug beats"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'HUG > BOTTLE')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">touch · movement · play</div></div>
""", f"""
pop("#ou-c", {t1:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "what does"), g("hook", "hugs it"))
wave(g("intro", "I'm Max"))
point(g("setup", "two fake moms"), 1.2)
think(g("predict", "should win"), g("predict", "right"))
wow(g("result", "Nope"), 1.0)
point(g("fear", "ran straight"), 1.2)
point(g("comfort", "comfort and touch"), 1.2)
point(g("alone", "completely alone"), 1.2)
point(g("grown", "As adults"), 1.2)
wow(g("recipe", "touch"), 1.0)
point(g("watson", "parenting book"), 1.2)
point(g("ethics", "seen as cruel"), 1.2)
point(g("legacy", "a need"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "feeds it"), 0.45), ("pop.mp3", A("hook", "hugs it"), 0.45), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click.mp3", A("setup", "a wire mom"), 0.4), ("click.mp3", A("setup", "soft cloth mom"), 0.4), ("impact-bass-1.mp3", A("result", "Nope"), 0.35),
        ("ping.mp3", A("comfort", "comfort and touch"), 0.35), ("riser.mp3", A("alone", "darkest part"), 0.25), ("pop.mp3", A("recipe", "touch"), 0.45),
        ("pop.mp3", A("recipe", "and play"), 0.45), ("click-soft.mp3", A("watson", "never to hug"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
