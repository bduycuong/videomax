# Do nearsighted eyes "train back" without glasses? Doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; tq = aw(s, "stop wearing"); tt = aw(s, "train themselves"); tg = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:56px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">No glasses = <span class="hl">eye training?</span></div>
  {tag('hk-a', 'glasses OFF', 620, 790, 'color:' + C['red'])}
  <div id="hk-n" class="note">yes or no? <span class="hl">guess!</span></div>
""", f"""
pop("#hk-t", 0.3); pop("#hk-a", {tq:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
rise("#hk-n", {tg-0.6:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); ti = aw(s, "inside the eye")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">inside the <span class="hl">eye</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {ti-0.3:.2f});
""")

s = "camera"; tc = aw(s, "cornea"); tr = aw(s, "retina")
scenes[s] = scene_file(s, OV, f"""
  {chip('ca-c', 'EYE = CAMERA')}
  {tag('ca-a', 'cornea + lens: focus', 60, 270, 'color:' + C['blue'])}
  {tag('ca-b', 'retina: the screen', 600, 790, 'color:' + C['red'])}
  <div id="ca-n" class="note">light in, <span class="hl">picture</span> out</div>
""", f"""
pop("#ca-c", 0.05); pop("#ca-a", {tc:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#ca-b", {tr:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#ca-n", {tr+0.6:.2f});
""")

s = "longeye"; tl2 = aw(s, "too long"); tb = aw(s, "before it reaches"); tbl = aw(s, "turn blurry")
scenes[s] = scene_file(s, OV, f"""
  {chip('lo-c', 'TOO LONG')}
  {tag('lo-a', 'eyeball stretched', 60, 270, 'font-size:50px;color:' + C['red'])}
  {tag('lo-b', 'focus lands too early', 560, 790, 'color:' + C['blue'])}
  <div id="lo-n" class="note">far away = <span class="hl">blurry</span></div>
""", f"""
pop("#lo-c", 0.05); pop("#lo-a", {tl2:.2f}, {{from:{{scale:1.6, rotation:-10}}, to:{{rotation:-2}}}});
pop("#lo-b", {tb:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#lo-n", {tbl-0.4:.2f});
""")

s = "myth"; ts = aw(s, "can't shrink"); tg2 = aw(s, "guessing fuzzy shapes")
scenes[s] = scene_file(s, OV, f"""
  {chip('my-c', 'MYTH')}
  {tag('my-a', 'eyes train back', 60, 270, 'font-size:54px')}
  <svg id="my-x" class="abs" style="left:40px;top:262px;overflow:visible" width="460" height="90"><path id="my-xp" d="M10 70 L450 20" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/></svg>
  {tag('my-b', 'brain guesses better', 560, 790, 'color:' + C['blue'])}
  <div id="my-n" class="note">the eyeball <span class="hl">stays long</span></div>
""", f"""
pop("#my-c", 0.05); pop("#my-a", 0.3, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
ink("#my-xp", {ts:.2f}, 0.4); rise("#my-n", {ts+0.6:.2f});
pop("#my-b", {tg2:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
""")

s = "lens"; tsp = aw(s, "spread the light"); tw = aw(s, "not make your eyes worse")
scenes[s] = scene_file(s, OV, f"""
  {chip('le-c', 'WHAT GLASSES DO')}
  {tag('le-a', 'focus moved back onto the retina', 60, 270, 'font-size:40px;color:' + C['blue'])}
  {tag('le-b', "don't make eyes worse", 520, 790, 'font-size:46px;color:' + C['red'])}
  <div id="le-n" class="note"><span class="hl">sharp</span> again</div>
""", f"""
pop("#le-c", 0.05); pop("#le-a", {tsp:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}}); rise("#le-n", {tsp+1.5:.2f});
pop("#le-b", {tw:.2f}, {{from:{{scale:1.6, rotation:10}}, to:{{rotation:2}}}});
""")

s = "adult"; tsee = aw(s, "don't see well"); td = aw(s, "when you drive")
scenes[s] = scene_file(s, OV, f"""
  {chip('ad-c', 'ADULTS')}
  {tag('ad-a', 'just blurry', 640, 270, 'font-size:54px;color:' + C['blue'])}
  <div id="ad-n" class="note">driving? <span class="hl">wear them</span></div>
""", f"""
pop("#ad-c", 0.05); pop("#ad-a", {tsee:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#ad-n", {td-0.3:.2f});
""")

s = "kids"; tw2 = aw(s, "weaker lenses"); tsl = aw(s, "doesn't slow"); tsu = aw(s, "speed it up")
scenes[s] = scene_file(s, OV, f"""
  {chip('ki-c', 'KIDS')}
  {tag('ki-a', 'weaker lenses on purpose?', 60, 270, 'font-size:44px')}
  {tag('ki-b', 'NOT a safe trick', 600, 790, 'font-size:50px;color:' + C['red'])}
  <div id="ki-n" class="note">may even <span class="hl">speed it up</span></div>
""", f"""
pop("#ki-c", 0.05); pop("#ki-a", {tw2:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#ki-b", {tsl-0.8:.2f}, {{from:{{scale:1.7, rotation:12}}, to:{{rotation:3}}}}); rise("#ki-n", {tsu-0.5:.2f});
""")

s = "lazy"; to1 = aw(s, "one eye"); tig = aw(s, "ignoring that eye"); tle = aw(s, "lazy eye"); te = aw(s, "caught early")
scenes[s] = scene_file(s, OV, f"""
  {chip('la-c', 'ONE BLURRY EYE')}
  {tag('la-a', 'brain ignores it', 60, 270, 'font-size:50px;color:' + C['red'])}
  {tag('la-b', 'LAZY EYE', 680, 790, 'font-size:60px;color:' + C['blue'])}
  <div id="la-n" class="note">check it <span class="hl">early</span></div>
""", f"""
pop("#la-c", {to1-0.2:.2f}); pop("#la-a", {tig:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#la-b", {tle:.2f}, {{from:{{scale:1.8, rotation:12}}, to:{{rotation:3}}}}); rise("#la-n", {te-0.4:.2f});
""")

s = "outro"; tno = aw(s, "So no"); tc2 = aw(s, "regular eye checks"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'NO: EYES WON’T TRAIN BACK')}
  {tag('ou-a', 'eye checks + the right glasses', 60, 270, 'font-size:42px;color:' + C['blue'])}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tno:.2f}); pop("#ou-a", {tc2:.2f}, {{from:{{scale:1.5, rotation:-8}}, to:{{rotation:-2}}}});
tl.to("#ou-a", {{opacity:0, duration:0.3}}, {tsc-0.4:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "stop wearing"), g("hook", "stop wearing") + 2.0)
point(g("hook", "take a guess"), 1.2)
wave(g("intro", "I'm Max"))
point(g("camera", "retina"), 1.0)
wow(g("longeye", "too long"), 1.2)
point(g("myth", "can't shrink"), 1.2)
point(g("lens", "spread the light"), 1.0)
wow(g("kids", "speed it up"), 1.2)
point(g("lazy", "lazy eye"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "take a guess"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("camera", "retina"), 0.45),
        ("impact-bass-1.mp3", A("longeye", "too long"), 0.35), ("click.mp3", A("myth", "can't shrink"), 0.5), ("pop.mp3", A("lens", "not make your eyes worse"), 0.45),
        ("pop.mp3", A("kids", "doesn't slow"), 0.45), ("impact-bass-2.mp3", A("lazy", "lazy eye"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
