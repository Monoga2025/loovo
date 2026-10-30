# EDL para audio de calle (sin silencios reales): bordes = mínimo de energía
# (voz filtrada 150-4000 Hz) en una ventana corta fuera de las palabras de Whisper.
import json, numpy as np, soundfile as sf
x,sr=sf.read("audio/voz_env.wav");h=int(sr*.01);n=len(x)//h
db=20*np.log10(np.sqrt((x[:n*h].reshape(n,h)**2).mean(1))+1e-9)
takes=json.load(open("plan/takes.json",encoding="utf-8"));words=json.load(open("transcript/words.json",encoding="utf-8"))
def lo(a,b):
    i,j=int(a*100),int(b*100); k=i+int(np.argmin(db[i:j])); return k/100, db[k]
clips=[];rep=[]
for t in takes["takes"]:
    ws=[w for w in words if w["s"]>=t["start"]-.06 and w["e"]<=t["end"]+.06]
    runs,cur=[],[ws[0]]
    for a,b in zip(ws,ws[1:]):
        if b["s"]-a["e"]>0.45: runs.append(cur);cur=[]
        cur.append(b)
    runs.append(cur)
    for i,r in enumerate(runs):
        s,ds=lo(r[0]["s"]-0.18,r[0]["s"]+0.02); nx=[w["s"] for w in words if w["s"]>=r[-1]["e"]-0.01 and w is not r[-1]]
        e,de=lo(r[-1]["e"]-0.02,min(r[-1]["e"]+0.22,(min(nx) if nx else 1e9)+0.02))
        cid=f"{t['id']}{'abcdefgh'[i]}" if len(runs)>1 else t["id"]
        clips.append(dict(id=cid,start=round(s,3),end=round(e,3),vs=r[0]["s"],ve=r[-1]["e"],ws=r[0]["s"],we=r[-1]["e"],note=" ".join(w["w"] for w in r)))
        rep.append(f"{cid}: {s:.2f}({ds:.0f} dB) - {e:.2f}({de:.0f} dB) | {clips[-1]['note'][:50]}")
edl={k:takes[k] for k in ("source","target","tolerance","max")};edl["clips"]=clips
json.dump(edl,open("plan/edl.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("\n".join(rep).encode("ascii","replace").decode()); print("total %.2f"%sum(c["end"]-c["start"] for c in clips))
