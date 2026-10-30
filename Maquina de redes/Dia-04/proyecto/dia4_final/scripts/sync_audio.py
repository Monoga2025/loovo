"""sync_audio.py - alinea el audio del computador (OBS) con un clip del celular.
Uso (python -I sync_audio.py ...):
  sync_audio.py CELULAR.mp4 COMPUTADOR.mp4 INICIO FIN [--out DIR] [--name cand] [--expected 2162]
                [--drift-times 30,660] [--search 60] [--ref 60] [--stereo]
Convencion: t_comp = t_cel + offset. Imprime offset (s), deriva (ppm) y escribe
  DIR/mic_<name>.wav (computador alineado), DIR/cel_<name>.wav (celular), DIR/sync_<name>.json
Los WAV son 48 kHz 24 bit. Solo lee los videos. Requiere ffmpeg, numpy, scipy.
"""
import argparse, json, subprocess, os, sys
import numpy as np
from scipy import signal

def pcm(path, t0, dur, sr, ch=1):
    """Lee audio como float32 (n,ch). t0 puede ser <0 (se rellena de ceros)."""
    pad = 0.0
    if t0 < 0:
        pad = -t0; dur -= pad; t0 = 0
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{t0:.6f}", "-t", f"{dur:.6f}", "-i", path,
           "-vn", "-ac", str(ch), "-ar", str(sr), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).reshape(-1, ch)
    if pad: x = np.concatenate([np.zeros((int(round(pad*sr)), ch), np.float32), x])
    return x

def bp(x, sr, lo=200, hi=6000):
    sos = signal.butter(4, [lo, hi], btype="band", fs=sr, output="sos")
    return signal.sosfiltfilt(sos, x)

def xcorr_lag(ref, win, sr, phat=True):
    """lag (s) tal que win[n+lag] ~ ref[n]. Devuelve lag, pico/mediana."""
    n = len(ref) + len(win)
    nfft = 1 << (n - 1).bit_length()
    R = np.fft.rfft(ref, nfft); W = np.fft.rfft(win, nfft)
    C = W * np.conj(R)
    if phat: C = C / (np.abs(C) + 1e-9 * np.abs(C).max())
    c = np.fft.irfft(C, nfft)
    c = np.concatenate([c[-(len(ref)-1):], c[:len(win)]])  # lags -(len(ref)-1)..len(win)-1
    lags = np.arange(-(len(ref)-1), len(win))
    i = int(np.argmax(c))
    return lags[i] / sr, c[i] / (np.median(np.abs(c)) + 1e-12), i, c, lags

def offset_at(cel, comp, t_cel, expected, ref_len=60, search=60, sr=16000):
    """Offset (s) en el instante t_cel del celular (ventana ref centrada)."""
    r0 = max(0.0, t_cel - ref_len/2)
    ref = bp(pcm(cel, r0, ref_len, sr)[:, 0], sr)
    w0 = r0 + expected - search
    win = bp(pcm(comp, w0, ref_len + 2*search, sr)[:, 0], sr)
    lag, q, *_ = xcorr_lag(ref, win, sr)
    return w0 + lag - r0, q  # t_comp = t_cel + off

def refine48(cel, comp, t0, dur, off0, sr=48000, maxms=15.0):
    """Afina a nivel de muestra a 48 kHz (xcorr sobre senal filtrada, interpolacion parabolica)."""
    ref = bp(pcm(cel, t0, dur, sr)[:, 0], sr)
    m = maxms/1000
    win = bp(pcm(comp, t0 + off0 - m, dur + 2*m, sr)[:, 0], sr)
    lag, q, i, c, lags = xcorr_lag(ref, win, sr, phat=True)  # PHAT: evita saltos de un periodo de f0 (~8,7 ms)
    # restringir a +-m
    sel = np.abs(lags/sr - (-m + m)) <= 2*m
    # win empieza en off0-m, asi lag=m  => desfase 0
    cc = np.where(np.abs(lags/sr - m) <= m, c, -np.inf)
    j = int(np.argmax(cc))
    d = 0.0
    if 0 < j < len(cc)-1:
        a, b, g = cc[j-1], cc[j], cc[j+1]
        den = a - 2*b + g
        d = 0.5*(a - g)/den if den != 0 else 0.0
    return off0 + ((lags[j] + d)/sr - m)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cel"); ap.add_argument("comp")
    ap.add_argument("inicio", type=float); ap.add_argument("fin", type=float)
    ap.add_argument("--out", default="."); ap.add_argument("--name", default="clip")
    ap.add_argument("--expected", type=float, default=0.0, help="offset esperado (s) por hora de inicio")
    ap.add_argument("--drift-times", default="45,660", help="instantes del celular (s) para medir deriva")
    ap.add_argument("--search", type=float, default=60); ap.add_argument("--ref", type=float, default=60)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    mid = (a.inicio + a.fin)/2
    off, q = offset_at(a.cel, a.comp, mid, a.expected, a.ref, a.search)
    off = refine48(a.cel, a.comp, max(0, a.inicio - 3), (a.fin - a.inicio) + 6, off)
    # deriva
    pts = []
    for t in [float(x) for x in a.drift_times.split(",") if x]:
        o, qq = offset_at(a.cel, a.comp, t, off, 30, 3)  # ventana corta y busqueda estrecha: evita falsos picos
        o = refine48(a.cel, a.comp, max(0, t - 15), 30, o)
        pts.append((t, o, qq))
    pts.append((mid, off, q))
    pts.sort()
    drift_ppm = None; factor = None
    if len(pts) >= 2:
        t = np.array([p[0] for p in pts]); o = np.array([p[1] for p in pts])
        slope = np.polyfit(t, o, 1)[0]
        drift_ppm = slope*1e6
        factor = 1 + slope   # t_comp = t_cel*factor + b -> atempo del comp = 1/factor
    # extraer WAV 24 bit alineados (2 canales conservados)
    dur = a.fin - a.inicio
    def wav(src, t0, path):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t0:.6f}", "-t", f"{dur:.6f}", "-i", src,
                        "-vn", "-ar", "48000", "-c:a", "pcm_s24le", path], check=True)
    wav(a.comp, a.inicio + off, os.path.join(a.out, f"mic_{a.name}.wav"))
    wav(a.cel, a.inicio, os.path.join(a.out, f"cel_{a.name}.wav"))
    res = dict(offset_s=off, offset_samples_48k=off*48000, peak_quality=q,
               drift_points=[dict(t_cel=p[0], offset=p[1], q=p[2]) for p in pts],
               drift_ppm=drift_ppm, correction_factor=factor)
    json.dump(res, open(os.path.join(a.out, f"sync_{a.name}.json"), "w"), indent=1)
    print(json.dumps(res, indent=1))

if __name__ == "__main__":
    main()
