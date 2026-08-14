# Hướng dẫn cho agent (Antigravity)

Workspace này biến khoá luyện thi **SWE202c** thành bộ khuôn làm bài.
Đề thi có khung cố định **Q1–Q7** (Use case diagram, Class diagram, test case…).

## Luật cứng — vi phạm là hỏng cả hệ thống

1. **KHÔNG mở, không đọc, không phân tích file `.mp4`.** Video đã được chuyển
   thành text ở `01_raw/<id>/dossier.md`. Chỉ làm việc trên dossier.
   Mở mp4 vừa vô ích vừa đốt sạch quota.
2. **Mọi khẳng định phải kèm nguồn** dạng `(b5 @ 12:30)`. Không có nguồn thì không viết ra.
3. **Không thêm kiến thức Software Engineering ngoài khoá học.** Trong dossier có gì
   thì dùng nấy. Nếu buộc phải bổ sung, đánh dấu `[NGOÀI-KHOÁ]` để người dùng tự quyết.
4. **Trong dossier, khi `Nói:` và `Màn hình:` lệch nhau:** tin `Màn hình` cho tên class,
   thuộc tính, bảng, code, ký hiệu UML; tin `Nói` cho quy trình và lời giải thích.
   Transcript do máy nhận dạng nên hay sai thuật ngữ tiếng Anh.
5. **Không tóm tắt bảng và sơ đồ.** Chép đầy đủ. Bảng test case thiếu một cột là mất điểm thật.
6. **Không sửa file trong `01_raw/`** — đó là dữ liệu gốc.

## Cách chia việc (vì chất lượng, không phải vì quota)

- **Một video = một hội thoại agent riêng.** Xong thì mở hội thoại mới. Nhồi nhiều
  video vào một hội thoại làm nội dung video này lẫn sang video kia — lỗi kiểu đó
  rất khó phát hiện vì bài làm vẫn trôi chảy.
- Pha B chạy song song trong Agent Manager, mỗi agent một video.
- Dossier dài (> ~15.000 token) thì xử lý theo nửa rồi ghép. Nhồi một lượt thì phần
  giữa video bị tóm tắt qua loa — đây là lỗi hay gặp nhất của cả pipeline.
- Được phép chạy lại một bước nhiều lần và so kết quả. Chỗ nào hai lần chạy ra khác
  nhau là chỗ đang đoán — ghi vào `cho_khong_ro` thay vì chọn bừa.

## Bản đồ thư mục

| Đường dẫn | Là gì | Ai ghi |
|---|---|---|
| `*.mp4` | video gốc | — (agent không đụng) |
| `01_raw/<id>/dossier.md` | **transcript + OCR màn hình, có timestamp** | script local |
| `01_raw/<id>/attach/` | ảnh sơ đồ để đính kèm cho agent nhìn (P1b) | script local |
| `02_extract/<id>.json` | bóc tách có cấu trúc | agent, pha B |
| `02_extract/<id>_sodo.json` | cấu trúc sơ đồ đọc từ ảnh | agent, pha B (P1b) |
| `03_kb/` | playbook, rubric, glossary, ví dụ mẫu | agent, pha C |
| `04_templates/` | **khuôn làm bài Q1–Q7** — sản phẩm cuối | agent, pha D |
| `page/de.txt` | chỗ dán đề | người dùng |
| `page/out/` | bài làm | agent, pha E |
| `papers/*.pdf` | đề thi mẫu, dùng đối chiếu ở pha D | — |
| `prompts/P1..P4` | nhiệm vụ của từng pha | — |

## Cách gọi

Nói với agent đúng một câu, không cần dán prompt dài:

- `Đọc prompts/P1_trich_xuat_video.md và làm cho b5. Ghi ra 02_extract/b5.json.`
- `Đọc prompts/P1b_doc_so_do.md và làm cho b5.` *(kèm ảnh từ `01_raw/b5/attach/`)*
- `Đọc prompts/P2_gop_knowledge_base.md và làm. Input là toàn bộ 02_extract/.`
- `Đọc prompts/P3_sinh_template_cau_hoi.md và làm.`
- `Đọc prompts/P4_lam_bai_khi_thi.md, đề nằm ở page/de.txt.`
- `Đọc prompts/P5_hop_nhat_3_ban.md và làm.` *(sau khi có run1/2/3.md)*

Thứ tự xử lý video xem `manifest.md`. Làm `tonghop` và `capcuu` trước.
