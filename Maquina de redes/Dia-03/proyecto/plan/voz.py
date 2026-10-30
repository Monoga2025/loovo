import json, numpy as np, soundfile as sf, librosa
x, sr = sf.read("audio/audio.wav")
w = json.load(open("transcript/words.json", encoding="utf-8"))
segs=[];cur=[]
for t in w:
    if cur and t["s"]-cur[-1]["e"]>0.45: segs.append(cur);cur=[]
    cur.append(t)
segs.append(cur)
for s in segs:
    a,b=s[0]["s"],s[-1]["e"]; y=x[int(a*sr):int(b*sr)].astype(np.float32)
    f0,_,_=librosa.pyin(y,fmin=70,fmax=400,sr=sr,frame_length=1024); f=f0[~np.isnan(f0)]
    med=np.median(f) if len(f)>5 else None
    txt=" ".join(t["w"] for t in s)
    print(f"{a:6.2f}-{b:6.2f} f0={med and round(float(med))} n={len(f)} | {txt[:60]}".encode("ascii","replace").decode())
