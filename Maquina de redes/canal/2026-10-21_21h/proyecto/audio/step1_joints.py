# Juntas = suma acumulada de duraciones de plan/edl.json (build_cut.py aplica fades de 30 ms en cada borde)
import json, numpy as np, soundfile as sf
x, sr = sf.read("build/voice-cut.wav")
if x.ndim > 1: x = x.mean(1)
e = json.load(open("plan/edl.json"))
J=[]; t=0
for k in e["clips"][:-1]:
    t+=k["end"]-k["start"]; J.append(round(t,3))
rms=lambda a:20*np.log10(np.sqrt(np.mean(a**2))+1e-9)
act=[]
for n,j in enumerate(J,1):
    w=[rms(x[int((j-0.05+k*0.02)*sr):int((j-0.05+k*0.02)*sr)+int(0.02*sr)]) for k in range(3)]
    # 20 ms justo tras la junta (siguiente toma) y últimos 30 ms previos
    a=max(w)>-36; act.append(a)
    print(f"junta {n} ({n}->{n+1}) t={j:.3f}s ventanas 20ms previas dB={[round(float(v),1) for v in w]} voz_activa={a}")
print("juntas con voz activa en los 50 ms previos:",sum(act),"de",len(J),[J[i] for i,a in enumerate(act) if a])
json.dump(J,open("audio/joints.json","w"))
