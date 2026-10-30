# FILE: make_edl.py
# Uso: python3 make_edl.py takes.json words.json edl.json
# Convierte tomas elegidas en clips de la EDL: parte cada toma en sus pausas
# internas > MAX_GAP y ajusta cada borde a la voz real medida en audio/audio.wav
# (los timestamps de Whisper se desvían ~0,2 s), dejando PRE/POST de aire.
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import audio_env as A

takes = json.load(open(sys.argv[1], encoding="utf-8"))
words = json.load(open(sys.argv[2], encoding="utf-8"))
speech = A.load()
MAX_GAP = 0.45
PRE, POST = 0.04, 0.08  # aire antes del primer sonido y después del último

clips = []
for t in takes["takes"]:
    ws = [w for w in words if w["s"] >= t["start"] - 0.06 and w["e"] <= t["end"] + 0.06]
    runs, cur = [], [ws[0]]
    for a, b in zip(ws, ws[1:]):
        if b["s"] - a["e"] > MAX_GAP:
            runs.append(cur)
            cur = []
        cur.append(b)
    runs.append(cur)
    for i, r in enumerate(runs):
        s0 = t["start"] if i == 0 else r[0]["s"]
        e0 = t["end"] if i == len(runs) - 1 else r[-1]["e"]
        vs, ve = A.snap_start(speech, s0), A.snap_end(speech, e0)
        clips.append({"id": f"{t['id']}{'abcdefgh'[i]}" if len(runs) > 1 else t["id"],
                      "start": round(vs - PRE, 3), "end": round(ve + POST, 3),
                      # voz medida (vs-ve) y tramo de Whisper (ws-we) de las mismas
                      # palabras: build_cut los usa para alinear los subtítulos
                      "vs": round(vs, 3), "ve": round(ve, 3),
                      "ws": r[0]["s"], "we": r[-1]["e"],
                      "note": " ".join(w["w"] for w in r)})

edl = {k: takes[k] for k in ("source", "target", "tolerance", "max")}
edl["clips"] = clips
json.dump(edl, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(clips)} clips -> {sys.argv[3]}")
