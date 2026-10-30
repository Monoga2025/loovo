"""faster-whisper medium sobre el mic del PC alineado (audio/B_pc15.wav: t=0 <-> t_cel=15). Rangos en tiempo del celular.
-> tr/B_pc_medium.json (palabras en tiempo del celular)"""
import json, numpy as np, soundfile as sf, librosa
from faster_whisper import WhisperModel
x, sr = sf.read("audio/B_pc15.wav"); x16 = librosa.resample(x.astype(np.float32), orig_sr=sr, target_sr=16000); B = 15.0
R = [(17.5, 36.0), (36.5, 62.5), (62.5, 84.0), (84.0, 106.0), (106.5, 121.0), (130.0, 147.5), (147.5, 175.0)]
m = WhisperModel("medium", device="cpu", compute_type="int8"); out = []
for a, b in R:
    seg = x16[int((a - B) * 16000):int((b - B) * 16000)]
    res, _ = m.transcribe(seg, language="es", word_timestamps=True, vad_filter=False, beam_size=5, condition_on_previous_text=False)
    ws = [dict(w=w.word.strip(), s=round(a + w.start, 3), e=round(a + w.end, 3), p=round(w.probability, 2)) for r in res for w in r.words]
    out.append(dict(range=[a, b], words=ws))
    print(f"== {a}-{b}\n" + " ".join(f"{w['w']}[{w['s']:.2f}-{w['e']:.2f}]" for w in ws), flush=True)
json.dump(out, open("tr/B_pc_medium.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
