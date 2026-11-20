import re,subprocess,os
sky=open('skyline.svg').read()
sky=sky.replace('#181A1C','var(--sky)').replace('fill="#ffffff"','fill="var(--win)"')
sky=re.sub(r'<svg [^>]*>','<svg class="sky" viewBox="0 0 1080 300" xmlns="http://www.w3.org/2000/svg">',sky)
zw=open('zaelot.svg').read()
zwhite=open(os.path.expanduser('~/.claude/plugins/cache/zaelot/zaelot-identity/0.14.19/brand/logo/zaelot-logo-white.svg')).read()
open('zaelot-white.svg','w').write(zwhite)

V={
 '1-classic':dict(bg='#FBFAF6',ink='#181A1C',cloud='#F3E060',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='std'),
 '2-night':dict(bg='#111315',ink='#FFFFFF',cloud='#F3E060',dot='#F3E060',win='#111315',winop='.7',inv=True,zl='zaelot-white.svg',layout='std',sky='#FFFFFF'),
 '3-zaelow':dict(bg='#F3E060',ink='#181A1C',cloud='#FFFFFF',dot='#181A1C',win='#F3E060',winop='.6',inv=False,zl='zaelot.svg',layout='std'),
 '4-adstudio-led':dict(bg='#FBFAF6',ink='#181A1C',cloud='#F3E060',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad'),
 '6-halloween':dict(bg='#0a0f1e',ink='#FFFFFF',cloud='#F28C28',dot='#F28C28',win='#2a4352',winop='.6',inv=True,zl='zaelot-white.svg',layout='std',sky='#05070c',cloudop='.0',hallow=True),
 '7-knicks':dict(bg='#006BB6',ink='#FFFFFF',cloud='#FFFFFF',dot='#F58426',win='#0A5C9C',winop='.6',inv=True,zl='zaelot-white.svg',layout='std',sky='#002F5A',cloudop='.12',knicks=True),
 '8-adstudio-knicks':dict(bg='#FBFAF6',ink='#181A1C',cloud='#F3E060',dot='#F58426',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',bigstroke='#006BB6',bigsw=6,dp=7,dr=3.1),
 '9-adstudio-knicks-blueclouds':dict(bg='#FBFAF6',ink='#181A1C',cloud='#7FB6E0',dot='#F58426',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',bigstroke='#006BB6',bigsw=6,dp=7,dr=3.1,cloudop='.6'),
 '10-adstudio-lime':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad'),
 '11-adstudio-lime-knicks':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#F58426',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',bigstroke='#006BB6',bigsw=6,dp=7,dr=3.1),
 '12-solid-din':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',solid=True,fill='#F58426',shadow='#006BB6',font="'DIN Condensed'",fw=700),
 '13-solid-futura':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',solid=True,fill='#F58426',shadow='#006BB6',font="'Futura'",fw=800,st='condensed'),
 '14-solid-instrument':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',solid=True,fill='#F58426',shadow='#006BB6',font="'Instrument Sans'",fw=700),
 '15-solid-rockwell':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',solid=True,fill='#F58426',shadow='#006BB6',font="'Rockwell'",fw=800),
 '16-solid-avenir':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',solid=True,fill='#F58426',shadow='#006BB6',font="'Avenir Next Condensed'",fw=800),
 '17-futura-final':dict(bg='#FBFAF6',ink='#181A1C',cloud='#D4F160',dot='#181A1C',win='#FBFAF6',winop='.55',inv=False,zl='zaelot.svg',layout='ad',solid=True,fill='#F58426',shadow='#006BB6',font="'Futura'",fw=800,st='condensed',nopresent=True,admt=20,bt=300),
 '5-hightouch-glow':dict(bg='#141022',ink='#FFFFFF',cloud='#FFFFFF',dot='#FFFFFF',win='#1a1c4a',winop='.7',inv=True,zl='zaelot-white.svg',layout='std',sky='#FFFFFF',cloudop='.10',glow=True),
}
HALLOW='''body{background:linear-gradient(180deg,#0a0f1e 0%,#121a2e 45%,#2a4352 78%,#3d5c66 100%)}
.moon{position:absolute;top:500px;left:690px;width:230px;height:230px;border-radius:50%;background:radial-gradient(circle at 40% 38%,#FFF7DC,#F1E2AE 60%,#D9C68A);box-shadow:0 0 60px 20px rgba(255,236,170,.35),0 0 160px 60px rgba(255,220,140,.15)}
.bat{position:absolute;fill:#05070c}
.pk{position:absolute;bottom:200px}
.logos .ht,.adstudio{filter:invert(1)}
.logos .z{filter:none}
'''
KN='''body{background:radial-gradient(ellipse 70% 55% at 80% 62%,#1A86D6,transparent 70%),linear-gradient(180deg,#00467F 0%,#006BB6 60%,#0A5C9C 100%)}
.ball{position:absolute;top:470px;left:700px;width:250px;height:250px}
.badge{position:absolute;top:398px;left:50%;transform:translateX(-50%) rotate(-3deg);background:#F58426;color:#fff;font-weight:700;font-size:26px;letter-spacing:.12em;text-transform:uppercase;padding:12px 28px;border-radius:999px;box-shadow:0 6px 0 #B85F12;z-index:5}
.logos .ht,.adstudio{filter:invert(1)}
.logos .z{filter:none}
.rule i{background:#F58426}
'''
GLOW='''body{background:radial-gradient(ellipse 60% 45% at 8% 100%,rgba(201,104,58,.65),transparent 70%),radial-gradient(ellipse 55% 60% at 100% 40%,rgba(95,192,201,.85),transparent 70%),linear-gradient(115deg,#120d1f 0%,#161536 40%,#1f2f78 70%,#3a78b8 100%)}
body:after{content:"";position:absolute;inset:0;opacity:.22;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
svg.sky,.big{filter:drop-shadow(0 0 10px rgba(255,255,255,.45))}
.logos img,.adstudio{filter:invert(1) drop-shadow(0 0 8px rgba(255,255,255,.35))}
.logos .z{filter:drop-shadow(0 0 8px rgba(255,255,255,.35))}
'''
css='''@font-face{font-family:"Instrument Sans";src:url("instrument-sans-variable.woff2") format("woff2");font-weight:400 700;font-stretch:75%% 100%%;}
:root{--bg:%(bg)s;--ink:%(ink)s;--cloud:%(cloud)s;--dot:%(dot)s;--sky:%(sky)s;--win:%(win)s}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px;background:var(--bg);overflow:hidden}
%(glowcss)s
body{font-family:"Instrument Sans",sans-serif;color:var(--ink);position:relative}
.cloud{position:absolute;width:560px;height:420px;opacity:%(cloudop)s;background-image:radial-gradient(circle,var(--cloud) 0 3.4px,transparent 3.8px);background-size:11px 11px}
.c1{top:-80px;left:-120px;-webkit-mask:radial-gradient(ellipse 55%% 50%% at 45%% 45%%,#000 30%%,transparent 72%%)}
.c2{top:-60px;right:-140px;-webkit-mask:radial-gradient(ellipse 55%% 50%% at 55%% 45%%,#000 25%%,transparent 70%%)}
.c3{top:330px;left:-210px;width:520px;height:360px;-webkit-mask:radial-gradient(ellipse 50%% 45%% at 50%% 50%%,#000 20%%,transparent 70%%)}
.c4{top:310px;right:-220px;width:520px;height:360px;-webkit-mask:radial-gradient(ellipse 50%% 45%% at 50%% 50%%,#000 20%%,transparent 70%%)}
.top{position:absolute;top:58px;left:0;right:0;text-align:center}
.adstudio{height:50px;%(invcss)s}
.present{margin-top:20px;font-size:17px;font-weight:700;letter-spacing:.32em;text-transform:uppercase}
h1{margin-top:16px;font-size:84px;line-height:.98;font-weight:700;letter-spacing:-.025em}
.meta{margin-top:22px;font-size:24px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.meta span{display:inline-block;margin:0 14px;transform:translateY(-3px)}
.big{position:absolute;top:%(bigtop)spx;left:50px;width:980px;height:%(bigh)spx}
.big:not(.solid) text{font-family:"Instrument Sans";font-weight:700;font-stretch:75%%}
svg.sky{position:absolute;top:556px;left:0;width:1080px;height:300px}
.rule{position:absolute;top:888px;left:64px;right:64px;display:flex;align-items:center;gap:22px}
.rule i{flex:1;height:2px;background:var(--ink)}
.rule b{font-size:15px;font-weight:700;letter-spacing:.32em;text-transform:uppercase}
.logos{position:absolute;top:930px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:110px}
.logos .ht{height:64px;%(invcss)s}
.logos .z{height:60px}
/* ad-led layout */
.adhero{height:92px;%(invcss)s}
.kicker{margin-top:14px;font-size:62px;font-weight:700;letter-spacing:-.02em;line-height:1}
.sub{margin-top:18px;font-size:30px;font-weight:600;letter-spacing:-.01em}
'''
def big(c):
    if c.get('solid'):
        return solid(c)
    return f'''<svg class="big" viewBox="0 0 980 {c['bigh']}" xmlns="http://www.w3.org/2000/svg">
<defs><pattern id="ht" width="{c.get('dp',8)}" height="{c.get('dp',8)}" patternUnits="userSpaceOnUse"><circle cx="{c.get('dp',8)/2}" cy="{c.get('dp',8)/2}" r="{c.get('dr',2.6)}" fill="var(--dot)"/></pattern></defs>
<text x="490" y="{c['bigh']-8}" text-anchor="middle" textLength="970" lengthAdjust="spacingAndGlyphs" font-size="{c['bigfs']}" fill="url(#ht)" stroke="{c.get('bigstroke','var(--ink)')}" stroke-width="{c.get('bigsw',3)}" paint-order="stroke">NEW YORK</text></svg>'''
BATS='''<svg class="bat" style="top:470px;left:120px;width:60px" viewBox="0 0 60 24"><path d="M30 8c2-4 4-4 5-1 3-4 9-6 13-4-4 1-6 5-5 9-3-2-6-1-8 2-1-2-3-3-5-3s-4 1-5 3c-2-3-5-4-8-2 1-4-1-8-5-9 4-2 10 0 13 4 1-3 3-3 5 1z"/></svg>
<svg class="bat" style="top:520px;left:230px;width:40px" viewBox="0 0 60 24"><path d="M30 8c2-4 4-4 5-1 3-4 9-6 13-4-4 1-6 5-5 9-3-2-6-1-8 2-1-2-3-3-5-3s-4 1-5 3c-2-3-5-4-8-2 1-4-1-8-5-9 4-2 10 0 13 4 1-3 3-3 5 1z"/></svg>
<svg class="bat" style="top:450px;left:930px;width:46px" viewBox="0 0 60 24"><path d="M30 8c2-4 4-4 5-1 3-4 9-6 13-4-4 1-6 5-5 9-3-2-6-1-8 2-1-2-3-3-5-3s-4 1-5 3c-2-3-5-4-8-2 1-4-1-8-5-9 4-2 10 0 13 4 1-3 3-3 5 1z"/></svg>'''
PKS='''<svg class="pk" style="left:40px;width:120px" viewBox="0 0 100 84"><defs><radialGradient id="pg40" cx="45%" cy="40%"><stop offset="0" stop-color="#FFA640"/><stop offset="1" stop-color="#C85A12"/></radialGradient></defs>
<path d="M48 14c0-8 4-12 10-13l2 4c-5 1-7 4-7 9z" fill="#3b4a2a"/>
<ellipse cx="30" cy="48" rx="24" ry="32" fill="url(#pg40)"/><ellipse cx="70" cy="48" rx="24" ry="32" fill="url(#pg40)"/><ellipse cx="50" cy="48" rx="26" ry="35" fill="url(#pg40)"/>
<path d="M30 38l9-9 9 9zM52 38l9-9 9 9z" fill="#FFE27A"/><path d="M28 56q22 16 44 0l-6 4-4-4-5 5-5-5-5 5-5-5-4 4z" fill="#FFE27A"/></svg><svg class="pk" style="left:150px;width:82px" viewBox="0 0 100 84"><defs><radialGradient id="pg150" cx="45%" cy="40%"><stop offset="0" stop-color="#FFA640"/><stop offset="1" stop-color="#C85A12"/></radialGradient></defs>
<path d="M48 14c0-8 4-12 10-13l2 4c-5 1-7 4-7 9z" fill="#3b4a2a"/>
<ellipse cx="30" cy="48" rx="24" ry="32" fill="url(#pg150)"/><ellipse cx="70" cy="48" rx="24" ry="32" fill="url(#pg150)"/><ellipse cx="50" cy="48" rx="26" ry="35" fill="url(#pg150)"/>
<path d="M30 38l9-9 9 9zM52 38l9-9 9 9z" fill="#FFE27A"/><path d="M28 56q22 16 44 0l-6 4-4-4-5 5-5-5-5 5-5-5-4 4z" fill="#FFE27A"/></svg><svg class="pk" style="left:900px;width:110px" viewBox="0 0 100 84"><defs><radialGradient id="pg900" cx="45%" cy="40%"><stop offset="0" stop-color="#FFA640"/><stop offset="1" stop-color="#C85A12"/></radialGradient></defs>
<path d="M48 14c0-8 4-12 10-13l2 4c-5 1-7 4-7 9z" fill="#3b4a2a"/>
<ellipse cx="30" cy="48" rx="24" ry="32" fill="url(#pg900)"/><ellipse cx="70" cy="48" rx="24" ry="32" fill="url(#pg900)"/><ellipse cx="50" cy="48" rx="26" ry="35" fill="url(#pg900)"/>
<path d="M30 38l9-9 9 9zM52 38l9-9 9 9z" fill="#FFE27A"/><path d="M28 56q22 16 44 0l-6 4-4-4-5 5-5-5-5 5-5-5-4 4z" fill="#FFE27A"/></svg>'''
BALL='''<svg class="ball" viewBox="0 0 100 100"><defs><radialGradient id="bb" cx="38%" cy="35%"><stop offset="0" stop-color="#FFA552"/><stop offset="1" stop-color="#D2650F"/></radialGradient></defs><circle cx="50" cy="50" r="48" fill="url(#bb)"/><g fill="none" stroke="#3a1a05" stroke-width="2.2"><circle cx="50" cy="50" r="48"/><path d="M2 50h96M50 2v96"/><path d="M16 16q22 34 0 68M84 16q-22 34 0 68"/></g></svg>'''

def solid(c):
    fam=c['font']; fill=c['fill']; sh=c['shadow']; off=c.get('off',8)
    return f'''<svg class="big solid" viewBox="0 0 980 {c['bigh']}" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
<g style="font-family:{fam};font-weight:{c.get('fw',400)};font-stretch:{c.get('st','normal')}" text-anchor="middle" class="ny">
<text x="{490+off}" y="{c['bigh']-8+off}" font-size="200" fill="{sh}">NEW YORK</text>
<text x="490" y="{c['bigh']-8}" font-size="200" fill="{fill}">NEW YORK</text></g></svg>
<script>
document.fonts.ready.then(()=>{{const ts=[...document.querySelectorAll('.ny text')];const w=ts[1].getComputedTextLength();const fs=200*{c.get('fitw',960)}/w;ts.forEach(t=>t.setAttribute('font-size',fs));
const bb=ts[1].getBBox();if(bb.height>{c['bigh']}*1.02){{const k={c['bigh']}/bb.height;ts.forEach(t=>t.setAttribute('font-size',fs*k));}}}});
</script>'''

for name,c in V.items():
    c.setdefault('sky',c['ink']); c.setdefault('cloudop','1')
    c['glowcss']=GLOW if c.get('glow') else (HALLOW if c.get('hallow') else (KN if c.get('knicks') else ''))
    c['invcss']='filter:invert(1)' if c['inv'] else ''
    if c['layout']=='std':
        c.update(bigtop=388,bigh=250,bigfs=300)
        top=f'''<img class="adstudio" src="adstudio.png" alt="Ad Studio">
<div class="present">Hightouch + Zaelot present</div>
<h1>Create Scroll-Stopping<br>Ads on Demand</h1>
<div class="meta">Oct 27, 2026<span>•</span>New York, NY</div>'''
    else:
        c.update(bigtop=c.get('bt',400),bigh=240,bigfs=290)
        pres='' if c.get('nopresent') else '<div class="present">Hightouch + Zaelot present</div>'
        top=f'''{pres}
<div style="margin-top:{c.get('admt',22)}px"><img class="adhero" src="adstudio.png" alt="Ad Studio"></div>
<div class="kicker">Hackathon</div>
<div class="sub">Never run out of on-brand ads again · Oct 27, 2026</div>'''
    html=f'''<!doctype html><html><head><meta charset="utf-8">{c.get('link','')}<style>{css%c}</style></head><body>
<div class="cloud c1"></div><div class="cloud c2"></div><div class="cloud c3"></div><div class="cloud c4"></div>
{("<div class='moon'></div>"+BATS) if c.get('hallow') else ''}{(BALL+"<div class='badge'>Win Knicks tickets</div>") if c.get('knicks') else ''}
<div class="top">{top}</div>
{big(c)}
{sky}
{PKS if c.get('hallow') else ''}
<div class="rule"><i></i><b>Hosted by</b><i></i></div>
<div class="logos"><img class="ht" src="hightouch.png" alt="Hightouch"><img class="z" src="{c['zl']}" alt="Zaelot"></div>
</body></html>'''
    open(f'cover-{name}.html','w').write(html)
    out=os.path.abspath(f'luma-cover-{name}.png')
    subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless=new','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files','--window-size=1080,1080','--force-device-scale-factor=1','--virtual-time-budget=5000',f'--screenshot={out}','file://'+os.path.abspath(f'cover-{name}.html')],capture_output=True)
    print(out, os.path.exists(out))
