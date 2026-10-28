# MAX WISE ep16 — How many years of your life do you spend eating?  Executed inside engine/maxwise.py.
# === SCENES ===
import math
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; MINT = "#C9E8C2"; CREAM = "#FFF4D6"

def plate_svg(pid, cx, cy, r):
    return (f'<g id="{pid}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" {WSF}/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.68:.0f}" fill="{CREAM}" stroke="{K}" stroke-width="4" stroke-dasharray="10 8"/>'
            f'<path d="M{cx-r-40},{cy-r*0.7:.0f} L{cx-r-40},{cy+r*0.9:.0f} M{cx-r-55},{cy-r*0.7:.0f} L{cx-r-55},{cy-r*0.25:.0f} M{cx-r-25},{cy-r*0.7:.0f} L{cx-r-25},{cy-r*0.25:.0f} M{cx-r-55},{cy-r*0.25:.0f} Q{cx-r-40},{cy-r*0.1:.0f} {cx-r-25},{cy-r*0.25:.0f}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M{cx+r+40},{cy-r*0.7:.0f} Q{cx+r+62},{cy-r*0.2:.0f} {cx+r+40},{cy:.0f} L{cx+r+40},{cy+r*0.9:.0f}" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></g>')

# 1 HOOK — plate + meal tags
s = "hook"; tb = aw(s, "breakfast"); tl_ = aw(s, "lunch"); td = aw(s, "dinner"); thm = aw(s, "How many years")
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:78px; }}
#hk-pl {{ position:absolute; left:0; top:0; }}
.hk-t {{ position:absolute; font-family:'Gochi Hand',cursive; font-size:50px; padding:6px 22px; border:4px solid {K}; {SKETCH} }}
#hk-qm {{ position:absolute; left:800px; top:700px; font-size:150px; color:{C['red']}; }}
""", f"""
  <div id="hk-q" class="h1" style="opacity:0">How many <span class="hl">years</span><br>do you spend eating?</div>
  <svg id="hk-pl" width="{W}" height="960" data-layout-ignore>{plate_svg('hk-p', 540, 620, 170)}</svg>
  <div id="hk-b" class="hk-t" style="left:90px;top:400px;background:{C['hi']};opacity:0;transform:rotate(-8deg)">breakfast</div>
  <div id="hk-l" class="hk-t" style="left:420px;top:330px;background:{SKY};opacity:0;transform:rotate(3deg)">lunch</div>
  <div id="hk-d" class="hk-t" style="left:760px;top:410px;background:{PINK};opacity:0;transform:rotate(7deg)">dinner</div>
  <div id="hk-qm" class="big" style="opacity:0">?</div>
