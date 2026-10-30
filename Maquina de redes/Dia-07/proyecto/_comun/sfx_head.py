"""Pista de SFX (48 kHz estéreo) en los beats de plan/beats.json (los mismos que usa la composición).
Sintetizados por código (scripts/make_sfx_lib.py) + glitch Mixkit 1022 (Mixkit SFX Free License) en el invert flash."""
import json, numpy as np, soundfile as sf
from scipy import signal
src = open("scripts/make_sfx_lib.py", encoding="utf-8").read()
G = {}; exec("import numpy as np\nSR = 48000\nrng = np.random.default_rng(7)\ndef tt" + src.split("def tt", 1)[1].split("GEN = {")[0], G)
SR = 48000; F = 1 / 30
B = json.load(open("plan/beats.json")); E = json.load(open("plan/edl.json", encoding="utf-8")); TOT = E["total"]
rng = np.random.default_rng(11)
def hiw(d=0.42, peak=0.55):
    t = np.arange(int(d * SR)) / SR; n = rng.standard_normal(len(t))
    n = signal.sosfilt(signal.butter(4, [2000, 16000], "band", fs=SR, output="sos"), n)
    u = t / d; env = np.where(u < peak, (u / peak) ** 2, np.exp(-(u - peak) * 9))
    return n * env * 0.35, 0.5
mx, _ = sf.read("assets_src/sfx_mixkit_1022_trim.wav", always_2d=True)
mx = signal.resample_poly(mx, 160, 147, axis=0)[:int(0.30 * SR)]; mx[-int(0.1 * SR):] *= np.linspace(1, 0, int(0.1 * SR))[:, None]
C = []
def c(t, ty, g): C.append(dict(t=round(t, 3), type=ty, gain=g))
