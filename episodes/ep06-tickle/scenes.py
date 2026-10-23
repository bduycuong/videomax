# MAX WISE ep06 — Why can't you tickle yourself?  Executed inside engine/maxwise.py.
# === SCENES ===
def feather_svg(pid, w=260):
    return f'''<svg id="{pid}" width="{w}" height="{w*1.4:.0f}" viewBox="0 0 100 140" style="overflow:visible" data-layout-ignore>
  <path d="M50,135 Q52,80 70,10" {WS}/>
  <path d="M70,10 Q95,30 82,70 Q72,100 54,118 Q40,90 46,60 Q52,25 70,10 Z" fill="#BFE3F7" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>
  <path d="M66,30 L82,36 M62,48 L84,52 M58,66 L80,72 M55,84 L74,90 M64,30 L50,40 M60,50 L46,58 M56,70 L44,78" stroke="{C['blue']}" stroke-width="3" stroke-linecap="round"/></svg>'''

def brain_svg(pid, w=420, cereb=False):
    cb = (f'<g id="{pid}-cb"><path d="M128,140 Q150,128 178,132 Q196,142 186,160 Q160,172 134,162 Q122,152 128,140 Z" fill="#FFC9C2" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
          f'<path d="M138,146 Q158,142 178,146 M136,155 Q158,152 180,154" stroke="{C["red"]}" stroke-width="3" fill="none" stroke-linecap="round"/></g>') if cereb else ""
    return f'''<svg id="{pid}" width="{w}" height="{w*0.86:.0f}" viewBox="0 0 210 180" style="overflow:visible" data-layout-ignore>
  {cb}
  <path d="M40,120 Q10,110 18,80 Q8,50 40,40 Q50,12 86,20 Q106,4 130,18 Q166,10 176,42 Q206,54 194,88 Q204,120 172,128 Q150,140 120,136 Q100,150 80,140 Q58,150 40,120 Z" fill="#FFD6E0" {WS.replace('fill="none" ', '')}/>
  <path d="M60,60 Q80,50 90,70 Q100,90 120,76 M70,100 Q96,96 110,116 M130,48 Q150,40 160,60 M140,96 Q160,90 170,104" {WS}/></svg>'''

def meter(pid, x, y, w, label, col):
    return (f'<div id="{pid}" class="abs" style="left:{x}px;top:{y}px;width:{w}px">'
            f'<div style="font-size:46px;margin-bottom:8px">{label}</div>'
            f'<div style="position:relative;height:64px;border:4px solid {K};{SKETCH}background:#fff;overflow:hidden">'
            f'<div id="{pid}-f" style="position:absolute;left:0;top:0;bottom:0;width:100%;background:{col};transform-origin:0 50%"></div></div></div>')

# 1 HOOK
s = "hook"; tq = aw(s, "why can't"); tt = aw(s, "tickle yourself")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:270px; font-size:96px; }}
#hk-fw {{ position:absolute; left:400px; top:540px; }}
#hk-ha {{ position:absolute; left:700px; top:600px; font-size:80px; color:{C['red']}; transform:rotate(8deg); }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">Why can't you <span class="hl">tickle</span> yourself?</div>
  <div id="hk-fw">{feather_svg('hk-f', 240)}</div>
  <div id="hk-ha" class="big">?!</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {tq-0.05:.2f}); pop("#hk-fw", {tt:.2f});
