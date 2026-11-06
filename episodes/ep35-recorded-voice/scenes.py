# MAX WISE ep35 — Why does your voice sound so weird on a recording?
# Kit: ink / morph / along helpers; 2D only (no three.js). Source: Scientific American, "Why does my voice sound so different
# when it is recorded and played back?" — two routes to the cochlea (air conduction via ear canal + eardrum, bone conduction
# through the skull), bone conduction boosts low frequencies, a mic only catches the air route; plugged ears + humming = mostly bone.
# Qualitative only (no Hz / dB numbers).
# === SCENES ===
import math, random
def J(src, **kw):
    """plain JS with @name placeholders (no brace doubling); longest names first"""
    for k, v in sorted(kw.items(), key=lambda kv: -len(kv[0])): src = src.replace("@" + k, f"{v:.3f}" if isinstance(v, float) else str(v))
    return src
GH = "font-family:'Gochi Hand',cursive;"
SKIN = "#FCE3D2"; HAIR = "#6B4E3D"; AIR = "#BFE3F7"; DRUM = "#E88A9A"; LIGHT = "#FFF3EC"; SHELL = "#F4D9A6"; BONE = "#EFE4CC"

AIRP = "M590,690 C680,760 800,800 880,720 C940,660 920,560 850,540 L748,540"
BONEP = "M540,860 C556,780 640,770 676,700 C705,640 702,590 695,566"
FACE = "M540,240 C700,240 772,370 770,520 C768,690 680,800 540,800 C400,800 312,690 310,520 C308,370 380,240 540,240 Z"
SKULL = "M540,262 C686,262 748,380 748,520 C746,676 666,778 540,778 C414,778 334,676 332,520 C332,380 394,262 540,262 Z"
M_OPEN = "M490,680 Q540,700 590,680 Q540,730 490,680 Z"
M_SHUT = "M492,684 Q540,694 588,684 Q540,698 492,684 Z"

def wave(x0, x1, y, cyc, amp, n=120, harm=0.0, seed=None, env=False):
    rnd = random.Random(seed) if seed is not None else None
    pts = []
    for i in range(n + 1):
        u = i / n; x = x0 + (x1 - x0) * u
        a = amp * (math.sin(math.pi * u) ** 0.6 if env else 1.0)
        v = math.sin(2 * math.pi * cyc * u) + harm * math.sin(2 * math.pi * cyc * 2 * u + 0.6)
        if rnd: v *= 0.4 + 0.9 * rnd.random()
        pts.append(f"{x:.1f},{y - a * v:.1f}")
    return "M" + " L".join(pts)

def head(p, air=True, bone=True, air_op=1.0, bone_op=1.0, hands=False, mouth=M_OPEN, skull=False):
    """front-view doodle head: face, hair, ears, ear canal + eardrum (#p-drum), cochlea (#p-coch) inside the right ear,
    blue air road (#p-air, outside) and red bone road (#p-bone, inside), vocal cords (#p-vc) in the neck"""
    o = (f'<path d="M480,790 L476,940 M600,790 L604,940" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
         f'<path d="M480,800 L600,800 L603,935 L477,935 Z" fill="{SKIN}"/>'
         f'<path d="M440,942 Q540,962 640,942" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>'
         f'<path d="M310,470 Q235,450 238,545 Q242,625 310,610 Z" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
         f'<path d="M770,470 Q845,450 842,545 Q838,625 770,610 Z" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>'
         f'<path d="{FACE}" fill="{SKIN}" stroke="{K}" stroke-width="7" stroke-linejoin="round"/>')
    if skull:
        o += (f'<defs><pattern id="{p}-hp" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
              f'<rect width="14" height="14" fill="{BONE}"/><rect width="5" height="14" fill="#C9B48C"/></pattern></defs>'
              f'<path id="{p}-skull" d="{SKULL}" stroke="url(#{p}-hp)" stroke-width="24" fill="none"/>')
    o += (f'<path d="M318,440 C310,270 440,222 540,224 C650,222 772,272 762,440 C730,340 650,316 560,330 C470,312 360,340 318,440 Z" fill="{HAIR}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
          f'<circle cx="455" cy="475" r="14" fill="{K}"/><circle cx="625" cy="475" r="14" fill="{K}"/>'
          f'<path d="M425,438 Q455,425 485,438 M595,438 Q625,425 655,438" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>'
          f'<path d="M545,505 Q518,585 552,592" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>'
          f'<path id="{p}-mouth" d="{mouth}" fill="#B5414A" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>'
          f'<path d="M812,540 L748,540" stroke="{K}" stroke-width="24" stroke-linecap="round" opacity=".8"/>'
          f'<path d="M810,540 L752,540" stroke="{LIGHT}" stroke-width="14" stroke-linecap="round"/>'
          f'<path id="{p}-drum" d="M742,520 L742,560" stroke="{DRUM}" stroke-width="10" stroke-linecap="round"/>'
          f'<circle cx="695" cy="540" r="32" fill="{SHELL}"/>'
          f'<path id="{p}-coch" d="M669,540 a26,26 0 1,1 52,0 a20,20 0 1,1 -40,0 a12,12 0 1,1 24,0" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>'
          f'<path id="{p}-vc" d="M520,856 Q540,848 560,856 M520,870 Q540,878 560,870" stroke="{C["red"]}" stroke-width="6" fill="none" stroke-linecap="round"/>')
    if air: o += f'<path id="{p}-air" d="{AIRP}" stroke="{C["blue"]}" stroke-width="11" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="{air_op}"/>'
    if bone: o += f'<path id="{p}-bone" d="{BONEP}" stroke="{C["red"]}" stroke-width="12" fill="none" stroke-linecap="round" opacity="{bone_op}"/>'
    if hands:
        for sx in (1, -1):
            cx = 540 + sx * 300
            o += (f'<g class="{p}-hand"><ellipse cx="{cx}" cy="545" rx="56" ry="92" fill="{SKIN}" stroke="{K}" stroke-width="7"/>'
                  f'<path d="M{cx - 22},480 L{cx - 22},600 M{cx},468 L{cx},610 M{cx + 22},480 L{cx + 22},600" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".55"/></g>')
    return o

