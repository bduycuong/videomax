# MAX WISE ep17 — Why do we get goosebumps?  Executed inside engine/maxwise.py.
# === SCENES ===
import random
WSF = WS.replace('fill="none" ', '')
PINK = "#FFC9C2"; SKY = "#BFE3F7"; MINT = "#C9E8C2"; SKIN = "#F6D2B5"; FUR = "#F2B66B"

def snowflake(x, y, r):
    return "".join(f'<path d="M{x},{y} L{x + r*__import__("math").cos(a*1.0472):.0f},{y + r*__import__("math").sin(a*1.0472):.0f}" stroke="{C["blue"]}" stroke-width="6" stroke-linecap="round"/>' for a in range(6))

# 1 HOOK — arm with bumps popping
s = "hook"; tc = aw(s, "the cold"); tsg = aw(s, "favorite song"); tbu = aw(s, "tiny bumps"); twq = aw(s, "Why do we")
rnd = random.Random(7)
bumps = "".join(f'<circle class="hk-bp" cx="{rnd.randint(200, 860)}" cy="{rnd.randint(540, 700)}" r="{rnd.randint(7, 11)}" fill="#E9B590" stroke="{K}" stroke-width="2.5" style="opacity:0"/>' for _ in range(70))
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:84px; }}
""", f"""
  <div id="hk-q" class="h1" style="opacity:0">Why do we get<br><span class="hl">goosebumps?</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <path id="hk-arm" d="M120,560 Q500,500 900,540 Q990,560 1000,620 Q990,690 900,700 Q500,730 120,720 Z" fill="{SKIN}" {WSF}/>
    {bumps}
    <g id="hk-sn" style="opacity:0">{snowflake(230, 400, 55)}</g>
    <g id="hk-mu" style="opacity:0"><path d="M820,440 L820,330 L890,315 L890,420" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round"/>
      <ellipse cx="800" cy="440" rx="26" ry="20" fill="{K}"/><ellipse cx="870" cy="422" rx="26" ry="20" fill="{K}"/></g></svg>
""", f"""
pop("#hk-arm", 0.1);
pop("#hk-sn", {tc:.2f}); pop("#hk-mu", {tsg:.2f});
tl.fromTo(".hk-bp", {{opacity:0, scale:0, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.15, stagger:0.02, ease:"back.out(3)"}}, {tbu:.2f});
rise("#hk-q", {twq-0.2:.2f});
""")

# 2 GUESS
s = "guess"; tg = aw(s, "Take a guess"); t1 = aw(s, "keep us warm"); t2 = aw(s, "scare enemies"); t3 = aw(s, "just a leftover")
notes = [("a", "keep<br>warm?", -6, 110, C['hi']), ("b", "scare<br>enemies?", 4, 405, SKY), ("c", "a<br>leftover?", -3, 700, PINK)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:270px;height:270px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);display:flex;align-items:center;justify-content:center;text-align:center;font-family:Gochi Hand,cursive;font-size:54px;line-height:1.05;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", f"""
pop("#gs-title", {tg:.2f}); pop("#gs-a", {t1:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-6}}}});
pop("#gs-b", {t2:.2f}, {{from:{{rotation:20}}, to:{{rotation:4}}}}); pop("#gs-c", {t3:.2f}, {{from:{{rotation:-20}}, to:{{rotation:-3}}}});
""")

# 3 INTRO
s = "intro"; tmw = aw(s, "Max Wise"); tz = aw(s, "zoom into")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; font-family:'Gochi Hand',cursive; font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="40" data-layout-ignore><path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1" style="opacity:0"><span class="hl">Let's zoom into your skin!</span></div>
""", f"""
pop("#in-logo", {tmw:.2f}, {{from:{{scale:1.6}}, to:{{}}}}); draw("#in-ul", {tmw+0.3:.2f}, 0.4);
rise("#in-sub", {tz-0.3:.2f});
""")

