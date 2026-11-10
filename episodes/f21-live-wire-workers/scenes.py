# Live-line workers: doodle overlays on the source animation. Footage panel x 20–1060, y 230–898.
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
def svgpath(i, d, color, w=7, extra=""): return f'<svg class="abs" style="left:0;top:0" width="1080" height="1100" data-layout-ignore><path id="{i}" d="{d}" stroke="{color}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round" style="opacity:0" {extra}/></svg>'


s = "hook"; tv = aw(s, "hundreds of thousands"); tq = aw(s, "take a guess")
scenes[s] = scene_file(s, OV + "#hk-t { top:110px; font-size:60px; white-space:nowrap; opacity:0; }", f"""
  <div id="hk-t" class="h1">Why no <span class="hl">ZAP?</span></div>
  <div id="hk-a" class="sticky" style="left:770px;top:280px;background:{C['hi']}">rubber gloves?</div>
  <div id="hk-b" class="sticky" style="left:770px;top:420px;background:#C9E8C2">power off?</div>
  <div id="hk-c" class="sticky" style="left:770px;top:560px;background:#F6C9C2">a secret suit?</div>
  {note('hk-n', 'your <span class="hl">guess?</span>')}
""", f"""
pop("#hk-t", 0.3); pop("#hk-a", {tv:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
pop("#hk-b", {tv+0.5:.2f}, {{from:{{rotation:12}}, to:{{rotation:3}}}}); pop("#hk-c", {tv+1.0:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-2}}}});
rise("#hk-n", {tq-0.2:.2f});
""")

s = "intro"; tm = aw(s, "Max Wise"); tb = aw(s, "a bird")
scenes[s] = scene_file(s, OV, f"""
  {chip('in-c', 'MAX WISE')}
  {note('in-n', 'clue: a <span class="hl">bird</span>')}
""", f"""
pop("#in-c", {tm:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); rise("#in-n", {tb-0.3:.2f});
""")

s = "bird"; tl1 = aw(s, "live wires"); tvd = aw(s, "voltage difference")
scenes[s] = scene_file(s, OV, f"""
  {chip('bi-c', 'BIRD ON A WIRE')}
  {tag('bi-a', 'live wire!', 760, 290, 'color:' + C['red'])}
  {note('bi-n', 'current needs a <span class="hl">push</span>')}
""", f"""
pop("#bi-c", 0.05); pop("#bi-a", {tl1:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#bi-n", {tvd-0.2:.2f});
""")

s = "same"; to1 = aw(s, "one wire"); tsv = aw(s, "wire's voltage"); tnc = aw(s, "no current")
scenes[s] = scene_file(s, OV, f"""
  {chip('sa-c', 'SAME VOLTAGE')}
  {tag('sa-a', 'one wire only', 440, 290)}
  {gauge('sa-g', 'bird = wire', 680, 400)}
  {note('sa-n', 'no difference → <span class="hl">no current</span>')}
""", f"""
pop("#sa-c", 0.05); pop("#sa-a", {to1:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}});
pop("#sa-g", {tsv:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#sa-n", {tnc-0.3:.2f});
""")

s = "danger"; tsw = aw(s, "second wire"); tr = aw(s, "rushes through")
scenes[s] = scene_file(s, OV, f"""
  {chip('da-c', '<span class="red">DANGER</span>')}
  {tag('da-a', '2 wires = ZAP!', 700, 290, 'font-size:56px;color:' + C['red'])}
""", f"""
pop("#da-c", 0.05); pop("#da-a", {tr-0.2:.2f}, {{from:{{scale:1.7, rotation:-14}}, to:{{rotation:-4}}}});
""")

s = "lineman"; tst = aw(s, "same trick"); tbw = aw(s, "bird on a wire")
scenes[s] = scene_file(s, OV, f"""
  {chip('li-c', 'LINE WORKERS')}
  {tag('li-a', 'the "bird on a wire" idea', 420, 290, 'font-size:42px')}
  {note('li-n', 'same <span class="hl">trick!</span>')}
""", f"""
pop("#li-c", 0.05); rise("#li-n", {tst-0.2:.2f}); pop("#li-a", {tbw:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
""")

s = "field"; tbg = aw(s, "much bigger"); tef = aw(s, "electric field"); tsp = aw(s, "spark")
scenes[s] = scene_file(s, OV, f"""
  {chip('fi-c', 'BUT PEOPLE ARE BIG')}
  {tag('fi-a', 'strong electric field', 420, 290, 'color:' + C['blue'])}
  {tag('fi-b', 'SPARK!', 800, 400, 'font-size:60px;color:' + C['red'])}
""", f"""
pop("#fi-c", {tbg-0.4:.2f}); pop("#fi-a", {tef:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}});
pop("#fi-b", {tsp:.2f}, {{from:{{scale:1.8, rotation:-16}}, to:{{rotation:-5}}}});
""")

s = "suit"; tss = aw(s, "stainless steel"); tmc = aw(s, "metal clothes")
scenes[s] = scene_file(s, OV, f"""
  {chip('su-c', 'THE SUIT')}
  {tag('su-a', 'woven steel threads', 440, 290)}
  {gauge('su-g', 'metal?!', 800, 420, 'color:' + C['red'])}
""", f"""
pop("#su-c", 0.05); pop("#su-a", {tss:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#su-g", {tmc:.2f}, {{from:{{scale:1.6, rotation:12}}, to:{{rotation:4}}}});
""")

