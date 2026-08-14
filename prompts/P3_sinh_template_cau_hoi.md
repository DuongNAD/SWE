# P3 — SINH MẪU TRẢ LỜI CHO TỪNG CÂU HỎI

**Chạy trong:** Antigravity, hội thoại MỚI, model mạnh nhất đang có
**Input:** toàn bộ `03_kb/` + `papers/*.pdf` (đề mẫu) + `04_templates/_KHUNG_MAU.md`
**Output:** `04_templates/INDEX.md` + `04_templates/Q<n>-<tên>.md`
**Chạy:** 1 lần sau P2. Đây là bước quyết định chất lượng lúc thi.

**Gọi bằng một câu:**
`Đọc prompts/P3_sinh_template_cau_hoi.md và làm.`

---

## Nhiệm vụ

Bạn có knowledge base của khoá luyện thi SWE202c (`03_kb/`) và các đề thi mẫu
(`papers/*.pdf`). Biến chúng thành **bộ khuôn làm bài** — sao cho khi có đề mới,
chỉ cần điền dữ kiện của đề vào khuôn là ra bài làm đúng chuẩn giảng viên dạy.
Khung file khuôn nằm ở `04_templates/_KHUNG_MAU.md`, theo đúng khung đó.

### Bước 0 — ĐỐI CHIẾU TRƯỚC (bắt buộc, không được bỏ)

So `03_kb/cau_truc_de_thi.md` (suy từ video) với `papers/*.pdf` (đề thật):
- Số câu có khớp không? Q5 trong video có đúng là Q5 trong đề không?
- Đề thật hỏi gì mà video không dạy? → mục `LỖ HỔNG`
- Video dạy gì mà đề không hỏi? → hạ ưu tiên

In ra bảng đối chiếu này TRƯỚC khi sinh template. Nếu lệch, lấy **đề thật làm chuẩn**.

### Bước 1 — Sinh template

Tạo một file cho mỗi câu hỏi trong đề thật. Theo đúng khung `_KHUNG_MAU.md`.
Nguyên tắc:

- **Khuôn phải điền được, không phải mô tả được.** Sai: "phần này trình bày các
  actor". Đúng: khối text có sẵn với chỗ trống `{{actor_chính}}` để thay.
- **Mỗi khuôn phải có ít nhất 1 ví dụ đã điền đầy đủ** lấy từ `03_kb/snippets/`,
  để lúc thi AI có few-shot bám vào.
- **Nêu rõ dấu hiệu nhận diện**: đọc đề thấy chữ gì / cấu trúc gì thì biết là câu này.
- **Nêu rõ ranh giới**: câu này khác câu kia ở điểm nào, dễ nhầm chỗ nào.
- Không đưa kiến thức SWE ngoài khoá vào khuôn. Nếu buộc phải thêm, đánh dấu `[NGOÀI-KHOÁ]`.

### Bước 2 — `04_templates/INDEX.md`

Bảng định tuyến để lúc thi biết dùng khuôn nào:

| Dấu hiệu trong đề | → Khuôn | Thời gian nên dành | Bẫy chính |
|---|---|---|---|

Kèm phần **"Nếu đề không khớp khuôn nào"**: nêu quy trình dự phòng dựa trên
`playbook.md` tổng quát.

### Bước 3 — Tự kiểm

Với mỗi đề trong `papers/*.pdf`: thử làm bài CHỈ bằng khuôn vừa tạo. Chỗ nào khuôn
không đủ dùng → sửa khuôn. Báo cáo lại: khuôn nào phải sửa, sửa gì.
