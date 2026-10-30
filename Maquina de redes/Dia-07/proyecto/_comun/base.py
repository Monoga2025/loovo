"""Base de video de toda la línea (persona + pantalla grabada con el celular) -> motion/assets/base.mp4.
Cada tramo i ocupa [start_i - gap_i, start_{i+1} - gap_{i+1}) (la pausa previa ya muestra el plano nuevo; nunca se congela).
Vista por tramo en plan/edl.json -> 'view': {src (s del crudo donde arranca la imagen; por defecto a),
keys [[t_rel, cx, cy, z], ...] (cámara 2.5D: reencuadre 9:16, paneo y zoom easeInOutSine, desenfoque de
movimiento por submuestreo), look 'cam' (LUT Adrià 75 %) o 'scr' (pantalla: verdes neutralizados, sat 0,72, levantado)}.
Desenfoques de privacidad en plan/edl.json -> 'blur': [{t0, t1 (s del crudo), r: [x0,y0,x1,y1] en 1080x1920 del crudo}]
(pixelado 1/28 + gauss 18 px, aplicado ANTES del reencuadre). Ejecutar en la carpeta del proyecto."""
import json, subprocess, numpy as np, cv2, sys
SRC = "C:/Users/you/Desktop/VID_20261013_110529.mp4"; LUT = "assets_src/adria_look_75.cube"
W, H, FPS = 1080, 1920, 30
E = json.load(open("plan/edl.json", encoding="utf-8")); segs = [s for s in E["segs"] if s.get("view")]
BL = E.get("blur", [])
sine = lambda u: 0.5 - 0.5 * np.cos(np.pi * u)
def cam(keys, tr):
    if tr <= keys[0][0]: return keys[0][1:]
    for k0, k1 in zip(keys, keys[1:]):
        if tr <= k1[0]:
            u = sine(min(max((tr - k0[0]) / max(k1[0] - k0[0], 1e-6), 0), 1))
            return [a + (b - a) * u for a, b in zip(k0[1:], k1[1:])]
    return keys[-1][1:]
def M_for(cx, cy, z):
    cx = min(max(cx, W / 2 / z), W - W / 2 / z); cy = min(max(cy, H / 2 / z), H - H / 2 / z)
    return np.array([[z, 0, W / 2 - z * cx], [0, z, H / 2 - z * cy]], np.float64)
def grade_scr(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    g = ((hsv[..., 0] > 30) & (hsv[..., 0] < 100)).astype(np.float32)
    hsv[..., 1] *= (1 - 0.9 * g); hsv[..., 1] *= 0.72
    o = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32)
    o = o * np.array([0.93, 0.985, 1.0], np.float32)   # BGR: un poco cálido
    o = 10 + o * 1.06
    return np.clip(o, 0, 255).astype(np.uint8)
# pantalla: verdes/cian neutralizados (marca: nada de verde), saturación 0,72, levantado y un poco cálido (en ffmpeg: menos RAM)
SCR = "huesaturation=saturation=-1:colors=g+c:strength=100,eq=saturation=0.72:brightness=0.035:gamma=1.04,colorbalance=rm=0.03:bm=-0.04"
def privacy(img, tsrc):
    for b in BL:
        if b["t0"] <= tsrc <= b["t1"]:
            x0, y0, x1, y1 = [int(v) for v in b["r"]]; x0, y0 = max(x0, 0), max(y0, 0); x1, y1 = min(x1, W), min(y1, H)
            roi = img[y0:y1, x0:x1]
            if roi.size == 0: continue
            sm = cv2.resize(roi, (max(1, (x1 - x0) // 28), max(1, (y1 - y0) // 28)), interpolation=cv2.INTER_AREA)
            roi = cv2.resize(sm, (x1 - x0, y1 - y0), interpolation=cv2.INTER_LINEAR)
            img[y0:y1, x0:x1] = cv2.GaussianBlur(roi, (0, 0), 18)
    return img
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "15", "-preset", "veryfast", "-threads", "2", "-x264-params", "rc-lookahead=8", "-g", "30", "motion/assets/base.mp4"], stdin=subprocess.PIPE)
NT = int(round(E["total"] * FPS)); log = []; n = 0
for i, s in enumerate(segs):
    # el plano i arranca en la pausa que lo precede (start - gap): las transiciones caen en la pausa y nunca asoma el plano anterior
    v = s["view"]; fa = 0 if i == 0 else int(round((s["start"] - s["gap"]) * FPS)); fb = NT if i == len(segs) - 1 else int(round((segs[i + 1]["start"] - segs[i + 1]["gap"]) * FPS))
    nf = fb - fa; src0 = v.get("src", s.get("a")) + (fa / FPS - s["start"])
    vf = "fps=30" + (f",lut3d=file={LUT}:interp=tetrahedral" if v.get("look") == "cam" else "," + SCR)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-threads", "2", "-ss", f"{src0:.4f}", "-i", SRC, "-t", f"{nf / FPS + 0.3:.4f}", "-vf", vf,
                          "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
    last = None; prev = None
    for j in range(nf):
        buf = p.stdout.read(W * H * 3)
        if len(buf) == W * H * 3: last = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
        fr = privacy(last.copy(), src0 + j / FPS)
        tr = (fa + j) / FPS - s["start"]; c = cam(v["keys"], tr)
        c1 = cam(v["keys"], tr + 1 / FPS)
        spd = abs(c1[0] - c[0]) * c[2] + abs(c1[1] - c[1]) * c[2] + abs(np.log(c1[2] / c[2])) * 900
        ns = 1 if spd < 7 else min(6, int(spd / 7) + 1)
        if ns == 1: o = cv2.warpAffine(fr, M_for(*c), (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
        else:
            acc = np.zeros((H, W, 3), np.float32)
            for q in range(ns):
                cq = cam(v["keys"], tr + q / (FPS * ns)); acc += cv2.warpAffine(fr, M_for(*cq), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            o = (acc / ns).astype(np.uint8)
        enc.stdin.write(o.tobytes()); n += 1
        log.append(dict(n=fa + j, seg=s["id"], src=round(src0 + j / FPS, 3), cam=[round(x, 3) for x in c]))
    p.stdout.close(); p.wait()
enc.stdin.close(); enc.wait(); json.dump(log, open("motion/assets/base_log.json", "w"), indent=0); print("cuadros", n, NT)
