import sys, subprocess, numpy as np, cv2
SRC="C:/Users/Monoga/Desktop/VID_20261013_110529.mp4"
out=sys.argv[1]; a,b,st=map(float,sys.argv[2:5])
ts=np.arange(a,b,st); ims=[]
for t in ts:
    raw=subprocess.run(["ffmpeg","-v","error","-ss",f"{t:.2f}","-i",SRC,"-frames:v","1","-vf","scale=216:384","-f","rawvideo","-pix_fmt","bgr24","-"],capture_output=True).stdout
    im=np.frombuffer(raw,np.uint8).reshape(384,216,3).copy() if len(raw)==216*384*3 else np.zeros((384,216,3),np.uint8)
    cv2.putText(im,f"{t:.0f}",(4,22),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2); ims.append(im)
C=10
while len(ims)%C: ims.append(np.zeros_like(ims[0]))
rows=[np.hstack(ims[i:i+C]) for i in range(0,len(ims),C)]
cv2.imwrite(out,np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,80]); print(out,len(ts))
