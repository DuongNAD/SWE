#!/usr/bin/env bash
# Pha A-phụ — Cắt video dài thành lát 12 phút, chồng lấn 45 giây.
# CHỈ dùng khi bạn upload video vào giao diện web (AI Studio / Gemini app)
# và không set được start_offset/end_offset qua API.
#
# Chạy:  bash scripts/02_chunk_video.sh b5
#        bash scripts/02_chunk_video.sh ucd1 10   # lát 10 phút
#
# Vì sao chồng lấn 45s: giảng viên hay nói vắt qua ranh giới lát cắt.
# Không chồng lấn = mất nguyên một ý ngay chỗ nối.

set -euo pipefail
cd "$(dirname "$0")/.."

id="${1:?Thiếu id video, vd: b5}"
chunk_min="${2:-12}"
overlap=45

src=$(grep '^file=' "01_raw/$id/info.txt" | cut -d= -f2-)
dur=$(grep '^duration_sec=' "01_raw/$id/info.txt" | cut -d= -f2)
step=$(( chunk_min * 60 ))
out="01_raw/$id/chunks"; mkdir -p "$out"

i=0; start=0
while (( start < dur )); do
  i=$((i+1))
  end=$(( start + step + overlap ))
  (( end > dur )) && end=$dur
  printf -v name "%s/%s_p%02d_%dm-%dm.mp4" "$out" "$id" "$i" $((start/60)) $((end/60))
  echo "  lát $i: $((start/60))m -> $((end/60))m"
  ffmpeg -nostdin -v error -y -ss "$start" -to "$end" -i "$src" \
         -c:v libx264 -crf 30 -preset veryfast -vf "scale=1280:-2" \
         -c:a aac -b:a 48k -ac 1 "$name"
  start=$(( start + step ))
done
echo "Xong: $i lát trong $out"
