"""Voz: piezas del WAV reparado (declip.py) con fundidos 20 ms, tono de sala en los huecos, cadena suave
(paso alto, reducción de ruido leve, de-esser, EQ, compresión 2:1) y ganancia lineal a -17,6 LUFS. -> audio/voz.wav"""
import json, re, subprocess, numpy as np, soundfile as sf
E = json.load(open("plan/edl.json", encoding="utf-8")); SR = 48000
x, sr = sf.read("audio/declip48.wav"); assert sr == SR
x = x * 0.4                                   # margen: el spline deja picos > 1
room = x[int(203.0 * SR):int(205.8 * SR)].copy()
N = int(E["total"] * SR); out = np.zeros(N)
reps = int(np.ceil(N / len(room))) + 1; bed = np.tile(room, reps)[:N]
mask = np.ones(N)                             # 1 = poner tono de sala
F = int(0.02 * SR)
for p in E["pieces"]:
    s = x[int(p["a"] * SR):int(p["b"] * SR)].copy()
    s[:F] *= np.linspace(0, 1, F); s[-F:] *= np.linspace(1, 0, F)
    i = int(p["o"] * SR); n = min(len(s), N - i); out[i:i + n] += s[:n]; mask[i + F:i + n - F] = 0
mask = np.convolve(mask, np.ones(2 * F) / (2 * F), "same")
out += bed * mask
sf.write("audio/voz_raw.wav", out.astype(np.float32), SR, subtype="FLOAT")
CH = ("highpass=f=80,afftdn=nr=10:nf=-58:tn=1,deesser=i=0.35:m=0.5:f=0.5,"
      "equalizer=f=240:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1.2:g=1.5,equalizer=f=8500:t=q:w=1:g=-1,"
      "acompressor=threshold=-24dB:ratio=2:attack=8:release=200:makeup=1:knee=6")
def run(g):
    f = f"{CH},volume={g:.3f}dB,aresample=192000,alimiter=limit={10 ** (-3.0 / 20):.4f}:attack=1:release=60:level=disabled,aresample=48000"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio/voz_raw.wav", "-af", f, "-c:a", "pcm_s24le", "audio/voz.wav"], check=True)
    s = subprocess.run(["ffmpeg", "-hide_banner", "-i", "audio/voz.wav", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr.split("Summary:")[-1]
    return [float(re.search(r, s)[1]) for r in (r"I:\s+(-?[\d.]+)", r"LRA:\s+(-?[\d.]+)", r"Peak:\s+(-?[\d.]+)")]
g = 0.0
for it in range(5):
    I, L, P = run(g); print(f"voz it{it} g{g:+.2f} -> I {I} LRA {L} TP {P}")
    if abs(I + 17.6) < 0.15: break
    g += -17.6 - I
