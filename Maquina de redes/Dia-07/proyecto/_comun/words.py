"""Palabras con tiempo en la línea final: whisper medium por tramo sobre audio/voz_raw.wav (guiado con el texto del EDL),
inicio afinado a la subida de la envolvente (10 ms); primera palabra = primer sonido del tramo. -> plan/words_tl.json"""
import json, numpy as np, soundfile as sf
from faster_whisper import WhisperModel
def _load():
    for n in ('small', 'base'):
        try: return WhisperModel(n, device='cpu', compute_type='int8', cpu_threads=2)
        except RuntimeError as e: print('whisper', n, 'sin memoria:', e)
    raise SystemExit('sin memoria para whisper')
E = json.load(open("plan/edl.json", encoding="utf-8"))
x, sr = sf.read("audio/voz_raw.wav"); h = int(0.01 * sr)
n = len(x) // h; env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
m = _load(); out = []
for s in E["segs"]:
    if s.get("a") is None: continue
    a, b = s["start"], s["end"]
    seg = x[int(a * sr):int(b * sr)]
    y = np.interp(np.arange(0, len(seg), sr / 16000), np.arange(len(seg)), seg).astype(np.float32)
    y = np.concatenate([np.zeros(4000, np.float32), y, np.zeros(8000, np.float32)])
    r, _ = m.transcribe(y, language="es", word_timestamps=True, beam_size=5, condition_on_previous_text=False)
    ws = [(w.word.strip(), a + w.start - 0.25) for q in r for w in q.words]
    ia, ib = int(a * 100), int(b * 100); first = ia + int(np.argmax(env[ia:ib] > -45)); prev = first; res = []
    for k, (w, st) in enumerate(ws):
        i0 = max(int((st - 0.12) * 100), prev); i1 = min(int((st + 0.15) * 100), ib - 1)
        on = (i0 + int(np.argmax(der[i0:i1 + 1]))) / 100 if i1 > i0 else i0 / 100
        if k == 0: on = first / 100
        res.append(dict(w=w, on=round(on, 2))); prev = int(on * 100) + 5
    out.append(dict(id=s["id"], start=a, end=b, words=res))
    print(s["id"], " ".join(f"{w['w']}[{w['on']:.2f}]" for w in res), flush=True)
json.dump(out, open("plan/words_tl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
