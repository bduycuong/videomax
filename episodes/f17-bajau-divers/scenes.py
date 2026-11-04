# Did the Bajau sea nomads evolve to dive? Doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; tq = aw(s, "better at diving"); t1 = aw(s, "one minute"); tg = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">Born to <span class="hl">dive?</span></div>
  {tag('hk-a', 'most of us: ≈ 1 minute', 520, 800, 'color:' + C['red'])}
  <div id="hk-n" class="note">yes or no? <span class="hl">guess!</span></div>
""", f"""
pop("#hk-t", {tq-0.8:.2f}); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
rise("#hk-n", {tg-0.6:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tb = aw(s, "sea nomads")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-a', 'the Bajau', 640, 270, 'font-size:56px;color:' + C['blue'])}
  <div id="in-n" class="note"><span class="hl">sea nomads</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-a", {tb-0.9:.2f}, {{from:{{rotation:10}}, to:{{rotation:3}}}}); rise("#in-n", {tb:.2f});
""")

s = "village"; ti = aw(s, "Indonesia"); ts = aw(s, "on stilts"); tn = aw(s, "no streets"); tbo = aw(s, "by boat")
scenes[s] = scene_file(s, OV, f"""
  {chip('vi-c', 'HOME ON THE SEA')}
  {tag('vi-a', 'Indonesia · Malaysia · Philippines', 60, 270, 'font-size:40px')}
  {tag('vi-b', 'stilt house', 700, 380, 'color:' + C['blue'])}
  {tag('vi-d', 'no streets!', 640, 270, 'font-size:54px;color:' + C['red'])}
  <div id="vi-n" class="note">get around by <span class="hl">boat</span></div>
""", f"""
pop("#vi-c", 0.05); pop("#vi-a", {ti:.2f}, {{from:{{rotation:-6}}, to:{{rotation:-1}}}});
tl.to("#vi-a", {{opacity:0, duration:0.3}}, {ts-0.4:.2f});
pop("#vi-b", {ts:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
tl.to("#vi-b", {{opacity:0, duration:0.3}}, {tn-0.4:.2f});
pop("#vi-d", {tn:.2f}, {{from:{{scale:1.6, rotation:-12}}, to:{{rotation:-3}}}}); rise("#vi-n", {tbo-0.5:.2f});
""")

s = "kids"; ty = aw(s, "very young"); tf = aw(s, "the food is")
scenes[s] = scene_file(s, OV, f"""
  {chip('ki-c', 'SWIM FIRST')}
  {tag('ki-a', 'SPLASH!', 640, 760, 'font-size:62px;color:' + C['blue'])}
  <div id="ki-n" class="note">the sea = the <span class="hl">kitchen</span></div>
""", f"""
pop("#ki-c", 0.05); pop("#ki-a", {ty:.2f}, {{from:{{scale:1.8, rotation:14}}, to:{{rotation:4}}}}); rise("#ki-n", {tf-0.6:.2f});
""")

s = "dive"; t60 = aw(s, "sixty percent"); tw = aw(s, "wooden mask"); t70 = aw(s, "seventy meters")
scenes[s] = scene_file(s, OV, f"""
  {chip('dv-c', 'THE DIVE')}
  {tag('dv-a', 'up to 60% of the workday', 520, 270, 'color:' + C['red'])}
  {tag('dv-b', 'wooden mask only', 60, 790)}
  {tag('dv-d', '70+ m deep', 700, 380, 'font-size:62px;color:' + C['blue'])}
  <div id="dv-n" class="note">one breath, <span class="hl">very deep</span></div>
""", f"""
pop("#dv-c", 0.05); pop("#dv-a", {t60:.2f}, {{from:{{scale:1.6, rotation:-10}}, to:{{rotation:-2}}}});
pop("#dv-b", {tw-0.3:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
pop("#dv-d", {t70:.2f}, {{from:{{scale:1.8, rotation:12}}, to:{{rotation:3}}}}); rise("#dv-n", {tw+0.3:.2f});
""")

s = "hunt"; tsp = aw(s, "spear fish"); tsb = aw(s, "single breath")
scenes[s] = scene_file(s, OV, f"""
  {chip('hu-c', 'DINNER HUNT')}
  {tag('hu-a', 'ZIP!', 760, 300, 'font-size:66px;color:' + C['red'])}
  <div id="hu-n" class="note">all on <span class="hl">one breath</span></div>
""", f"""
pop("#hu-c", 0.05); pop("#hu-a", {tsp:.2f}, {{from:{{scale:1.8, rotation:-14}}, to:{{rotation:-4}}}}); rise("#hu-n", {tsb-0.5:.2f});
""")

s = "history"; tt = aw(s, "a thousand years")
scenes[s] = scene_file(s, OV, f"""
  {chip('hi-c', 'GENERATIONS')}
  {tag('hi-a', '1,000+ years', 680, 270, 'font-size:62px;color:' + C['blue'])}
  <div id="hi-n" class="note">life at <span class="hl">sea</span></div>
""", f"""
pop("#hi-c", 0.05); rise("#hi-n", 0.4); pop("#hi-a", {tt:.2f}, {{from:{{scale:1.8, rotation:12}}, to:{{rotation:3}}}});
""")

s = "spleen"; tu = aw(s, "ultrasound"); tsl = aw(s, "the spleen"); t50 = aw(s, "fifty percent")
scenes[s] = scene_file(s, OV, f"""
  {chip('sp-c', 'THE SPLEEN')}
  {tag('sp-a', 'ultrasound check', 60, 270)}
  {tag('sp-b', '≈ 50% bigger', 640, 270, 'font-size:62px;color:' + C['red'])}
  <div id="sp-n" class="note">vs. neighbors <span class="hl">on land</span></div>
""", f"""
pop("#sp-c", {tsl-0.3:.2f}); pop("#sp-a", {tu:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.to("#sp-a", {{opacity:0, duration:0.3}}, {t50-0.5:.2f});
pop("#sp-b", {t50:.2f}, {{from:{{scale:1.8, rotation:12}}, to:{{rotation:3}}}}); rise("#sp-n", {t50+0.8:.2f});
""")

s = "tank"; tr = aw(s, "red blood cells"); tq2 = aw(s, "squeezes them"); ta = aw(s, "spare air tank"); tgn = aw(s, "gene changes")
scenes[s] = scene_file(s, OV, f"""
  {chip('ta-c', 'WHY IT MATTERS')}
  {tag('ta-a', 'stores oxygen-rich blood', 60, 270, 'color:' + C['red'])}
  {tag('ta-b', 'SQUEEZE!', 720, 380, 'font-size:60px;color:' + C['blue'])}
  {tag('ta-d', 'gene changes', 60, 790, 'font-size:50px;color:' + C['blue'])}
  <div id="ta-n" class="note">a spare <span class="hl">air tank</span></div>
""", f"""
pop("#ta-c", 0.05); pop("#ta-a", {tr:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#ta-b", {tq2:.2f}, {{from:{{scale:1.8, rotation:14}}, to:{{rotation:4}}}}); rise("#ta-n", {ta-0.4:.2f});
tl.to("#ta-a, #ta-b", {{opacity:0, duration:0.3}}, {tgn-0.6:.2f});
pop("#ta-d", {tgn:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
""")

s = "outro"; tys = aw(s, "So yes"); tad = aw(s, "thousand years at sea"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'YES: BUILT FOR THE SEA')}
  {tag('ou-a', 'bigger spleen = spare tank', 520, 270, 'font-size:42px;color:' + C['red'])}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tys:.2f}); pop("#ou-a", {tad:.2f}, {{from:{{scale:1.5, rotation:10}}, to:{{rotation:2}}}});
tl.to("#ou-a", {{opacity:0, duration:0.3}}, {tsc-0.4:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "better at diving"), g("hook", "better at diving") + 2.0)
point(g("hook", "take a guess"), 1.2)
wave(g("intro", "I'm Max"))
point(g("village", "on stilts"), 1.2)
wow(g("dive", "seventy meters"), 1.2)
point(g("hunt", "spear fish"), 1.0)
wow(g("spleen", "fifty percent"), 1.2)
point(g("tank", "spare air tank"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "take a guess"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("village", "no streets"), 0.45),
        ("click.mp3", A("kids", "very young"), 0.5), ("pop.mp3", A("dive", "sixty percent"), 0.45), ("impact-bass-1.mp3", A("dive", "seventy meters"), 0.35),
        ("click.mp3", A("hunt", "spear fish"), 0.5), ("pop.mp3", A("history", "a thousand years"), 0.45), ("impact-bass-2.mp3", A("spleen", "fifty percent"), 0.35),
        ("pop.mp3", A("tank", "squeezes them"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
