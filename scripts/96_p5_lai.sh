#!/usr/bin/env bash
set -uo pipefail; cd "$(dirname "$0")/.."
log(){ printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" | tee -a logs/p5_lai.log; }
for try in 1 2 3 4; do
  [ -s page/out/FINAL.md ] && { log "FINAL.md đã có"; break; }
  log "P5 lần $try…"
  agy -p "Đọc prompts/P5_hop_nhat_3_ban.md và làm đúng theo đó.
Input: page/out/run1.md, page/out/run2.md, page/out/run3.md, page/de.txt,
04_templates/, 03_kb/rubric.md
Output: GHI RA FILE page/out/FINAL.md — bắt buộc phải ghi ra file, không chỉ in ra màn hình.

Đối chiếu TỪNG CÂU trong 6 câu. Phân loại mỗi điểm khác biệt thành
ĐỒNG THUẬN / ĐA SỐ / BẤT ĐỒNG. Lệch nhỏ như thiếu một requirement, khác một
user story, hay khác cách chia activity cũng phải ghi ra.

FINAL.md gồm 2 phần:
1. Bài làm cuối cùng bằng TIẾNG ANH, sạch, sẵn sàng nộp, đúng số lượng đề yêu cầu
   (5 functional + 3 security + 2 scalability ở câu 3; đúng 5 user story ở câu 4;
   đúng 2 design pattern ở câu 5; câu 6 đúng định dạng A/B của EOS).
2. Mục '## CẦN NGƯỜI KIỂM TRA' — mọi chỗ BẤT ĐỒNG, THIẾU, [NGOÀI KHUÔN],
   mỗi mục một dòng kèm câu hỏi cụ thể." \
    --model gemini-3.1-pro-high --dangerously-skip-permissions --print-timeout 25m \
    > "logs/P5_try$try.log" 2>&1
  [ -s page/out/FINAL.md ] && { log "OK: $(wc -c < page/out/FINAL.md | tr -d ' ') byte"; break; }
  log "   hỏng: $(tail -1 logs/P5_try$try.log | cut -c1-80)"; sleep 30
done
