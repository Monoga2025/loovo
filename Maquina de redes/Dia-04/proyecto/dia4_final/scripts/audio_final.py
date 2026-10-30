"""Voz al nivel de Adrià (receta medida: I -17,6 LUFS, LRA 4,5, TP -2 dBTP).
Cadena: highpass+EQ+compresor sobre la voz -> mezcla con SFX -> ganancia lineal al objetivo (medida con ebur128)
-> limitador de pico real (sobremuestreo x4) a -2,2 dBFS. loudnorm 2 pasadas caía en modo 'dynamic' (LRA 4,1) porque
el pico real no cabía; la ganancia lineal + limitador conserva la dinámica (LRA ~4,6). -> audio/final.wav"""
import re, subprocess, sys
CH = ("highpass=f=80,equalizer=f=150:t=q:w=1:g=-2,equalizer=f=350:t=q:w=1:g=-1.5,equalizer=f=3500:t=q:w=0.8:g=-2.5,"
      "acompressor=threshold=-30dB:ratio=3.5:attack=8:release=200:makeup=4:knee=6")
TARGET, TP = -17.6, -2.0
def mix(gain, out):
    f = (f"[0:a]{CH},aformat=channel_layouts=stereo[v];[v][1:a]amix=inputs=2:normalize=0:duration=first,volume={gain:.3f}dB,"
         f"aresample=192000,alimiter=limit={10 ** ((TP - 0.7) / 20):.4f}:attack=1:release=60:level=disabled,aresample=48000")
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", "audio/voz_raw.wav", "-i", "audio/sfx.wav", "-filter_complex", f,
                    "-c:a", "pcm_s24le", out], check=True)
def meas(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    s = e.split("Summary:")[-1]
    return float(re.search(r"I:\s+(-?[\d.]+)", s)[1]), float(re.search(r"LRA:\s+(-?[\d.]+)", s)[1]), float(re.search(r"Peak:\s+(-?[\d.]+)", s)[1])
g = 0.0
for it in range(3):
    mix(g, "audio/final.wav"); I, LRA, P = meas("audio/final.wav")
    print(f"it{it} gain {g:+.2f} dB -> I {I} LRA {LRA} TP {P}")
    if abs(I - TARGET) < 0.15: break
    g += TARGET - I
