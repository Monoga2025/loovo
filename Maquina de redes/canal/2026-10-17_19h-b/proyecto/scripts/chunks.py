import sys, numpy as np, soundfile as sf
from faster_whisper import WhisperModel
from scipy.signal import resample_poly
x, sr = sf.read("audio/declip48.wav"); m = WhisperModel("medium", device="cpu", compute_type="int8")
a = sys.argv[1:]
for i in range(0, len(a), 2):
    t0, t1 = float(a[i]), float(a[i + 1]); seg = resample_poly(x[int(t0 * sr):int(t1 * sr)], 1, 3).astype(np.float32)
    segs, _ = m.transcribe(seg, language="es", word_timestamps=True, initial_prompt="Contador, DIAN, exógena, NIT, CUFE, Siigo, Alegra, 4x1000.")
    print(f"{t0}-{t1}:", " ".join(f"{w.word.strip()}[{t0 + w.start:.2f}]" for s in segs for w in s.words), flush=True)
