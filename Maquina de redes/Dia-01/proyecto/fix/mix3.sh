#!/bin/bash
set -e
cd "$(dirname "$0")"
MUS="$1"; OUT="$2"; TAIL="${3:-2.0}"
TOTAL=$(python -c "print(38.058583+$TAIL)")
ffmpeg -hide_banner -loglevel error -y -i voice_clean48.wav -i "$MUS" -i ../audio/sfx.wav -filter_complex "[0:a]aformat=sample_rates=48000:channel_layouts=stereo,apad=whole_dur=$TOTAL[v];[1:a]aformat=sample_rates=48000:channel_layouts=stereo,equalizer=f=300:t=q:w=1:g=-3,equalizer=f=1500:t=q:w=0.8:g=-4[m];[2:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-8dB,apad=whole_dur=$TOTAL[s];[v][m][s]amix=inputs=3:normalize=0:duration=first[o]" -map "[o]" -c:a pcm_s16le mix_$OUT.wav
P1=$(ffmpeg -hide_banner -nostats -i mix_$OUT.wav -af loudnorm=I=-14:TP=-2:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$P1" | grep "\"$1\"" | sed -E 's/.*: *"([^"]+)".*/\1/'; }
ffmpeg -hide_banner -loglevel error -y -i mix_$OUT.wav -af "loudnorm=I=-14:TP=-2:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,alimiter=limit=0.708:level=disabled,afade=t=out:st=$(python -c "print($TOTAL-0.9)"):d=0.9" -ar 48000 -c:a pcm_s16le final_audio_$OUT.wav
VF="tpad=stop_mode=clone:stop_duration=$TAIL,fade=t=out:st=$(python -c "print(38.033333+0.2)"):d=$(python -c "print($TAIL-0.2)")"
ffmpeg -hide_banner -loglevel error -y -i ../out/final_tiktok.mp4 -i final_audio_$OUT.wav -vf "$VF" -map 0:v -map 1:a -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart -shortest ../out/final_tiktok_$OUT.mp4
ffmpeg -hide_banner -loglevel error -y -i ../out/final_reels.mp4 -i final_audio_$OUT.wav -vf "$VF" -map 0:v -map 1:a -c:v libx264 -profile:v high -level 4.2 -b:v 4500k -maxrate 5000k -bufsize 10000k -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart -shortest ../out/final_reels_$OUT.mp4
for p in tiktok reels; do echo -n "$p $OUT: "; ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of compact ../out/final_${p}_$OUT.mp4 | tr '\n' ' '; echo; ffmpeg -hide_banner -nostats -i ../out/final_${p}_$OUT.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | tr -s ' ' | tr '\n' ' '; echo; done
