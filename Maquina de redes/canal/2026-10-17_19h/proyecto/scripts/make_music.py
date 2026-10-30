# FILE: make_music.py
# Uso: python3 make_music.py salida.wav duracion_s [bpm]
# Instrumental suave generado nota a nota (libre de derechos): pad de acordes
# Am-F-C-G tipo piano eléctrico, bajo, kick y hi-hat suaves. 48 kHz estéreo.
import sys, wave
import numpy as np

out, dur = sys.argv[1], float(sys.argv[2])
bpm = float(sys.argv[3]) if len(sys.argv) > 3 else 88
SR = 48000
beat = 60 / bpm
n = int(SR * (dur + 1))
L = np.zeros(n)
R = np.zeros(n)


def midi(m):
    return 440 * 2 ** ((m - 69) / 12)


def add(buf, start, sig):
    i = int(start * SR)
    if i >= n:
        return
    sig = sig[:n - i]
    buf[i:i + len(sig)] += sig


def epiano(f, length, vel):
    t = np.arange(int(length * SR)) / SR
    env = np.exp(-t * 2.2) * (1 - np.exp(-t * 200))
    tone = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 6)
    trem = 1 + 0.08 * np.sin(2 * np.pi * 4.5 * t)
    return vel * tone * env * trem


def bass(f, length, vel):
    t = np.arange(int(length * SR)) / SR
    env = np.minimum(t * 80, 1) * np.exp(-t * 1.5)
    return vel * np.sin(2 * np.pi * f * t) * env


def kick(vel):
    t = np.arange(int(0.35 * SR)) / SR
    f = 50 + 70 * np.exp(-t * 30)
    return vel * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


rng = np.random.default_rng(42)


def hat(vel):
    t = np.arange(int(0.05 * SR)) / SR
    noise = rng.standard_normal(len(t))
    noise = np.diff(noise, prepend=0)  # pasa-altos simple
    return vel * noise * np.exp(-t * 90)


# Am - F - C - G (voicings en registro medio)
chords = [[57, 60, 64, 69], [53, 57, 60, 65], [55, 60, 64, 67], [55, 59, 62, 67]]
roots = [45, 41, 48, 43]
bar = 4 * beat
t = 0.0
k = 0
while t < dur:
    ch, rt = chords[k % 4], roots[k % 4]
    for b in (0, 2.5):  # acorde en el 1 y anticipación en el "y" del 3
        for j, m in enumerate(ch):
            sig = epiano(midi(m), bar, 0.10 if b == 0 else 0.06)
            pan = 0.35 + 0.1 * j
            add(L, t + b * beat + 0.012 * j, sig * (1 - pan))
            add(R, t + b * beat + 0.012 * j, sig * pan)
    for b in (0, 1.5, 2):
        sig = bass(midi(rt), beat * 1.4, 0.22)
        add(L, t + b * beat, sig)
        add(R, t + b * beat, sig)
    for b in (0, 2):
        s = kick(0.35)
        add(L, t + b * beat, s)
        add(R, t + b * beat, s)
    for b in np.arange(0, 4, 0.5):
        s = hat(0.05 if b % 1 else 0.03)
        add(L, t + b * beat, s * 0.7)
        add(R, t + b * beat, s)
    t += bar
    k += 1

L, R = L[:int(dur * SR)], R[:int(dur * SR)]
fade_in, fade_out = int(0.4 * SR), int(1.5 * SR)
for ch in (L, R):
    ch[:fade_in] *= np.linspace(0, 1, fade_in)
    ch[-fade_out:] *= np.linspace(1, 0, fade_out)
peak = max(abs(L).max(), abs(R).max())
st = (np.stack([L, R], 1) / peak * 0.7 * 32767).astype(np.int16)
wf = wave.open(out, "wb")
wf.setnchannels(2)
wf.setsampwidth(2)
wf.setframerate(SR)
wf.writeframes(st.tobytes())
wf.close()
print(f"{dur:.2f}s a {bpm:.0f} BPM -> {out}")
