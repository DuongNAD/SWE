#!/usr/bin/env bash
# Pha A1 — Chuẩn bị media LOCAL, không tốn quota AI.
# Chạy: bash scripts/01_prep_media.sh          (tất cả video trong scripts/videos.tsv)
#       bash scripts/01_prep_media.sh b5 b7    (chỉ vài video)
#       FRAME_INTERVAL=10 bash scripts/01_prep_media.sh   (lấy mẫu thưa hơn cho nhanh)
#
# Với mỗi video sinh ra:
#   01_raw/<id>/audio.m4a      : audio mono 16kHz 48kbps
#   01_raw/<id>/frames/NNNN.jpg: 1 ảnh mỗi FRAME_INTERVAL giây, giữ 720p gốc
#                                 -> timestamp(giây) = (NNNN - 1) * FRAME_INTERVAL
#   01_raw/<id>/scenes/*.jpg   : ảnh tại điểm chuyển cảnh (slide đổi, IDE đổi)
#   01_raw/<id>/scenes/times.txt: mốc thời gian của từng ảnh scene
#   01_raw/<id>/info.txt       : thời lượng + map id -> tên file gốc
#
# Chạy lại an toàn: phần nào đã có thì bỏ qua.

set -euo pipefail
cd "$(dirname "$0")/.."

# Khoảng lấy mẫu khung hình. 5 giây = dày, bắt được cả nội dung thoáng qua.
# Giá trị này phải khớp với lúc chạy OCR (scripts/01c_ocr.sh đọc cùng biến).
FRAME_INTERVAL="${FRAME_INTERVAL:-5}"
export FRAME_INTERVAL
echo "FRAME_INTERVAL = ${FRAME_INTERVAL}s"

want=" $* "   # rỗng = làm tất cả
failed=""     # video lỗi được ghi lại, không làm chết cả lượt chạy

while IFS=$'\t' read -r id src; do
  case "$id" in ''|\#*) continue ;; esac
  [[ $# -gt 0 && $want != *" $id "* ]] && continue
  if [[ ! -f "$src" ]]; then echo "!! thiếu file: $src"; continue; fi

  out="01_raw/$id"
  mkdir -p "$out/frames" "$out/scenes"

  # Đổi FRAME_INTERVAL thì phải cắt lại ảnh, nếu không timestamp sẽ lệch hết.
  old_fi=""
  [[ -f "$out/info.txt" ]] && old_fi=$(sed -n 's/^frame_interval=//p' "$out/info.txt" | head -1)
  if [[ -n $old_fi && $old_fi != "$FRAME_INTERVAL" ]]; then
    echo "    FRAME_INTERVAL đổi ${old_fi}s -> ${FRAME_INTERVAL}s, cắt lại ảnh"
    rm -rf "$out/frames" "$out/ocr_frames.txt"; mkdir -p "$out/frames"
  fi

  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$src")
  printf 'id=%s\nfile=%s\nduration_sec=%.0f\nframe_interval=%s\n' \
    "$id" "$src" "$dur" "$FRAME_INTERVAL" > "$out/info.txt"
  echo "==> $id  ($(printf '%.1f' "$(echo "$dur/60" | bc -l)") phút)"

  # 1) Audio: mono 16k, đủ nghe rõ giọng, file nhỏ
  if [[ ! -f "$out/audio.m4a" ]]; then
    if ! ffmpeg -nostdin -v error -y -i "$src" -vn -ac 1 -ar 16000 -c:a aac -b:a 48k "$out/audio.m4a"; then
      echo "!! $id: lỗi tách audio, bỏ qua video này"; failed="$failed $id"; continue
    fi
  fi

  # 2) Keyframe đều đặn -> timestamp suy ra được từ tên file.
  #    Giữ nguyên độ phân giải gốc để OCR đọc được chữ nhỏ trong IDE.
  if [[ -z "$(ls -A "$out/frames" 2>/dev/null)" ]]; then
    if ! ffmpeg -nostdin -v error -y -i "$src" -vf "fps=1/${FRAME_INTERVAL}" \
           -pix_fmt yuvj420p -q:v 2 "$out/frames/%04d.jpg"; then
      echo "!! $id: lỗi cắt ảnh, bỏ qua video này"; failed="$failed $id"; continue
    fi
  fi

  # 3) Ảnh tại điểm chuyển cảnh -> bắt được slide/sơ đồ xuất hiện giữa 2 mốc.
  #    times.txt ghi pts_time của từng ảnh để OCR biết mốc thời gian.
  #
  #    -pix_fmt yuvj420p là bắt buộc: nếu không có, video quay màn hình đổi chậm
  #    (không cảnh nào vượt ngưỡng) sẽ làm ffmpeg khởi tạo encoder mjpeg với
  #    yuv420p dải hẹp rồi chết với thông báo "Error while opening encoder" —
  #    nghe như lỗi tham số nhưng thật ra chỉ là "không chọn được khung nào".
  #
  #    Video screencast gõ phím liên tục không có cảnh cắt rõ, phải hạ ngưỡng.
  if [[ ! -f "$out/scenes/times.txt" ]]; then
    for thr in "${SCENE_THRESHOLD:-0.25}" 0.08 0.03; do
      ffmpeg -nostdin -v error -y -i "$src" \
        -vf "select='gt(scene,${thr})',metadata=print:file=$out/scenes/times.txt" \
        -vsync vfr -pix_fmt yuvj420p -q:v 2 "$out/scenes/s%04d.jpg" || true
      # find chứ không phải ls: ls không khớp file nào sẽ trả mã lỗi,
      # gặp `set -o pipefail` là chết cả script.
      n=$(find "$out/scenes" -name '*.jpg' | wc -l | tr -d ' ')
      [[ $n -ge 10 ]] && break
      echo "    ngưỡng $thr chỉ ra $n ảnh chuyển cảnh, hạ ngưỡng thử lại"
    done
  fi

  printf '    frames=%s  scenes=%s  audio=%s\n' \
    "$(find "$out/frames" -name '*.jpg' | wc -l | tr -d ' ')" \
    "$(find "$out/scenes" -name '*.jpg' | wc -l | tr -d ' ')" \
    "$(du -h "$out/audio.m4a" | cut -f1)"
done < scripts/videos.tsv

echo
echo "Xong Pha A1. Dung lượng 01_raw: $(du -sh 01_raw | cut -f1)"
[[ -n $failed ]] && echo "!! CÁC VIDEO LỖI, cần xem lại:$failed"
exit 0
