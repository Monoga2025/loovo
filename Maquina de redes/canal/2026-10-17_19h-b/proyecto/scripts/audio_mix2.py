"""Audio 19h-b: SFX (make_sfx.py + glitch Mixkit en los 2 invert flash), música por código (Re menor, 112 BPM, libre de derechos)
~7 dB bajo la voz con ducking por voz, mezcla y ganancia lineal a -17,6 LUFS. Adaptado de canal/2026-10-17_17h/c2/audio_mix.py.
-> audio/sfx.wav, audio/music.wav, audio/final.wav"""
import json, re, subprocess, unicodedata, numpy as np, soundfile as sf
from scipy import signal
SR = 48000; E = json.load(open("plan/edl.json")); TOT = E["total"]; N = int(TOT * SR)
FLASH = [9.50, 35.72]   # invert flash (corte); el pico es 1 cuadro antes
WO = json.load(open("plan/words_on.json", encoding="utf-8"))
nz = lambda x: re.sub(r"[^a-z0-9x]", "", unicodedata.normalize("NFD", x).encode("ascii", "ignore").decode().lower())
def at(q, after=0): return next(w["on"] for w in WO if w["on"] >= after - 0.05 and nz(w["w"]) == nz(q))
C = []
def c(t, ty, g, **k): C.append(dict(t=round(t, 3), type=ty, gain=g, **k))
F = 1 / 30
MGA, MG1, MG1E, MG2, MG3, MG3E, PL = 3.27, 13.95, 25.33, 26.62, 37.72, 46.92, 59.95
c(0.0, "hit", .8); c(at("2026") - .03, "pop", .6); c(at("2026") - .5, "riser", .3)
for T0 in (MGA, MG2, MG3): c(T0 - .5, "swish", .55); c(T0, "hit", .8)          # zoom-out radial -> aterrizaje
c(MG1 - .45, "whoosh", .8); c(MG1, "hit", .6)                                    # zoom-through
for T in (MG1E, MG3E): c(T - .28, "whoosh", .3)                                  # destellos
for q, a in [("contador", 3.4), ("que", 3.8), ("hace", 3.9), ("todo", 4.1), ("de", 4.4), ("forma", 4.5)]: c(at(q, a) - .05, "pop", .35)
c(at("manual", 4.8) - 4 * F, "click", .5); c(at("manual", 4.8) + .45, "swish", .35)
c(at("a", 5.1) - .2, "whoosh", .7)
for i in range(6): c(at("a", 5.1) + .1 + i * .06, "pop", .25)
P = at("pocos", 6)
for i in range(3): c(P + i * .1, "step", .4, pitch=1 + .15 * i)
c(at("inteligencia", 7.5), "riser", .35); c(at("herramienta", 8.5) - 4 * F, "click", .5); c(at("herramienta", 8.5), "ding", .4)
c(at("tres", 9.9), "pop", .5); c(at("destacar", 12.3), "ding", .35)
c(at("uno", 13.9), "hit", .5); c(at("agente", 15.3) - .05, "pop", .6)
c(at("estatuto", 17.6) - .1, "whoosh", .6); c(at("estatuto", 17.6), "pop", .5); c(at("conceptos", 19.2), "pop", .5)
c(at("que", 20.5) - .2, "swish", .5); c(at("exógena", 21.5), "pop", .55); c(at("retención", 22.2), "pop", .55)
c(at("tres", 22.9), "ding", .55); c(at("citando", 23.6), "pop", .5); c(at("exacto", 24.5) - 4 * F, "click", .5)
c(at("dos", 25.7), "pop", .45)
c(at("fotos", 27.6), "swish", .45); c(at("pdfs", 28.5), "swish", .45)
c(at("y", 29.4), "scramble", .35); c(at("tabla", 30.5) - .15, "whoosh", .6)
for i in range(5): c(at("tabla", 30.5) + .1 + i * .09, "step", .25, pitch=1 + .08 * i)
c(at("excel", 31.2) - 4 * F, "click", .5)
for q, a in [("nit", 31.9), ("cufe", 32.3), ("impuestos", 32.7)]: c(at(q, a) - .05, "pop", .45)
c(at("lista", 33.5), "whoosh", .4); c(at("siigo", 34.4), "ding", .35); c(at("alegra", 34.9), "ding", .35)
c(at("tres", 36.6), "pop", .45)
c(at("conciliador", 37.8), "pop", .5); c(at("bancario", 38.4), "swish", .4); c(at("automático", 39) - 4 * F, "click", .5)
c(at("cruza", 40) - .15, "whoosh", .6)
for i in range(6): c(at("segundos", 43.6) - .2 + i * .09, "step", .3, pitch=1 + .1 * i)
c(at("marca", 44.6), "hit", .6); c(at("rojo", 45), "glitch", .2); c(at("4x1000", 45.7) - 4 * F, "click", .5); c(at("4x1000", 45.7), "ding", .5)
for q, a in [("d1", 48.6), ("d2", 51.8), ("d3", 55.4)]: c(at(q, a) - .05, "pop", .6); c(at(q, a), "ding", .3)
c(PL - .1, "whoosh", .45); c(PL + .35, "ding", .45)
json.dump(C, open("plan/sfx.json", "w"), indent=0)
subprocess.run(["python", "scripts/make_sfx.py", "plan/sfx.json", "audio/sfx_raw.wav", str(TOT)], check=True)
sx, sr = sf.read("audio/sfx_raw.wav", always_2d=True); assert sr == SR
sx = sx[:N] if len(sx) >= N else np.r_[sx, np.zeros((N - len(sx), 2))]
g, sr2 = sf.read("assets/sfx_mixkit_1022_trim.wav", always_2d=True)
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
