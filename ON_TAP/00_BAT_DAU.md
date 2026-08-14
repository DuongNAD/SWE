# Bắt đầu từ đây

Đề thi **6 câu, 10 điểm, trả lời bằng tiếng Anh**. Bạn không cần giỏi tiếng Anh —
cả bài chỉ dùng khoảng 6 mẫu câu, học đúng chỗ đó là đủ.

## Đọc theo thứ tự này

| Thứ tự | File | Mất bao lâu | Để làm gì |
|---|---|---|---|
| 1 | `TIENG_ANH.md` | 40 phút | Đọc hiểu đề + 6 mẫu câu + lỗi ngữ pháp hay mắc |
| 2 | `Q3_requirements.md` | 45 phút | 2.0đ — nền của câu 4, học trước |
| 3 | `Q4_user_story.md` | 30 phút | 1.5đ — suy thẳng ra từ câu 3 |
| 4 | `Q6_story_map.md` | 60 phút | **2.5đ, câu nặng nhất** |
| 5 | `Q1_mo_hinh_phat_trien.md` | 45 phút | 2.0đ |
| 6 | `Q2_kiem_thu.md` | 30 phút | 1.0đ — phần (b) học thuộc là xong |
| 7 | `Q5_design_pattern.md` | 30 phút | 1.0đ — cần hỏi giảng viên trước |

Thứ tự này theo **điểm số và mức phụ thuộc**, không theo số câu.
Câu 3 → 4 → 6 chiếm **6/10 điểm** và liên kết với nhau: requirement ở câu 3 biến
thành user story ở câu 4, rồi xếp vào release ở câu 6. Học đúng mạch này là được
quá nửa số điểm.

## Lúc thi

Mở `../page/DIEN_VAO_KHI_THI.txt`. Điền theo khung có sẵn, có gợi ý tiếng Việt ở
từng chỗ trống.

## Ba việc phải làm TRƯỚC ngày thi

1. **Hỏi giảng viên lớp bạn thi định dạng nào.** Có ba nguồn nói ba kiểu: 4 đề trong
   `../papers/` là 6 câu; giảng viên trong video nói đề thật 5 câu, đề thử 7 câu;
   tên video đánh số tới Q7. Toàn bộ tài liệu này dựng theo **định dạng 6 câu**.
   Nếu lớp bạn thi kiểu khác thì phải làm lại — xem `../BAN_GIAO.md` mục 3.
2. **Hỏi giảng viên lớp dạy design pattern nào.** Đề ghi rõ *"two design patterns
   discussed in the courses"* — phải đúng pattern đã học trên lớp. Tài liệu đang dùng
   Singleton, Observer, Factory là phỏng đoán an toàn, không phải chắc chắn.
3. **Làm thử một đề trong `../papers/`, bấm giờ 60 phút, không nhìn tài liệu.**
   Xong so với `../page/out/FINAL.md`.

## Ba mẹo ăn điểm nhanh nhất

**1. Đề trừ 0.1 điểm cho mỗi câu trả lời sai.** Hỏi 5 functional requirement thì
viết đúng 5. Viết 7 cho chắc là mất điểm, không phải được thêm.

**2. Phần (b) câu 2 gần như không đổi giữa các đề.** Ai làm unit test, ai làm
integration, ai làm system, ai làm acceptance — học thuộc nguyên khối trong
`Q2_kiem_thu.md` là ăn trọn 0.3 điểm mà không cần suy nghĩ.

**3. Không bao giờ viết `As a system, I want to…`** trong user story. Phải là vai trò
con người. Chức năng tự động thì viết `As a <người hưởng lợi>, I want **the system to**
<hành động>, so that <lợi ích>`. Đây là lỗi kinh điển người chấm nhận ra ngay.

## Khi có đề mới muốn AI làm thử

```bash
# dán đề vào page/de.txt trước, rồi:
bash scripts/98_thu_de.sh
```
Nó chạy 3 lượt độc lập rồi hợp nhất, xuất ra `page/out/FINAL.md` kèm mục
**`## CẦN NGƯỜI KIỂM TRA`** — danh sách những chỗ ba lượt làm khác nhau, tức là
chỗ AI đang đoán và bạn phải tự quyết. Đọc mục đó trước, đừng đọc bài làm trước.
