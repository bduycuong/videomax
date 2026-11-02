# Is the kiwi even a real bird? Doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; tq = aw(s, "real bird"); tf = aw(s, "can't fly"); th = aw(s, "like hair"); tt = aw(s, "tip of its beak"); tg = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">A real <span class="hl">bird?</span></div>
  {tag('hk-a', "can't fly", 640, 270, 'color:' + C['red'])}
  {tag('hk-b', 'hair?', 60, 700)}
  {tag('hk-c', 'nose on the beak tip', 520, 790, 'color:' + C['blue'])}
  <div id="hk-n" class="note">bird or mammal? <span class="hl">guess!</span></div>
""", f"""
pop("#hk-t", {tq-0.6:.2f}); pop("#hk-a", {tf:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#hk-b", {th:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#hk-c", {tt:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
rise("#hk-n", {tg-1.2:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tk = aw(s, "New Zealand")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">meet the <span class="hl">kiwi</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tk-0.6:.2f});
""")

s = "egg"; tc = aw(s, "size of a chicken"); te = aw(s, "enormous"); t15 = aw(s, "fifteen percent"); t20 = aw(s, "twenty percent"); tr = aw(s, "little room")
scenes[s] = scene_file(s, OV, f"""
  {chip('eg-c', 'THE EGG')}
  {tag('eg-a', '≈ chicken size', 60, 270)}
  {tag('eg-b', '≈ 15% of mom', 620, 270, 'font-size:56px;color:' + C['red'])}
  {tag('eg-d', 'up to 20%', 660, 380, 'font-size:50px;color:' + C['red'])}
  <div id="eg-n" class="note">a <span class="hl">huge</span> egg</div>
""", f"""
pop("#eg-c", 0.05); pop("#eg-a", {tc:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#eg-n", {te-0.3:.2f});
tl.to("#eg-a", {{opacity:0, duration:0.3}}, {te+0.8:.2f});
pop("#eg-b", {t15:.2f}, {{from:{{scale:1.7, rotation:12}}, to:{{rotation:3}}}}); pop("#eg-d", {t20:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

s = "feathers"; tp = aw(s, "gentle pat"); ts = aw(s, "stiff feathers"); thr = aw(s, "shaggy hair")
scenes[s] = scene_file(s, OV, f"""
  {chip('fe-c', 'THE FEATHERS')}
  {tag('fe-a', 'most birds: stiff', 60, 790, 'color:' + C['blue'])}
  {tag('fe-b', 'kiwi: soft, like hair', 560, 270, 'color:' + C['red'])}
  <div id="fe-n" class="note">feels like <span class="hl">fur</span></div>
""", f"""
pop("#fe-c", {tp-0.4:.2f}); pop("#fe-a", {ts:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#fe-b", {thr-0.8:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#fe-n", {thr:.2f});
""")

s = "bones"; th2 = aw(s, "hollow bones"); tmw = aw(s, "filled with marrow")
scenes[s] = scene_file(s, OV, f"""
  {chip('bo-c', 'THE BONES')}
  {tag('bo-a', 'hollow', 640, 270, 'font-size:54px;text-decoration:line-through;text-decoration-color:' + C['red'])}
  {tag('bo-b', 'filled with marrow', 520, 790, 'color:' + C['red'])}
  <div id="bo-n" class="note">heavy, like a <span class="hl">mammal</span></div>
""", f"""
pop("#bo-c", 0.05); pop("#bo-a", {th2:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
pop("#bo-b", {tmw:.2f}, {{from:{{scale:1.6, rotation:-10}}, to:{{rotation:-2}}}}); rise("#bo-n", {tmw+0.6:.2f});
""")

s = "wings"; tw = aw(s, "the wings"); ti = aw(s, "one inch")
scenes[s] = scene_file(s, OV, f"""
  {chip('wi-c', 'THE WINGS?')}
  {tag('wi-a', '≈ 1 inch', 700, 270, 'font-size:64px;color:' + C['red'])}
  <div id="wi-n" class="note"><span class="hl">hidden</span> under feathers</div>
""", f"""
pop("#wi-c", {tw-0.3:.2f}); pop("#wi-a", {ti:.2f}, {{from:{{scale:1.8, rotation:12}}, to:{{rotation:3}}}}); rise("#wi-n", {aw(s, "hidden under"):.2f});
""")

s = "legs"; tl1 = aw(s, "its legs"); t3 = aw(s, "a third"); tk2 = aw(s, "kicks hard")
scenes[s] = scene_file(s, OV, f"""
  {chip('lg-c', 'THE LEGS')}
  {tag('lg-a', '≈ 1/3 of its weight', 520, 270, 'color:' + C['blue'])}
  {tag('lg-b', 'KICK!', 760, 760, 'font-size:68px;color:' + C['red'])}
  <div id="lg-n" class="note">power in the <span class="hl">legs</span></div>
""", f"""
pop("#lg-c", {tl1-0.5:.2f}); rise("#lg-n", {tl1:.2f}); pop("#lg-a", {t3:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#lg-b", {tk2:.2f}, {{from:{{scale:1.8, rotation:14}}, to:{{rotation:4}}}});
""")

s = "nose"; tsp = aw(s, "strangest part"); tn = aw(s, "nostrils"); tw2 = aw(s, "worms and grubs")
scenes[s] = scene_file(s, OV, f"""
  {chip('no-c', 'THE NOSE')}
  {tag('no-a', 'nostrils here!', 600, 270, 'font-size:54px;color:' + C['red'])}
  {tag('no-b', 'SNIFF SNIFF', 60, 790, 'font-size:54px')}
  <div id="no-n" class="note">the <span class="hl">only</span> bird like this</div>
""", f"""
pop("#no-c", {tsp-0.3:.2f}); pop("#no-a", {tn:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#no-n", {tn+0.8:.2f});
pop("#no-b", {tw2-0.6:.2f}, {{from:{{scale:1.6, rotation:-12}}, to:{{rotation:-4}}}});
""")

s = "night"; twh = aw(s, "whiskers"); tni = aw(s, "at night"); tbu = aw(s, "sleeps in a burrow")
scenes[s] = scene_file(s, OV, f"""
  {chip('ni-c', 'WHISKERS + NIGHT')}
  {tag('ni-a', 'whiskers, like a cat', 520, 270, 'color:' + C['blue'])}
  {tag('ni-b', 'night owl', 60, 790, 'font-size:54px')}
  <div id="ni-n" class="note">sleeps all <span class="hl">day</span></div>
""", f"""
pop("#ni-c", 0.05); pop("#ni-a", {twh:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.to("#ni-a", {{opacity:0, duration:0.3}}, {tni-0.6:.2f});
pop("#ni-b", {tni:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#ni-n", {tbu:.2f});
""")

s = "outro"; ty = aw(s, "really is a bird"); trl = aw(s, "every bird rule"); tnf = aw(s, "No flying"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'YES, A REAL BIRD')}
  {tag('ou-a', 'rule breaker', 640, 270, 'font-size:54px;color:' + C['red'])}
  {tag('ou-b', 'no flight · hair · heavy bones · beak nose', 40, 790, 'font-size:38px')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {ty-0.4:.2f}); pop("#ou-a", {trl:.2f}, {{from:{{scale:1.7, rotation:12}}, to:{{rotation:3}}}});
pop("#ou-b", {tnf:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "real bird"), g("hook", "real bird") + 2.0)
point(g("hook", "take a guess"), 1.2)
wave(g("intro", "I'm Max"))
wow(g("egg", "fifteen percent"), 1.2)
point(g("feathers", "shaggy hair"), 1.2)
point(g("bones", "filled with marrow"), 1.2)
wow(g("wings", "one inch"), 1.2)
point(g("legs", "a third"), 1.2)
wow(g("nose", "nostrils"), 1.2)
point(g("night", "whiskers"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "take a guess"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("impact-bass-1.mp3", A("egg", "fifteen percent"), 0.35),
        ("pop.mp3", A("egg", "twenty percent"), 0.45), ("pop.mp3", A("feathers", "shaggy hair"), 0.45), ("pop.mp3", A("bones", "filled with marrow"), 0.45),
        ("impact-bass-2.mp3", A("wings", "one inch"), 0.35), ("pop.mp3", A("legs", "a third"), 0.45), ("click.mp3", A("legs", "kicks hard"), 0.5),
        ("pop.mp3", A("nose", "nostrils"), 0.45), ("pop.mp3", A("night", "whiskers"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
