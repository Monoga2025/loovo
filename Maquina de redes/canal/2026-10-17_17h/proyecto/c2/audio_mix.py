"""Audio del corte 2: SFX (make_sfx.py del Día 1 + glitch Mixkit en los invert flash), música por código
(Re menor, 112 BPM, libre de derechos) con ducking por voz ~7 dB bajo la voz, mezcla y ganancia lineal a -17,6 LUFS.
-> audio/sfx.wav, audio/music.wav, audio/final.wav"""
import json, re, subprocess, numpy as np, soundfile as sf
from scipy import signal
SR = 48000; E = json.load(open("plan/edl.json")); TOT = E["total"]; N = int(TOT * SR)
FLASH = [17.20, 36.95]   # invert flash (corte); el pico es 1 cuadro antes
C = []
def c(t, ty, g, **k): C.append(dict(t=round(t, 3), type=ty, gain=g, **k))
c(0.0, "hit", .8); c(0.24, "click", .5); c(0.41, "pop", .5); c(1.12, "swish", .5)
for i in range(4): c(1.30 + i * .07, "pop", .35)
c(1.86, "click", .4); c(2.33, "whoosh", .25); c(3.04, "hit", .5); c(4.46, "swish", .45); c(4.95, "hit", .8); c(4.97, "glitch", .3)
c(5.37, "click", .45); c(5.72, "swish", .35); c(5.63, "whoosh", .8); c(5.95, "hit", .5)
c(6.15, "whoosh", .45); c(7.90, "pop", .45); c(8.10, "swish", .35); c(8.52, "whoosh", .6)
for i, t in enumerate([8.69, 8.96, 9.18, 9.37]): c(t - .05, "step", .3, pitch=1 + .12 * i)
c(9.90, "pop", .7); c(10.55, "swish", .35)
for i in range(3): c(10.65 + i * .08, "pop", .4)
c(11.25, "whoosh", .8); c(11.96, "click", .45); c(12.14, "hit", .6); c(12.45, "whoosh", .35); c(13.58, "pop", .55)
c(15.37, "click", .45); c(15.55, "hit", .6); c(15.75, "glitch", .22); c(16.43, "swish", .25); c(16.75, "riser", .45)
for i, t in enumerate([17.32, 17.51, 17.70, 17.80, 18.03, 18.19]): c(t - .05, "step", .28, pitch=1 + .08 * i)
c(18.76, "swish", .3); c(19.39, "click", .45); c(19.57, "hit", .7); c(20.02, "whoosh", .8); c(20.15, "hit", .55)
c(21.02, "pop", .65); c(21.46, "swish", .3); c(23.18, "whoosh", .4)
for i in range(3): c(23.25 + i * .12, "pop", .4)
c(23.61, "swish", .28); c(25.10, "swish", .3); c(26.30, "whoosh", .4); c(26.42, "ding", .45); c(26.70, "swish", .4)
c(27.22, "pop", .55); c(27.24, "ding", .35); c(28.40, "whoosh", .6); c(29.33, "pop", .55); c(29.73, "swish", .45)
c(31.05, "click", .45); c(31.23, "hit", .6); c(31.99, "ding", .7); c(32.60, "whoosh", .5); c(33.30, "pop", .5)
for i in range(3): c(33.60 + i * .08, "pop", .3)
c(34.51, "pop", .4); c(34.84, "swish", .4); c(35.45, "hit", .9); c(35.47, "glitch", .3); c(35.95, "swish", .35); c(36.50, "riser", .45)
c(36.97, "scramble", .3); c(37.70, "whoosh", .5); c(38.11, "click", .45); c(38.29, "hit", .7)
c(38.62, "whoosh", .6)
for i in range(4): c(38.80 + i * .07, "pop", .35)
c(39.0, "swish", .4); c(40.32, "hit", .7); c(40.31, "click", .4); c(40.49, "ding", .6)
json.dump(C, open("plan/sfx.json", "w"), indent=0)
subprocess.run(["python", "scripts/make_sfx.py", "plan/sfx.json", "audio/sfx_raw.wav", str(TOT)], check=True)
sx, sr = sf.read("audio/sfx_raw.wav", always_2d=True); assert sr == SR
sx = sx[:N] if len(sx) >= N else np.r_[sx, np.zeros((N - len(sx), 2))]
g, sr2 = sf.read("../../../../.claude/skills/monoga-adria/assets/sfx_mixkit_1022_trim.wav", always_2d=True)
if sr2 != SR: g = signal.resample_poly(g, 160, 147, axis=0)
g = g[:int(.30 * SR)]; g[-int(.1 * SR):] *= np.linspace(1, 0, int(.1 * SR))[:, None]
if g.shape[1] == 1: g = np.repeat(g, 2, 1)
g = g / np.abs(g).max() * 0.9
for t in FLASH:
    i = int((t - 1 / 30) * SR); sx[i:i + len(g)] += g[:N - i]