# 4 MUSCLE — skin cutaway: follicle, hair, muscle squeezes
s = "muscle"; tfo = aw(s, "follicle"); tmu = aw(s, "Attached to it"); tsq = aw(s, "it squeezes"); tsu = aw(s, "stands up"); tbp = aw(s, "into a bump")
scenes[s] = scene_file(s, f"""
#mu-t {{ top:150px; font-size:70px; }}
.mu-lab {{ position:absolute; font-family:'Gochi Hand',cursive; font-size:46px; padding:4px 18px; border:4px solid {K}; {SKETCH} }}
""", f"""
  <div id="mu-t" class="h1">Inside your <span class="hl">skin</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <rect x="80" y="420" width="920" height="460" fill="{PINK}" opacity=".55"/>
    <path id="mu-skin" d="M80,420 L400,420 Q480,420 480,420 L1000,420" stroke="{K}" stroke-width="7" fill="none"/>
    <path id="mu-bump" d="M380,420 Q480,360 580,420" stroke="{K}" stroke-width="7" fill="{SKIN}" style="opacity:0"/>
    <path id="mu-fol" d="M450,420 L430,720 Q480,770 530,720 L510,420" fill="#fff" {WSF} style="opacity:0"/>
    <path id="mu-h1" d="M480,740 L480,420 L270,300" stroke="{K}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="mu-h2" d="M480,740 L480,300" stroke="{K}" stroke-width="10" fill="none" stroke-linecap="round" style="opacity:0"/>
    <path id="mu-m" d="M520,600 Q640,560 760,470" stroke="{C['red']}" stroke-width="26" fill="none" stroke-linecap="round" style="opacity:0"/></svg>
  <div id="mu-lf" class="mu-lab" style="left:120px;top:620px;background:#fff;opacity:0">follicle</div>
  <div id="mu-lm" class="mu-lab" style="left:720px;top:560px;background:{C['hi']};opacity:0">tiny muscle</div>
  <div id="mu-lb" class="mu-lab" style="left:640px;top:300px;background:{SKY};opacity:0">bump!</div>
""", f"""
pop("#mu-fol", {tfo-0.2:.2f}); pop("#mu-lf", {tfo:.2f});
tl.to("#mu-m", {{opacity:1, duration:0.3}}, {tmu:.2f}); pop("#mu-lm", {tmu+0.3:.2f});
tl.fromTo("#mu-m", {{scale:1}}, {{scale:0.86, transformOrigin:"100% 0%", duration:0.3, yoyo:true, repeat:3}}, {tsq:.2f});
tl.to("#mu-h1", {{opacity:0, duration:0.15}}, {tsu-0.1:.2f}); tl.to("#mu-h2", {{opacity:1, duration:0.15}}, {tsu-0.1:.2f});
tl.fromTo("#mu-h2", {{scaleY:0.9}}, {{scaleY:1, svgOrigin:"480 740", duration:0.4, ease:"back.out(3)"}}, {tsu-0.1:.2f});
tl.to("#mu-bump", {{opacity:1, duration:0.25}}, {tbp-0.2:.2f}); pop("#mu-lb", {tbp:.2f});
""")

# 5 NERVE — three triggers, one switch, wired to the muscle
s = "nerve"; tff = aw(s, "fight or flight"); tco = aw(s, "So cold"); tfe = aw(s, "fear"); tso = aw(s, "thrilling song"); tsw = aw(s, "same switch")
scenes[s] = scene_file(s, f"""
#nv-t {{ top:150px; font-size:70px; }}
.nv-c {{ position:absolute; width:250px; text-align:center; font-family:'Gochi Hand',cursive; font-size:50px; padding:10px 0; border:4px solid {K}; {SKETCH} }}
#nv-sw {{ position:absolute; left:380px; top:600px; width:320px; text-align:center; font-family:'Gochi Hand',cursive; font-size:44px; line-height:1.05; padding:14px 0; background:#fff; border:5px solid {K}; {SKETCH} }}
""", f"""
  <div id="nv-t" class="h1" style="opacity:0"><span class="hl">Fight or flight</span> nerves</div>
  <div id="nv-a" class="nv-c" style="left:80px;top:320px;background:{SKY};opacity:0">cold</div>
  <div id="nv-b" class="nv-c" style="left:415px;top:300px;background:{PINK};opacity:0">fear</div>
  <div id="nv-c" class="nv-c" style="left:750px;top:320px;background:{C['hi']};opacity:0">a song</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <path id="nv-la" d="M205,400 Q300,520 470,600" stroke="{K}" stroke-width="5" fill="none" stroke-dasharray="12 8"/>
    <path id="nv-lb" d="M540,385 L540,600" stroke="{K}" stroke-width="5" fill="none" stroke-dasharray="12 8"/>
    <path id="nv-lc" d="M875,400 Q780,520 610,600" stroke="{K}" stroke-width="5" fill="none" stroke-dasharray="12 8"/>
    <path id="nv-n" d="M700,650 Q760,620 800,680 T900,700 T990,660" stroke="{C['blue']}" stroke-width="9" fill="none" stroke-linecap="round"/></svg>
  <div id="nv-sw" style="opacity:0">ONE<br>SWITCH</div>
""", f"""
rise("#nv-t", {tff-0.3:.2f}); pop("#nv-sw", {tff:.2f}); draw("#nv-n", {tff+0.4:.2f}, 0.6);
pop("#nv-a", {tco:.2f}); draw("#nv-la", {tco+0.2:.2f}, 0.4);
pop("#nv-b", {tfe:.2f}); draw("#nv-lb", {tfe+0.2:.2f}, 0.4);
pop("#nv-c", {tso:.2f}); draw("#nv-lc", {tso+0.2:.2f}, 0.4);
tl.fromTo("#nv-sw", {{scale:1}}, {{scale:1.12, duration:0.15, yoyo:true, repeat:1}}, {tsw:.2f});
tl.to("#nv-sw", {{backgroundColor:"{C['hi']}", duration:0.2}}, {tsw:.2f});
""")

