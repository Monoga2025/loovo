# FILE: build_cut.py
# Uso: python3 build_cut.py edl.json salida.mp4 [words.json]
# Aplica fades de 30 ms en cada corte y remapea los timestamps de las palabras.
import json, subprocess, sys, os

edl = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]
words_path = sys.argv[3] if len(sys.argv) > 3 else None
FADE = 0.03


def stream_start(path, sel):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", sel,
                                   "-show_entries", "stream=start_time", "-of", "csv=p=0", path])
    return float(out.decode().strip() or 0)


# Los tiempos de la EDL están en la línea del WAV extraído, que empieza en 0.
# En el MP4 del celular el audio arranca más tarde (start_time > 0): se suma
# ese desfase a ambos trims para cortar justo donde se diseñó sin romper la
# sincronía labios/voz del original.
OFFSET = stream_start(edl["source"], "a:0") - stream_start(edl["source"], "v:0")
print(f"desfase audio/video de la fuente: {OFFSET:+.4f}s")
# Bordes ajustados a fotogramas reales (fuente VFR): así cada tramo de audio
# mide lo mismo que su tramo de video y la sincronía no deriva entre clips.
pts = sorted(float(x) for x in subprocess.check_output(
    ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "packet=pts_time",
     "-of", "csv=p=0", edl["source"]]).decode().split())
snap = lambda t: min(pts, key=lambda p: abs(p - t))
parts, labels = [], ""
for i, c in enumerate(edl["clips"]):
    s, e = snap(c["start"] + OFFSET), snap(c["end"] + OFFSET)
    d = e - s
    parts.append(f"[0:v]trim=start={s}:end={e},setpts=PTS-STARTPTS[v{i}]")
    parts.append(
        f"[0:a]atrim=start={s}:end={e},asetpts=PTS-STARTPTS,"
        f"afade=t=in:d={FADE},afade=t=out:st={max(d - FADE, 0):.3f}:d={FADE}[a{i}]")
    labels += f"[v{i}][a{i}]"
parts.append(f"{labels}concat=n={len(edl['clips'])}:v=1:a=1[v][a]")
cmd = ["ffmpeg", "-y", "-i", edl["source"], "-filter_complex", ";".join(parts),
       "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18",
       "-preset", "slow", "-c:a", "aac", "-b:a", "192k", out]
subprocess.run(cmd, check=True)

if words_path:
    words = json.load(open(words_path, encoding="utf-8"))
    remapped, offset = [], 0.0
    for c in edl["clips"]:
        # mismos bordes que el corte real (ajustados a fotograma), en tiempo del WAV
        s, e = snap(c["start"] + OFFSET) - OFFSET, snap(c["end"] + OFFSET) - OFFSET
        if "ws" in c:
            # Whisper se desvía de la voz real: se estira linealmente el tramo
            # de Whisper (ws-we) sobre la voz medida (vs-ve) del clip
            ws, we, vs, ve = c["ws"], c["we"], c["vs"], c["ve"]
            k = (ve - vs) / max(we - ws, 0.01)
            for w in words:
                if w["s"] >= ws - 0.001 and w["e"] <= we + 0.001:
                    remapped.append({"w": w["w"],
                                     "s": round(vs + (w["s"] - ws) * k - s + offset, 3),
                                     "e": round(vs + (w["e"] - ws) * k - s + offset, 3)})
        else:
            for w in words:
                if w["s"] >= s - 0.001 and w["e"] <= e + 0.001:
                    remapped.append({"w": w["w"], "s": round(w["s"] - s + offset, 3),
                                     "e": round(w["e"] - s + offset, 3)})
        offset += e - s
    dest = os.path.join(os.path.dirname(out) or ".", "words_out.json")
    json.dump(remapped, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(remapped)} palabras remapeadas -> {dest}")
dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                               "-of", "csv=p=0", out]).decode().strip()
print(f"DURACION_REAL={float(dur):.2f}s")
