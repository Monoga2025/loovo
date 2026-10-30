import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, sosfiltfilt

HERE = Path(__file__).resolve().parent
SR = 48000
PRESETS = {
    "v4": {"under": 1.5, "lift": 9.0, "open_until": 0.0, "open_lift": 0.0, "tail": 0.0},
    "v5": {"under": 3.0, "lift": 9.0, "open_until": 0.3, "open_lift": 4.0, "tail": 2.0},
    # v6 (Día 2): música de fondo (14 dB bajo la voz), SFX bajos y voz limpia/realzada
    "v8": {"under": 7.0, "lift": 3.0, "open_until": 0.0, "open_lift": 0.0, "tail": 0.0, "voice_fx": True, "voice_chain": "v8", "sfx_db": -15.0, "lufs": -11.0, "tp": -1.5, "limit": 0.85},
    "v6": {"under": 14.0, "lift": 3.0, "open_until": 0.0, "open_lift": 0.0, "tail": 0.0, "voice_fx": True, "sfx_db": -17.0},
}
# v8: voz más grave (-1 semitono con formantes preservados + cuerpo en graves), más densa y más fuerte
VOICE_FX_V8 = ("highpass=f=70,afftdn=nr=10:nf=-34:tn=1,"
               "agate=threshold=0.035:ratio=2.5:attack=5:release=180:range=0.25,"
               "rubberband=pitch=0.944:formant=preserved:pitchq=quality,"
               "equalizer=f=120:t=h:w=1:g=3,equalizer=f=300:t=q:w=1:g=-2,equalizer=f=3000:t=q:w=1:g=1.5,"
               "acompressor=threshold=-24dB:ratio=3.2:attack=6:release=130:makeup=3,"
               "acompressor=threshold=-14dB:ratio=2:attack=3:release=80:makeup=1,alimiter=limit=0.9")
VOICE_FX = ("highpass=f=80,afftdn=nr=10:nf=-34:tn=1,"
            "agate=threshold=0.035:ratio=2.5:attack=5:release=180:range=0.25,"
            "equalizer=f=220:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1:g=2.5,"
            "acompressor=threshold=-20dB:ratio=1.8:attack=10:release=150:makeup=1,alimiter=limit=0.9")
MIN_GAP = 0.12
ATTACK = 0.04
RELEASE = 0.16
STRONG_ATTACK_DB = 17.0


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)], check=True)


def lufs(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
    return float(re.findall(r"I:\s+(-?\d+\.\d+) LUFS", r.stderr)[-1])


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return float(r.stdout.strip())


def level_db(a, sr, t0, t1):
    seg = a[max(0, int(t0 * sr)): int(t1 * sr)]
    return 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9) if len(seg) else -120.0


def detect_taps(x, sr):
    lo = sosfilt(butter(4, [60, 500], "bandpass", fs=sr, output="sos"), x)
    blk = int(0.005 * sr)
    env = np.array([np.max(np.abs(lo[i:i + blk])) for i in range(0, len(lo) - blk, blk)])
    hits = []
    for i in range(12, len(env) - 30):
        if env[i] < env[i - 1] or env[i] < env[i + 1]:
            continue
        t = i * 0.005
        peak = level_db(lo, sr, t - 0.003, t + 0.007)
        attack = peak - level_db(lo, sr, t - 0.080, t - 0.020)
        decay = peak - level_db(lo, sr, t + 0.050, t + 0.110)
        if attack > 10 and decay > 10:
            hits.append((t, attack))
    events = []
    for t, attack in sorted(hits):
        if events and t - events[-1]["t"] <= 0.05:
            events[-1]["attack"] = max(events[-1]["attack"], attack)
        else:
            events.append({"t": round(t, 2), "attack": attack})
    return events


def ramp(n, sr, t0, t1, t2, t3, depth):
    g = np.ones(n)
    i0, i1, i2, i3 = [int(max(0, min(n - 1, t * sr))) for t in (t0, t1, t2, t3)]
    g[i0:i1] = 1 - (1 - depth) * 0.5 * (1 - np.cos(np.linspace(0, np.pi, max(1, i1 - i0))))
    g[i1:i2] = depth
    g[i2:i3] = depth + (1 - depth) * 0.5 * (1 - np.cos(np.linspace(0, np.pi, max(1, i3 - i2))))
    return g


