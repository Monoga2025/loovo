"""Audio solo del micrófono del PC (0% celular).
Construye voz_pc_only.wav con HPF 70 Hz y loudnorm I=-17.6 LUFS.
Mezcla con sfx.wav y sustituye en video sin recodificar.
Uso: python -I audio_solo_pc.py [--corr] [--out SALIDA.mp4]
  --corr: Verifica correlación cruzada contra cada archivo de PC
  --out:  Video de salida (default: ../../entregables/Dia4_final_tiktok_audioPC.mp4)
"""
import argparse, json, subprocess, os, sys, re
import numpy as np
from scipy import signal

E = json.load(open("plan/edl.json", encoding="utf-8"))
SR = 48000
PC_MAIN = "../../CAMARA 10-45-16.mp4"
SFX = "audio/sfx.wav"
TARGET_LUFS = -17.6
TARGET_LRA = 4.5
TARGET_TP = -2.0

def pcm(path, t0, dur, sr=SR, ch=1):
    """Lee audio como float32 (n,ch). Retorna ceros si el archivo no existe."""
    try:
        cmd = ["ffmpeg", "-v", "error", "-ss", f"{t0:.6f}", "-t", f"{dur:.6f}", "-i", path,
               "-vn", "-ac", str(ch), "-ar", str(sr), "-f", "f32le", "-"]
        raw = subprocess.run(cmd, capture_output=True, check=True, timeout=30).stdout
        x = np.frombuffer(raw, np.float32).reshape(-1, ch)
        n = int(round(dur * sr))
        return np.pad(x, ((0, max(0, n - len(x))), (0, 0)), mode='constant')[:n, :]
    except Exception as e:
        print(f"Advertencia: no se pudo leer {path} @ {t0:.2f}: {e}", file=sys.stderr)
        return np.zeros((int(round(dur * sr)), ch), np.float32)

def hpf(x, sr, f_cut=70):
    """Highpass IIR Butterworth a f_cut Hz."""
    sos = signal.butter(2, f_cut, "highpass", fs=sr, output="sos")
    return signal.sosfiltfilt(sos, x, axis=0)

def xcorr_quality(ref, win, sr=SR, phat=True):
    """Correlación cruzada GCC-PHAT. Retorna (lag_s, pico/mediana, lag_idx, correlacion_vec, lags_vec)."""
    n = len(ref) + len(win)
    nfft = 1 << (n - 1).bit_length()
    R = np.fft.rfft(ref, nfft)
    W = np.fft.rfft(win, nfft)
    C = W * np.conj(R)
    if phat:
        C = C / (np.abs(C) + 1e-9 * np.abs(C).max())
    c = np.fft.irfft(C, nfft)
    c = np.concatenate([c[-(len(ref)-1):], c[:len(win)]])
    lags = np.arange(-(len(ref)-1), len(win))
    i = int(np.argmax(c))
    lag_s = lags[i] / sr
    q = c[i] / (np.median(np.abs(c)) + 1e-12)
    return lag_s, q, i, c, lags

def verify_correlation(seg_id, t0, dur, src_file, pc_file=PC_MAIN):
    """Verifica correlación cruzada entre un segmento y el archivo de PC."""
    ref_duration = min(5.0, dur)  # Ventana de referencia (máx 5 s)
    if t0 + ref_duration > duration_video(src_file):
        ref_duration = duration_video(src_file) - t0 - 0.1
    if ref_duration < 0.5:
        return None

    # Extrae audio del celular (referencia)
    ref = pcm(src_file, t0, ref_duration, sr=SR, ch=1)[:, 0]
    ref = hpf(ref, SR, 70)

    # Busca en el archivo PC con ventana amplia
    search_range = ref_duration + 30  # +30 s de búsqueda
    t_pc_approx = t0 + (seg_id["off"] if seg_id["off"] else 0)
    t_start = max(0, t_pc_approx - 15)

    win = pcm(pc_file, t_start, search_range, sr=SR, ch=1)[:, 0]
    win = hpf(win, SR, 70)

    try:
        lag, q, *_ = xcorr_quality(ref, win)
        return {"lag_s": lag, "quality": q, "t_approx": t_pc_approx}
    except Exception as e:
        print(f"Error en correlación para {seg_id['id']}: {e}", file=sys.stderr)
        return None

def duration_video(path):
    """Retorna duración en segundos."""
    try:
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
        return float(result.stdout.strip())
    except:
        return 3600  # Default: 1 hora

def build_voz_pc_only():
    """Construye voz_pc_only.wav con solo PC (0% celular), HPF 70 Hz."""
    total_samples = int(round(E["total"] * SR)) + SR
    voz = np.zeros(total_samples, np.float32)

    # Fade window (10-15 ms en los cortes)
    F = int(0.012 * SR)  # 12 ms
    r = np.sin(np.linspace(0, np.pi / 2, F)) ** 2

    print("Construyendo pista PC-only...")
    for s in E["segs"]:
        if not s["cam"]:
            continue

        d = s["dur"]
        t0_pc = s["t0"] + s["off"]

        # Lee audio del PC
        pc_audio = pcm(PC_MAIN, t0_pc, d, SR, 1)[:, 0]

        # Aplica HPF 70 Hz
        pc_audio = hpf(pc_audio, SR, 70)

        # Aplica fundidos en los extremos
        pc_audio[:F] *= r
        pc_audio[-F:] *= r[::-1]

        # Coloca en la línea de tiempo
        i = int(round(s["start"] * SR))
        voz[i:i + len(pc_audio)] += pc_audio
        print(f"  {s['id']:4s} ({s['start']:6.2f}-{s['end']:6.2f}) PC @ {t0_pc:.2f}s -> {d:.2f}s")

    N = int(round(E["total"] * SR))
    voz = voz[:N]

    # Guarda WAV
    import soundfile as sf
    sf.write("audio/voz_pc_only.wav", voz, SR, subtype="FLOAT")
    print(f"Guardado audio/voz_pc_only.wav ({N / SR:.2f} s, {len(voz)} muestras)")
    return voz

