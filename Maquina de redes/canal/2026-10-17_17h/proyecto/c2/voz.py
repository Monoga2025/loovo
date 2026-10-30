"""Voz del corte 2: arma las piezas (fundidos 20 ms), cadena aprendida (aprendizajes.md: filtro de graves,
reducción de ruido leve, compuerta, EQ de presencia, compresión suave), ganancia lineal a -17,6 LUFS
y afina el inicio de cada palabra con la envolvente (como onsets.py). -> audio/voz.wav, plan/words_on.json"""
import json, re, subprocess, numpy as np, soundfile as sf
E = json.load(open("plan/edl.json")); SR = 48000
x, sr = sf.read("audio/cam48.wav"); assert sr == SR
out = np.zeros(int(E["total"] * SR)); F = int(0.02 * SR)
for p in E["pieces"]:
    s = x[int(p["a"] * SR):int(p["b"] * SR)].copy()
    s[:F] *= np.linspace(0, 1, F); s[-F:] *= np.linspace(1, 0, F)
    i = int(p["o"] * SR); out[i:i + len(s)] += s
sf.write("audio/voz_raw.wav", out, SR, subtype="FLOAT")
CH = ("highpass=f=85,afftdn=nr=8:nf=-50,agate=threshold=0.004:ratio=1.8:attack=5:release=180:range=0.25,"
      "equalizer=f=220:t=q:w=1:g=-1.5,equalizer=f=3200:t=q:w=1.2:g=1.5,"
      "acompressor=threshold=-26dB:ratio=2:attack=10:release=220:makeup=2:knee=6")
def run(g):
    f = f"{CH},volume={g:.3f}dB,aresample=192000,alimiter=limit={10 ** (-2.7 / 20):.4f}:attack=1:release=60:level=disabled,aresample=48000"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio/voz_raw.wav", "-af", f, "-c:a", "pcm_s24le", "audio/voz.wav"], check=True)
    s = subprocess.run(["ffmpeg", "-hide_banner", "-i", "audio/voz.wav", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr.split("Summary:")[-1]
    return [float(re.search(r, s)[1]) for r in (r"I:\s+(-?[\d.]+)", r"LRA:\s+(-?[\d.]+)", r"Peak:\s+(-?[\d.]+)")]
g = 0.0
for it in range(4):
    I, L, P = run(g); print(f"voz it{it} g{g:+.2f} -> I {I} LRA {L} TP {P}")
    if abs(I + 17.6) < 0.15: break
    g += -17.6 - I
# afinar onsets en la línea de salida
h = SR // 100; n = len(out) // h
env = 20 * np.log10(np.sqrt((out[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
W = json.load(open("plan/words.json", encoding="utf-8")); prev = 0
for w in W:
    i0 = max(int((w["s"] - 0.12) * 100), prev); i1 = int((w["s"] + 0.15) * 100)
    on = (i0 + int(np.argmax(der[i0:i1 + 1]))) / 100 if i1 > i0 else i0 / 100
    w["on"] = round(on, 2); prev = int(on * 100) + 5
json.dump(W, open("plan/words_on.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("dif media onset-whisper", round(float(np.mean([w["on"] - w["s"] for w in W])), 3))
