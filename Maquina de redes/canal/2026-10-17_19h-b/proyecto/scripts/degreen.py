"""Quita el derrame de luz verde (piel) en Lab: empuja a* negativo hacia piel y baja b* donde hubo verde.
Uso como módulo: degreen(bgr_uint8) -> bgr_uint8."""
import numpy as np, cv2
def degreen(im, target_a=12.0, strength=1.0):
    lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB).astype(np.float32)
    L, a, b = lab[..., 0], lab[..., 1] - 128, lab[..., 2] - 128
    C = np.sqrt(a * a + b * b)
    w = np.clip((-a + 1.0) / 8.0, 0, 1) * np.clip((L - 20) / 30.0, 0, 1) * np.clip((C - 9.0) / 8.0, 0, 1)   # verde con luz (no la camisa negra)
    w = cv2.GaussianBlur(w, (0, 0), 3) * strength
    a2 = a + w * (target_a - a)
    b2 = b - w * np.clip(b - 13, 0, None) * 0.85
    L2 = L - w * 4.0                                   # el verde sobreexpone: baja un poco
    # leve neutralización global del verde residual (pared/camisa)
    a2 = a2 + 0.6
    lab = np.dstack([L2, a2 + 128, b2 + 128])
    return cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        im = cv2.imread(f); o = degreen(im)
        cv2.imwrite(f.replace(".png", "_dg.png"), o)
