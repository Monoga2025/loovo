N = int(round(TOT * SR)); L = np.zeros(N); R = np.zeros(N)
for q in C:
    i = int(q["t"] * SR)
    if i >= N: continue
    if q["type"] == "mixkit":
        s2 = mx[:N - i] * q["gain"]; L[i:i + len(s2)] += s2[:, 0]; R[i:i + len(s2)] += s2[:, -1]; continue
    s, pan = hiw() if q["type"] == "hiw" else G[q["type"]]()
    s = s[:N - i] * q["gain"]; p = np.linspace(-pan, pan, len(s)) if pan else np.zeros(len(s))
    L[i:i + len(s)] += s * (1 - p) / 2 * 2 ** .5; R[i:i + len(s)] += s * (1 + p) / 2 * 2 ** .5
sf.write("audio/sfx.wav", np.stack([L, R], 1).astype(np.float32), SR, subtype="FLOAT")
json.dump(C, open("plan/sfx_cues.json", "w"), indent=0)
print(len(C), "cues; pico", round(float(max(abs(L).max(), abs(R).max())), 3))
