# MAX WISE ep04 — How long would it take to count to one billion? Executed inside engine/maxwise.py.
# === SCENES ===
WSF = WS.replace('fill="none" ', '')
def watch_svg(pid, w=300):
    return (f'<svg id="{pid}" width="{w}" height="{w*1.07:.0f}" viewBox="0 0 200 215" style="overflow:visible" data-layout-ignore>'
            f'<path d="M86,10 L114,10 M100,10 L100,26" {WS}/>'
            f'<path d="M100,28 Q182,30 184,118 Q182,206 100,208 Q18,206 16,118 Q18,30 100,28 Z" fill="#fff" {WSF}/>'
            + ''.join(f'<path d="M100,{44 if i%3==0 else 50} L100,54" transform="rotate({i*30} 100 118)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(12)) +
            f'<g id="{pid}-hand"><path d="M100,118 L100,52" stroke="{C["red"]}" stroke-width="6" stroke-linecap="round"/></g>'
            f'<circle cx="100" cy="118" r="6" fill="{K}"/></svg>')
def tick_js(pid, t0, n, step=6):
    return (f'tl.set("#{pid}-hand", {{rotation:0, svgOrigin:"100 118"}}, 0);'
            f'for (let k=1;k<={n};k++) tl.to("#{pid}-hand", {{rotation:k*{step}, duration:0.08, ease:"back.out(3)"}}, {t0:.2f}+(k-1)*0.5);')

# 1 HOOK
s = "hook"; tfc = aw(s, "fun challenge"); thl = aw(s, "how long"); tob = aw(s, "one billion")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:260px; font-size:84px; }}
#hk-seq {{ position:absolute; left:0; right:0; top:560px; text-align:center; font-size:66px; color:{C['blue']}; }}
#hk-big {{ position:absolute; left:0; right:0; top:620px; text-align:center; }}
#hk-big span {{ font-size:104px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">How long to count to <span class="hl">one billion</span>?</div>
  <div id="hk-big"><span class="pill">1,000,000,000</span></div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
rise("#hk-q", {thl-0.05:.2f}); pop("#hk-big span", {tob:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); ta = aw(s, "few months"); tb = aw(s, "ten years"); tc = aw(s, "whole lifetime")
notes = [("a", "a few months?", -6, 110, C['hi']), ("b", "10 years?", 4, 400, "#BFE3F7"), ("c", "a whole lifetime?", -3, 690, "#FFC9C2")]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:280px;height:250px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:60px;line-height:1.05;padding:10px">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {ta:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {tb:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {tc:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tlt = aw(s, "let's start")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's start counting!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tlt:.2f});
""")

# 4 RULE — one per second, never stop
s = "rule"; tr = aw(s, "the rules"); t1 = aw(s, "one number"); tns = aw(s, "never stop"); tsl = aw(s, "no sleep"); tsn = aw(s, "no snacks")
scenes[s] = scene_file(s, f"""
#ru-title {{ top:150px; font-size:76px; }}
#ru-w {{ position:absolute; left:120px; top:300px; }}
#ru-r1 {{ position:absolute; left:450px; top:340px; width:560px; text-align:center; font-size:62px; white-space:nowrap; }}
#ru-r2 {{ position:absolute; left:470px; top:450px; width:520px; text-align:center; font-size:60px; color:{C['blue']}; }}
.ru-no {{ position:absolute; left:470px; width:520px; text-align:center; }}
.ru-no span {{ font-size:58px; color:{C['red']}; }}
""", f"""
  <div id="ru-title" class="h1">The <span class="hl">rules</span></div>
  <div id="ru-w">{watch_svg('ru-sw', 300)}</div>
  <div id="ru-r1" class="big">1 number / second</div>
  <div id="ru-r2" class="big">never stop!</div>
  <div id="ru-n1" class="ru-no" style="top:620px"><span class="pill">no sleep</span></div>
  <div id="ru-n2" class="ru-no" style="top:740px"><span class="pill">no snacks</span></div>
""", f"""
rise("#ru-title", {tr-0.2:.2f}); pop("#ru-w", {t1-0.2:.2f}); {tick_js('ru-sw', t1, 12)}
pop("#ru-r1", {t1:.2f}); pop("#ru-r2", {tns:.2f});
pop("#ru-n1 span", {tsl:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}}); pop("#ru-n2 span", {tsn:.2f}, {{from:{{rotation:12}}, to:{{rotation:2}}}});
""")

# 5 DAY — 86,400 seconds
s = "day"; tod = aw(s, "one day"); t86 = aw(s, "eighty six")
scenes[s] = scene_file(s, f"""
#dy-title {{ top:150px; font-size:76px; }}
#dy-sun {{ position:absolute; left:400px; top:270px; }}
#dy-num {{ position:absolute; left:0; right:0; top:560px; text-align:center; font-size:140px; color:{C['red']}; }}
#dy-sub {{ top:720px; font-size:56px; }}
""", f"""
  <div id="dy-title" class="h1">One <span class="hl">day</span></div>
  <svg id="dy-sun" width="280" height="260" viewBox="0 0 140 130" data-layout-ignore>
    <circle cx="70" cy="70" r="34" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>
    {''.join(f'<path d="M70,22 L70,8" transform="rotate({i*45} 70 70)" {WS}/>' for i in range(8))}</svg>
  <div id="dy-num" class="big"><span id="dy-n">0</span></div>
  <div id="dy-sub" class="h2">seconds in one day</div>
