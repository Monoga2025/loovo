#!/bin/bash
set -e
cd "$(dirname "$0")"
MV="${1:-0.2}"
OUT="${2:-v3}"
ffmpeg -hide_banner -loglevel error -y -i ../audio/music.wav -i voice_clean48.wav -filter_complex "[0:a]aresample=48000[mu];[1:a]aresample=48000[vo];[mu][vo]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=400:makeup=1,volume=${MV}dB[m]" -map "[m]" -ar 48000 -c:a pcm_s16le music_$OUT.wav
ffmpeg -hide_banner -loglevel error -y -i voice_clean48.wav -i music_$OUT.wav -i ../audio/sfx.wav -filter_complex "[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];[1:a]aformat=sample_rates=48000:channel_layouts=stereo[m];[2:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=-8dB[s];[v][m][s]amix=inputs=3:normalize=0:duration=longest[o]" -map "[o]" -c:a pcm_s16le mix_$OUT.wav
P1=$(ffmpeg -hide_banner -nostats -i mix_$OUT.wav -af loudnorm=I=-14:TP=-2:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$P1" | grep "\"$1\"" | sed -E 's/.*: *"([^"]+)".*/\1/'; }
ffmpeg -hide_banner -loglevel error -y -i mix_$OUT.wav -af "loudnorm=I=-14:TP=-2:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,alimiter=limit=0.708:level=disabled" -ar 48000 -c:a pcm_s16le final_audio_$OUT.wav
for p in tiktok reels; do
  ffmpeg -hide_banner -loglevel error -y -i ../out/final_$p.mp4 -i final_audio_$OUT.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 128k -movflags +faststart -shortest ../out/final_${p}_$OUT.mp4
done
echo -n "musica: "; ffmpeg -hide_banner -nostats -i music_$OUT.wav -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tr -s ' '
echo -n "voz: "; ffmpeg -hide_banner -nostats -i voice_clean48.wav -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tr -s ' '
for p in tiktok reels; do echo -n "$p $OUT: "; ffmpeg -hide_banner -nostats -i ../out/final_${p}_$OUT.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | tr -s ' ' | tr '\n' ' '; echo; done