s = "cage"; tfc = aw(s, "Faraday cage"); tar = aw(s, "around the suit")
scenes[s] = scene_file(s, OV, f"""
  {chip('ca-c', 'FARADAY <span class="hl">CAGE</span>')}
  {note('ca-n', 'goes <span class="hl">around</span>, not through')}
""", f"""
pop("#ca-c", {tfc-0.2:.2f}, {{from:{{scale:1.5}}, to:{{}}}}); rise("#ca-n", {tar-0.3:.2f});
""")

s = "plane"; tli = aw(s, "lightning hits"); tms = aw(s, "metal skin"); tsf = aw(s, "safe inside")
scenes[s] = scene_file(s, OV, f"""
  {chip('pl-c', 'SAME IDEA')}
  {tag('pl-a', 'current rides the metal skin', 400, 790, 'font-size:42px;color:' + C['blue'])}
  {note('pl-n', 'passengers: <span class="hl">safe</span>')}
""", f"""
pop("#pl-c", 0.05); pop("#pl-a", {tms-0.2:.2f}, {{from:{{rotation:6}}, to:{{rotation:1}}}}); rise("#pl-n", {tsf-0.4:.2f});
""")

s = "bucket"; tin = aw(s, "insulated")
scenes[s] = scene_file(s, OV, f"""
  {chip('bu-c', 'STEP 1: GO UP')}
  {tag('bu-a', 'insulated bucket', 700, 290)}
""", f"""
pop("#bu-c", 0.05); pop("#bu-a", {tin:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

s = "bond"; twd = aw(s, "metal wand"); tsn = aw(s, "Snap"); tmt = aw(s, "match the line"); trk = aw(s, "riskiest")
scenes[s] = scene_file(s, OV + "#bo-s { position:absolute; left:640px; top:330px; font-family:'Gochi Hand',cursive; font-size:110px; color:#FFE14D; -webkit-text-stroke:4px " + K + "; opacity:0; }", f"""
  {chip('bo-c', 'STEP 2: MATCH THE LINE')}
  {tag('bo-a', 'metal wand', 440, 300)}
  <div id="bo-s">SNAP!</div>
  {note('bo-n', 'riskiest <span class="red">moment</span>')}
""", f"""
pop("#bo-c", 0.05); pop("#bo-a", {twd:.2f}, {{from:{{rotation:8}}, to:{{rotation:2}}}});
tl.to("#bo-a", {{opacity:0, duration:0.2}}, {tsn-0.25:.2f});
pop("#bo-s", {tsn:.2f}, {{from:{{scale:2.2, rotation:-18}}, to:{{rotation:-6}}}});
tl.to("#bo-s", {{opacity:0, duration:0.25}}, {tmt+0.6:.2f}); rise("#bo-n", {trk-0.2:.2f});
""")

s = "work"; tbh = aw(s, "bare handed"); th = aw(s, "homes")
scenes[s] = scene_file(s, OV, f"""
  {chip('wo-c', 'STEP 3: FIX IT LIVE')}
  {tag('wo-a', 'bare hands!', 760, 290, 'color:' + C['red'])}
  {note('wo-n', 'power keeps <span class="hl">flowing</span>')}
""", f"""
pop("#wo-c", 0.05); pop("#wo-a", {tbh:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}}); rise("#wo-n", {th-0.5:.2f});
""")

s = "outro"; tmx = aw(s, "matching the line"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, OV, f"""
  {chip('ou-c', 'MATCH THE LINE = <span class="blue">NO ZAP</span>')}
  <div id="ou-big" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><span class="chip" style="font-size:96px;padding:6px 40px">Stay curious!</span>
    <div style="margin-top:22px;font-family:'Gochi Hand',cursive;font-size:56px;color:#FFFFFF;text-shadow:0 3px 0 {K},0 -3px 0 {K},3px 0 0 {K},-3px 0 0 {K}">be the bird on the wire</div></div>
""", f"""
pop("#ou-c", {tmx-0.3:.2f});
pop("#ou-big", {tsc:.2f}, {{from:{{scale:0.3, rotation:-8}}, to:{{rotation:-2}}}});
""", fade=False)

# === GESTURES ===
think(g("hook", "how can"), g("hook", "not get hurt"))
point(g("hook", "take a guess"), 1.0)
wave(g("intro", "I'm Max"))
point(g("intro", "a bird"), 1.2)
point(g("bird", "voltage difference"), 1.2)
point(g("same", "no current"), 1.0)
wow(g("danger", "rushes through"), 1.0)
point(g("lineman", "bird on a wire"), 1.2)
wow(g("field", "spark"), 1.0)
think(g("suit", "metal clothes"), g("suit", "power line") + 0.5)
wow(g("cage", "Faraday cage"), 1.0)
point(g("plane", "metal skin"), 1.2)
point(g("bucket", "insulated"), 1.0)
wow(g("bond", "Snap"), 1.0)
point(g("work", "bare handed"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "hundreds of thousands"), 0.45), ("ping.mp3", A("hook", "take a guess"), 0.35),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("pop.mp3", A("same", "wire's voltage"), 0.45),
        ("impact-bass-1.mp3", A("danger", "rushes through"), 0.35), ("click.mp3", A("lineman", "bird on a wire"), 0.4),
        ("impact-bass-2.mp3", A("field", "spark"), 0.3), ("pop.mp3", A("suit", "metal clothes"), 0.45),
        ("sparkle.mp3", A("cage", "Faraday cage"), 0.4), ("click-soft.mp3", A("bucket", "insulated"), 0.5),
        ("impact-bass-1.mp3", A("bond", "Snap"), 0.4), ("ping.mp3", A("work", "bare handed"), 0.35),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
