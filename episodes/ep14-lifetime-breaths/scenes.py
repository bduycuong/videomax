# MAX WISE ep14 — How many breaths will you take in your lifetime?  Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; MINT = "#C9E8C2"

def lungs_svg(lid, w):
    return (f'<svg id="{lid}" width="{w}" height="{w*0.9:.0f}" viewBox="0 0 400 360" data-layout-ignore>'
            f'<path d="M200,20 L200,120 M200,120 Q170,140 150,170 M200,120 Q230,140 250,170" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>'
            f'<g class="lg-l"><path d="M180,110 Q90,60 50,170 Q20,290 80,330 Q150,350 175,300 Z" fill="{PINK}" {WSF}/></g>'
            f'<g class="lg-r"><path d="M220,110 Q310,60 350,170 Q380,290 320,330 Q250,350 225,300 Z" fill="{PINK}" {WSF}/></g></svg>')

# 1 HOOK — breathing lungs
s = "hook"; tb = aw(s, "took a breath"); thm = aw(s, "how many"); twl = aw(s, "whole life")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:80px; }}
#hk-lu {{ position:absolute; left:300px; top:470px; }}
#hk-qm {{ position:absolute; left:780px; top:560px; font-size:150px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How many <span class="hl">breaths</span><br>in your whole life?</div>
  <div id="hk-lu">{lungs_svg('hk-l', 480)}</div>
  <div id="hk-qm" class="big">?</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#hk-lu", {tb:.2f});
