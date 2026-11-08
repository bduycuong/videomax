# How a distillation tower splits crude oil: doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
# === SCENES ===
OV = f"""
.top {{ position:absolute; left:0; right:0; top:120px; text-align:center; opacity:0; }}
.top .chip {{ font-size:46px; }}
.tag {{ position:absolute; background:#FFFFFF; border:4px solid {K}; {SKETCH} padding:2px 22px; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.15; box-shadow:4px 5px 0 rgba(38,42,59,.25); white-space:nowrap; opacity:0; }}
.note {{ position:absolute; left:430px; right:40px; top:906px; text-align:center; font-family:'Gochi Hand',cursive; font-size:48px; line-height:1.1; opacity:0; }}
.sticky {{ position:absolute; width:230px; padding:12px 10px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; border:4px solid {K}; {SKETCH} opacity:0; }}
"""
def chip(i, txt): return f'<div class="top" id="{i}"><span class="chip">{txt}</span></div>'
def tag(i, txt, x, y, extra=""): return f'<div id="{i}" class="tag" style="left:{x}px;top:{y}px;{extra}">{txt}</div>'
def note(i, txt): return f'<div id="{i}" class="note">{txt}</div>'
def svgpath(i, d, color, w=7, extra=""): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round" style="opacity:0" {extra}/></svg>'

s = "hook"; tg = aw(s, "gasoline"); td = aw(s, "diesel"); tr = aw(s, "road tar"); tq = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:62px; white-space:nowrap; opacity:0; }", f"""
  <div id="hk-t" class="h1">One tower, <span class="hl">many fuels?</span></div>
  <div id="hk-a" class="sticky" style="left:50px;top:270px;background:{C['hi']}">gasoline</div>
  <div id="hk-b" class="sticky" style="left:50px;top:400px;background:#C9E8C2">diesel</div>
  <div id="hk-c" class="sticky" style="left:50px;top:530px;background:#F6C9C2">road tar</div>
  {note('hk-n', 'how? <span class="hl">guess!</span>')}