def tape(idn, txt, left, top, rot=-3, size=46, bg="rgba(255,226,122,.92)"):
    return (f'<div id="{idn}" class="abs" style="left:{left}px;top:{top}px;opacity:0"><span style="display:inline-block;padding:4px 24px;background:{bg};'
            f'{GH}font-size:{size}px;transform:rotate({rot}deg);border-left:6px dashed #fff;border-right:6px dashed #fff">{txt}</span></div>')

def phone(p, x, y, w=260, h=420):
    cx = x + w / 2; cy = y + h * 0.42
    return (f'<g id="{p}-ph"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="#FFFFFF" stroke="{K}" stroke-width="8"/>'
            f'<rect x="{x + 20}" y="{y + 40}" width="{w - 40}" height="{h - 100}" rx="14" fill="{AIR}" stroke="{K}" stroke-width="4"/>'
            f'<path d="M{cx - 30},{cy - 42} L{cx + 44},{cy} L{cx - 30},{cy + 42} Z" fill="{C["red"]}" stroke="{K}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M{x + 44},{y + h - 100} L{x + w - 44},{y + h - 100}" stroke="{K}" stroke-width="5" stroke-linecap="round" opacity=".4"/>'
            f'<path id="{p}-prog" d="M{x + 44},{y + h - 100} L{x + w - 44},{y + h - 100}" stroke="{C["red"]}" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="{y + h - 32}" r="13" fill="none" stroke="{K}" stroke-width="4"/></g>')

# 1 HOOK — a phone plays a recording; a weird jagged wave inks out of it; "huh?!"
s = "hook"; twh = aw(s, "why does"); twe = aw(s, "weird"); tre = aw(s, "recording")
HKW = wave(700, 1010, 690, 7, 70, 90, seed=7, env=True)
scenes[s] = scene_file(s, f"""
#hk-svg {{ position:absolute; left:0; top:0; }}
#hk-q {{ top:160px; font-size:84px; line-height:1.08; opacity:0; }}
#hk-huh {{ position:absolute; left:100px; top:600px; {GH} font-size:120px; color:{C['red']}; opacity:0; }}
#hk-ph {{ opacity:0; }}
""", f"""
  <svg id="hk-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {phone("hk", 420, 470)}
    <path id="hk-w" d="{HKW}" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="hk-q" class="h1">Why does your voice sound so <span class="hl">weird</span> on a recording?</div>
  <div id="hk-huh">huh?!</div>
""", J("""
tl.fromTo("#hk-ph", {opacity:0, scale:0.6, svgOrigin:"550 680"}, {opacity:1, scale:1, svgOrigin:"550 680", duration:0.4, ease:"back.out(2)"}, 0.05);
ink("#hk-prog", 0.3, @dp, {ease:"none"});
tl.set("#hk-q", {opacity:1}, @tw); rise("#hk-q", @tw);
ink("#hk-w", @tr, 0.8, {ease:"power1.out"});
tl.set("#hk-huh", {opacity:1}, @te); pop("#hk-huh", @te, {from:{rotation:-30, scale:1.8}, to:{rotation:-8}});
tl.fromTo("#hk-ph", {rotation:0, svgOrigin:"550 680"}, {rotation:4, svgOrigin:"550 680", duration:0.08, yoyo:true, repeat:5, immediateRender:false}, @te);
""", tw=twh - 0.1, te=twe, tr=tre - 0.3, dp=3.8))

# 2 GUESS — sticky notes
s = "guess"; tg = aw(s, "take a"); t1 = aw(s, "cheap"); t2 = aw(s, "nerves"); t3 = aw(s, "or something")
notes = [("a", "Cheap mic?", -6, 110, "#E6E6E6"), ("b", "Nerves?", 4, 405, "#FFC9C2"), ("c", "Your own head?", -3, 700, C['hi'])]
nh = "".join(f'<div id="gs-{k}" class="abs" style="left:{x}px;top:360px;width:275px;height:300px;background:{bg};border:4px solid {K};{SKETCH}transform:rotate({r}deg);text-align:center;{GH}font-size:58px;line-height:1.05;padding:80px 14px 0;box-sizing:border-box;opacity:0">{txt}</div>' for k, txt, r, x, bg in notes)
scenes[s] = scene_file(s, "", f"""
  <div id="gs-title" class="h1" style="top:170px">Take a guess!</div>
  {nh}
""", J("""
pop("#gs-title", @tg);
tl.set("#gs-a", {opacity:1}, @t1); pop("#gs-a", @t1, {from:{rotation:-20}, to:{rotation:-6}});
tl.set("#gs-b", {opacity:1}, @t2); pop("#gs-b", @t2, {from:{rotation:20}, to:{rotation:4}});
tl.set("#gs-c", {opacity:1}, @t3); pop("#gs-c", @t3, {from:{rotation:-20}, to:{rotation:-3}});
""", tg=tg, t1=t1 - 0.2, t2=t2 - 0.2, t3=t3))

