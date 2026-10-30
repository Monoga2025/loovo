# Cama musical generada por codigo (libre de derechos): pad suave Dm9 (D2 A2 D3 F3 A3 E4), lento, con ducking por voz.
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
sr=48000; v,_=sf.read("audio/voz.wav"); v=v if v.ndim==1 else v.mean(1)
T=len(v)/sr+0.8; n=int(T*sr); t=np.arange(n)/sr
rng=np.random.default_rng(7)
freqs=[73.42,110.0,146.83,174.61,220.0,329.63]; amps=[1.0,0.7,0.6,0.35,0.3,0.12]
out=np.zeros((n,2))
for k,(f,a) in enumerate(zip(freqs,amps)):
    for side,det in ((0,0.997),(1,1.003)):
        lfo=1+0.2*np.sin(2*np.pi*(0.07+0.013*k)*t+k)
        out[:,side]+=a*lfo*np.sin(2*np.pi*f*det*t+k)
# pulso suave de 60 bpm sobre el sub
out*= (0.85+0.15*np.sin(2*np.pi*1.0*t))[:,None]
sos=butter(4,1400,"low",fs=sr,output="sos"); out=sosfilt(sos,out,axis=0)
# envolvente de voz (10 ms) -> ganancia: -0 dB con voz, +7 dB en huecos
h=480; m=len(v)//h; e=20*np.log10(np.sqrt((v[:m*h].reshape(m,h)**2).mean(1))+1e-9)
act=(e>-45).astype(float)
act=np.convolve(act,np.ones(12)/12,"same")  # suaviza (~120 ms)
act=np.maximum.accumulate(act[::-1]*0+act[::-1])[::-1]*0+act  # sin cambio (marcador)
gdb=-0*act+(1-act)*7  # relativo
# suavizado lento (release 0.5s)
a=np.exp(-0.01/0.5); g=np.zeros(m); cur=0
for i in range(m):
    tgt=gdb[i]; cur=tgt+(cur-tgt)*(a if tgt<cur else np.exp(-0.01/0.15)); g[i]=cur
gs=np.interp(t,np.arange(m)*0.01,np.r_[g]) if True else 0
out*=(10**(gs/20))[:,None]
# fade in/out
fi=int(1.0*sr); fo=int(1.2*sr); out[:fi]*=np.linspace(0,1,fi)[:,None]; out[-fo:]*=np.linspace(1,0,fo)[:,None]
# normaliza a un nivel base (RMS) y fija -20 dB bajo la voz durante el habla
vr=np.sqrt((v[act[np.minimum((np.arange(len(v))//h),m-1)]>0.5]**2).mean())
sp=(act>0.9); idx=np.where(sp)[0]
mus_sp=np.concatenate([out[i*h:(i+1)*h,0] for i in idx[::1]])
r=np.sqrt((mus_sp**2).mean())
out*= (vr*10**(-20/20))/r
sf.write("audio/music.wav",out,sr,subtype="PCM_24")
print("voz rms",20*np.log10(vr),"musica rms habla",20*np.log10(np.sqrt((np.concatenate([out[i*h:(i+1)*h,0] for i in idx])**2).mean())))
