# Inside the womb, month by month: doodle overlays on the source 3D animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.sticky {{ position:absolute; width:230px; padding:14px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} }}
.big {{ font-family:'Gochi Hand',cursive; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'

s = "hook"; t1 = aw(s, "nine months"); t2 = aw(s, "float and nap"); t3 = aw(s, "Not even close")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:72px; }", f"""
  <div id="hk-t" class="h1">9 months of <span class="hl">what?</span></div>
  <div id="hk-a" class="sticky" style="left:60px;top:300px;background:#DDE3EA;transform:rotate(-6deg)">float?<br>nap?</div>
  <div id="hk-x" class="abs" style="left:700px;top:300px;font-family:'Gochi Hand',cursive;font-size:96px;color:{C['red']};transform:rotate(-8deg);background:#FFFFFF;border:4px solid {K};padding:0 22px;opacity:0">NOPE!</div>
""", f"""
pop("#hk-t", {t1:.2f}); pop("#hk-a", {t2:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-x", {t3:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tm = aw(s, "month by month")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-f', 'month by month', 540, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-f", {tm:.2f});
""")

s = "month1"; tp = aw(s, "poppy seed"); tb = aw(s, "brain and spinal")
scenes[s] = scene_file(s, OV, f"""
  {chip('m1-c', 'MONTH 1')}
  <div id="m1-s" class="sticky" style="left:790px;top:290px;background:{C['hi']};transform:rotate(4deg)">size of a<br>poppy seed</div>
  <div id="m1-n" class="note">building the <span class="hl">brain + spine</span></div>
""", f"""
pop("#m1-c", 0.05); pop("#m1-s", {tp:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); rise("#m1-n", {tb:.2f});
""")

s = "heart"; ta = aw(s, "arms and legs"); th = aw(s, "heart starts"); tn = aw(s, "one hundred ten")
scenes[s] = scene_file(s, OV, f"""
  {chip('ht-c', 'MONTH 2')}
  {tag('ht-a', 'arm + leg buds', 60, 300)}
  <div id="ht-n" class="note"><span class="red">&#9829;</span> <span id="ht-num">0</span> beats / min</div>
""", f"""
pop("#ht-c", 0.05); pop("#ht-a", {ta:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#ht-n", {th:.2f});
count("#ht-num", 0, 110, {tn:.2f}, 1.2, fmtInt);
""")

s = "drink"; td = aw(s, "drinking the water"); tpe = aw(s, "peeing it back"); tg = aw(s, "Gross"); tf = aw(s, "fingerprints")
scenes[s] = scene_file(s, OV, f"""
  {chip('dr-c', 'MONTH 3')}
  <div id="dr-a" class="sticky" style="left:60px;top:290px;background:#C9E2F5;transform:rotate(-4deg)">drink</div>
  <div id="dr-b" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">pee</div>
  <div id="dr-g" class="abs" style="left:420px;top:600px;font-family:'Gochi Hand',cursive;font-size:96px;color:{C['red']};transform:rotate(-6deg);background:#FFFFFF;border:4px solid {K};padding:0 22px;opacity:0">EWW!</div>
  <div id="dr-n" class="note">then: <span class="hl">fingerprints</span></div>
""", f"""
pop("#dr-c", 0.05); pop("#dr-a", {td:.2f}); pop("#dr-b", {tpe:.2f}); pop("#dr-g", {tg:.2f}, {{from:{{scale:0.3, rotation:-25}}, to:{{rotation:-6}}}}); rise("#dr-n", {tf:.2f});
""")

s = "moves"; tbo = aw(s, "Bones get harder"); tfz = aw(s, "fuzzy hair"); tfa = aw(s, "little faces"); tfl = aw(s, "first flutters")
scenes[s] = scene_file(s, OV, f"""
  {chip('mv-c', 'MONTH 4')}
  {tag('mv-1', 'harder bones', 60, 290)}{tag('mv-2', 'fuzzy hair', 700, 290)}
  <div id="mv-n" class="note">mom feels <span class="hl">flutters</span></div>
""", f"""
pop("#mv-c", 0.05); pop("#mv-1", {tbo:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); pop("#mv-2", {tfz:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#mv-n", {tfl:.2f});
""")

s = "hear"; tw2 = aw(s, "twenty two"); thb = aw(s, "heartbeat"); tst = aw(s, "stomach rumbling"); tv = aw(s, "her voice"); tc = aw(s, "calm down")
scenes[s] = scene_file(s, OV, f"""
  {chip('hr-c', 'WEEK 22: HEARING')}
  {tag('hr-1', 'thump thump', 60, 290)}{tag('hr-2', 'GRRR', 760, 290)}{tag('hr-3', 'mom talking', 600, 760)}
  <div id="hr-n" class="note">mom's voice = <span class="hl">calm</span></div>
""", f"""
pop("#hr-c", {tw2:.2f}); pop("#hr-1", {thb:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}}); pop("#hr-2", {tst:.2f}, {{from:{{rotation:14}}, to:{{rotation:4}}}}); pop("#hr-3", {tv:.2f}); rise("#hr-n", {tc:.2f});
""")

s = "coat"; tve = aw(s, "vernix"); tbr = aw(s, "practices breathing"); thi = aw(s, "hiccups")
scenes[s] = scene_file(s, OV, f"""
  {chip('ct-c', 'WATERPROOF SKIN')}
  {tag('ct-t', 'vernix = waxy coat', 60, 290)}
  <div id="ct-h" class="abs" style="left:740px;top:300px;font-family:'Gochi Hand',cursive;font-size:90px;color:{C['blue']};transform:rotate(6deg);background:#FFFFFF;border:4px solid {K};padding:0 22px;opacity:0">HIC!</div>
  <div id="ct-n" class="note">breathing <span class="hl">practice</span></div>
""", f"""
pop("#ct-c", 0.05); pop("#ct-t", {tve:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#ct-n", {tbr:.2f}); pop("#ct-h", {thi:.2f}, {{from:{{scale:0.3, rotation:30}}, to:{{rotation:6}}}});
""")

s = "eyes"; te = aw(s, "eyes can open"); tfat = aw(s, "packing on fat")
scenes[s] = scene_file(s, OV, f"""
  {chip('ey-c', 'MONTH 7')}
  {tag('ey-t', 'eyes open + blink', 600, 290)}
  <div id="ey-n" class="note">fat = <span class="hl">winter jacket</span></div>
""", f"""
pop("#ey-c", 0.05); pop("#ey-t", {te:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#ey-n", {tfat:.2f});
""")

s = "lungs"; tsp = aw(s, "Space runs out"); tsu = aw(s, "surfactant"); tpo = aw(s, "pop open")
scenes[s] = scene_file(s, OV, f"""
  {chip('lg-c', 'MONTH 8')}
  {tag('lg-t', '<s>somersaults</s>', 60, 290)}
  <div id="lg-s" class="sticky" style="left:790px;top:290px;background:#C9E2F5;transform:rotate(4deg)">lung<br>soap</div>
  <div id="lg-n" class="note">ready to <span class="hl">POP</span> open</div>
""", f"""
pop("#lg-c", 0.05); pop("#lg-t", {tsp:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); pop("#lg-s", {tsu:.2f}); rise("#lg-n", {tpo:.2f});
""")

s = "headdown"; tw3 = aw(s, "thirty six"); thd = aw(s, "head down")
scenes[s] = scene_file(s, OV, f"""
  {chip('hd-c', 'WEEK 36')}
  <div id="hd-n" class="note"><span class="hl">head down</span>, ready!</div>
""", f"""
pop("#hd-c", {tw3:.2f}); rise("#hd-n", {thd:.2f});
""")

s = "birth"; tfw = aw(s, "forty weeks"); ttw = aw(s, "twists and turns"); tcr = aw(s, "first cry")
scenes[s] = scene_file(s, OV, f"""
  {chip('bi-c', 'WEEK 40')}
  {tag('bi-t', 'twist + turn', 60, 290)}
  <div id="bi-n" class="note">first <span class="red">WAAAH!</span></div>
""", f"""
pop("#bi-c", {tfw:.2f}); pop("#bi-t", {ttw:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#bi-n", {tcr:.2f});
""")

s = "outro"; t1 = aw(s, "single cell"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', '1 CELL &rarr; 1 BABY')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">40 weeks, one busy baby</div></div>
""", f"""
pop("#ou-c", {t1:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "What does"), g("hook", "Not even close"))
wave(g("intro", "I'm Max"))
point(g("month1", "poppy seed"), 1.2)
wow(g("heart", "heart starts"), 1.0)
wow(g("drink", "Gross"), 1.0)
point(g("moves", "first flutters"), 1.2)
point(g("hear", "her voice"), 1.2)
wow(g("coat", "hiccups"), 1.0)
point(g("eyes", "eyes can open"), 1.2)
point(g("lungs", "surfactant"), 1.2)
point(g("headdown", "head down"), 1.2)
wow(g("birth", "first cry"), 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "float and nap"), 0.45), ("impact-bass-1.mp3", A("hook", "Not even close"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("ping.mp3", A("month1", "poppy seed"), 0.35), ("click.mp3", A("heart", "heart starts"), 0.4), ("pop.mp3", A("drink", "Gross"), 0.45),
        ("pop.mp3", A("moves", "fuzzy hair"), 0.45), ("click-soft.mp3", A("hear", "heartbeat"), 0.5), ("pop.mp3", A("coat", "hiccups"), 0.45),
        ("click.mp3", A("lungs", "surfactant"), 0.4), ("riser.mp3", A("birth", "big day"), 0.25), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
