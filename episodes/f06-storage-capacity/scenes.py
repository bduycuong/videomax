# Storage capacity: doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
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

s = "hook"; t1 = aw(s, "two terabytes"); t2 = aw(s, "so tiny")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:76px; }", f"""
  <div id="hk-t" class="h1">Fingernail = <span class="hl">2 TB</span>?!</div>
  <div id="hk-a" class="sticky" style="left:60px;top:290px;background:{C['hi']};transform:rotate(-6deg)">2 TB!</div>
  {tag('hk-c', 'how so tiny?', 620, 800)}
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-c", {t2:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tb = aw(s, "open up")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-f', 'open it up →', 560, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-f", {tb:.2f});
""")

s = "bits"; to_ = aw(s, "ones and zeros"); tk = aw(s, "keep them safe")
digs = "".join(f'<div id="bt-d{i}" class="abs" style="left:{90+i*120}px;top:300px;font-family:\'Gochi Hand\',cursive;font-size:96px;color:{C["blue"] if i%2 else C["red"]};background:#FFFFFF;border:4px solid {K};{SKETCH} width:90px;text-align:center;opacity:0">{"10110100"[i]}</div>' for i in range(8))
scenes[s] = scene_file(s, OV, f"""
  {chip('bt-c', 'IT IS ALL 1s AND 0s')}
  {digs}
  <div id="bt-n" class="note">job: keep them <span class="hl">safe</span></div>
""", f"""
pop("#bt-c", {to_-0.3:.2f}); {"".join(f'pop("#bt-d{i}", {to_:.2f}+{i}*0.08);' for i in range(8))} rise("#bt-n", {tk:.2f});
""")

s = "disk"; tp = aw(s, "spinning platters"); th = aw(s, "tiny head"); tn = aw(s, "north or south")
scenes[s] = scene_file(s, OV, f"""
  {chip('dk-c', 'HARD DRIVE')}
  {tag('dk-p', 'spinning platter', 80, 300)}
  {tag('dk-h', 'head', 760, 300)}
  <div id="dk-n" class="note">bit = magnet <span class="red">N</span> or <span class="blue">S</span></div>
""", f"""
pop("#dk-c", {tp-0.3:.2f}); pop("#dk-p", {tp:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); pop("#dk-h", {th:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}}); rise("#dk-n", {tn:.2f});
""")

s = "shrink"; ta = aw(s, "add platters"); ts = aw(s, "shrink the magnets"); tw = aw(s, "wiping your data")
scenes[s] = scene_file(s, OV, f"""
  {chip('sh-c', 'MORE ROOM?')}
  <div id="sh-a" class="sticky" style="left:60px;top:290px;background:#C9E8C2;transform:rotate(-4deg)">more<br>platters</div>
  <div id="sh-b" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">smaller<br>magnets</div>
  <div id="sh-n" class="note">too small = <span class="red">data flips!</span></div>
""", f"""
pop("#sh-c", 0.05); pop("#sh-a", {ta:.2f}); pop("#sh-b", {ts:.2f}); rise("#sh-n", {tw:.2f});
""")

s = "shingle"; tr = aw(s, "roof shingles"); tm = aw(s, "more fits"); tsl = aw(s, "gets slow")
scenes[s] = scene_file(s, OV, f"""
  {chip('sg-c', 'TRICK · SHINGLED TRACKS')}
  <div id="sg-n" class="note">more room, <span class="red">slow rewrites</span></div>
  {tag('sg-t', 'overlap!', 760, 800)}
