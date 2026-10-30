import sys, numpy as np, soundfile as sf
from faster_whisper import WhisperModel
x, sr = sf.read("tr/reg16.wav")
m = WhisperModel("medium", device="cpu", compute_type="int8")
for r in sys.argv[1:]:
    a, b = map(float, r.split("-"))
    seg = np.concatenate([np.zeros(8000), x[int(a*sr):int(b*sr)], np.zeros(8000)]).astype(np.float32)
    s, _ = m.transcribe(seg, language="es", beam_size=5, vad_filter=False, condition_on_previous_text=False)
    print(f"{r}: {' '.join(t.text.strip() for t in s)}", flush=True)
