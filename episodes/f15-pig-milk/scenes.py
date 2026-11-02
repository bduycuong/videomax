# Why does nobody drink pig milk? Doodle overlays on the source cartoon. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;opacity:0;{extra}">{txt}</div>'

s = "hook"; tp = aw(s, "milk all kinds"); tw = aw(s, "why does"); tg = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">Why no <span class="hl">pig milk?</span></div>
  {tag('hk-a', 'gross? dangerous? ...?', 560, 270)}
  <div id="hk-n" class="note">take a <span class="hl">guess</span>!</div>
""", f"""
pop("#hk-t", {tw:.2f}); pop("#hk-a", {tg-2.2:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#hk-n", {tg:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tc = aw(s, "pig milk mystery")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">the <span class="hl">pig milk</span> mystery</div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tc:.2f});
""")

s = "safe"; tsk = aw(s, "make you sick"); tno = aw(s, "no good evidence"); tpg = aw(s, "grow piglets")
scenes[s] = scene_file(s, OV, f"""
  {chip('sf-c', 'IS IT DANGEROUS?')}
  {tag('sf-t', 'myth!', 800, 270, 'font-size:60px;color:' + C['red'])}
  <div id="sf-n" class="note">just milk for <span class="hl">piglets</span></div>
""", f"""
pop("#sf-c", {tsk-1.2:.2f}); pop("#sf-t", {tno:.2f}, {{from:{{rotation:14}}, to:{{rotation:4}}}}); rise("#sf-n", {tpg-0.4:.2f});
""")

s = "taste"; tt = aw(s, "deal breaker"); tr = aw(s, "getting the milk")
scenes[s] = scene_file(s, OV, f"""
  {chip('ts-c', 'IS IT THE TASTE?')}
  {tag('ts-t', 'nope', 820, 270, 'font-size:60px;color:' + C['red'])}
  <div id="ts-n" class="note">the problem: <span class="hl">getting it out</span></div>
""", f"""
pop("#ts-c", 0.05); pop("#ts-t", {tt:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#ts-n", {tr:.2f});
""")

s = "history"; tf = aw(s, "early farmers"); td = aw(s, "dairy animals")
scenes[s] = scene_file(s, OV, f"""
  {chip('hi-c', 'THOUSANDS OF YEARS AGO')}
  <div id="hi-n" class="note">only some became <span class="hl">dairy animals</span></div>
""", f"""
pop("#hi-c", {tf-0.6:.2f}); rise("#hi-n", {td-0.5:.2f});
""")

s = "udder"; tb = aw(s, "the body"); t4 = aw(s, "four large teats"); tmn = aw(s, "several minutes")
scenes[s] = scene_file(s, OV, f"""
  {chip('ud-c', 'THE BODY')}
  {tag('ud-t', 'cow: 1 big udder, 4 big teats', 60, 790)}
  <div id="ud-n" class="note">milk for <span class="hl">minutes</span></div>
""", f"""
pop("#ud-c", {tb-0.3:.2f}); pop("#ud-t", {t4:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#ud-n", {tmn:.2f});
""")

s = "sow"; ts = aw(s, "called a sow"); tr2 = aw(s, "two long rows"); tn = aw(s, "no big udder")
scenes[s] = scene_file(s, OV, f"""
  {chip('sw-c', 'THE BODY')}
  {tag('sw-t', 'sow: 2 rows of small teats', 60, 790)}
  <div id="sw-n" class="note"><span class="hl">no big udder</span></div>
""", f"""
pop("#sw-c", {ts-0.6:.2f}); pop("#sw-t", {tr2:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#sw-n", {tn:.2f});
""")

s = "seconds"; t20 = aw(s, "twenty seconds"); tst = aw(s, "it stops"); t50 = aw(s, "fifty minutes")
scenes[s] = scene_file(s, OV, f"""
  {chip('sc-c', 'THE TIMING')}
  {tag('sc-t', '≈ 20 seconds', 700, 270, 'font-size:64px;color:' + C['red'])}
  {tag('sc-s', 'STOP.', 60, 790, 'font-size:60px')}
  <div id="sc-n" class="note">next round in <span class="hl">≈ 50 min</span></div>
""", f"""
pop("#sc-c", 0.05); pop("#sc-t", {t20:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
pop("#sc-s", {tst:.2f}, {{from:{{scale:1.8, rotation:-12}}, to:{{rotation:-4}}}}); rise("#sc-n", {t50:.2f});
""")

s = "amount"; tm2 = aw(s, "isn't much"); t22 = aw(s, "twenty two pounds"); t66 = aw(s, "sixty six pounds")
scenes[s] = scene_file(s, OV, f"""
  {chip('am-c', 'HOW MUCH MILK?')}
  {tag('am-a', 'sow: ≈ 22 lb a day', 60, 270, 'color:' + C['red'])}
  {tag('am-b', 'cow: ≈ 66 lb a day', 560, 790, 'color:' + C['blue'])}
  <div id="am-n" class="note">the cow wins, <span class="hl">every day</span></div>
""", f"""
pop("#am-c", {tm2:.2f}); pop("#am-a", {t22:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#am-b", {t66:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#am-n", {aw(s, "every single day"):.2f});
""")

s = "angry"; tg2 = aw(s, "guards her babies"); tbt = aw(s, "get bitten")
scenes[s] = scene_file(s, OV, f"""
  {chip('an-c', 'THE ATTITUDE')}
  {tag('an-t', 'GRRR!', 760, 270, 'font-size:68px;color:' + C['red'])}
  <div id="an-n" class="note">protective <span class="hl">mom</span></div>
""", f"""
pop("#an-c", 0.05); rise("#an-n", {tg2:.2f}); pop("#an-t", {tbt-0.6:.2f}, {{from:{{scale:1.8, rotation:14}}, to:{{rotation:4}}}});
""")

s = "outro"; tpo = aw(s, "isn't poison"); tti = aw(s, "tiny teats"); tco = aw(s, "cows simply"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'WHY NO PIG MILK?')}
  {tag('ou-a', 'small teats · 20 s · little milk', 60, 790)}
  <div id="ou-n" class="note">cows got <span class="hl">the job</span></div>
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tpo:.2f}); pop("#ou-a", {tti:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); rise("#ou-n", {tco:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "why does"), g("hook", "why does") + 2.0)
point(g("hook", "take a guess"), 1.2)
wave(g("intro", "I'm Max"))
point(g("safe", "no good evidence"), 1.2)
think(g("history", "early farmers"), g("history", "dairy animals"))
point(g("udder", "four large teats"), 1.2)
point(g("sow", "two long rows"), 1.2)
wow(g("seconds", "twenty seconds"), 1.2)
point(g("amount", "twenty two pounds"), 1.2)
wow(g("amount", "sixty six pounds"), 1.2)
wow(g("angry", "get bitten"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "take a guess"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("safe", "no good evidence"), 0.45),
        ("pop.mp3", A("taste", "deal breaker"), 0.45), ("pop.mp3", A("udder", "four large teats"), 0.45), ("pop.mp3", A("sow", "two long rows"), 0.45),
        ("impact-bass-1.mp3", A("seconds", "twenty seconds"), 0.35), ("click.mp3", A("seconds", "it stops"), 0.5), ("pop.mp3", A("amount", "twenty two pounds"), 0.45),
        ("impact-bass-2.mp3", A("amount", "sixty six pounds"), 0.35), ("pop.mp3", A("angry", "get bitten"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
