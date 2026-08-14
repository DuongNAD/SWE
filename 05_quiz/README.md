# 05_quiz — Ngân hàng câu hỏi từ slide SWE202c

Bóc từ Google Slides `Sever_1_SEMESTER_3-4_SWE202c`
(`1_MO0B88ZCLa7cV_bi8NmbwS-o9h-MiHuGnS9I2G5NwQ`, 276 slide, quyền "Chỉ xem").

| File | Là gì |
|---|---|
| `quiz.html` | Trang luyện tập cả 260 câu — mở bằng trình duyệt, không cần mạng |
| `phan_1..5.html` | Cùng trang đó nhưng chia nhỏ: 50/50/50/50/60 câu |
| `NGAN_HANG_CAU_HOI.md` | 260 câu + đáp án, để đọc/in |
| `cau_hoi.json` | Dữ liệu có cấu trúc, để script khác dùng lại |
| `anh_slide/` | 276 ảnh chụp gốc, `slide_NNN.png` khớp số slide trong deck |

## Số liệu

- **260** câu trắc nghiệm — trong đó **51** câu nhiều đáp án, **13** câu True/False
- **16** slide nội dung (bìa, quảng cáo khoá học, link tài liệu) — không phải câu hỏi
- 1 câu bị lặp 2 lần: đó là lỗi của deck gốc, không phải lỗi bóc tách

## Cách lấy dữ liệu

1. Chụp màn hình từng slide trong Google Slides (deck chặn tải xuống) — vùng chụp gồm
   cả khung ghi chú ở đáy, nơi chứa đáp án.
2. OCR bằng Gemini `gemini-3.5-flash-lite`, xoay vòng API key.
3. 26 slide bị Gemini từ chối (`finishReason=RECITATION` — bộ câu hỏi OOAD kinh điển
   của Bruegge & Dutoit có nhiều trong dữ liệu huấn luyện) được Claude đọc tay từ ảnh.
   Các câu này có cờ `nguon_ocr: "claude-doc-tay"` trong dữ liệu thô.

## Điểm còn thiếu — cần biết

Khung ghi chú của Slides chỉ hiện **1 dòng** ở độ cao mặc định. Với phần lớn câu hỏi,
ghi chú có dạng:

```
B
Explanation: <phần giải thích bị khuất>
```

→ **Đáp án lấy đủ, nhưng phần giải thích thì không.** Muốn có luôn giải thích thì
kéo cao khung ghi chú trong Slides rồi chụp lại — chạy lại `capture.py` là xong.

## Mẹo ghi nhớ

Cả **260/260** câu đều có mẹo, do Gemini soạn từ câu hỏi + đáp án đúng, gồm 3 phần:

- **Móc nhớ** — cụm ngắn nối từ khoá trong đề với từ khoá trong đáp án, kiểu
  `Cyclomatic complexity → độ phức tạp → safety`. Đây là thứ nhẩm lại trong phòng thi.
- **Vì sao** — một câu giải thích đáp án đúng.
- **Bẫy** — phương án dễ chọn nhầm nhất và lý do nó sai.

Trong `quiz.html`: bấm **💡 Gợi ý** (phím `H`) để xem trước móc nhớ khi bí; trả lời xong
thì hiện đầy đủ cả vì sao lẫn bẫy. Trong file Markdown thì nằm ngay dưới đáp án.

## Dùng `quiz.html`

Mở bằng trình duyệt. Chọn phương án → **Kiểm tra**, qua câu bằng ← →.
Phím tắt: `A`–`E` chọn, `Enter` kiểm tra / sang câu sau, `H` gợi ý.

- **Lặp câu sai** (mặc định BẬT): câu trả lời sai được chèn lại vào 5 câu sau để gặp lại
  ngay khi còn nhớ — nhớ được là nhờ chỗ này chứ không phải nhờ đọc lại.
- **Ôn câu sai**: lọc riêng những câu từng sai.
- **Xáo trộn**, **Làm lại từ đầu**.

### Bản chia nhỏ

| File | Câu (theo số thứ tự trong `NGAN_HANG_CAU_HOI.md`) | Số câu |
|---|---|---|
| `phan_1.html` | 1–50 | 50 |
| `phan_2.html` | 51–100 | 50 |
| `phan_3.html` | 101–150 | 50 |
| `phan_4.html` | 151–200 | 50 |
| `phan_5.html` | 201–260 | 60 |

Mỗi phần là một trang độc lập, đầy đủ tính năng như bản 260 câu, và có **khoá
`localStorage` riêng** — làm phần nào tính điểm phần đó, không đè lên nhau cũng không đè
lên `quiz.html`. Hàng nút ở đầu trang nhảy qua lại giữa các phần (phải để chung một thư mục).

Sinh lại: `python3 scripts/build.py` (bản đủ) rồi `python3 scripts/chia.py` (các phần).
Muốn đổi cỡ phần thì sửa `CO` trong `scripts/trang.py` — phần cuối luôn nuốt phần dư,
nên `CO = 50` với 260 câu ra 50/50/50/50/60. Khung HTML nằm ở `scripts/quiz_tpl.html`,
cả hai script dùng chung.

### Tiến độ

Tiến độ lưu trong `localStorage`. Nếu mở ở nơi chặn `localStorage` (khung xem sandbox,
cửa sổ ẩn danh), trang vẫn chạy bình thường, chỉ hiện cảnh báo là không lưu được.
Dòng dưới tiêu đề có ghi **bản HH:MM dd/mm** — để biết chắc không phải bản cũ trong cache.

## Kiểm thử

`quiz.html` được kiểm tra tự động bằng jsdom (`scripts/test_quiz.js`): bấm chọn,
chọn nhiều đáp án, chấm điểm, phím tắt, gợi ý, giữ trạng thái khi chuyển câu.
Sửa file rồi thì chạy lại test trước khi tin là nó chạy.

Cần `jsdom` (`npm i jsdom`, đặt `NODE_PATH` tới thư mục `node_modules` đó nếu cài chỗ khác).
Không truyền gì thì test bản đủ; truyền đường dẫn để test một phần:

```
cd scripts
for f in ../quiz.html ../phan_*.html; do node test_quiz.js "$f" || break; done
```