# 3 INTRO — logo + underline + a wavy sound line inks itself (Max centre: keep y < 640)
s = "intro"; tmw = aw(s, "max wise"); tfo = aw(s, "follow")
INW = wave(200, 880, 70, 5, 28, 100, env=True)
scenes[s] = scene_file(s, f"""
#in-logo {{ position:absolute; left:0; right:0; top:170px; text-align:center; {GH} font-size:150px; line-height:1; }}
#in-sub {{ top:395px; font-size:62px; opacity:0; }}
""", f"""
  <div id="in-logo">MAX WISE</div>
  <svg class="abs" style="left:0;top:330px" width="{W}" height="60" data-layout-ignore>
    <path id="in-ul" d="M190,20 Q540,6 890,18" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>
  <div id="in-sub" class="h1"><span class="hl">Let's follow your voice</span></div>
  <svg class="abs" style="left:0;top:480px" width="{W}" height="140" data-layout-ignore>
    <path id="in-w" d="{INW}" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
""", J("""
pop("#in-logo", @tmw, {from:{scale:1.6}, to:{}}); ink("#in-ul", @tu, 0.4);
tl.set("#in-sub", {opacity:1}, @ts); rise("#in-sub", @ts);
ink("#in-w", @ts, 0.9, {ease:"power1.inOut"});
""", tmw=tmw, tu=tmw + 0.3, ts=tfo - 0.3))

# 4 ROADS — the head; the inner ear lights up; two roads ink themselves and meet at the cochlea
s = "roads"; tin = aw(s, "inner ear"); ttw = aw(s, "two different")
scenes[s] = scene_file(s, f"""
#rd-svg {{ position:absolute; left:0; top:0; }}
#rd-c {{ position:absolute; left:0; right:0; top:140px; text-align:center; opacity:0; }}
#rd-hd {{ opacity:0; }}
""", f"""
  <svg id="rd-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="rd-hd">{head("rd")}</g>
    <path id="rd-ld" d="M700,512 L760,380" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
  </svg>
  {tape("rd-t1", "inner ear", 730, 300, 4, 48)}
  <div id="rd-c"><span class="chip" style="background:#FFFFFF;font-size:56px;transform:rotate(-2deg)">2 roads in</span></div>
""", J("""
tl.fromTo("#rd-hd", {opacity:0, y:30}, {opacity:1, y:0, duration:0.4, ease:"power3.out"}, 0.0);
tl.fromTo("#rd-coch", {scale:1, svgOrigin:"695 540"}, {scale:1.4, svgOrigin:"695 540", duration:0.25, yoyo:true, repeat:1, immediateRender:false}, @ti);
ink("#rd-ld", @ti, 0.25); tl.set("#rd-t1", {opacity:1}, @ti); pop("#rd-t1 span", @ti, {from:{rotation:14}, to:{rotation:4}});
tl.set("#rd-c", {opacity:1}, @tt); pop("#rd-c .chip", @tt, {from:{rotation:-10, scale:1.4}, to:{rotation:-2}});
ink("#rd-air", @tt, 0.9); ink("#rd-bone", @tt2, 0.7);
""", ti=tin - 0.1, tt=ttw - 0.1, tt2=ttw + 0.3))

