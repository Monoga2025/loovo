import json
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfiltfilt

x, sr = sf.read("fix/voice48.wav")
mono = x.ndim == 1
if mono: x = x[:, None]
ev = json.load(open("fix/events.json"))
pause_events = {8.21}
strong = {20.0, 23.28}
lo_sos = butter(4, [60, 500], "bandpass", fs=sr, output="sos")
out = x.copy()
n = len(x)
def ramp(t0, t1, t2, t3, depth):
    g = np.ones(n)
    i0, i1, i2, i3 = [int(max(0, min(n-1, t*sr))) for t in (t0, t1, t2, t3)]
    g[i0:i1] = 1 - (1 - depth) * 0.5 * (1 - np.cos(np.linspace(0, np.pi, max(1, i1-i0))))
    g[i1:i2] = depth
    g[i2:i3] = depth + (1 - depth) * 0.5 * (1 - np.cos(np.linspace(0, np.pi, max(1, i3-i2))))
    return g
for ch in range(x.shape[1]):
    low = sosfiltfilt(lo_sos, x[:, ch])
    gain = np.ones(n)
    for t in ev:
        depth = 0.03 if t in pause_events else (0.06 if t in strong else 0.2)
        gain = np.minimum(gain, ramp(t-0.070, t-0.050, t+0.075, t+0.110, depth))
    out[:, ch] = x[:, ch] - low * (1 - gain)
    for t in ev:
        if t in pause_events or t in strong:
            g = ramp(t-0.065, t-0.050, t+0.035 if t in strong else t+0.075, t+0.060 if t in strong else t+0.110, 0.03 if t in pause_events else 0.5)
            out[:, ch] = np.where(g < 1, out[:, ch] * g, out[:, ch])
sf.write("fix/voice_clean48.wav", out[:, 0] if mono else out, sr, subtype="PCM_16")
print("ok", len(ev), "eventos suavizados")
