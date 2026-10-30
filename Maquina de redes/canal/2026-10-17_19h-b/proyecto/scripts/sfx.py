"""Pista de SFX en la línea final (48 kHz estéreo, sin normalizar: los 'gain' son absolutos, pico ~1 = 0 dBFS).
Sintetizados por código (scripts/make_sfx_lib.py, libres) + glitch de Mixkit (licencia Mixkit Free) en el invert flash."""
import json, numpy as np, soundfile as sf
from scipy import signal
src = open("scripts/make_sfx_lib.py", encoding="utf-8").read()
HEAD = "import numpy as np\nSR = 48000\nrng = np.random.default_rng(7)\n"
src = HEAD + "def tt" + src.split("def tt", 1)[1].split("GEN = {")[0]
G = {}; exec(src, G)
SR = 48000
E = {s["id"]: s for s in json.load(open("plan/edl.json", encoding="utf-8"))["segs"]}
WD = {s["id"]: [x["on"] for x in s["words"]] for s in json.load(open("plan/words_tl.json", encoding="utf-8"))}
C = json.load(open("plan/scene25d.json")); F = 1 / 30
S = lambda i: E[i]["start"]; TOT = json.load(open("plan/edl.json", encoding="utf-8"))["total"]
rng = np.random.default_rng(11)
def hiwhoosh(d=0.42, peak=0.55):   # whoosh de agudos 2-16 kHz (Adrià 8:51), pico al 55 %
    t = np.arange(int(d * SR)) / SR; n = rng.standard_normal(len(t))
    n = signal.sosfilt(signal.butter(4, [2000, 16000], "band", fs=SR, output="sos"), n)
    u = t / d; env = np.where(u < peak, (u / peak) ** 2, np.exp(-(u - peak) * 9))
    return n * env * 0.35, 0.5
glitch_mx, sr2 = sf.read("assets_src/sfx_mixkit_1022_trim.wav", always_2d=True)
glitch_mx = signal.resample_poly(glitch_mx, 160, 147, axis=0)[:int(0.30 * SR)]          # 44,1 -> 48 kHz, 0,30 s
glitch_mx[-int(0.1 * SR):] *= np.linspace(1, 0, int(0.1 * SR))[:, None]                 # fundido 0,1 s (el original decae lento)
cues = []
T0 = S("C1")   # entreno02
for c in json.load(open("../entreno02/plan/sfx.json")): cues.append(dict(c, t=T0 + c["t"]))
cues += [dict(t=S("T1") - 0.08 - 0.2, type="whoosh", gain=0.10),           # destellos
         dict(t=S("PR1") - 0.08 - 0.2, type="whoosh", gain=0.10),
         dict(t=S("Q2") - 0.07, type="hiw", gain=0.55),                     # zoom-through A1 -> cita (pico ~5 cuadros tras el corte)
         dict(t=S("Q1") - 0.25, type="swish", gain=0.10),
         dict(t=C["start"] + 0.08, type="hiw", gain=0.55),                  # cita -> biblioteca
         dict(t=C["start"] + C["A"]["dur"] - C["xfade"] + 0.06, type="hiw", gain=0.5),   # plano A -> B
         dict(t=S("PR2") - 0.5, type="swish", gain=0.22),                   # entrada del motion graphic (corte seco en el pico)
         dict(t=WD["PR2"][12] - 4 * F, type="click", gain=0.12),
         dict(t=S("PR3") + 2 * F, type="mixkit", gain=0.42),                # invert flash: en el cuadro del pico
         dict(t=S("PL") - 0.05, type="hiw", gain=0.35), dict(t=S("PL") + 0.5, type="ding", gain=0.10)]
cues += [dict(t=max(S("PR2") + 0.12, WD["PR2"][i] - 2 * F), type="pop", gain=0.07) for i in range(6)]
N = int(round(TOT * SR)); L = np.zeros(N); R = np.zeros(N)
for c in cues:
    if c["type"] == "mixkit": sig = glitch_mx * c["gain"]; i = int(c["t"] * SR); sig = sig[:max(0, N - i)]; L[i:i+len(sig)] += sig[:, 0]; R[i:i+len(sig)] += sig[:, -1]; continue
    if c["type"] == "hiw": s, pan = hiwhoosh()
    else: s, pan = G[c["type"]]()
    s = s * c.get("gain", 1.0); i = int(c["t"] * SR); s = s[:max(0, N - i)]
    p = np.linspace(-pan, pan, len(s)) if pan else np.zeros(len(s))
    L[i:i+len(s)] += s * (1 - p) / 2 * 2 ** .5; R[i:i+len(s)] += s * (1 + p) / 2 * 2 ** .5
sf.write("audio/sfx.wav", np.stack([L, R], 1).astype(np.float32), SR, subtype="FLOAT")
json.dump(cues, open("plan/sfx_cues.json", "w"), indent=0)
print(len(cues), "cues; pico", float(max(abs(L).max(), abs(R).max())))
