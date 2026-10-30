"""voz_adria.py - deja la voz "al nivel de Adrià Solà" (medido en su video: I -17,6 LUFS, LRA 4,3-4,9, TP <= -2 dBTP).
Cadena: highpass 80 + EQ (-2 dB 150 Hz, -1,5 dB 350 Hz, -2,5 dB 3,5 kHz) + compresor 3,5:1 (umbral -30 dB, +4 dB)
-> mezcla opcional con SFX -> ganancia LINEAL al objetivo (medida con ebur128, 2-3 iteraciones)
-> limitador con sobremuestreo x4 a TP-0,7 dB (el AAC sube el pico ~0,3-0,5 dB: con -0,25 salió -1,7 dBTP en el MP4).
Por qué no loudnorm: en el Día 4 loudnorm (2 pasadas) caía en modo 'dynamic' porque el pico real no cabía y aplastaba
el LRA a 4,1. La ganancia lineal + limitador dio I -17,6 / LRA 4,6 / TP -2,2.
Uso: python voz_adria.py voz.wav [sfx.wav|-] salida.wav [--target -17.6] [--tp -2]
Mide SIEMPRE otra vez en el MP4 final: ffmpeg -i final.mp4 -af ebur128=peak=true -f null -"""
import argparse, re, subprocess
CH = ("highpass=f=80,equalizer=f=150:t=q:w=1:g=-2,equalizer=f=350:t=q:w=1:g=-1.5,equalizer=f=3500:t=q:w=0.8:g=-2.5,"
      "acompressor=threshold=-30dB:ratio=3.5:attack=8:release=200:makeup=4:knee=6")
ap = argparse.ArgumentParser(); ap.add_argument("voz"); ap.add_argument("sfx"); ap.add_argument("out")
ap.add_argument("--target", type=float, default=-17.6); ap.add_argument("--tp", type=float, default=-2.0)
a = ap.parse_args()
def mix(gain):
    inp = ["-i", a.voz] + (["-i", a.sfx] if a.sfx != "-" else [])
    pre = f"[0:a]{CH},aformat=channel_layouts=stereo[v];" + ("[v][1:a]amix=inputs=2:normalize=0:duration=first" if a.sfx != "-" else "[v]anull")
    f = (pre + f",volume={gain:.3f}dB,aresample=192000,alimiter=limit={10 ** ((a.tp - 0.7) / 20):.4f}:attack=1:release=60:level=disabled,"
         "aresample=48000")
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", *inp, "-filter_complex", f, "-c:a", "pcm_s24le", a.out], check=True)
def meas(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    s = e.split("Summary:")[-1]
    return [float(re.search(rx, s)[1]) for rx in (r"I:\s+(-?[\d.]+)", r"LRA:\s+(-?[\d.]+)", r"Peak:\s+(-?[\d.]+)")]
g = 0.0
for it in range(3):
    mix(g); I, LRA, P = meas(a.out); print(f"it{it} ganancia {g:+.2f} dB -> I {I} LUFS  LRA {LRA} LU  TP {P} dBTP")
    if abs(I - a.target) < 0.15: break
    g += a.target - I
