# segmentos (tiempo del crudo, dentro de silencios medidos con silencedetect -40dB)
SEGS=[(67.28,70.50),(71.28,82.43),(83.00,84.31),(84.83,86.29),(87.05,92.64),(94.53,113.52)]
def o2t(t):  # tiempo crudo -> tiempo de salida
    acc=0
    for a,b in SEGS:
        if a<=t<=b: return acc+(t-a)
        acc+=b-a
    return None
TOTAL=sum(b-a for a,b in SEGS)
CUTS=[]; acc=0
for a,b in SEGS[:-1]:
    acc+=b-a; CUTS.append(acc)
if __name__=="__main__": print(TOTAL,CUTS)
