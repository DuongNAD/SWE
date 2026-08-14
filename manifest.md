# MANIFEST — Nguồn dữ liệu khoá SWE202c

> File này là "bản đồ" cho AI. Dán kèm file này vào MỌI prompt để AI biết
> nó đang xử lý video nào, video đó dạy câu hỏi nào trong đề thi.

## Cấu trúc đề thi (suy ra từ tên video — AI phải VERIFY lại ở Pha C)

| Slot | Nội dung phỏng đoán      | Video dạy chính            |
|------|--------------------------|----------------------------|
| Q1   | (chưa xác định)          | b2                         |
| Q2   | (chưa xác định)          | b3-2, b3-3                 |
| Q3   | (chưa xác định)          | b6                         |
| Q4   | (chưa xác định)          | b4                         |
| Q5   | Class Diagram            | b5                         |
| Q6   | (chưa xác định)          | — (thiếu video, xem cap-cuu)|
| Q7   | Test case                | b7                         |
| UC   | Use case diagram         | ucd1 (có thể là Q1 hoặc Q2)|

**Nhiệm vụ bắt buộc của Pha C:** điền đầy đủ bảng trên bằng bằng chứng từ
video + `papers/*.pdf`, KHÔNG được đoán.

## Danh sách video

| id     | phút | file |
|--------|------|------|
| b1-1   | 28.8 | YTSave_YouTube_Buoi-1-1-Luyen-tap-viet-Prompt-AI-de-tri_Media_wZxVP4c4QXo_002_720p.mp4 |
| b1-2   | 31.4 | YTSave_YouTube_Buoi-1-2-Luyen-prompt-AI-de-Trial_Media_G_le7-qZK64_002_720p.mp4 |
| b2     | 18.6 | YTSave_YouTube_Buoi-2-Cach-lam-Q1_Media_jQRYxaZ8J7c_002_720p.mp4 |
| b3-2   | 48.4 | YTSave_YouTube_Buoi-3-2-Luyen-tap-Q2-de-so-1_Media_QToTGFd3W3I_002_720p.mp4 |
| b3-3   | 30.3 | YTSave_YouTube_Buoi-3-3-Luyen-tap-Q2-de-so-2-va-3_Media_yF4Qp3MNxzQ_002_720p.mp4 |
| b4     | 24.4 | YTSave_YouTube_Buoi-4-Luyen-tap-Q4_Media_Bs3085SXkI_002_720p.mp4 |
| b5     | 52.7 | YTSave_YouTube_Buoi-5-Luyen-tap-Q5-Class-Diagram_Media_-fbE7S8thBI_002_720p.mp4 |
| b6     | 14.4 | YTSave_YouTube_Buoi-6-Cach-lam-Q3_Media_pm7lnASFB-8_002_720p.mp4 |
| b7     | 41.0 | YTSave_YouTube_Buoi-7-Luyen-tap-Q7-Cach-viet-test-case_Media_8QTtCmm6Fq0_002_720p.mp4 |
| capcuu | 32.8 | YTSave_YouTube_CAP-CUU-CAP-TOC-SWE202c-chinh-phuc-9-SWE_Media_ZvcHCc4GYQQ_002_720p.mp4 |
| ucd1   | 60.7 | YTSave_YouTube_Luyen-Use-case-diagram-1_Media_0zr0WJhgp_o_002_720p.mp4 |
| tonghop|  7.1 | YTSave_YouTube_Tong-hop-toan-bo-kien-thuc-co-ban-SWE202_Media_MaC95ZwAotk_001_720p.mp4 |

Tổng: ~390 phút.

## Thứ tự xử lý (QUAN TRỌNG — không làm tuỳ tiện)

1. `tonghop` (7 phút) → lấy khung kiến thức tổng quát trước, làm "từ điển" cho các video sau.
2. `capcuu` (33 phút) → thường là video tổng ôn, chứa nguyên cấu trúc đề thi + tiêu chí chấm.
3. `b2` → `b6` → `b4` → `b3-2` → `b3-3` → `b5` → `b7` → `ucd1` (theo từng Q).
4. `b1-1`, `b1-2` (prompt AI) → xử lý CUỐI, dùng để rút ra "prompt gốc mà giảng viên dạy",
   nhập thẳng vào `03_kb/prompt_giangvien.md`.

## Nguồn phụ

- `papers/*.pdf` (5 file) — nghi là đề thi mẫu. Dùng ở Pha C để đối chiếu
  cấu trúc đề thật với cấu trúc suy ra từ video.
