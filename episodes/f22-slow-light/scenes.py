# Slow light: doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
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


s = "hook"; tl7 = aw(s, "seven and a half"); tsn = aw(s, "snail"); tq = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; opacity:0; }", f"""
  <div id="hk-t" class="h1">Light is <span class="hl">slow?!</span></div>
  {gauge('hk-g', '7.5 laps / second', 520, 270)}
  <div id="hk-a" class="sticky" style="left:60px;top:420px;background:{C['hi']}">space is huge?</div>
  <div id="hk-b" class="sticky" style="left:60px;top:560px;background:#C9E8C2">light gets tired?</div>
  <div id="hk-c" class="sticky" style="left:60px;top:700px;background:#F6C9C2">a trick question?</div>
  {note('hk-n', 'your <span class="hl">guess?</span>')}
""", f"""
pop("#hk-t", 0.3); pop("#hk-g", {tl7:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
tl.to("#hk-g", {{opacity:0, duration:0.25}}, {tsn-0.3:.2f});
pop("#hk-a", {tq-1.2:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
pop("#hk-b", {tq-0.7:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#hk-c", {tq-0.2:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}});
rise("#hk-n", {tq:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tr = aw(s, "race")
scenes[s] = scene_file(s, OV, f"""
  {chip('in-c', 'MAX WISE')}
  {note('in-n', 'race a beam of <span class="hl">light</span>')}
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tr-0.3:.2f});
""")

s = "fast"; tfa = aw(s, "fastest thing"); tkm = aw(s, "three hundred thousand"); tes = aw(s, "every second")
scenes[s] = scene_file(s, OV, f"""
  {chip('fa-c', 'THE SPEED OF LIGHT')}
  {tag('fa-a', 'fastest thing there is', 440, 290)}
  {gauge('fa-g', '300,000 km', 560, 400, 'color:' + C['blue'])}
  {note('fa-n', 'every <span class="hl">second!</span>')}
""", f"""
pop("#fa-c", 0.05); pop("#fa-a", {tfa:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#fa-g", {tkm:.2f}, {{from:{{scale:1.5, rotation:10}}, to:{{rotation:3}}}}); rise("#fa-n", {tes-0.2:.2f});
""")

s = "sun"; t8 = aw(s, "eight minutes and twenty seconds"); tago = aw(s, "eight minutes ago")
scenes[s] = scene_file(s, OV, f"""
  {chip('su-c', 'SUN → EARTH')}
  {gauge('su-g', '8 min 20 s', 600, 290, 'color:' + C['red'])}
  {note('su-n', 'you see the Sun of <span class="hl">8 min ago</span>')}
""", f"""
pop("#su-c", 0.05); pop("#su-g", {t8:.2f}, {{from:{{scale:1.6, rotation:-12}}, to:{{rotation:-3}}}});
rise("#su-n", {tago-0.4:.2f});
""")

s = "nearest"; tpc = aw(s, "Proxima Centauri"); t4 = aw(s, "more than four years")
scenes[s] = scene_file(s, OV, f"""
  {chip('ne-c', 'NEAREST STAR')}
  {tag('ne-a', 'Proxima Centauri', 440, 290, 'color:' + C['blue'])}
  {gauge('ne-g', '4+ years', 700, 420)}
  {note('ne-n', 'light, travelling for <span class="hl">4+ years</span>')}
""", f"""
pop("#ne-c", 0.05); pop("#ne-a", {tpc:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}});
pop("#ne-g", {t4:.2f}, {{from:{{scale:1.6, rotation:12}}, to:{{rotation:4}}}}); rise("#ne-n", {t4+0.3:.2f});
""")

s = "voyager"; tv1 = aw(s, "Voyager One"); tsp = aw(s, "sixty one thousand"); t75 = aw(s, "seventy five thousand")
scenes[s] = scene_file(s, OV, f"""
  {chip('vo-c', 'BY SPACE PROBE?')}
  {tag('vo-a', '61,000 km/h', 640, 290)}
  {gauge('vo-g', '~75,000 years', 520, 760, 'color:' + C['red'])}
  {note('vo-n', 'Voyager 1 to the nearest star')}
""", f"""
pop("#vo-c", 0.05); rise("#vo-n", {tv1-0.2:.2f}); pop("#vo-a", {tsp:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#vo-g", {t75:.2f}, {{from:{{scale:1.7, rotation:-12}}, to:{{rotation:-3}}}});
""")

s = "galaxy"; tmw = aw(s, "Milky Way"); tly = aw(s, "one hundred thousand light years"); tcr = aw(s, "cross it")
scenes[s] = scene_file(s, OV, f"""
  {chip('ga-c', 'THE MILKY WAY')}
  {gauge('ga-g', '100,000 light years', 330, 290, 'color:' + C['blue'])}
  {note('ga-n', 'light needs <span class="hl">100,000 years</span>')}
""", f"""
pop("#ga-c", {tmw-0.3:.2f}); pop("#ga-g", {tly:.2f}, {{from:{{scale:1.5, rotation:-8}}, to:{{rotation:-2}}}});
rise("#ga-n", {tcr-1.2:.2f});
""")

s = "past"; tol = aw(s, "old light"); tpa = aw(s, "the past")
scenes[s] = scene_file(s, OV, f"""
  {chip('pa-c', 'LOOK UP = LOOK BACK')}
  {tag('pa-a', 'old light', 720, 290, 'font-size:56px;color:' + C['red'])}
  {note('pa-n', 'a window into the <span class="hl">past</span>')}
""", f"""
pop("#pa-c", 0.05); pop("#pa-a", {tol:.2f}, {{from:{{scale:1.6, rotation:10}}, to:{{rotation:3}}}}); rise("#pa-n", {tpa-0.4:.2f});
""")

s = "andromeda"; tan = aw(s, "Andromeda galaxy"); t25 = aw(s, "two and a half million"); tte = aw(s, "telescope")
scenes[s] = scene_file(s, OV, f"""
  {chip('an-c', 'ANDROMEDA')}
  {gauge('an-g', '2.5 million light years', 300, 290, 'font-size:56px;color:' + C['blue'])}
  {note('an-n', 'looking at <span class="hl">Earth</span>...')}
""", f"""
pop("#an-c", {tan-0.2:.2f}); pop("#an-g", {t25:.2f}, {{from:{{scale:1.5, rotation:8}}, to:{{rotation:2}}}});
rise("#an-n", {tte-0.2:.2f});
""")

s = "ancestors"; tci = aw(s, "not see cities"); tst = aw(s, "stone tools")
scenes[s] = scene_file(s, OV, f"""
  {chip('ac-c', 'EARTH, SEEN FROM THERE')}
  {tag('ac-a', 'no cities', 720, 290, 'color:' + C['red'])}
  {note('ac-n', 'the first <span class="hl">stone tools</span>')}
""", f"""
pop("#ac-c", 0.05); pop("#ac-a", {tci:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
tl.to("#ac-a", {{opacity:0, duration:0.25}}, {tst-1.2:.2f}); rise("#ac-n", {tst-0.3:.2f});
""")

s = "lonely"; thl = aw(s, "A hello"); tmy = aw(s, "millions of years")
scenes[s] = scene_file(s, OV, f"""
  {chip('lo-c', 'A LONELY UNIVERSE')}
  {tag('lo-a', 'star to star: years', 440, 290)}
  {tag('lo-b', 'galaxy to galaxy: millions', 380, 400, 'color:' + C['red'])}
""", f"""
pop("#lo-c", 0.05); pop("#lo-a", {thl:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#lo-b", {tmy-0.3:.2f}, {{from:{{scale:1.4, rotation:8}}, to:{{rotation:2}}}});
""")

s = "outro"; tbig = aw(s, "unbelievably big"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'LIGHT IS FAST. SPACE IS <span class="blue">HUGE</span>.')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">look up, look back</div></div>
""", f"""
pop("#ou-c", {tbig-0.4:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "So why"), g("hook", "out in space"))
point(g("hook", "take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("fast", "three hundred thousand"), 1.2)
wow(g("sun", "eight minutes and twenty seconds"), 1.0)
point(g("nearest", "Proxima Centauri"), 1.2)
wow(g("voyager", "seventy five thousand"), 1.0)
point(g("galaxy", "one hundred thousand light years"), 1.2)
think(g("past", "When you look up"), g("past", "the past") + 0.4)
point(g("andromeda", "two and a half million"), 1.2)
wow(g("ancestors", "stone tools"), 1.0)
think(g("lonely", "so lonely"), g("lonely", "takes years"))
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "seven and a half"), 0.45), ("ping.mp3", A("hook", "take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("fast", "three hundred thousand"), 0.45),
        ("impact-bass-1.mp3", A("sun", "eight minutes and twenty seconds"), 0.35), ("click.mp3", A("nearest", "Proxima Centauri"), 0.4),
        ("impact-bass-2.mp3", A("voyager", "seventy five thousand"), 0.35), ("pop.mp3", A("galaxy", "one hundred thousand light years"), 0.45),
        ("ping.mp3", A("past", "old light"), 0.35), ("pop.mp3", A("andromeda", "two and a half million"), 0.45),
        ("click-soft.mp3", A("ancestors", "stone tools"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
