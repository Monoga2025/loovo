"""Desfase voz final (mic PC) vs celular por tramo (GCC-PHAT, 300-4000 Hz). + = la voz del PC va retrasada."""
import json, numpy as np, soundfile as sf
from scipy import signal
v, sr = sf.read("audio/voz_raw.wav"); c, _ = sf.read("audio/cel_raw.wav")
E = json.load(open("plan/edl.json", encoding="utf-8"))
sos = signal.butter(4, [300, 4000], "band", fs=sr, output="sos"); v = signal.sosfiltfilt(sos, v); c = signal.sosfiltfilt(sos, c)
M = int(0.1 * sr)
for s in E["segs"]:
    if not s["cam"]: continue
    a, b = int(s["start"] * sr), int(s["end"] * sr)
    x, y = v[a:b], c[a:b]; n = 1 << (len(x) * 2).bit_length()
    X, Y = np.fft.rfft(x, n), np.fft.rfft(y, n); C = X * np.conj(Y); C /= np.abs(C) + 1e-12
    cc = np.fft.irfft(C, n); cc = np.r_[cc[-M:], cc[:M + 1]]; k = int(np.argmax(cc)) - M
    print(f"{s['id']:4s} lag {1000 * k / sr:+6.1f} ms  q {cc.max() / (np.median(np.abs(cc)) + 1e-12):6.1f}")
