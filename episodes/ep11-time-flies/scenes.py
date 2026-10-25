# MAX WISE ep11 — Why does time fly faster the older you get?  Executed inside engine/maxwise.py.
# === SCENES ===
import math
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; MINT = "#CDEBC5"

# 1 HOOK — long summer vs vanishing year
s = "hook"; tsu = aw(s, "summer"); tkid = aw(s, "a kid"); tyr = aw(s, "a whole year"); tbl = aw(s, "in a blink")
rays = "".join(f'<path d="M{60+52*math.cos(math.radians(a)):.0f},{60+52*math.sin(math.radians(a)):.0f} L{60+74*math.cos(math.radians(a)):.0f},{60+74*math.sin(math.radians(a)):.0f}" stroke="{C["red"]}" stroke-width="5" stroke-linecap="round"/>' for a in range(0, 360, 45))
pages = "".join(f'<div id="hk-pg{k}" class="abs" style="left:0;top:0;width:220px;height:220px;background:#fff;border:4px solid {K};border-radius:10px;text-align:center;font-family:Gochi Hand,cursive"><div style="background:{C["red"]};color:#fff;font-size:34px;border-bottom:4px solid {K}">{m}</div><div style="font-size:110px;line-height:150px">{d}</div></div>'
                for k, (m, d) in enumerate([("DEC", 31), ("NOV", 30), ("SEP", 30), ("JUN", 30), ("MAR", 31), ("JAN", 1)]))
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:80px; }}
#hk-sun {{ position:absolute; left:110px; top:480px; }}
#hk-rib {{ position:absolute; left:110px; top:640px; width:420px; height:70px; border:4px solid {K}; {SKETCH} background:{C['hi']}; font-family:'Gochi Hand',cursive; font-size:44px; line-height:62px; text-align:center; transform-origin:0 50%; }}
#hk-cal {{ position:absolute; left:680px; top:470px; width:220px; height:220px; }}
#hk-wh {{ position:absolute; left:600px; top:730px; width:400px; text-align:center; font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="hk-tag"><span class="chip">MAX WISE</span></div>
  <div id="hk-q" class="h1">Why does time <span class="hl">fly faster</span><br>as you get older?</div>
  <svg id="hk-sun" width="140" height="140" viewBox="-10 -10 140 140" data-layout-ignore><circle cx="60" cy="60" r="40" fill="{C['hi']}" {WSF}/>{rays}</svg>
  <div id="hk-rib">summer, age 8 . . . . . .</div>
  <div id="hk-cal">{pages}</div>
  <div id="hk-wh" class="big">WHOOSH!</div>
