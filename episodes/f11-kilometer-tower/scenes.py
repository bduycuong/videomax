# Why is a one-kilometer skyscraper so hard to build? (Jeddah Tower) Doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
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

s = "hook"; tk = aw(s, "one whole kilometer"); th = aw(s, "so hard")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">A <span class="hl">1 km</span> tall building?</div>
  {tag('hk-a', '1,000 m!', 700, 290)}
  <div id="hk-n" class="note">why is it <span class="hl">so hard?</span></div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {tk:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-3}}}}); rise("#hk-n", {th-0.3:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tj = aw(s, "Jeddah Tower")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-t', 'Jeddah Tower', 620, 290)}
  <div id="in-n" class="note">one <span class="hl">problem</span> at a time</div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-t", {tj:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#in-n", {tj+0.6:.2f});
""")

s = "pause"; t13 = aw(s, "twenty thirteen"); t18 = aw(s, "twenty eighteen"); t25 = aw(s, "twenty twenty five")
scenes[s] = scene_file(s, OV, f"""
  {chip('pa-c', 'A LONG PAUSE')}
  {tag('pa-a', '2013 start', 40, 290)}
  {tag('pa-b', '2018 stop', 380, 290, 'background:#FFC9C2;')}
  {tag('pa-d', '2025 restart', 700, 290, 'background:#C9E8C2;')}
""", f"""
pop("#pa-c", 0.05); pop("#pa-a", {t13:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#pa-b", {t18:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#pa-d", {t25:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}});
""")

s = "join"; tn = aw(s, "brand new concrete"); tst = aw(s, "like stitches")
scenes[s] = scene_file(s, OV, f"""
  {chip('jn-c', 'PROBLEM 1: OLD + NEW')}
  {tag('jn-a', 'old', 60, 290)}
  {tag('jn-b', 'new', 900, 290, 'background:'+C['hi']+';')}
  <div id="jn-n" class="note">steel <span class="hl">stitches</span></div>
""", f"""
pop("#jn-c", 0.05); pop("#jn-a", {tn-0.6:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); pop("#jn-b", {tn:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
rise("#jn-n", {tst:.2f});
""")

s = "weight"; t860 = aw(s, "eight hundred sixty thousand"); ttl = aw(s, "could tilt")
scenes[s] = scene_file(s, OV, f"""
  {chip('wt-c', 'PROBLEM 2: WEIGHT')}
  {tag('wt-a', '≈ 860,000 tonnes', 560, 290)}
  <div id="wt-x" class="gag" style="left:80px;top:290px;transform:rotate(-8deg)">TILT?!</div>
  <div id="wt-n" class="note">sink <span class="hl">evenly</span>, or tilt</div>
""", f"""
pop("#wt-c", 0.05); pop("#wt-a", {t860:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}});
pop("#wt-x", {ttl:.2f}, {{from:{{scale:0.3, rotation:-25}}, to:{{rotation:-8}}}}); rise("#wt-n", {ttl+0.3:.2f});
""")

s = "piles"; t270 = aw(s, "two hundred seventy"); tdp = aw(s, "into the rock")
scenes[s] = scene_file(s, OV, f"""
  {chip('pl-c', 'THE FIX: PILES')}
  {tag('pl-a', '270 piles', 700, 290)}
  <div id="pl-n" class="note">pushed deep into <span class="hl">rock</span></div>
""", f"""
pop("#pl-c", 0.05); pop("#pl-a", {t270:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#pl-n", {tdp-0.3:.2f});
""")

s = "deep"; t105 = aw(s, "one hundred five"); t45 = aw(s, "forty five"); tev = aw(s, "settles evenly")
scenes[s] = scene_file(s, OV, f"""
  {chip('dp-c', 'LONGER IN THE MIDDLE')}
  {tag('dp-a', 'middle ≈ 105 m', 300, 790, 'background:'+C['hi']+';')}
  {tag('dp-b', 'wing tips ≈ 45 m', 600, 290)}
  <div id="dp-n" class="note">settles <span class="hl">evenly</span></div>
""", f"""
pop("#dp-c", 0.05); pop("#dp-a", {t105:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#dp-b", {t45:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#dp-n", {tev:.2f});
""")

s = "wind"; ty = aw(s, "letter Y"); tco = aw(s, "concrete core")
scenes[s] = scene_file(s, OV, f"""
  {chip('wd-c', 'PROBLEM 3: WIND')}
  <div id="wd-y" class="gag" style="left:70px;top:270px;font-size:120px">Y</div>
  {tag('wd-a', 'concrete core', 620, 790)}
""", f"""
pop("#wd-c", 0.05); pop("#wd-y", {ty:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-4}}}});
pop("#wd-a", {tco:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}});
""")

s = "taper"; tth = aw(s, "gets thinner"); tsw = aw(s, "top sway")
scenes[s] = scene_file(s, OV, f"""
  {chip('tp-c', 'THINNER AS IT RISES')}
  <div id="tp-x" class="gag" style="left:640px;top:280px;transform:rotate(-6deg)">WHOOSH</div>
  <div id="tp-n" class="note">no wobbly <span class="hl">rhythm</span></div>
""", f"""
pop("#tp-c", {tth-0.3:.2f}); pop("#tp-x", {tth+1.5:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-6}}}}); rise("#tp-n", {tsw-0.4:.2f});
""")

s = "lift"; t640 = aw(s, "six hundred forty"); thv = aw(s, "crushingly heavy")
scenes[s] = scene_file(s, OV, f"""
  {chip('lf-c', 'PROBLEM 4: THE ELEVATOR')}
  {tag('lf-a', '≈ 640 m in one go', 560, 290)}
  <div id="lf-x" class="gag" style="left:60px;top:780px;transform:rotate(-6deg)">HEAVY!</div>
""", f"""
pop("#lf-c", 0.05); pop("#lf-a", {t640:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}});
pop("#lf-x", {thv:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-6}}}});
""")

s = "belt"; tcf = aw(s, "carbon fiber"); t86 = aw(s, "eighty six percent")
scenes[s] = scene_file(s, OV, f"""
  {chip('bt-c', 'THE FIX: CARBON FIBER')}
  {tag('bt-a', '86% lighter', 680, 290, 'background:'+C['hi']+';')}
  <div id="bt-n" class="note">lighter than <span class="hl">steel</span></div>
