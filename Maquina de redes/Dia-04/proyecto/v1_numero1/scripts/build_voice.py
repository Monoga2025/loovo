"""Voz en la línea final: SOLO mic del PC (canal 1 de CAMARA 10-45-16), HPF 70 Hz, fundidos 12 ms por corte.
-> audio/voz_raw.wav (48 kHz mono float) y audio/cel_raw.wav (celular, solo para verificar sincronía; no va al video)."""
import json, subprocess, numpy as np, soundfile as sf
from scipy import signal
E = json.load(open("plan/edl.json", encoding="utf-8")); SR = 48000
PC = "../../CAMARA 10-45-16.mp4"
def rd(src, t0, d, pan=None):
    af = ["-af", "pan=mono|c0=c0"] if pan else ["-ac", "1"]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0:.6f}", "-t", f"{d:.6f}", "-i", src, "-vn", *af, "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).astype(np.float64); n = int(round(d * SR))
    return np.pad(x, (0, max(0, n - len(x))))[:n]
hp = signal.butter(2, 70, "highpass", fs=SR, output="sos")
N = int(round(E["total"] * SR))
voz, cel = np.zeros(N + SR), np.zeros(N + SR)
F = int(0.012 * SR); r = np.sin(np.linspace(0, np.pi / 2, F)) ** 2
for s in E["segs"]:
    if not s["cam"]: continue
    d = s["dur"]; pre = 0.5
    pc = signal.sosfiltfilt(hp, rd(PC, s["t0"] + s["off"] - pre, d + pre, pan=True))[int(pre * SR):]   # filtro con margen: sin transitorio
    c = rd(s["src"], s["t0"], d)
    for x in (pc, c):
        x[:F] *= r; x[-F:] *= r[::-1]
    i = int(round(s["start"] * SR))
    voz[i:i + len(pc)] += pc; cel[i:i + len(c)] += c
sf.write("audio/voz_raw.wav", voz[:N].astype(np.float32), SR, subtype="FLOAT")
sf.write("audio/cel_raw.wav", cel[:N].astype(np.float32), SR, subtype="FLOAT")
print("dur", N / SR)
