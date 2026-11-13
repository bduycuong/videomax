# Power lines: doodle overlays on the source 3D animation. Footage panel x 20–1060, y 230–898.
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




s = "hook"; tcr = aw(s, "crazy high voltage"); tdc = aw(s, "direct current"); tq = aw(s, "take a guess")
scenes[s] = scene_file(s, OV, f"""
  {chip('hk-c', 'POWER ACROSS A COUNTRY')}
  {tag('hk-v', 'HIGH voltage?', 600, 280, 'color:' + C['red'])}
  {tag('hk-d', 'DC, not AC?', 660, 400, 'color:' + C['blue'])}
  <div id="hk-a" class="sticky" style="left:60px;top:440px;background:{C['hi']}">less heat?</div>
  <div id="hk-b" class="sticky" style="left:60px;top:580px;background:#C9E8C2">cheaper?</div>
  <div id="hk-e" class="sticky" style="left:60px;top:720px;background:#F6C9C2">safer?</div>
  {note('hk-n', 'your <span class="hl">guess?</span>')}
""", f"""
pop("#hk-c", 0.3); pop("#hk-v", {tcr:.2f}, {{from:{{scale:1.5, rotation:-10}}, to:{{rotation:-3}}}});
pop("#hk-d", {tdc:.2f}, {{from:{{scale:1.5, rotation:10}}, to:{{rotation:3}}}});
tl.to(["#hk-v","#hk-d"], {{opacity:0, duration:0.25}}, {tq-1.4:.2f});
pop("#hk-a", {tq-1.2:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
pop("#hk-b", {tq-0.7:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#hk-e", {tq-0.2:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}});
rise("#hk-n", {tq:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tf = aw(s, "follow the power")
scenes[s] = scene_file(s, OV, f"""
  {chip('in-c', 'MAX WISE')}
  {note('in-n', 'follow the <span class="hl">power</span>')}
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tf-0.3:.2f});
""")

s = "power"; tvc = aw(s, "voltage times current"); tlo = aw(s, "lots of current"); tli = aw(s, "a little current")
scenes[s] = scene_file(s, OV, f"""
  {chip('pw-c', 'STEP 1: THE RULE')}
  {gauge('pw-g', 'power = voltage × current', 230, 760)}
  {note('pw-n', 'same power, two ways')}
  <div id="pw-a" class="sticky" style="left:60px;top:300px;width:300px;background:#F6C9C2">low V, BIG current</div>
  <div id="pw-b" class="sticky" style="left:700px;top:300px;width:300px;background:#C9E8C2">high V, small current</div>