""", f"""
pop("#hk-tag .chip", 0.0, {{from:{{rotation:-8}}, to:{{rotation:-2}}}}); rise("#hk-q", 0.1);
pop("#hk-sun", {tsu:.2f}); tl.fromTo("#hk-rib", {{opacity:0, scaleX:0.1}}, {{opacity:1, scaleX:1, duration:1.4, ease:"power1.out"}}, {tsu+0.1:.2f});
pop("#hk-cal", {tyr:.2f});
for (let k=0;k<5;k++) tl.to("#hk-pg"+k, {{x:300 - k*40, y:-260 + k*30, rotation:40 + k*12, opacity:0, duration:0.35, ease:"power2.in"}}, {tbl-0.5:.2f}+k*0.12);
pop("#hk-wh", {tbl:.2f}, {{from:{{rotation:-14}}, to:{{rotation:-4}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "take a guess"); tage = aw(s, "your age"); tmem = aw(s, "fewer new memories"); tbus = aw(s, "just being busy")
notes = [("age", "Age?", -6, 110, C['hi']), ("mem", "<span style='font-size:44px'>Fewer new<br>memories?</span>", 4, 405, SKY), ("bus", "Just<br>busy?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:56px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-age", {tage:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-mem", {tmem:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-bus", {tbus:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tdb = aw(s, "still debating"); tcl = aw(s, "the clues")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
#in-tag {{ position:absolute; left:0; right:0; top:500px; text-align:center; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's look at the clues!</span></div>
  <div id="in-tag"><span class="pill red" style="font-size:46px">still debated</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
pop("#in-tag .pill", {tdb:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}}); rise("#in-sub", {tcl-0.3:.2f});
""")

# 4 RATIO — 1/5 vs 1/50
s = "ratio"; tc1 = aw(s, "clue one"); t5 = aw(s, "you're five"); tf = aw(s, "a fifth"); t50 = aw(s, "at fifty"); t150 = aw(s, "one fiftieth")
BX, BW = 110, 860
b5 = "".join(f'<div class="abs" style="left:{BX + k*BW/5 + 4:.0f}px;top:330px;width:{BW/5 - 8:.0f}px;height:110px;border:4px solid {K};border-radius:10px 14px 8px 12px;background:{C["hi"] if k==4 else "#fff"}"></div>' for k in range(5))
b50 = "".join(f'<div class="abs" style="left:{BX + k*BW/50 + 1:.1f}px;top:620px;width:{BW/50 - 3:.1f}px;height:110px;border:2px solid {K};border-radius:3px;background:{C["hi"] if k==49 else "#fff"}"></div>' for k in range(50))
scenes[s] = scene_file(s, f"""
#ra-title {{ top:150px; font-size:72px; }}
#ra-l5 {{ position:absolute; left:110px; top:262px; font-size:50px; }}
#ra-l50 {{ position:absolute; left:110px; top:552px; font-size:50px; }}
#ra-f5 {{ position:absolute; left:370px; top:455px; width:600px; white-space:nowrap; text-align:right; font-size:96px; color:{C['red']}; }}
#ra-f50 {{ position:absolute; left:370px; top:745px; width:600px; white-space:nowrap; text-align:right; font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="ra-title" class="h1">Clue 1: <span class="hl">proportion</span></div>
  <div id="ra-l5" class="big">age 5 &nbsp;<span style="font-size:36px;color:{C['muted']}">(1 box = 1 year)</span></div>
  <div id="ra-g5">{b5}</div>
  <div id="ra-f5" class="big">1 year = 1/5</div>
  <div id="ra-l50" class="big">age 50</div>
  <div id="ra-g50">{b50}</div>
  <div id="ra-f50" class="big">1 year = 1/50</div>
""", f"""
rise("#ra-title", {tc1:.2f}); rise("#ra-l5", {t5-0.2:.2f}); rise("#ra-g5", {t5:.2f}); pop("#ra-f5", {tf:.2f});
rise("#ra-l50", {t50-0.2:.2f}); tl.fromTo("#ra-g50", {{opacity:0, scaleX:0.2, transformOrigin:"110px 50%"}}, {{opacity:1, scaleX:1, duration:0.5, ease:"power2.out"}}, {t50:.2f});
pop("#ra-f50", {t150:.2f});
""")

# 5 FIRSTS — taped photo cards
s = "firsts"; tc2 = aw(s, "clue two"); tbk = aw(s, "first bike"); tsc = aw(s, "first school"); tsn = aw(s, "first snow"); tlb = aw(s, "looking back")
bike = f'<circle cx="45" cy="95" r="30" {WS}/><circle cx="155" cy="95" r="30" {WS}/><path d="M45,95 L85,50 L135,50 L155,95 M85,50 L100,95 L135,50 M75,40 L95,40 M135,50 L130,32 L145,30" {WS}/>'
school = f'<path d="M30,120 L30,60 L100,22 L170,60 L170,120 Z" fill="{PINK}" {WSF}/><rect x="85" y="80" width="30" height="40" fill="#fff" stroke="{K}" stroke-width="4"/><path d="M100,22 L100,4 L122,10 L100,16" stroke="{C["red"]}" stroke-width="4" fill="{C["red"]}"/>'
snow = "".join(f'<path d="M100,70 L{100+55*math.cos(math.radians(a)):.0f},{70+55*math.sin(math.radians(a)):.0f}" stroke="{C["blue"]}" stroke-width="6" stroke-linecap="round"/>' for a in range(0, 360, 60)) + f'<circle cx="100" cy="70" r="10" fill="{SKY}" stroke="{C["blue"]}" stroke-width="4"/>'
cards = [("bk", "1st bike", bike, 90, 280, -5, C['hi']), ("sc", "1st school", school, 400, 330, 3, SKY), ("sn", "1st snow", snow, 710, 280, -3, PINK)]
ch = "".join(f'<div id="fs-{k}" class="abs" style="left:{x}px;top:{y}px;width:270px;height:300px;background:#fff;border:4px solid {K};border-radius:6px;transform:rotate({r}deg);opacity:0">'
             f'<div style="position:absolute;left:85px;top:-18px;width:100px;height:34px;background:{tape};opacity:0.85;transform:rotate(-4deg)"></div>'
             f'<svg style="position:absolute;left:35px;top:40px" width="200" height="140" viewBox="0 0 200 140">{pic}</svg>'
             f'<div style="position:absolute;left:0;right:0;top:200px;text-align:center;font-family:Gochi Hand,cursive;font-size:50px">{lab}</div></div>' for k, lab, pic, x, y, r, tape in cards)
scenes[s] = scene_file(s, f"""
#fs-title {{ top:150px; font-size:72px; }}
#fs-lab {{ position:absolute; left:400px; top:720px; width:600px; text-align:center; font-size:58px; }}
""", f"""
  <div id="fs-title" class="h1">Clue 2: <span class="hl">firsts</span></div>
  {ch}
  <div id="fs-lab" class="big">new memories =<br><span class="red">long years</span></div>
""", f"""
rise("#fs-title", {tc2:.2f});
pop("#fs-bk", {tbk:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-5}}}}); pop("#fs-sc", {tsc:.2f}, {{from:{{rotation:16}}, to:{{rotation:3}}}}); pop("#fs-sn", {tsn:.2f}, {{from:{{rotation:-16}}, to:{{rotation:-3}}}});
pop("#fs-lab", {tlb:.2f});
""")

# 6 BLUR — identical days collapse into one
s = "blur"; tsd = aw(s, "same days"); tbo = aw(s, "blur into one")
days = "".join(f'<div id="bl-d{k}" class="abs" style="left:{110 + k*118}px;top:360px;width:170px;height:230px;background:#fff;border:4px solid {K};{SKETCH}text-align:center;font-family:Patrick Hand;font-size:34px;line-height:1.25;padding-top:20px;box-sizing:border-box;opacity:0">wake<br>work<br>eat<br>sleep</div>' for k in range(7))
scenes[s] = scene_file(s, f"""
#bl-title {{ top:160px; font-size:72px; }}
#bl-q {{ position:absolute; left:400px; top:690px; width:600px; text-align:center; font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="bl-title" class="h1">Same day, <span class="hl">again</span></div>
  {days}
  <div id="bl-q" class="big">a whole month?</div>
""", f"""
rise("#bl-title", 0.0);
for (let k=0;k<7;k++) tl.fromTo("#bl-d"+k, {{opacity:0, y:40}}, {{opacity:1, y:0, duration:0.22, ease:"back.out(1.6)"}}, {tsd-0.3:.2f}+k*0.1);
for (let k=0;k<7;k++) tl.to("#bl-d"+k, {{x:(3-k)*118, filter:"blur(3px)", duration:0.5, ease:"power2.inOut"}}, {tbo:.2f});
pop("#bl-q", {tbo+0.4:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 7 SURVEY — 499 people, last 10 years vs 1 week
s = "survey"; tc3 = aw(s, "clue three"); t499 = aw(s, "four hundred"); t14 = aw(s, "fourteen to"); t10y = aw(s, "last ten years"); twk = aw(s, "single week"); tsame = aw(s, "about the same")
ages = ["teen", "20s", "30s", "40s", "50s", "60s+"]
dec = [0.40, 0.52, 0.64, 0.76, 0.86, 0.86]
def chart(pid, vals, col, x0):
    bars = "".join(f'<rect id="{pid}-b{k}" x="{x0 + k*62}" y="{300 - v*220:.0f}" width="46" height="{v*220:.0f}" rx="6" fill="{col}" stroke="{K}" stroke-width="3"/>'
                   f'<text x="{x0 + k*62 + 23}" y="336" text-anchor="middle" font-family="Patrick Hand" font-size="26" fill="{K}">{ages[k]}</text>' for k, v in enumerate(vals))
    return bars + f'<path d="M{x0-12},300 L{x0 + 6*62},300" {WS}/>'
scenes[s] = scene_file(s, f"""
#sv-title {{ top:150px; font-size:72px; }}
#sv-tag {{ position:absolute; left:0; right:0; top:260px; text-align:center; font-size:50px; }}
#sv-ch {{ position:absolute; left:40px; top:390px; }}
#sv-l1 {{ position:absolute; left:60px; top:370px; width:440px; text-align:center; font-size:44px; }}
#sv-l2 {{ position:absolute; left:560px; top:370px; width:440px; text-align:center; font-size:44px; }}
#sv-s1 {{ position:absolute; left:60px; top:780px; width:440px; text-align:center; font-size:56px; color:{C['red']}; }}
#sv-s2 {{ position:absolute; left:560px; top:780px; width:440px; text-align:center; font-size:56px; color:{C['blue']}; }}
""", f"""
  <div id="sv-title" class="h1">Clue 3: <span class="hl">a survey</span></div>
  <div id="sv-tag"><span id="sv-n" class="pill">499 people</span> <span id="sv-a" class="pill">ages 14–94</span></div>
  <div id="sv-l1" class="big">last 10 years</div><div id="sv-l2" class="big">one week</div>
  <svg id="sv-ch" width="1000" height="360" viewBox="0 0 1000 360" data-layout-ignore>
    <g id="sv-c1">{chart("sv-x", dec, PINK, 60)}</g><g id="sv-c2">{chart("sv-y", [0.5]*6, SKY, 560)}</g></svg>
  <div id="sv-s1" class="big">faster with age</div><div id="sv-s2" class="big">about the same</div>
""", f"""
rise("#sv-title", {tc3:.2f}); pop("#sv-n", {t499:.2f}); pop("#sv-a", {t14:.2f});
rise("#sv-l1", {t10y-0.2:.2f});
for (let k=0;k<6;k++) tl.fromTo("#sv-x-b"+k, {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:0.3, ease:"back.out(1.6)"}}, {t10y:.2f}+k*0.12);
tl.fromTo("#sv-c1 text", {{opacity:0}}, {{opacity:1, duration:0.2}}, {t10y:.2f}); pop("#sv-s1", {t10y+1.0:.2f});
rise("#sv-l2", {twk-0.2:.2f}); tl.fromTo("#sv-c2 text", {{opacity:0}}, {{opacity:1, duration:0.2}}, {twk:.2f});
for (let k=0;k<6;k++) tl.fromTo("#sv-y-b"+k, {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:0.3, ease:"back.out(1.6)"}}, {twk:.2f}+k*0.1);
pop("#sv-s2", {tsame:.2f});
""")

# 8 PRESSURE — clock speeds up as to-dos pile
s = "pressure"; ttp = aw(s, "time pressure"); tbz = aw(s, "the busier"); tfl = aw(s, "seemed to fly")
todo = ["email!", "bills", "meeting", "laundry", "call back", "deadline!"]
notes_p = "".join(f'<div id="pr-n{k}" class="abs" style="left:{560 + (k%2)*200}px;top:{300 + (k//2)*150}px;width:180px;height:120px;background:{[C["hi"], PINK, SKY][k%3]};border:3px solid {K};transform:rotate({[-6,4,-3,7,-5,3][k]}deg);font-family:Gochi Hand,cursive;font-size:40px;line-height:120px;text-align:center;opacity:0">{t}</div>' for k, t in enumerate(todo))
scenes[s] = scene_file(s, f"""
#pr-title {{ top:150px; font-size:70px; }}
#pr-clk {{ position:absolute; left:100px; top:320px; }}
#pr-tick {{ position:absolute; left:80px; top:740px; width:440px; text-align:center; font-size:72px; color:{C['red']}; }}
""", f"""
  <div id="pr-title" class="h1">Strongest clue: <span class="hl">busy!</span></div>
  <svg id="pr-clk" width="400" height="400" viewBox="0 0 200 200" data-layout-ignore>
    <circle cx="100" cy="100" r="88" fill="#fff" {WSF}/>
    {''.join(f'<path d="M100,{18 if i%3==0 else 24} L100,32" transform="rotate({i*30} 100 100)" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for i in range(12))}
    <g id="pr-hh"><path d="M100,100 L100,58" stroke="{K}" stroke-width="7" stroke-linecap="round"/></g>
    <g id="pr-mh"><path d="M100,100 L100,30" stroke="{C['red']}" stroke-width="5" stroke-linecap="round"/></g>
    <circle cx="100" cy="100" r="6" fill="{K}"/></svg>
  {notes_p}
  <div id="pr-tick" class="big">TICK TICK!</div>
""", f"""
rise("#pr-title", {ttp-0.3:.2f}); pop("#pr-clk", {ttp:.2f});
tl.set("#pr-mh", {{rotation:0, svgOrigin:"100 100"}}, 0); tl.set("#pr-hh", {{rotation:0, svgOrigin:"100 100"}}, 0);
tl.to("#pr-mh", {{rotation:360, duration:{max(0.3, tbz-ttp-0.05):.2f}, ease:"none"}}, {ttp:.2f});
tl.to("#pr-mh", {{rotation:360*7, duration:3.0, ease:"power2.in"}}, {tbz:.2f}); tl.to("#pr-hh", {{rotation:200, duration:3.0, ease:"power2.in"}}, {tbz:.2f});
for (let k=0;k<6;k++) tl.fromTo("#pr-n"+k, {{opacity:0, scale:0.4, y:-60}}, {{opacity:1, scale:1, y:0, duration:0.25, ease:"back.out(2)"}}, {tbz:.2f}+k*0.35);
pop("#pr-tick", {tfl:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-4}}}});
""")

# 9 TIP — a year full of new things
s = "tip"; ttr = aw(s, "a trick"); tnew = aw(s, "new things"); tlg = aw(s, "feel longer")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
mg = "".join(f'<div class="abs" style="left:{110 + (k%4)*220}px;top:{270 + (k//4)*170}px;width:200px;height:150px;background:#fff;border:4px solid {K};{SKETCH}font-family:Gochi Hand,cursive;font-size:44px;text-align:center;padding-top:10px;box-sizing:border-box">{m}'
             f'<div id="tp-s{k}" style="margin:6px auto 0;width:110px;font-size:34px;background:{[C["hi"], PINK, SKY, MINT][k%4]};border:3px solid {K};border-radius:20px;opacity:0">NEW!</div></div>' for k, m in enumerate(months))
scenes[s] = scene_file(s, f"""
#tp-title {{ top:150px; font-size:72px; }}
#tp-lab {{ position:absolute; left:400px; top:810px; width:600px; text-align:center; font-size:62px; }}
""", f"""
  <div id="tp-title" class="h1">Trick: <span class="hl">collect firsts</span></div>
  <div id="tp-grid">{mg}</div>
  <div id="tp-lab" class="big">→ a <span class="red">longer</span> year to look back on</div>
""", f"""
rise("#tp-title", {ttr:.2f}); rise("#tp-grid", {ttr+0.2:.2f});
for (let k=0;k<12;k++) pop("#tp-s"+k, {tnew:.2f}+k*0.12, {{from:{{rotation:-30}}, to:{{rotation:-6}}}});
pop("#tp-lab", {tlg-0.2:.2f});
""")

# 10 OUTRO
s = "outro"; tsp = aw(s, "speeding up"); tfc = aw(s, "funny clock"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:78px; }}
#ou-b {{ top:390px; font-size:72px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1">Time isn't <span class="hl">speeding up</span>…</div>
  <div id="ou-b" class="h1">your brain is a <span class="red">funny clock!</span></div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tsp-0.4:.2f}); pop("#ou-b", {tfc-0.3:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "remember"), SC["guess"]["start"] + 0.2)
point(g("guess", "your age"), 2.6)
wave(g("intro", "I'm Max"))
think(g("intro", "still debating"), g("intro", "the clues"))
point(g("ratio", "a fifth"), 1.2)
wow(g("ratio", "one fiftieth"), 1.2)
point(g("firsts", "first bike"), 2.0)
think(g("blur", "same days"), g("blur", "blur into one") + 0.6)
point(g("survey", "last ten years"), 1.6)
wow(g("survey", "about the same"), 1.2)
wow(g("pressure", "seemed to fly"), 1.4)
point(g("tip", "new things"), 1.6)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "in a blink") - 0.2, 0.45), ("pop.mp3", A("guess", "your age"), 0.5), ("pop.mp3", A("guess", "fewer new memories"), 0.5),
        ("pop.mp3", A("guess", "just being busy"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("ping.mp3", A("ratio", "one fiftieth"), 0.4),
        ("click-soft.mp3", A("firsts", "first bike"), 0.6), ("click-soft.mp3", A("firsts", "first school"), 0.6), ("click-soft.mp3", A("firsts", "first snow"), 0.6),
        ("pop.mp3", A("survey", "four hundred"), 0.5), ("click.mp3", A("pressure", "the busier"), 0.4), ("impact-bass-1.mp3", A("pressure", "seemed to fly"), 0.4),
        ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
