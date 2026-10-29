# Why don't containers fall off ships in storms? Doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
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

s = "hook"; tw = aw(s, "Monster waves"); ts = aw(s, "slide off"); tg = aw(s, "Glue"); tgu = aw(s, "Take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:58px; white-space:nowrap; }", f"""
  <div id="hk-t" class="h1">Why don't the boxes <span class="hl">fall off</span>?</div>
  {tag('hk-a', 'glue?', 60, 280)}
  {tag('hk-b', 'gravity?', 300, 280)}
  {tag('hk-c', 'something clever?', 620, 280)}
  <div id="hk-n" class="note">take a <span class="hl">guess</span>!</div>
""", f"""
pop("#hk-t", 0.05); pop("#hk-a", {tg:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#hk-b", {tg+0.55:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
pop("#hk-c", {tgu:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#hk-n", {tgu+0.3:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); th = aw(s, "the hold")
scenes[s] = scene_file(s, OV, f"""
  <div class="top"><span id="in-c" class="chip">MAX WISE</span></div>
  <div id="in-n" class="note">the secret starts in the <span class="hl">hold</span></div>
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {th:.2f});
""")

s = "rails"; tr = aw(s, "steel rails"); tc = aw(s, "drift sideways")
scenes[s] = scene_file(s, OV, f"""
  {chip('rl-c', 'BELOW DECK')}
  {tag('rl-t', 'steel guide rails', 600, 290)}
  <div id="rl-n" class="note">no room to <span class="hl">drift</span></div>
""", f"""
pop("#rl-c", 0.05); pop("#rl-t", {tr:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#rl-n", {tc:.2f});
""")

s = "deck"; tn = aw(s, "no rails"); tl = aw(s, "own lock")
scenes[s] = scene_file(s, OV, f"""
  {chip('dk-c', 'ON DECK')}
  <div id="dk-x" class="gag" style="left:600px;top:280px;transform:rotate(-8deg)">NO RAILS!</div>
  <div id="dk-n" class="note">each box needs a <span class="hl">lock</span></div>
""", f"""
pop("#dk-c", 0.05); pop("#dk-x", {tn:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#dk-n", {tl:.2f});
""")

s = "corner"; tco = aw(s, "box's corner"); to = aw(s, "oval holes")
scenes[s] = scene_file(s, OV, f"""
  {chip('cn-c', 'CORNER CASTING')}
  {tag('cn-t', 'oval holes', 640, 790)}
  <div id="cn-n" class="note">solid <span class="hl">steel</span> block</div>
""", f"""
pop("#cn-c", {tco:.2f}); pop("#cn-t", {to:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#cn-n", {to+0.5:.2f});
""")

s = "lock"; tt = aw(s, "a twistlock"); tcn = aw(s, "Its cone"); ttw = aw(s, "One twist"); tlk = aw(s, "locked together")
scenes[s] = scene_file(s, OV, f"""
  {chip('lk-c', 'THE TWISTLOCK')}
  {tag('lk-a', 'cone in both holes', 60, 790)}
  <div id="lk-x" class="gag" style="left:640px;top:280px;transform:rotate(-8deg)">TWIST!</div>
  <div id="lk-n" class="note">boxes <span class="hl">locked</span> together</div>
""", f"""
pop("#lk-c", {tt:.2f}); pop("#lk-a", {tcn:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#lk-x", {ttw:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#lk-n", {tlk:.2f});
""")

s = "semi"; tsa = aw(s, "semi automatic"); tsn = aw(s, "snaps shut"); tro = aw(s, "pulls a rod")
scenes[s] = scene_file(s, OV, f"""
  {chip('sm-c', 'SEMI-AUTOMATIC')}
  <div id="sm-x" class="gag" style="left:560px;top:600px;transform:rotate(-8deg)">CLICK!</div>
  {tag('sm-t', 'pull rod = release', 560, 290)}
  <div id="sm-n" class="note">locks <span class="hl">by itself</span></div>
""", f"""
pop("#sm-c", {tsa:.2f}); pop("#sm-x", {tsn:.2f}, {{from:{{scale:0.3, rotation:-30}}, to:{{rotation:-8}}}}); rise("#sm-n", {tsn+0.6:.2f});
tl.to("#sm-x", {{opacity:0, duration:0.3}}, {tro-0.4:.2f});
pop("#sm-t", {tro:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
""")

s = "lash"; tla = aw(s, "lashing rods"); ttp = aw(s, "tip over")
scenes[s] = scene_file(s, OV, f"""
  {chip('ls-c', 'LASHING RODS')}
  {tag('ls-t', 'ties boxes to the ship', 360, 790)}
  <div id="ls-n" class="note">or a tall stack can <span class="hl">tip</span></div>
""", f"""
pop("#ls-c", 0.05); pop("#ls-t", {tla:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#ls-n", {ttp:.2f});
""")

s = "lost"; tf = aw(s, "do fall"); t15 = aw(s, "fifteen hundred"); t280 = aw(s, "two hundred eighty million")
scenes[s] = scene_file(s, OV, f"""
  {chip('ls2-c', 'LOST AT SEA · 2025')}
  {tag('lo-a', '≈ 1,500 lost', 60, 290)}
  {tag('lo-b', 'of ≈ 280,000,000', 520, 290)}
  <div id="lo-n" class="note">a <span class="hl">tiny</span> fraction</div>
""", f"""
pop("#ls2-c", {tf:.2f}); pop("#lo-a", {t15:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
pop("#lo-b", {t280:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); rise("#lo-n", {t280+1.2:.2f});
""")

s = "float"; tfl = aw(s, "float for a while"); td = aw(s, "a danger")
scenes[s] = scene_file(s, OV, f"""
  {chip('fl-c', 'WHAT IF ONE FALLS?')}
  {tag('fl-t', 'floats just under the waves', 300, 790)}
  <div id="fl-n" class="note">a hidden <span class="hl">danger</span></div>
""", f"""
pop("#fl-c", 0.05); pop("#fl-t", {tfl:.2f}, {{from:{{rotation:10}}, to:{{rotation:-2}}}}); rise("#fl-n", {td:.2f});
""")

s = "outro"; tgl = aw(s, "not glue"); tr2 = aw(s, "rails below"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'RAILS · TWISTLOCKS · LASHINGS')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span></div>
""", f"""
pop("#ou-c", {tr2:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "So why"), g("hook", "slide off"))
point(g("hook", "Take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("rails", "steel rails"), 1.2)
wow(g("deck", "no rails"), 1.2)
point(g("corner", "oval holes"), 1.2)
wow(g("lock", "One twist"), 1.2)
point(g("semi", "snaps shut"), 1.2)
point(g("lash", "lashing rods"), 1.2)
wow(g("lost", "fifteen hundred"), 1.2)
point(g("float", "a danger"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "Monster waves"), 0.45), ("pop.mp3", A("hook", "Glue"), 0.45), ("ping.mp3", A("hook", "Take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("rails", "steel rails"), 0.4), ("impact-bass-1.mp3", A("deck", "no rails"), 0.35),
        ("pop.mp3", A("corner", "oval holes"), 0.45), ("click.mp3", A("lock", "One twist"), 0.5), ("click.mp3", A("semi", "snaps shut"), 0.5),
        ("pop.mp3", A("lash", "lashing rods"), 0.45), ("impact-bass-2.mp3", A("lost", "fifteen hundred"), 0.35),
        ("ping.mp3", A("float", "a danger"), 0.35), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
