# FILE: transcribe.py
# Uso: python transcribe.py audio.wav words.json [idioma] [modelo|auto]
# Requiere: pip install faster-whisper
# - device="cpu": en Windows CUDA puede detectarse sin cublas64_12.dll y fallar.
# - "auto" prueba medium y cae a small si no hay RAM (mkl_malloc falló con 1,7 GB libres).
# - El tamaño del modelo NO mejora los timestamps (medido: error mediano ~0,2 s
#   en small y medium); medium sí acierta mejor nombres propios. Los cortes se
#   ajustan después a la voz medida (audio_env.py), no a estos tiempos.
import json, sys
from faster_whisper import WhisperModel

audio, out = sys.argv[1], sys.argv[2]
lang = sys.argv[3] if len(sys.argv) > 3 else "es"
size = sys.argv[4] if len(sys.argv) > 4 else "auto"


def run(name):
    model = WhisperModel(name, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio, language=lang, word_timestamps=True)
    return [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)}
            for seg in segments for w in seg.words]


if size == "auto":
    try:
        words, used = run("medium"), "medium"
    except (RuntimeError, MemoryError) as e:
        print(f"medium no cabe ({e}); uso small")
        words, used = run("small"), "small"
else:
    words, used = run(size), size
json.dump(words, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(words)} palabras ({used}) -> {out}")
