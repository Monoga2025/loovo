# FILE: transcribe.py
# Uso: python3 transcribe.py audio.wav words.json [idioma] [modelo]
# Requiere: pip install faster-whisper
import json, sys
from faster_whisper import WhisperModel

audio, out = sys.argv[1], sys.argv[2]
lang = sys.argv[3] if len(sys.argv) > 3 else "es"
size = sys.argv[4] if len(sys.argv) > 4 else "medium"  # "small" si falta RAM
# device="cpu": en este equipo CUDA se detecta pero falta cublas64_12.dll
model = WhisperModel(size, device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, language=lang, word_timestamps=True)
words = [
    {"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)}
    for seg in segments for w in seg.words
]
json.dump(words, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(words)} palabras -> {out}")
