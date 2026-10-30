import cv2, json, subprocess, numpy as np, soundfile as sf, math, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from plan_cut import SEGS, o2t, CUTS, TOTAL
W,H,FPS=1080,1920,30
TAIL=0.6; DUR=TOTAL+TAIL; NF=int(round(DUR*FPS))
CR=(0xF6,0xF4,0xEF); GOLD=(0xE6,0xD6,0xAE); CREMA=(0xFB,0xF8,0xF1)
# ---------- cara -> centro suavizado
pts=np.array(json.load(open("build/face.json",encoding="utf-8")))
ts=pts[:,0]; fx=np.convolve(np.r_[[pts[0,1]]*3,pts[:,1],[pts[-1,1]]*3],np.ones(7)/7,"valid"); fy=np.convolve(np.r_[[pts[0,2]]*3,pts[:,2],[pts[-1,2]]*3],np.ones(7)/7,"valid")
# ---------- zoom por bloques
B=[0]+CUTS+[TOTAL]
KEY=[ [(0,1.14),(3.22,1.07)],
      [(3.22,1.00),(8.5,1.05),(14.37,1.01)],
      [(14.37,1.09),(15.68,1.07)],
      [(15.68,1.00),(17.14,1.02)],
      [(17.14,1.09),(22.73,1.06)],
      [(22.73,1.00),(27,1.06),(31,1.01),(36,1.07),(TOTAL,1.02)] ]
def ease(u): return 0.5-0.5*math.cos(math.pi*min(max(u,0),1))
def zoom(t):
    for kf in KEY:
        if kf[0][0]<=t<=kf[-1][0]+1e-6:
            for (t0,z0),(t1,z1) in zip(kf,kf[1:]):
                if t0<=t<=t1: return z0+(z1-z0)*ease((t-t0)/(t1-t0))
    return KEY[-1][-1][1]
# ---------- subtitulos
words=json.load(open("transcript/words.json",encoding="utf-8"))
vz,sr=sf.read("audio/voz_raw.wav"); hop=int(.01*sr); m=len(vz)//hop
env=20*np.log10(np.sqrt((vz[:m*hop].reshape(m,hop)**2).mean(1))+1e-9); env=np.convolve(env,np.ones(3)/3,"same"); der=np.r_[0,np.diff(env)]
FIX={"toques":"tokens","cloud":"Claude"}
ws=[]
for w in words:
    if 67.2<=w["s"]<=113.4:
        o=o2t(w["s"]); 
        if o is None:
            # palabra al borde de un tramo recortado: ajusta al siguiente tramo
            continue
        ws.append(dict(w=FIX.get(w["w"].strip(",.¿?").lower(),w["w"]),t=o,raw=w["w"]))
# afinar inicio con la envolvente (max subida +-)
prev=0
for x in ws:
    i0=max(int((x["t"]-0.12)*100),prev); i1=min(int((x["t"]+0.15)*100),m-1)
    on=(i0+int(np.argmax(der[i0:i1+1])))/100 if i1>i0 else i0/100
    x["on"]=on; prev=int(on*100)+5
KEYW={"subagentes","terminales","orquestador","contexto","tokens","rápido","texto","principal"}
# tarjetas de 2-4 palabras, cortadas en puntuacion
cards=[];cur=[]
def flush():
    global cur
    if cur: cards.append(cur); cur=[]
for x in ws:
    cur.append(x)
    ends=x["raw"].endswith((",","?","."))
    if len(cur)>=4 or (ends and len(cur)>=2) : flush()
flush()
# evitar tarjetas de 1 palabra: unir con la anterior si cabe
c2=[]
for c in cards:
    if len(c)==1 and c2 and len(c2[-1])<4: c2[-1]+=c
    else: c2.append(c)
cards=c2
json.dump([[ (x["w"],round(x["on"],2)) for x in c] for c in cards],open("build/cards.json","w",encoding="utf-8"),ensure_ascii=False)
F_SANS=ImageFont.truetype("fonts/montserrat-600.ttf",86); F_SERIF=ImageFont.truetype("fonts/playfair-display-latin-700-italic.ttf",118)
def card_img(c,dark=False):
    toks=[]
    for x in c:
        w=re.sub(r"[¿?]","",x["w"]).rstrip(",.")
        key=w.lower() in KEYW
        toks.append((w,key))
    # lineas
    def width(tk): 
        f=F_SERIF if tk[1] else F_SANS
        return f.getlength(tk[0])
    sp=F_SANS.getlength(" ")
    lines=[[]]; cw=0
    for tk in toks:
        wd=width(tk)+(sp if lines[-1] else 0)
        if cw+wd>940 and lines[-1]: lines.append([]); cw=0; wd=width(tk)
        lines[-1].append(tk); cw+=wd
    lh=130; hh=lh*len(lines)+40
    im=Image.new("RGBA",(W,hh),(0,0,0,0)); sh=Image.new("RGBA",(W,hh),(0,0,0,0))
    d=ImageDraw.Draw(im); ds=ImageDraw.Draw(sh)
    for li,l in enumerate(lines):
        tw=sum(width(t) for t in l)+sp*(len(l)-1); x0=(W-tw)/2; y=20+li*lh
        for tk in l:
            f=F_SERIF if tk[1] else F_SANS; col=((0xA8,0x8F,0x57) if tk[1] else (0x2A,0x29,0x26)) if dark else (GOLD if tk[1] else CREMA)
            yy=y+(-8 if tk[1] else 0)
            ds.text((x0,yy+6),tk[0],font=f,fill=(20,16,10,0 if dark else 150)); d.text((x0,yy),tk[0],font=f,fill=col+(255,))
            x0+=f.getlength(tk[0])+sp
    sh=sh.filter(ImageFilter.GaussianBlur(14)); sh.alpha_composite(im); 
    # sombra inferior (sin bordes): se devuelve la capa compuesta
    return sh,len(lines)
