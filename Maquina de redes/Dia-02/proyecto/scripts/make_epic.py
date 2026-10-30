import sys
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve

out = sys.argv[1]
DUR = float(sys.argv[2])
STING = float(sys.argv[3]) if len(sys.argv) > 3 else None
BPM = 100
SR = 48000
beat = 60 / BPM
bar = 4 * beat
section = 2 * bar
n = int(SR * (DUR + 1.5))
rng = np.random.default_rng(7)


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def lp(x, f, order=2):
    return sosfilt(butter(order, f, "low", fs=SR, output="sos"), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], "bandpass", fs=SR, output="sos"), x)


def add(buf, start, sig):
    i = int(start * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i]


def saw(freq, length, phase=0.0):
    tt = np.arange(int(length * SR)) / SR
    return 2.0 * ((freq * tt + phase) % 1.0) - 1.0


def swell(length, attack, release):
    m = int(length * SR)
    e = np.ones(m)
    a = int(attack * SR)
    r = int(release * SR)
    if a > 0:
        e[:a] = np.linspace(0, 1, a) ** 1.5
    if r > 0:
        e[-r:] *= np.linspace(1, 0, r) ** 1.5
    return e


def intensity(t):
    pts = [(0, 0.55), (4.8, 0.6), (9.6, 0.75), (14.4, 0.85), (24.0, 1.0), (33.6, 1.0), (DUR + 1.5, 0.8)]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return np.interp(t, xs, ys)


tgrid = np.arange(n) / SR
inten = intensity(tgrid)

chords = [
    ([50, 53, 57, 62], 38),
    ([46, 50, 53, 58], 34),
    ([53, 57, 60, 65], 41),
    ([48, 52, 55, 60], 36),
    ([50, 53, 57, 62], 38),
    ([46, 50, 53, 58], 34),
    ([48, 52, 55, 60], 36),
    ([50, 53, 57, 62], 38),
]

wetL = np.zeros(n)
wetR = np.zeros(n)
dryL = np.zeros(n)
dryR = np.zeros(n)

for k, (notes, root) in enumerate(chords):
    start = k * section
    length = section + 1.4
    env = swell(length, 1.0, 1.3)
    padL = np.zeros(int(length * SR))
    padR = np.zeros(int(length * SR))
    for m in notes:
        f = mtof(m)
        for cents in (-14, -7, 0, 7, 14):
            fd = f * 2 ** (cents / 1200)
            padL += saw(fd, length, rng.random()) * (1.0 if cents <= 0 else 0.6)
            padR += saw(fd, length, rng.random()) * (1.0 if cents >= 0 else 0.6)
    padL = lp(padL * env, 2300) * 0.035
    padR = lp(padR * env, 2300) * 0.035
    add(wetL, start, padL)
    add(wetR, start, padR)

    sub_len = length
    ts = np.arange(int(sub_len * SR)) / SR
    f0 = mtof(root + 12)
    sub = np.sin(2 * np.pi * f0 * ts) + 0.5 * np.sin(2 * np.pi * 2 * f0 * ts) + 0.25 * np.sin(2 * np.pi * 3 * f0 * ts)
    sub = np.tanh(1.6 * sub) * swell(sub_len, 0.05, 0.6) * 0.22
    if start >= 14.4:
        eighth = beat / 2
        ph = (ts % eighth) / eighth
        sub = sub * (0.35 + 0.65 * np.exp(-3.2 * ph))
    add(dryL, start, sub)
    add(dryR, start, sub)

    if start >= 14.4:
        hero = np.zeros(int(length * SR))
        for m in (notes[0] + 12, notes[2] + 12):
            f = mtof(m)
            vib = 1 + 0.003 * np.sin(2 * np.pi * 5.2 * np.arange(len(hero)) / SR)
            hero += saw(f, length) * vib + 0.7 * saw(f * 1.004, length)
        hero = lp(hero * swell(length, 0.5, 1.2), 1700) * 0.05
        add(wetL, start, hero)
        add(wetR, start, hero * 0.92)

    if start >= 24.0:
        choir = np.zeros(int(length * SR))
        for m in (notes[1] + 24, notes[2] + 24, notes[3] + 12):
            f = mtof(m)
            vib = 1 + 0.004 * np.sin(2 * np.pi * 5.6 * np.arange(len(choir)) / SR + rng.random() * 6)
            choir += saw(f, length) * vib
        choir = (bp(choir, 600, 900, 2) + 0.8 * bp(choir, 1000, 1400, 2) + 0.4 * bp(choir, 2300, 2900, 2)) * swell(length, 1.1, 1.3) * 0.07
        add(wetL, start, choir)
        add(wetR, start, choir)


