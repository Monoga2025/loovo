"""Mezcla final (canal): voz del CELULAR (HPF 70 Hz + afftdn suave ya en voz_raw) -> compresor 2:1 ->
+ cama musical Mixkit 464 con ducking por EDL (>= 18 dB bajo la voz al hablar, sube en huecos/motion y en la placa)
+ SFX -> ganancia lineal + limitador x4 a I -17,6 LUFS / TP <= -2 dBTP. Guarda tallos para medir el ducking."""
import json, re, subprocess, numpy as np, soundfile as sf
SR = 48000; E = json.load(open("plan/edl.json", encoding="utf-8")); TOT = E["total"]; N = int(round(TOT * SR))
MUS_OFF = 14.0          # arranque dentro de la pista (zona estable)
DUCK, UP, PLACA = -40.0, -29.0, -25.0   # LUFS objetivo de la música: bajo la voz / huecos / placa
def lufs(path):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr.split("Summary:")[-1]
    return float(re.search(r"I:\s+(-?[\d.]+)", e)[1]), float(re.search(r"LRA:\s+(-?[\d.]+)", e)[1]), float(re.search(r"Peak:\s+(-?[\d.]+)", e)[1])
# 1) voz comprimida
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio/voz_raw.wav", "-af", "acompressor=threshold=-24dB:ratio=2:attack=12:release=180:knee=6:makeup=1",
                "-ar", "48000", "-c:a", "pcm_f32le", "audio/voz_c.wav"], check=True)
v, _ = sf.read("audio/voz_c.wav"); v = v[:N] if v.ndim == 1 else v[:N, 0]; v = np.pad(v, (0, N - len(v)))
Iv = lufs("audio/voz_c.wav")[0]; v *= 10 ** ((-17.6 - Iv) / 20)
# 2) música a DUCK LUFS (medida sobre el tramo usado)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(MUS_OFF), "-t", f"{TOT + 0.5:.3f}", "-i", "assets_src/musica_mixkit_464_sci-fi-score.mp3",
                "-ac", "2", "-ar", "48000", "-c:a", "pcm_f32le", "audio/mus_raw.wav"], check=True)
m, _ = sf.read("audio/mus_raw.wav"); m = m[:N]; m = np.pad(m, ((0, N - len(m)), (0, 0)))
Im = lufs("audio/mus_raw.wav")[0]; m *= 10 ** ((DUCK - Im) / 20)
# envolvente de ducking: base UP; DUCK desde 0,15 s antes de cada tramo hasta 0,20 s después; PLACA al final
t = np.arange(N) / SR; g = np.full(N, UP - DUCK)
for s in E["segs"]:
    if s.get("a") is None: continue
    g[(t >= s["start"] - 0.15) & (t < s["end"] + 0.20)] = 0.0
pl = next(s for s in E["segs"] if s["id"] == "PL")["start"]
g[t >= pl] = PLACA - DUCK
k = int(0.12 * SR); g = np.convolve(np.pad(g, (k, k), mode="edge"), np.ones(k) / k, "same")[k:-k]   # rampas ~120 ms
fo = int(1.4 * SR); env = 10 ** (g / 20); env[:int(0.25 * SR)] *= np.linspace(0, 1, int(0.25 * SR)); env[-fo:] *= np.linspace(1, 0, fo) ** 1.5
m *= env[:, None]
# 3) sfx
x, _ = sf.read("audio/sfx.wav"); x = np.pad(x[:N], ((0, max(0, N - len(x))), (0, 0))) * 10 ** (-2 / 20)
sf.write("audio/stem_voz.wav", np.stack([v, v], 1).astype(np.float32), SR, subtype="FLOAT")
sf.write("audio/stem_mus.wav", m.astype(np.float32), SR, subtype="FLOAT")
sf.write("audio/stem_sfx.wav", x.astype(np.float32), SR, subtype="FLOAT")
mix = np.stack([v, v], 1) + m + x
sf.write("audio/premix.wav", mix.astype(np.float32), SR, subtype="FLOAT")
g2 = 0.0
for it in range(5):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio/premix.wav", "-af",
                    f"volume={g2:.3f}dB,aresample=192000,alimiter=limit={10 ** (-2.7 / 20):.4f}:attack=1:release=60:level=disabled,aresample=48000",
                    "-c:a", "pcm_s24le", "audio/final.wav"], check=True)
    I, LRA, TP = lufs("audio/final.wav"); print(f"it{it} g {g2:+.2f} -> I {I} LRA {LRA} TP {TP}")
    if abs(I + 17.6) < 0.1: break
    g2 += -17.6 - I
json.dump(dict(final_gain_db=g2, voz_gain_db=-17.6 - Iv, mus_gain_db=DUCK - Im), open("audio/mix_params.json", "w"))