def clean_voice(x, sr, events, words):
    n = len(x)
    low = sosfiltfilt(butter(4, [60, 500], "bandpass", fs=sr, output="sos"), x)
    gain = np.ones(n)
    broad = np.ones(n)
    report = []
    for e in events:
        t = e["t"]
        in_pause = not any(w["s"] - 0.03 <= t <= w["e"] + 0.03 for w in words)
        strong = e["attack"] >= STRONG_ATTACK_DB
        depth = 0.03 if in_pause else (0.06 if strong else 0.2)
        gain = np.minimum(gain, ramp(n, sr, t - 0.070, t - 0.050, t + 0.075, t + 0.110, depth))
        if in_pause:
            broad = np.minimum(broad, ramp(n, sr, t - 0.065, t - 0.050, t + 0.075, t + 0.110, 0.03))
        elif strong:
            broad = np.minimum(broad, ramp(n, sr, t - 0.065, t - 0.050, t + 0.035, t + 0.060, 0.5))
        report.append((t, "pausa" if in_pause else ("fuerte" if strong else "normal")))
    return (x - low * (1 - gain)) * broad, report


def speech_segments(words):
    segs = []
    for w in words:
        if segs and w["s"] - segs[-1][1] < MIN_GAP:
            segs[-1][1] = w["e"]
        else:
            segs.append([w["s"], w["e"]])
    return segs


def duck(music, sr, words, under, lift, open_until, open_lift, voice_lufs, work):
    n = len(music)
    mask = np.zeros(n)
    for a, b in speech_segments(words):
        mask[int(a * sr): int(b * sr)] = 1.0
    target_db = np.where(mask > 0.5, 0.0, lift)
    if open_until > 0:
        target_db[: int(open_until * sr)] = open_lift
    ca = np.exp(-1.0 / (ATTACK * sr))
    cr = np.exp(-1.0 / (RELEASE * sr))
    smooth = np.zeros(n)
    cur = target_db[0]
    for i in range(n):
        tgt = target_db[i]
        c = ca if tgt < cur else cr
        cur = c * cur + (1 - c) * tgt
        smooth[i] = cur
    y = music * (10 ** (smooth / 20))[:, None]
    tmp = work / "_tmp.wav"
    sf.write(tmp, y.astype(np.float32), sr, subtype="PCM_16")
    delta = (voice_lufs - under) - lufs(tmp)
    return np.clip(y * 10 ** (delta / 20), -1, 1), delta


