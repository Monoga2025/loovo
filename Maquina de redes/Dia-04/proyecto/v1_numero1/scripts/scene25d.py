"""Escena 2.5D 'cámara en el entorno' (receta Adrià 8:51): foto -> profundidad (Depth Anything V2) -> 3 capas
(fondo/medio/sujeto) con relleno detrás, parallax 1 : 1,65 : 1,9 en x, escala por capa, fondo más desenfocado,
desenfoque de movimiento por submuestreo en los empujes. Dos planos con zoom-through entre ellos.
Uso: scene25d.py out.mp4   (tiempos en plan/scene25d.json)"""
import sys, json, subprocess, numpy as np, cv2
W, H, FPS = 1080, 1920, 30
OUT = sys.argv[1]
def grade(img, sat=0.62, warm=(1.0, 0.975, 0.92), lift=8, kill_green=True):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    if kill_green:  # cuerdas verdes/teal -> neutras (marca: nada de verde)
        g = ((hsv[..., 0] > 35) & (hsv[..., 0] < 105)).astype(np.float32)
        hsv[..., 1] *= (1 - 0.85 * cv2.GaussianBlur(g, (0, 0), 3))
    hsv[..., 1] *= sat
    o = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32)
    o = o * np.array(warm[::-1], np.float32)          # BGR
    o = lift + o * (255 - lift) / 255
    return np.clip(o, 0, 255).astype(np.uint8)
def layers(img_p, dep_p, t1, t2, cover, crop_x=None, blur_far=6.0, quant=False):
    img = cv2.imread(img_p); d = cv2.imread(dep_p, cv2.IMREAD_UNCHANGED).astype(np.float32) / 65535
    if crop_x is not None:   # recorte vertical 9:16 de una foto horizontal
        w = int(img.shape[0] * 9 / 16 * crop_x[1]); x0 = int((img.shape[1] - w) * crop_x[0])
        img, d = img[:, x0:x0 + w], d[:, x0:x0 + w]
    s = max(W * cover / img.shape[1], H * cover / img.shape[0])
    img = cv2.resize(img, None, fx=s, fy=s, interpolation=cv2.INTER_AREA); d = cv2.resize(d, (img.shape[1], img.shape[0]))
    img = grade(img)
    if quant: t1, t2 = np.quantile(d, t1), np.quantile(d, t2)   # umbrales por cuantil (fotos con poco primer plano)
    def soft(m, sig): return np.clip(cv2.GaussianBlur(m.astype(np.float32), (0, 0), sig), 0, 1)
    mn = soft(d > t2, 2.5); mm = soft(d > t1, 4)
    def fill(im, m):  # rellena lo tapado por capas cercanas (inpaint a 1/4 y vuelve)
        sm = cv2.resize(im, None, fx=.25, fy=.25, interpolation=cv2.INTER_AREA)
        mk = (cv2.resize(m, (sm.shape[1], sm.shape[0])) > 0.02).astype(np.uint8) * 255
        mk = cv2.dilate(mk, np.ones((7, 7), np.uint8))
        f = cv2.resize(cv2.inpaint(sm, mk, 9, cv2.INPAINT_TELEA), (im.shape[1], im.shape[0]), interpolation=cv2.INTER_CUBIC)
        a = cv2.GaussianBlur(cv2.resize(mk, (im.shape[1], im.shape[0])).astype(np.float32) / 255, (0, 0), 4)[..., None]
        return (im * (1 - a) + f * a).astype(np.uint8)
    far = fill(img, mm); mid = fill(img, mn)
    far = cv2.GaussianBlur(far, (0, 0), blur_far); mid = cv2.GaussianBlur(mid, (0, 0), 1.6)   # fondo ~4x más borroso
    return [(far, None), (mid, mm), (img, mn)]
