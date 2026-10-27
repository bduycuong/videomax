# Tubeless tire: doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
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

s = "hook"; t1 = aw(s, "a nail"); t2 = aw(s, "go flat")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:76px; }", f"""
  <div id="hk-t" class="h1">Nail in the <span class="hl">tire</span>?!</div>
  <div id="hk-a" class="sticky" style="left:60px;top:290px;background:{C['hi']};transform:rotate(-6deg)">NAIL!</div>
  {tag('hk-c', 'still not flat?', 600, 800)}
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-c", {t2:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tb = aw(s, "inside the tire")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-f', 'look inside →', 560, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-f", {tb:.2f});
""")

s = "tube"; tp = aw(s, "two parts"); to_ = aw(s, "outer tire"); tb = aw(s, "rubber balloon")
scenes[s] = scene_file(s, OV, f"""
  {chip('tb-c', 'OLD TIRES: 2 PARTS')}
  {tag('tb-o', 'outer tire', 640, 300)}
  {tag('tb-i', 'inner tube', 80, 300)}
  <div id="tb-n" class="note">a <span class="hl">rubber balloon</span> inside</div>
""", f"""
pop("#tb-c", {tp:.2f}); pop("#tb-o", {to_:.2f}, {{from:{{rotation:8}}, to:{{rotation:-2}}}}); pop("#tb-i", {tb-0.6:.2f}, {{from:{{rotation:-8}}, to:{{rotation:2}}}}); rise("#tb-n", {tb:.2f});
""")

s = "pop"; th = aw(s, "poke a hole"); tf = aw(s, "out fast"); tc = aw(s, "collapse quickly")
scenes[s] = scene_file(s, OV, f"""
  {chip('pp-c', 'TUBE + HOLE = <span class="red">TROUBLE</span>')}
  <div id="pp-p" class="abs" style="left:640px;top:300px;font-family:'Gochi Hand',cursive;font-size:120px;color:{C['red']};transform:rotate(-8deg);text-shadow:4px 4px 0 #FFFFFF">PSSSH!</div>
  <div id="pp-n" class="note">air out <span class="red">fast</span></div>