""", f"""
pop("#sg-c", {tr-0.4:.2f}); pop("#sg-t", {tr:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#sg-n", {tsl:.2f});
""")

s = "flash"; tf = aw(s, "flash memory"); tc = aw(s, "electric charge"); to_ = aw(s, "power is off")
scenes[s] = scene_file(s, OV, f"""
  {chip('fl-c', 'FLASH MEMORY')}
  {tag('fl-1', 'SSD', 80, 300)}{tag('fl-2', 'USB stick', 80, 380)}{tag('fl-3', 'SD card', 80, 460)}
  <div id="fl-n" class="note">charge stays, <span class="hl">power off</span></div>
""", f"""
pop("#fl-c", {tf:.2f}); pop("#fl-1", 0.2); pop("#fl-2", 0.6); pop("#fl-3", 1.0);
tl.to("#fl-1, #fl-2, #fl-3", {{opacity:0, duration:0.25}}, {tc-0.3:.2f}); rise("#fl-n", {to_:.2f});
""")

s = "levels"; to_ = aw(s, "one bit"); tf = aw(s, "four bits"); ts = aw(s, "sixteen different levels")
bars = "".join(f'<div id="lv-b{i}" class="abs" style="left:{450+i*36}px;top:{985-(i+1)*5}px;width:28px;height:{(i+1)*5}px;background:{C["blue"]};border:2px solid {K};opacity:0"></div>' for i in range(16))
scenes[s] = scene_file(s, OV, f"""
  {chip('lv-c', '1 BIT → 4 BITS PER CELL')}
  {tag('lv-a', '1 bit = 2 levels', 80, 300)}
  {tag('lv-b', '4 bits = 16 levels', 560, 300)}
  {bars}
""", f"""
pop("#lv-c", {to_-0.3:.2f}); pop("#lv-a", {to_:.2f}); pop("#lv-b", {tf:.2f}); {"".join(f'pop("#lv-b{i}", {ts:.2f}+{i}*0.06);' for i in range(16))}
""")

s = "flat"; ts = aw(s, "side by side"); tt = aw(s, "tiny houses"); td = aw(s, "disturb each other")
scenes[s] = scene_file(s, OV, f"""
  {chip('ft-c', 'FLAT CHIP = ONE FLOOR')}
  {tag('ft-t', 'a town of tiny houses', 560, 300)}
  <div id="ft-n" class="note">too close = <span class="red">interference</span></div>
""", f"""
pop("#ft-c", {ts:.2f}); pop("#ft-t", {tt:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#ft-n", {td:.2f});
""")

s = "tower"; tb = aw(s, "built up"); tl3 = aw(s, "three hundred layers"); tp = aw(s, "one package")
stack = "".join(f'<div id="tw-s{i}" class="abs" style="left:900px;top:{860-i*48}px;width:130px;height:38px;background:{C["hi"]};border:4px solid {K};{SKETCH} opacity:0"></div>' for i in range(10))
scenes[s] = scene_file(s, OV, f"""
  {chip('tw-c', 'BUILD UP: 3D')}
  {stack}
  {tag('tw-t', '300+ layers', 60, 300)}
  <div id="tw-n" class="note">many chips, <span class="hl">one package</span></div>
""", f"""
pop("#tw-c", {tb:.2f}); {"".join(f'pop("#tw-s{i}", {tb:.2f}+{i}*0.12);' for i in range(10))}
pop("#tw-t", {tl3:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#tw-n", {tp:.2f});
""")

s = "speed"; tq = aw(s, "faster than"); tb = aw(s, "powerful brain"); th = aw(s, "giant highway"); tn = aw(s, "narrow road")
scenes[s] = scene_file(s, OV, f"""
  {chip('sp-c', 'WHY IS SSD FASTER?')}
  <div id="sp-a" class="sticky" style="left:60px;top:290px;background:#C9E8C2;transform:rotate(-4deg)">SSD:<br>highway</div>
  <div id="sp-b" class="sticky" style="left:780px;top:290px;background:{C['hi']};transform:rotate(4deg)">stick:<br>narrow road</div>
  <div id="sp-n" class="note">the <span class="hl">controller</span> decides</div>
""", f"""
pop("#sp-c", {tq:.2f}); rise("#sp-n", {tb:.2f}); pop("#sp-a", {th:.2f}); pop("#sp-b", {tn:.2f});
""")

s = "outro"; t1 = aw(s, "tiny magnets"); t2 = aw(s, "trapped charges"); t3 = aw(s, "skyscrapers of cells"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'THE SECRET')}
  {tag('ou-1', 'magnets', 440, 905)}{tag('ou-2', 'charges', 640, 905)}{tag('ou-3', 'layers', 850, 905)}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">flat town → skyscraper</div></div>
""", f"""
pop("#ou-c", {t1-0.2:.2f}); pop("#ou-1", {t1:.2f}); pop("#ou-2", {t2:.2f}); pop("#ou-3", {t3:.2f});
tl.to("#ou-c, #ou-1, #ou-2, #ou-3", {{opacity:0, duration:0.25}}, {tsc-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "how do"), g("hook", "so tiny"))
wave(g("intro", "I'm Max"))
point(g("intro", "open up"), 1.2)
point(g("bits", "ones and zeros"), 1.2)
point(g("disk", "tiny head"), 1.2)
wow(g("shrink", "wiping your data"), 1.0)
point(g("shingle", "roof shingles"), 1.2)
point(g("flash", "electric charge"), 1.2)
wow(g("levels", "sixteen different levels"), 1.0)
point(g("flat", "tiny houses"), 1.2)
wow(g("tower", "three hundred layers"), 1.0)
point(g("speed", "giant highway"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "two terabytes"), 0.45), ("ping.mp3", A("hook", "so tiny"), 0.35), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click.mp3", A("bits", "ones and zeros"), 0.4), ("pop.mp3", A("disk", "tiny head"), 0.4), ("impact-bass-1.mp3", A("shrink", "wiping your data"), 0.3),
        ("pop.mp3", A("shingle", "roof shingles"), 0.4), ("ping.mp3", A("flash", "electric charge"), 0.35), ("riser.mp3", A("levels", "four bits"), 0.3),
        ("pop.mp3", A("flat", "tiny houses"), 0.4), ("impact-bass-2.mp3", A("tower", "three hundred layers"), 0.35), ("whoosh-short.mp3", A("speed", "giant highway"), 0.4),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
