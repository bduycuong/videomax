# Dingo Fence: doodle overlays on the map footage. Footage panel sits at x 20–1060, y 230–898.
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

s = "hook"; t1 = aw(s, "longest fence"); t2 = aw(s, "keep out")
scenes[s] = scene_file(s, OV + "#hk-t { top:96px; font-size:74px; }", f"""
  <div id="hk-t" class="h1">The <span class="hl">longest</span> fence?</div>
  <div id="hk-a" class="sticky" style="left:60px;top:300px;background:{C['hi']};transform:rotate(-6deg)">world record</div>
  <div id="hk-b" class="sticky" style="left:780px;top:320px;background:#C9E8C2;transform:rotate(5deg)">keeping out... who?</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}}); pop("#hk-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:5}}}});
""")

s = "intro"; tw = aw(s, "Max Wise"); tz = aw(s, "zoom in")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  {tag('in-z', 'zoom in → Australia', 430, 905, 'font-size:50px')}
""", f"""
pop("#in-c", {tw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); pop("#in-z", {tz:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
""")

s = "length"; tf = aw(s, "Dingo Fence"); tk = aw(s, "five thousand six hundred"); t3 = aw(s, "three Australian states")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="le-c"><span class="chip">THE <span class="red">DINGO FENCE</span></span></div>
  <div id="le-n" class="note">about <span class="hl" id="le-k">5,600 km</span> · 3 states</div>
""", f"""
pop("#le-c", {tf:.2f}); rise("#le-n", {tk:.2f}); tl.fromTo("#le-k", {{scale:0.6}}, {{scale:1, duration:0.35, ease:"back.out"}}, {tk:.2f});
""")

s = "compare"; tl_ = aw(s, "London to New York"); tm = aw(s, "wire mesh"); t6 = aw(s, "six feet tall")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="co-c"><span class="chip">≈ LONDON → NEW YORK</span></div>
  <div id="co-n" class="note">wire mesh, about <span class="hl">6 ft</span> tall</div>
""", f"""
pop("#co-c", {tl_:.2f}); rise("#co-n", {tm:.2f}); tl.fromTo("#co-n .hl", {{scale:0.6}}, {{scale:1, duration:0.3, ease:"back.out"}}, {t6:.2f});
""")

s = "dingo"; tg = aw(s, "this guy"); twd = aw(s, "wild dog"); tmd = aw(s, "medium pet dog")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="dg-c"><span class="chip">MEET THE <span class="red">DINGO</span></span></div>
  {tag('dg-w', 'wild dog', 60, 270)}
  <div id="dg-n" class="note">size: a medium pet dog</div>
""", f"""
pop("#dg-c", {tg:.2f}); pop("#dg-w", {twd:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); rise("#dg-n", {tmd:.2f});
""")

s = "speed"; ts = aw(s, "sixty kilometers"); th = aw(s, "kangaroos")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="sd-c"><span class="chip">ZOOM! <span class="red">~60 km/h</span></span></div>
  <div id="sd-n" class="note">menu: kangaroos + small animals</div>
""", f"""
pop("#sd-c", {ts:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}}); rise("#sd-n", {th:.2f});
""")

s = "sheep"; te = aw(s, "Europeans arrived"); tsh = aw(s, "brought sheep"); tmn = aw(s, "brand new menu")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="sh-c"><span class="chip">LATE 1700s</span></div>
  {tag('sh-s', '+ sheep!', 760, 600, 'font-size:52px')}
  <div id="sh-n" class="note">a <span class="hl">brand new menu</span></div>
""", f"""
pop("#sh-c", {te:.2f}); pop("#sh-s", {tsh:.2f}, {{from:{{rotation:15}}, to:{{rotation:-3}}}}); rise("#sh-n", {tmn:.2f});
""")

s = "farmers"; ttr = aw(s, "traps and guns"); tl2 = aw(s, "losing sheep"); t80 = aw(s, "eighteen eighties")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="fa-c"><span class="chip">FARMERS VS DINGOES</span></div>
  <div id="fa-n" class="note"><span class="hatch-r" id="fa-t">traps · guns</span> → <span class="hl" id="fa-f">fences, 1880s</span></div>
""", f"""
pop("#fa-c", {ttr-0.3:.2f}); tl.fromTo("#fa-n", {{opacity:0}}, {{opacity:1, duration:0.01}}, {ttr-0.05:.2f});
tl.fromTo("#fa-t", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.3, ease:"back.out"}}, {ttr:.2f});
tl.fromTo("#fa-f", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.3, ease:"back.out"}}, {t80:.2f});
""")

s = "connect"; tj = aw(s, "joined"); tgb = aw(s, "giant barrier")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="cn-c"><span class="chip">JOIN THE DOTS</span></div>
  <div id="cn-n" class="note">many fences → <span class="hl">one barrier</span></div>
""", f"""
pop("#cn-c", {tj-0.3:.2f}); rise("#cn-n", {tgb-0.3:.2f});
""")

s = "outro"; ts1 = aw(s, "sheep country"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  <div class="top" id="ou-c"><span class="chip">sheep | dingoes</span></div>
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">one very long fence</div></div>
""", f"""
pop("#ou-c", {ts1:.2f}); pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "what is"), g("hook", "keep out"))
wave(g("intro", "I'm Max"))
point(g("intro", "zoom in"), 1.2)
wow(g("length", "five thousand six hundred"), 1.2)
point(g("compare", "London to New York"), 1.2)
point(g("dingo", "this guy"), 1.2)
wow(g("speed", "sixty kilometers"), 1.0)
point(g("sheep", "brought sheep"), 1.2)
point(g("farmers", "eighteen eighties"), 1.2)
wow(g("connect", "giant barrier"), 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "longest fence"), 0.45), ("pop.mp3", A("hook", "keep out"), 0.45), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("impact-bass-1.mp3", A("length", "five thousand six hundred"), 0.35), ("click-soft.mp3", A("compare", "London to New York"), 0.5),
        ("pop.mp3", A("dingo", "wild dog"), 0.45), ("whoosh-short.mp3", A("speed", "sixty kilometers"), 0.35), ("pop.mp3", A("sheep", "brought sheep"), 0.45),
        ("click.mp3", A("farmers", "eighteen eighties"), 0.35), ("ping.mp3", A("connect", "giant barrier"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
