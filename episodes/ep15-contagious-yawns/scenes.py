# MAX WISE ep15 — Why are yawns contagious?  Executed inside engine/maxwise.py.
# === SCENES ===
import random as _r
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; MINT = "#C9E8C2"; SKIN = "#FFE3C4"

def face_svg(fid, w, mouth_id):
    return (f'<svg id="{fid}" width="{w}" height="{w}" viewBox="0 0 300 300" data-layout-ignore>'
            f'<circle cx="150" cy="150" r="130" fill="{SKIN}" {WSF}/>'
            f'<path d="M90,115 Q105,128 120,115 M180,115 Q195,128 210,115" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>'
            f'<ellipse id="{mouth_id}" cx="150" cy="200" rx="34" ry="8" fill="#7A2E2E" stroke="{K}" stroke-width="5"/></svg>')

# 1 HOOK — a face that yawns
s = "hook"; tch = aw(s, "Quick challenge"); tyn = aw(s, "not to yawn"); tct = aw(s, "so contagious")
scenes[s] = scene_file(s, f"""
#hk-tag {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
#hk-q {{ top:250px; font-size:80px; }}
#hk-f {{ position:absolute; left:330px; top:460px; }}
#hk-y {{ position:absolute; left:640px; top:470px; font-size:96px; color:{C['red']}; transform:rotate(10deg); }}
""", f"""
  <div id="hk-tag"><span class="chip">CHALLENGE: DON'T YAWN!</span></div>
  <div id="hk-q" class="h1">Why are yawns<br><span class="hl">contagious</span>?</div>
  <div id="hk-f">{face_svg('hk-fs', 400, 'hk-m')}</div>
  <div id="hk-y" class="big" style="opacity:0">YAAAWN</div>
""", f"""
pop("#hk-tag .chip", {tch:.2f}, {{from:{{rotation:-8}}, to:{{rotation:-2}}}});
pop("#hk-f", {tyn-0.3:.2f});
tl.to("#hk-m", {{attr:{{ry:52, rx:46}}, duration:0.8, ease:"power2.out"}}, {tyn:.2f});
pop("#hk-y", {tyn+0.4:.2f}, {{from:{{rotation:30}}, to:{{rotation:10}}}});
tl.to("#hk-m", {{attr:{{ry:8, rx:34}}, duration:0.5}}, {tct-0.6:.2f});
tl.to("#hk-y", {{opacity:0, duration:0.2}}, {tct-0.6:.2f});
rise("#hk-q", {tct-0.9:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "Take a guess"); t1 = aw(s, "tired"); t2 = aw(s, "copy others"); t3 = aw(s, "care about")
notes = [("a", "tired?", -6, 110, C['hi']), ("b", "copying?", 4, 405, SKY), ("c", "caring?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:54px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tmy = aw(s, "real mystery")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">A real mystery!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
pop("#in-sub", {tmy-0.3:.2f});
""")