# 5 AIR — road one: sound dots ride the air road from the mouth into the ear canal and hit the eardrum
s = "air"; tai = aw(s, "the air"); tmo = aw(s, "mouth"); tfl = aw(s, "flies"); tca = aw(s, "ear canal"); tdr = aw(s, "eardrum")
NDOT = 8
dots = "".join(f'<circle id="ar-d{i}" cx="0" cy="0" r="12" fill="#FFFFFF" stroke="{C["blue"]}" stroke-width="5" opacity="0"/>' for i in range(NDOT))
arcs = "".join(f'<path class="ar-arc" d="M{600 + k * 22},{660 + k * 8} Q{620 + k * 26},{690 + k * 10} {598 + k * 22},{722 + k * 10}" stroke="{C["blue"]}" stroke-width="6" fill="none" stroke-linecap="round"/>' for k in range(3))
scenes[s] = scene_file(s, f"""
#ar-svg {{ position:absolute; left:0; top:0; }}
#ar-c {{ position:absolute; left:90px; top:140px; opacity:0; }}
""", f"""
  <svg id="ar-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {head("ar", bone_op=0.15)}
    <path id="ar-rt" d="{AIRP}" fill="none" stroke="none"/>
    {arcs}{dots}
    <path id="ar-l1" d="M830,530 L880,410" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path id="ar-l2" d="M742,562 L800,820" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="ar-c"><span class="chip" style="background:{AIR};font-size:54px;transform:rotate(-3deg)">road 1: air</span></div>
  {tape("ar-t1", "ear canal", 760, 330, 4, 46)}
  {tape("ar-t2", "eardrum", 720, 820, -3, 46, "rgba(232,138,154,.9)")}
""", J("""
tl.set("#ar-c", {opacity:1}, @ta); pop("#ar-c .chip", @ta, {from:{rotation:-12}, to:{rotation:-3}});
tl.fromTo("#ar-air", {opacity:0.25}, {opacity:1, duration:0.3}, @ta);
ink(".ar-arc", @tm, 0.3, {stagger:0.1});
tl.fromTo("#ar-mouth", {scaleY:1, svgOrigin:"540 690"}, {scaleY:0.5, svgOrigin:"540 690", duration:0.12, yoyo:true, repeat:5, immediateRender:false}, @tm);
ink("#ar-l1", @tc, 0.25); tl.set("#ar-t1", {opacity:1}, @tc); pop("#ar-t1 span", @tc, {from:{rotation:14}, to:{rotation:4}});
ink("#ar-l2", @td, 0.25); tl.set("#ar-t2", {opacity:1}, @td); pop("#ar-t2 span", @td, {from:{rotation:-14}, to:{rotation:-3}});
tl.fromTo("#ar-drum", {x:0}, {x:-6, duration:0.07, yoyo:true, repeat:7, immediateRender:false}, @td);
""", ta=tai - 0.1, tm=tmo - 0.1, tc=tca - 0.1, td=tdr - 0.1)
  + "".join(f'tl.set("#ar-d{i}", {{opacity:1}}, {tfl - 0.4 + i * 0.22:.3f}); along("#ar-d{i}", "#ar-rt", {tfl - 0.4 + i * 0.22:.3f}, 1.3, {{ease:"power1.inOut"}}); tl.to("#ar-d{i}", {{opacity:0, duration:0.12}}, {tfl + 0.88 + i * 0.22:.3f});\n' for i in range(NDOT)))

# 6 BONE — road two: the vocal cords buzz, the skull hatches in, red dots shoot up the bone road to the cochlea
s = "bone"; tsh = aw(s, "shortcut"); tvc = aw(s, "vocal cords"); tbo = aw(s, "bones of"); tbz = aw(s, "buzz"); tco = aw(s, "cochlea")
NB = 7
bdots = "".join(f'<circle id="bn-d{i}" cx="0" cy="0" r="11" fill="{C["red"]}" stroke="{K}" stroke-width="3" opacity="0"/>' for i in range(NB))
rings = "".join(f'<circle class="bn-ring" cx="540" cy="862" r="26" fill="none" stroke="{C["red"]}" stroke-width="5" opacity="0"/>' for _ in range(3))
scenes[s] = scene_file(s, f"""
#bn-svg {{ position:absolute; left:0; top:0; }}
#bn-c {{ position:absolute; left:90px; top:140px; opacity:0; }}
#bn-s {{ position:absolute; left:640px; top:150px; opacity:0; }}
""", f"""
  <svg id="bn-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    {head("bn", air_op=0.15, skull=True)}
    <path id="bn-rt" d="{BONEP}" fill="none" stroke="none"/>
    {rings}{bdots}
    <path id="bn-l1" d="M565,868 L640,900" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
    <path id="bn-l2" d="M700,508 L770,390" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>
  </svg>
  <div id="bn-c"><span class="chip" style="background:#FFC9C2;font-size:54px;transform:rotate(-3deg)">road 2: bone</span></div>
  <div id="bn-s"><span class="chip" style="background:{C['hi']};font-size:50px;transform:rotate(3deg)">shortcut!</span></div>
  {tape("bn-t1", "vocal cords", 640, 880, -3, 44, "rgba(247,198,207,.95)")}
  {tape("bn-t2", "cochlea", 740, 320, 4, 48)}
""", J("""
tl.set("#bn-c", {opacity:1}, 0.1); pop("#bn-c .chip", 0.1, {from:{rotation:-12}, to:{rotation:-3}});
tl.set("#bn-s", {opacity:1}, @ts); pop("#bn-s .chip", @ts, {from:{rotation:14, scale:1.5}, to:{rotation:3}});
ink("#bn-l1", @tv, 0.25); tl.set("#bn-t1", {opacity:1}, @tv); pop("#bn-t1 span", @tv, {from:{rotation:-14}, to:{rotation:-3}});
tl.fromTo(".bn-ring", {opacity:0.9, scale:1, svgOrigin:"540 862"}, {opacity:0, scale:2.8, svgOrigin:"540 862", duration:0.6, stagger:0.2, repeat:4, ease:"power1.out", immediateRender:false}, @tv);
tl.fromTo("#bn-vc", {x:0}, {x:4, duration:0.05, yoyo:true, repeat:23, immediateRender:false}, @tv);
ink("#bn-skull", @tb, 0.9, {ease:"power1.inOut"});
ink("#bn-bone", @tz, 0.7);
ink("#bn-l2", @tc, 0.25); tl.set("#bn-t2", {opacity:1}, @tc); pop("#bn-t2 span", @tc, {from:{rotation:14}, to:{rotation:4}});
tl.fromTo("#bn-coch", {scale:1, svgOrigin:"695 540"}, {scale:1.45, svgOrigin:"695 540", duration:0.25, yoyo:true, repeat:1, immediateRender:false}, @tc);
""", ts=tsh - 0.1, tv=tvc - 0.1, tb=tbo - 0.2, tz=tbz - 0.3, tc=tco - 0.1)
  + "".join(f'tl.set("#bn-d{i}", {{opacity:1}}, {tbz - 0.1 + i * 0.16:.3f}); along("#bn-d{i}", "#bn-rt", {tbz - 0.1 + i * 0.16:.3f}, 0.6, {{ease:"power2.in"}}); tl.to("#bn-d{i}", {{opacity:0, duration:0.1}}, {tbz + 0.48 + i * 0.16:.3f});\n' for i in range(NB)))

