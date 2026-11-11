# MAX WISE ep45 — Who has more bones, a newborn baby or you?
# Kit: ink / morph / along helpers; no three.js (pure doodles).
# Sources: Cleveland Clinic (newborn ~270–300 bones, adult 206, fontanelles close in 1–2 years, 106 bones in hands+feet);
#  NCBI StatPearls Sacral Vertebrae (5 vertebrae fuse into the sacrum, finished by 25–30).
# === SCENES ===
import math as _m, random as _r
def J(src, **kw):
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
BONE = "#F3E6C8"; CART = "#BFE3F7"
WSF = WS.replace('fill="none" ', '')
def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.92)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 26px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff;white-space:nowrap">{txt}</span></div>')
def stamp(idn, txt, left, top, rot=-8, size=60, col=None):
    col = col or C['red']
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;{GH}font-size:{size}px;color:{col};'
            f'border:5px solid {col};padding:0 20px;border-radius:12px;background:#FFFFFF;transform:rotate({rot}deg);white-space:nowrap">{txt}</span></div>')
def bone_d(L, w):
    """one closed sub-path bone outline centred at 0,0 (knobby ends)"""
    r = w * 1.7
    return f"M{-L/2:.1f},{-w:.1f} L{L/2:.1f},{-w:.1f} A{r:.1f},{r:.1f} 0 1 1 {L/2:.1f},{w:.1f} L{-L/2:.1f},{w:.1f} A{r:.1f},{r:.1f} 0 1 1 {-L/2:.1f},{-w:.1f} Z"
def bone(idn, x, y, L, w, ang=0, cls="", fill=BONE, sw=5):
    c = f' class="{cls}"' if cls else ""
    i = f' id="{idn}"' if idn else ""
    return f'<path{i}{c} d="{bone_d(L, w)}" transform="translate({x},{y}) rotate({ang})" fill="{fill}" stroke="{K}" stroke-width="{sw}" stroke-linejoin="round"/>'

# 1 HOOK — baby vs grown-up ink themselves
s = "hook"; tbb = aw(s, "newborn baby"); tyo = aw(s, "or you"); tmb = aw(s, "more bones")
baby = (f'<path class="hk-b" d="M300,560 C230,560 200,640 210,720 C220,800 380,800 390,720 C400,640 370,560 300,560 Z" fill="#FFC9C2" {WSF}/>'
        f'<path class="hk-b" d="M300,460 C350,460 360,500 360,520 C360,560 330,580 300,580 C270,580 240,560 240,520 C240,500 250,460 300,460 Z" fill="#FFFFFF" {WSF}/>'
        f'<path class="hk-b" d="M268,515 Q278,525 288,515" {WS}/><path class="hk-b" d="M312,515 Q322,525 332,515" {WS}/>'
        f'<path class="hk-b" d="M290,545 Q300,552 310,545" {WS}/><path class="hk-b" d="M240,640 Q300,610 360,640" {WS}/>')
grown = (f'<circle cx="780" cy="410" r="56" fill="#FFFFFF" stroke="{K}" stroke-width="6" class="hk-a"/>'
         f'<path class="hk-a" d="M780,466 L780,660" {WS} stroke-width="7"/><path class="hk-a" d="M780,520 L700,610" {WS}/><path class="hk-a" d="M780,520 L860,610" {WS}/>'
         f'<path class="hk-a" d="M780,660 L720,800" {WS}/><path class="hk-a" d="M780,660 L840,800" {WS}/>'
         f'<path class="hk-a" d="M760,400 L762,402" {WS}/><path class="hk-a" d="M800,400 L802,402" {WS}/><path class="hk-a" d="M765,430 Q780,440 795,430" {WS}/>')
