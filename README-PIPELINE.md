# Hệ thống luyện đề SWE202c — chạy bằng Antigravity IDE

Biến 6.5 giờ video khoá học thành **bộ khuôn làm bài Q1–Q7**, để khi có đề mới chỉ cần
dán đề vào `page/de.txt` và bảo agent một câu là ra bài làm đúng cách giảng viên dạy.

Cấu hình hiện tại chạy ở **chế độ chất lượng cao**: lấy mẫu màn hình dày, model nhận
dạng giọng nói lớn nhất, đọc sơ đồ bằng mắt, làm bài ba lần rồi đối chiếu.

---

## Sơ đồ

```
mp4 (12 file, 390 phút)
   │
   │  ── LOCAL (ffmpeg + Whisper + Vision OCR) ─────────
   │  01_prep_media.sh    → audio + 1 ảnh/5 giây (720p gốc)
   │  01b_transcribe.sh   → transcript.srt   (Whisper large-v3)
   │  01c_ocr.sh          → chữ trên màn hình
   │  02_build_dossier.py → ghép theo timestamp
   │  03_frames_for_attach.py → lọc ảnh sơ đồ để agent nhìn
   ▼
01_raw/<id>/dossier.md  +  attach/*.jpg
   │
   │  ── ANTIGRAVITY ──────────────────────────────────
   │  P1   × 12 hội thoại (song song)      → text
   │  P1b  × 5 video có sơ đồ (kèm ảnh)    → cấu trúc sơ đồ
   ▼
02_extract/<id>.json  +  <id>_sodo.json
   │  P2  × 1   (có bước tự kiểm chứng lại dossier)
   ▼
03_kb/  playbook · rubric · glossary · snippets
   │  P3  × 1   (+ đối chiếu papers/*.pdf)
   ▼
04_templates/  INDEX.md · Q1..Q7.md      ★ sản phẩm cuối
   │  P4 × 3 lượt độc lập  →  P5 hợp nhất
   ▼
page/de.txt  →  page/out/FINAL.md
```

---

## Vì sao bóc video ra text ở máy thay vì đưa video cho AI

Không phải để tiết kiệm — mà vì **kết quả tốt hơn** ở đúng thứ môn này cần:

| | Đưa video cho Gemini | Đường dossier |
|---|---|---|
| Chữ nhỏ trong IDE, bảng test case | khung hình bị nén ở 1 fps, hay mờ | ảnh **720p gốc**, OCR đọc từng ký tự |
| Thuật ngữ tiếng Anh trong giọng Việt | tuỳ model nghe | Whisper large-v3 + **mồi từ vựng SWE** |
| Truy nguồn khi nghi AI bịa | khó | mở `dossier.md` tại đúng `mm:ss` |
| Chạy lại, sửa prompt | phải upload lại | text nằm sẵn trên máy |
| Cấu trúc sơ đồ (mũi tên, multiplicity) | **model nhìn thấy** | OCR mất → **P1b vá bằng ảnh** |

Ô cuối là điểm yếu duy nhất của đường text, và `P1b_doc_so_do.md` sinh ra để bịt nó:
lọc riêng các khung hình có sơ đồ, đổi tên thành mốc thời gian, đính kèm cho agent
nhìn thẳng. Với Q5 Class Diagram và use case diagram thì bước này không được bỏ.

Chi phí chỉ là hệ quả: ~175k token cho cả khoá thay vì ~6.6 triệu nếu đẩy video lên.

---

## dossier.md là gì

Một file text cho mỗi video, ghép lời giảng và chữ trên màn hình theo mốc 30 giây:

````markdown
## [12:30]
**Nói:** bước tiếp theo mình xác định các thuộc tính của class...
**Màn hình:**
```
Book
- bookId : String
- title  : String
+ borrow() : void
```
````

Lời giảng cho **quy trình**, OCR cho **tên class, bảng test case, code**. Timestamp giữ
nguyên nên truy ngược được về video gốc. Màn hình đứng yên thì ghi `(không đổi)`;
trong một block có hai trạng thái khác nhau thì in cả hai (lúc mới hiện và lúc hoàn chỉnh).

---

## Chạy

**Bước 1 — cài Whisper (một lần):**

```bash
pip3 install mlx-whisper
```

**Bước 2 — bóc toàn bộ video thành text. Chạy một lần, để đó đi làm việc khác:**

```bash
bash scripts/01_prep_media.sh && bash scripts/01c_ocr.sh && bash scripts/01b_transcribe.sh && python3 scripts/02_build_dossier.py
```

