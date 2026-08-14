#!/usr/bin/env bash
# Sinh bộ tài liệu ôn tập trong ON_TAP/
#
# BÀI HỌC: luôn truyền --add-dir <đường dẫn tuyệt đối dự án> cho agy, và dùng
# đường dẫn TUYỆT ĐỐI cho file output. Không có nó, agy ghi vào thư mục nháp
# riêng (~/.gemini/antigravity-cli/scratch/) rồi vẫn báo "đã tạo thành công".
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)
mkdir -p ON_TAP logs
log(){ printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" | tee -a logs/on_tap.log; }

CAUHOI='1|Q1_mo_hinh_phat_trien|Software development models: Waterfall, Agile, Scrum, Kanban, XP|2.0
2|Q2_kiem_thu|Testing: type (white-box/black-box) va level (unit, integration, system, acceptance)|1.0
3|Q3_requirements|Functional vs non-functional requirements: security, performance, usability, scalability|2.0
4|Q4_user_story|User story, cong thuc As a / I want / So that|1.5
5|Q5_design_pattern|Design patterns: Singleton, Observer, Factory, Strategy, MVC|1.0
6|Q6_story_map|Story map: activities, user tasks, releases theo dinh dang EOS|2.5'

echo "$CAUHOI" | while IFS='|' read -r num file chude diem; do
  out="$ROOT/ON_TAP/${file}.md"
  for try in 1 2; do
    [ -s "$out" ] && break
    log "$file: lần $try…"
    agy -p "NHIỆM VỤ: dùng công cụ ghi file để TẠO FILE tại đúng đường dẫn tuyệt đối:
$out

Trước khi viết, hãy ĐỌC các file nguồn sau trong dự án $ROOT :
- $ROOT/03_kb/playbook.md
- $ROOT/03_kb/glossary.md
- $ROOT/03_kb/rubric.md
- $ROOT/04_templates/Q${num}-*.md
- $ROOT/page/de.txt   (đề thi thật)
- $ROOT/page/out/FINAL.md  (bài làm mẫu đã hợp nhất)

NỘI DUNG FILE: tài liệu ÔN TẬP cho Question $num của đề thi SWE202c —
$chude — $diem điểm.

NGƯỜI ĐỌC: sinh viên Việt Nam **yếu tiếng Anh**, cần hiểu bản chất bằng tiếng Việt
rồi mới viết được đáp án tiếng Anh. Đừng giả định họ đã biết khái niệm.

CẤU TRÚC BẮT BUỘC, viết bằng TIẾNG VIỆT (trừ thuật ngữ và câu mẫu tiếng Anh):

# Question $num — <tên> ($diem điểm)

## 1. Đề sẽ hỏi thế nào
Trích nguyên văn tiếng Anh từ page/de.txt, kèm bản dịch tiếng Việt ngay bên dưới.

## 2. Hiểu bản chất
Giải thích khái niệm từ số 0 bằng tiếng Việt, dùng ví dụ đời thường dễ hình dung
(ví dụ: giải thích Kanban bằng bảng công việc trong quán ăn). Đây là phần dài nhất,
viết cho người chưa biết gì. Không chép định nghĩa sách vở khô khan.

## 3. So sánh / phân loại
Bảng các khái niệm dễ nhầm: cột thuật ngữ tiếng Anh + cột nghĩa tiếng Việt + cột
dấu hiệu nhận ra trong đề.

## 4. Cách làm bài, từng bước
Đánh số bước. Mỗi bước nói rõ: đọc gì trong đề → viết ra cái gì.

## 5. Câu mẫu tiếng Anh
Bảng 3 cột: mẫu câu tiếng Anh | nghĩa tiếng Việt | dùng khi nào.

## 6. Ví dụ đầy đủ
Một đề nhỏ + bài làm hoàn chỉnh bằng tiếng Anh, kèm chú thích tiếng Việt giải thích
vì sao viết như vậy.

## 7. Bẫy hay mất điểm
Bảng: lỗi | hậu quả | cách tránh.

## 8. Tự kiểm tra
3-5 câu hỏi cho người học tự trả lời, đáp án để ở cuối file.

QUY TẮC: kiến thức có trong khoá học thì ưu tiên và ghi nguồn dạng (b5 @ 12:30).
Kiến thức phải bổ sung từ ngoài thì đánh dấu [NGOÀI-KHOÁ]. Không bịa. Chỗ nào không
chắc thì ghi 'cần xác minh với giảng viên'. Viết thẳng, không sáo rỗng.

QUAN TRỌNG: phải thực sự GHI RA FILE, không chỉ mô tả nội dung trong câu trả lời." \
      --add-dir "$ROOT" \
      --model gemini-3.1-pro-high --dangerously-skip-permissions --print-timeout 25m \
      > "logs/ontap_${file}_try${try}.log" 2>&1
    if [ -s "$out" ]; then
      log "   OK $(wc -c < "$out" | tr -d ' ') byte"
    else
      log "   hỏng lần $try"; sleep 15
    fi
  done
done

log "XONG. ON_TAP/: $(ls ON_TAP/*.md 2>/dev/null | wc -l | tr -d ' ') file"
ls -la ON_TAP/*.md 2>/dev/null | awk '{printf "   %7s byte  %s\n", $5, $NF}' | tee -a logs/on_tap.log
