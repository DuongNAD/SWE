# P2 — GỘP TOÀN BỘ THÀNH KNOWLEDGE BASE

**Chạy trong:** Antigravity, hội thoại MỚI, dùng model mạnh nhất đang có
**Input:** toàn bộ `02_extract/*.json` + `manifest.md` — agent tự đọc
**Output:** ghi vào `03_kb/`
**Chạy:** 1 lần, sau khi Pha B xong hết. Không chạy sớm.

**Gọi bằng một câu:**
`Đọc prompts/P2_gop_knowledge_base.md và làm. Input là toàn bộ 02_extract/.`

---

## Nhiệm vụ

Mỗi file trong `02_extract/` là bản bóc tách của một video trong khoá luyện thi SWE202c.
Đọc hết, cộng với `manifest.md`, rồi hợp nhất thành bộ tài liệu chuẩn để sau này dùng
làm bài thi. Không mở lại `01_raw/` trừ khi cần đối chiếu một chỗ nghi ngờ cụ thể.

### Nguyên tắc hợp nhất

1. **Gộp các lát cùng một video trước** (b5_p01 + b5_p02 + b5_p03 → b5), khử phần
   chồng lấn 45 giây bị lặp.
2. **Mâu thuẫn thì không được im lặng chọn bừa.** Nếu 2 video nói khác nhau về cùng
   một điểm, ghi CẢ HAI vào `03_kb/mau_thuan.md` kèm ts, và chọn bản trong video
   ôn tổng (`capcuu`, `tonghop`) làm bản ưu tiên, nêu rõ lý do chọn.
3. **Phân biệt 3 mức tin cậy** và gắn nhãn cho từng khẳng định:
   - `[GV-NÓI]` giảng viên nói thẳng ra
   - `[GV-LÀM]` suy ra từ thao tác giảng viên làm mẫu (không nói ra miệng)
   - `[SUY-LUẬN]` bạn tự suy ra → phải ghi rõ và để riêng
4. **Mỗi khẳng định phải kèm nguồn** dạng `(b5 @ 12:30)`. Không nguồn = không đưa vào.

### Sản phẩm — tạo đúng 6 file

#### `03_kb/cau_truc_de_thi.md`
Bảng: mỗi câu Q1..Q7 gồm — tên câu, yêu cầu đề thường ra, thang điểm (nếu có nhắc),
thời gian nên dành, video nào dạy, độ chắc chắn. Đây là file quan trọng nhất.
Nếu không đủ bằng chứng cho một câu → ghi `CHƯA XÁC ĐỊNH` chứ không đoán.

#### `03_kb/playbook.md`
Với MỖI câu Q1..Q7: quy trình làm bài dạng đánh số bước, hợp nhất từ mọi video dạy
câu đó. Mỗi bước phải trả lời được "đọc gì trong đề → viết ra cái gì". Kèm nguồn.

#### `03_kb/glossary.md`
Thuật ngữ ↔ định nghĩa **theo cách giảng viên định nghĩa** (không theo sách chuẩn),
kèm ví dụ và nguồn. Ghi chú chỗ nào giảng viên định nghĩa khác sách.

#### `03_kb/rubric.md`
Checklist chấm điểm rút từ mọi câu `luu_y_cham_diem` + `loi_sai_thuong_gap`.
Nhóm theo từng câu Q. Ưu tiên các lỗi bị nhắc ở nhiều video (= hay mất điểm nhất).

#### `03_kb/prompt_giangvien.md`
Toàn bộ prompt AI mà giảng viên dạy trong b1-1, b1-2 — chép nguyên văn, kèm mục đích
dùng và câu Q áp dụng. Đây là "prompt gốc" của khoá, quý hơn prompt tự nghĩ.

#### `03_kb/snippets/` (nhiều file)
Mỗi ví dụ hoàn chỉnh giảng viên làm mẫu → 1 file `.md` riêng, đặt tên
`Q5-vidu-01-<chủ đề>.md`, nội dung là đề bài + bài làm đầy đủ. Giữ nguyên định dạng.
Đây là bộ few-shot example dùng lại khi thi.

### Bước kiểm chứng (bắt buộc — đừng bỏ vì "tốn lượt")

Sau khi viết xong `03_kb/`, chọn **ngẫu nhiên 15 khẳng định** trong `playbook.md` và
`rubric.md`, mở đúng `01_raw/<id>/dossier.md` tại timestamp đã trích, và kiểm tra xem
dossier có thực sự nói vậy không.

In ra bảng: `khẳng định | nguồn | dossier có nói vậy không | sửa gì`.

Khẳng định nào **không tìm thấy trong dossier** → xoá khỏi KB hoặc hạ xuống
`[SUY-LUẬN]`. Đây là bước bắt lỗi bịa đặt — nếu bỏ qua, sai sót sẽ chui thẳng vào
khuôn làm bài và bạn không bao giờ phát hiện ra.

### Nếu có file `_sodo.json`

Các file `02_extract/<id>_sodo.json` (từ P1b) chứa cấu trúc sơ đồ đọc từ ảnh:
quan hệ, hướng mũi tên, multiplicity, mã PlantUML. Ưu tiên chúng hơn phần sơ đồ
trong file `.json` thường — vì bản thường chỉ có chữ OCR, đã mất cấu trúc.
Đưa PlantUML vào `03_kb/snippets/` để tái sử dụng.

### Cuối cùng, in ra bảng KIỂM KÊ
| Câu | Số bước playbook | Số ví dụ mẫu | Số tiêu chí rubric | Lỗ hổng cần bổ sung |

Câu nào có < 2 ví dụ mẫu → đánh dấu ⚠️ và nói rõ nên xem lại video nào.