scenes[s] = scene_file(s, f"""
#hk-q {{ top:150px; font-size:76px; }}
#hk-vs {{ position:absolute; left:470px; top:560px; {GH} font-size:110px; color:{C['red']}; opacity:0; }}
#hk-l1 {{ position:absolute; left:190px; top:830px; width:220px; text-align:center; {GH} font-size:52px; opacity:0; }}
#hk-l2 {{ position:absolute; left:670px; top:830px; width:220px; text-align:center; {GH} font-size:52px; opacity:0; }}
""", f"""
  <div id="hk-q" class="h1" style="opacity:0">Who has <span class="hl">more bones</span>?</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>{baby}{grown}</svg>
  <div id="hk-vs">VS</div>
  <div id="hk-l1">baby</div><div id="hk-l2">you</div>
""", J("""
rise("#hk-q", @tq);
ink(".hk-b", @tb, 0.8, {stagger:0.1}); tl.fromTo("#hk-l1", {opacity:0}, {opacity:1, duration:0.2}, @tb2);
pop("#hk-vs", @tv, {from:{rotation:-25, scale:2}, to:{rotation:-6}});
ink(".hk-a", @ty, 0.7, {stagger:0.06}); tl.fromTo("#hk-l2", {opacity:0}, {opacity:1, duration:0.2}, @ty2);
""", tq=max(0.0, tmb - 2.2), tb=tbb - 0.15, tb2=tbb + 0.5, tv=tyo - 0.35, ty=tyo - 0.05, ty2=tyo + 0.4))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "the baby"); t2 = aw(s, "you"); t3 = aw(s, "exactly the same")
notes = [("a", "The baby?", -6, 110, C['hi'], 66), ("b", "You?", 4, 405, "#BFE3F7", 80), ("c", "Same?", -3, 700, "#FFC9C2", 76)]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:380px;width:275px;height:280px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:{fs}px;line-height:1.05;padding-top:95px">{txt}</div>' for k, txt, r, x, bg, fs in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}}); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.05, t2=t2 - 0.05, t3=t3 - 0.1))

# 3 INTRO — logo, underline + a bone inks itself (Max centre: keep y < 620)
s = "intro"; tmw = aw(s, "Max Wise"); tct = aw(s, "count some")
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:400px; font-size:66px; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="620" data-layout-ignore>
    <path id="in-ul" d="M190,350 Q540,336 890,348" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    {bone("in-bn", 540, 555, 220, 18, -6)}
  </svg>
  <div id="in-sub" class="h1"><span class="hl">Let's count bones!</span></div>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
rise("#in-sub", @tct); ink("#in-bn", @tb, 0.6);
""", tmw=tmw, tu=tmw + 0.3, tct=tct - 0.2, tb=tct + 0.1))

# 4 ADULT — 206 tiny bones fill a grid, counter runs
s = "adult"; tgu = aw(s, "skeleton"); t206 = aw(s, "two hundred and six")
cols, rows = 16, 13; gx0, gy0, dx, dy = 135, 330, 54, 36
rs = _r.Random(45)
grid = "".join(bone(None, gx0 + (i % cols) * dx, gy0 + (i // cols) * dy, 22, 3.6, rs.uniform(-25, 25), "ad-b", BONE, 3) for i in range(206))
scenes[s] = scene_file(s, f"""
#ad-title {{ top:150px; font-size:74px; }}
#ad-cnt {{ position:absolute; left:0; right:0; top:800px; text-align:center; }}
#ad-cnt .big {{ font-size:120px; color:{C['blue']}; }}
""", f"""
  <div id="ad-title" class="h1">A grown-up <span class="hl">skeleton</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="800" viewBox="0 0 {W} 800" data-layout-ignore>{grid}</svg>
  <div id="ad-cnt"><span id="ad-n" class="big">0</span><span style="font-size:56px"> bones</span></div>
