# FILE: validate_edl.py
# Uso: python3 validate_edl.py edl.json words.json   (exit 1 si hay errores)
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import audio_env as A

edl = json.load(open(sys.argv[1], encoding="utf-8"))
speech = A.load() if os.path.exists("audio/audio.wav") else None
words = json.load(open(sys.argv[2], encoding="utf-8"))
starts = [w["s"] for w in words]
ends = [w["e"] for w in words]
FILLER = {"y", "pero", "entonces", "bueno", "eh", "este", "o", "and", "so", "well", "but"}


def duration(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path])
    return float(out.decode().strip())


def near(x, arr, tol):
    return bool(arr) and min(abs(x - a) for a in arr) <= tol


def in_gap(x):
    return any(ends[i] <= x <= starts[i + 1] and starts[i + 1] - ends[i] >= 0.12
               for i in range(len(words) - 1))


src_d = duration(edl["source"])
errors, warns, total = [], [], 0.0
for c in edl["clips"]:
    s, e, cid = c["start"], c["end"], c["id"]
    if not (0 <= s < e <= src_d + 0.01):
        errors.append(f"{cid}: rango inválido ({s}-{e}, fuente dura {src_d:.2f})")
        continue
    total += e - s
    # La voz medida manda: un corte sobre voz es error. Los timestamps de
    # Whisper se desvían ~0,2 s, así que no coincidir con ellos solo es aviso.
    if speech is not None:
        if not A.is_silent(speech, s):
            errors.append(f"{cid}: el inicio {s:.2f}s cae sobre voz (audio)")
        if not A.is_silent(speech, e):
            errors.append(f"{cid}: el final {e:.2f}s cae sobre voz (audio)")
        lead = A.snap_start(speech, s, back=0) - s
        tail = e - A.snap_end(speech, e, fwd=0)
        if lead > 0.12 or tail > 0.20:
            warns.append(f"{cid}: aire de sobra (inicio {lead:.2f}s, final {tail:.2f}s)")
    else:
        if not (near(s, starts, 0.06) or in_gap(s)):
            errors.append(f"{cid}: el inicio {s:.2f}s cae dentro de una palabra")
        if not (near(e, ends, 0.06) or in_gap(e)):
            errors.append(f"{cid}: el final {e:.2f}s cae dentro de una palabra")
    first = next((w for w in words if abs(w["s"] - s) <= 0.15 or w["s"] >= s), None)
    if first and first["w"].lower().strip(".,;:¿?¡!") in FILLER:
        warns.append(f"{cid}: empieza con '{first['w']}' (revisar)")
    last = [w for w in words if w["e"] <= e + 0.08 and w["e"] >= e - 0.4]
    if last and not last[-1]["w"].endswith((".", "?", "!", "…")):
        warns.append(f"{cid}: no termina en puntuación final (revisar idea completa)")

target, tol = edl.get("target"), edl.get("tolerance", 3)
if target is not None and abs(total - target) > tol:
    errors.append(f"duración total {total:.2f}s fuera de {target}±{tol}s")
if total > edl.get("max", 60):
    errors.append(f"duración total {total:.2f}s supera el máximo {edl.get('max', 60)}s")

print(f"TOTAL_REAL={total:.2f}s  CLIPS={len(edl['clips'])}")
for w in warns:
    print("AVISO:", w)
for e in errors:
    print("ERROR:", e)
print("RESULTADO:", "FALLA" if errors else "OK")
sys.exit(1 if errors else 0)
