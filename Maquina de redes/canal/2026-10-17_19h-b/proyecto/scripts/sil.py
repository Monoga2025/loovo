import sys, numpy as np, soundfile as sf
x, sr = sf.read("audio/declip48.wav"); h = sr // 100
n = len(x) // h; env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
np.save("build/env10.npy", env)
thr = float(sys.argv[1]); a = sys.argv[2:]
for i in range(0, len(a), 2):
    t0, t1 = float(a[i]), float(a[i + 1]); seg = env[int(t0 * 100):int(t1 * 100)]
    runs, st = [], None
    for k, v in enumerate(np.r_[seg < thr, False]):
        if v and st is None: st = k
        if not v and st is not None:
            if k - st >= 12: runs.append(f"{t0 + st / 100:.2f}-{t0 + k / 100:.2f}")
            st = None
    print(f"{t0}-{t1}: sil", " ".join(runs))
