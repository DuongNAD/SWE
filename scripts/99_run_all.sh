#!/usr/bin/env bash
# Chạy nốt toàn bộ pipeline không cần người ngồi canh.
#   bash scripts/99_run_all.sh
#
# Việc AI do `agy` (Antigravity CLI) làm, dùng quota Antigravity chứ không phải
# token của phiên chat. Mọi bước đều bỏ qua nếu đã có kết quả -> chạy lại an toàn.
#
# Log từng bước: logs/<bước>.log   |   Tổng kết cuối: BAN_GIAO.md

set -uo pipefail
cd "$(dirname "$0")/.."
mkdir -p logs 02_extract 03_kb 04_templates

M_FAST=gemini-3.6-flash-high
M_PRO=gemini-3.1-pro-high
VIDEOS=$(awk -F'\t' '!/^#/ && NF==2 {print $1}' scripts/videos.tsv)
CO_SODO="ucd1 b5 b7 b3-2 b3-3 b4"

log(){ printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" | tee -a logs/run_all.log; }

# Gọi agy, thử lại 1 lần nếu hỏng. $1=tên log $2=model $3=prompt
ask(){
  local name=$1 model=$2 prompt=$3 try
  for try in 1 2; do
    if agy -p "$prompt" --model "$model" --dangerously-skip-permissions \
         --print-timeout 25m > "logs/$name.log" 2>&1; then return 0; fi
    log "   ! $name hỏng lần $try"; sleep 10
  done
  return 1
}

# ---------------------------------------------------------------- PHA 0: chờ
log "PHA 0 — chờ Whisper và OCR xong"
while :; do
  w=$(find 01_raw -name transcript.srt | wc -l | tr -d ' ')
  o=$(find 01_raw -name ocr_frames.txt -size +1k | wc -l | tr -d ' ')
  [ "$w" -ge 12 ] && [ "$o" -ge 12 ] && break
  log "   whisper $w/12 · ocr $o/12 — chờ tiếp"
  sleep 120
done
log "   xong: whisper 12/12, ocr 12/12"

# ------------------------------------------------------- PHA 1: dossier + ảnh
log "PHA 1 — dựng dossier và lọc ảnh sơ đồ"
python3 scripts/02_build_dossier.py >> logs/dossier.log 2>&1
for v in $CO_SODO; do
  python3 scripts/03_frames_for_attach.py "$v" --max 40 >> logs/dossier.log 2>&1
done
log "   $(find 01_raw -name dossier.md | wc -l | tr -d ' ')/12 dossier"

# ------------------------------------------------------------- PHA 2: P1 × 12
log "PHA 2 — trích xuất từng video (P1)"
for v in $VIDEOS; do
  out="02_extract/$v.json"
  if [ -s "$out" ] && jq -e . "$out" >/dev/null 2>&1; then log "   $v: đã có, bỏ qua"; continue; fi
  log "   $v: đang trích xuất…"
  ask "P1_$v" "$M_FAST" "Đọc file prompts/P1_trich_xuat_video.md và làm đúng theo đó cho video id = $v.
Input: 01_raw/$v/dossier.md — đọc TOÀN BỘ file từ đầu đến cuối, không đọc lướt, không bỏ phần giữa.
Output: ghi ra $out
Tuyệt đối không mở file .mp4. Xong in một dòng tóm tắt số liệu, không in lại JSON."

  # Cổng chất lượng: quá mỏng thì làm lại bằng model mạnh hơn
  steps=$(jq '.quy_trinh_lam_bai | length' "$out" 2>/dev/null || echo 0)
  vidu=$(jq '.vi_du_giang_vien_lam | length' "$out" 2>/dev/null || echo 0)
  if [ "$steps" -lt 3 ] || [ "$vidu" -lt 1 ]; then
    log "   $v: mỏng ($steps bước, $vidu ví dụ) -> làm lại bằng $M_PRO"
    mv -f "$out" "$out.mong" 2>/dev/null
    ask "P1_${v}_pro" "$M_PRO" "Đọc prompts/P1_trich_xuat_video.md và làm cho video id = $v.
Bản trích xuất trước quá sơ sài. Lần này đọc kỹ TOÀN BỘ 01_raw/$v/dossier.md,
lấy đủ mọi bước trong quy trình và chép NGUYÊN VĂN mọi bảng/sơ đồ/bài mẫu.
Ghi ra $out. Không mở .mp4."
  fi
  jq -e . "$out" >/dev/null 2>&1 \
    && log "   $v: OK ($(jq '.quy_trinh_lam_bai|length' "$out") bước, $(jq '.vi_du_giang_vien_lam|length' "$out") ví dụ)" \
    || log "   $v: THẤT BẠI"
done

# ------------------------------------------------------------ PHA 3: P1b × N
log "PHA 3 — đọc cấu trúc sơ đồ từ ảnh (P1b)"
for v in $CO_SODO; do
  out="02_extract/${v}_sodo.json"
  [ -s "$out" ] && { log "   $v: đã có, bỏ qua"; continue; }
  n=$(find "01_raw/$v/attach" -name '*.jpg' 2>/dev/null | wc -l | tr -d ' ')
  [ "$n" -eq 0 ] && { log "   $v: không có ảnh, bỏ qua"; continue; }
  log "   $v: đọc $n ảnh sơ đồ…"
  ask "P1b_$v" "$M_PRO" "Đọc prompts/P1b_doc_so_do.md và làm đúng theo đó cho video id = $v.
Các ảnh sơ đồ nằm trong thư mục 01_raw/$v/attach/ (có $n file .jpg).
MỞ VÀ NHÌN TỪNG ẢNH MỘT. Tên file chính là mốc thời gian: 12m30s.jpg = phút 12 giây 30.
Việc quan trọng nhất là lấy QUAN HỆ giữa các phần tử (nối từ đâu tới đâu, hướng mũi tên,
loại quan hệ, multiplicity) — thứ mà OCR đã làm mất. Mỗi sơ đồ xuất kèm mã PlantUML.
Ghi ra $out"
  [ -s "$out" ] && log "   $v: OK" || log "   $v: THẤT BẠI"
done

# ---------------------------------------------------------------- PHA 4: P2
log "PHA 4 — gộp knowledge base (P2)"
if [ -s 03_kb/playbook.md ]; then log "   đã có, bỏ qua"; else
  ask P2 "$M_PRO" "Đọc prompts/P2_gop_knowledge_base.md và làm đúng theo đó.
Input: toàn bộ 02_extract/*.json (gồm cả các file _sodo.json) và manifest.md.
Tạo đủ 6 sản phẩm trong 03_kb/ như prompt mô tả.
Đừng bỏ bước kiểm chứng cuối: lấy ngẫu nhiên 15 khẳng định, mở lại dossier đúng
timestamp, khẳng định nào không tìm thấy thì xoá hoặc hạ xuống [SUY-LUẬN]."
  log "   $(ls 03_kb/*.md 2>/dev/null | wc -l | tr -d ' ') file trong 03_kb/"
fi

# ---------------------------------------------------------------- PHA 5: P3
log "PHA 5 — sinh khuôn làm bài (P3)"
if [ -s 04_templates/INDEX.md ]; then log "   đã có, bỏ qua"; else
  ask P3 "$M_PRO" "Đọc prompts/P3_sinh_template_cau_hoi.md và làm đúng theo đó.
Input: toàn bộ 03_kb/, các đề mẫu papers/*.pdf, và khung 04_templates/_KHUNG_MAU.md.
Làm Bước 0 TRƯỚC và in kết quả: đối chiếu cấu trúc đề suy từ video với đề thật
trong papers/*.pdf. Lệch chỗ nào thì LẤY ĐỀ THẬT LÀM CHUẨN.
Lưu ý: trong video giảng viên có nói đề thi thật khác đề thi thử về số câu —
phải xác minh bằng papers/*.pdf, đừng tin bảng phỏng đoán trong manifest.md.
Tạo 04_templates/INDEX.md và một file Q<n>-<tên>.md cho mỗi câu trong đề thật."
  log "   $(ls 04_templates/Q*.md 2>/dev/null | wc -l | tr -d ' ') khuôn"
fi

# ------------------------------------------------------------ PHA 6: bàn giao
log "PHA 6 — viết báo cáo bàn giao"
ask BANGIAO "$M_PRO" "Viết file BAN_GIAO.md ở thư mục gốc, tiếng Việt, cho người vừa đi vắng về.
Đọc: 03_kb/cau_truc_de_thi.md, 04_templates/INDEX.md, toàn bộ 04_templates/Q*.md,
và đếm số liệu trong 02_extract/*.json.

Nội dung cần có, ngắn gọn, không dài dòng:
1. Bảng: mỗi câu Q trong đề thật — tên câu, thang điểm, đã có khuôn chưa, độ tin cậy.
2. Kết quả đối chiếu với papers/*.pdf: cấu trúc đề thật là gì, khác gì so với phỏng đoán ban đầu.
3. Những chỗ CÒN THIẾU hoặc CHƯA CHẮC — cần người tự kiểm tra. Đây là phần quan trọng nhất.
4. Cách dùng khi có đề: dán đề vào page/de.txt rồi chạy prompts/P4 ba lượt, sau đó P5.
5. Việc nên làm tiếp nếu có thời gian.
Không tô hồng. Chỗ nào hệ thống làm chưa tốt thì nói thẳng."

log "HOÀN TẤT. Xem BAN_GIAO.md"