sx *= 10 ** (-15 / 20)                     # SFX a -15 dB (aprendizajes, Día 2 v8)
sf.write("audio/sfx.wav", sx, SR, subtype="FLOAT")

# ---------- música por código ----------
t = np.arange(N) / SR; BPM = 112; b = 60 / BPM; rng = np.random.default_rng(3)
mus = np.zeros((N, 2))
def add(sig, t0, pan=0.0, g=1.0):
    i = int(t0 * SR); n = min(len(sig), N - i)
    if n <= 0: return
    mus[i:i + n, 0] += sig[:n] * g * (1 - pan) ; mus[i:i + n, 1] += sig[:n] * g * (1 + pan)
def env(d, a=.005, r=.2):
    x = np.arange(int(d * SR)) / SR; return np.minimum(x / a, 1) * np.exp(-x / r)
kick = lambda: np.sin(2 * np.pi * (48 + 70 * np.exp(-np.arange(int(.35 * SR)) / SR / .03)) * np.arange(int(.35 * SR)) / SR) * env(.35, .002, .12)
hat = lambda: signal.sosfilt(signal.butter(4, 7000, "high", fs=SR, output="sos"), rng.standard_normal(int(.06 * SR))) * env(.06, .001, .015)
def pluck(f, d=.32):
    x = np.arange(int(d * SR)) / SR; s = np.sign(np.sin(2 * np.pi * f * x)) * .4 + np.sin(2 * np.pi * f * x)
    return signal.sosfilt(signal.butter(2, 2600, "low", fs=SR, output="sos"), s) * env(d, .003, .09)
