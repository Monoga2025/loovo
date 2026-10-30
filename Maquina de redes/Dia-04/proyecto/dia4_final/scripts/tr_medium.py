"""Re-transcribe tramos con faster-whisper medium (CPU int8). Tiempos en reloj del crudo."""
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
rngs = [tuple(map(float, r.split("-"))) for r in sys.argv[3:]]
m = WhisperModel("medium", device="cpu", compute_type="int8")
res = []
for a, b in rngs:
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(a),"-t",str(b-a),"-i",src,"-vn","-ac","1","-ar","16000","-f","f32le","-"],capture_output=True,check=True).stdout
    x = np.frombuffer(raw, np.float32)
    seg, _ = m.transcribe(x, language="es", word_timestamps=True, vad_filter=False, beam_size=5)
    ws = [(w.word.strip(), round(a+w.start,3), round(a+w.end,3), round(w.probability,2)) for s in seg for w in s.words]
    res.append({"range":[a,b],"words":ws})
    print(f"== {a}-{b}"); print(" ".join(f"{w[0]}[{w[1]:.2f}]" for w in ws), flush=True)
json.dump(res, open(out,"w",encoding="utf-8"), ensure_ascii=False, indent=0)
