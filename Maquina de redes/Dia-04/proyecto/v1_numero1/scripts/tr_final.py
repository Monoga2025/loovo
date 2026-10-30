"""Palabras con tiempos en la línea final (whisper medium por tramo de la EDL + afinado con la envolvente)."""
import json, numpy as np, soundfile as sf, librosa
from faster_whisper import WhisperModel
E = json.load(open("plan/edl.json", encoding="utf-8"))
x, sr = sf.read("audio/voz_raw.wav"); x16 = librosa.resample(x.astype(np.float32), orig_sr=sr, target_sr=16000)
m = WhisperModel("medium", device="cpu", compute_type="int8")
h = 160; env = 20*np.log10(np.sqrt(np.convolve(x16**2, np.ones(h)/h, "same"))+1e-9)  # 10 ms
out = []
for s in E["segs"]:
    if not s["cam"]: continue
    a, b = s["start"], s["end"]; seg = x16[int(a*16000):int(b*16000)]
    seg = np.concatenate([np.zeros(8000, np.float32), seg, np.zeros(8000, np.float32)])
    res, _ = m.transcribe(seg, language="es", word_timestamps=True, vad_filter=False, beam_size=5, condition_on_previous_text=False)
    ws = []
    for r in res:
        for w in r.words:
            st, en = a + w.start - 0.5, a + w.end - 0.5
            # afinado: primer cruce de umbral (pico-18 dB) en [st-0.12, st+0.20]
            i0, i1 = int(max(st-0.12, a)*16000), int(min(st+0.20, b)*16000)
            win = env[i0:i1]
            if len(win):
                span = env[int(max(st,a)*16000):int(min(max(en, st+0.05), b)*16000)+1]
                thr = (span.max() if len(span) else win.max()) - 18
                k = np.argmax(win > thr) if (win > thr).any() else None
                on = (i0 + k)/16000 if k is not None else st
            else: on = st
            ws.append(dict(w=w.word.strip(), st=round(st, 3), on=round(on, 3), en=round(en, 3)))
    out.append(dict(id=s["id"], words=ws))
    print(s["id"], " ".join(f"{w['w']}[{w['on']:.2f}]" for w in ws), flush=True)
json.dump(out, open("plan/words_final.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
