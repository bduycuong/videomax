# Mariana Trench dive: doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; opacity:0; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; opacity:0; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; opacity:0; }}
.sticky {{ position:absolute; width:250px; padding:12px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:42px; line-height:1.1; border:4px solid {K}; {SKETCH} opacity:0; }}
.gauge {{ position:absolute; background:#FFFFFF; border:5px solid {K}; {SKETCH} padding:4px 26px; font-family:'Gochi Hand',cursive; font-size:64px; line-height:1.1; box-shadow:5px 6px 0 rgba(38,42,59,.25); white-space:nowrap; opacity:0; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def gauge(i, txt, x, y, extra=""): return f'<div id="{i}" class="gauge" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def note(i, txt): return f'<div id="{i}" class="note">{txt}</div>'
def svgpath(i, d, color, w=7, extra=""): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round" style="opacity:0" {extra}/></svg>'

s = "hook"; td = aw(s, "deepest spot"); tq = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:62px; white-space:nowrap; opacity:0; }", f"""
  <div id="hk-t" class="h1">What's at the <span class="hl">very bottom?</span></div>
  <div id="hk-a" class="sticky" style="left:770px;top:280px;background:{C['hi']}">monsters?</div>
  <div id="hk-b" class="sticky" style="left:770px;top:410px;background:#C9E8C2">nothing?</div>
  <div id="hk-c" class="sticky" style="left:770px;top:540px;background:#F6C9C2">mud?</div>
  {note('hk-n', 'your <span class="hl">guess?</span>')}
""", f"""
pop("#hk-t", 0.3); pop("#hk-a", {td:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
pop("#hk-b", {td+0.5:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#hk-c", {td+1.0:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}});
rise("#hk-n", {tq-0.2:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tt = aw(s, "Mariana Trench")
scenes[s] = scene_file(s, OV, f"""
  {chip('in-c', 'MAX WISE')}
  {note('in-n', 'dive! <span class="hl">Mariana Trench</span> ↓')}
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tt-0.3:.2f});
""")

s = "sunlight"; t2 = aw(s, "two hundred meters"); tf = aw(s, "fades fast")
scenes[s] = scene_file(s, OV, f"""
  {chip('su-c', 'SUNLIGHT ZONE')}
  {gauge('su-g', '200 m', 760, 270)}
  {note('su-n', 'below: the blue <span class="blue">fades</span>')}
""", f"""
pop("#su-c", 0.05); pop("#su-g", {t2:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#su-n", {tf-0.3:.2f});
""")

s = "glow"; t1 = aw(s, "one thousand meters"); tgo = aw(s, "is gone"); tgl = aw(s, "own glow")
scenes[s] = scene_file(s, OV, f"""
  {chip('gl-c', 'MIDNIGHT ZONE')}
  {gauge('gl-g', '1,000 m', 720, 270)}
  {tag('gl-t', 'glow-in-the-dark!', 600, 790, 'color:' + C['blue'])}
""", f"""
pop("#gl-c", 0.05); pop("#gl-g", {t1:.2f}, {{from:{{rotation:10}}, to:{{rotation:3}}}});
tl.to("#gl-g", {{opacity:0, duration:0.25}}, {tgl-0.6:.2f}); pop("#gl-t", {tgl:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

s = "snow"; ts = aw(s, "snowing"); tms = aw(s, "marine snow"); tfo = aw(s, "food")
scenes[s] = scene_file(s, OV, f"""
  {chip('sn-c', 'MARINE <span class="blue">SNOW</span>')}
  {tag('sn-a', 'dead bits drifting down', 470, 280, 'font-size:42px')}
  {note('sn-n', '= <span class="hl">food</span> for the deep')}
""", f"""
pop("#sn-c", {ts:.2f}); pop("#sn-a", {tms+0.3:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}}); rise("#sn-n", {tfo-0.3:.2f});
""")

s = "pressure"; t10 = aw(s, "every ten meters"); t4k = aw(s, "four thousand meters"); t400 = aw(s, "four hundred times")
scenes[s] = scene_file(s, OV, f"""
  {chip('pr-c', 'PRESSURE')}
  {tag('pr-a', '+10 m = +1 atmosphere', 520, 270, 'font-size:42px')}
  {gauge('pr-g', '4,000 m', 740, 270)}
  {note('pr-n', 'about <span class="hl">400×</span> the surface')}
""", f"""
pop("#pr-c", 0.05); pop("#pr-a", {t10:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
tl.to("#pr-a", {{opacity:0, duration:0.25}}, {t4k-0.4:.2f}); pop("#pr-g", {t4k:.2f}, {{from:{{rotation:10}}, to:{{rotation:3}}}});
rise("#pr-n", {t400:.2f});
""")

s = "floor"; tpb = aw(s, "pitch black"); tcf = aw(s, "close to freezing"); tan = aw(s, "animals")
scenes[s] = scene_file(s, OV, f"""
  {chip('fl-c', 'THE ABYSS')}
  {tag('fl-a', 'dark + near freezing', 560, 280, 'color:' + C['blue'])}
  {note('fl-n', 'still <span class="hl">alive!</span>')}
""", f"""
pop("#fl-c", {tpb-0.3:.2f}); pop("#fl-a", {tcf:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}}); rise("#fl-n", {tan:.2f});
""")

s = "edge"; tdr = aw(s, "drops away"); t6 = aw(s, "six thousand meters"); thz = aw(s, "hadal zone")
scenes[s] = scene_file(s, OV, f"""
  {chip('ed-c', 'THE DROP')}
  {gauge('ed-g', '6,000 m', 740, 270)}
  {note('ed-n', 'the <span class="hl">hadal zone</span>')}
""", f"""
pop("#ed-c", {tdr:.2f}); pop("#ed-g", {t6:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#ed-n", {thz-0.2:.2f});
""")

s = "plates"; tw = aw(s, "why is there"); tdv = aw(s, "dives down"); tgr = aw(s, "deep groove")
scenes[s] = scene_file(s, OV, f"""
  {chip('pl-c', 'WHY A TRENCH?')}
  {svgpath('pl-p', 'M560,300 Q760,330 900,520 M850,500 L900,520 L905,465', C['red'], 9)}
  {tag('pl-a', 'plate dives under', 420, 270, 'color:' + C['red'])}
  {note('pl-n', '→ a long, deep <span class="hl">groove</span>')}
""", f"""
pop("#pl-c", {tw:.2f});
pop("#pl-a", {tdv-0.3:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}}); tl.set("#pl-p", {{opacity:1}}, {tdv:.2f}); draw("#pl-p", {tdv:.2f}, 0.8);
rise("#pl-n", {tgr-0.4:.2f});
""")

s = "fish"; tsn = aw(s, "snailfish"); t83 = aw(s, "eight thousand three hundred"); t84 = aw(s, "eight thousand four hundred")
scenes[s] = scene_file(s, OV, f"""
  {chip('fi-c', 'HOW DEEP DO FISH GO?')}
  {tag('fi-a', 'snailfish filmed: ~8,300 m', 450, 270, 'font-size:42px')}
  {note('fi-n', 'fish limit: about <span class="hl">8,400 m</span>')}
""", f"""
pop("#fi-c", 0.05); pop("#fi-a", {t83:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}}); rise("#fi-n", {t84:.2f});
""")

s = "deeper"; t9 = aw(s, "nine thousand"); t10k = aw(s, "ten thousand")
scenes[s] = scene_file(s, OV, f"""
  {chip('dp-c', 'DEEPER…')}
  {gauge('dp-a', '9,000 m', 740, 270)}
  {gauge('dp-b', '10,000 m', 700, 270, 'color:' + C['red'])}
""", f"""
pop("#dp-c", 0.05); pop("#dp-a", {t9:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
tl.to("#dp-a", {{opacity:0, duration:0.2}}, {t10k-0.25:.2f}); pop("#dp-b", {t10k:.2f}, {{from:{{scale:1.5, rotation:10}}, to:{{rotation:3}}}});
""")

s = "bottom"; tch = aw(s, "Challenger Deep"); t109 = aw(s, "ten thousand nine hundred"); tev = aw(s, "Mount Everest")
scenes[s] = scene_file(s, OV, f"""
  {chip('bo-c', 'CHALLENGER <span class="hl">DEEP</span>')}
  {gauge('bo-g', '~10,900 m', 670, 270)}
  {note('bo-n', 'Everest + <span class="hl">about 2 km</span>')}
""", f"""
pop("#bo-c", {tch:.2f}); pop("#bo-g", {t109:.2f}, {{from:{{rotation:10}}, to:{{rotation:3}}}}); rise("#bo-n", {tev-0.6:.2f});
""")

s = "crush"; t1k = aw(s, "one thousand times")
scenes[s] = scene_file(s, OV, f"""
  {chip('cr-c', 'SQUEEZE!')}
  {tag('cr-a', '1,000×+', 780, 290, 'font-size:66px;color:' + C['red'])}
  {note('cr-n', 'than at the <span class="hl">beach</span>')}
""", f"""
pop("#cr-c", 0.05); pop("#cr-a", {t1k:.2f}, {{from:{{scale:1.8, rotation:-16}}, to:{{rotation:-5}}}}); rise("#cr-n", {t1k+0.6:.2f});
""")

s = "history"; t60 = aw(s, "nineteen sixty"); ttr = aw(s, "Trieste"); t20 = aw(s, "twenty minutes")
scenes[s] = scene_file(s, OV, f"""
  {chip('hi-c', 'PEOPLE MADE IT!')}
  {gauge('hi-g', '1960', 800, 270)}
  {tag('hi-a', 'Walsh + Piccard · Trieste', 440, 790, 'font-size:42px')}
  {note('hi-n', '~<span class="hl">20 minutes</span> at the bottom')}
""", f"""
pop("#hi-c", 0.05); pop("#hi-g", {t60:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
pop("#hi-a", {ttr-0.4:.2f}, {{from:{{rotation:6}}, to:{{rotation:1}}}}); rise("#hi-n", {t20-0.3:.2f});
""")

s = "outro"; tdk = aw(s, "dark"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'DARK · CRUSHING · <span class="blue">ALIVE</span>')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">the deepest place on Earth</div></div>
""", f"""
pop("#ou-c", {tdk-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "what would"), g("hook", "on Earth"))
point(g("hook", "take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("intro", "Mariana Trench"), 1.2)
point(g("sunlight", "two hundred meters"), 1.2)
wow(g("glow", "own glow"), 1.0)
wow(g("snow", "snowing"), 1.0)
point(g("pressure", "four hundred times"), 1.2)
point(g("floor", "animals"), 1.2)
point(g("edge", "drops away"), 1.2)
think(g("plates", "why is there"), g("plates", "a trench at all") + 0.6)
point(g("fish", "snailfish"), 1.2)
point(g("deeper", "ten thousand"), 1.0)
wow(g("bottom", "Challenger Deep"), 1.2)
wow(g("crush", "one thousand times"), 1.0)
point(g("history", "nineteen sixty"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "deepest spot"), 0.45), ("ping.mp3", A("hook", "take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("sunlight", "two hundred meters"), 0.45),
        ("sparkle.mp3", A("glow", "own glow"), 0.35), ("click-soft.mp3", A("snow", "marine snow"), 0.5),
        ("impact-bass-1.mp3", A("pressure", "four hundred times"), 0.35), ("whoosh-short.mp3", A("edge", "drops away"), 0.3),
        ("click.mp3", A("fish", "eight thousand three hundred"), 0.35), ("pop.mp3", A("deeper", "ten thousand"), 0.45),
        ("impact-bass-2.mp3", A("bottom", "Challenger Deep"), 0.3), ("impact-bass-1.mp3", A("crush", "one thousand times"), 0.35),
        ("ping.mp3", A("history", "nineteen sixty"), 0.4), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
