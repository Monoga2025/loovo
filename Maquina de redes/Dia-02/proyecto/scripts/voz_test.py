# Compara cadenas de limpieza: piso de ruido (percentil 10 de tramas de 20 ms), nivel de habla (p90) y SNR
import sys, numpy as np, soundfile as sf
for p in sys.argv[1:]:
    x, sr = sf.read(p)
    if x.ndim > 1: x = x.mean(1)
    h = int(sr * 0.02); n = len(x) // h
    db = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
    lo, hi = np.percentile(db, 10), np.percentile(db, 90)
    print(f"{p:36s} piso {lo:6.1f} dB | habla {hi:6.1f} dB | SNR {hi - lo:5.1f} dB")
