"""Mezcla final: voz (SOLO mic del PC, HPF 70 Hz, fundidos 12 ms) -> compresor suave 2:1 -> + SFX (SFX_DB) ->
medición loudnorm (pasada 1) -> ganancia lineal + limitador x4 (pasada 2, iterada) a I -17,6 LUFS / TP <= -2 dBTP.
(loudnorm de 2 pasadas pasaba a modo 'dynamic' porque el pico no cabía: ver voz-y-color.md de la skill). -> audio/final.wav"""
import json, subprocess, sys
SFX_DB = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
inp = ["-i", "audio/voz_raw.wav", "-i", "audio/sfx.wav"]
pre = (f"[0:a]acompressor=threshold=-24dB:ratio=2:attack=12:release=180:knee=6:makeup=1,pan=stereo|c0=c0|c1=c0[v];"
       f"[1:a]volume={SFX_DB}dB[s];[v][s]amix=inputs=2:normalize=0:duration=first")
def meas(chain, out=None):
    args = ["ffmpeg", "-hide_banner", "-y", *inp, "-filter_complex", chain + ",loudnorm=I=-17.6:TP=-2:print_format=json"]
    if out: args = ["ffmpeg", "-hide_banner", "-y", *inp, "-filter_complex", chain, "-c:a", "pcm_f32le", "-ar", "48000", out]
    else: args += ["-f", "null", "-"]
    r = subprocess.run(args, capture_output=True, text=True).stderr
    return None if out else json.loads(r[r.rindex("{"):r.rindex("}") + 1])
m = meas(pre); g = -17.6 - float(m["input_i"])
for it in range(4):
    chain = pre + f",volume={g:.3f}dB,aresample=192000,alimiter=limit=0.70:attack=1:release=60:level=false,aresample=48000"
    m2 = meas(chain); I = float(m2["input_i"])
    print(f"iter {it}: ganancia {g:+.2f} dB -> I {I} LUFS, TP {m2['input_tp']} dBTP, LRA {m2['input_lra']}")
    if abs(I + 17.6) < 0.08: break
    g += -17.6 - I
meas(chain, "audio/final.wav"); print("ok audio/final.wav; pasada1:", m["input_i"], m["input_tp"], m["input_lra"])
