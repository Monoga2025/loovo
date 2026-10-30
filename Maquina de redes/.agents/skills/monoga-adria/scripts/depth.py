"""Mapa de profundidad (Depth Anything V2 Small, Apache-2.0) para la escena 2.5D. Uso: depth.py img.jpg out.png"""
import sys, numpy as np, cv2, torch
from transformers import pipeline
from PIL import Image
pipe = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Small-hf", device=0 if torch.cuda.is_available() else -1)
for src in sys.argv[1:]:
    im = Image.open(src).convert("RGB")
    r = pipe(im)
    d = np.array(r["predicted_depth"].squeeze().float().cpu() if hasattr(r["predicted_depth"],"cpu") else r["predicted_depth"], np.float32)
    d = cv2.resize(d, im.size, interpolation=cv2.INTER_CUBIC)
    d = (d - d.min()) / (d.max() - d.min() + 1e-9)   # 1 = cerca
    out = src.rsplit(".",1)[0] + "_depth.png"
    cv2.imwrite(out, (d*65535).astype(np.uint16)); print(out, d.shape)