def taiko(vel, tail=0.9):
    m = int(tail * SR)
    ts = np.arange(m) / SR
    pitch = 46 + 60 * np.exp(-ts * 22)
    ph = 2 * np.pi * np.cumsum(pitch) / SR
    body = np.sin(ph) * np.exp(-ts * 5.0)
    skin = bp(rng.standard_normal(m), 180, 2200) * np.exp(-ts * 38) * 0.55
    return (body + skin) * vel


bars = int(DUR / bar) + 2
for b in range(bars):
    tb = b * bar
    iv = float(intensity(tb))
    add(dryL, tb, taiko(0.6 * iv))
    add(dryR, tb, taiko(0.6 * iv))
    if tb >= 4.8:
        add(wetL, tb + 2 * beat, taiko(0.45 * iv))
        add(wetR, tb + 2 * beat, taiko(0.45 * iv))
    if tb >= 9.6:
        for q in (3, 3.5):
            add(wetL, tb + q * beat, taiko(0.3 * iv, 0.5))
            add(wetR, tb + q * beat, taiko(0.3 * iv, 0.5))
    if tb >= 14.4:
        for e in range(8):
            if e in (1, 4, 6):
                continue
            add(dryL, tb + e * beat / 2, taiko(0.16 * iv, 0.35))
            add(dryR, tb + e * beat / 2, taiko(0.16 * iv, 0.35))


def riser(length, peak):
    m = int(length * SR)
    ts = np.arange(m) / SR
    nz = rng.standard_normal(m)
    sig = np.zeros(m)
    chunks = 24
    for c in range(chunks):
        a, z = int(c * m / chunks), int((c + 1) * m / chunks)
        cut = 300 * (9000 / 300) ** (c / (chunks - 1))
        seg = hp(nz[a:z], min(cut, 18000), 1) if a < z else nz[a:z]
        sig[a:z] = seg
    return sig * (ts / length) ** 2.2 * peak


for tr in (12.4, 22.0, 31.6):
    r = riser(2.0, 0.22)
    add(wetL, tr, r)
    add(wetR, tr, r[::-1] if False else r * 0.9)


def crash(length, peak):
    m = int(length * SR)
    ts = np.arange(m) / SR
    return hp(rng.standard_normal(m), 4500, 2) * np.exp(-ts * 1.5) * peak


for tc, pk in ((0.0, 0.25), (14.4, 0.14), (24.0, 0.18), (33.6, 0.3)):
    c = crash(3.0, pk)
    add(wetL, tc, c)
    add(wetR, tc, c * 0.95)

for tb in (0.0, 33.6):
    big = taiko(1.0, 2.0) * 1.4
    add(dryL, tb, big)
    add(dryR, tb, big)

if STING is not None:
    big2 = taiko(1.0, 2.0) * 1.2
    add(dryL, STING, big2)
    add(dryR, STING, big2)
    c2 = crash(3.0, 0.28)
    add(wetL, STING, c2)
    add(wetR, STING, c2 * 0.95)

irm = int(2.4 * SR)
ti = np.arange(irm) / SR
irL = rng.standard_normal(irm) * np.exp(-ti / 0.75)
irR = rng.standard_normal(irm) * np.exp(-ti / 0.75)
irL = lp(irL, 7000)
irR = lp(irR, 7000)
irL /= np.sqrt(np.sum(irL ** 2))
irR /= np.sqrt(np.sum(irR ** 2))
revL = fftconvolve(wetL, irL)[:n]
revR = fftconvolve(wetR, irR)[:n]

L = dryL + 0.7 * wetL + 0.55 * revL
R = dryR + 0.7 * wetR + 0.55 * revR
L = L * (0.55 + 0.45 * inten)
R = R * (0.55 + 0.45 * inten)

total = int(DUR * SR)
L = L[:total]
R = R[:total]
fade = int(1.0 * SR)
L[-fade:] *= np.linspace(1, 0, fade)
R[-fade:] *= np.linspace(1, 0, fade)
st = np.stack([L, R], axis=1)
st = np.tanh(1.2 * st) / np.tanh(1.2)
st = st / np.max(np.abs(st)) * 0.8
sf.write(out, st.astype(np.float32), SR, subtype="PCM_16")
print("ok", out, round(len(st) / SR, 2), "s")
