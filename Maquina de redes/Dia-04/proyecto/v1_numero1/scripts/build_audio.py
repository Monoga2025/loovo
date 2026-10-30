"""Voz en la línea final: mic del PC (100 %) + celular (15 %, HPF 80 Hz), cortes con fundidos de 12 ms.
Uso: build_audio.py  -> audio/voz_raw.wav (48 kHz mono float) y audio/cel_raw.wav (solo celular, para verificar sincronía)"""
import json, subprocess, numpy as np, soundfile as sf
from scipy import signal
E = json.load(open("plan/edl.json", encoding="utf-8")); SR = 48000
PC = "../../CAMARA 10-45-16.mp4"
def rd(src, t0, d):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0:.6f}", "-t", f"{d:.6f}", "-i", src, "-vn", "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).astype(np.float64); n = int(round(d * SR))
    return np.pad(x, (0, max(0, n - len(x))))[:n]
hp = signal.butter(2, 80, "highpass", fs=SR, output="sos")
N = int(round(E["total"] * SR)) + SR
voz, cel = np.zeros(N), np.zeros(N)
F = int(0.012 * SR); r = np.sin(np.linspace(0, np.pi / 2, F)) ** 2
for s in E["segs"]:
    if not s["cam"]: continue
    d = s["dur"]; pc = rd(PC, s["t0"] + s["off"], d); c = rd(s["src"], s["t0"], d)
    m = pc + 0.15 * signal.sosfiltfilt(hp, c)
    for x in (m, c):
        x[:F] *= r; x[-F:] *= r[::-1]
    i = int(round(s["start"] * SR))
    voz[i:i + len(m)] += m; cel[i:i + len(c)] += c
    print(s["id"], "ok")
N = int(round(E["total"] * SR))
sf.write("audio/voz_raw.wav", voz[:N].astype(np.float32), SR, subtype="FLOAT")
sf.write("audio/cel_raw.wav", cel[:N].astype(np.float32), SR, subtype="FLOAT")
print("dur", N / SR)
