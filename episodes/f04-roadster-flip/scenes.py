# Roadster flip: doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.sticky {{ position:absolute; width:230px; padding:14px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def arrow(i, d, color=None, w=7): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color or C["red"]}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/></svg>'

s = "hook"; t1 = aw(s, "upside down"); t2 = aw(s, "flip in midair"); t3 = aw(s, "land on")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:76px; }", f"""
  <div id="hk-t" class="h1">Upside <span class="hl">down</span>?!</div>
  <div id="hk-a" class="sticky" style="left:50px;top:280px;background:{C['hi']};transform:rotate(-6deg)">upside down</div>
  <div id="hk-b" class="sticky" style="left:790px;top:300px;background:#C9E8C2;transform:rotate(5deg)">FLIP!</div>
  {tag('hk-c', 'lands on wheels?', 600, 800)}
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-b", {t2:.2f}, {{from:{{rotation:30}}, to:{{rotation:5}}}});
pop("#hk-c", {t3:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tb = aw(s, "break this stunt")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-f', 'step by step →', 560, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-f", {tb:.2f});
""")

s = "real"; tt = aw(s, "Tesla showed"); to_ = aw(s, "in October"); tx = aw(s, "in Texas")
scenes[s] = scene_file(s, OV, f"""
  {chip('rl-c', 'REAL DEMO <span class="blue">✓</span>')}
  {tag('rl-o', 'this October', 640, 280)}
  <div id="rl-n" class="note">SpaceX test site · <span class="hl">Texas</span></div>
""", f"""
pop("#rl-c", {tt:.2f}); pop("#rl-o", {to_:.2f}, {{from:{{rotation:8}}, to:{{rotation:-2}}}}); rise("#rl-n", {tx:.2f});
""")

s = "problem"; tf = aw(s, "falls off"); tg = aw(s, "gravity wins"); tl_ = aw(s, "lose their grip")
scenes[s] = scene_file(s, OV, f"""
  {chip('pb-c', 'PROBLEM: <span class="red">gravity</span>')}
  {arrow('pb-a', 'M880,300 L880,760 M850,720 L880,770 L910,720', C['red'], 9)}
  {tag('pb-g', 'gravity', 720, 520)}
  <div id="pb-n" class="note">tires: <span class="red">no grip</span></div>
""", f"""
pop("#pb-c", {tf:.2f}); tl.set("#pb-a", {{opacity:1}}, 0); draw("#pb-a", {tg:.2f}, 0.5); pop("#pb-g", {tg+0.3:.2f}); rise("#pb-n", {tl_:.2f});
""")

s = "fans"; tu = aw(s, "underneath"); tp = aw(s, "powerful fans"); ts = aw(s, "suck the air")
arrs = "".join(arrow(f'fn-a{i}', f'M{640+i*120},700 L{640+i*120},560 M{615+i*120},595 L{640+i*120},555 L{665+i*120},595', C['blue'], 7) for i in range(3))
scenes[s] = scene_file(s, OV, f"""
  {chip('fn-c', 'STEP 1 · FANS')}
  {arrs}
  <div id="fn-n" class="note">air sucked <span class="blue">OUT</span></div>
""", f"""
pop("#fn-c", {tu:.2f}); {"".join(f'tl.set("#fn-a{i}", {{opacity:1}}, 0); draw("#fn-a{i}", {ts:.2f}+{i}*0.15, 0.4);' for i in range(3))}
rise("#fn-n", {tp:.2f});
""")

s = "skirt"; tk = aw(s, "a skirt"); tse = aw(s, "seals the gap"); tsn = aw(s, "sneak back")
scenes[s] = scene_file(s, OV, f"""
  {chip('sk-c', 'STEP 2 · SKIRT SEAL')}
  {tag('sk-t', 'sealed edge', 80, 300)}
  <div id="sk-n" class="note">outside air: <span class="red">blocked</span></div>
""", f"""
pop("#sk-c", {tk:.2f}); pop("#sk-t", {tse:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#sk-n", {tsn:.2f});
""")

s = "suction"; tlo = aw(s, "is low"); tpu = aw(s, "pushes it hard"); tst = aw(s, "car stops")
scenes[s] = scene_file(s, OV, f"""
  {chip('su-c', 'SUCTION!')}
  <div id="su-lo" class="sticky" style="left:60px;top:290px;background:#C9E8C2;transform:rotate(-4deg)">low<br>pressure</div>
  <div id="su-hi" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">air<br>pushes</div>
  <div id="su-n" class="note">works even when <span class="hl">stopped</span></div>
""", f"""
pop("#su-c", 0.05); pop("#su-lo", {tlo:.2f}); pop("#su-hi", {tpu:.2f}); rise("#su-n", {tst:.2f});
""")

s = "leave"; tle = aw(s, "leaves the ramp"); tr = aw(s, "air rushes in"); tgo = aw(s, "grip is gone")
scenes[s] = scene_file(s, OV, f"""
  {chip('lv-c', 'OFF THE RAMP')}
  {tag('lv-t', 'air rushes in', 640, 300)}
  <div id="lv-n" class="note">suction = <span class="red">gone</span></div>
""", f"""
pop("#lv-c", {tle:.2f}); pop("#lv-t", {tr:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#lv-n", {tgo:.2f});
""")

s = "tanks"; tc = aw(s, "cold gas thrusters"); tsq = aw(s, "squeezed"); thp = aw(s, "high pressure tanks")
scenes[s] = scene_file(s, OV, f"""
  {chip('tk-c', 'STEP 3 · COLD GAS')}
  {tag('tk-t', 'squeezed air', 80, 300)}
  <div id="tk-n" class="note">stored in <span class="hl">high pressure tanks</span></div>
""", f"""
pop("#tk-c", {tc:.2f}); pop("#tk-t", {tsq:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}}); rise("#tk-n", {thp:.2f});
""")

s = "nozzle"; tv = aw(s, "valve opens"); tbl = aw(s, "blasts out")
scenes[s] = scene_file(s, OV, f"""
  {chip('nz-c', 'VALVE <span class="blue">OPEN</span>')}
  <div id="nz-p" class="abs" style="left:700px;top:300px;font-family:'Gochi Hand',cursive;font-size:110px;color:{C['red']};transform:rotate(-8deg);text-shadow:4px 4px 0 #FFFFFF">PSSHH!</div>
  <div id="nz-n" class="note">gas out of the <span class="hl">nozzle</span></div>
""", f"""
pop("#nz-c", {tv:.2f}); pop("#nz-p", {tbl:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#nz-n", {tbl+0.3:.2f});
""")

s = "thrust"; td = aw(s, "shoots down"); tup = aw(s, "pushed up"); tro = aw(s, "a rocket")
scenes[s] = scene_file(s, OV, f"""
  {chip('th-c', 'ACTION = REACTION')}
  {arrow('th-d', 'M180,420 L180,760 M150,720 L180,770 L210,720', C['blue'], 9)}
  {arrow('th-u', 'M900,760 L900,420 M870,460 L900,410 L930,460', C['red'], 9)}
  {tag('th-gd', 'gas ↓', 60, 300)}{tag('th-cu', 'car ↑', 800, 300)}
  <div id="th-n" class="note">just like a <span class="hl">rocket</span></div>
""", f"""
pop("#th-c", 0.05); tl.set("#th-d", {{opacity:1}}, 0); draw("#th-d", {td:.2f}, 0.4); pop("#th-gd", {td:.2f});
tl.set("#th-u", {{opacity:1}}, 0); draw("#th-u", {tup:.2f}, 0.4); pop("#th-cu", {tup:.2f}); rise("#th-n", {tro:.2f});
""")

s = "cases"; toff = aw(s, "thrusters off"); tff = aw(s, "faster and faster"); ton = aw(s, "both on"); tsl = aw(s, "but slower")
scenes[s] = scene_file(s, OV, f"""
  {chip('cs-c', 'THREE CASES')}
  {tag('cs-1', 'OFF: faster ↓↓', 600, 280)}
  {tag('cs-2', 'BOTH ON: slower ↓', 560, 380)}
""", f"""
pop("#cs-c", {toff-0.2:.2f}); pop("#cs-1", {tff:.2f}); pop("#cs-2", {tsl:.2f});
""")

s = "tilt"; th_ = aw(s, "harder at one end"); tn = aw(s, "nose lifts"); trt = aw(s, "rotates")
scenes[s] = scene_file(s, OV, f"""
  {chip('tl-c', 'CASE 3 · UNEVEN PUSH')}
  {arrow('tl-r', 'M700,520 A170,170 0 0 0 1010,380 M970,360 L1012,378 L1000,420', C['red'], 8)}
  {tag('tl-t', 'nose up!', 760, 600)}
  <div id="tl-n" class="note">uneven push = <span class="hl">rotation</span></div>
""", f"""
pop("#tl-c", {th_:.2f}); tl.set("#tl-r", {{opacity:1}}, 0); draw("#tl-r", {tn:.2f}, 0.6); pop("#tl-t", {tn+0.2:.2f}); rise("#tl-n", {trt:.2f});
""")

s = "stop"; tsp = aw(s, "spinning car"); tlv = aw(s, "it's level"); tow = aw(s, "other way")
scenes[s] = scene_file(s, OV, f"""
  {chip('sp-c', 'STOP THE SPIN')}
  {tag('sp-t', 'keeps spinning...', 80, 300)}
  <div id="sp-n" class="note">push back = <span class="blue">brake</span></div>
""", f"""
pop("#sp-c", {tsp:.2f}); pop("#sp-t", {tsp+0.4:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}}); rise("#sp-n", {tow:.2f});
""")

s = "land"; ttd = aw(s, "touchdown"); tsf = aw(s, "slows the fall")
scenes[s] = scene_file(s, OV, f"""
  {chip('ld-c', 'SOFT LANDING')}
  {tag('ld-t', 'extra thrust ↑', 640, 300)}
  <div id="ld-n" class="note">slow down, then <span class="hl">touch</span></div>
""", f"""
pop("#ld-c", {ttd-0.3:.2f}); pop("#ld-t", {ttd:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#ld-n", {tsf:.2f});
""")

s = "budget"; tsm = aw(s, "so much air"); tpl = aw(s, "be planned")
bars = "".join(f'<div id="bg-b{i}" class="abs" style="left:{450+i*70}px;top:915px;width:52px;height:70px;background:{C["blue"]};border:4px solid {K};{SKETCH}"></div>' for i in range(8))
scenes[s] = scene_file(s, OV, f"""
  {chip('bg-c', 'AIR BUDGET')}
  {bars}
  {tag('bg-t', 'plan every puff', 600, 300)}
""", f"""
pop("#bg-c", 0.05); {"".join(f'pop("#bg-b{i}", 0.1+{i}*0.06);' for i in range(8))}
{"".join(f'tl.to("#bg-b{7-i}", {{opacity:0.12, duration:0.2}}, {tsm:.2f}+{i}*0.25);' for i in range(5))}
pop("#bg-t", {tpl:.2f});
""")

s = "outro"; t1 = aw(s, "suction to stick"); t2 = aw(s, "thrusters to flip"); t3 = aw(s, "air budget"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'THE RECIPE')}
  {tag('ou-1', 'stick', 450, 905)}{tag('ou-2', 'flip', 640, 905)}{tag('ou-3', 'land', 810, 905)}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">ramp → flip → land</div></div>
""", f"""
pop("#ou-c", {t1-0.2:.2f}); pop("#ou-1", {t1:.2f}); pop("#ou-2", {t2:.2f}); pop("#ou-3", {t3:.2f});
tl.to("#ou-1, #ou-2, #ou-3", {{opacity:0, duration:0.25}}, {tsc-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "how does"), g("hook", "on its wheels"))
wave(g("intro", "I'm Max"))
point(g("intro", "break this stunt"), 1.2)
wow(g("real", "Tesla showed"), 1.0)
point(g("problem", "gravity wins"), 1.2)
point(g("fans", "powerful fans"), 1.2)
point(g("skirt", "seals the gap"), 1.2)
wow(g("suction", "pushes it hard"), 1.0)
point(g("leave", "air rushes in"), 1.2)
point(g("tanks", "cold gas thrusters"), 1.2)
wow(g("nozzle", "blasts out"), 1.0)
point(g("thrust", "pushed up"), 1.2)
point(g("cases", "thrusters off"), 1.2)
wow(g("tilt", "nose lifts"), 1.0)
point(g("stop", "other way"), 1.2)
point(g("land", "touchdown"), 1.2)
point(g("budget", "so much air"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "upside down"), 0.45), ("whoosh-short.mp3", A("hook", "flip in midair"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("ping.mp3", A("real", "Tesla showed"), 0.35), ("impact-bass-1.mp3", A("problem", "gravity wins"), 0.35), ("click.mp3", A("fans", "suck the air"), 0.35),
        ("pop.mp3", A("suction", "is low"), 0.45), ("pop.mp3", A("tanks", "cold gas thrusters"), 0.45), ("whoosh-short.mp3", A("nozzle", "blasts out"), 0.4),
        ("riser.mp3", A("tilt", "harder at one end"), 0.3), ("impact-bass-2.mp3", A("land", "touchdown"), 0.35), ("click-soft.mp3", A("budget", "so much air"), 0.5),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