""", f"""
pop("#bt-c", {tcf-0.3:.2f}); pop("#bt-a", {t86:.2f}, {{from:{{rotation:12}}, to:{{rotation:-3}}}}); rise("#bt-n", {t86+0.6:.2f});
""")

s = "outro"; t828 = aw(s, "eight hundred twenty eight"); t170 = aw(s, "one hundred seventy"); t28 = aw(s, "twenty twenty eight"); tsc = aw(s, "Stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'THE RACE TO 1 KM')}
  {tag('ou-a', 'Burj Khalifa: 828 m', 40, 290)}
  {tag('ou-b', '+170 m', 760, 290, 'background:'+C['hi']+';')}
  {tag('ou-d', '~2028?', 760, 790)}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", 0.05); pop("#ou-a", {t828:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#ou-b", {t170:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#ou-d", {t28:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.to("#ou-a, #ou-b, #ou-d", {{opacity:0, duration:0.25}}, {tsc-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "So what makes"), g("hook", "so hard") + 0.6)
wave(g("intro", "I'm Max"))
point(g("pause", "twenty eighteen"), 1.2)
point(g("join", "like stitches"), 1.2)
wow(g("weight", "eight hundred sixty thousand"), 1.3)
point(g("piles", "two hundred seventy"), 1.2)
point(g("deep", "one hundred five"), 1.2)
point(g("wind", "letter Y"), 1.2)
think(g("taper", "gets thinner"), g("taper", "top sway"))
wow(g("lift", "crushingly heavy"), 1.2)
point(g("belt", "eighty six percent"), 1.2)
wow(g("outro", "one hundred seventy"), 1.2)
wave(g("outro", "Stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "one whole kilometer"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click.mp3", A("pause", "twenty thirteen"), 0.4), ("click.mp3", A("pause", "twenty eighteen"), 0.4), ("pop.mp3", A("pause", "twenty twenty five"), 0.45),
        ("pop.mp3", A("join", "like stitches"), 0.45), ("impact-bass-1.mp3", A("weight", "eight hundred sixty thousand"), 0.35),
        ("whoosh-short.mp3", A("weight", "could tilt"), 0.4), ("pop.mp3", A("piles", "two hundred seventy"), 0.45),
        ("click-soft.mp3", A("deep", "one hundred five"), 0.5), ("pop.mp3", A("wind", "letter Y"), 0.45),
        ("impact-bass-2.mp3", A("lift", "crushingly heavy"), 0.35), ("ping.mp3", A("belt", "eighty six percent"), 0.35),
        ("riser.mp3", A("outro", "If all goes"), 0.3), ("sparkle.mp3", A("outro", "Stay curious"), 0.45)]