""", f"""
pop("#pp-c", {th:.2f}); pop("#pp-p", {tf:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#pp-n", {tc:.2f});
""")

s = "tubeless"; ta = aw(s, "threw the tube away"); th = aw(s, "holds the air"); tt = aw(s, "tubeless tire")
scenes[s] = scene_file(s, OV, f"""
  {chip('tl-c', 'NO TUBE')}
  <div id="tl-x" class="abs" style="left:80px;top:290px;font-family:'Gochi Hand',cursive;font-size:64px;color:{K};background:#FFFFFF;border:4px solid {K};{SKETCH} padding:2px 22px">inner tube</div>
  <svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="tl-s" d="M70,345 L420,320" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round" style="opacity:0"/></svg>
  <div id="tl-n" class="note">the tire <span class="hl">is</span> the seal</div>
""", f"""
pop("#tl-c", {ta-0.3:.2f}); pop("#tl-x", {ta-0.3:.2f}); tl.set("#tl-s", {{opacity:1}}, 0); draw("#tl-s", {ta+0.3:.2f}, 0.4); rise("#tl-n", {th:.2f});
tl.to("#tl-c", {{scale:1.15, duration:0.2, yoyo:true, repeat:1}}, {tt:.2f});
""")

s = "nail"; ts = aw(s, "squeezes tight"); tg = aw(s, "tiny gap"); tsl = aw(s, "leaks slowly")
scenes[s] = scene_file(s, OV, f"""
  {chip('nl-c', 'RUBBER <span class="blue">HUGS</span> THE NAIL')}
  {tag('nl-t', 'tiny gap', 640, 300)}
  <div id="nl-n" class="note">leak = <span class="hl">slow</span></div>
""", f"""
pop("#nl-c", {ts:.2f}); pop("#nl-t", {tg:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#nl-n", {tsl:.2f});
""")

s = "bead"; tb = aw(s, "the bead"); tw = aw(s, "steel wire"); tp = aw(s, "pushes it outward"); tt = aw(s, "tighter and tighter")
arrs = "".join(arrow(f'bd-a{i}', f'M{560+i*160},700 L{560+i*160},560 M{535+i*160},595 L{560+i*160},555 L{585+i*160},595', C['blue'], 7) for i in range(3))
scenes[s] = scene_file(s, OV, f"""
  {chip('bd-c', 'SEAL 1 · THE BEAD')}
  {tag('bd-t', 'steel wire ring', 80, 300)}
  {arrs}
  <div id="bd-n" class="note">tighter and <span class="hl">tighter</span></div>
""", f"""
pop("#bd-c", {tb:.2f}); pop("#bd-t", {tw:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
{"".join(f'tl.set("#bd-a{i}", {{opacity:1}}, 0); draw("#bd-a{i}", {tp:.2f}+{i}*0.15, 0.4);' for i in range(3))}
rise("#bd-n", {tt:.2f});
""")

s = "ribs"; tk = aw(s, "the skeleton"); tu = aw(s, "an umbrella"); tc = aw(s, "in corners")
scenes[s] = scene_file(s, OV, f"""
  {chip('rb-c', 'THE SKELETON')}
  <div id="rb-u" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">like<br>umbrella ribs</div>
  <div id="rb-n" class="note">steady in <span class="hl">corners</span></div>
""", f"""
pop("#rb-c", {tk:.2f}); pop("#rb-u", {tu:.2f}); rise("#rb-n", {tc:.2f});
""")

s = "tread"; tt = aw(s, "the tread"); tr = aw(s, "touches the road"); tb = aw(s, "right balance")
scenes[s] = scene_file(s, OV, f"""
  {chip('tr-c', 'THE TREAD')}
  {tag('tr-t', 'touches the road', 600, 300)}
  {tag('tr-1', 'hard', 450, 905)}{tag('tr-2', 'bouncy', 610, 905)}{tag('tr-3', 'pattern', 820, 905)}
""", f"""
pop("#tr-c", {tt:.2f}); pop("#tr-t", {tr:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}});
pop("#tr-1", {tb+0.4:.2f}); pop("#tr-2", {tb+0.8:.2f}); pop("#tr-3", {tb+1.2:.2f});
""")

s = "rubber"; th = aw(s, "hardest part"); ts = aw(s, "soft enough"); tg = aw(s, "tough enough")
scenes[s] = scene_file(s, OV, f"""
  {chip('ru-c', 'THE TRICKY PART')}
  <div id="ru-s" class="sticky" style="left:60px;top:290px;background:#C9E8C2;transform:rotate(-4deg)">soft<br>to grip</div>
  <div id="ru-t" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">tough<br>to last</div>
  <div id="ru-n" class="note">soft <span class="hl">and</span> tough</div>
""", f"""
pop("#ru-c", {th:.2f}); pop("#ru-s", {ts:.2f}); pop("#ru-t", {tg:.2f}); rise("#ru-n", {tg+0.8:.2f});
""")

s = "outro"; t1 = aw(s, "slow leak"); t2 = aw(s, "pull it out"); t3 = aw(s, "tire shop"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'NAIL? SLOW LEAK')}
  {tag('ou-1', 'leave it in', 450, 905)}{tag('ou-2', 'tire shop →', 730, 905)}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">bead · skeleton · tread</div></div>
""", f"""
pop("#ou-c", {t1-0.2:.2f}); pop("#ou-1", {t2:.2f}); pop("#ou-2", {t3:.2f});
tl.to("#ou-c, #ou-1, #ou-2", {{opacity:0, duration:0.25}}, {tsc-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "so why"), g("hook", "in seconds"))
wave(g("intro", "I'm Max"))
point(g("intro", "inside the tire"), 1.2)
point(g("tube", "rubber balloon"), 1.2)
wow(g("pop", "out fast"), 1.0)
point(g("tubeless", "holds the air"), 1.2)
point(g("nail", "tiny gap"), 1.2)
point(g("bead", "steel wire"), 1.2)
point(g("ribs", "an umbrella"), 1.2)
point(g("tread", "touches the road"), 1.2)
wow(g("rubber", "tough enough"), 1.0)
point(g("outro", "tire shop"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "a nail"), 0.45), ("ping.mp3", A("hook", "go flat"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("pop.mp3", A("tube", "rubber balloon"), 0.4), ("whoosh-short.mp3", A("pop", "out fast"), 0.45), ("click.mp3", A("tubeless", "threw the tube away"), 0.4),
        ("pop.mp3", A("nail", "tiny gap"), 0.4), ("click-soft.mp3", A("bead", "tighter and tighter"), 0.5), ("pop.mp3", A("ribs", "an umbrella"), 0.4),
        ("ping.mp3", A("tread", "right balance"), 0.35), ("impact-bass-1.mp3", A("rubber", "tough enough"), 0.3), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