""", f"""
pop("#hk-p", 0.1);
pop("#hk-b", {tb:.2f}, {{from:{{rotation:-25}}, to:{{rotation:-8}}}});
pop("#hk-l", {tl_:.2f}, {{from:{{rotation:20}}, to:{{rotation:3}}}});
pop("#hk-d", {td:.2f}, {{from:{{rotation:25}}, to:{{rotation:7}}}});
rise("#hk-q", {thm-0.2:.2f});
pop("#hk-qm", {thm+0.8:.2f}, {{from:{{rotation:30}}, to:{{rotation:8}}}});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "Take a guess"); t1 = aw(s, "A few months"); t2 = aw(s, "One year"); t3 = aw(s, "four whole years")
notes = [("a", "a few<br>months?", -6, 110, C['hi']), ("b", "1 year?", 4, 405, SKY), ("c", "4 years?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:54px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "every bite")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1" style="opacity:0"><span class="hl">Let's add up every bite!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tct-0.3:.2f});
""")

# 4 SURVEY — diary clipboard + clock pie sweeping to 74 min
s = "survey"; twd = aw(s, "write down"); tav = aw(s, "On average"); t74 = aw(s, "seventy four minutes")
rows = ["7:00 wake up", "7:30 breakfast", "9:00 work", "12:30 lunch", "15:00 study", "19:00 dinner"]
meal = {1, 3, 5}
rh = "".join(f'<div class="sv-r{" sv-m" if i in meal else ""}" style="opacity:0">{r}</div>' for i, r in enumerate(rows))
ang = 74 / 60 * 360  # more than one lap: show 1 full lap + 14 min
scenes[s] = scene_file(s, f"""
#sv-t {{ top:150px; font-size:70px; }}
#sv-cb {{ position:absolute; left:80px; top:280px; width:440px; height:560px; background:#fff; border:5px solid {K}; {SKETCH} padding:60px 26px 20px; box-sizing:border-box; }}
#sv-clip {{ position:absolute; left:220px; top:262px; width:160px; height:44px; background:#9aa0a6; border:4px solid {K}; border-radius:10px; }}
.sv-r {{ font-family:'Gochi Hand',cursive; font-size:42px; line-height:76px; border-bottom:2px dashed #b9c4d6; position:relative; }}
#sv-n {{ position:absolute; left:560px; top:700px; width:480px; text-align:center; font-size:74px; color:{C['red']}; }}
""", f"""
  <div id="sv-t" class="h1">One whole day, <span class="hl">written down</span></div>
  <div id="sv-cb" style="opacity:0">{rh}</div><div id="sv-clip" style="opacity:0"></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <g id="sv-ck" style="opacity:0"><circle cx="800" cy="470" r="170" fill="#fff" stroke="{K}" stroke-width="7"/>
      <path id="sv-pie" d="" fill="{MINT}" stroke="{K}" stroke-width="3"/>
      {"".join(f'<path d="M{800+150*math.sin(k/12*6.283):.0f},{470-150*math.cos(k/12*6.283):.0f} L{800+168*math.sin(k/12*6.283):.0f},{470-168*math.cos(k/12*6.283):.0f}" stroke="{K}" stroke-width="5"/>' for k in range(12))}
      <circle cx="800" cy="470" r="10" fill="{K}"/></g></svg>
  <div id="sv-n" class="big" style="opacity:0">≈ 74 min a day</div>
""", f"""
pop("#sv-cb", {twd-0.4:.2f}); pop("#sv-clip", {twd-0.4:.2f});
tl.fromTo(".sv-r", {{opacity:0, x:-20}}, {{opacity:1, x:0, duration:0.2, stagger:0.15}}, {twd:.2f});
tl.to(".sv-m", {{color:"{C['red']}", duration:0.2, stagger:0.2}}, {tav:.2f});
pop("#sv-ck", {tav:.2f});
var pie = {{a:0}};
tl.to(pie, {{a:{ang:.1f}, duration:{max(1.0, t74 - tav):.2f}, ease:"power1.inOut", onUpdate:function(){{
  var a = Math.min(pie.a, 359.9) * Math.PI/180, x = 800 + 150*Math.sin(a), y = 470 - 150*Math.cos(a);
  document.querySelector("#sv-pie").setAttribute("d", "M800,470 L800,320 A150,150 0 " + (a > Math.PI ? 1 : 0) + ",1 " + x.toFixed(1) + "," + y.toFixed(1) + " Z");
}}}}, {tav+0.2:.2f});
pop("#sv-n", {t74:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
""")

# 5 WEEK — seven plates
s = "week"; t7 = aw(s, "Seven days"); t9 = aw(s, "nine hours")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
pl = "".join(f'<g class="wk-p" style="opacity:0"><circle cx="{150 + (i%4)*260}" cy="{360 + (i//4)*230}" r="90" fill="#fff" {WSF}/><circle cx="{150 + (i%4)*260}" cy="{360 + (i//4)*230}" r="58" fill="{CREAM}" stroke="{K}" stroke-width="3" stroke-dasharray="8 6"/><text x="{150 + (i%4)*260}" y="{374 + (i//4)*230}" text-anchor="middle" font-family="Gochi Hand" font-size="40" fill="{K}">{d}</text></g>' for i, d in enumerate(days))
scenes[s] = scene_file(s, f"""
#wk-t {{ top:150px; font-size:72px; }}
#wk-n {{ position:absolute; left:0; right:0; top:760px; text-align:center; font-size:96px; color:{C['blue']}; }}
""", f"""
  <div id="wk-t" class="h1"><span class="hl">7 days</span> of meals</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{pl}</svg>
  <div id="wk-n" class="big" style="opacity:0">almost <span class="red">9 hours</span></div>
""", f"""
rise("#wk-t", {t7-0.3:.2f});
tl.fromTo(".wk-p", {{opacity:0, scale:0.3, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.25, stagger:0.17, ease:"back.out(2)"}}, {t7:.2f});
pop("#wk-n", {t9:.2f});
""")

# 6 YEAR — 450 hours = almost 19 days, day squares fill
s = "year"; toy = aw(s, "One year"); t450 = aw(s, "four hundred fifty"); t19 = aw(s, "nineteen full days")
sq = "".join(f'<rect class="yr-s{" yr-f" if k < 19 else ""}" x="{160 + (k%7)*110}" y="{430 + (k//7)*100}" width="90" height="80" fill="#fff" stroke="{K}" stroke-width="4" rx="6"/>' for k in range(21))
scenes[s] = scene_file(s, f"""
#yr-t {{ position:absolute; left:0; right:0; top:150px; text-align:center; font-size:80px; }}
#yr-c {{ position:absolute; left:0; right:0; top:280px; text-align:center; font-size:76px; }}
#yr-d {{ position:absolute; left:0; right:0; top:760px; text-align:center; font-size:76px; color:{C['red']}; }}
""", f"""
  <div id="yr-t" class="big" style="opacity:0">1 year = <span id="yr-n">0</span> hours</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore><g id="yr-g" style="opacity:0">{sq}</g></svg>
  <div id="yr-d" class="big" style="opacity:0">≈ 19 days of chewing!</div>
""", f"""
rise("#yr-t", {toy:.2f}); count("#yr-n", 0, 450, {toy+0.2:.2f}, {max(0.6, t450-toy):.2f}, fmtInt);
pop("#yr-g", {t450+0.6:.2f});
tl.to(".yr-f", {{attr:{{fill:"{C['hi']}"}}, duration:0.08, stagger:0.06}}, {t450+0.9:.2f});
pop("#yr-d", {t19:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
""")

# 7 LIFE — 80-year bar, total about 4 years
s = "life"; t80 = aw(s, "eighty years"); t4 = aw(s, "About four years")
scenes[s] = scene_file(s, f"""
#lf-lab {{ position:absolute; left:0; right:0; top:160px; text-align:center; font-size:76px; }}
#lf-bar {{ position:absolute; left:120px; top:340px; width:840px; height:110px; border:5px solid {K}; {SKETCH} background:#fff; overflow:hidden; }}
#lf-fill {{ width:100%; height:100%; background:{MINT}; transform-origin:0 50%; }}
#lf-0 {{ position:absolute; left:110px; top:470px; font-size:44px; }}
#lf-80 {{ position:absolute; left:860px; top:470px; font-size:44px; }}
#lf-c {{ position:absolute; left:0; right:0; top:600px; text-align:center; }}
#lf-c .big {{ font-size:120px; color:{C['red']}; }}
""", f"""
  <div id="lf-lab" class="big" style="opacity:0"><span class="hl">80 years</span> of meals</div>
  <div id="lf-bar" style="opacity:0"><div id="lf-fill"></div></div>
  <div id="lf-0" class="big" style="opacity:0">age 0</div><div id="lf-80" class="big" style="opacity:0">age 80</div>
  <div id="lf-c" style="opacity:0"><span class="big">≈ 4 years!</span></div>
""", f"""
rise("#lf-lab", {t80-0.4:.2f}); pop("#lf-bar", {t80-0.4:.2f}); rise("#lf-0", {t80:.2f}); rise("#lf-80", {t80:.2f});
tl.fromTo("#lf-fill", {{scaleX:0}}, {{scaleX:1, duration:{max(0.8, t4-t80):.2f}, ease:"power1.inOut"}}, {t80:.2f});
pop("#lf-c", {t4:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.fromTo("#lf-c", {{scale:1}}, {{scale:1.08, duration:0.14, yoyo:true, repeat:1}}, {t4+0.7:.2f});
""")

# 8 WEEKEND — two clocks side by side
s = "weekend"; tws = aw(s, "weekends are slower"); t11 = aw(s, "eleven more minutes")
def clock(cid, cx, lab, col):
    return (f'<g id="{cid}" style="opacity:0"><circle cx="{cx}" cy="470" r="150" fill="#fff" stroke="{K}" stroke-width="7"/>'
            f'<path d="M{cx},470 L{cx},350" stroke="{K}" stroke-width="8" stroke-linecap="round"/>'
            f'<path class="hand" d="M{cx},470 L{cx+90},470" stroke="{col}" stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="470" r="9" fill="{K}"/>'
            f'<text x="{cx}" y="690" text-anchor="middle" font-family="Gochi Hand" font-size="52" fill="{K}">{lab}</text></g>')
scenes[s] = scene_file(s, f"""
#we-t {{ top:150px; font-size:76px; }}
#we-p {{ position:absolute; left:640px; top:740px; width:400px; text-align:center; font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="we-t" class="h1" style="opacity:0">Weekends are <span class="hl">slower</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{clock('we-a', 290, 'weekday', C['blue'])}{clock('we-b', 790, 'weekend', C['red'])}</svg>
  <div id="we-p" class="big" style="opacity:0">+11 min</div>
""", f"""
rise("#we-t", {tws-0.3:.2f}); pop("#we-a", {tws:.2f}); pop("#we-b", {tws+0.3:.2f});
tl.fromTo("#we-a .hand", {{rotation:0}}, {{rotation:300, svgOrigin:"290 470", duration:1.6, ease:"power1.inOut"}}, {tws+0.4:.2f});
tl.fromTo("#we-b .hand", {{rotation:0}}, {{rotation:366, svgOrigin:"790 470", duration:{max(1.8, t11-tws):.2f}, ease:"power1.inOut"}}, {tws+0.4:.2f});
pop("#we-p", {t11:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 9 YOU — family table, arrow up
s = "you"; tyf = aw(s, "your family"); tld = aw(s, "Long dinners"); thi = aw(s, "even higher")
ppl = "".join(f'<g class="yo-pp" style="opacity:0"><circle cx="{x}" cy="{y}" r="34" fill="#fff" stroke="{K}" stroke-width="5"/><path d="M{x-12},{y+6} Q{x},{y+16} {x+12},{y+6}" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="{x-11}" cy="{y-8}" r="4" fill="{K}"/><circle cx="{x+11}" cy="{y-8}" r="4" fill="{K}"/></g>' for x, y in [(200, 420), (380, 400), (560, 420), (200, 700), (380, 720), (560, 700)])
scenes[s] = scene_file(s, f"""
#yo-t {{ top:150px; font-size:76px; }}
""", f"""
  <div id="yo-t" class="h1" style="opacity:0">What about <span class="hl">your family?</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <rect id="yo-tb" x="130" y="480" width="500" height="160" rx="18" fill="{CREAM}" {WSF} style="opacity:0"/>
    {ppl}
    <g id="yo-ar" style="opacity:0"><path d="M860,820 L860,380" stroke="{C['red']}" stroke-width="16" stroke-linecap="round"/>
      <path d="M800,450 L860,370 L920,450" stroke="{C['red']}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="860" y="330" text-anchor="middle" font-family="Gochi Hand" font-size="60" fill="{K}">more?</text></g></svg>
""", f"""
rise("#yo-t", {tyf-0.4:.2f});
pop("#yo-tb", {tld:.2f});
tl.fromTo(".yo-pp", {{opacity:0, scale:0.3, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.25, stagger:0.12, ease:"back.out(2)"}}, {tld+0.2:.2f});
tl.fromTo("#yo-ar", {{opacity:0, y:120}}, {{opacity:1, y:0, duration:0.5, ease:"back.out(1.6)"}}, {thi:.2f});
""")

# 10 OUTRO
s = "outro"; t4o = aw(s, "four years"); tbc = aw(s, "every bite"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:80px; }}
#ou-b {{ top:300px; font-size:64px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1" style="opacity:0"><span class="hl">≈ 4 years</span> of eating</div>
  <div id="ou-b" class="h1" style="opacity:0">Make <span class="red">every bite</span> count</div>
  <div id="ou-c" style="opacity:0"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {t4o:.2f}); rise("#ou-b", {tbc-0.3:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "How many years"), SC["guess"]["start"] + 0.2)
point(g("guess", "A few months"), 3.0)
wave(g("intro", "I'm Max"))
point(g("survey", "seventy four minutes"), 1.4)
point(g("week", "nine hours"), 1.2)
wow(g("year", "nineteen full days"), 1.3)
wow(g("life", "About four years"), 1.4)
point(g("weekend", "eleven more minutes"), 1.2)
think(g("you", "your family"), g("you", "Long dinners"))
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("pop.mp3", A("hook", "breakfast"), 0.45), ("pop.mp3", A("hook", "lunch"), 0.45), ("pop.mp3", A("hook", "dinner"), 0.45),
        ("ping.mp3", A("hook", "How many years"), 0.35), ("pop.mp3", A("guess", "A few months"), 0.5), ("pop.mp3", A("guess", "One year"), 0.5),
        ("pop.mp3", A("guess", "four whole years"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("survey", "seventy four minutes"), 0.5),
        ("click-soft.mp3", A("week", "nine hours"), 0.5), ("impact-bass-1.mp3", A("year", "nineteen full days"), 0.4),
        ("impact-bass-2.mp3", A("life", "About four years"), 0.4), ("ping.mp3", A("weekend", "eleven more minutes"), 0.4),
        ("riser.mp3", A("you", "Long dinners"), 0.3), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