D2, F2, A2, C3, D3, E3, F3, A3, C4, D4, E4, F4, A4 = 73.42, 87.31, 110, 130.81, 146.83, 164.81, 174.61, 220, 261.63, 293.66, 329.63, 349.23, 440
CH = [[D3, F3, A3, C4, E4], [D3, F3, A3, C4, E4], [C3 * 0 + 116.54, D3, F3, A3, D4], [C3, E3, A3 * 0 + 196, C4, E4]]   # Dm9, Dm9, Bb, C
BASS = [D2, D2, 58.27, 65.41]
drop = lambda x: any(f - .55 <= x < f for f in FLASH)
nb = int(TOT / b) + 1
for k in range(nb):
    tb = k * b; bar = (k // 4) % 4
    if tb > TOT - 1.0: break
    if not drop(tb):
        add(kick(), tb, 0, .55 if k % 2 == 0 else .35)
        add(hat(), tb + b / 2, .3, .18); add(hat(), tb + b / 4 * 3, -.3, .08)
        sub = np.sin(2 * np.pi * BASS[bar] * np.arange(int(b * .9 * SR)) / SR) * env(b * .9, .01, .35)
        add(sub, tb, 0, .35)
    for j in range(2):   # arpegio en corcheas
        nt = CH[bar][(k * 2 + j) % 5] * 2
        add(pluck(nt), tb + j * b / 2, .35 if j else -.35, .10)
for k in range(0, nb, 16):   # pad por compás de 4
    tb = k * b; d = min(16 * b, TOT - tb)
    if d <= 0: break
    x = np.arange(int(d * SR)) / SR; s = sum(np.sin(2 * np.pi * f * x * (1 + .002 * i)) for i, f in enumerate(CH[(k // 4) % 4][:4]))
    add(s * np.minimum(x / .8, 1) * np.minimum((d - x) / .8, 1), tb, 0, .05)
mus = signal.sosfilt(signal.butter(2, [300, 1500], "bandstop", fs=SR, output="sos"), mus, axis=0) * .5 + mus * .5   # deja sitio a la voz
# ducking por voz: -0 dB en habla, +5 dB en huecos > 0,12 s
v, _ = sf.read("audio/voz.wav", always_2d=True); v = v.mean(1)[:N]; h = SR // 100; m = len(v) // h
e = 20 * np.log10(np.sqrt((v[:m * h].reshape(m, h) ** 2).mean(1)) + 1e-9); act = (e > -45).astype(float)
act = np.convolve(act, np.ones(13) / 13, "same") > 0.05
gdb = np.where(act, 0.0, 5.0); cur = 0; gs = np.zeros(m)
for i in range(m):
    a = np.exp(-.01 / (.08 if gdb[i] < cur else .35)); cur = gdb[i] + (cur - gdb[i]) * a; gs[i] = cur
mus *= (10 ** (np.interp(t, np.arange(m) * .01, gs) / 20))[:, None]
fo = int(1.2 * SR); mus[-fo:] *= np.linspace(1, 0, fo)[:, None]
sp = np.repeat(act, h)[:N]; vr = np.sqrt((v[:len(sp)][sp > 0] ** 2).mean()); mr = np.sqrt((mus[:len(sp)][sp > 0, 0] ** 2).mean())
mus *= vr * 10 ** (-7 / 20) / mr            # música 7 dB bajo la voz en el habla (RMS)
sf.write("audio/music.wav", mus, SR, subtype="FLOAT")
mr2 = np.sqrt((mus[:len(sp)][sp > 0, 0] ** 2).mean()); mg = np.sqrt((mus[:len(sp)][sp == 0, 0] ** 2).mean())
print(f"voz rms habla {20*np.log10(vr):.1f} dB | música habla {20*np.log10(mr2):.1f} | música huecos {20*np.log10(mg):.1f}")

# ---------- mezcla + ganancia lineal a -17,6 LUFS ----------
def mixit(gain):
    f = (f"[0:a]aformat=channel_layouts=stereo[v];[v][1:a][2:a]amix=inputs=3:normalize=0:duration=first,volume={gain:.3f}dB,"
         f"aresample=192000,alimiter=limit={10 ** (-2.7 / 20):.4f}:attack=1:release=60:level=disabled,aresample=48000")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio/voz.wav", "-i", "audio/music.wav", "-i", "audio/sfx.wav",
                    "-filter_complex", f, "-c:a", "pcm_s24le", "audio/final.wav"], check=True)
    s = subprocess.run(["ffmpeg", "-hide_banner", "-i", "audio/final.wav", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr.split("Summary:")[-1]
    return [float(re.search(r, s)[1]) for r in (r"I:\s+(-?[\d.]+)", r"LRA:\s+(-?[\d.]+)", r"Peak:\s+(-?[\d.]+)")]
gg = 0.0
for it in range(4):
    I, L, P = mixit(gg); print(f"mezcla it{it} g{gg:+.2f} -> I {I} LRA {L} TP {P}")
    if abs(I + 17.6) < 0.15: break
    gg += -17.6 - I
print("SFX cues", len(C) + len(FLASH))
