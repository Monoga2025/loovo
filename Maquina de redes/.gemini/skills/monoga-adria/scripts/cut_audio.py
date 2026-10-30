"""Aplica los cortes de video al audio mezclado con fundidos de 12 ms. Uso: cut_audio.py in.wav out.wav"""
import sys, numpy as np, soundfile as sf
x, sr = sf.read(sys.argv[1], always_2d=True)
SEGS = [(0.42, 2.60), (2.80, 6.14)]
FADE = 0.012
parts = []
for a, b in SEGS:
    s = x[int(round(a*sr)):int(round(b*sr))].copy()
    n = int(FADE*sr); r = np.sin(np.linspace(0, np.pi/2, n))**2
    s[:n] *= r[:, None]; s[-n:] *= r[::-1][:, None]
    parts.append(s)
y = np.concatenate(parts)
sf.write(sys.argv[2], y, sr, subtype="PCM_24")
print("dur", len(y)/sr)
