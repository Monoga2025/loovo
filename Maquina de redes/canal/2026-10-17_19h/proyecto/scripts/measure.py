"""Mide color de una imagen: luma media/percentiles, RGB por terciles, piel (caja dada) y pared. Uso: measure.py img [x0 y0 x1 y1 piel] [x0 y0 x1 y1 pared]"""
import sys, cv2, numpy as np
im = cv2.imread(sys.argv[1])[:, :, ::-1].astype(np.float32)
Y = 0.2126*im[...,0]+0.7152*im[...,1]+0.0722*im[...,2]
p = np.percentile(Y, [1,5,25,50,75,95,99])
print("Y media %.1f  p1/5/25/50/75/95/99 %s" % (Y.mean(), " ".join("%.0f"%v for v in p)))
hsv = cv2.cvtColor((im/255).astype(np.float32), cv2.COLOR_RGB2HSV)
print("Sat media %.3f  clip(>=250) %.2f%%" % (hsv[...,1].mean(), 100*(im.max(-1)>=250).mean()))
t1, t2 = np.percentile(Y, [33, 66])
for n, m in [("bajas", Y < t1), ("medias", (Y>=t1)&(Y<t2)), ("altas", Y >= t2)]:
    print(n, "RGB", " ".join("%.1f" % v for v in im[m].mean(0)))
args = sys.argv[2:]
for name, i in [("piel", 0), ("pared", 4)]:
    if len(args) >= i+4:
        x0,y0,x1,y1 = map(int, args[i:i+4]); r = im[y0:y1, x0:x1].reshape(-1,3)
        lab = cv2.cvtColor((r.reshape(1,-1,3)/255).astype(np.float32), cv2.COLOR_RGB2Lab)[0].mean(0)
        print(name, "RGB %.0f %.0f %.0f  Lab L%.1f a%+.1f b%+.1f" % (*r.mean(0), *lab))
