import json, re, subprocess, sys
import numpy as np, soundfile as sf

SPEECH_UNDER_VOICE_DB = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
PAUSE_LIFT_DB = float(sys.argv[2]) if len(sys.argv) > 2 else 9.0
OUT = sys.argv[3] if len(sys.argv) > 3 else "epic_ducked.wav"
SRC = sys.argv[4] if len(sys.argv) > 4 else "music.wav"
OPEN_UNTIL = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
OPEN_LIFT_DB = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
MIN_GAP = 0.12
ATTACK = 0.04
RELEASE = 0.16

x, sr = sf.read(SRC)
n = len(x)
w = json.load(open("words_duck_env.json", encoding="utf-8"))
mask = np.zeros(n)
segs = []
for q in w:
    if segs and q["s"] - segs[-1][1] < MIN_GAP:
        segs[-1][1] = q["e"]
    else:
        segs.append([q["s"], q["e"]])
for a, b in segs:
    mask[int(a * sr): int(b * sr)] = 1.0
print("tramos de voz:", len(segs), "| huecos que suben la musica:", len(segs) - 1)

g_db = np.where(mask > 0.5, 0.0, PAUSE_LIFT_DB)
if OPEN_UNTIL > 0:
    g_db[: int(OPEN_UNTIL * sr)] = OPEN_LIFT_DB
ca = np.exp(-1.0 / (ATTACK * sr))
cr = np.exp(-1.0 / (RELEASE * sr))
sm = np.zeros(n)
cur = g_db[0]
for i in range(n):
    tgt = g_db[i]
    c = ca if tgt < cur else cr
    cur = c * cur + (1 - c) * tgt
    sm[i] = cur
gain = 10 ** (sm / 20)
y = x * gain[:, None]

def lufs(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
    return float(re.findall(r"I:\s+(-?\d+\.\d+) LUFS", r.stderr)[-1])

voice = lufs("voice_clean.wav")
sf.write("_tmp.wav", y.astype(np.float32), sr, subtype="PCM_16")
cur_l = lufs("_tmp.wav")
target = voice - SPEECH_UNDER_VOICE_DB
delta = target - cur_l
y = y * 10 ** (delta / 20)
sf.write(OUT, np.clip(y, -1, 1).astype(np.float32), sr, subtype="PCM_16")
print(f"voz {voice:.1f} LUFS | musica objetivo {target:.1f} LUFS | ajuste {delta:+.1f} dB | pico {20*np.log10(np.max(np.abs(y))):.1f} dBFS")
