# FILE: composite_behind.py
# Uso: python composite_behind.py build/r_all.mp4 build/r_nob.mp4 build/r_mask.mp4 build/motion.mp4
# final = R_all donde no hay persona, R_nob donde la hay (la máscara con el
# mismo zoom). Se hace en RGB planar (gbrp): con la máscara en YUV, U/V valen
# 128 y el croma se mezclaría al 50 %.
import subprocess, sys

a, b, m, out = sys.argv[1:5]
counts = []
for f in (a, b, m):
    n = subprocess.check_output(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                                 "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", f]).decode().strip()
    counts.append(int(n))
print("fotogramas:", counts)
if len(set(counts)) != 1:
    sys.exit("ERROR: los tres renders deben tener el mismo número de fotogramas")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a, "-i", b, "-i", m,
                "-filter_complex",
                "[0:v]format=gbrp[x];[1:v]format=gbrp[y];[2:v]format=gray,format=gbrp[k];"
                "[x][y][k]maskedmerge,format=yuv420p[o]",
                "-map", "[o]", "-c:v", "libx264", "-crf", "14", "-preset", "medium", out], check=True)
print("->", out)