# 4 TEST — TV with a yawning face, 328 people dots
rnd = _r.Random(15)
yawned = set(rnd.sample(range(328), 222))
def people(cls_extra):
    out = ""
    for k in range(328):
        x = 120 + (k % 41) * 21; y = 545 + (k // 41) * 40
        c = "pp-y" if k in yawned else "pp-n"
        out += f'<g class="pp {c} {cls_extra}" style="opacity:0"><circle cx="{x}" cy="{y}" r="7" fill="#fff" stroke="{K}" stroke-width="3"/><path d="M{x},{y+7} L{x},{y+24}" stroke="{K}" stroke-width="3"/></g>'
    return out
s = "test"; tdk = aw(s, "at Duke"); t328 = aw(s, "Three hundred twenty eight"); tvd = aw(s, "three minute")
scenes[s] = scene_file(s, f"""
#ts-tv {{ position:absolute; left:380px; top:160px; width:420px; height:270px; background:{SKY}; border:6px solid {K}; {SKETCH} }}
#ts-tv .t {{ position:absolute; right:12px; bottom:6px; font-family:'Gochi Hand',cursive; font-size:44px; }}
#ts-tvf {{ position:absolute; left:110px; top:20px; }}
#ts-n {{ position:absolute; left:0; right:0; top:450px; text-align:center; font-size:56px; }}
#ts-d {{ position:absolute; left:30px; top:110px; transform:rotate(-6deg); }}
""", f"""
  <div id="ts-d"><span class="chip">DUKE STUDY</span></div>
  <div id="ts-tv"><div id="ts-tvf">{face_svg('ts-fs', 200, 'ts-m')}</div><div class="t">3 min</div></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{people('ts')}</svg>
  <div id="ts-n" class="big" style="opacity:0"><span class="red">328</span> people</div>
""", f"""
pop("#ts-d", {tdk-0.4:.2f}); pop("#ts-tv", {tvd-0.6:.2f});
tl.to("#ts-m", {{attr:{{ry:50, rx:44}}, duration:0.6, yoyo:true, repeat:1, ease:"sine.inOut"}}, {tvd:.2f});
tl.to(".pp.ts", {{opacity:1, duration:0.05, stagger:0.004}}, {t328:.2f});
pop("#ts-n", {t328+0.6:.2f});
""")

# 5 RESULT — 222 of them turn yellow
s = "result"; t222 = aw(s, "Two hundred twenty two"); t23 = aw(s, "two out of every")
yel = "".join(f'<g class="rs-g" style="opacity:0"><circle cx="{120 + (k % 41) * 21}" cy="{545 + (k // 41) * 40}" r="9" fill="{C["hi"]}" stroke="{C["red"]}" stroke-width="3"/></g>' for k in sorted(yawned))
scenes[s] = scene_file(s, f"""
#rs-a {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-size:90px; }}
#rs-b {{ position:absolute; left:0; right:0; top:330px; text-align:center; }}
#rs-b .pill {{ font-size:76px; }}
""", f"""
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>{people('rs')}{yel}</svg>
  <div id="rs-a" class="big"><span class="red">222</span> / 328 yawned</div>
  <div id="rs-b" style="opacity:0"><span class="pill">≈ 2 out of 3</span></div>
""", f"""
tl.set(".pp.rs", {{opacity:1}}, 0.0);
rise("#rs-a", {t222:.2f});
tl.to(".rs-g", {{opacity:1, duration:0.05, stagger:0.006}}, {t222+0.1:.2f});
pop("#rs-b", {t23:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-3}}}});
""")

# 6 SPREAD — ruler from 0 to 15 yawns
s = "spread"; tnv = aw(s, "never yawned"); t15 = aw(s, "fifteen times")
ticks = "".join(f'<path d="M{140+k*53},420 L{140+k*53},{460 if k%5 else 480}" stroke="{K}" stroke-width="4"/>' + (f'<text x="{140+k*53}" y="525" text-anchor="middle" font-family="Gochi Hand" font-size="44" fill="{K}">{k}</text>' if k % 5 == 0 else "") for k in range(16))
scenes[s] = scene_file(s, f"""
#sp-t {{ top:160px; font-size:76px; }}
#sp-a {{ position:absolute; left:60px; top:600px; width:260px; text-align:center; font-size:52px; color:{C['blue']}; }}
#sp-b {{ position:absolute; left:770px; top:600px; width:290px; text-align:center; font-size:52px; color:{C['red']}; }}
""", f"""
  <div id="sp-t" class="h1">yawns <span class="hl">per person</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <rect id="sp-r" x="110" y="400" width="860" height="150" rx="10" fill="{C['hi']}" opacity=".5" stroke="{K}" stroke-width="5"/>{ticks}
    <path id="sp-m0" d="M140,370 L140,330" stroke="{C['blue']}" stroke-width="8" stroke-linecap="round" style="opacity:0"/>
    <path id="sp-m15" d="M935,370 L935,330" stroke="{C['red']}" stroke-width="8" stroke-linecap="round" style="opacity:0"/></svg>
  <div id="sp-a" class="big" style="opacity:0">0 yawns</div>
  <div id="sp-b" class="big" style="opacity:0">15 yawns!</div>
""", f"""
pop("#sp-t", 0.05); pop("#sp-r", 0.1);
tl.to("#sp-m0", {{opacity:1, duration:0.2}}, {tnv:.2f}); pop("#sp-a", {tnv:.2f});
tl.to("#sp-m15", {{opacity:1, duration:0.2}}, {t15:.2f}); pop("#sp-b", {t15:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}});
""")

# 7 EMPATHY — myth crossed out
s = "empathy"; tem = aw(s, "show empathy"); tst = aw(s, "this study"); tdn = aw(s, "did not")
scenes[s] = scene_file(s, f"""
#em-myth {{ position:absolute; left:0; right:0; top:260px; text-align:center; font-family:'Gochi Hand',cursive; font-size:100px; color:{C['pencil']}; }}
#em-real {{ position:absolute; left:0; right:0; top:520px; text-align:center; }}
#em-real .pill {{ font-size:66px; }}
#em-lab {{ position:absolute; left:0; right:0; top:150px; text-align:center; }}
""", f"""
  <div id="em-lab"><span class="chip">THE POPULAR IDEA</span></div>
  <div id="em-myth">yawn = empathy</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore><path id="em-x" d="M200,350 Q540,300 880,330" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/></svg>
  <div id="em-real" style="opacity:0"><span class="pill">no strong link found</span></div>
""", f"""
pop("#em-lab", 0.05); rise("#em-myth", {tem-0.6:.2f});
draw("#em-x", {tdn:.2f}, 0.35); pop("#em-real", {tdn+0.5:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
""")

# 8 AGE — young vs older, a tiny slice of the pie
s = "age"; tcl = aw(s, "was age"); told = aw(s, "Older people"); ttn = aw(s, "tiny part")
def bubbles(x, n, cls):
    return "".join(f'<circle class="{cls}" cx="{x + (k%3)*44}" cy="{560 - (k//3)*44}" r="16" fill="{SKY}" stroke="{K}" stroke-width="3" style="opacity:0"/>' for k in range(n))
scenes[s] = scene_file(s, f"""
#ag-t {{ top:150px; font-size:76px; }}
#ag-y {{ position:absolute; left:120px; top:640px; width:220px; text-align:center; font-size:46px; }}
#ag-o {{ position:absolute; left:400px; top:640px; width:220px; text-align:center; font-size:46px; }}
#ag-pl {{ position:absolute; left:660px; top:680px; width:380px; text-align:center; font-size:46px; }}
""", f"""
  <div id="ag-t" class="h1">the only clue: <span class="hl">age</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    {bubbles(160, 9, 'ag-by')}{bubbles(440, 3, 'ag-bo')}
    <g id="ag-pie" style="opacity:0"><circle cx="850" cy="500" r="140" fill="#fff" stroke="{K}" stroke-width="6"/>
      <path d="M850,500 L850,360 A140,140 0 0,1 914,376 Z" fill="{C['red']}" stroke="{K}" stroke-width="4"/></g></svg>
  <div id="ag-y" class="big" style="opacity:0">younger</div>
  <div id="ag-o" class="big" style="opacity:0">older</div>
  <div id="ag-pl" class="big" style="opacity:0">age = a <span class="red">tiny</span> part</div>
""", f"""
rise("#ag-t", {tcl-0.6:.2f});
rise("#ag-y", {told-0.4:.2f}); tl.to(".ag-by", {{opacity:1, duration:0.1, stagger:0.06}}, {told-0.4:.2f});
rise("#ag-o", {told:.2f}); tl.to(".ag-bo", {{opacity:1, duration:0.1, stagger:0.08}}, {told+0.2:.2f});
pop("#ag-pie", {ttn-0.6:.2f}); rise("#ag-pl", {ttn:.2f});
""")

# 9 MYSTERY — three question stickies
s = "mystery"; tnb = aw(s, "nobody knows"); tcp = aw(s, "Copying"); tsb = aw(s, "social bonding"); tgn = aw(s, "your genes")
st = [("a", "copying?", -5, 110, C['hi']), ("b", "bonding?", 3, 405, MINT), ("c", "genes?", -4, 700, PINK)]
sh = "".join(f'<div id="my-{k}" class="abs" style="left:{x}px;top:470px;width:270px;height:200px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;font-family:Gochi Hand,cursive;font-size:54px;opacity:0">{txt}</div>' for k, txt, r, x, bg in st)
scenes[s] = scene_file(s, f"""
#my-t {{ top:150px; font-size:66px; white-space:nowrap; }}
#my-q {{ position:absolute; left:0; right:0; top:300px; text-align:center; font-size:110px; color:{C['red']}; }}
""", f"""
  <div id="my-t" class="h1">Nobody knows <span class="hl">for sure</span>… yet</div>
  <div id="my-q" class="big" style="opacity:0">? ? ?</div>
  {sh}
""", f"""
rise("#my-t", {tnb-0.3:.2f}); pop("#my-q", {tnb+0.3:.2f});
pop("#my-a", {tcp:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-5}}}}); pop("#my-b", {tsb:.2f}, {{from:{{rotation:20}}, to:{{rotation:3}}}});
pop("#my-c", {tgn:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-4}}}});
""")

# 10 OUTRO
s = "outro"; t23 = aw(s, "Two out of three"); tdy = aw(s, "did you yawn"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:76px; }}
#ou-b {{ top:300px; font-size:90px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1"><span class="hl">2 out of 3</span> catch a yawn</div>
  <div id="ou-b" class="h1">Did <span class="red">you</span> yawn?</div>
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {t23:.2f}); pop("#ou-b", {tdy:.2f}, {{from:{{rotation:-10}}, to:{{rotation:-2}}}});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc-0.3:.2f});
pop("#ou-c", {tsc:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "Why is"), SC["guess"]["start"] + 0.2)
point(g("guess", "tired"), 3.0)
wave(g("intro", "I'm Max"))
point(g("test", "Three hundred twenty eight"), 1.3)
wow(g("result", "two out of every"), 1.3)
point(g("spread", "fifteen times"), 1.2)
point(g("empathy", "did not"), 1.2)
point(g("age", "Older people"), 1.2)
think(g("mystery", "nobody knows"), g("mystery", "Copying"))
wow(g("outro", "did you yawn"), 1.0)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "so contagious"), 0.35), ("whoosh-short.mp3", A("hook", "not to yawn"), 0.4), ("pop.mp3", A("guess", "tired"), 0.5),
        ("pop.mp3", A("guess", "copy others"), 0.5), ("pop.mp3", A("guess", "care about"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click-soft.mp3", A("test", "Three hundred twenty eight"), 0.5), ("impact-bass-1.mp3", A("result", "two out of every"), 0.4),
        ("pop.mp3", A("spread", "fifteen times"), 0.5), ("click.mp3", A("empathy", "did not"), 0.45), ("pop.mp3", A("age", "tiny part"), 0.5),
        ("riser.mp3", A("mystery", "nobody knows"), 0.25), ("pop.mp3", A("outro", "did you yawn"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
