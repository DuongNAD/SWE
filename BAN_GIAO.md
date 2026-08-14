# BÀN GIAO — hệ thống luyện đề SWE202c

Pipeline đã chạy xong toàn bộ. Nhưng **có một phát hiện bạn phải đọc trước khi dùng bất cứ thứ gì**.

---

## ⚠️ 1. Khoá học bạn mua KHÔNG khớp với 4 đề trong `papers/`

Tôi đã OCR trực tiếp cả 4 file `papers/*.pdf`. Chúng nhất quán tuyệt đối với nhau:
đề thi thực hành trên EOS, **6 câu, tổng 10 điểm**, case study về hệ thống quản lý
phòng khám (MedCare) hoặc bán hàng.

| Câu | Đề thật hỏi gì | Điểm | Khoá học có dạy không? |
|---|---|---|---|
| 1 | Biện luận chọn mô hình phát triển (Kanban/XP/Scrum/Agile) | **2.0** | ✅ b2 dạy đúng chủ đề (Agile vs Waterfall) |
| 2 | a) loại + cấp độ kiểm thử (0.7) · b) ai thực hiện, vì sao (0.3) | **1.0** | ⚠️ b7 dạy *viết test case*, không phải lý thuyết loại/cấp độ |
| 3 | Liệt kê 5 functional + 3 performance/security + 2 usability/scalability | **2.0** | ⚠️ b4 dạy NFR, thiếu phần functional |
| 4 | Viết 5 user story suy ra từ câu 3 | **1.5** | ❌ **không có video nào dạy** |
| 5 | Mô tả chi tiết 2 design pattern | **1.0** | ❌ **không có video nào dạy** |
| 6 | Vẽ story map cho một hoạt động trong đề | **2.5** | ❌ **không có video nào dạy** |

**Khoá học dạy gì (theo nội dung trích xuất, không theo tên file):**
Use Case Diagram (4 video: b3-2, b3-3, capcuu, ucd1), Class Diagram (b5),
Use Case Specification (b6), Test Case (b7), viết prompt AI để review code Java (b1-1, b1-2).

**Trong 4 đề này không có câu nào hỏi Use Case Diagram hay Class Diagram.**

### Nghĩa là gì

Khoảng **5.0/10 điểm** (câu 4, 5, 6) hoàn toàn không có kiến thức nào từ khoá học chống lưng.
Khuôn `Q4-User_Stories.md`, `Q5-Design_Patterns.md`, `Q6-Story_Map.md` được dựng từ
**chính đề thi và kiến thức nền của model**, không phải từ bài giảng bạn đã mua.

### Việc đầu tiên bạn phải làm

Xác minh xem **kỳ thi của bạn dùng định dạng nào**. Có ba nguồn đang nói ba kiểu khác nhau:

- 4 đề trong `papers/` (nguồn: FUOVERFLOW, sinh viên tải lên): **6 câu**
- Giảng viên trong video nói: đề thật **5 câu**, đề thi thử **7 câu**
- Tên video đánh số tới **Q7**

Không ai trong hệ thống này trả lời được câu đó thay bạn. Hỏi giảng viên hoặc xem đề cương môn.

---

## 2. Nếu bạn thi theo định dạng 6 câu (giống `papers/`)

Dùng được ngay. `04_templates/` đã có đủ 6 khuôn, sinh từ đề thật.

- **Mạnh nhất:** Q1 (khoá học dạy đúng), Q6 Story Map (đề thi có sẵn hướng dẫn định dạng ở trang 2).
- **Cần bạn tự bổ sung:** Q5 design pattern — đề ghi *"two design patterns **discussed in the courses**"*,
  tức là phải lấy pattern đã học trên lớp, không phải pattern bất kỳ. Khuôn hiện tại không biết
  lớp bạn dạy pattern nào.
- **Cần kiểm tra:** Q2 — khoá học dạy lệch hướng, khuôn này chủ yếu là kiến thức nền.

## 3. Nếu bạn thi theo định dạng khoá học dạy (Use Case, Class Diagram)

`04_templates/` hiện tại **không dùng được**, nhưng dữ liệu vẫn còn nguyên và rất tốt:

- `03_kb/playbook.md` (28 KB) — quy trình làm bài cho Use Case Diagram, Class Diagram, Use Case Spec, Test Case
- `03_kb/rubric.md` (22 KB) — tiêu chí chấm điểm
- `03_kb/glossary.md` (23 KB)
- `02_extract/*_sodo.json` (6 file) — cấu trúc sơ đồ đã đọc từ ảnh, kèm PlantUML dựng lại được
- 12 dossier trong `01_raw/*/dossier.md` — toàn bộ lời giảng + màn hình, có timestamp

Chỉ cần chạy lại P3 với chỉ thị *"lấy cấu trúc từ video làm chuẩn, bỏ qua papers/"* là ra bộ khuôn khác.
**Đừng xoá gì trong `02_extract/`** — đó là toàn bộ 6.5 giờ khoá học đã được số hoá.

---

## 4. Cách dùng khi có đề

```
1. Dán nguyên văn đề vào page/de.txt
2. Chạy 3 lượt, mỗi lượt một hội thoại RIÊNG:
   agy -p "Đọc prompts/P4_lam_bai_khi_thi.md, đề ở page/de.txt. Ghi ra page/out/run1.md" --model gemini-3.1-pro-high
   (đổi run1 -> run2 -> run3)
3. Hợp nhất:
   agy -p "Đọc prompts/P5_hop_nhat_3_ban.md và làm." --model gemini-3.1-pro-high
4. Đọc page/out/FINAL.md, phần "## CẦN NGƯỜI KIỂM TRA" là chỗ bạn phải tự quyết.
```

Trước ngày thi: lấy một đề trong `papers/` bạn đã biết đáp án, chạy thử, sai chỗ nào thì
**sửa khuôn chứ đừng sửa bài làm**.

---

## 5. Chất lượng dữ liệu — chỗ nào tin được, chỗ nào không

| Hạng mục | Tình trạng |
|---|---|
| Transcript 12 video | 10 video sạch. `b2` lặp 13%, `b1-2` lặp 15% — lặp ở từ đệm ("Đấy", "x"), không mất nội dung giảng |
| OCR màn hình | 12/12, ~5.900 khung hình, đọc được cả bảng và code trong IDE |
| Cấu trúc sơ đồ | 6 video, có quan hệ + hướng mũi tên + PlantUML. Multiplicity trống vì **giảng viên không vẽ** |
| Trích xuất 12 video | 4–8 bước quy trình mỗi video, không video nào phải làm lại |
| `03_kb/cau_truc_de_thi.md` | **ĐÃ LỖI THỜI** — lập từ video, ghi Q7 và "AI in Coding". Dùng bảng ở mục 1 thay thế |

**Chỗ tôi không kiểm chứng được:** phần lớn video chỉ trích ra 1 ví dụ mẫu, kể cả `b3-3`
có tên là "Q2 đề số 2 **và 3**". Có thể đã bỏ sót một đề. Nếu cần, chạy lại P1 cho video đó
với chỉ thị "liệt kê TẤT CẢ các đề giảng viên giải trong buổi này".

## 6. Nên làm tiếp

1. **Chốt định dạng đề** (mục 1) — mọi thứ khác phụ thuộc vào đây.
2. Hỏi giảng viên **lớp dạy design pattern nào** — Q5 đòi đúng pattern đã học.
3. Nếu thi 6 câu: chạy thử 4 đề trong `papers/` để kiểm khuôn.
4. Xoá `03_kb/cau_truc_de_thi.md` hoặc sửa cho khớp, tránh nhầm lẫn về sau.