# 7 BASS — a BASS knob turns up; the waveform morphs from thin and quick into big, slow, full waves
s = "bass"; tbr = aw(s, "bone road"); tbs = aw(s, "boosts"); tlo = aw(s, "low"); tfu = aw(s, "fuller"); tin = aw(s, "inside your")
KX, KY = 540, 420
def pol(a, r): return KX + r * math.sin(math.radians(a)), KY - r * math.cos(math.radians(a))
kt = "".join(f'<path d="M{pol(a,170)[0]:.1f},{pol(a,170)[1]:.1f} L{pol(a,195)[0]:.1f},{pol(a,195)[1]:.1f}" stroke="{K}" stroke-width="6" stroke-linecap="round"/>' for a in range(-135, 136, 27))
a0, a1 = pol(-135, 214), pol(110, 214)
W_THIN = wave(130, 950, 760, 13, 26, 160)
W_FAT = wave(130, 950, 760, 3, 62, 160, harm=0.35)
scenes[s] = scene_file(s, f"""
#bs-svg {{ position:absolute; left:0; top:0; }}
#bs-b {{ position:absolute; left:80px; top:150px; opacity:0; }}
#bs-lo {{ position:absolute; left:740px; top:160px; opacity:0; }}
#bs-h {{ position:absolute; left:130px; top:615px; opacity:0; }}
#bs-f {{ position:absolute; left:430px; top:868px; opacity:0; }}
#bs-kn {{ opacity:0; }}
""", f"""
  <svg id="bs-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="bs-kn">{kt}
      <circle cx="{KX}" cy="{KY}" r="150" fill="#FFFFFF" stroke="{K}" stroke-width="8"/>
      <circle cx="{KX}" cy="{KY}" r="112" fill="{C['hi']}" stroke="{K}" stroke-width="5"/>
      <text x="{KX}" y="{KY + 18}" text-anchor="middle" style="{GH}font-size:58px" fill="{K}">BASS</text>
      <g id="bs-ptr"><path d="M{KX},{KY - 118} L{KX},{KY - 150}" stroke="{C['red']}" stroke-width="14" stroke-linecap="round"/></g>
    </g>
    <path id="bs-arc" d="M{a0[0]:.1f},{a0[1]:.1f} A214,214 0 1,1 {a1[0]:.1f},{a1[1]:.1f}" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path id="bs-w" d="{W_THIN}" stroke="{C['blue']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  {tape("bs-b", "bone road", 80, 150, -4, 46, "rgba(247,198,207,.95)")}
  <div id="bs-lo"><span class="chip" style="background:#FFFFFF;font-size:44px;transform:rotate(3deg)">low tones up</span></div>
  <div id="bs-h"><span class="chip" style="background:#FFFFFF;font-size:40px">in your head</span></div>
  <div id="bs-f"><span class="chip" style="background:{C['hi']};font-size:52px;transform:rotate(-2deg)">fuller and deeper</span></div>
""", J("""
tl.fromTo("#bs-kn", {opacity:0, scale:0.7, svgOrigin:"@kx @ky"}, {opacity:1, scale:1, svgOrigin:"@kx @ky", duration:0.4, ease:"back.out(2)"}, 0.05);
tl.set("#bs-ptr", {rotation:-135, svgOrigin:"@kx @ky"}, 0.0);
tl.set("#bs-b", {opacity:1}, @tr); pop("#bs-b span", @tr, {from:{rotation:-14}, to:{rotation:-4}});
ink("#bs-w", 0.3, 0.6);
tl.to("#bs-ptr", {rotation:110, svgOrigin:"@kx @ky", duration:1.0, ease:"back.out(1.4)"}, @tb);
ink("#bs-arc", @tb, 1.0, {ease:"power2.out"});
tl.set("#bs-lo", {opacity:1}, @tl); pop("#bs-lo .chip", @tl, {from:{rotation:12}, to:{rotation:3}});
tl.set("#bs-h", {opacity:1}, @th); pop("#bs-h .chip", @th);
morph("#bs-w", "@fat", @tm, 1.0, {ease:"power2.inOut"});
tl.to("#bs-w", {attr:{"stroke-width":14}, duration:0.6}, @tm);
tl.set("#bs-f", {opacity:1}, @tf); pop("#bs-f .chip", @tf, {from:{rotation:-10, scale:1.4}, to:{rotation:-2}});
""", kx=KX, ky=KY, tr=tbr - 0.1, tb=tbs - 0.15, tl=tlo - 0.1, th=tin - 0.1, tm=tin + 0.2, tf=tfu - 0.1, fat=W_FAT))

