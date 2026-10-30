# FILE: zoom_cuts.py
# Uso: python3 zoom_cuts.py edl.json words_out.json zoom.json entrada.mp4 salida.mp4
# Interrupción de patrón para cámara fija: alterna plano normal / zoom-in en
# cada corte, y parte en dos los clips de más de MAX_SEG s en la palabra más
# cercana a su mitad. El plan queda en zoom.json (revisable) y se renderiza
# con trim + crop + concat (exacto a frame, audio copiado).
import json, subprocess, sys

edl = json.load(open(sys.argv[1], encoding="utf-8"))
words = json.load(open(sys.argv[2], encoding="utf-8"))
plan_path, src, out = sys.argv[3], sys.argv[4], sys.argv[5]
Z = 1.12                 # zoom sutil
CX, CY = 540, 800        # centro del zoom: cara (medido en qa/contact.png)
MAX_SEG = 5.0
W, H = 1080, 1920

segs, t = [], 0.0
for c in edl["clips"]:
    d = c["end"] - c["start"]
    cuts = [t, t + d]
    if d > MAX_SEG:
        mid = t + d / 2
        inside = [w["s"] for w in words if t + 1.5 < w["s"] < t + d - 1.5]
        if inside:
            cuts.insert(1, min(inside, key=lambda x: abs(x - mid)))
    for a, b in zip(cuts, cuts[1:]):
        segs.append({"clip": c["id"], "start": round(a, 3), "end": round(b, 3)})
    t += d
for i, s in enumerate(segs):
    s["zoom"] = Z if i % 2 else 1.0
json.dump(segs, open(plan_path, "w", encoding="utf-8"), indent=1)

parts, labels = [], ""
for i, s in enumerate(segs):
    z = s["zoom"]
    cw, ch = round(W / z / 2) * 2, round(H / z / 2) * 2
    x0, y0 = round(CX * (1 - 1 / z)), round(CY * (1 - 1 / z))
    parts.append(f"[0:v]trim=start={s['start']}:end={s['end']},setpts=PTS-STARTPTS,"
                 f"crop={cw}:{ch}:{x0}:{y0},scale={W}:{H}:flags=lanczos,setsar=1[v{i}]")
    labels += f"[v{i}]"
parts.append(f"{labels}concat=n={len(segs)}:v=1:a=0,fps=30[v]")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", src,
                "-filter_complex", ";".join(parts), "-map", "[v]", "-map", "0:a",
                "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-c:a", "copy", out],
               check=True)
longest = max(s["end"] - s["start"] for s in segs)
print(f"{len(segs)} segmentos (máx {longest:.2f}s) -> {out}")
