"""Ajusta bordes al mínimo de energía cercano y transcribe cada pieza (whisper small) para confirmar.
Uso: snap.py a-b [a-b ...]   (s del crudo). Imprime borde ajustado + texto."""
import sys, numpy as np, soundfile as sf
from faster_whisper import WhisperModel
def _load():
    for n in ('small', 'base'):
        try: return WhisperModel(n, device='cpu', compute_type='int8', cpu_threads=2)
        except RuntimeError as e: print('whisper', n, 'sin memoria:', e)
    raise SystemExit('sin memoria para whisper')
f = sf.SoundFile("C:/Users/you/Desktop/Loovo-42/Dia-07/proyecto/_scan/cel48.wav"); sr = f.samplerate
def rd(t0, t1): f.seek(int(t0*sr)); return f.read(int((t1-t0)*sr))
def env(t0, t1, h=0.01):
    x = rd(t0, t1); n = int(h*sr); k = len(x)//n
    return 20*np.log10(np.sqrt((x[:k*n].reshape(k,n)**2).mean(1))+1e-9)
def snap(t, lo, hi):
    e = env(t+lo, t+hi); e = np.convolve(e, np.ones(3)/3, "same"); return round(t+lo+int(np.argmin(e))*0.01, 2)
m = _load()
for r in sys.argv[1:]:
    fix = r.endswith("!"); r = r.rstrip("!")
    a, b = map(float, r.split("-"))
    if not fix: a, b = snap(a, -0.25, 0.08), snap(b, -0.08, 0.30)
    x = rd(a, b).astype(np.float32); y = np.interp(np.arange(0, len(x), sr/16000), np.arange(len(x)), x).astype(np.float32)
    y = np.concatenate([np.zeros(8000, np.float32), y, np.zeros(8000, np.float32)])
    s, _ = m.transcribe(y, language="es", beam_size=5, vad_filter=False, condition_on_previous_text=False, word_timestamps=True)
    ws = [(w.word.strip(), a + w.start - 0.5) for q in s for w in q.words]
    print(f"{a:.2f}-{b:.2f} ({b-a:.2f}s): " + " ".join(f"{w}[{t:.2f}]" for w, t in ws), flush=True)