""", J("""
rise("#ad-title", 0.0); pop("#ad-cnt", @tc0);
tl.fromTo(".ad-b", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.12, stagger:@stg}, @tc0);
count("#ad-n", 0, 206, @tc0, @dc, v => String(Math.round(v)));
tl.fromTo("#ad-n", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1}, @t206e);
""", tc0=tgu - 0.1, stg=(t206 + 0.9 - tgu) / 206, dc=t206 + 1.0 - tgu, t206e=t206 + 1.0))

# 5 BABY — number line: adult 206, baby band 270–300, stamp
s = "baby"; tnb = aw(s, "newborn"); t270 = aw(s, "two hundred and seventy"); t300 = aw(s, "three hundred"); tbw = aw(s, "baby wins")
X0, X1, Y = 110, 990, 560
def nx(v): return X0 + (X1 - X0) * v / 320
ticks = "".join(f'<path d="M{nx(v):.1f},{Y-(24 if v%100==0 else 12)} L{nx(v):.1f},{Y}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
                (f'<text x="{nx(v):.1f}" y="{Y+50}" text-anchor="middle" font-family="Patrick Hand" font-size="38" fill="{K}">{v}</text>' if v % 100 == 0 else "") for v in range(0, 321, 20))
scenes[s] = scene_file(s, f"""
#bb-title {{ top:150px; font-size:74px; }}
#bb-ad {{ position:absolute; left:{nx(206)-150:.0f}px; top:300px; width:300px; text-align:center; {GH} font-size:52px; color:{C['blue']}; opacity:0; }}
#bb-bl {{ position:absolute; left:{nx(285)-270:.0f}px; top:640px; width:420px; text-align:center; opacity:0; }}
#bb-bl .big {{ font-size:84px; color:{C['red']}; }}
""", f"""
  <div id="bb-title" class="h1">A <span class="hl">newborn</span> starts with…</div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <path id="bb-ax" d="M{X0},{Y} L{X1},{Y}" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>{ticks}
    <rect id="bb-band" x="{nx(270):.1f}" y="{Y-70}" width="{nx(300)-nx(270):.1f}" height="70" fill="#FFC9C2" stroke="{C['red']}" stroke-width="5"/>
    <path id="bb-adm" d="M{nx(206):.1f},{Y-140} L{nx(206):.1f},{Y-4}" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path id="bb-adh" d="M{nx(206)-18:.1f},{Y-30} L{nx(206):.1f},{Y-4} L{nx(206)+18:.1f},{Y-30}" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="bb-ad">you: 206</div>
  <div id="bb-bl"><div class="big"><span id="bb-n">270</span></div><div style="font-size:46px">newborn baby</div></div>
  {stamp("bb-st", "BABY WINS!", 150, 680, -8, 64)}
""", J("""
rise("#bb-title", @tnb); ink("#bb-ax", 0.1, 0.5);
ink("#bb-adm", 0.4, 0.4); ink("#bb-adh", 0.75, 0.2); tl.fromTo("#bb-ad", {opacity:0}, {opacity:1, duration:0.25}, 0.5);
tl.fromTo("#bb-band", {scaleX:0, svgOrigin:"@bx @by"}, {scaleX:1, duration:0.8, ease:"power2.out"}, @t270);
pop("#bb-bl", @t270);
tl.set("#bb-n", {textContent:"270–300"}, @t300m); tl.fromTo("#bb-n", {scale:1}, {scale:1.15, duration:0.15, yoyo:true, repeat:1}, @t300m);
pop("#bb-st", @tbw, {from:{rotation:-25, scale:1.8}, to:{rotation:-8}});
""", tnb=tnb - 0.4, t270=t270, bx=f"{nx(270):.0f}", by=Y, t300m=t300, tbw=tbw - 0.1))

# 6 SOFT — cut-away baby bone: middle hard, blue hatched cartilage ends; nose tip
s = "soft"; tsc = aw(s, "soft cartilage"); tns = aw(s, "tip of your nose"); tbd = aw(s, "bend and grow")
hatch = "".join(f'<path d="M{x},{300} L{x+40},{420}" stroke="{C["blue"]}" stroke-width="3"/>' for x in range(150, 330, 18)) + \
        "".join(f'<path d="M{x},{300} L{x+40},{420}" stroke="{C["blue"]}" stroke-width="3"/>' for x in range(730, 910, 18))
scenes[s] = scene_file(s, f"""
#sf-title {{ top:150px; font-size:74px; }}
#sf-nose {{ position:absolute; left:560px; top:560px; }}
#sf-gr {{ position:absolute; left:0; top:0; }}
""", f"""
  <div id="sf-title" class="h1">Still <span class="hl">soft</span> inside</div>
  <svg id="sf-gr" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <defs><clipPath id="sf-cl"><path d="M150,300 L330,300 L330,420 L150,420 Z M750,300 L930,300 L930,420 L750,420 Z"/></clipPath></defs>
    <g id="sf-bone">
      <path d="M200,330 L880,330 A70,70 0 1 1 880,390 L200,390 A70,70 0 1 1 200,330 Z" fill="{BONE}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
      <g id="sf-cart" opacity="0"><path d="M200,330 L300,330 L300,390 L200,390 A70,70 0 1 1 200,330 Z M880,330 L780,330 L780,390 L880,390 A70,70 0 1 1 880,330 Z" fill="{CART}" stroke="{C['blue']}" stroke-width="5"/>
        <g clip-path="url(#sf-cl)">{hatch}</g></g>
      <path id="sf-cut" d="M120,360 L960,360" stroke="{C['red']}" stroke-width="4" stroke-dasharray="14 10" fill="none"/>
    </g>
  </svg>
  {tape("sf-t1", "soft cartilage", 90, 460, -4, 46, "rgba(191,227,247,.95)")}
  {tape("sf-t2", "bone", 470, 230, 3, 46)}
  <svg id="sf-nose" width="400" height="300" viewBox="0 0 200 150" data-layout-ignore style="opacity:0">
    <path class="sf-n" d="M70,10 C80,60 60,90 40,105 C30,115 40,130 60,128" {WS}/>
    <path class="sf-n" d="M60,128 C80,135 95,128 100,118" {WS}/>
    <circle cx="48" cy="112" r="16" fill="{CART}" stroke="{C['blue']}" stroke-width="4"/>
    <text x="78" y="70" font-family="Gochi Hand" font-size="26" fill="{C['blue']}">squishy!</text>
  </svg>
  {tape("sf-t3", "bend + grow", 600, 840, -3, 46, "rgba(255,201,194,.95)")}
