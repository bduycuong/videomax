# Why do whole pods of pilot whales strand together? Doodle overlays on the source animation. Footage panel sits at x 20–1060, y 230–898.
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

s = "hook"; tb = aw(s, "onto a beach"); tf = aw(s, "rest of its group"); tw = aw(s, "whole pod")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">Why does the <span class="hl">whole pod</span> follow?</div>
  {tag('hk-a', '1 whale…', 60, 280)}
  {tag('hk-b', '…then the rest', 640, 280)}
  <div id="hk-n" class="note">one after <span class="hl">another</span></div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {tb:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#hk-b", {tf:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#hk-n", {tf+0.9:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tp = aw(s, "pilot whale")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">meet the <span class="hl">pilot whale</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tp:.2f});
""")

s = "dolphin"; tg = aw(s, "giant dolphins"); t6 = aw(s, "six meters")
scenes[s] = scene_file(s, OV, f"""
  {chip('dl-c', 'SURPRISE!')}
  <div id="dl-x" class="gag" style="left:60px;top:270px;transform:rotate(-6deg)"><s>whale</s></div>
  {tag('dl-t', 'giant dolphin', 560, 285)}
  <div id="dl-n" class="note">male ≈ <span class="hl">6 m</span> long</div>
""", f"""
pop("#dl-c", 0.05); pop("#dl-x", {tg-0.5:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-6}}}});
pop("#dl-t", {tg:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#dl-n", {t6:.2f});
""")

s = "squid"; ts = aw(s, "is squid"); td = aw(s, "dive deep")
scenes[s] = scene_file(s, OV, f"""
  {chip('sq-c', 'FAVORITE FOOD')}
  {tag('sq-t', 'squid!', 760, 300)}
  <div id="sq-n" class="note">hunting in the <span class="hl">dark</span></div>
""", f"""
pop("#sq-c", 0.05); pop("#sq-t", {ts:.2f}, {{from:{{rotation:14}}, to:{{rotation:4}}}}); rise("#sq-n", {td:.2f});
""")

s = "brain"; th = aw(s, "round head"); t37 = aw(s, "thirty seven billion"); t2 = aw(s, "roughly double")
scenes[s] = scene_file(s, OV, f"""
  {chip('br-c', 'INSIDE THE HEAD')}
  {tag('br-t', '≈ 37 billion nerve cells', 470, 790)}
  <div id="br-n" class="note">about <span class="hl">2×</span> a human's</div>
""", f"""
pop("#br-c", {th-0.4:.2f}); pop("#br-t", {t37:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#br-n", {t2:.2f});
""")

s = "family"; tsp = aw(s, "real superpower"); t10 = aw(s, "ten whales"); t200 = aw(s, "two hundred"); tmo = aw(s, "mother's group")
scenes[s] = scene_file(s, OV, f"""
  {chip('fm-c', 'SUPERPOWER: FAMILY')}
  {tag('fm-a', '10', 60, 290)}
  {tag('fm-b', '200+', 220, 290)}
  <div id="fm-n" class="note">kids stay with <span class="hl">mom</span></div>
""", f"""
pop("#fm-c", {tsp:.2f}); pop("#fm-a", {t10:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
pop("#fm-b", {t200:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#fm-n", {tmo:.2f});
""")

s = "milk"; t3 = aw(s, "three years"); tl_ = aw(s, "longest childhoods")
scenes[s] = scene_file(s, OV, f"""
  {chip('mk-c', 'BABY PILOT WHALES')}
  {tag('mk-t', 'milk for 3+ years', 520, 790)}
  <div id="mk-n" class="note">a <span class="hl">long</span> childhood</div>
""", f"""
pop("#mk-c", 0.05); pop("#mk-t", {t3:.2f}, {{from:{{rotation:10}}, to:{{rotation:-3}}}}); rise("#mk-n", {tl_:.2f});
""")

s = "strand"; tst = aw(s, "gets stuck"); tgr = aw(s, "strand in groups")
scenes[s] = scene_file(s, OV, f"""
  {chip('st-c', 'MASS STRANDING')}
  <div id="st-x" class="gag" style="left:640px;top:270px;transform:rotate(-8deg)">STUCK!</div>
  <div id="st-n" class="note">one of the <span class="hl">most often</span></div>
""", f"""
pop("#st-c", 0.05); pop("#st-x", {tst:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#st-n", {tgr:.2f});
""")

s = "twist"; ttw = aw(s, "the twist"); tge = aw(s, "the genes"); tse = aw(s, "several families"); tbr = aw(s, "broken family")
scenes[s] = scene_file(s, OV, f"""
  {chip('tw-c', 'THE TWIST')}
  {tag('tw-g', 'DNA test', 60, 290)}
  {tag('tw-x', '<s style="color:'+C['red']+'">one family</s>', 640, 290)}
  {tag('tw-t', 'several families mixed', 420, 790)}
  <div id="tw-n" class="note">a <span class="hl">broken</span> family?</div>
""", f"""
pop("#tw-c", {ttw:.2f}); pop("#tw-g", {tge:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#tw-x", {tse-1.2:.2f}, {{from:{{scale:0.3, rotation:-20}}, to:{{rotation:-4}}}});
pop("#tw-t", {tse:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#tw-n", {tbr:.2f});
""")

s = "outro"; tbb = aw(s, "Big brains"); tmy = aw(s, "still a mystery"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'BIG BRAINS · BIG FAMILIES')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tbb:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "Why would"), g("hook", "do that"))
wave(g("intro", "I'm Max"))
wow(g("dolphin", "giant dolphins"), 1.2)
point(g("squid", "is squid"), 1.2)
wow(g("brain", "thirty seven billion"), 1.2)
point(g("family", "two hundred"), 1.2)
point(g("milk", "three years"), 1.2)
point(g("strand", "strand in groups"), 1.2)
wow(g("twist", "several families"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "onto a beach"), 0.45), ("pop.mp3", A("hook", "rest of its group"), 0.45), ("ping.mp3", A("hook", "whole pod"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("dolphin", "giant dolphins"), 0.4), ("pop.mp3", A("squid", "is squid"), 0.45),
        ("impact-bass-1.mp3", A("brain", "thirty seven billion"), 0.35), ("pop.mp3", A("family", "two hundred"), 0.45),
        ("click-soft.mp3", A("milk", "three years"), 0.5), ("whoosh-short.mp3", A("strand", "gets stuck"), 0.45),
        ("riser.mp3", A("twist", "the twist"), 0.3), ("ping.mp3", A("twist", "several families"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
