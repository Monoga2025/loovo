# FILE: make_sfx.py
# Uso: python3 make_sfx.py sfx.json salida.wav duracion_s
# Pista de efectos sintetizada por código (libre de derechos): un sonido en
# cada golpe visual, en los tiempos de sfx.json. 48 kHz estéreo.
import json, sys, wave
import numpy as np

cues = json.load(open(sys.argv[1], encoding="utf-8"))
out, dur = sys.argv[2], float(sys.argv[3])
SR = 48000
rng = np.random.default_rng(7)
n = int(dur * SR)
L, R = np.zeros(n), np.zeros(n)


def tt(sec):
    return np.arange(int(sec * SR)) / SR


def lowpass(x, a):
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc += a * (v - acc)
        y[i] = acc
    return y


def whoosh():
    t = tt(0.45)
    noise = rng.standard_normal(len(t))
    env = np.sin(np.pi * np.clip(t / 0.45, 0, 1)) ** 2
    # barrido de filtro: más brillante en el centro
    lo = lowpass(noise, 0.08)
    hi = noise - lowpass(noise, 0.3)
    mix = lo + hi * env * 0.6
    return mix * env * 0.5, 0.25  # (señal, paneo izquierda->derecha)


def hit():
    t = tt(0.6)
    f = 42 + 90 * np.exp(-t * 28)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 5.5)
    click = rng.standard_normal(len(t)) * np.exp(-t * 120) * 0.3
    return (body + click) * 0.9, 0


def pop():
    t = tt(0.12)
    f = 900 * np.exp(-t * 25) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 40) * 0.5, 0


def click():
    t = tt(0.05)
    s = np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 160)
    return (s + rng.standard_normal(len(t)) * np.exp(-t * 300) * 0.2) * 0.45, 0


def swish():
    t = tt(0.7)
    noise = rng.standard_normal(len(t))
    hi = noise - lowpass(noise, 0.5)
    env = np.minimum(t / 0.5, 1) * np.exp(-np.maximum(t - 0.5, 0) * 25)
    return hi * env * 0.25, 0.4


def riser():
    t = tt(0.25)
    f = 200 + 1400 * (t / 0.25) ** 2
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * (t / 0.25) * 0.25
    return s, 0


def glitch():
    t = tt(0.32)
    sq = np.sign(np.sin(2 * np.pi * 180 * t)) * 0.25
    gate = (np.floor(t * 40) % 2 == 0).astype(float)
    bits = np.round(rng.standard_normal(len(t)) * 3) / 3 * 0.25
    return (sq * gate + bits * (1 - gate)) * np.exp(-t * 4), 0


def scramble():
    t = tt(0.4)
    s = np.zeros(len(t))
    for k in range(7):
        i0 = int(k * 0.06 * SR)
        seg = tt(0.03)
        s[i0:i0 + len(seg)] += np.sin(2 * np.pi * (1200 + 260 * k) * seg) * np.exp(-seg * 90)
    return s * 0.3, 0


def step(p):
    t = tt(0.18)
    f = 520 * p
    s = (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-t * 22)
    return s * 0.4, 0


def ding():
    t = tt(1.0)
    s = sum(a * np.sin(2 * np.pi * f * t) for f, a in ((1320, 1), (2640, 0.4), (3960, 0.15)))
    return s * np.exp(-t * 4.5) * 0.3, 0


GEN = {"whoosh": whoosh, "hit": hit, "pop": pop, "click": click, "swish": swish,
       "riser": riser, "glitch": glitch, "scramble": scramble, "ding": ding}

for c in cues:
    sig, pan = step(c.get("pitch", 1.0)) if c["type"] == "step" else GEN[c["type"]]()
    sig = sig * c.get("gain", 1.0)
    i = int(c["t"] * SR)
    sig = sig[:max(n - i, 0)]
    if pan:  # barrido estéreo para whooshes
        p = np.linspace(-pan, pan, len(sig))
    else:
        p = np.zeros(len(sig))
    L[i:i + len(sig)] += sig * (1 - p) / 2 * 2 ** 0.5
    R[i:i + len(sig)] += sig * (1 + p) / 2 * 2 ** 0.5

peak = max(abs(L).max(), abs(R).max(), 1e-9)
st = (np.stack([L, R], 1) / peak * 0.8 * 32767).astype(np.int16)
wf = wave.open(out, "wb")
wf.setnchannels(2)
wf.setsampwidth(2)
wf.setframerate(SR)
wf.writeframes(st.tobytes())
wf.close()
print(f"{len(cues)} efectos -> {out}")