ffmpeg ~10 phút · OCR ~5 phút · Whisper large-v3 là phần lâu nhất, khoảng 1–2 giờ cho
390 phút audio trên Apple Silicon. Chạy lại an toàn: file nào có rồi thì bỏ qua.

Muốn nhẹ và nhanh hơn: `FRAME_INTERVAL=10 bash scripts/01_prep_media.sh`, hoặc
`WHISPER_MODEL=mlx-community/whisper-large-v3-turbo bash scripts/01b_transcribe.sh`.

**Bước 3 — lọc ảnh sơ đồ cho các video có hình:**

```bash
for v in ucd1 b5 b7 b3-2 b3-3; do python3 scripts/03_frames_for_attach.py $v; done
```

**Bước 4 — mở workspace này trong Antigravity**, rồi lần lượt:

| Pha | Câu lệnh nói với agent | Số hội thoại |
|---|---|---|
| B | `Đọc prompts/P1_trich_xuat_video.md và làm cho <id>. Ghi ra 02_extract/<id>.json.` | 12, song song |
| B+ | `Đọc prompts/P1b_doc_so_do.md và làm cho <id>.` + kéo `01_raw/<id>/attach/` vào chat | 5 |
| C | `Đọc prompts/P2_gop_knowledge_base.md và làm. Input là toàn bộ 02_extract/.` | 1 |
| D | `Đọc prompts/P3_sinh_template_cau_hoi.md và làm.` | 1 |
| E | `Đọc prompts/P4_lam_bai_khi_thi.md, đề ở page/de.txt. Ghi ra page/out/runN.md` | 3 mỗi đề |
| E+ | `Đọc prompts/P5_hop_nhat_3_ban.md và làm.` | 1 mỗi đề |

Thứ tự video: `tonghop` → `capcuu` → `b2` → `b6` → `b4` → `b3-2` → `b3-3` → `b5` → `b7`
→ `ucd1` → `b1-1` → `b1-2` (lý do trong `manifest.md`).

`AGENTS.md` được Antigravity đọc tự động — trong đó có luật cấm agent mở `.mp4` và bắt
buộc trích nguồn `(id @ mm:ss)`. Nếu bản Antigravity của bạn dùng tên file luật khác,
copy `AGENTS.md` sang tên đó.

---

## Ba lượt độc lập ở pha E — vì sao đáng làm

Chạy P4 ba lần trong ba hội thoại riêng rồi để P5 đối chiếu. Chỗ nào ba bản giống nhau
thì gần như chắc đúng; chỗ nào lệch chính là chỗ model đang đoán. P5 xuất ra
`page/out/FINAL.md` kèm mục **`## CẦN NGƯỜI KIỂM TRA`** — danh sách ngắn những điểm
bạn phải tự quyết, thay vì phải rà lại cả bài. Nếu Antigravity cho đổi model, cho mỗi
lượt một model khác nhau: ba model cùng sai một chỗ hiếm hơn nhiều.

---

## Điểm dễ hỏng và cách chống

- **Whisper nghe sai thuật ngữ** ("class diagram" → "cờ lát đai ơ gram").
  → mồi từ vựng SWE trong `01b_transcribe.sh`; dossier có OCR song song;
  `AGENTS.md` luật 4 bắt agent tin màn hình cho thuật ngữ.
- **OCR mất quan hệ trong sơ đồ.** → P1b đọc lại từ ảnh, xuất cả PlantUML.
- **AI trả lời bằng kiến thức SWE chuẩn thay vì cách giảng viên dạy.**
  → P1 quy tắc 1; P2 gắn nhãn `[GV-NÓI]` / `[GV-LÀM]` / `[SUY-LUẬN]`.
- **KB chứa khẳng định bịa.** → P2 bước kiểm chứng: lấy ngẫu nhiên 15 khẳng định, mở
  lại dossier đúng timestamp, cái nào không có thì xoá.
- **Video đánh số Q khác đề thật.** → P3 Bước 0 đối chiếu `papers/*.pdf`, lấy đề thật làm chuẩn.
- **Lúc thi agent chọn nhầm khuôn.** → P4 tách riêng giai đoạn phân loại, bắt nêu căn cứ.
- **Bài trôi chảy nhưng sai dữ kiện.** → P4 bắt đánh dấu `THIẾU` thay vì bịa; P5 lọc ra
  chỗ ba bản bất đồng.

---

## Kiểm tra trước ngày thi

Lấy một đề trong `papers/` mà bạn **đã biết đáp án**, dán vào `page/de.txt`, chạy P4 ba
lượt + P5, so với đáp án. Sai chỗ nào thì **sửa `04_templates/`, không sửa bài làm**.
Lặp 2–3 lần. Đây là lúc phát hiện khuôn thiếu — không phải lúc đang thi.