# 6 FUR — cat: flat fur -> puffed fur, warm air band
s = "fur"; tfa = aw(s, "furry animals"); ttr = aw(s, "traps"); tbg = aw(s, "look bigger")
def cat(cid, puff):
    sp = "".join(f'<path d="M{540 + 230*__import__("math").cos(a/24*6.283):.0f},{520 + 160*__import__("math").sin(a/24*6.283):.0f} L{540 + (230+puff)*__import__("math").cos((a+0.5)/24*6.283):.0f},{520 + (160+puff)*__import__("math").sin((a+0.5)/24*6.283):.0f} L{540 + 230*__import__("math").cos((a+1)/24*6.283):.0f},{520 + 160*__import__("math").sin((a+1)/24*6.283):.0f}" fill="{FUR}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>' for a in range(24))
    return (f'<g id="{cid}">{sp}<ellipse cx="540" cy="520" rx="230" ry="160" fill="{FUR}" stroke="{K}" stroke-width="0"/>'
            f'<circle cx="780" cy="420" r="90" fill="{FUR}" stroke="{K}" stroke-width="6"/>'
            f'<path d="M720,350 L735,280 L770,335 M800,335 L835,280 L845,350" fill="{FUR}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
            f'<circle cx="755" cy="410" r="9" fill="{K}"/><circle cx="810" cy="410" r="9" fill="{K}"/>'
            f'<path d="M770,450 Q782,460 794,450" stroke="{K}" stroke-width="4" fill="none"/></g>')
scenes[s] = scene_file(s, f"""
#fu-t {{ top:150px; font-size:70px; }}
.fu-lab {{ position:absolute; font-family:'Gochi Hand',cursive; font-size:48px; padding:4px 18px; border:4px solid {K}; {SKETCH} }}
""", f"""
  <div id="fu-t" class="h1" style="opacity:0">Useful for <span class="hl">furry animals</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <ellipse id="fu-air" cx="540" cy="520" rx="330" ry="250" fill="{C['hi']}" opacity=".0"/>
    <g id="fu-flat">{cat('fu-c1', 14)}</g>
    <g id="fu-puff" style="opacity:0">{cat('fu-c2', 70)}</g></svg>
  <div id="fu-lw" class="fu-lab" style="left:110px;top:270px;background:#fff;opacity:0">warm air trapped</div>
  <div id="fu-lb" class="fu-lab" style="left:620px;top:800px;background:{PINK};opacity:0">looks BIGGER!</div>
""", f"""
rise("#fu-t", {tfa-0.3:.2f}); pop("#fu-flat", {tfa:.2f});
tl.to("#fu-flat", {{opacity:0, duration:0.2}}, {ttr-0.2:.2f}); tl.to("#fu-puff", {{opacity:1, duration:0.2}}, {ttr-0.2:.2f});
tl.to("#fu-air", {{opacity:0.45, duration:0.4}}, {ttr:.2f}); pop("#fu-lw", {ttr+0.2:.2f});
tl.fromTo("#fu-puff", {{scale:1}}, {{scale:1.1, svgOrigin:"540 520", duration:0.4, ease:"back.out(2)"}}, {tbg-0.1:.2f});
pop("#fu-lb", {tbg:.2f}, {{from:{{rotation:-15}}, to:{{rotation:-4}}}});
""")