CARDIMG=[card_img(c) for c in cards]; CARDDARK=[card_img(c,True) for c in cards]
starts=[c[0]["on"]-2/FPS for c in cards]
ends=[]
for i,c in enumerate(cards):
    nxt=starts[i+1] if i+1<len(cards) else TOTAL
    last=c[-1]["on"]+0.55
    ends.append(min(max(last,c[0]["on"]+0.5),nxt-1/FPS,TOTAL))
# ---------- insert (sidebar de la pantalla)
IN0,IN1=o2t(73.8),o2t(76.7)
scr=cv2.VideoCapture("../crudo/PANTALLA 17-52-13.mp4")
def screen_frame(orig_t):
    scr.set(cv2.CAP_PROP_POS_MSEC,orig_t*1000); ok,f=scr.read(); return f
sidebar=[]
def dots():
    bg=np.full((H,W,3),CR[::-1],np.uint8)
    for y in range(12,H,24):
        for x in range(12,W,24): cv2.circle(bg,(x,y),1,(156,165,170),-1,cv2.LINE_AA)
    return bg
DOTS=dots()
def insert_frame(t):
    u=(t-IN0)/(IN1-IN0); ot=73.8+ (76.7-73.8)*u
    f=screen_frame(ot)[35:205,0:300]            # sidebar: Monoga OS / Ventas / Videos / CRM
    s=1000/300*(1.0+0.05*(1-u)); pw=int(300*s); ph=int(170*s)
    p=cv2.resize(f,(1000,567),interpolation=cv2.INTER_LANCZOS4)
    cv2.rectangle(p,(0,0),(999,566),(0xC8,0xB0,0x7A)[::-1],3)
    bg=DOTS.copy()
    # sombra calida difusa
    sh=np.zeros((H,W),np.float32); sh[470+34:470+34+567,40:1040]=0.34; sh=cv2.GaussianBlur(sh,(0,0),34)
    bg=(bg*(1-sh[...,None])+np.array([44,74,90])[None,None,:]*sh[...,None]).astype(np.uint8)
    y0=470; bg[y0:y0+567,40:1040]=p
    return bg
# ---------- render
cap=cv2.VideoCapture("build/cut_graded.mkv")
ff=subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-crf","14","-preset","medium","-pix_fmt","yuv420p","build/video_silent.mp4"],stdin=subprocess.PIPE)
s0=H/720
last=None
for n in range(NF):
    t=n/FPS
    if n<cap.get(cv2.CAP_PROP_FRAME_COUNT):
        ok,src=cap.read()
        if ok: last=src
    src=last
    tt=min(t,TOTAL)
    z=zoom(tt); s=s0*z
    cx=float(np.interp(tt,ts,fx)); cy=float(np.interp(tt,ts,fy))
    vw,vh=W/s,H/s
    cx=min(max(cx,vw/2),1280-vw/2); cyy=min(max(0.5*(360+cy),vh/2),720-vh/2)
    M=np.array([[s,0,W/2-s*cx],[0,s,H/2-s*cyy]],np.float32)
    fr=cv2.warpAffine(src,M,(W,H),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REPLICATE)
    # insert con disolvencia de 5 cuadros
    a=0
    if IN0-5/FPS<=t<=IN1+5/FPS:
        a=min(1,(t-(IN0-5/FPS))/(5/FPS),((IN1+5/FPS)-t)/(5/FPS))
        a=max(a,0)
        ins=insert_frame(min(max(t,IN0),IN1))
        fr=cv2.addWeighted(fr,1-a,ins,a,0)
    # sombra inferior leve sobre persona
    if a<1:
        g=np.linspace(0,1,H)[:,None]**3*0.28*(1-a)
        fr=(fr*(1-g[...,None])).astype(np.uint8)
    # tarjeta
    for i,(st,en) in enumerate(zip(starts,ends)):
        if st<=t<en:
            im,nl=(CARDDARK if a>0.5 else CARDIMG)[i]; hh=im.size[1]
            # fundido 2 cuadros
            al=min(1,(t-st)/(2/FPS))
            y=1410-hh+40
            pil=Image.fromarray(cv2.cvtColor(fr,cv2.COLOR_BGR2RGB)).convert("RGBA")
            if al<1:
                im=im.copy(); im.putalpha(im.getchannel("A").point(lambda v:int(v*al)))
            pil.alpha_composite(im,(0,y)); fr=cv2.cvtColor(np.array(pil.convert("RGB")),cv2.COLOR_RGB2BGR)
            break
    # fade de salida a pastel (ultimos 0,4 s) 
    fo=(t-(DUR-0.45))/0.35
    if fo>0:
        fo=min(fo,1); fr=(fr*(1-fo)+np.array(CR[::-1])*fo).astype(np.uint8)
    # fade de entrada desde pastel (3 cuadros)
    if n<3: fi=1-(n+1)/4; fr=(fr*(1-fi)+np.array(CR[::-1])*fi).astype(np.uint8)
    ff.stdin.write(fr.tobytes())
ff.stdin.close(); ff.wait(); print("frames",NF,"cards",len(cards),"insert",IN0,IN1)
