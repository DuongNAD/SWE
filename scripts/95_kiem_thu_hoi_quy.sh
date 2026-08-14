#!/usr/bin/env bash
# Kiểm thử hồi quy bộ khuôn trên toàn bộ đề trong papers/
#   bash scripts/95_kiem_thu_hoi_quy.sh
# Mỗi đề chạy P4 MỘT lượt (đủ để kiểm cấu trúc và số lượng),
# rồi chấm tự động theo đúng yêu cầu riêng của từng đề.
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)
mkdir -p page/out logs
log(){ printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" | tee -a logs/hoi_quy.log; }

for de in page/de_batch/de*.txt; do
  name=$(basename "$de" .txt)
  out="$ROOT/page/out/batch_$name.md"
  for try in 1 2; do
    [ -s "$out" ] && break
    log "$name: làm bài (lần $try)…"
    agy -p "Đọc $ROOT/prompts/P4_lam_bai_khi_thi.md và làm đúng theo đó.
Đề nằm ở $ROOT/$de (OCR từ đề thi thật, có thể sai vài ký tự — hiểu theo ngữ cảnh).
Khuôn làm bài ở $ROOT/04_templates/. Rubric ở $ROOT/03_kb/rubric.md.

GHI BÀI LÀM RA FILE: $out

Bắt buộc:
- Đúng số lượng đề yêu cầu ở câu 3 (đọc kỹ đề, mỗi đề một kiểu khác nhau).
- Câu 4 đúng 5 user story, KHÔNG được viết 'As a system' — vai trò phải là con người.
- Câu 5 đúng 2 design pattern.
- Câu 6 đúng định dạng A. Activities and User tasks / B. Releases của EOS.
- Câu 2 phải nói RÕ RÀNG type là white-box hay black-box ngay ở phần (a).
Phải thực sự ghi ra file, không chỉ in ra màn hình." \
      --add-dir "$ROOT" --model gemini-3.1-pro-high \
      --dangerously-skip-permissions --print-timeout 25m \
      > "logs/hoiquy_${name}_try${try}.log" 2>&1
    [ -s "$out" ] && log "   OK $(wc -c < "$out" | tr -d ' ') byte" || log "   hỏng lần $try"
  done
done
log "XONG"
