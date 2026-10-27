# Brazil's borders: doodle overlays on the map footage. Footage panel sits at x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; }}
.sticky {{ position:absolute; width:230px; padding:14px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} }}
"""
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def arrow(i, d, color=None): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color or C["red"]}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/></svg>'

s = "hook"; t1 = aw(s, "Portuguese"); t2 = aw(s, "speak Spanish")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:74px; }", f"""
  <div id="hk-t" class="h1">Why <span class="hl">Portuguese</span>?</div>
  <div id="hk-a" class="sticky" style="left:60px;top:300px;background:#C9E8C2;transform:rotate(-6deg)">Brazil: Português</div>
  <div id="hk-b" class="sticky" style="left:780px;top:320px;background:{C['hi']};transform:rotate(5deg)">neighbors: Español</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:5}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tl_ = aw(s, "a line drawn")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-l', 'one line on the ocean?!', 430, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-l", {tl_:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
""")

s = "race"; tr = aw(s, "racing"); ta = aw(s, "around Africa"); tc = aw(s, "Columbus west")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="ra-c"><span class="chip">THE RACE TO <span class="red">ASIA</span></span></div>
  <div id="ra-n" class="note"><span id="ra-p">Portugal → south</span> · <span id="ra-s" class="blue">Spain → west</span></div>
""", f"""
pop("#ra-c", {tr:.2f}); tl.fromTo("#ra-n", {{opacity:0}}, {{opacity:1, duration:0.01}}, {ta-0.05:.2f});
tl.fromTo("#ra-p", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.3, ease:"back.out"}}, {ta:.2f});
tl.fromTo("#ra-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.3, ease:"back.out"}}, {tc:.2f});
""")

s = "land"; tl2 = aw(s, "land"); tas = aw(s, "wasn't Asia"); tam = aw(s, "the Americas")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="la-c"><span class="chip">LAND HO!</span></div>
  <div id="la-n" class="note"><span id="la-a">Asia</span> <span id="la-b" class="hl">the Americas!</span></div>
  {arrow('la-x', 'M560,950 L700,950')}
""", f"""
pop("#la-c", {tl2:.2f}); rise("#la-n", {tas-0.1:.2f}); tl.set("#la-x", {{opacity:1}}, 0); draw("#la-x", {tas+0.3:.2f}, 0.3);
tl.fromTo("#la-b", {{opacity:0}}, {{opacity:1, duration:0.2}}, {tam:.2f});
""")

s = "pope"; tp = aw(s, "the Pope"); ty = aw(s, "fourteen ninety three"); tpp = aw(s, "pole to pole"); tlg = aw(s, "one hundred leagues")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="po-c"><span class="chip">ASK THE <span class="red">POPE</span></span></div>
  {tag('po-y', '1493', 820, 260, 'font-size:56px')}
  <div id="po-n" class="note">a line, pole to pole: <span class="hl">100 leagues</span></div>
""", f"""
pop("#po-c", {tp:.2f}); pop("#po-y", {ty:.2f}, {{from:{{rotation:12}}, to:{{rotation:-3}}}}); rise("#po-n", {tpp:.2f});
""")

s = "split"; tw2 = aw(s, "to the west"); te = aw(s, "to the east")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="sp-c"><span class="chip">SPLIT THE WORLD</span></div>
  {tag('sp-w', '← Spain', 60, 720, 'background:#FFD7A8')}
  {tag('sp-e', 'Portugal →', 700, 720, 'background:#C9E8C2')}
""", f"""
pop("#sp-c", 0.05); pop("#sp-w", {tw2:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); pop("#sp-e", {te:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
""")

s = "treaty"; tmr = aw(s, "more room"); tt = aw(s, "Treaty of Tordesillas"); t370 = aw(s, "three hundred seventy leagues")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="tr-c"><span class="chip">MOVE IT <span class="red">WEST!</span></span></div>
  <div id="tr-n" class="note"><span class="hatch-r" id="tr-o">100</span> → <span class="hl" id="tr-v">370 leagues</span></div>
  {arrow('tr-x', 'M520,958 L600,940')}
  {tag('tr-t', 'Treaty of Tordesillas · 1494', 330, 260, 'font-size:40px')}
""", f"""
pop("#tr-c", {tmr:.2f}); pop("#tr-t", {tt:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#tr-n", {t370-0.4:.2f}); tl.set("#tr-x", {{opacity:1}}, 0); draw("#tr-x", {t370:.2f}, 0.25);
tl.fromTo("#tr-v", {{scale:0.6}}, {{scale:1, duration:0.35, ease:"back.out"}}, {t370:.2f});
""")

s = "luck"; t15 = aw(s, "fifteen hundred"); tb = aw(s, "eastern bulge"); ts = aw(s, "Portugal's side")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="lu-c"><span class="chip">WHAT <span class="red">LUCK!</span></span></div>
  {tag('lu-y', '1500', 820, 260, 'font-size:56px')}
  <div id="lu-n" class="note">the bulge = <span class="hl">Portugal's side</span></div>
""", f"""
pop("#lu-c", {t15-0.3:.2f}); pop("#lu-y", {t15:.2f}, {{from:{{rotation:12}}, to:{{rotation:-3}}}}); rise("#lu-n", {tb:.2f});
tl.fromTo("#lu-n .hl", {{opacity:0}}, {{opacity:1, duration:0.2}}, {ts:.2f});
""")

s = "grow"; tbe = aw(s, "far beyond"); tam2 = aw(s, "the Amazon"); ttr = aw(s, "later treaties")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="gr-c"><span class="chip">GROWING WEST</span></div>
  {tag('gr-a', 'deep into the Amazon', 560, 300)}
  <div id="gr-n" class="note">later treaties → <span class="hl">today's borders</span></div>
""", f"""
pop("#gr-c", {tbe:.2f}); pop("#gr-a", {tam2:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#gr-n", {ttr:.2f});
""")

s = "outro"; tl3 = aw(s, "one line"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="ou-c"><span class="chip">1 LINE → 1 LANGUAGE</span></div>
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">one line → Portuguese</div></div>
""", f"""
pop("#ou-c", {tl3:.2f}); pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "why does"), g("hook", "speak Spanish"))
wave(g("intro", "I'm Max"))
point(g("intro", "a line drawn"), 1.2)
point(g("race", "racing"), 1.2)
wow(g("land", "wasn't Asia"), 1.0)
point(g("pope", "pole to pole"), 1.2)
point(g("split", "to the west"), 1.0)
point(g("treaty", "three hundred seventy"), 1.2)
wow(g("luck", "eastern bulge"), 1.2)
point(g("grow", "the Amazon"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "Portuguese"), 0.45), ("pop.mp3", A("hook", "speak Spanish"), 0.45), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click-soft.mp3", A("race", "around Africa"), 0.5), ("click-soft.mp3", A("race", "Columbus west"), 0.5), ("ping.mp3", A("land", "the Americas"), 0.35),
        ("pop.mp3", A("pope", "fourteen ninety three"), 0.45), ("pop.mp3", A("split", "to the east"), 0.45), ("impact-bass-1.mp3", A("treaty", "three hundred seventy"), 0.35),
        ("pop.mp3", A("luck", "fifteen hundred"), 0.45), ("pop.mp3", A("grow", "the Amazon"), 0.45), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
