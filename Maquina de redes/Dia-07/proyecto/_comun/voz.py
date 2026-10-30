"""Voz en la línea final desde el audio del CELULAR (no hay mic del PC el 13-oct). Tramos de plan/edl.json,
fundidos 12 ms, HPF 70 Hz + limpieza suave (afftdn 6 dB) -> audio/voz_raw.wav (48 kHz mono float). Ejecutar en la carpeta del proyecto."""
import json, numpy as np, soundfile as sf, subprocess
E = json.load(open("plan/edl.json", encoding="utf-8")); SR = 48000
f = sf.SoundFile("../_scan/cel48.wav"); assert f.samplerate == SR
N = int(round(E["total"] * SR)); y = np.zeros(N); fd = int(0.012 * SR)
for s in E["segs"]:
    if s.get("a") is None: continue
    f.seek(int(round(s["a"] * SR))); a = f.read(int(round((s["b"] - s["a"]) * SR))).astype(np.float64)
    a[:fd] *= np.linspace(0, 1, fd); a[-fd:] *= np.linspace(1, 0, fd)
    i = int(round(s["start"] * SR)); y[i:i + len(a)] += a[:N - i]
sf.write("audio/voz_cut.wav", y.astype(np.float32), SR, subtype="FLOAT")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio/voz_cut.wav", "-af", "highpass=f=70:poles=2,afftdn=nr=6:nf=-60:tn=1",
                "-c:a", "pcm_f32le", "audio/voz_raw.wav"], check=True)
print("ok", N / SR)
