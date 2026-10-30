"""Desfase labios-voz: energía de movimiento en la zona de la boca vs envolvente de voz (derivada positiva),
correlación cruzada en ±8 cuadros. Lag>0 = la voz va tarde respecto a la boca. Uso: lipsync.py video t0 t1 cx cy w h"""
import sys, subprocess, numpy as np, cv2
v, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]); cx, cy, w, h = map(int, sys.argv[4:8])
raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t0),"-t",str(t1-t0),"-i",v,"-vf","fps=30,format=gray","-f","rawvideo","-"],capture_output=True).stdout
f = np.frombuffer(raw,np.uint8).reshape(-1,1920,1080)[:, cy-h//2:cy+h//2, cx-w//2:cx+w//2].astype(np.float32)
f = np.array([cv2.GaussianBlur(x,(5,5),0) for x in f])
mot = np.r_[0, np.abs(np.diff(f,axis=0)).mean((1,2))]
a = subprocess.run(["ffmpeg","-v","error","-ss",str(t0),"-t",str(t1-t0),"-i",v,"-vn","-ac","1","-ar","48000","-f","f32le","-"],capture_output=True).stdout
a = np.frombuffer(a,np.float32); hop = 1600; n = min(len(mot), len(a)//hop); mot = mot[:n]
env = np.array([np.sqrt(np.mean(a[i*hop:(i+1)*hop]**2)+1e-9) for i in range(n)])
env = 20*np.log10(env); da = np.r_[0, np.abs(np.diff(env))]
z = lambda x: (x-x.mean())/(x.std()+1e-9)
m, d = z(mot), z(da)
res = []
for L in range(-8, 9):
    if L >= 0: c = np.mean(m[:n-L]*d[L:])
    else: c = np.mean(m[-L:]*d[:n+L])
    res.append((L, c))
best = max(res, key=lambda r: r[1])
print(" ".join(f"{L:+d}:{c:.2f}" for L, c in res))
print(f"mejor lag {best[0]:+d} cuadros = {best[0]*1000/30:+.0f} ms (r={best[1]:.2f})")