def main():
    p = argparse.ArgumentParser()
    p.add_argument("proyecto")
    p.add_argument("--preset", choices=sorted(PRESETS), default="v4")
    p.add_argument("--under", type=float)
    p.add_argument("--sufijo", default="")
    a = p.parse_args()

    P = Path(a.proyecto).resolve()
    cfg = dict(PRESETS[a.preset])
    if a.under is not None:
        cfg["under"] = a.under
    name = a.sufijo or a.preset
    work = P / "audio_pro"
    work.mkdir(exist_ok=True)
    cut = P / "build" / "cut.mp4"
    words = json.loads((P / "build" / "words_out.json").read_text(encoding="utf-8"))
    base = {"tiktok": P / "out" / "final_tiktok.mp4", "reels": P / "out" / "final_reels.mp4"}

    voice_path = work / "voice48.wav"
    ffmpeg("-i", cut, "-vn", "-ac", 1, "-ar", SR, "-c:a", "pcm_s16le", voice_path)
    voice, _ = sf.read(voice_path)
    voice16_path = work / "voice16.wav"
    ffmpeg("-i", voice_path, "-ar", 16000, "-ac", 1, voice16_path)
    v16, sr16 = sf.read(voice16_path)
    events = detect_taps(v16, sr16)
    print(f"Golpes detectados: {len(events)} -> {[e['t'] for e in events]}")
    cleaned, report = clean_voice(voice, SR, events, words)
    clean_path = work / "voice_clean48.wav"
    sf.write(clean_path, cleaned, SR, subtype="PCM_16")
    ffmpeg("-i", clean_path, "-ar", 16000, "-ac", 1, work / "voice_clean16.wav")
    if cfg.get("voice_fx"):
        fx_path = work / "voice_fx48.wav"
        ffmpeg("-i", clean_path, "-af", VOICE_FX_V8 if cfg.get("voice_chain") == "v8" else VOICE_FX, "-ar", SR, "-ac", 1, "-c:a", "pcm_s16le", fx_path)
        clean_path = fx_path
    left = detect_taps(sf.read(work / "voice_clean16.wav")[0], 16000)
    print(f"Golpes que quedan tras limpiar: {len(left)}")

    voice_len = duration(clean_path)
    total = voice_len + cfg["tail"]
    # Día 3: el video trae un cierre animado después de la voz; la música cubre todo el video
    if base["tiktok"].exists():
        total = max(total, duration(base["tiktok"]))
    epic_path = work / "epic.wav"
    sting = [str(round(voice_len + 0.1, 2))] if (cfg["tail"] > 0 or total - voice_len > 0.5) else []
    subprocess.run([sys.executable, "-X", "utf8", str(HERE / "make_epic.py"), str(epic_path), f"{total:.4f}", *sting], check=True)
    music, sr_m = sf.read(epic_path)
    voice_lufs = lufs(clean_path)
    ducked, delta = duck(music, sr_m, words, cfg["under"], cfg["lift"], cfg["open_until"], cfg["open_lift"], voice_lufs, work)
    ducked_path = work / f"epic_ducked_{name}.wav"
    sf.write(ducked_path, ducked.astype(np.float32), sr_m, subtype="PCM_16")
    print(f"Voz {voice_lufs:.1f} LUFS | musica a {cfg['under']} dB bajo la voz | ajuste {delta:+.1f} dB")

    sfx = P / "audio" / "sfx.wav"
    sfx_input = ["-i", sfx] if sfx.exists() else []
    sfx_chain = f"[2:a]aformat=sample_rates={SR}:channel_layouts=stereo,volume={cfg.get('sfx_db', -8.0)}dB,apad=whole_dur={total}[s];" if sfx.exists() else ""
    mix_inputs = "[v][m][s]amix=inputs=3" if sfx.exists() else "[v][m]amix=inputs=2"
    mix_path = work / f"mix_{name}.wav"
    ffmpeg("-i", clean_path, "-i", ducked_path, *sfx_input, "-filter_complex",
           f"[0:a]aformat=sample_rates={SR}:channel_layouts=stereo,apad=whole_dur={total}[v];"
           f"[1:a]aformat=sample_rates={SR}:channel_layouts=stereo,equalizer=f=300:t=q:w=1:g=-3,equalizer=f=1500:t=q:w=0.8:g=-4[m];"
           f"{sfx_chain}{mix_inputs}:normalize=0:duration=first[o]", "-map", "[o]", "-c:a", "pcm_s16le", mix_path)
    first = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(mix_path), "-af", f"loudnorm=I={cfg.get('lufs', -14.0)}:TP={cfg.get('tp', -2.0)}:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(first[first.rindex("{"): first.rindex("}") + 1])
    fade = f",afade=t=out:st={total - 0.9:.3f}:d=0.9" if (cfg["tail"] > 0 or total - voice_len > 0.5) else ""
    final_audio = work / f"final_audio_{name}.wav"
    ffmpeg("-i", mix_path, "-af", f"loudnorm=I={cfg.get('lufs', -14.0)}:TP={cfg.get('tp', -2.0)}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,alimiter=limit={cfg.get('limit', 0.708)}:level=disabled{fade}", "-ar", SR, "-c:a", "pcm_s16le", final_audio)

    for platform, source in base.items():
        if not source.exists():
            print(f"Falta {source.name}; se omite {platform}.")
            continue
        out = P / "out" / f"final_{platform}_{name}.mp4"
        if cfg["tail"] > 0:
            vf = f"tpad=stop_mode=clone:stop_duration={cfg['tail']},fade=t=out:st={voice_len + 0.2:.3f}:d={cfg['tail'] - 0.2:.3f}"
            codec = ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "30"]
            if platform == "reels":
                codec = ["-c:v", "libx264", "-profile:v", "high", "-level", "4.2", "-b:v", "4500k", "-maxrate", "5000k", "-bufsize", "10000k", "-pix_fmt", "yuv420p", "-r", "30"]
            ffmpeg("-i", source, "-i", final_audio, "-vf", vf, "-map", "0:v", "-map", "1:a", *codec, "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", "-shortest", out)
        else:
            ffmpeg("-i", source, "-i", final_audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", "-shortest", out)
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(out), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
        i_val = re.findall(r"I:\s+(-?\d+\.\d+) LUFS", r)[-1]
        peak = re.findall(r"Peak:\s+(-?\d+\.\d+) dBFS", r)[-1]
        print(f"{out.name}: {i_val} LUFS, pico {peak} dBTP, {duration(out):.2f} s")


main()
