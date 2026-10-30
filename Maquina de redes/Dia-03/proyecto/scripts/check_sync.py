# FILE: check_sync.py
# Uso: python check_sync.py plan/edl.json build/cut.mp4 audio/audio.wav
# Verifica, clip por clip, que el corte respeta lo diseñado y que labios y voz
# siguen sincronizados:
#   1) audio: correlación del audio del corte contra el WAV de la transcripción
#      (desfase esperado ~0; un valor constante como -0,18 s delata el
#      start_time del audio del MP4 de celular no compensado)
#   2) labios/voz: el fotograma del corte se busca en la fuente; su tiempo,
#      comparado con el del audio, da el desfase video-audio (tolerancia ±45 ms)
# Exit 1 si algún clip supera la tolerancia.
import json, subprocess, sys, wave
import numpy as np

edl = json.load(open(sys.argv[1], encoding="utf-8"))
cut, wav = sys.argv[2], sys.argv[3]
SR, TOL = 16000, 0.045
W, H = 54, 96


def probe_start(path, sel):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", sel,
                                   "-show_entries", "stream=start_time", "-of", "csv=p=0", path])
    return float(out.decode().strip() or 0)


def load_wav(path):
    w = wave.open(path)
    return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)


def frames(path, t0, dur):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(t0, 0):.3f}", "-i", path, "-t", f"{dur:.3f}",
                          "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)


src = edl["source"]
off = probe_start(src, "a:0") - probe_start(src, "v:0")
fps = eval(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                    "stream=r_frame_rate", "-of", "csv=p=0", src]).decode().strip())
pts = sorted(float(x) for x in subprocess.check_output(
    ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "packet=pts_time",
     "-of", "csv=p=0", src]).decode().split())
snap = lambda x: min(pts, key=lambda p: abs(p - x))  # mismos bordes que build_cut.py
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cut, "-vn", "-ac", "1", "-ar", str(SR), "_cut_audio.wav"], check=True)
ref, cutw = load_wav(wav), load_wav("_cut_audio.wav")
print(f"desfase audio/video en la fuente: {off:+.4f}s (debe compensarse en build_cut)")
print("clip   audio vs diseño   labios vs voz")
bad, t = 0, 0.0
for c in edl["clips"]:
    s_real = snap(c["start"] + off) - off
    d = snap(c["end"] + off) - snap(c["start"] + off)
    seg = cutw[int((t + 0.3) * SR):int((t + min(d, 2.0) - 0.1) * SR)]
    a = int((c["start"] - 0.6) * SR)
    win = ref[a:a + len(seg) + int(1.5 * SR)]
    k = int(np.argmax(np.correlate(win, seg, mode="valid")))
    fa = a / SR + k / SR - 0.3                       # inicio real del clip (tiempo WAV)
    tm = min(1.0, d / 2)                             # fotograma interior del clip
    refimg = frames(cut, t + tm, 0.04)[0]
    s0 = fa + off + tm - 0.4
    cand = frames(src, s0, 0.8)
    kk = int(np.argmin([np.mean((f - refimg) ** 2) for f in cand]))
    va = (s0 + kk / fps - off) - (fa + tm)
    flag = abs(va) > TOL or abs(fa - s_real) > TOL
    bad += flag
    print(f"{c['id']:5}  {fa - s_real:+.3f}s          {va:+.3f}s {'<-- REVISAR' if flag else ''}")
    t += d
print("RESULTADO:", "FALLA" if bad else "OK")
sys.exit(1 if bad else 0)
