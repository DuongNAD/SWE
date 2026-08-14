# P5 — LÀM BÀI 3 LẦN ĐỘC LẬP RỒI HỢP NHẤT

Dùng thay cho P4 khi bạn muốn chất lượng cao nhất và không tiếc quota.
Đây là cách hiệu quả nhất để bắt lỗi của model: cùng một đề, chỗ nào ba lần chạy
đều ra giống nhau thì gần như chắc đúng; chỗ nào lệch nhau chính là chỗ model đang
đoán — và đó đúng là chỗ bạn cần tự kiểm tra bằng đầu mình.

## Quy trình

**Bước 1 — chạy P4 ba lần trong BA hội thoại RIÊNG BIỆT.**
Phải là hội thoại mới hoàn toàn, không nối tiếp, để ba bản thực sự độc lập.

```
Hội thoại 1:  Đọc prompts/P4_lam_bai_khi_thi.md, đề ở page/de.txt. Ghi ra page/out/run1.md
Hội thoại 2:  Đọc prompts/P4_lam_bai_khi_thi.md, đề ở page/de.txt. Ghi ra page/out/run2.md
Hội thoại 3:  Đọc prompts/P4_lam_bai_khi_thi.md, đề ở page/de.txt. Ghi ra page/out/run3.md
```

Nếu Antigravity cho chọn model khác nhau, càng tốt: cho mỗi lượt một model khác nhau.
Ba model khác nhau cùng sai một chỗ thì hiếm hơn nhiều so với một model chạy ba lần.

**Bước 2 — hội thoại thứ tư, đối chiếu:**
```
Đọc prompts/P5_hop_nhat_3_ban.md và làm.
```

---

## Nhiệm vụ (hội thoại thứ tư)

Đọc `page/out/run1.md`, `run2.md`, `run3.md`, `page/de.txt`, `04_templates/`, `03_kb/rubric.md`.

### 1. Bảng đối chiếu

Với **từng câu** trong đề:

| Câu | Ba bản có chọn cùng một khuôn không | Chỗ giống nhau | Chỗ lệch nhau |
|---|---|---|---|

Lệch ở mức nào cũng phải ghi ra, kể cả lệch nhỏ như số lượng actor, tên một thuộc tính,
một dòng test case. Đừng bỏ qua vì "đại khái giống nhau".

### 2. Phân loại từng chỗ lệch

- **`ĐỒNG THUẬN`** — cả ba giống nhau → giữ nguyên.
- **`ĐA SỐ`** — hai giống, một khác → lấy bản hai, nhưng **nêu rõ bản thiểu số nói gì
  và vì sao bạn không chọn**. Đôi khi bản thiểu số mới đúng.
- **`BẤT ĐỒNG`** — cả ba khác nhau → **cảnh báo đỏ**. Đối chiếu với `03_kb/playbook.md`
  và ví dụ mẫu trong `03_kb/snippets/` để phân xử, và nếu vẫn không chắc thì nói thẳng
  là không chắc. Không được chọn bừa rồi trình bày như thể chắc chắn.

### 3. Bản hợp nhất

Ghi `page/out/FINAL.md` gồm:

1. **Bài làm cuối cùng** — sạch, đúng định dạng khuôn, sẵn sàng nộp. Không chú thích
   xen vào, không "theo tôi thì".
2. Cuối file, tách riêng phần **`## CẦN NGƯỜI KIỂM TRA`**: liệt kê mọi chỗ `BẤT ĐỒNG`
   và mọi chỗ đánh dấu `THIẾU` hoặc `[NGOÀI KHUÔN]`, kèm câu hỏi cụ thể bạn cần
   người học tự quyết. Ngắn gọn, mỗi mục một dòng.

Phần 2 mới là thứ đáng tiền: nó chỉ đúng chỗ bạn phải tự nghĩ, thay vì phải rà lại cả bài.

### 4. Chấm theo rubric

Chạy `03_kb/rubric.md` trên bản hợp nhất. Mục nào chưa đạt thì sửa `FINAL.md` ngay,
rồi in bảng kết quả chấm ở cuối.
