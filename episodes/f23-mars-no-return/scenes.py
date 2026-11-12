# Mars no return: doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
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



s = "hook"; t7 = aw(s, "seven months"); tnh = aw(s, "never come home"); tq = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; opacity:0; }", f"""
  <div id="hk-t" class="h1">A trip to <span class="hl">Mars</span></div>
  {gauge('hk-g', '~7 months', 600, 270)}
  <div id="hk-a" class="sticky" style="left:60px;top:420px;background:{C['hi']}">no fuel?</div>
  <div id="hk-b" class="sticky" style="left:60px;top:560px;background:#C9E8C2">bad air?</div>
  <div id="hk-c" class="sticky" style="left:60px;top:700px;background:#F6C9C2">wrong timing?</div>
  {note('hk-n', 'your <span class="hl">guess?</span>')}
""", f"""
pop("#hk-t", 0.3); pop("#hk-g", {t7:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
tl.to("#hk-g", {{opacity:0, duration:0.25}}, {tnh-0.2:.2f});
pop("#hk-a", {tq-1.2:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
pop("#hk-b", {tq-0.7:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#hk-c", {tq-0.2:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}});
rise("#hk-n", {tq:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tst = aw(s, "step outside")
scenes[s] = scene_file(s, OV, f"""
  {chip('in-c', 'MAX WISE')}
  {note('in-n', 'let’s step <span class="hl">outside</span>')}
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tst-0.3:.2f});
""")

s = "air"; tth = aw(s, "so thin"); t1 = aw(s, "less than one percent"); tbo = aw(s, "boil")
scenes[s] = scene_file(s, OV, f"""
  {chip('ai-c', 'PROBLEM 1: THE AIR')}
  {gauge('ai-g', '&lt; 1% of Earth’s', 520, 290, 'color:' + C['blue'])}
  {tag('ai-a', 'spit would BOIL', 600, 420, 'color:' + C['red'])}
  {note('ai-n', 'air pressure: almost <span class="hl">none</span>')}
""", f"""
pop("#ai-c", 0.05); rise("#ai-n", {tth:.2f}); pop("#ai-g", {t1:.2f}, {{from:{{scale:1.6, rotation:-10}}, to:{{rotation:-3}}}});
pop("#ai-a", {tbo-0.2:.2f}, {{from:{{scale:1.4, rotation:10}}, to:{{rotation:3}}}});
""")

s = "gravity"; t38 = aw(s, "thirty eight percent"); t3 = aw(s, "three times higher"); twk = aw(s, "weakens bones")
scenes[s] = scene_file(s, OV, f"""
  {chip('gr-c', 'PROBLEM 2: GRAVITY')}
  {gauge('gr-g', '38% gravity', 560, 290)}
  {tag('gr-a', 'jump ~3x higher', 640, 410, 'color:' + C['blue'])}
  {note('gr-n', 'bones + muscles <span class="hl">weaken</span>')}
""", f"""
pop("#gr-c", 0.05); pop("#gr-g", {t38:.2f}, {{from:{{scale:1.6, rotation:10}}, to:{{rotation:3}}}});
pop("#gr-a", {t3:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#gr-n", {twk-0.3:.2f});
""")

s = "shield"; tmf = aw(s, "magnetic field"); trd = aw(s, "space radiation")
scenes[s] = scene_file(s, OV, f"""
  {chip('sh-c', 'PROBLEM 3: RADIATION')}
  {tag('sh-a', 'no magnetic shield', 560, 290)}
  {tag('sh-b', 'thin air', 760, 400)}
  {note('sh-n', 'more <span class="hl">radiation</span> at the ground')}
""", f"""
pop("#sh-c", 0.05); pop("#sh-a", {tmf-0.3:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#sh-b", {tmf+0.6:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}}); rise("#sh-n", {trd-0.2:.2f});
""")

s = "call"; tch = aw(s, "call home"); t3m = aw(s, "three to twenty two minutes")
scenes[s] = scene_file(s, OV, f"""
  {chip('ca-c', 'CALLING EARTH...')}
  {gauge('ca-g', '3 – 22 min', 600, 290, 'color:' + C['red'])}
  {note('ca-n', 'one way, at the speed of <span class="hl">light</span>')}
""", f"""
pop("#ca-c", {tch-0.3:.2f}); pop("#ca-g", {t3m:.2f}, {{from:{{scale:1.6, rotation:-12}}, to:{{rotation:-3}}}});
rise("#ca-n", {t3m+1.2:.2f});
""")

s = "rocket"; tbg = aw(s, "biggest problem"); tno = aw(s, "No rocket"); t0 = aw(s, "Not one")
scenes[s] = scene_file(s, OV, f"""
  {chip('ro-c', 'THE BIGGEST PROBLEM')}
  {gauge('ro-g', 'launches from Mars: 0', 380, 290, 'color:' + C['red'])}
  {note('ro-n', '<span class="hl">not one</span>, ever')}
""", f"""
pop("#ro-c", {tbg-0.3:.2f}); pop("#ro-g", {tno:.2f}, {{from:{{scale:1.5, rotation:8}}, to:{{rotation:2}}}});
rise("#ro-n", {t0-0.2:.2f});
""")

s = "fuel"; tsh = aw(s, "from Earth"); tpv = aw(s, "Perseverance rover"); t122 = aw(s, "one hundred twenty two grams"); tdg = aw(s, "small dog")
scenes[s] = scene_file(s, OV, f"""
  {chip('fu-c', 'FUEL + OXYGEN FOR HOME')}
  {tag('fu-a', 'ship it, or make it there', 400, 290)}
  {gauge('fu-g', '122 g of oxygen', 520, 400, 'color:' + C['blue'])}
  {note('fu-n', '= a small dog, <span class="hl">10 hours</span>')}
""", f"""
pop("#fu-c", 0.05); pop("#fu-a", {tsh-0.4:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
tl.to("#fu-a", {{opacity:0, duration:0.25}}, {tpv:.2f});
pop("#fu-g", {t122:.2f}, {{from:{{scale:1.6, rotation:10}}, to:{{rotation:3}}}}); rise("#fu-n", {tdg-0.3:.2f});
""")

s = "window"; t26 = aw(s, "twenty six months"); t3y = aw(s, "close to three years")
scenes[s] = scene_file(s, OV, f"""
  {chip('wi-c', 'THE LAUNCH WINDOW')}
  {gauge('wi-g', 'every ~26 months', 480, 290)}
  {note('wi-n', 'round trip: almost <span class="hl">3 years</span>')}
""", f"""
pop("#wi-c", 0.05); pop("#wi-g", {t26:.2f}, {{from:{{scale:1.5, rotation:-8}}, to:{{rotation:-2}}}});
rise("#wi-n", {t3y-0.4:.2f});
""")

s = "outro"; thd = aw(s, "Getting there"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'THERE: HARD. BACK: <span class="red">HARDER</span>.')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">next stop: Mars?</div></div>
""", f"""
pop("#ou-c", {thd-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "So why"), g("hook", "never come home"))
point(g("hook", "take a guess"), 1.0)
wave(g("intro", "I'm Max"))
wow(g("air", "boil"), 1.0)
point(g("gravity", "thirty eight percent"), 1.2)
think(g("shield", "Problem three"), g("shield", "magnetic field"))
point(g("call", "three to twenty two minutes"), 1.2)
wow(g("rocket", "Not one"), 1.0)
point(g("fuel", "one hundred twenty two grams"), 1.2)
point(g("window", "twenty six months"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "seven months"), 0.45), ("ping.mp3", A("hook", "take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("air", "less than one percent"), 0.45),
        ("impact-bass-1.mp3", A("air", "boil"), 0.35), ("pop.mp3", A("gravity", "thirty eight percent"), 0.45),
        ("click.mp3", A("shield", "magnetic field"), 0.4), ("ping.mp3", A("call", "three to twenty two minutes"), 0.35),
        ("impact-bass-2.mp3", A("rocket", "No rocket"), 0.35), ("pop.mp3", A("fuel", "one hundred twenty two grams"), 0.45),
        ("click-soft.mp3", A("window", "twenty six months"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
