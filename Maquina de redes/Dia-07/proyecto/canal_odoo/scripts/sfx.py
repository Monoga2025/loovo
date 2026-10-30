"""Pista de SFX (48 kHz estéreo) en los beats de plan/beats.json (los mismos que usa la composición).
Sintetizados por código (scripts/make_sfx_lib.py) + glitch Mixkit 1022 (Mixkit SFX Free License) en el invert flash."""
import json, numpy as np, soundfile as sf
from scipy import signal
src = open("scripts/make_sfx_lib.py", encoding="utf-8").read()
G = {}; exec("import numpy as np\nSR = 48000\nrng = np.random.default_rng(7)\ndef tt" + src.split("def tt", 1)[1].split("GEN = {")[0], G)
SR = 48000; F = 1 / 30
B = json.load(open("plan/beats.json")); E = json.load(open("plan/edl.json", encoding="utf-8")); TOT = E["total"]
S = {s["id"]: s for s in E["segs"]}
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
# A gancho
c(0.0, "whoosh", 0.14); c(B["a_yo"] - 0.08, "swish", 0.2)
for k in range(12): c(B["a_yo"] + 0.12 + k * ((B["a_pero"] - B["a_yo"] - 0.35) / 11), "pop", 0.06)
c(B["a_pero"] - 0.02, "hit", 0.40); c(B["a_nada"] - 4 * F, "click", 0.16); c(B["a_nada"] + 2 * F, "scramble", 0.08)
c(B["cut1"] - F, "mixkit", 0.42)
# persona -> repos
c(B["mg1"] - 0.30, "whoosh", 0.12); c(B["mg1"] - 0.05, "hiw", 0.40); c(B["r_dos"] - 0.02, "hit", 0.26)
c(B["r_dos"] + 0.02, "swish", 0.14); c(B["r_dos"] + 0.16, "swish", 0.14); c(B["r_buenos"], "ding", 0.09)
c(B["r_buenos"] + 0.12, "click", 0.10); c(B["r_buenos"] + 0.22, "click", 0.10)
# embudo
c(B["f_in"] - 0.3, "riser", 0.08); c(B["f_in"] - 0.02, "hiw", 0.38)
for t in B["f_items"]: c(t - 0.12, "swish", 0.13); c(t + 0.2, "click", 0.08)
c(B["f_emb"] - 0.25, "whoosh", 0.12); c(B["f_emb"] + 0.33, "pop", 0.10); c(B["f_ven"] - 4 * F, "click", 0.15)
# VENTAS
c(B["v_in"] - 0.2, "swish", 0.24); c(B["v_ven"] - 0.30, "riser", 0.12); c(B["v_ven"] - 0.02, "hit", 0.46); c(B["v_ven"] + 0.1, "ding", 0.10)
# agentes
c(B["g_in"] - 0.15, "swish", 0.24); c(B["g_name"] - 0.05, "whoosh", 0.10)
for k in range(9): c(B["g_tiles"] - 0.05 + k * 0.06, "pop", 0.06)
c(B["g_cap"], "scramble", 0.08); c(B["g_b2b"] - 0.15, "whoosh", 0.14); c(B["g_b2b"] + 0.18, "hit", 0.34)
# carné
c(B["k_in"] - 0.15, "swish", 0.24)
for k in range(7): c(B["k_in"] + 0.3 + k * (B["k_card"] - 0.6 - B["k_in"]) / 7, "click", 0.06)
c(B["k_card"] - 0.15, "whoosh", 0.14); c(B["k_card"] + 0.05, "swish", 0.14); c(B["k_yo"] - F, "hit", 0.38)
c(B["o_in"] - 0.1, "whoosh", 0.12); c(B["o_orq"] - 4 * F, "click", 0.15)
for k in range(4): c(B["o_orq"] + 0.53 + k * 0.09, "pop", 0.07)
# entrenamiento
c(B["t_in"] - 0.15, "swish", 0.24); c(B["t_ent"], "riser", 0.07); c(B["t2_in"] - 0.15, "swish", 0.22)
c(B["t_orq"] - 4 * F, "click", 0.15); c(B["t_orq"] + 0.15, "pop", 0.08)
for k in range(4): c(B["t_orq"] + 0.88 + k * 0.1, "pop", 0.07)
# placa
c(B["pl"] - 0.45, "whoosh", 0.12); c(B["pl"] - 0.08, "hiw", 0.35); c(B["pl"] + 0.5, "ding", 0.09)
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