# 8 MIC — side by side: what you hear (air + bone, full wave) vs what the mic hears (air only, thin high wave)
s = "mic"; tmi = aw(s, "microphone"); tar = aw(s, "air road"); tnb = aw(s, "no bone"); tth = aw(s, "thinner")
L_FAT = wave(110, 500, 700, 2.5, 60, 100, harm=0.35)
R_THIN = wave(580, 1000, 700, 9, 26, 120)
def pill(idn, txt, x, y, col, bg, op=1):
    return f'<div id="{idn}" class="abs" style="left:{x}px;top:{y}px;opacity:{op}"><span class="pill" style="color:{col};background:{bg};font-size:48px">{txt}</span></div>'
scenes[s] = scene_file(s, f"""
#mc-svg {{ position:absolute; left:0; top:0; }}
#mc-lh {{ position:absolute; left:110px; top:150px; opacity:0; }}
#mc-rh {{ position:absolute; left:600px; top:150px; opacity:0; }}
#mc-th {{ position:absolute; left:560px; top:820px; opacity:0; }}
#mc-mic, #mc-lw {{ opacity:0; }}
""", f"""
  <svg id="mc-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="mc-div" d="M545,160 L545,860" stroke="{C['pencil']}" stroke-width="5" stroke-dasharray="14 14" fill="none"/>
    <g id="mc-mic">
      <rect x="742" y="240" width="96" height="130" rx="48" fill="#E6E6E6" stroke="{K}" stroke-width="7"/>
      <path d="M760,280 L820,280 M756,310 L824,310 M760,340 L820,340" stroke="{K}" stroke-width="4" stroke-linecap="round" opacity=".6"/>
      <path class="mc-st" d="M712,320 Q712,410 790,410 Q868,410 868,320" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path class="mc-st" d="M790,410 L790,440" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round"/>
    </g>
    <g id="mc-lw"><path d="{L_FAT}" stroke="{C['blue']}" stroke-width="13" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
    <path id="mc-rw" d="{R_THIN}" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="mc-lh"><span class="chip" style="background:#FFFFFF;font-size:50px;transform:rotate(-2deg)">you hear</span></div>
  {pill("mc-la", "air road", 140, 320, C['blue'], AIR, 0)}
  {pill("mc-lb", "+ bone road", 120, 430, C['red'], "#FFE4E1", 0)}
  <div id="mc-rh"><span class="chip" style="background:#FFFFFF;font-size:50px;transform:rotate(2deg)">the mic hears</span></div>
  {pill("mc-ra", "air road", 690, 470, C['blue'], AIR, 0)}
  {pill("mc-rb", "bone road", 660, 565, C['pencil'], "#FFFFFF", 0)}
  <svg class="abs" style="left:0;top:0" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore><path id="mc-x" d="M640,605 L930,595" stroke="{C['red']}" stroke-width="10" fill="none" stroke-linecap="round"/></svg>
  <div id="mc-th"><span class="chip" style="background:{C['hi']};font-size:50px;transform:rotate(-2deg)">thinner and higher</span></div>
""", J("""
ink("#mc-div", 0.0, 0.5);
tl.set("#mc-lh", {opacity:1}, 0.1); pop("#mc-lh .chip", 0.1);
tl.set("#mc-la", {opacity:1}, 0.3); pop("#mc-la .pill", 0.3); tl.set("#mc-lb", {opacity:1}, 0.5); pop("#mc-lb .pill", 0.5);
tl.fromTo("#mc-lw", {opacity:0, scaleY:0.2, svgOrigin:"305 700"}, {opacity:1, scaleY:1, svgOrigin:"305 700", duration:0.4, ease:"back.out(2)"}, 0.7);
tl.fromTo("#mc-mic", {opacity:0, y:-30}, {opacity:1, y:0, duration:0.35, ease:"back.out(2)"}, @tm);
tl.set("#mc-rh", {opacity:1}, @tm); pop("#mc-rh .chip", @tm);
tl.set("#mc-ra", {opacity:1}, @ta); pop("#mc-ra .pill", @ta);
tl.set("#mc-rb", {opacity:1}, @tn); pop("#mc-rb .pill", @tn, {from:{rotation:8}, to:{rotation:0}});
ink("#mc-x", @tn2, 0.3);
ink("#mc-rw", @tt, 0.6, {ease:"none"});
tl.set("#mc-th", {opacity:1}, @tt2); pop("#mc-th .chip", @tt2, {from:{rotation:-10, scale:1.4}, to:{rotation:-2}});
""", tm=tmi - 0.1, ta=tar - 0.1, tn=tnb - 0.1, tn2=tnb + 0.25, tt=tth - 0.6, tt2=tth - 0.1))

