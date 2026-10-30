import sys, re, subprocess, numpy as np, soundfile as sf
def meas(p):
    x,sr=sf.read(p); x=x.mean(1) if x.ndim>1 else x
    n=int(0.1*sr); m=len(x)//n
    r=20*np.log10(np.sqrt((x[:m*n].reshape(m,n)**2).mean(1))+1e-9)
    sp=r[r>-36]
    r2=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",p,"-af","ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
    I=re.findall(r"I:\s+(-?[\d.]+) LUFS",r2)[-1]; tp=re.findall(r"Peak:\s+(-?[\d.]+) dBFS",r2)[-1]
    return dict(floor_p5=round(float(np.percentile(r,5)),2),speech=round(float(20*np.log10(np.sqrt(np.mean(10**(sp/10))))),2),n_speech=len(sp),n=len(r),LUFS=I,TP=tp)
for p in sys.argv[1:]: print(p,meas(p))