# 7 US — human arm, thermometer barely moves, crossed out
s = "us"; tlo = aw(s, "lost most"); tba = aw(s, "barely keep")
scenes[s] = scene_file(s, f"""
#us-t {{ top:150px; font-size:70px; }}
#us-w {{ position:absolute; left:620px; top:300px; font-family:'Gochi Hand',cursive; font-size:70px; }}
""", f"""
  <div id="us-t" class="h1" style="opacity:0">Humans: <span class="hl">not much fur</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <g id="us-arm" style="opacity:0"><path d="M60,520 Q300,470 520,500 Q590,515 595,560 Q590,610 520,620 Q300,640 60,620 Z" fill="{SKIN}" {WSF}/>
      {"".join(f'<path d="M{x},{505 + (x%3)*3} L{x+6},{482}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' for x in range(110, 520, 70))}</g>
    <g id="us-th" style="opacity:0"><rect x="780" y="420" width="60" height="330" rx="30" fill="#fff" {WSF}/>
      <circle cx="810" cy="770" r="50" fill="{C['red']}" stroke="{K}" stroke-width="6"/>
      <rect id="us-mer" x="795" y="690" width="30" height="60" fill="{C['red']}"/></g>
    <path id="us-x" d="M640,380 L980,820 M980,380 L640,820" stroke="{C['red']}" stroke-width="14" stroke-linecap="round" fill="none"/></svg>
  <div id="us-w" style="opacity:0">warmer?</div>
""", f"""
rise("#us-t", {tlo-0.3:.2f}); pop("#us-arm", {tlo:.2f});
pop("#us-th", {tba-0.8:.2f}); rise("#us-w", {tba-0.8:.2f});
tl.fromTo("#us-mer", {{attr:{{y:690, height:60}}}}, {{attr:{{y:676, height:74}}, duration:0.6}}, {tba-0.3:.2f});
draw("#us-x", {tba+0.4:.2f}, 0.5);
""")

# 8 TWIST — 2020 Harvard: nerve + muscle wake stem cells
s = "twist"; ttw = aw(s, "the twist"); t20 = aw(s, "twenty twenty"); tnm = aw(s, "same nerve"); tsc = aw(s, "stem cells")
scenes[s] = scene_file(s, f"""
#tw-t {{ top:150px; font-size:76px; }}
#tw-y {{ position:absolute; left:120px; top:290px; transform:rotate(-5deg); }}
#tw-y .chip {{ font-size:54px; }}
.tw-b {{ position:absolute; width:250px; text-align:center; font-family:'Gochi Hand',cursive; font-size:46px; line-height:1.05; padding:16px 0; border:4px solid {K}; {SKETCH} }}
""", f"""
  <div id="tw-t" class="h1" style="opacity:0">Here's the <span class="red">twist</span></div>
  <div id="tw-y" style="opacity:0"><span class="chip">2020 · Harvard study</span></div>
  <div id="tw-n" class="tw-b" style="left:60px;top:520px;background:{SKY};opacity:0">nerve</div>
  <div id="tw-m" class="tw-b" style="left:415px;top:520px;background:{PINK};opacity:0">muscle</div>
  <div id="tw-s" class="tw-b" style="left:770px;top:500px;background:{MINT};opacity:0">stem cells<br>wake up!</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <path id="tw-a1" d="M320,560 L400,560 M385,545 L405,560 L385,575" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="tw-a2" d="M675,560 L755,560 M740,545 L760,560 L740,575" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path id="tw-h" d="M895,720 L895,840 M870,740 L895,700 L920,740" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round" style="opacity:0"/></svg>
""", f"""
rise("#tw-t", {ttw-0.3:.2f}); pop("#tw-y", {t20:.2f}, {{from:{{rotation:-15}}, to:{{rotation:-5}}}});
pop("#tw-n", {tnm:.2f}); draw("#tw-a1", {tnm+0.3:.2f}, 0.3); pop("#tw-m", {tnm+0.5:.2f}); draw("#tw-a2", {tsc-0.4:.2f}, 0.3);
pop("#tw-s", {tsc:.2f}); tl.to("#tw-h", {{opacity:1, duration:0.3}}, {tsc+0.6:.2f});
tl.fromTo("#tw-s", {{scale:1}}, {{scale:1.1, duration:0.15, yoyo:true, repeat:3}}, {tsc+0.4:.2f});
""")

# 9 MICE — timeline: day 0 -> less than two weeks, fur grows
s = "mice"; tcl = aw(s, "in the cold"); tnh = aw(s, "new hair"); t2w = aw(s, "two weeks")
def mouse(mid, x, hair):
    hr = "".join(f'<path class="{mid}-h" d="M{x-90+i*18},{560 - (i%2)*6} L{x-94+i*18},{530 - (i%3)*6}" stroke="{K}" stroke-width="4" stroke-linecap="round" style="opacity:{1 if hair else 0}"/>' for i in range(11))
    return (f'<g id="{mid}"><ellipse cx="{x}" cy="600" rx="120" ry="70" fill="#D9D9D9" stroke="{K}" stroke-width="6"/>'
            f'<circle cx="{x+120}" cy="575" r="45" fill="#D9D9D9" stroke="{K}" stroke-width="6"/>'
            f'<circle cx="{x+108}" cy="530" r="24" fill="{PINK}" stroke="{K}" stroke-width="5"/><circle cx="{x+135}" cy="568" r="7" fill="{K}"/>'
            f'<path d="M{x-120},610 Q{x-200},640 {x-170},700" stroke="{K}" stroke-width="5" fill="none"/>{hr}</g>')