""", J("""
rise("#sf-title", 0.0); tl.fromTo("#sf-bone", {opacity:0}, {opacity:1, duration:0.3}, 0.15); ink("#sf-cut", 0.5, 0.6); rise("#sf-t2", 0.8);
tl.to("#sf-cart", {opacity:1, duration:0.4}, @tsc); rise("#sf-t1", @tsc2);
tl.to("#sf-nose", {opacity:1, duration:0.2}, @tns); ink(".sf-n", @tns, 0.6, {stagger:0.2});
tl.fromTo("#sf-bone", {rotation:0, svgOrigin:"540 360"}, {rotation:-5, duration:0.3, yoyo:true, repeat:3, ease:"sine.inOut"}, @tbd);
rise("#sf-t3", @tbd);
""", tsc=tsc - 0.1, tsc2=tsc + 0.3, tns=tns - 0.1, tbd=tbd - 0.1))

# 7 SKULL — top view, plates with gaps + soft spot; gaps narrow, diamond morphs shut
s = "skull"; tsk = aw(s, "take the skull"); tpl = aw(s, "separate plates"); tsp = aw(s, "soft spots"); tcl = aw(s, "close up"); tyr = aw(s, "first year")
CX, CY = 540, 560
scenes[s] = scene_file(s, f"""
#sk-title {{ top:150px; font-size:74px; }}
#sk-wrap {{ position:absolute; left:0; top:0; transform-origin:540px 560px; }}
#sk-ch {{ position:absolute; left:760px; top:820px; opacity:0; }}
""", f"""
  <div id="sk-title" class="h1">Baby <span class="hl">skull</span>, from the top</div>
  <svg id="sk-wrap" width="{W}" height="980" viewBox="0 0 {W} 980" data-layout-ignore>
    <ellipse cx="{CX}" cy="{CY}" rx="230" ry="300" fill="{BONE}" stroke="{K}" stroke-width="7"/>
    <path id="sk-s1" d="M{CX},{CY-300} L{CX},{CY+300}" stroke="#FFFDF6" stroke-width="26" fill="none"/>
    <path id="sk-s2" d="M{CX-230},{CY-60} Q{CX},{CY-110} {CX+230},{CY-60}" stroke="#FFFDF6" stroke-width="26" fill="none"/>
    <path id="sk-s3" d="M{CX-190},{CY+170} Q{CX},{CY+120} {CX+190},{CY+170}" stroke="#FFFDF6" stroke-width="22" fill="none"/>
    <path id="sk-f" d="M{CX},{CY-170} L{CX+70},{CY-85} L{CX},{CY} L{CX-70},{CY-85} Z" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>
    <path id="sk-fz" d="M{CX},{CY-90} L{CX+3},{CY-87} L{CX},{CY-84} L{CX-3},{CY-87} Z" fill="none" stroke="none"/>
    <text x="{CX-230}" y="{CY-250}" font-family="Gochi Hand" font-size="40" fill="{C['muted']}">front</text>
  </svg>
  {tape("sk-t1", "separate plates", 50, 300, -4, 44)}
  {tape("sk-t2", "soft spot", 690, 380, 4, 44, "rgba(255,201,194,.95)")}
  <div id="sk-ch"><span class="pill" style="font-size:52px">1–2 years</span></div>
