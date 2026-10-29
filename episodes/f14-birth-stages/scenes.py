# What really happens during childbirth? Doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; tg = aw(s, "every guy"); tw = aw(s, "is wild"); tq = aw(s, "how wide")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">Childbirth: <span class="hl">what really happens?</span></div>
  {tag('hk-a', 'how wide?', 640, 790)}
  <div id="hk-n" class="note">take a <span class="hl">guess</span>!</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {tq:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#hk-n", {tq+0.6:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); t3 = aw(s, "three stages")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note"><span class="hl">3 stages</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {t3:.2f});
""")

s = "squeeze"; tc = aw(s, "called contractions"); tcv = aw(s, "the cervix")
scenes[s] = scene_file(s, OV, f"""
  {chip('sq-c', 'STAGE 1 · OPENING')}
  {tag('sq-t', 'squeeze… relax… squeeze', 60, 790)}
  <div id="sq-n" class="note">head presses on the <span class="hl">cervix</span></div>
""", f"""
pop("#sq-c", 0.05); pop("#sq-t", {tc:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#sq-n", {tcv:.2f});
""")

s = "open"; tth = aw(s, "thins and opens"); t10 = aw(s, "ten centimeters"); tbg = aw(s, "a bagel")
scenes[s] = scene_file(s, OV, f"""
  {chip('op-c', 'STAGE 1 · OPENING')}
  {tag('op-t', '≈ 10 cm', 760, 270, 'font-size:64px;color:' + C['red'])}
  <div id="op-n" class="note">≈ 4 inches · a <span class="hl">bagel</span></div>
""", f"""
pop("#op-c", 0.05); pop("#op-t", {t10:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#op-n", {tbg-0.6:.2f});
""")

s = "hours"; tf = aw(s, "first baby"); t48 = aw(s, "four to eight")
scenes[s] = scene_file(s, OV, f"""
  {chip('hr-c', 'STAGE 1 · THE LONG PART')}
  {tag('hr-t', '4–8 hours or more', 560, 790, 'color:' + C['red'])}
  <div id="hr-n" class="note">longest with a <span class="hl">first baby</span></div>
""", f"""
pop("#hr-c", 0.05); rise("#hr-n", {tf:.2f}); pop("#hr-t", {t48:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}});
""")

s = "push"; tp = aw(s, "pushing"); tt = aw(s, "tightest part")
scenes[s] = scene_file(s, OV, f"""
  {chip('pu-c', 'STAGE 2 · PUSHING')}
  {tag('pu-t', 'turn + squeeze', 620, 790)}
  <div id="pu-n" class="note">the <span class="hl">tightest</span> part</div>
""", f"""
pop("#pu-c", {tp-0.2:.2f}); pop("#pu-t", {tp+1.0:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#pu-n", {tt:.2f});
""")

s = "born"; tfm = aw(s, "few minutes"); tb = aw(s, "is born")
scenes[s] = scene_file(s, OV, f"""
  {chip('bn-c', 'STAGE 2 · BIRTH')}
  <div id="bn-n" class="note">minutes … or <span class="hl">hours</span></div>
  {tag('bn-t', 'hello, baby!', 640, 790)}
""", f"""
pop("#bn-c", 0.05); rise("#bn-n", {tfm:.2f}); pop("#bn-t", {tb:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

s = "placenta"; tpl = aw(s, "the placenta"); t30 = aw(s, "thirty minutes")
scenes[s] = scene_file(s, OV, f"""
  {chip('pl-c', 'STAGE 3 · PLACENTA')}
  {tag('pl-t', "baby's food supply", 60, 790)}
  <div id="pl-n" class="note">usually within <span class="hl">30 min</span></div>
""", f"""
pop("#pl-c", {tpl-0.3:.2f}); pop("#pl-t", {tpl+0.6:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#pl-n", {t30:.2f});
""")

s = "support"; tg = aw(s, "where do"); t15 = aw(s, "fifteen thousand"); tsh = aw(s, "a bit shorter"); tce = aw(s, "fewer cesarean"); tfb = aw(s, "felt better")
scenes[s] = scene_file(s, OV, f"""
  {chip('sp-c', 'WHERE DO GUYS COME IN?')}
  {tag('sp-a', '15,000+ women studied', 60, 270)}
  {tag('sp-b', 'shorter labor', 60, 790)}
  {tag('sp-d', 'fewer C-sections', 440, 790)}
  <div id="sp-n" class="note">moms felt <span class="hl">better</span></div>
""", f"""
pop("#sp-c", {tg:.2f}); pop("#sp-a", {t15:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#sp-b", {tsh:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); pop("#sp-d", {tce:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
rise("#sp-n", {tfb:.2f});
""")

s = "help"; th = aw(s, "hold her hand"); tbr = aw(s, "help her breathe"); trb = aw(s, "rub her back"); tpr = aw(s, "pain relief")
scenes[s] = scene_file(s, OV, f"""
  {chip('hp-c', 'HOW TO HELP')}
  {tag('hp-a', 'hold hands', 60, 270)}
  {tag('hp-b', 'breathe together', 330, 270)}
  {tag('hp-d', 'back rubs', 760, 270)}
  <div id="hp-n" class="note">she decides on <span class="hl">pain relief</span></div>
""", f"""
pop("#hp-c", 0.05); pop("#hp-a", {th:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); pop("#hp-b", {tbr:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
pop("#hp-d", {trb:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#hp-n", {tpr-0.4:.2f});
""")

s = "outro"; to = aw(s, "one person"); tsu = aw(s, "show up"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'NOT A ONE-PERSON JOB')}
  <div id="ou-n" class="note">learn it · <span class="hl">show up</span></div>
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {to:.2f}); rise("#ou-n", {tsu-0.4:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "how wide"), g("hook", "how wide") + 2.0)
wave(g("intro", "I'm Max"))
point(g("squeeze", "called contractions"), 1.2)
wow(g("open", "ten centimeters"), 1.2)
point(g("hours", "four to eight"), 1.2)
point(g("push", "tightest part"), 1.2)
wow(g("born", "is born"), 1.2)
point(g("placenta", "the placenta"), 1.2)
think(g("support", "where do"), g("support", "a big"))
point(g("support", "fewer cesarean"), 1.2)
point(g("help", "hold her hand"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "how wide"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("squeeze", "called contractions"), 0.45),
        ("impact-bass-1.mp3", A("open", "ten centimeters"), 0.35), ("pop.mp3", A("hours", "four to eight"), 0.45), ("pop.mp3", A("push", "pushing"), 0.4),
        ("sparkle.mp3", A("born", "is born"), 0.4), ("pop.mp3", A("placenta", "the placenta"), 0.45), ("click.mp3", A("support", "fifteen thousand"), 0.45),
        ("pop.mp3", A("support", "fewer cesarean"), 0.45), ("pop.mp3", A("help", "hold her hand"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