""", f"""
pop("#pw-c", 0.05); pop("#pw-g", {tvc-0.3:.2f}, {{from:{{scale:1.4, rotation:-6}}, to:{{rotation:-2}}}});
tl.to("#pw-g", {{opacity:0, duration:0.25}}, {tlo-0.4:.2f});
rise("#pw-n", {tlo-0.3:.2f}); pop("#pw-a", {tlo:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#pw-b", {tli:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
""")

s = "heat"; thot = aw(s, "makes it hot"); tsq = aw(s, "current squared"); tdb = aw(s, "Double the current"); t4 = aw(s, "four times")
scenes[s] = scene_file(s, OV, f"""
  {chip('he-c', 'STEP 2: WIRES GET HOT')}
  {tag('he-a', 'heat lost ∝ current²', 520, 760, 'color:' + C['red'])}
  {gauge('he-g', '2× current → 4× heat', 330, 640, 'color:' + C['red'])}
  {note('he-n', 'wasted as <span class="hl">heat</span>')}
""", f"""
pop("#he-c", 0.05); rise("#he-n", {thot:.2f});
pop("#he-a", {tsq-0.3:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
tl.to("#he-a", {{opacity:0, duration:0.25}}, {tdb-0.3:.2f});
pop("#he-g", {t4-0.2:.2f}, {{from:{{scale:1.6, rotation:8}}, to:{{rotation:2}}}});
""")

s = "voltage"; tcr = aw(s, "crank up"); tlc = aw(s, "less current"); tdn = aw(s, "step it back down")
scenes[s] = scene_file(s, OV, f"""
  {chip('vo-c', 'STEP 3: VOLTAGE UP!')}
  {gauge('vo-g', 'voltage ↑  current ↓  heat ↓', 180, 760, 'color:' + C['blue'])}
  {note('vo-n', 'down again near the <span class="hl">city</span>')}
""", f"""
pop("#vo-c", {tcr-0.3:.2f}, {{from:{{scale:1.5}}, to:{{}}}}); pop("#vo-g", {tlc-0.3:.2f}, {{from:{{scale:1.4, rotation:-6}}, to:{{rotation:-2}}}});
rise("#vo-n", {tdn:.2f});
""")

s = "ac"; tal = aw(s, "alternating current"); t50 = aw(s, "fifty or sixty times")
scenes[s] = scene_file(s, OV, f"""
  {chip('ac-c', 'AC = ALTERNATING CURRENT')}
  {gauge('ac-g', '50 or 60 flips / second', 280, 300, 'color:' + C['red'])}
  {note('ac-n', '← → ← → ← →')}
""", f"""
pop("#ac-c", {tal-0.3:.2f}); pop("#ac-g", {t50:.2f}, {{from:{{scale:1.6, rotation:-10}}, to:{{rotation:-3}}}});
rise("#ac-n", {t50+0.6:.2f});
""")

s = "waste"; tbat = aw(s, "giant battery"); tno = aw(s, "no useful work")
scenes[s] = scene_file(s, OV, f"""
  {chip('wa-c', 'PROBLEM 1: WASTED CURRENT')}
  {tag('wa-a', 'the line = a giant battery', 330, 760)}
  {note('wa-n', 'busy wires, <span class="hl">no useful work</span>')}
""", f"""
pop("#wa-c", 0.05); pop("#wa-a", {tbat-0.4:.2f}, {{from:{{scale:1.4, rotation:-8}}, to:{{rotation:-2}}}});
rise("#wa-n", {tno-0.5:.2f});
""")

s = "sync"; tst = aw(s, "perfect step"); twb = aw(s, "gets wobbly"); tbo = aw(s, "blackout")
scenes[s] = scene_file(s, OV, f"""
  {chip('sy-c', 'PROBLEM 2: KEEP IN STEP')}
  {tag('sy-a', 'in step... in step...', 560, 300)}
  {gauge('sy-g', 'BLACKOUT!', 600, 420, 'color:' + C['red'])}
  {note('sy-n', 'thousands of km = <span class="hl">wobbly</span>')}
""", f"""
pop("#sy-c", 0.05); pop("#sy-a", {tst-0.3:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#sy-n", {twb-0.4:.2f}); tl.to("#sy-a", {{opacity:0, duration:0.25}}, {tbo-0.5:.2f});
pop("#sy-g", {tbo:.2f}, {{from:{{scale:1.8, rotation:10}}, to:{{rotation:4}}}});
""")

s = "dc"; tfx = aw(s, "fixes this"); tone = aw(s, "flows one way"); t50 = aw(s, "up to fifty percent")
scenes[s] = scene_file(s, OV, f"""
  {chip('dc-c', 'DC = DIRECT CURRENT')}
  {tag('dc-a', 'one way only →', 600, 290, 'color:' + C['blue'])}
  {gauge('dc-g', 'up to 50% less loss', 470, 410, 'color:' + C['blue'])}
  {note('dc-n', 'no flips, no <span class="hl">keeping step</span>')}
""", f"""
pop("#dc-c", {tfx-0.3:.2f}, {{from:{{scale:1.5}}, to:{{}}}}); pop("#dc-a", {tone:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#dc-n", {tone+1.0:.2f}); pop("#dc-g", {t50:.2f}, {{from:{{scale:1.6, rotation:8}}, to:{{rotation:2}}}});
""")

s = "cost"; tcv = aw(s, "converter stations"); t60 = aw(s, "up to sixty percent")
scenes[s] = scene_file(s, OV, f"""
  {chip('co-c', 'THE CATCH')}
  {tag('co-a', 'AC → DC → AC', 640, 290)}
  {gauge('co-g', 'up to 60% of the cost', 450, 410, 'color:' + C['red'])}
  {note('co-n', 'giant <span class="hl">converter stations</span>')}
""", f"""
pop("#co-c", 0.05); rise("#co-n", {tcv-0.3:.2f}); pop("#co-a", {tcv+0.4:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}});
pop("#co-g", {t60:.2f}, {{from:{{scale:1.6, rotation:-8}}, to:{{rotation:-2}}}});
""")

s = "outro"; tac = aw(s, "AC wins"); t500 = aw(s, "five hundred kilometers"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'SHORT: AC &nbsp;·&nbsp; 500+ km: <span class="blue">DC</span>')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">voltage up, heat down</div></div>
""", f"""
pop("#ou-c", {t500-0.2:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "Why such"), g("hook", "crazy high voltage"))
point(g("hook", "take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("power", "voltage times current"), 1.2)
wow(g("heat", "four times"), 1.0)
point(g("voltage", "crank up"), 1.2)
point(g("ac", "fifty or sixty times"), 1.2)
think(g("waste", "On a very long line"), g("waste", "giant battery"))
wow(g("sync", "blackout"), 1.0)
point(g("dc", "up to fifty percent"), 1.2)
point(g("cost", "up to sixty percent"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "crazy high voltage"), 0.45), ("ping.mp3", A("hook", "take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("power", "voltage times current"), 0.45),
        ("impact-bass-1.mp3", A("heat", "four times"), 0.35), ("riser.mp3", A("voltage", "crank up"), 0.3),
        ("click.mp3", A("ac", "fifty or sixty times"), 0.4), ("pop.mp3", A("waste", "giant battery"), 0.4),
        ("impact-bass-2.mp3", A("sync", "blackout"), 0.35), ("ping.mp3", A("dc", "up to fifty percent"), 0.4),
        ("click-soft.mp3", A("cost", "up to sixty percent"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