def place(layer, sx, dx, dy):
    im, a = layer; h, w = im.shape[:2]
    M = np.array([[sx, 0, W / 2 - sx * w / 2 + dx], [0, sx, H / 2 - sx * h / 2 + dy]])
    o = cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    if a is None: return o.astype(np.float32), None
    return o.astype(np.float32), cv2.warpAffine(a, M, (W, H), flags=cv2.INTER_LINEAR, borderValue=0)[..., None]
def comp(L, cam):
    # cam(t) -> (escala, dx, dy) del plano; capas: k_x = 1, 1.65, 1.9 ; escala^k = 1, 1.15, 1.3
    s, dx, dy = cam
    out = None
    for (lay, kx, ks) in zip(L, (1.0, 1.65, 1.9), (1.0, 1.15, 1.3)):
        im, a = place(lay, s ** ks, dx * kx, dy * kx)
        out = im if a is None else out * (1 - a) + im * a
    return out
expo_out = lambda u: 1 - 2 ** (-10 * u) if u < 1 else 1.0
p2io = lambda u: 2 * u * u if u < .5 else 1 - (-2 * u + 2) ** 2 / 2
p4in = lambda u: u ** 4
def seg(t, a, b, v0, v1, f): u = min(max((t - a) / (b - a), 0), 1); return v0 + (v1 - v0) * f(u)
cfg = json.load(open("plan/scene25d.json"))
LA = layers("_dl/lib_busto.jpg", "_dl/lib_busto_depth.png", cfg["A"]["t1"], cfg["A"]["t2"], 1.32)
LB = layers("_dl/lib_sala.jpg", "_dl/lib_sala_depth.png", cfg["B"]["t1"], cfg["B"]["t2"], 1.30, crop_x=(0.5, 1.0), blur_far=3.0, quant=True)
TA, TB, XF = cfg["A"]["dur"], cfg["B"]["dur"], cfg["xfade"]       # B empieza en TA - XF
def camA(t):   # paneo expo.out 2,7 s (fondo -140 px), reposo, empuje power4.in a 1,45
    dx = seg(t, 0, 2.7, 70, -70, expo_out); dy = seg(t, 0, 2.7, 0, -12, expo_out)
    s = seg(t, TA - 1.15, TA, 1.0, 1.45, p4in)
    return s, dx, dy
def camB(t):   # entra empujando y frena (expo.out), reposo, dolly-out power2.inOut 1,9 s, empuje final power4.in
    s = seg(t, 0, 0.7, 1.06, 1.20, expo_out)
    s = s * seg(t, 0.7, TB - 0.92, 1.0, 0.86, p2io) * seg(t, TB - 0.92, TB, 1.0, 1.40, p4in)
    dy = seg(t, 0.7, TB - 0.92, 0, 40, p2io)
    return s, 0.0, dy
def speed(f, t, dt=1 / FPS):
    a, b = f(t), f(t + dt); return abs(np.log(b[0] / a[0])) * 900 + abs(b[1] - a[1]) + abs(b[2] - a[2])
N = int(round((TA + TB - XF) * FPS))
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                       "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "14", "-preset", "medium", OUT], stdin=subprocess.PIPE)
def render(L, f, t):
    v = speed(f, t); n = 1 if v < 6 else min(8, int(v / 6) + 1)   # submuestreo = desenfoque de movimiento
    acc = sum(comp(L, f(t + k / (FPS * n))) for k in range(n)) / n
    return acc
yy, xx = np.mgrid[0:H, 0:W]; vig = 1 - 0.22 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
vig = np.clip(vig, 0.6, 1)[..., None].astype(np.float32)
for n in range(N):
    t = n / FPS
    if t < TA - XF: o = render(LA, camA, t)
    elif t < TA:
        u = (t - (TA - XF)) / XF; u = u * u * (3 - 2 * u)
        o = render(LA, camA, t) * (1 - u) + render(LB, camB, t - (TA - XF)) * u
    else: o = render(LB, camB, t - (TA - XF))
    o = np.clip(o * vig, 0, 255).astype(np.uint8)
    enc.stdin.write(o.tobytes())
enc.stdin.close(); enc.wait(); print("frames", N)
