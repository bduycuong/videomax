# Is skipping glasses harmful or helpful when you're nearsighted? Doodle overlays on the source footage. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.gag {{ position:absolute; font-family:'Gochi Hand',cursive; font-size:90px; color:{C['red']}; text-shadow:4px 4px 0 #FFFFFF; opacity:0; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; th = aw(s, "hurting your eyes"); tw = aw(s, "a workout"); tg = aw(s, "Take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">No glasses: <span class="hl">harm</span> or <span class="hl">help</span>?</div>
  {tag('hk-a', 'hurting?', 60, 280)}
  {tag('hk-b', 'a workout?', 700, 280)}
  <div id="hk-n" class="note">take a <span class="hl">guess</span>!</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {th:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#hk-b", {tw:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#hk-n", {tg:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tf = aw(s, "eye focuses")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">how an eye <span class="hl">focuses</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tf:.2f});
""")

s = "focus"; tc = aw(s, "the cornea"); tl = aw(s, "the lens"); tr = aw(s, "on the retina")
scenes[s] = scene_file(s, OV, f"""
  {chip('fc-c', 'HOW FOCUS WORKS')}
  {tag('fc-a', '1 cornea', 60, 290)}
  {tag('fc-b', '2 lens', 360, 290)}
  {tag('fc-r', '3 retina', 620, 290)}
  <div id="fc-n" class="note">picture lands <span class="hl">on</span> the retina</div>
""", f"""
pop("#fc-c", 0.05); pop("#fc-a", {tc:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#fc-b", {tl:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
pop("#fc-r", {tr:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#fc-n", {tr+0.4:.2f});
""")

s = "long"; tlo = aw(s, "too long"); tfr = aw(s, "in front of"); tb = aw(s, "turn blurry")
scenes[s] = scene_file(s, OV, f"""
  {chip('lg-c', 'NEARSIGHTED EYE')}
  {tag('lg-t', 'eyeball too long', 520, 790)}
  <div id="lg-x" class="gag" style="left:640px;top:270px;transform:rotate(-8deg)">BLURRY!</div>
  <div id="lg-n" class="note">focus lands <span class="hl">in front</span></div>
""", f"""
pop("#lg-c", 0.05); pop("#lg-t", {tlo:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#lg-n", {tfr:.2f});
pop("#lg-x", {tb:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}});
""")

s = "shrink"; tk = aw(s, "key part"); ts = aw(s, "shrink that eyeball"); twe = aw(s, "wear off")
scenes[s] = scene_file(s, OV, f"""
  {chip('sh-c', 'THE KEY PART')}
  {tag('sh-t', '<s style="color:'+C['red']+'">rest = cure</s>', 600, 290)}
  <div id="sh-n" class="note">it doesn't <span class="hl">wear off</span></div>
""", f"""
pop("#sh-c", {tk:.2f}); pop("#sh-t", {ts:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-4}}}}); rise("#sh-n", {twe:.2f});
""")

s = "myth"; tf_ = aw(s, "eyes weaker"); tmy = aw(s, "a myth"); tbe = aw(s, "bend the light")
scenes[s] = scene_file(s, OV, f"""
  {chip('my-c', 'MYTH CHECK')}
  {tag('my-a', 'glasses make eyes weaker', 60, 290)}
  <div id="my-x" class="gag" style="left:600px;top:380px;transform:rotate(-8deg)">MYTH!</div>
  <div id="my-n" class="note">lenses just <span class="hl">bend light</span></div>
""", f"""
pop("#my-c", 0.05); pop("#my-a", {tf_:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#my-x", {tmy:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#my-n", {tbe:.2f});
""")

s = "answer"; tad = aw(s, "most adults"); tle = aw(s, "less clearly")
scenes[s] = scene_file(s, OV, f"""
  {chip('an-c', 'THE ANSWER')}
  {tag('an-t', 'no harm · no cure', 560, 790)}
  <div id="an-n" class="note">you just see <span class="hl">less clearly</span></div>
""", f"""
pop("#an-c", {tad-0.3:.2f}); pop("#an-t", {tad+0.8:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#an-n", {tle:.2f});
""")

s = "squint"; tsq = aw(s, "means squinting"); tp = aw(s, "tiny peephole"); thd = aw(s, "headaches")
scenes[s] = scene_file(s, OV, f"""
  {chip('sq-c', 'THE SQUINT TRAP')}
  {tag('sq-t', 'tiny peephole', 640, 300)}
  <div id="sq-n" class="note">tired eyes + <span class="hl">headaches</span></div>
""", f"""
pop("#sq-c", {tsq:.2f}); pop("#sq-t", {tp:.2f}, {{from:{{rotation:14}}, to:{{rotation:4}}}}); rise("#sq-n", {thd:.2f});
""")

s = "kids"; tbr = aw(s, "bigger risk"); tbe2 = aw(s, "better eye"); tlz = aw(s, "lazy eye"); te = aw(s, "early really")
scenes[s] = scene_file(s, OV, f"""
  {chip('kd-c', 'KIDS: BIGGER RISK')}
  {tag('kd-t', 'lazy eye', 700, 300)}
  <div id="kd-n" class="note">treat it <span class="hl">early</span></div>
""", f"""
pop("#kd-c", {tbr:.2f}); pop("#kd-t", {tlz:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#kd-n", {te:.2f});
""")

s = "rules"; tpl = aw(s, "doctor's plan"); tfa = aw(s, "far away")
scenes[s] = scene_file(s, OV, f"""
  {chip('ru-c', 'SO WHAT DO I DO?')}
  {tag('ru-a', "doctor's plan", 60, 290)}
  {tag('ru-b', 'far away = wear', 600, 290)}
""", f"""
pop("#ru-c", 0.05); pop("#ru-a", {tpl:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#ru-b", {tfa:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
""")

s = "outro"; tsk = aw(s, "Skipping glasses"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', "WON'T HEAL · WON'T RUIN")}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tsk:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "If you're"), g("hook", "that helps"))
point(g("hook", "Take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("focus", "on the retina"), 1.2)
wow(g("long", "too long"), 1.2)
point(g("shrink", "shrink that eyeball"), 1.2)
wow(g("myth", "a myth"), 1.2)
point(g("answer", "less clearly"), 1.0)
point(g("squint", "tiny peephole"), 1.2)
wow(g("kids", "lazy eye"), 1.2)
point(g("rules", "far away"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "hurting your eyes"), 0.45), ("pop.mp3", A("hook", "a workout"), 0.45), ("ping.mp3", A("hook", "Take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("focus", "the cornea"), 0.4), ("click.mp3", A("focus", "the lens"), 0.4),
        ("ping.mp3", A("focus", "on the retina"), 0.35), ("whoosh-short.mp3", A("long", "turn blurry"), 0.45),
        ("impact-bass-1.mp3", A("myth", "a myth"), 0.35), ("pop.mp3", A("squint", "tiny peephole"), 0.45),
        ("riser.mp3", A("kids", "bigger risk"), 0.3), ("ping.mp3", A("kids", "lazy eye"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