""", f"""
rise("#dy-title", 0.0); pop("#dy-sun", {tod:.2f}); tl.fromTo("#dy-sun", {{rotation:0}}, {{rotation:90, duration:3, ease:"none"}}, {tod:.2f});
pop("#dy-num", {tod+0.2:.2f}); count("#dy-n", 0, 86400, {tod+0.3:.2f}, {t86-tod+1.0:.2f}, fmtInt); rise("#dy-sub", {t86+0.6:.2f});
""")

# 6 MILLION — about 11.5 days
s = "million"; tom = aw(s, "one million"); t11 = aw(s, "eleven and"); tnb = aw(s, "not bad")
pages = "".join(f'<div class="ml-pg" id="ml-p{i}" style="left:{560+i*20}px;top:{330+i*16}px;transform:rotate({(-1)**i*3}deg)"></div>' for i in range(12))
scenes[s] = scene_file(s, f"""
#ml-title {{ top:150px; font-size:76px; }}
#ml-goal {{ position:absolute; left:80px; top:330px; width:460px; text-align:center; font-size:90px; color:{C['blue']}; }}
.ml-pg {{ position:absolute; width:150px; height:150px; background:#fff; border:4px solid {K}; {SKETCH} border-top:26px solid {C['red']}; }}
#ml-ans {{ position:absolute; left:0; right:0; top:700px; text-align:center; }}
#ml-ans span {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="ml-title" class="h1">To <span class="hl">one million</span></div>
  <div id="ml-goal" class="big">1,000,000</div>
  {pages}
  <div id="ml-ans"><span class="pill">≈ 11.5 days</span></div>
""", f"""
rise("#ml-title", 0.0); pop("#ml-goal", {tom:.2f});
for (let i=0;i<12;i++) pop("#ml-p"+i, {tom+0.2:.2f}+i*0.1);
pop("#ml-ans span", {t11:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
tl.fromTo("#ml-ans span", {{scale:1}}, {{scale:1.1, duration:0.14, yoyo:true, repeat:1}}, {tnb:.2f});
""")

# 7 THOUSAND — a billion is a thousand millions
s = "thousand"; tbn = aw(s, "one billion"); ttm = aw(s, "thousand millions"); ttl = aw(s, "thousand times")
blocks = "".join(f'<rect x="{120+(i%40)*21}" y="{350+(i//40)*16}" width="17" height="12" fill="{C["blue"] if i == 0 else "#BFE3F7"}" stroke="{K}" stroke-width="2"/>' for i in range(1000))
scenes[s] = scene_file(s, f"""
#th-eq {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-size:76px; line-height:1.15; }}
#th-x {{ position:absolute; left:0; right:0; top:780px; text-align:center; }}
#th-x span {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="th-eq" class="big"><span id="th-a">1 billion</span><br><span id="th-b">= <span class="blue">1,000</span> × 1 million</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="760" data-layout-ignore><g id="th-blk">{blocks}</g></svg>
  <div id="th-x"><span class="pill">1,000 × longer!</span></div>
""", f"""
pop("#th-a", {tbn:.2f}); pop("#th-b", {ttm-0.3:.2f});
tl.fromTo("#th-blk rect", {{opacity:0, scale:0}}, {{opacity:1, scale:1, duration:0.15, stagger:0.0012, transformOrigin:"50% 50%"}}, {ttm:.2f});
pop("#th-x span", {ttl:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 8 YEAR — about 31.5 million seconds
s = "year"; toy = aw(s, "one year"); t31 = aw(s, "thirty one")
scenes[s] = scene_file(s, f"""
#yr-title {{ top:150px; font-size:76px; }}
#yr-num {{ position:absolute; left:0; right:0; top:380px; text-align:center; font-size:120px; color:{C['red']}; }}
#yr-sub {{ top:540px; font-size:56px; }}
#yr-cal {{ position:absolute; left:0; right:0; top:650px; text-align:center; font-size:52px; color:{C['muted']}; }}
""", f"""
  <div id="yr-title" class="h1">One <span class="hl">year</span></div>
  <div id="yr-num" class="big">≈ 31.5 million</div>
  <div id="yr-sub" class="h2">seconds in one year</div>
""", f"""
rise("#yr-title", {toy-0.2:.2f}); pop("#yr-num", {t31:.2f}, {{from:{{scale:1.5}}, to:{{}}}}); rise("#yr-sub", {t31+0.4:.2f});
""")

# 9 ANSWER — almost 32 years
s = "answer"; tob = aw(s, "one billion"); t32 = aw(s, "almost thirty")
X0, X1, Y = 110, 970, 520
ticks = "".join(f'<path d="M{X0+(X1-X0)*y/40:.1f},{Y-(26 if y%10==0 else 14)} L{X0+(X1-X0)*y/40:.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{X0+(X1-X0)*y/40:.1f}" y="{Y+52}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{y}</text>' if y % 10 == 0 else "") for y in range(0, 41, 5))
seg = (X1 - X0) * 31.7 / 40
scenes[s] = scene_file(s, f"""
#an-title {{ top:150px; font-size:76px; }}
#an-bar {{ position:absolute; left:{X0}px; top:{Y-70}px; width:{X1-X0}px; height:60px; border:4px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#an-seg {{ position:absolute; left:0; top:0; height:100%; width:{seg:.1f}px; transform-origin:0 50%; }}
#an-ans {{ position:absolute; left:0; right:0; top:660px; text-align:center; }}
#an-ans span {{ font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="an-title" class="h1">Counting to <span class="hl">1 billion</span></div>
  <div id="an-bar"><div id="an-seg" class="hatch-r"></div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>{ticks}
    <text x="{X1}" y="{Y+100}" text-anchor="end" font-family="Patrick Hand" font-size="36" fill="{C['muted']}">years</text></svg>
  <div id="an-ans"><span class="pill">almost 32 years!</span></div>
""", f"""
rise("#an-title", 0.0); rise("#an-bar", 0.1);
tl.fromTo("#an-seg", {{scaleX:0}}, {{scaleX:1, duration:{t32-0.3:.2f}, ease:"power1.inOut"}}, 0.3);
pop("#an-ans span", {t32:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 10 TWIST — big numbers take seconds to say
s = "twist"; tgn = aw(s, "being generous"); t78 = aw(s, "seven hundred eighty"); tsv = aw(s, "several seconds"); tlr = aw(s, "longer than")
scenes[s] = scene_file(s, f"""
#tw-title {{ top:150px; font-size:76px; }}
#tw-bub {{ position:absolute; left:110px; top:300px; width:860px; height:220px; background:#fff; border:4px solid {K}; {SKETCH} display:flex; align-items:center; justify-content:center; }}
#tw-bub .big {{ font-size:104px; color:{C['blue']}; }}
#tw-tail {{ position:absolute; left:200px; top:510px; }}
#tw-w {{ position:absolute; left:440px; top:560px; }}
#tw-sev {{ position:absolute; left:640px; top:600px; width:360px; text-align:center; font-size:58px; }}
#tw-life {{ position:absolute; left:0; right:0; top:730px; text-align:center; }}
#tw-life span {{ font-size:62px; color:{C['red']}; }}
""", f"""
  <div id="tw-title" class="h1">Being <span class="hl">generous</span>…</div>
  <div id="tw-bub"><div class="big">782,400,000</div></div>
  <svg id="tw-tail" width="120" height="80" data-layout-ignore><path d="M10,4 L40,70 L80,4" fill="#fff" {WSF}/></svg>
  <div id="tw-w">{watch_svg('tw-sw', 180)}</div>
  <div id="tw-sev" class="big">several seconds!</div>
  <div id="tw-life"><span class="pill">longer than your whole life</span></div>
""", f"""
rise("#tw-title", {tgn-0.6:.2f}); pop("#tw-bub", {t78-0.2:.2f}); pop("#tw-tail", {t78-0.1:.2f});
pop("#tw-w", {t78+0.3:.2f}); {tick_js('tw-sw', t78+0.4, 6, 30)}
pop("#tw-sev", {tsv:.2f}); pop("#tw-life span", {tlr:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 11 OUTRO
s = "outro"; ta = aw(s, "almost thirty"); tj = aw(s, "just to"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:84px; }}
#ou-b {{ top:390px; font-size:60px; color:{C['muted']}; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">almost 32 years</span> of counting…</div>
  <div id="ou-b" class="h1">…just to reach one billion.</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {ta:.2f}); rise("#ou-b", {min(tj, ta+1.0):.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "how long"), SC["guess"]["start"] + 0.2)
point(g("guess", "few months"), 2.6)
wave(g("intro", "I'm Max"))
point(g("rule", "one number"), 1.4)
point(g("day", "eighty six"), 1.2)
point(g("million", "eleven and"), 1.2)
wow(g("thousand", "thousand times"), 1.2)
point(g("year", "thirty one"), 1.2)
wow(g("answer", "almost thirty"), 1.8)
think(g("twist", "being generous"), g("twist", "several seconds"))
wow(g("twist", "longer than"), 1.4)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "one billion"), 0.35), ("pop.mp3", A("guess", "few months"), 0.5), ("pop.mp3", A("guess", "ten years"), 0.5),
        ("pop.mp3", A("guess", "whole lifetime"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click-soft.mp3", A("rule", "one number"), 0.6),
        ("pop.mp3", A("million", "eleven and"), 0.55), ("pop.mp3", A("thousand", "thousand times"), 0.55),
        ("impact-bass-1.mp3", A("answer", "almost thirty"), 0.45), ("click.mp3", A("twist", "several seconds"), 0.45),
        ("pop.mp3", A("twist", "longer than"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
