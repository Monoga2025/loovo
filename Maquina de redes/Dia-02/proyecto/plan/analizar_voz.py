import json
import numpy as np, soundfile as sf, librosa

out = {}
for n in (1, 2):
    x, sr = sf.read(f"audio/audio{n}.wav")
    seg = json.load(open(f"transcript/clip{n}.segments.json", encoding="utf-8"))
    rows = []
    for s in seg:
        a, b = int(s["s"] * sr), int(s["e"] * sr)
        y = x[a:b]
        if len(y) < sr * 0.4:
            rows.append({**s, "f0": None, "rms": None, "f0std": None})
            continue
        f0, voiced, _ = librosa.pyin(y.astype(np.float32), fmin=70, fmax=400, sr=sr, frame_length=1024)
        f = f0[~np.isnan(f0)]
        rms = float(20 * np.log10(np.sqrt(np.mean(y ** 2)) + 1e-9))
        rows.append({**s, "f0": round(float(np.median(f)), 0) if len(f) > 5 else None, "f0std": round(float(np.std(f)), 1) if len(f) > 5 else None, "rms": round(rms, 1)})
    out[n] = rows
json.dump(out, open("plan/voz.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for n in (1, 2):
    print(f"=== CLIP {n} ===")
    for r in out[n]:
        tag = "" if r["f0"] is None else ("  <-- AGUDA (otra voz?)" if r["f0"] > 165 else "")
        print(f'{r["s"]:7.1f}-{r["e"]:7.1f} f0={r["f0"]} std={r["f0std"]} rms={r["rms"]} | {r["text"][:70]}{tag}')