""", J("""
rise("#sk-title", @tsk); tl.fromTo("#sk-wrap", {opacity:0, scale:0.7}, {opacity:1, scale:1, duration:0.4, ease:"back.out(1.6)"}, @tsk);
rise("#sk-t1", @tpl); tl.fromTo("#sk-s1, #sk-s2, #sk-s3", {attr:{"stroke-width":26}}, {attr:{"stroke-width":34}, duration:0.2, yoyo:true, repeat:1}, @tpl);
pop("#sk-f", @tsp); rise("#sk-t2", @tsp2);
tl.to("#sk-s1, #sk-s2, #sk-s3", {attr:{"stroke-width":5}, stroke:"#262A3B", duration:1.0, ease:"power2.inOut"}, @tcl);
morph("#sk-f", "#sk-fz", @tcl, 1.0); tl.to("#sk-t2", {opacity:0, duration:0.3}, @tcl2);
pop("#sk-ch", @tyr);
""", tsk=tsk - 0.1, tpl=tpl - 0.1, tsp=tsp - 0.1, tsp2=tsp + 0.2, tcl=tcl - 0.1, tcl2=tcl + 0.6, tyr=tyr - 0.1))

# 8 FUSE — spine side view; five sacral blocks morph into one sacrum
s = "fuse"; tgr = aw(s, "as you grow"); tjn = aw(s, "join into"); tfv = aw(s, "five little"); tsg = aw(s, "single bone"); tsa = aw(s, "sacrum")
SX = 620
lumb = "".join(f'<path class="fu-l" d="M{SX-60},{250+i*62} L{SX+60},{250+i*62} L{SX+60},{296+i*62} L{SX-60},{296+i*62} Z" fill="{BONE}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>' for i in range(4))
sac = []
for i in range(5):
    w = 56 - i * 9; y = 510 + i * 54
    sac.append(f'<path id="fu-s{i}" d="M{SX-w},{y} L{SX+w},{y} L{SX+w-4},{y+44} L{SX-w+4},{y+44} Z" fill="{BONE}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>')
SAC = f"M{SX-66},{510} L{SX+66},{510} L{SX+20},{770} L{SX-20},{770} Z"
scenes[s] = scene_file(s, f"""
#fu-title {{ top:150px; font-size:72px; }}
#fu-ch {{ position:absolute; left:120px; top:560px; opacity:0; }}
#fu-ch .big {{ font-size:110px; }}
""", f"""
  <div id="fu-title" class="h1">Small bones <span class="hl">join up</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {lumb}{''.join(sac)}
    <path id="fu-sac" d="{SAC}" fill="none" stroke="none"/>
    <path id="fu-br" d="M{SX+90},{510} Q{SX+130},{640} {SX+90},{770}" stroke="{C['red']}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="fu-ch"><span class="big"><span id="fu-n" class="red">5</span> → 1</span></div>
  {tape("fu-t1", "sacrum", 760, 610, 4, 52)}
