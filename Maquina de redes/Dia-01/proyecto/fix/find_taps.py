import sys, json
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, find_peaks

x, sr = sf.read("build/cut_audio.wav")
if x.ndim > 1: x = x.mean(axis=1)
sos = butter(4, [60, 6000], "bandpass", fs=sr, output="sos")
y = sosfilt(sos, x)
win = int(0.004 * sr)
env = np.sqrt(np.convolve(y**2, np.ones(win) / win, "same"))
env_db = 20 * np.log10(env + 1e-9)
med_win = int(0.25 * sr)
from scipy.ndimage import median_filter, uniform_filter1d
step = int(0.01 * sr)
env_ds = env_db[::step]
base = median_filter(env_ds, size=int(0.25 / 0.01) | 1)
rise = env_ds - base
peaks, props = find_peaks(rise, height=float(sys.argv[1]) if len(sys.argv) > 1 else 9, distance=3)
words = json.load(open("build/words_out.json"))
ws = words if isinstance(words, list) else words.get("words", words)
def word_at(t):
    for w in ws:
        s, e = w.get("start", w.get("s", 0)), w.get("end", w.get("e", 0))
        if s - 0.02 <= t <= e + 0.02: return w.get("word", w.get("text", "?"))
    return None
out = []
for p in peaks:
    t = p * step / sr
    out.append((round(t, 3), round(float(rise[p]), 1), round(float(env_ds[p]), 1), word_at(t)))
print(len(out), "candidatos (t, subida dB, nivel dB, palabra)")
for o in out: print(o)
json.dump(out, open("fix/taps_candidates.json", "w"))