tl.fromTo("#hk-l .lg-l, #hk-l .lg-r", {{scale:1}}, {{scale:1.08, transformOrigin:"50% 30%", duration:0.8, yoyo:true, repeat:5, ease:"sine.inOut"}}, {tb+0.2:.2f});
rise("#hk-q", {thm-0.2:.2f});
pop("#hk-qm", {twl:.2f}, {{from:{{rotation:30}}, to:{{rotation:8}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); t1 = aw(s, "A million"); t2 = aw(s, "A hundred million"); t3 = aw(s, "half a billion")
notes = [("a", "1 million?", -6, 110, C['hi']), ("b", "100 million?", 4, 405, SKY), ("c", "500 million +?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:50px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "count every")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count every breath!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tct:.2f});
""")

# 4 RATE — stopwatch + 15 breath bubbles
s = "rate"; tsit = aw(s, "sit still"); t15 = aw(s, "fifteen times"); tin = aw(s, "In, and")
bub = "".join(f'<circle class="rt-b" cx="{560 + (k%5)*95}" cy="{420 + (k//5)*110}" r="38" fill="{SKY}" stroke="{K}" stroke-width="4" style="opacity:0"/>' for k in range(15))
scenes[s] = scene_file(s, f"""
#rt-lab {{ position:absolute; left:0; right:0; top:150px; text-align:center; font-size:84px; }}
#rt-io {{ position:absolute; left:520px; top:780px; width:520px; text-align:center; font-size:60px; color:{C['blue']}; }}
""", f"""
  <div id="rt-lab" class="big"><span class="red">15</span> breaths / minute</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <circle id="rt-w" cx="270" cy="530" r="190" fill="#fff" stroke="{K}" stroke-width="7"/>
    <rect x="245" y="310" width="50" height="34" fill="{K}"/>
    <path id="rt-h" d="M270,530 L270,380" stroke="{C['red']}" stroke-width="8" stroke-linecap="round"/>
    <text x="270" y="650" text-anchor="middle" font-family="Gochi Hand" font-size="44" fill="{K}">1 min</text>
    {bub}</svg>
  <div id="rt-io" class="big">in… out…</div>
""", f"""
pop("#rt-w", {tsit:.2f}); tl.fromTo("#rt-h", {{rotation:0}}, {{rotation:360, svgOrigin:"270 530", duration:3.0, ease:"none"}}, {t15-0.3:.2f});
rise("#rt-lab", {t15:.2f});
tl.fromTo(".rt-b", {{opacity:0, scale:0.3, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.2, stagger:0.18, ease:"back.out(2)"}}, {t15:.2f});
rise("#rt-io", {tin:.2f});
""")

# 5 HOUR — 30 x 30 dot grid = 900
s = "hour"; tsx = aw(s, "Sixty minutes"); t900 = aw(s, "nine hundred")
dots = "".join(f'<circle class="hr-d" cx="{300 + (k%30)*17}" cy="{340 + (k//30)*17}" r="6" fill="{C["blue"]}" style="opacity:0"/>' for k in range(900))
scenes[s] = scene_file(s, f"""
#hr-m {{ position:absolute; left:0; right:0; top:160px; text-align:center; font-size:84px; }}
#hr-r {{ position:absolute; left:0; right:0; top:880px; text-align:center; font-size:60px; }}
""", f"""
  <div id="hr-m" class="big">15 × 60 = <span class="red">900</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{dots}</svg>
  <div id="hr-r" class="big" style="opacity:0"><span class="hl">every hour</span></div>
""", f"""
rise("#hr-m", {tsx:.2f});
tl.to(".hr-d", {{opacity:1, duration:0.02, stagger:{{each:0.0022, from:"start"}}}}, {tsx+0.2:.2f});
pop("#hr-r", {t900:.2f});
""")

# 6 DAY — sun / moon and a counter to 21,600
s = "day"; tday = aw(s, "all day"); tsl = aw(s, "you sleep"); t216 = aw(s, "twenty one thousand")
scenes[s] = scene_file(s, f"""
#dy-c {{ position:absolute; left:0; right:0; top:560px; text-align:center; }}
#dy-c .big {{ font-size:140px; color:{C['red']}; }}
#dy-u {{ position:absolute; left:0; right:0; top:740px; text-align:center; font-size:60px; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="560" data-layout-ignore>
    <g id="dy-sun"><circle cx="540" cy="330" r="110" fill="{C['hi']}" stroke="{K}" stroke-width="6"/>
      {"".join(f'<path d="M{540+150*__import__("math").cos(a/8*6.283):.0f},{330+150*__import__("math").sin(a/8*6.283):.0f} L{540+190*__import__("math").cos(a/8*6.283):.0f},{330+190*__import__("math").sin(a/8*6.283):.0f}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>' for a in range(8))}</g>
    <g id="dy-moon" style="opacity:0"><path d="M600,210 A130,130 0 1,0 640,440 A100,100 0 1,1 600,210 Z" fill="#E7E9F2" stroke="{K}" stroke-width="6"/>
      </g></svg>
  <div id="dy-c"><span class="big" id="dy-n">900</span></div>
  <div id="dy-u" class="big" style="opacity:0">breaths <span class="hl">a day</span></div>
""", f"""
pop("#dy-sun", {tday:.2f}); rise("#dy-c", {tday:.2f});
tl.to("#dy-sun", {{opacity:0, duration:0.3}}, {tsl-0.2:.2f}); tl.to("#dy-moon", {{opacity:1, duration:0.3}}, {tsl-0.2:.2f});
count("#dy-n", 900, 21600, {tday+0.2:.2f}, {t216-tday-0.1:.2f}, fmtInt);
rise("#dy-u", {t216:.2f});
""")

# 7 YEAR — calendar + counter to almost 8 million
s = "year"; toy = aw(s, "One year"); t8 = aw(s, "eight million")
scenes[s] = scene_file(s, f"""
#yr-cal {{ position:absolute; left:340px; top:170px; width:400px; height:340px; background:#fff; border:5px solid {K}; {SKETCH} }}
#yr-cal .top {{ height:90px; background:{C['red']}; border-bottom:5px solid {K}; color:#fff; font-family:'Gochi Hand',cursive; font-size:60px; text-align:center; line-height:90px; }}
#yr-cal .mid {{ font-family:'Gochi Hand',cursive; font-size:120px; text-align:center; line-height:240px; }}
#yr-c {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#yr-c .big {{ font-size:110px; color:{C['blue']}; }}
""", f"""
  <div id="yr-cal"><div class="top">1 YEAR</div><div class="mid">365</div></div>
  <div id="yr-c"><span class="big">almost <span class="red">8 million</span></span></div>
""", f"""
pop("#yr-cal", {toy:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
pop("#yr-c", {t8:.2f});
""")

# 8 LIFE — 80-year bar fills, total 630 million
s = "life"; t80 = aw(s, "eighty years"); t630 = aw(s, "six hundred thirty million")
scenes[s] = scene_file(s, f"""
#lf-lab {{ position:absolute; left:0; right:0; top:160px; text-align:center; font-size:76px; }}
#lf-bar {{ position:absolute; left:120px; top:340px; width:840px; height:110px; border:5px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-fill {{ width:100%; height:100%; background:{MINT}; transform-origin:0 50%; }}
#lf-0 {{ position:absolute; left:110px; top:470px; font-size:44px; }}
#lf-80 {{ position:absolute; left:860px; top:470px; font-size:44px; }}
#lf-c {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#lf-c .big {{ font-size:120px; color:{C['red']}; }}
""", f"""
  <div id="lf-lab" class="big"><span class="hl">80 years</span> of breathing</div>
  <div id="lf-bar"><div id="lf-fill"></div></div>
  <div id="lf-0" class="big">age 0</div><div id="lf-80" class="big">age 80</div>
  <div id="lf-c"><span class="big">≈ 630 million!</span></div>
""", f"""
rise("#lf-lab", {t80-0.3:.2f}); pop("#lf-bar", {t80-0.3:.2f}); rise("#lf-0", {t80:.2f}); rise("#lf-80", {t80:.2f});
tl.fromTo("#lf-fill", {{scaleX:0}}, {{scaleX:1, duration:{t630-t80:.2f}, ease:"power1.inOut"}}, {t80:.2f});
pop("#lf-c", {t630:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.fromTo("#lf-c", {{scale:1}}, {{scale:1.08, duration:0.14, yoyo:true, repeat:1}}, {t630+0.6:.2f});
""")

# 9 RANGE — honest error bar
s = "range"; tdf = aw(s, "everyone is different"); t12 = aw(s, "twelve to twenty"); t5 = aw(s, "five hundred"); t8b = aw(s, "eight hundred")
scenes[s] = scene_file(s, f"""
#rg-t {{ top:160px; font-size:76px; }}
#rg-l {{ position:absolute; left:80px; top:560px; width:320px; text-align:center; }}
#rg-r {{ position:absolute; left:660px; top:560px; width:340px; text-align:center; }}
#rg-l .big, #rg-r .big {{ font-size:72px; color:{C['blue']}; }}
#rg-l .s, #rg-r .s {{ font-size:42px; font-family:'Gochi Hand',cursive; }}
""", f"""
  <div id="rg-t" class="h1">Everyone is <span class="hl">different</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <rect id="rg-band" x="240" y="420" width="600" height="70" fill="{C['hi']}" opacity=".7" style="opacity:0"/>
    <path id="rg-bar" d="M240,455 L840,455 M240,415 L240,495 M840,415 L840,495" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <circle id="rg-me" cx="460" cy="455" r="16" fill="{C['red']}" stroke="{K}" stroke-width="4" style="opacity:0"/></svg>
  <div id="rg-l" style="opacity:0"><div class="big">500 million</div><div class="s">12 a minute</div></div>
  <div id="rg-r" style="opacity:0"><div class="big">800+ million</div><div class="s">20 a minute</div></div>
""", f"""
rise("#rg-t", {tdf-0.4:.2f}); draw("#rg-bar", {t12:.2f}, 0.6);
tl.to("#rg-band", {{opacity:0.7, duration:0.3}}, {t12+0.5:.2f});
pop("#rg-l", {t5:.2f}); pop("#rg-r", {t8b:.2f}); pop("#rg-me", {t8b+0.8:.2f});
""")

# 10 AUTO — brain with brain stem, AUTOPILOT tape
s = "auto"; tw = aw(s, "wild part"); tnt = aw(s, "never think"); tbs = aw(s, "brain stem"); tap = aw(s, "autopilot")
scenes[s] = scene_file(s, f"""
#au-q {{ top:150px; font-size:76px; }}
#au-tape {{ position:absolute; left:600px; top:690px; transform:rotate(-6deg); }}
#au-tape .chip {{ font-size:56px; }}
#au-z {{ position:absolute; left:120px; top:300px; font-size:64px; color:{C['blue']}; }}
""", f"""
  <div id="au-q" class="h1">You <span class="hl">never</span> think about it</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <g id="au-br"><path d="M340,520 Q300,360 450,320 Q520,260 620,300 Q760,300 760,430 Q790,540 680,570 Q600,600 520,580 Q400,600 340,520 Z" fill="{PINK}" {WSF}/>
      <path d="M420,420 Q470,380 520,430 Q570,380 620,430 M450,500 Q520,470 600,510" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/></g>
    <path id="au-st" d="M560,585 Q575,650 560,740" stroke="{C['red']}" stroke-width="34" fill="none" stroke-linecap="round" style="opacity:0"/>
    <path id="au-ld" d="M590,690 L640,720" stroke="{K}" stroke-width="4"/></svg>
  <div id="au-tape" style="opacity:0"><span class="chip">AUTOPILOT</span></div>
  <div id="au-z" class="big" style="opacity:0">in… out…</div>
""", f"""
pop("#au-br", {tw:.2f}); rise("#au-q", {tnt-0.2:.2f}); rise("#au-z", {tnt+0.6:.2f});
tl.to("#au-st", {{opacity:1, duration:0.3}}, {tbs:.2f}); draw("#au-ld", {tbs+0.2:.2f}, 0.3);
pop("#au-tape", {tap:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
""")

# 11 OUTRO
s = "outro"; t6 = aw(s, "six hundred million"); tfm = aw(s, "few more"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:80px; }}
#ou-b {{ top:300px; font-size:64px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">600+ million</span> breaths</div>
  <div id="ou-b" class="h1">…and you just took <span class="red">a few more</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {t6:.2f}); rise("#ou-b", {tfm-0.3:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "how many"), SC["guess"]["start"] + 0.2)
point(g("guess", "A million"), 3.0)
wave(g("intro", "I'm Max"))
point(g("rate", "fifteen times"), 1.4)
point(g("hour", "nine hundred"), 1.2)
wow(g("day", "twenty one thousand"), 1.3)
point(g("year", "eight million"), 1.2)
wow(g("life", "six hundred thirty million"), 1.4)
point(g("range", "five hundred"), 1.2)
think(g("auto", "wild part"), g("auto", "never think"))
point(g("auto", "autopilot"), 1.2)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "how many"), 0.35), ("pop.mp3", A("guess", "A million"), 0.5), ("pop.mp3", A("guess", "A hundred million"), 0.5),
        ("pop.mp3", A("guess", "half a billion"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("rate", "fifteen times"), 0.5),
        ("pop.mp3", A("hour", "nine hundred"), 0.5), ("impact-bass-1.mp3", A("day", "twenty one thousand"), 0.4), ("click.mp3", A("year", "eight million"), 0.45),
        ("impact-bass-2.mp3", A("life", "six hundred thirty million"), 0.4), ("click-soft.mp3", A("range", "eight hundred"), 0.5),
        ("pop.mp3", A("auto", "autopilot"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