def mix_with_sfx(gain_db=0.0, out_path="audio/mixed_pc_only.wav"):
    """Mezcla voz_pc_only.wav + sfx.wav con ganancia lineal y limita a TP."""
    filter_str = (
        f"[0:a]highpass=f=70[v];"
        f"[v][1:a]amix=inputs=2:normalize=0:duration=first,"
        f"volume={gain_db:.3f}dB,"
        f"aresample=192000,"
        f"alimiter=limit={10 ** ((TARGET_TP - 0.7) / 20):.4f}:attack=1:release=60:level=disabled,"
        f"aresample=48000"
    )
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-v", "error", "-y",
         "-i", "audio/voz_pc_only.wav",
         "-i", SFX,
         "-filter_complex", filter_str,
         "-c:a", "pcm_s24le", out_path],
        check=True
    )
    print(f"Mezcla guardada en {out_path}")

def measure_loudness(path):
    """Mide LUFS, LRA y pico con ebur128."""
    result = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True
    )
    stderr = result.stderr
    summary = stderr.split("Summary:")[-1] if "Summary:" in stderr else ""

    try:
        I = float(re.search(r"I:\s+(-?[\d.]+)", summary)[1])
    except:
        I = None
    try:
        LRA = float(re.search(r"LRA:\s+(-?[\d.]+)", summary)[1])
    except:
        LRA = None
    try:
        P = float(re.search(r"Peak:\s+(-?[\d.]+)", summary)[1])
    except:
        P = None

    return I, LRA, P

def loudnorm_iterative(mixed_path="audio/mixed_pc_only.wav", final_path="audio/final_pc_only.wav"):
    """Itera para alcanzar I=-17.6 LUFS con ganancia lineal."""
    TARGET = TARGET_LUFS
    gain_db = 0.0

    print("Normalizando loudness...")
    for iteration in range(3):
        mix_with_sfx(gain_db, mixed_path)
        I, LRA, P = measure_loudness(mixed_path)
        print(f"  Iter {iteration}: gain={gain_db:+.2f} dB -> I={I} LUFS, LRA={LRA} LU, TP={P} dBTP")

        if I is None or abs(I - TARGET) < 0.15:
            break

        gain_db += TARGET - I

    # Copia el resultado como final
    import shutil
    shutil.copy(mixed_path, final_path)
    print(f"Final guardado en {final_path}: I={I}, LRA={LRA}, TP={P}")
    return I, LRA, P

def replace_audio_in_video(video_in, audio_in, video_out):
    """Sustituye audio en video sin recodificar el video (copy)."""
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-v", "error", "-y",
         "-i", video_in,
         "-i", audio_in,
         "-map", "0:v", "-map", "1:a",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-ar", "48000",
         video_out],
        check=True
    )
    print(f"Video con audio nuevo: {video_out}")

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corr", action="store_true", help="Verificar correlación cruzada")
    ap.add_argument("--out", default="../../entregables/Dia4_final_tiktok_audioPC.mp4", help="Video de salida")
    args = ap.parse_args()

    # 1. Verifica correlación si se pide
    if args.corr:
        print("\n=== Verificación de correlación cruzada ===")
        pc_files = ["../../CAMARA 10-45-16.mp4", "../../CAMARA 11-41-25.mp4", "../../PANTALLA 11-41-25.mp4"]
        results = {}

        for seg in E["segs"][:5]:  # Verifica primeros 5 tramos
            if not seg["cam"] or not seg["src"]:
                continue
            print(f"\nSegmento {seg['id']}: {seg['que'][:40]}...")
            results[seg["id"]] = {}

            for pc_file in pc_files:
                if not os.path.exists(pc_file):
                    print(f"  {pc_file}: NO EXISTE")
                    continue
                corr = verify_correlation(seg, seg["t0"], seg["dur"], seg["src"], pc_file)
                if corr:
                    print(f"  {pc_file}: lag={corr['lag_s']:+.4f}s, q={corr['quality']:.2f}")
                    results[seg["id"]][pc_file] = corr

        print("\nResultados guardados. El archivo con correlación más alta (q) es el correcto.")

    # 2. Construye pista PC-only
    print("\n=== Construcción de audio PC-only ===")
    os.makedirs("audio", exist_ok=True)
    build_voz_pc_only()

    # 3. Normaliza loudness
    print("\n=== Normalización de loudness ===")
    I, LRA, P = loudnorm_iterative()

    # 4. Sustituye en video
    print("\n=== Sustitución de audio en video ===")
    video_in = "../../entregables/Dia4_final_tiktok.mp4"
    if os.path.exists(video_in):
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        replace_audio_in_video(video_in, "audio/final_pc_only.wav", args.out)

        # 5. Mide el video final
        print("\n=== Mediciones del video final ===")
        I_final, LRA_final, P_final = measure_loudness(args.out)
        print(f"Final: I={I_final} LUFS, LRA={LRA_final} LU, TP={P_final} dBTP")
        print(f"Archivo: {args.out}")
    else:
        print(f"ERROR: No encontré {video_in}")

if __name__ == "__main__":
    main()
