"""Envolvente RMS 20 ms del crudo (../_scan/cel48.wav). Uso: env.py t0 t1 [t0 t1 ...]"""
import sys, numpy as np, soundfile as sf
f = sf.SoundFile("C:/Users/you/Desktop/Loovo-42/Dia-07/proyecto/_scan/cel48.wav"); sr = f.samplerate
a = sys.argv[1:]
for i in range(0, len(a), 2):
    t0, t1 = float(a[i]), float(a[i+1]); f.seek(int(t0*sr)); x = f.read(int((t1-t0)*sr))
    h = int(0.02*sr); n = len(x)//h; r = 20*np.log10(np.sqrt((x[:n*h].reshape(n,h)**2).mean(1))+1e-9)
    s = f"== {t0}-{t1}"
    for k, v in enumerate(r):
        if k % 10 == 0: s += f"\n{t0+k*0.02:7.2f} "
        s += f"{int(round(v)):4d}"
    print(s)
