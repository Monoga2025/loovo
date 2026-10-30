"""Envolvente RMS (20 ms) de un wav alineado a la línea del celular. Uso: env.py wav offset t0 t1 [t0 t1 ...]
wav = audio cuyo t=0 corresponde a t_cel=offset (p.ej. B_pc.wav -> 0)."""
import sys, numpy as np, soundfile as sf
f = sf.SoundFile(sys.argv[1]); sr = f.samplerate; base = float(sys.argv[2])
a = sys.argv[3:]
for i in range(0, len(a), 2):
    t0, t1 = float(a[i]), float(a[i+1])
    f.seek(int((t0-base)*sr)); x = f.read(int((t1-t0)*sr))
    if x.ndim > 1: x = x.mean(1)
    h = int(0.02*sr); n = len(x)//h
    r = 20*np.log10(np.sqrt((x[:n*h].reshape(n,h)**2).mean(1))+1e-9)
    print(f"== {t0}-{t1}")
    s = ""
    for k, v in enumerate(r):
        t = t0 + k*0.02
        if k % 10 == 0: s += f"\n{t:7.2f} "
        s += f"{int(round(v)):4d}"
    print(s)