# 9 REAL — myth crossed out: "the mic is broken?" gets a red strike; the recording = what everyone else hears
s = "real"; tbk = aw(s, "broken"); tno = aw(s, "nope"); tre = aw(s, "that recording"); tev = aw(s, "everyone else")
lis = ""
for i, x in enumerate((560, 740, 920)):
    lis += (f'<g class="rl-f" id="rl-f{i}"><circle cx="{x}" cy="740" r="62" fill="{SKIN}" stroke="{K}" stroke-width="6"/>'
            f'<circle cx="{x - 20}" cy="728" r="7" fill="{K}"/><circle cx="{x + 20}" cy="728" r="7" fill="{K}"/>'
            f'<path d="M{x - 20},760 Q{x},776 {x + 20},760" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round"/>'
            f'<path d="M{x - 62},722 Q{x - 82},740 {x - 62},760" fill="{SKIN}" stroke="{K}" stroke-width="5"/></g>')
rarcs = "".join(f'<path class="rl-a" d="M{340 + k * 40},{650 - k * 10} Q{370 + k * 46},{720} {340 + k * 40},{790 + k * 10}" stroke="{C["blue"]}" stroke-width="7" fill="none" stroke-linecap="round"/>' for k in range(3))
scenes[s] = scene_file(s, f"""
#rl-svg {{ position:absolute; left:0; top:0; }}
#rl-m {{ top:190px; font-size:96px; color:{C['pencil']}; opacity:0; }}
#rl-no {{ position:absolute; left:720px; top:330px; opacity:0; }}
#rl-no span {{ display:inline-block; {GH} font-size:72px; color:{C['red']}; border:6px solid {C['red']}; padding:0 22px; border-radius:12px; transform:rotate(-8deg); background:#FFFFFF; }}
#rl-r {{ top:450px; font-size:68px; line-height:1.15; opacity:0; }}
#rl-ph, .rl-f {{ opacity:0; }}
""", f"""
  <div id="rl-m" class="h1">the mic is broken?</div>
  <div id="rl-r" class="h1"><span class="hl">close to what everyone<br>else hears</span></div>
  <svg id="rl-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <path id="rl-st" d="M120,262 Q540,236 960,252" stroke="{C['red']}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <g id="rl-ph">{phone("rl", 140, 600, 170, 250)}</g>
    {rarcs}{lis}
  </svg>
  <div id="rl-no"><span>NOPE</span></div>
""", J("""
tl.set("#rl-m", {opacity:1}, @tb); rise("#rl-m", @tb);
ink("#rl-st", @tn, 0.35, {ease:"power2.out"});
tl.set("#rl-no", {opacity:1}, @tn2); pop("#rl-no span", @tn2, {from:{rotation:-26, scale:1.8}, to:{rotation:-8}});
tl.set("#rl-r", {opacity:1}, @tr); rise("#rl-r", @tr);
tl.fromTo("#rl-ph", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35, ease:"back.out(2)"}, @tr);
ink("#rl-prog", @tr, 2.0, {ease:"none"});
ink(".rl-a", @te, 0.3, {stagger:0.12});
tl.fromTo(".rl-f", {opacity:0, scale:0.5, transformOrigin:"50% 50%"}, {opacity:1, scale:1, transformOrigin:"50% 50%", duration:0.3, stagger:0.12, ease:"back.out(2)"}, @te);
""", tb=tbk - 0.6, tn=tno - 0.15, tn2=tno + 0.1, tr=tre - 0.1, te=tev - 0.2))

# 10 TIP — the same head: hands plug the ears, the air road gets an X, the bone road glows, MMMM!
s = "tip"; ttr = aw(s, "try this"); tpl = aw(s, "plug"); thu = aw(s, "and hum"); tbr = aw(s, "bone road"); tlo = aw(s, "louder")
scenes[s] = scene_file(s, f"""
#tp-svg {{ position:absolute; left:0; top:0; }}
#tp-m {{ position:absolute; left:80px; top:130px; {GH} font-size:130px; line-height:1; color:{C['red']}; opacity:0; }}
#tp-c {{ position:absolute; left:600px; top:170px; opacity:0; }}
#tp-l {{ position:absolute; left:500px; top:885px; white-space:nowrap; opacity:0; }}
.tp-hand, #tp-xx {{ opacity:0; }}
""", f"""
  <svg id="tp-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g transform="translate(540 600) scale(0.82) translate(-540 -600)">
      {head("tp", air_op=0.35, hands=True)}
      <g id="tp-xx"><path d="M850,670 L920,740 M920,670 L850,740" stroke="{C['red']}" stroke-width="14" stroke-linecap="round"/></g>
    </g>
  </svg>
  <div id="tp-m">Mmmmm</div>
  <div id="tp-c"><span class="chip" style="background:#FFFFFF;font-size:50px;transform:rotate(2deg)">plug ears, hum</span></div>
  <div id="tp-l"><span class="chip" style="background:{C['hi']};font-size:48px;transform:rotate(-2deg)">louder and boomier</span></div>
""", J("""
tl.set("#tp-c", {opacity:1}, @tt); pop("#tp-c .chip", @tt, {from:{rotation:12}, to:{rotation:2}});
tl.fromTo(".tp-hand", {opacity:0, scale:1.5, transformOrigin:"50% 50%"}, {opacity:1, scale:1, transformOrigin:"50% 50%", duration:0.35, stagger:0.1, ease:"back.out(2)"}, @tp);
tl.fromTo("#tp-xx", {opacity:0, scale:1.6, svgOrigin:"885 705"}, {opacity:1, scale:1, svgOrigin:"885 705", duration:0.3, ease:"back.out(2)"}, @tp2);
morph("#tp-mouth", "@shut", @th, 0.3);
tl.set("#tp-m", {opacity:1}, @th); pop("#tp-m", @th, {from:{scale:1.6, rotation:-10}, to:{rotation:-4}});
tl.fromTo("#tp-m", {x:0}, {x:7, duration:0.06, yoyo:true, repeat:40, ease:"sine.inOut", immediateRender:false}, @th2);
tl.to("#tp-bone", {attr:{"stroke-width":26}, duration:0.35, ease:"back.out(2)"}, @tb);
tl.fromTo("#tp-bone", {opacity:1}, {opacity:0.55, duration:0.18, yoyo:true, repeat:9, immediateRender:false}, @tb2);
tl.fromTo("#tp-coch", {scale:1, svgOrigin:"695 540"}, {scale:1.5, svgOrigin:"695 540", duration:0.25, yoyo:true, repeat:3, immediateRender:false}, @tb);
tl.set("#tp-l", {opacity:1}, @tl); pop("#tp-l .chip", @tl, {from:{rotation:-12, scale:1.5}, to:{rotation:-2}});
""", tt=ttr - 0.1, tp=tpl - 0.15, tp2=tpl + 0.4, th=thu, th2=thu + 0.3, tb=tbr - 0.1, tb2=tbr + 0.3, tl=tlo - 0.1, shut=M_SHUT))

