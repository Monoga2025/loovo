"""Offset local t_PC = t_cel + off en varios instantes. Uso: local_off.py CEL PC expected t1 t2 ..."""
import sys; sys.path.insert(0, __file__.rsplit("\\",1)[0].rsplit("/",1)[0])
from sync_audio import offset_at, refine48
cel, pc, exp = sys.argv[1], sys.argv[2], float(sys.argv[3])
for t in map(float, sys.argv[4:]):
    o, q = offset_at(cel, pc, t, exp, 20, 1.0)
    o2 = refine48(cel, pc, t-8, 16, o)
    print(f"t={t:.1f} off={o2:.4f} q={q:.1f}")
