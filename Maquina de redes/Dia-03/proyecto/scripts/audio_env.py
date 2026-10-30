# FILE: audio_env.py
# Envolvente de energía (10 ms) de audio/audio.wav para ajustar y validar cortes
# contra la voz real, no contra los timestamps de Whisper.
import os
import wave
import numpy as np

HOP = 0.01
THR = float(os.environ.get("AUDIO_THR", -36.0))  # dB (AUDIO_THR para cuartos o calles ruidosas); piso de ruido ~-44, voz -12 a -30 (calibrado en este clip)
MIN_RUN = 3      # frames sobre THR para contar como voz (ignora clics)
MIN_SIL = 5      # frames bajo THR para contar como silencio real


def load(path="audio/audio.wav"):
    wf = wave.open(path)
    sr = wf.getframerate()
    a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    hop = int(sr * HOP)
    n = len(a) // hop
    db = 20 * np.log10(np.sqrt((a[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)
    raw = db > THR
    speech = np.zeros(n, bool)
    i = 0
    while i < n:
        if raw[i]:
            j = i
            while j < n and raw[j]:
                j += 1
            if j - i >= MIN_RUN:
                speech[i:j] = True
            i = j
        else:
            i += 1
    return speech


def is_silent(speech, t, half=2):
    i = int(round(t / HOP))
    return not speech[max(i - half, 0):i + half + 1].any()


def snap_start(speech, t, back=40, fwd=100):
    """Inicio real de la voz cerca de t (frame)."""
    i = int(round(t / HOP))
    if speech[i]:
        k = 0
        while k < back and not (~speech[i - MIN_SIL:i]).all():
            i -= 1
            k += 1
        while i > 0 and not speech[i]:
            i += 1
        return i * HOP
    k = 0
    while k < fwd and not speech[i]:
        i += 1
        k += 1
    return i * HOP


def snap_end(speech, t, fwd=40, back=100, look=15):
    """Final real de la voz cerca de t (fin del último frame con voz).
    Whisper suele cerrar la palabra antes de su cola: si hay voz en los
    siguientes `look` frames, se sigue hasta el silencio real."""
    i = int(round(t / HOP))
    if not speech[i] and look:
        ahead = np.flatnonzero(speech[i + 1:i + 1 + look])
        if ahead.size:
            i = i + 1 + int(ahead[0])
    if speech[i]:
        k = 0
        while k < fwd and not (~speech[i + 1:i + 1 + MIN_SIL]).all():
            i += 1
            k += 1
        return (i + 1) * HOP
    k = 0
    while k < back and not speech[i]:
        i -= 1
        k += 1
    return (i + 1) * HOP