# 11 OUTRO — callback: the phone plays again; a tiny BASS knob turns down; "that's the real you" (Max centre, keep y < 620)
s = "outro"; tre = aw(s, "the real"); tba = aw(s, "bass"); tsc = aw(s, "stay curious")
OW = wave(480, 1000, 300, 6, 26, 90)
scenes[s] = scene_file(s, f"""
#ou-svg {{ position:absolute; left:0; top:0; }}
#ou-r {{ position:absolute; left:0; right:0; top:480px; text-align:center; opacity:0; }}
#ou-sc {{ top:470px; font-size:110px; opacity:0; }}
#ou-ph {{ opacity:0; }}
""", f"""
  <svg id="ou-svg" width="{W}" height="960" viewBox="0 0 {W} 960" data-layout-ignore>
    <g id="ou-ph">{phone("ou", 200, 150, 200, 300)}</g>
    <path id="ou-w" d="{OW}" stroke="{C['blue']}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div id="ou-r"><span class="chip" style="background:#FFFFFF;font-size:56px">that's the real you!</span></div>
  <div id="ou-sc" class="h1"><span class="hl">Stay curious!</span></div>
""", J("""
tl.fromTo("#ou-ph", {opacity:0, scale:0.6, svgOrigin:"300 300"}, {opacity:1, scale:1, svgOrigin:"300 300", duration:0.4, ease:"back.out(2)"}, 0.05);
ink("#ou-prog", 0.3, 3.0, {ease:"none"});
ink("#ou-w", 0.3, 0.8);
tl.set("#ou-r", {opacity:1}, @tr); pop("#ou-r .chip", @tr, {from:{rotation:-8, scale:1.4}, to:{rotation:-1}});
tl.to("#ou-w", {attr:{"stroke-width":12}, duration:0.2, yoyo:true, repeat:1}, @tb);
tl.to("#ou-r", {opacity:0, y:-30, duration:0.25, ease:"power2.in"}, @tx);
tl.set("#ou-sc", {opacity:1}, @tsc); pop("#ou-sc", @tsc, {from:{scale:1.5}, to:{}});
""", tr=tre - 0.1, tb=tba - 0.1, tx=tsc - 0.3, tsc=tsc), fade=False)
# === GESTURES ===
think(g("hook", "why does"), SC["guess"]["start"] + 0.2)
point(g("guess", "cheap"), 2.6)
wave(g("intro", "I'm Max"))
point(g("roads", "two different"), 1.3)
point(g("air", "eardrum"), 1.2)
wow(g("bone", "cochlea"), 1.1)
point(g("bass", "fuller"), 1.3)
point(g("mic", "thinner"), 1.2)
wow(g("real", "nope"), 1.0)
wow(g("tip", "louder"), 1.1)
wave(g("outro", "stay curious"), 2)
# === SFX ===
sfx += [("whoosh-short.mp3", A("hook", "quick question"), 0.3), ("pop.mp3", A("hook", "weird"), 0.5),
        ("pop.mp3", A("guess", "cheap"), 0.45), ("pop.mp3", A("guess", "nerves"), 0.45), ("pop.mp3", A("guess", "or something"), 0.5),
        ("sparkle.mp3", A("intro", "max wise"), 0.4), ("click.mp3", A("roads", "two different"), 0.45),
        ("whoosh-short.mp3", A("air", "flies"), 0.3), ("click-soft.mp3", A("air", "eardrum"), 0.5),
        ("impact-bass-1.mp3", A("bone", "buzz"), 0.35), ("riser.mp3", A("bass", "boosts"), 0.25),
        ("ping.mp3", A("mic", "thinner"), 0.4), ("impact-bass-2.mp3", A("real", "nope"), 0.35),
        ("click-soft.mp3", A("tip", "plug"), 0.5), ("pop.mp3", A("tip", "louder"), 0.5), ("sparkle.mp3", A("outro", "stay curious"), 0.45)]