tl.fromTo("#hk-f", {{rotation:-14, svgOrigin:"50 135"}}, {{rotation:14, svgOrigin:"50 135", duration:0.18, yoyo:true, repeat:9, ease:"sine.inOut"}}, {tt+0.2:.2f});
pop("#hk-ha", {tt+0.5:.2f}, {{from:{{rotation:-10}}, to:{{rotation:8}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "skin too"); t2 = aw(s, "too brave"); t3 = aw(s, "brain playing")
notes = [("skin", "Tough<br>skin?", -6, 110, C['hi']), ("brave", "Too<br>brave?", 4, 405, "#BFE3F7"), ("brain", "Brain<br>trick?", -3, 700, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:64px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-skin", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-brave", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-brain", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's find")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's find out!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 TRY — self tickle, meter stays at zero
s = "try"; ttr = aw(s, "try it"); tno = aw(s, "nothing right")
scenes[s] = scene_file(s, f"""
#tr-arm {{ position:absolute; left:140px; top:300px; }}
#tr-fw {{ position:absolute; left:520px; top:200px; }}
#tr-meh {{ position:absolute; left:0; right:0; top:830px; text-align:center; font-size:64px; color:{C['red']}; }}
""", f"""
  <div id="tr-title" class="h1" style="top:150px;font-size:74px">Try it <span class="hl">right now</span>…</div>
  <svg id="tr-arm" width="800" height="300" viewBox="0 0 800 300" data-layout-ignore>
    <path d="M10,120 Q300,100 560,118 Q640,110 700,130 Q760,150 740,190 Q700,220 620,210 Q560,214 300,214 Q120,216 10,210" fill="#FFE8D6" {WS.replace('fill="none" ', '')}/>
    <path d="M620,140 Q660,150 690,146 M620,175 Q665,182 700,176" {WS}/></svg>
  <div id="tr-fw">{feather_svg('tr-f', 200)}</div>
  {meter('tr-m', 240, 640, 600, 'tickle-o-meter', C['red'])}
  <div id="tr-meh" class="big">…nothing?</div>
""", f"""
rise("#tr-title", 0.0); rise("#tr-arm", 0.1); pop("#tr-fw", {ttr:.2f}); rise("#tr-m", {ttr+0.2:.2f});
tl.fromTo("#tr-fw", {{x:0, rotation:-10}}, {{x:-160, rotation:10, duration:0.3, yoyo:true, repeat:5, ease:"sine.inOut"}}, {ttr+0.3:.2f});
tl.fromTo("#tr-m-f", {{scaleX:0}}, {{scaleX:0.05, duration:0.3}}, {ttr+0.4:.2f});
pop("#tr-meh", {tno:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 5 PREDICT — move -> brain -> guess bubble
s = "predict"; tmv = aw(s, "you move"); tbr = aw(s, "your brain"); tgs = aw(s, "quick guess"); tfe = aw(s, "going to feel")
scenes[s] = scene_file(s, f"""
#pr-move {{ left:90px; top:330px; width:300px; height:170px; display:flex; align-items:center; justify-content:center; font-family:'Gochi Hand',cursive; font-size:60px; }}
#pr-bw {{ position:absolute; left:560px; top:330px; }}
#pr-bub {{ left:200px; top:640px; width:700px; height:200px; display:flex; align-items:center; justify-content:center; text-align:center; font-family:'Gochi Hand',cursive; font-size:58px; line-height:1.05; background:{C['hi']}; }}
""", f"""
  <div id="pr-title" class="h1" style="top:150px;font-size:72px">Your brain <span class="hl">predicts</span></div>
  <div id="pr-move" class="card">I move…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore><path id="pr-ar" d="M400,415 Q470,395 545,415 M520,395 L548,416 L518,434" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <div id="pr-bw">{brain_svg('pr-b', 380)}</div>
  <div id="pr-bub" class="card">"I know what<br>you'll feel next!"</div>
""", f"""
rise("#pr-title", 0.0); pop("#pr-move", {tmv:.2f}); draw("#pr-ar", {tmv+0.3:.2f}, 0.35);
pop("#pr-bw", {tbr:.2f}); pop("#pr-bub", {tgs:.2f}, {{from:{{rotation:-6}}, to:{{rotation:-2}}}});
tl.fromTo("#pr-bub", {{scale:1}}, {{scale:1.06, duration:0.14, yoyo:true, repeat:1}}, {tfe:.2f});
""")

# 6 CANCEL — cerebellum turns the feeling down
s = "cancel"; tbk = aw(s, "back of"); tcb = aw(s, "the cerebellum"); tdn = aw(s, "way down")
scenes[s] = scene_file(s, f"""
#cn-bw {{ position:absolute; left:110px; top:250px; }}
#cn-lab {{ position:absolute; left:560px; top:560px; font-family:'Gochi Hand',cursive; font-size:62px; color:{C['red']}; }}
""", f"""
  <div id="cn-title" class="h1" style="top:150px;font-size:72px">The <span class="hl">volume knob</span></div>
  <div id="cn-bw">{brain_svg('cn-b', 440, cereb=True)}</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="700" data-layout-ignore><path id="cn-ar" d="M560,600 Q500,620 470,580" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
  <div id="cn-lab">cerebellum</div>
  {meter('cn-m', 560, 300, 420, 'feeling', C['red'])}
""", f"""
rise("#cn-title", 0.0); pop("#cn-bw", 0.1);
tl.fromTo("#cn-b-cb", {{scale:1}}, {{scale:1.18, svgOrigin:"158 150", duration:0.2, yoyo:true, repeat:3}}, {tbk:.2f});
draw("#cn-ar", {tcb:.2f}, 0.3); pop("#cn-lab", {tcb+0.1:.2f});
rise("#cn-m", {tcb+0.4:.2f}); tl.fromTo("#cn-m-f", {{scaleX:0}}, {{scaleX:1, duration:0.4}}, {tcb+0.5:.2f});
tl.fromTo("#cn-m-f", {{scaleX:1}}, {{scaleX:0.1, duration:0.7, ease:"power2.inOut", immediateRender:false}}, {tdn:.2f});
""")

# 7 OTHER — you vs someone else
s = "other"; tse = aw(s, "someone else"); tcp = aw(s, "can't predict"); tsu = aw(s, "a surprise"); tti = aw(s, "what tickles")
scenes[s] = scene_file(s, f"""
#ot-l {{ left:90px; top:300px; width:420px; height:430px; text-align:center; }}
#ot-r {{ left:570px; top:300px; width:420px; height:430px; text-align:center; background:#FFF4D0; }}
.ot-h {{ font-family:'Gochi Hand',cursive; font-size:58px; margin-top:24px; }}
.ot-b {{ font-size:46px; margin-top:30px; line-height:1.15; }}
.ot-v {{ font-family:'Gochi Hand',cursive; font-size:80px; margin-top:30px; }}
#ot-big {{ position:absolute; left:0; right:0; top:790px; text-align:center; font-size:64px; }}
""", f"""
  <div id="ot-title" class="h1" style="top:150px;font-size:70px">Me vs. <span class="hl">someone else</span></div>
  <div id="ot-l" class="card"><div class="ot-h">My hand</div><div class="ot-b">brain predicted it</div><div class="ot-v blue">meh</div></div>
  <div id="ot-r" class="card"><div class="ot-h">Their hand</div><div id="ot-rb" class="ot-b">no prediction</div><div id="ot-rv" class="ot-v red">HA HA!</div></div>
  <div id="ot-big"><span class="pill red">surprise = tickle</span></div>
""", f"""
rise("#ot-title", 0.0); pop("#ot-l", 0.15); pop("#ot-r", {tse:.2f});
tl.fromTo("#ot-rb", {{opacity:0}}, {{opacity:1, duration:0.2}}, {tcp:.2f});
tl.fromTo("#ot-rv", {{opacity:0, scale:0.5}}, {{opacity:1, scale:1, duration:0.3, ease:"back.out(2.5)"}}, {tsu:.2f});
tl.fromTo("#ot-rv", {{rotation:0}}, {{rotation:6, duration:0.07, yoyo:true, repeat:7}}, {tsu+0.35:.2f});
pop("#ot-big span", {tti:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 8 ROBOT — handle -> robot arm -> palm
s = "robot"; trb = aw(s, "tickle robot"); thd = aw(s, "moved a"); tbs = aw(s, "brushed")
scenes[s] = scene_file(s, f"""
#rb-svg {{ position:absolute; left:80px; top:270px; }}
.rb-l {{ position:absolute; font-family:'Gochi Hand',cursive; font-size:50px; }}
""", f"""
  <div id="rb-title" class="h1" style="top:150px;font-size:72px">The <span class="hl">tickle robot</span></div>
  <svg id="rb-svg" width="920" height="560" viewBox="0 0 920 560" data-layout-ignore>
    <g id="rb-hd"><path d="M60,330 L240,330 L240,380 L60,380 Z" fill="#BFE3F7" {WS.replace('fill="none" ', '')}/><path id="rb-stick" d="M150,330 L150,230" stroke="{K}" stroke-width="10" stroke-linecap="round"/><circle cx="150" cy="222" r="22" fill="{C['red']}" stroke="{K}" stroke-width="5"/></g>
    <path id="rb-wire" d="M240,355 Q330,420 420,340" stroke="{C['pencil']}" stroke-width="5" stroke-dasharray="12 10" fill="none"/>
    <g id="rb-bot"><path d="M410,300 L520,300 L520,400 L410,400 Z" fill="#fff" {WS.replace('fill="none" ', '')}/><circle cx="445" cy="335" r="8" fill="{K}"/><circle cx="485" cy="335" r="8" fill="{K}"/><path d="M445,370 L485,370" {WS}/>
      <g id="rb-arm"><path d="M520,330 L640,250 L700,300" {WS}/><path d="M700,300 L728,340" stroke="{C['blue']}" stroke-width="12" stroke-linecap="round"/></g></g>
    <g id="rb-palm" transform="translate(-10,-45)"><path d="M640,420 Q700,360 800,380 Q880,400 870,460 Q840,520 740,515 Q660,510 640,470 Z" fill="#FFE8D6" {WS.replace('fill="none" ', '')}/><path d="M700,450 Q760,430 820,450" {WS}/></g>
  </svg>
  <div id="rb-lh" class="rb-l" style="left:110px;top:670px">handle</div>
  <div id="rb-lp" class="rb-l" style="left:700px;top:765px">palm</div>
""", f"""
rise("#rb-title", 0.0); pop("#rb-bot", {trb:.2f}); pop("#rb-hd", {thd:.2f}); rise("#rb-lh", {thd+0.2:.2f});
draw("#rb-wire", {thd+0.3:.2f}, 0.4); pop("#rb-palm", {tbs-0.5:.2f}); rise("#rb-lp", {tbs-0.3:.2f});
tl.fromTo("#rb-stick", {{rotation:-15, svgOrigin:"150 330"}}, {{rotation:15, svgOrigin:"150 330", duration:0.3, yoyo:true, repeat:5, ease:"sine.inOut"}}, {thd+0.1:.2f});
tl.fromTo("#rb-arm", {{rotation:-8, svgOrigin:"520 330"}}, {{rotation:8, svgOrigin:"520 330", duration:0.3, yoyo:true, repeat:5, ease:"sine.inOut"}}, {tbs:.2f});
""")

# 9 DELAY — no delay vs < 1/3 s
s = "delay"; tnd = aw(s, "no delay"); tbt = aw(s, "barely tickled"); tld = aw(s, "less than"); tse = aw(s, "someone else")
scenes[s] = scene_file(s, f"""
#dl-big {{ position:absolute; left:0; right:0; top:740px; text-align:center; font-size:60px; }}
""", f"""
  <div id="dl-title" class="h1" style="top:150px;font-size:72px">Add a tiny <span class="hl">delay</span></div>
  {meter('dl-a', 140, 300, 800, 'no delay', C['blue'])}
  {meter('dl-b', 140, 510, 800, 'delay: less than <b class="red">1/3</b> second', C['red'])}
  <div id="dl-big"><span class="pill red">feels like someone else!</span></div>
""", f"""
rise("#dl-title", 0.0); rise("#dl-a", {tnd:.2f});
tl.fromTo("#dl-a-f", {{scaleX:0}}, {{scaleX:0.12, duration:0.4, ease:"power2.out"}}, {tbt:.2f});
rise("#dl-b", {tld:.2f}); tl.fromTo("#dl-b-f", {{scaleX:0}}, {{scaleX:0.9, duration:0.8, ease:"power2.out"}}, {tld+0.5:.2f});
pop("#dl-big span", {tse:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 10 MYSTERY
s = "mystery"; tpz = aw(s, "a puzzle"); targ = aw(s, "argue")
scenes[s] = scene_file(s, f"""
#my-q {{ position:absolute; left:0; right:0; top:300px; text-align:center; font-size:300px; color:{C['blue']}; }}
#my-p {{ position:absolute; left:0; right:0; top:700px; text-align:center; font-size:56px; }}
""", f"""
  <div id="my-title" class="h1" style="top:150px;font-size:70px">Why tickles <span class="hl">exist</span>?</div>
  <div id="my-q" class="big">?</div>
  <div id="my-p"><span class="pill">still debated</span></div>
""", f"""
rise("#my-title", 0.0); pop("#my-q", {tpz:.2f}, {{from:{{rotation:-20}}, to:{{rotation:6}}}});
pop("#my-p span", {targ:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 11 OUTRO
s = "outro"; tsc0 = aw(s, "sees it coming"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:170px; font-size:82px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">Your brain always<br><span class="hl">sees it coming</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
rise("#ou-a", 0.1); tl.fromTo("#ou-a .hl", {{scale:1}}, {{scale:1.08, duration:0.15, yoyo:true, repeat:1}}, {tsc0:.2f});
tl.to("#ou-a", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "skin too"), 3.0)
wave(g("intro", "I'm Max"))
point(g("try", "try it"), 1.2)
think(SC["predict"]["start"] + 0.1, g("predict", "quick guess"))
point(g("cancel", "the cerebellum"), 1.4)
wow(g("other", "a surprise"), 1.4)
point(g("robot", "tickle robot"), 1.2)
wow(g("delay", "someone else"), 1.4)
think(SC["mystery"]["start"] + 0.1, SC["outro"]["start"] - 0.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "tickle yourself"), 0.35), ("pop.mp3", A("guess", "skin too"), 0.5), ("pop.mp3", A("guess", "too brave"), 0.5),
        ("pop.mp3", A("guess", "brain playing"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("try", "nothing right"), 0.6),
        ("pop.mp3", A("predict", "quick guess"), 0.5), ("click.mp3", A("cancel", "way down"), 0.5),
        ("impact-bass-1.mp3", A("other", "a surprise"), 0.45),
        ("ping.mp3", A("delay", "less than"), 0.35), ("pop.mp3", A("delay", "someone else"), 0.55),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
