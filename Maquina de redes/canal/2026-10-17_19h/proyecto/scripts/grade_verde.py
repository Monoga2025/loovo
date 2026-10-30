"""Corrección del verde lateral (luz RGB) + exposición. Uso: grade_verde.py in.png out.png  (o importar fix())"""
import sys, cv2, numpy as np
LUT = None
def fix(bgr):
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    d = np.clip(130.0 - a, 0, None)           # cuanto le falta al rojo/magenta (verde)
    w = np.clip((L - 20) / 60, 0, 1)          # no tocar negros (camisa)
    a += d * 1.05 * w
    b -= np.clip(b - 136, 0, None) * 0.55 * np.clip(d / 12, 0, 1) * w  # el verde-amarillo deja b alto
    # exposición: subir medios (gamma) y un poco de contraste
    Ln = L / 255.0
    Ln = np.power(Ln, 0.86)
    Ln = 0.5 + (Ln - 0.5) * 1.06
    lab[..., 0] = np.clip(Ln * 255, 0, 255)
    out = cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
    return out
if __name__ == "__main__":
    cv2.imwrite(sys.argv[2], fix(cv2.imread(sys.argv[1])))
