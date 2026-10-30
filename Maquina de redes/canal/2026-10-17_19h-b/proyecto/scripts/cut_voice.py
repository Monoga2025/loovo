"""Voz en la línea final desde audio/declip48.wav (mono, x0,5) con fundidos de 30 ms por pieza -> audio/voz_cut.wav (48 kHz)."""
import json, numpy as np, soundfile as sf
E = json.load(open("plan/edl.json")); x, sr = sf.read("audio/declip48.wav")
out = np.zeros(int(round(E["total"] * sr))); f = int(0.03 * sr)
for p in E["pieces"]:
    s = x[int(round(p["a"] * sr)):int(round(p["b"] * sr))].copy()
    r = np.linspace(0, 1, f); s[:f] *= r; s[-f:] *= r[::-1]
    i = int(round(p["o"] * sr)); out[i:i + len(s)] += s
sf.write("audio/voz_cut.wav", out.astype(np.float32), sr, subtype="FLOAT"); print("ok", len(out) / sr)