""", f"""
pop("#hk-t", 0.3); pop("#hk-a", {tg:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}}); pop("#hk-b", {td:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}});
pop("#hk-c", {tr:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}}); rise("#hk-n", {tq-0.2:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); ti = aw(s, "inside the tower")
scenes[s] = scene_file(s, OV, f"""
  {chip('in-c', 'MAX WISE')}
  {note('in-n', 'inside the <span class="hl">tower</span> →')}
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {ti-0.3:.2f});
""")

s = "oldway"; tb = aw(s, "boiled"); tc = aw(s, "coiled pipe"); tdr = aw(s, "dripped out")
scenes[s] = scene_file(s, OV, f"""
  {chip('ow-c', 'THE OLD WAY')}
  {tag('ow-a', 'boil the pot', 640, 280, 'color:' + C['red'])}
  {tag('ow-b', 'cool → drip', 660, 790, 'color:' + C['blue'])}
""", f"""
pop("#ow-c", 0.05); pop("#ow-a", {tb:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
tl.to("#ow-a", {{opacity:0, duration:0.25}}, {tc-0.3:.2f}); pop("#ow-b", {tc:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
""")

s = "slow"; tdn = aw(s, "drained"); trf = aw(s, "refilled"); tsl = aw(s, "slow and messy")
scenes[s] = scene_file(s, OV, f"""
  {chip('sl-c', 'ONE BATCH AT A TIME')}
  {note('sl-n', 'drain · refill · <span class="red">repeat…</span>')}
  {tag('sl-t', 'SLOW!', 760, 300, 'font-size:60px;color:' + C['red'])}
""", f"""
pop("#sl-c", 0.05); rise("#sl-n", {tdn:.2f}); pop("#sl-t", {tsl:.2f}, {{from:{{scale:1.8, rotation:-20}}, to:{{rotation:-6}}}});
""")

s = "mix"; ts = aw(s, "the secret"); tmx = aw(s, "many molecules"); te = aw(s, "boil easily"); th = aw(s, "really hot")
scenes[s] = scene_file(s, OV, f"""
  {chip('mx-c', 'CRUDE = A <span class="hl">MIX</span>')}
  <div id="mx-card" class="card" style="left:640px;top:600px;width:390px;padding:14px 22px;font-family:'Gochi Hand',cursive;opacity:0">
    <div id="mx-1" style="font-size:42px;line-height:1.3;opacity:0"><span class="blue">●</span> boils easily</div>
    <div id="mx-2" style="font-size:42px;line-height:1.3;opacity:0"><span class="red">●</span> needs real heat</div></div>
""", f"""
pop("#mx-c", {tmx:.2f}); rise("#mx-card", {tmx+0.3:.2f});
tl.fromTo("#mx-1", {{opacity:0, x:-20}}, {{opacity:1, x:0, duration:0.25}}, {te:.2f});
tl.fromTo("#mx-2", {{opacity:0, x:-20}}, {{opacity:1, x:0, duration:0.25}}, {th-0.3:.2f});
""")

s = "heat"; tcl = aw(s, "cleaned"); tf = aw(s, "furnace"); thd = aw(s, "hundreds of degrees")
scenes[s] = scene_file(s, OV, f"""
  {chip('ht-c', 'STEP 1 · FURNACE')}
  {tag('ht-a', 'HOT!', 820, 290, 'font-size:60px;color:' + C['red'])}
  {note('ht-n', 'heated to <span class="hl">hundreds of °C</span>')}
""", f"""
pop("#ht-c", {tcl-0.2:.2f}); pop("#ht-a", {tf:.2f}, {{from:{{scale:1.8, rotation:16}}, to:{{rotation:5}}}}); rise("#ht-n", {thd-0.2:.2f});
""")

s = "feed"; tv = aw(s, "into vapor"); tri = aw(s, "vapor rises"); tlf = aw(s, "liquid falls")
scenes[s] = scene_file(s, OV, f"""
  {chip('fd-c', 'STEP 2 · INTO THE TOWER')}
  {svgpath('fd-u', 'M960,820 L960,330 M920,380 L960,330 L1000,380', C['blue'], 9)}
  {svgpath('fd-d', 'M90,330 L90,820 M50,770 L90,820 L130,770', C['red'], 9)}
  {tag('fd-a', 'vapor ↑', 760, 260, 'color:' + C['blue'])}
  {tag('fd-b', 'liquid ↓', 130, 790, 'color:' + C['red'])}
""", f"""
pop("#fd-c", {tv-0.3:.2f});
tl.set("#fd-u", {{opacity:1}}, {tri:.2f}); draw("#fd-u", {tri:.2f}, 0.6); pop("#fd-a", {tri+0.3:.2f});
tl.set("#fd-d", {{opacity:1}}, {tlf:.2f}); draw("#fd-d", {tlf:.2f}, 0.6); pop("#fd-b", {tlf+0.3:.2f});
""")

s = "trays"; tt = aw(s, "stacked with trays"); tbc = aw(s, "bubble caps")
scenes[s] = scene_file(s, OV, f"""
  {chip('tr-c', 'STEP 3 · TRAYS')}
  {tag('tr-a', 'bubble caps', 700, 790, 'font-size:50px')}
  {svgpath('tr-p', 'M800,780 Q760,700 700,640', K, 6)}
""", f"""
pop("#tr-c", {tt:.2f}); pop("#tr-a", {tbc:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.set("#tr-p", {{opacity:1}}, {tbc+0.2:.2f}); draw("#tr-p", {tbc+0.2:.2f}, 0.4);
""")

s = "bubble"; tu = aw(s, "under each cap"); tbt = aw(s, "bubble through")
scenes[s] = scene_file(s, OV, f"""
  {chip('bb-c', 'BUBBLE <span class="blue">THROUGH</span>')}
  {note('bb-n', 'vapor <span class="blue">meets</span> liquid')}
  {tag('bb-a', 'blub blub', 780, 300, 'font-size:50px;color:' + C['blue'])}
""", f"""
pop("#bb-c", 0.05); pop("#bb-a", {tu:.2f}, {{from:{{rotation:12}}, to:{{rotation:4}}}}); rise("#bb-n", {tbt:.2f});
""")

s = "sort"; tho = aw(s, "is hot"); tco = aw(s, "cooler"); thv = aw(s, "heavier molecules"); tlg = aw(s, "lighter ones")
therm = f'''<svg id="so-th" class="abs" style="left:950px;top:270px;opacity:0" width="90" height="600" viewBox="0 0 90 600" data-layout-ignore>
  <defs><linearGradient id="so-g" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{C['red']}"/><stop offset="1" stop-color="{C['blue']}"/></linearGradient></defs>
  <rect x="25" y="10" width="40" height="520" rx="20" fill="url(#so-g)" stroke="{K}" stroke-width="5"/>
  <circle cx="45" cy="555" r="36" fill="{C['red']}" stroke="{K}" stroke-width="5"/></svg>'''
scenes[s] = scene_file(s, OV, f"""
  {chip('so-c', 'HOT BOTTOM · <span class="blue">COOL TOP</span>')}
  {therm}
  {tag('so-a', 'light → climbs ↑', 520, 280, 'color:' + C['blue'])}
  {tag('so-b', 'heavy → stays', 560, 790, 'color:' + C['red'])}
""", f"""
pop("#so-c", {tho-0.3:.2f}); rise("#so-th", {tho:.2f}, 0.5);
pop("#so-b", {thv:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}}); pop("#so-a", {tlg:.2f}, {{from:{{rotation:10}}, to:{{rotation:2}}}});
""")

s = "draw"; tdh = aw(s, "each height"); tga = aw(s, "gasoline"); tke = aw(s, "kerosene"); thv2 = aw(s, "heavy oils")
tower = f'''<div id="dw-card" class="card" style="left:660px;top:250px;width:380px;height:620px;opacity:0">
  <svg class="abs" style="left:20px;top:20px" width="120" height="580" viewBox="0 0 120 580" data-layout-ignore>
    <rect x="20" y="10" width="80" height="560" rx="30" fill="#FFFFFF" {WS.replace('fill="none" ', '')}/>
    {"".join(f'<path d="M28,{90+i*80} L92,{90+i*80}" stroke="{K}" stroke-width="4"/>' for i in range(6))}
    <rect x="24" y="490" width="72" height="76" rx="20" fill="{C['red']}" opacity=".55"/></svg>
  <div id="dw-1" class="abs" style="left:150px;top:60px;font-family:'Gochi Hand',cursive;font-size:42px;opacity:0">← <span class="hl">gasoline</span></div>
  <div id="dw-2" class="abs" style="left:150px;top:250px;font-family:'Gochi Hand',cursive;font-size:42px;line-height:1.1;opacity:0">← kerosene<br>&nbsp;&nbsp;&nbsp;+ diesel</div>
  <div id="dw-3" class="abs" style="left:150px;top:480px;font-family:'Gochi Hand',cursive;font-size:42px;opacity:0">← <span class="red">heavy oils</span></div></div>'''
scenes[s] = scene_file(s, OV, f"""
  {chip('dw-c', 'EACH FLOOR, A NEW PRODUCT')}
  {tower}
""", f"""
pop("#dw-c", {tdh:.2f}); rise("#dw-card", {tdh+0.2:.2f});
{"".join(f'tl.fromTo("#dw-{k}", {{opacity:0, x:-20}}, {{opacity:1, x:0, duration:0.25}}, {t:.2f});' for k, t in [(1, tga), (2, tke), (3, thv2)])}
""")

s = "reflux"; tcd = aw(s, "is cooled"); tbk = aw(s, "back down"); tcl2 = aw(s, "gets cleaner")
scenes[s] = scene_file(s, OV, f"""
  {chip('rf-c', 'STEP 4 · COOL + SEND BACK')}
  {svgpath('rf-p', 'M760,300 Q1010,300 1010,520 Q1010,760 840,800 M880,760 L840,800 L885,835', C['blue'], 9)}
  {tag('rf-a', 'back down!', 560, 470, 'color:' + C['blue'])}
  {note('rf-n', '→ a <span class="hl">cleaner split</span>')}
""", f"""
pop("#rf-c", {tcd-0.2:.2f}); tl.set("#rf-p", {{opacity:1}}, {tbk:.2f}); draw("#rf-p", {tbk:.2f}, 0.8);
pop("#rf-a", {tbk+0.4:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#rf-n", {tcl2-0.3:.2f});
""")

s = "bottom"; tsc = aw(s, "second tower"); tlp = aw(s, "low pressure"); tas = aw(s, "road asphalt")
scenes[s] = scene_file(s, OV, f"""
  {chip('bt-c', 'THE LEFTOVERS')}
  {tag('bt-a', 'tower #2: low pressure', 520, 280, 'font-size:42px')}
  {note('bt-n', 'sticky bits → <span class="hl">asphalt</span>')}
""", f"""
pop("#bt-c", 0.05); pop("#bt-a", {tlp:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}}); rise("#bt-n", {tas-0.4:.2f});
""")

s = "barrel"; tft = aw(s, "forty two"); tni = aw(s, "nineteen to twenty"); tus = aw(s, "US refineries")
scenes[s] = scene_file(s, OV, f"""
  {chip('br-c', 'ONE BARREL')}
  <div id="br-card" class="card" style="left:540px;top:290px;width:480px;padding:18px 26px;text-align:center;font-family:'Gochi Hand',cursive;opacity:0">
    <div style="font-size:64px;line-height:1.1">42 gal crude</div>
    <div id="br-ar" style="font-size:56px;line-height:1;opacity:0">↓</div>
    <div id="br-g" style="font-size:54px;line-height:1.15;opacity:0;white-space:nowrap">about <span class="hl">19–20 gal</span><br>of gasoline</div></div>
  {note('br-n', 'in US refineries')}
""", f"""
pop("#br-c", {tft-0.6:.2f}); rise("#br-card", {tft-0.1:.2f});
tl.to("#br-ar", {{opacity:1, duration:0.2}}, {tni-0.4:.2f}); pop("#br-g", {tni:.2f}); rise("#br-n", {tus-0.2:.2f});
""")

s = "outro"; tbp = aw(s, "boiling point"); tsc2 = aw(s, "floor by floor")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'SORTED BY BOILING POINT')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">one tower, many fuels</div></div>
""", f"""
pop("#ou-c", {tbp-0.3:.2f});
pop("#ou-big", {tsc2:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "how can"), g("hook", "road tar"))
point(g("hook", "take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("intro", "inside the tower"), 1.2)
point(g("oldway", "boiled"), 1.2)
wow(g("slow", "slow and messy"), 1.0)
wow(g("mix", "the secret"), 1.0)
point(g("heat", "furnace"), 1.2)
point(g("feed", "vapor rises"), 1.2)
point(g("trays", "bubble caps"), 1.2)
point(g("bubble", "bubble through"), 1.2)
point(g("sort", "heavier molecules"), 1.2)
point(g("draw", "gasoline"), 1.2)
point(g("reflux", "back down"), 1.2)
point(g("bottom", "second tower"), 1.2)
wow(g("barrel", "nineteen to twenty"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "gasoline"), 0.45), ("pop.mp3", A("hook", "diesel"), 0.45), ("pop.mp3", A("hook", "road tar"), 0.45),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("impact-bass-1.mp3", A("slow", "slow and messy"), 0.35),
        ("click-soft.mp3", A("mix", "boil easily"), 0.5), ("impact-bass-2.mp3", A("heat", "furnace"), 0.3),
        ("whoosh-short.mp3", A("feed", "vapor rises"), 0.3), ("pop.mp3", A("trays", "bubble caps"), 0.45),
        ("click.mp3", A("sort", "heavier molecules"), 0.35), ("ping.mp3", A("draw", "gasoline"), 0.35),
        ("whoosh-short.mp3", A("reflux", "back down"), 0.3), ("ping.mp3", A("barrel", "nineteen to twenty"), 0.4),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
