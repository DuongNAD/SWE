#!/usr/bin/env bash
# Chạy thử một đề: P4 ba lượt độc lập -> P5 hợp nhất
set -uo pipefail; cd "$(dirname "$0")/.."
mkdir -p page/out logs
log(){ printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" | tee -a logs/thu_de.log; }
for i in 1 2 3; do
  [ -s "page/out/run$i.md" ] && { log "run$i đã có, bỏ qua"; continue; }
  log "P4 lượt $i…"
  agy -p "Đọc prompts/P4_lam_bai_khi_thi.md và làm đúng theo đó.
Đề nằm ở page/de.txt (đã OCR từ đề thi thật, có thể sai vài ký tự — đọc hiểu theo ngữ cảnh).
Ghi bài làm ra page/out/run$i.md
Chỉ đọc: page/de.txt, 04_templates/, 03_kb/playbook.md, 03_kb/rubric.md.
Làm đủ 4 giai đoạn. Chỗ nào đề không cho dữ kiện thì ghi THIẾU, đừng bịa." \
    --model gemini-3.1-pro-high --dangerously-skip-permissions --print-timeout 25m \
    > "logs/P4_run$i.log" 2>&1
  log "   run$i: $([ -s page/out/run$i.md ] && wc -c < page/out/run$i.md | tr -d ' ' || echo 0) byte"
done
log "P5 hợp nhất…"
agy -p "Đọc prompts/P5_hop_nhat_3_ban.md và làm đúng theo đó.
Input: page/out/run1.md, run2.md, run3.md, page/de.txt, 04_templates/, 03_kb/rubric.md
Output: page/out/FINAL.md
Đối chiếu TỪNG CÂU. Lệch nhỏ như thiếu một requirement hay khác một user story cũng phải ghi ra.
Mục '## CẦN NGƯỜI KIỂM TRA' ở cuối là phần quan trọng nhất." \
  --model gemini-3.1-pro-high --dangerously-skip-permissions --print-timeout 25m \
  > logs/P5.log 2>&1
log "XONG. page/out/FINAL.md $([ -s page/out/FINAL.md ] && wc -c < page/out/FINAL.md | tr -d ' ' || echo 'KHÔNG CÓ') byte"
