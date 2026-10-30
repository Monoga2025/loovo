"""Transcribe trozos exactos de un wav (para confirmar qué palabra queda en un borde). Uso: tr_chunks.py wav base a-b ..."""
import sys, numpy as np, soundfile as sf, librosa
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[3] if False else "medium", device="cpu", compute_type="int8")
f = sf.SoundFile(sys.argv[1]); sr = f.samplerate; base = float(sys.argv[2])
for r in sys.argv[3:]:
    a, b = map(float, r.split("-")); f.seek(int((a-base)*sr)); x = f.read(int((b-a)*sr)).astype(np.float32)
    if x.ndim > 1: x = x.mean(1)
    x = np.concatenate([np.zeros(8000, np.float32), librosa.resample(x, orig_sr=sr, target_sr=16000), np.zeros(8000, np.float32)])
    seg, _ = m.transcribe(x, language="es", word_timestamps=True, vad_filter=False, beam_size=5, condition_on_previous_text=False)
    print(r, "|", " ".join(f"{w.word.strip()}[{a+w.start-0.5:.2f}-{a+w.end-0.5:.2f}]" for s in seg for w in s.words), flush=True)