""", J("""
rise("#fu-title", @tgr);
tl.fromTo(".fu-l", {opacity:0, x:-40}, {opacity:1, x:0, duration:0.25, stagger:0.08}, @tgr2);
for (let i=0;i<5;i++) pop("#fu-s"+i, @tfv + i*0.12);
ink("#fu-br", @tfv2, 0.4); pop("#fu-ch", @tfv2);
for (let i=0;i<5;i++) morph("#fu-s"+i, "#fu-sac", @tsg, 0.8);
tl.to("#fu-s0, #fu-s1, #fu-s2, #fu-s3, #fu-s4", {fill:"#FFE27A", duration:0.4}, @tsg2);
rise("#fu-t1", @tsa);
""", tgr=tgr - 0.1, tgr2=tjn - 0.2, tfv=tfv - 0.1, tfv2=tfv + 0.7, tsg=tsg - 0.2, tsg2=tsg + 0.6, tsa=tsa - 0.1))

# 9 TIME — age ruler, glue drop rides along to the 20s band
s = "time"; tjg = aw(s, "joining"); ttw = aw(s, "twenties")
RX0, RX1, RY = 120, 980, 560
def rx(a): return RX0 + (RX1 - RX0) * a / 30
rt = "".join(f'<path d="M{rx(a):.1f},{RY-(26 if a%10==0 else 14)} L{rx(a):.1f},{RY}" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' +
             (f'<text x="{rx(a):.1f}" y="{RY+52}" text-anchor="middle" font-family="Patrick Hand" font-size="40" fill="{K}">{a}</text>' if a % 10 == 0 else "") for a in range(0, 31, 2))
scenes[s] = scene_file(s, f"""
#tm-title {{ top:150px; font-size:72px; }}
""", f"""
  <div id="tm-title" class="h1">Still joining… <span class="hl">for years</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    <rect id="tm-band" x="{rx(20):.1f}" y="{RY-110}" width="{rx(30)-rx(20):.1f}" height="110" fill="#FFE27A" opacity="0"/>
    <path d="M{RX0},{RY} L{RX1},{RY}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>{rt}
    <text x="{RX1}" y="{RY+100}" text-anchor="end" font-family="Gochi Hand" font-size="40" fill="{C['muted']}">age (years)</text>
    <path id="tm-p" d="M{RX0},{RY-40} Q{rx(8):.0f},{RY-150} {rx(14):.0f},{RY-60} T{rx(25):.0f},{RY-50}" stroke="{C['pencil']}" stroke-width="4" stroke-dasharray="10 12" fill="none"/>
    <g id="tm-drop"><path d="M0,-30 Q22,0 0,18 Q-22,0 0,-30 Z" fill="#BFE3F7" stroke="{K}" stroke-width="4"/></g>
    <text id="tm-lab" x="{rx(25):.0f}" y="{RY-130}" text-anchor="middle" font-family="Gochi Hand" font-size="56" fill="{C['red']}" opacity="0">your 20s</text>
  </svg>
""", J("""
rise("#tm-title", 0.0); ink("#tm-p", 0.2, 0.6);
tl.set("#tm-drop", {x:@x0, y:@y0}, 0);
along("#tm-drop", "#tm-p", @tj, @dj, {ease:"power1.inOut"});
tl.to("#tm-band", {opacity:0.8, duration:0.3}, @ttw); pop("#tm-lab", @ttw);
""", x0=RX0, y0=RY - 40, tj=tjg - 0.2, dj=ttw - tjg + 0.4, ttw=ttw - 0.1))

# 10 HANDS — hand + foot ink themselves; bar 106 of 206 past the ½ line
s = "hands"; tbn = aw(s, "a bonus"); thf = aw(s, "more than half"); tht = aw(s, "hands and feet"); t106 = aw(s, "one hundred and six")
hand = [f"M150,560 C140,480 150,420 170,400", "M170,400 L160,290", "M200,395 L200,270", "M235,398 L245,280", "M265,410 L290,315",
        "M150,520 L95,450", "M150,560 C180,600 260,600 280,540 L290,420"]
foot = ["M760,330 C740,420 740,500 770,560", "M770,560 C810,600 920,600 940,560 C960,520 900,500 860,480 C840,440 830,380 820,330",
        "M890,505 L900,480", "M915,520 L928,498", "M935,540 L950,520"]
hp = "".join(f'<path class="hn-h" d="{d}" {WS} stroke-width="6"/>' for d in hand)
fp = "".join(f'<path class="hn-f" d="{d}" {WS} stroke-width="6"/>' for d in foot)
BX0, BX1, BY = 120, 960, 700
bw106 = (BX1 - BX0) * 106 / 206
scenes[s] = scene_file(s, f"""
#hn-title {{ top:150px; font-size:72px; }}
#hn-n {{ position:absolute; left:420px; top:780px; opacity:0; }}
#hn-n .big {{ font-size:96px; color:{C['red']}; }}
""", f"""
  <div id="hn-title" class="h1">Bonus: <span class="hl">hands + feet</span></div>
  <svg class="abs" style="left:0;top:0" width="{W}" height="900" viewBox="0 0 {W} 900" data-layout-ignore>
    {hp}{fp}
    <rect x="{BX0}" y="{BY-40}" width="{BX1-BX0}" height="70" fill="#FFFFFF" stroke="{K}" stroke-width="5"/>
    <rect id="hn-fill" x="{BX0}" y="{BY-40}" width="{bw106:.1f}" height="70" fill="#FFE27A" stroke="{K}" stroke-width="5"/>
    <path id="hn-half" d="M{(BX0+BX1)/2:.0f},{BY-75} L{(BX0+BX1)/2:.0f},{BY+60}" stroke="{C['red']}" stroke-width="6" stroke-dasharray="12 9" fill="none"/>
    <text x="{(BX0+BX1)/2:.0f}" y="{BY-90}" text-anchor="middle" font-family="Gochi Hand" font-size="48" fill="{C['red']}">½</text>
  </svg>
  <div id="hn-n"><span class="big">106</span><span style="font-size:48px"> in hands + feet!</span></div>
