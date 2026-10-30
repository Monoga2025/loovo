"""Pista de SFX en la línea final (48 kHz estéreo). Tiempos = plan/beats.json (los mismos que usa la composición).
Sintetizados por código (scripts/make_sfx_lib.py, libres) + glitch Mixkit 1022 (licencia Mixkit Free) en los 2 invert flash.
Ganancias absolutas (pico ~1 = 0 dBFS); el nivel final relativo a la voz lo fija scripts/mix.py (SFX_DB)."""
import json, numpy as np, soundfile as sf
from scipy import signal
src = open("scripts/make_sfx_lib.py", encoding="utf-8").read()
G = {}; exec("import numpy as np\nSR = 48000\nrng = np.random.default_rng(7)\ndef tt" + src.split("def tt", 1)[1].split("GEN = {")[0], G)
SR = 48000; F = 1 / 30
B = json.load(open("plan/beats.json")); TOT = json.load(open("plan/edl.json", encoding="utf-8"))["total"]
rng = np.random.default_rng(11)
def hiw(d=0.42, peak=0.55):   # whoosh de agudos 2-16 kHz (Adrià 8:51)
    t = np.arange(int(d * SR)) / SR; n = rng.standard_normal(len(t))
    n = signal.sosfilt(signal.butter(4, [2000, 16000], "band", fs=SR, output="sos"), n)
    u = t / d; env = np.where(u < peak, (u / peak) ** 2, np.exp(-(u - peak) * 9))
    return n * env * 0.35, 0.5
mx, _ = sf.read("assets_src/sfx_mixkit_1022_trim.wav", always_2d=True)
mx = signal.resample_poly(mx, 160, 147, axis=0)[:int(0.30 * SR)]; mx[-int(0.1 * SR):] *= np.linspace(1, 0, int(0.1 * SR))[:, None]
C = []
def c(t, ty, g): C.append(dict(t=round(t, 3), type=ty, gain=g))
# A gancho
c(0.0, "whoosh", 0.14); c(B["a_no1"] - 0.30, "riser", 0.10); c(B["a_no1"] - 0.03, "hit", 0.40)
c(B["a_w1"] - 0.22, "swish", 0.24); c(B["a_box"] - 4 * F, "click", 0.14)
for k in range(3): c(B["a_box"] - 0.75 + k * 0.12, "pop", 0.06)
c(B["a_w2"] - 0.22, "swish", 0.24); c(B["a_stamp"] - F, "hit", 0.42); c(B["p_h3"] - 0.30, "whoosh", 0.10)
# B entreno02 (cues aprobados)
for q in json.load(open("../entreno02/plan/sfx.json")): c(B["e02"] + q["t"], q["type"], q["gain"])
# C ranking
c(B["c_in"] - 0.08, "hiw", 0.45); c(B["c_in"] + 0.3, "riser", 0.08); c(B["c_land"], "hit", 0.28)
c(B["c_sw"] - 0.2, "swish", 0.2); c(B["c_box"] - 4 * F, "click", 0.14)
# D desde pequeño
c(B["d_in"] - 0.15, "swish", 0.24); c(B["d_grid"] - 0.05, "whoosh", 0.12)
for k in range(10): c(B["d_flip0"] + (B["d_flip1"] - B["d_flip0"]) * k / 9, "click", 0.07)
c(B["cut1"] - F, "mixkit", 0.42)
# F fracasos
c(B["f_in"] - 0.45, "swish", 0.2); c(B["f_big"] - 0.24, "scramble", 0.10); c(B["f_big"] + 0.08, "hit", 0.42)
c(B["f_list"] - 0.2, "swish", 0.24)
for t in B["f_cards"]: c(t - 0.12, "swish", 0.13); c(t + 0.55, "click", 0.11)
c(B["f_all"], "whoosh", 0.12); c(B["p_in"] - 0.30, "whoosh", 0.10)
# P tensión
c(B["p_no1"] - 0.05, "hit", 0.22); c(B["p_crack"] - 0.08, "glitch", 0.14); c(B["p_crack"], "hit", 0.18)
# R1 orden
c(B["r1_in"] - 0.45, "swish", 0.2); c(B["r1_org1"], "scramble", 0.16); c(B["r1_org1"] + 0.02, "whoosh", 0.12)
c(B["r1_org2"], "swish", 0.16); c(B["r2_in"] - 0.30, "whoosh", 0.10)
# R3 habilidades -> fruto
c(B["r3_in"] - 0.45, "swish", 0.2)
for k in range(7): c(B["r3_nodes"] + k * 0.09, "pop", 0.06)
c(B["r3_lines"], "swish", 0.10); c(B["r3_fruto"] - 0.26, "riser", 0.10); c(B["r3_fruto"], "ding", 0.11); c(B["r3_fruto"] + 0.01, "hit", 0.16)
# R4 suerte
c(B["r4_in"] - 0.15, "swish", 0.24)
for k in range(10): c(B["r4_tags"] + k * 0.11, "pop", 0.06)
c(B["r4_big"] - 0.03, "hit", 0.26); c(B["r4_no"], "click", 0.16); c(B["r4_drop"] + 0.05, "whoosh", 0.18)
# R5 esfuerzo
c(B["r5_in"] - 0.15, "swish", 0.24)
for t in B["r5_rows"]: c(t - 0.1, "swish", 0.10)
c(B["r5_lay"] - 0.05, "whoosh", 0.12)
for k in range(8): c(B["r5_lay"] + 0.3 + k * (B["cut2"] - B["r5_lay"] - 0.7) / 7, "click", 0.05)
c(B["cut2"] - F, "mixkit", 0.42)
# Z días -> placa
c(B["z_in"] - 0.14, "whoosh", 0.14)
for k in range(4): c(B["z_days"] + k * 0.07, "click", 0.08)
c(B["z_five"], "ding", 0.10); c(B["pl"] - 0.08, "hiw", 0.35); c(B["pl"] + 0.5, "ding", 0.09)
N = int(round(TOT * SR)); L = np.zeros(N); R = np.zeros(N)
for q in C:
    i = int(q["t"] * SR)
    if i >= N: continue
    if q["type"] == "mixkit":
        s2 = mx[:N - i] * q["gain"]; L[i:i + len(s2)] += s2[:, 0]; R[i:i + len(s2)] += s2[:, -1]; continue
    s, pan = hiw() if q["type"] == "hiw" else G[q["type"]]()
    s = s[:N - i] * q["gain"]; p = np.linspace(-pan, pan, len(s)) if pan else np.zeros(len(s))
    L[i:i + len(s)] += s * (1 - p) / 2 * 2 ** .5; R[i:i + len(s)] += s * (1 + p) / 2 * 2 ** .5
sf.write("audio/sfx.wav", np.stack([L, R], 1).astype(np.float32), SR, subtype="FLOAT")
json.dump(C, open("plan/sfx_cues.json", "w"), indent=0)
print(len(C), "cues; pico", round(float(max(abs(L).max(), abs(R).max())), 3))