scenes[s] = scene_file(s, f"""
#mi-t {{ top:150px; font-size:70px; }}
.mi-d {{ position:absolute; top:760px; width:300px; text-align:center; font-family:'Gochi Hand',cursive; font-size:54px; }}
""", f"""
  <div id="mi-t" class="h1" style="opacity:0">Mice in the <span class="hl">cold</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" data-layout-ignore>
    <g id="mi-sn" style="opacity:0">{snowflake(540, 320, 50)}</g>
    {mouse('mi-a', 230, False)}
    <path id="mi-ar" d="M440,600 L600,600 M580,580 L605,600 L580,620" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round" style="opacity:0"/>
    <g id="mi-bw" style="opacity:0">{mouse('mi-b', 790, False)}</g></svg>
  <div id="mi-d0" class="mi-d" style="left:90px;opacity:0">day 0</div>
  <div id="mi-d1" class="mi-d" style="left:690px;opacity:0;color:{C['red']}">&lt; 2 weeks</div>
""", f"""
pop("#mi-a", {tcl-0.6:.2f}); rise("#mi-t", {tcl-0.4:.2f}); pop("#mi-sn", {tcl:.2f}); rise("#mi-d0", {tcl:.2f});
tl.to("#mi-ar", {{opacity:1, duration:0.3}}, {tnh-0.3:.2f}); pop("#mi-bw", {tnh-0.2:.2f});
tl.to(".mi-b-h", {{opacity:1, duration:0.1, stagger:0.06}}, {tnh+0.1:.2f});
pop("#mi-d1", {t2w:.2f}, {{from:{{rotation:-12}}, to:{{rotation:-3}}}});
""")

# 10 OUTRO
s = "outro"; tlf = aw(s, "a leftover"); thh = aw(s, "hair growing helper"); tsc2 = aw(s, "Stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ top:150px; font-size:74px; }}
#ou-b {{ top:300px; font-size:64px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a" class="h1" style="opacity:0">a <span class="hl">furry leftover</span></div>
  <div id="ou-b" class="h1" style="opacity:0">…and maybe a <span class="red">hair helper</span></div>
  <div id="ou-c" style="opacity:0"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", f"""
pop("#ou-a", {tlf:.2f}); rise("#ou-b", {thh-0.3:.2f});
tl.to("#ou-a, #ou-b", {{opacity:0, y:-30, duration:0.25, ease:"power2.in"}}, {tsc2-0.3:.2f});
pop("#ou-c", {tsc2:.2f});
""", fade=False)

# === GESTURES ===
think(g("hook", "Why do we"), SC["guess"]["start"] + 0.2)
point(g("guess", "keep us warm"), 3.0)
wave(g("intro", "I'm Max"))
point(g("muscle", "stands up"), 1.2)
point(g("nerve", "same switch"), 1.2)
wow(g("fur", "look bigger"), 1.3)
think(g("us", "lost most"), g("us", "barely keep"))
wow(g("twist", "stem cells"), 1.4)
point(g("mice", "two weeks"), 1.2)
wave(g("outro", "Stay curious"), 2)
# === SFX ===
sfx += [("sparkle.mp3", A("hook", "tiny bumps"), 0.4), ("ping.mp3", A("hook", "Why do we"), 0.35),
        ("pop.mp3", A("guess", "keep us warm"), 0.5), ("pop.mp3", A("guess", "scare enemies"), 0.5), ("pop.mp3", A("guess", "just a leftover"), 0.55),
        ("sparkle.mp3", A("intro", "Max Wise"), 0.4), ("click.mp3", A("muscle", "stands up"), 0.5), ("pop.mp3", A("muscle", "into a bump"), 0.5),
        ("click-soft.mp3", A("nerve", "same switch"), 0.55), ("whoosh-short.mp3", A("fur", "traps"), 0.4), ("pop.mp3", A("fur", "look bigger"), 0.5),
        ("click.mp3", A("us", "barely keep"), 0.45), ("impact-bass-1.mp3", A("twist", "stem cells"), 0.4),
        ("ping.mp3", A("mice", "two weeks"), 0.4), ("sparkle.mp3", A("outro", "Stay curious"), 0.45)]