""", J("""
rise("#hn-title", @tbn); ink(".hn-h", @tht, 0.7, {stagger:0.06}); ink(".hn-f", @tht2, 0.7, {stagger:0.06});
ink("#hn-half", @thf, 0.4);
tl.fromTo("#hn-fill", {scaleX:0, svgOrigin:"@hx @hy"}, {scaleX:1, duration:1.0, ease:"power2.out"}, @thf2);
pop("#hn-n", @t106);
""", tbn=tbn - 0.1, tht=max(tbn + 0.4, thf - 0.3), tht2=max(tbn + 0.9, thf + 0.2), thf=thf - 0.1, thf2=thf + 0.3, hx=BX0, hy=BY, t106=t106 - 0.1))

# 11 OUTRO — recap chips, stamp, Stay curious (Max centre: keep y < 620)
s = "outro"; tmb = aw(s, "more bones"); tst = aw(s, "stronger"); tsc = aw(s, "stay curious")
scenes[s] = scene_file(s, f"""
#ou-a {{ position:absolute; left:60px; top:170px; width:440px; text-align:center; }}
#ou-b {{ position:absolute; left:580px; top:170px; width:440px; text-align:center; }}
#ou-a .big, #ou-b .big {{ font-size:84px; }}
#ou-c {{ position:absolute; left:0; right:0; top:180px; text-align:center; }}
#ou-c .big {{ font-size:110px; }}
""", f"""
  <div id="ou-a"><div style="font-size:48px">baby</div><div class="big red">≈ 270–300</div></div>
  <div id="ou-b"><div style="font-size:48px">you</div><div class="big blue">206</div></div>
  {stamp("ou-st", "fewer, stronger!", 300, 420, -6, 64)}
  <div id="ou-c"><div class="big">Stay curious!</div><div style="margin-top:22px"><span class="chip">MAX WISE</span></div></div>
""", J("""
pop("#ou-a", @ta); pop("#ou-b", @tb); pop("#ou-st", @tst, {from:{rotation:-25, scale:1.8}, to:{rotation:-6}});
tl.to("#ou-a, #ou-b, #ou-st", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tout);
pop("#ou-c", @tsc);
""", ta=tmb - 0.2, tb=tmb + 0.2, tst=tst - 0.1, tout=tsc - 0.3, tsc=tsc), fade=False)

# === GESTURES ===
think(g("hook", "here's"), SC["guess"]["start"] + 0.2)
point(g("guess", "the baby"), 2.4)
wave(g("intro", "I'm Max"))
point(g("adult", "two hundred and six"), 1.2)
wow(g("baby", "baby wins"), 1.3)
point(g("soft", "soft cartilage"), 1.2)
point(g("skull", "soft spots"), 1.2)
wow(g("fuse", "single bone"), 1.3)
think(SC["time"]["start"] + 0.05, g("time", "twenties"))
wow(g("hands", "one hundred and six"), 1.3)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("ping.mp3", A("hook", "more bones"), 0.35), ("pop.mp3", A("guess", "the baby"), 0.5), ("pop.mp3", A("guess", "you"), 0.5),
        ("pop.mp3", A("guess", "exactly the same"), 0.55), ("sparkle.mp3", A("intro", "Max Wise"), 0.4),
        ("click-soft.mp3", A("adult", "two hundred and six") + 1.0, 0.6), ("impact-bass-1.mp3", A("baby", "baby wins"), 0.45),
        ("click.mp3", A("skull", "close up"), 0.4), ("riser.mp3", A("fuse", "five little"), 0.3), ("impact-bass-2.mp3", A("fuse", "single bone"), 0.45),
        ("pop.mp3", A("hands", "one hundred and six"), 0.55), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
