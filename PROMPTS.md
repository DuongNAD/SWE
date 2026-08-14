# Bộ prompt copy-paste cho Antigravity (Gemini 3.1 Pro)

Mở thư mục `SWE` này làm workspace trong Antigravity, rồi dán từng khối bên dưới.
**Mỗi khối = một hội thoại MỚI.** Đừng nối tiếp — nội dung video này sẽ lẫn sang video kia.

Thứ tự: `0` → `1` (×12) → `1b` (×5) → `2` → `3` → khi có đề thì `4` (×3) + `5`.

---

## PROMPT 0 — Khởi động (dán ngay bây giờ)

```text
Bạn đang ở workspace luyện thi SWE202c. Đọc AGENTS.md và README-PIPELINE.md trước.

Nhiệm vụ: chuẩn bị dữ liệu local. Chạy trong terminal, theo đúng thứ tự dưới đây,
báo kết quả từng bước. KHÔNG mở file .mp4 nào.

BƯỚC 1 — Thử Whisper trên 60 giây trước khi chạy 6.5 tiếng.
Đây là bước bắt buộc: nếu tên model sai thì phát hiện ngay, thay vì hỏng sau 2 tiếng.

  mkdir -p /tmp/wtest
  ffmpeg -nostdin -v error -y -ss 180 -t 60 -i 01_raw/tonghop/audio.m4a /tmp/wtest/s.m4a
  mlx_whisper /tmp/wtest/s.m4a --model mlx-community/whisper-large-v3-mlx \
    --language vi --output-format srt --output-dir /tmp/wtest --output-name s
  cat /tmp/wtest/s.srt

Lần đầu sẽ tải model vài GB, đợi.
- Nếu báo lỗi không tải được model: thử lại với mlx-community/whisper-large-v3-turbo.
  Model nào chạy được thì dùng model đó cho mọi bước sau (đặt qua biến WHISPER_MODEL).
- In ra 10 dòng đầu của file srt và nhận xét: tiếng Việt có dấu đúng không, thuật ngữ
  tiếng Anh (use case, class diagram...) có ra đúng chữ không. Nếu sai bét thì DỪNG
  và báo tôi, đừng chạy tiếp.

BƯỚC 2 — Cắt ảnh + audio cho toàn bộ 12 video (khoảng 10 phút):

  bash scripts/01_prep_media.sh

BƯỚC 3 — OCR chữ trên màn hình (khoảng 5 phút):

  bash scripts/01c_ocr.sh

BƯỚC 4 — Nhận dạng giọng nói. Chạy NỀN vì mất 1-2 tiếng:

  nohup bash scripts/01b_transcribe.sh > 01_raw/whisper.log 2>&1 &

Nếu bước 1 phải đổi model thì chạy:
  WHISPER_MODEL=<model chạy được> nohup bash scripts/01b_transcribe.sh > 01_raw/whisper.log 2>&1 &

BƯỚC 5 — Báo cáo. In bảng: mỗi video một dòng, gồm id, số phút, số frame, số ảnh
scene, đã có transcript chưa. Rồi nói cho tôi biết:
- Whisper đang chạy tới video nào (xem: tail -3 01_raw/whisper.log)
- Ước tính bao lâu nữa xong
- Lệnh để tôi tự kiểm tra tiến độ sau

Đừng chạy bước 6 bây giờ. Khi nào Whisper xong tôi sẽ bảo.
```

---

## PROMPT 0b — Sau khi Whisper chạy xong

```text
Kiểm tra Whisper đã xong chưa:  ls 01_raw/*/transcript.srt | wc -l   (phải ra 12)

Nếu đủ 12, chạy tiếp:

  python3 scripts/02_build_dossier.py
  for v in ucd1 b5 b7 b3-2 b3-3; do python3 scripts/03_frames_for_attach.py $v; done

Rồi mở 01_raw/b5/dossier.md, đọc khoảng 100 dòng ở giữa file và đánh giá giúp tôi:
- Phần "Nói:" có đọc hiểu được không, hay Whisper nghe sai quá nhiều?
- Phần "Màn hình:" có bắt được tên class / bảng không?
- Có chỗ nào hai phần mâu thuẫn nhau không?

In bảng cuối: mỗi video một dòng gồm id, số ký tự dossier, ước tính token,
số ảnh trong attach/. Video nào dossier < 3000 ký tự thì cảnh báo — nhiều khả năng
transcript hỏng, cần chạy lại riêng video đó.

Chưa làm gì thêm. Xong báo tôi.
```

---

## PROMPT 1 — Trích xuất một video (lặp 12 lần, đổi `<id>`)

Chạy song song được trong Agent Manager. Thứ tự nên làm:
`tonghop` → `capcuu` → `b2` → `b6` → `b4` → `b3-2` → `b3-3` → `b5` → `b7` → `ucd1` → `b1-1` → `b1-2`

```text
Đọc prompts/P1_trich_xuat_video.md và làm đúng theo đó cho video id = b5.

Input: 01_raw/b5/dossier.md và manifest.md.
Output: ghi ra 02_extract/b5.json.

Nhắc lại 3 luật quan trọng nhất trong file đó:
- KHÔNG mở file .mp4. Toàn bộ nội dung đã nằm trong dossier.md.
- Mọi mục phải có timestamp lấy từ mốc "## [mm:ss]" của dossier.
- Chép NGUYÊN VĂN mọi bảng, sơ đồ, code trong khối "Màn hình:". Không tóm tắt.

Dossier dài thì xử lý nửa đầu trước rồi nửa sau, đừng đọc lướt phần giữa.
Xong thì in ra: số bước trong quy_trinh_lam_bai, số ví dụ mẫu, số lưu ý chấm điểm,
và những chỗ bạn đưa vào cho_khong_ro.
```

---

## PROMPT 1b — Đọc sơ đồ từ ảnh (cho `ucd1`, `b5`, `b7`, `b3-2`, `b3-3`)

**Trước khi dán: kéo cả thư mục `01_raw/b5/attach/` vào ô chat.**

```text
Đọc prompts/P1b_doc_so_do.md và làm theo, cho video id = b5.

Các ảnh tôi vừa đính kèm là khung hình chứa sơ đồ, lấy từ 01_raw/b5/attach/.
TÊN FILE CHÍNH LÀ MỐC THỜI GIAN: 12m30s.jpg nghĩa là phút 12 giây 30.

Việc cần làm: nhìn ảnh và lấy lại phần mà OCR đã làm mất — QUAN HỆ giữa các phần tử.
Không phải chỉ liệt kê tên class. Với mỗi quan hệ phải nói rõ: nối từ đâu đến đâu,
hướng mũi tên, loại quan hệ (association / aggregation / composition / inheritance /
include / extend), và multiplicity nằm ở đầu nào.

Mỗi sơ đồ phải xuất kèm mã PlantUML dựng lại được. Chỗ nào ảnh mờ hoặc sơ đồ đang
vẽ dở thì ghi vào ghi_chu, KHÔNG bịa quan hệ cho đủ cú pháp.

Ghi ra 02_extract/b5_sodo.json.
```

---

## PROMPT 2 — Gộp thành knowledge base (1 lần, sau khi xong hết Pha 1)

```text
Đọc prompts/P2_gop_knowledge_base.md và làm đúng theo đó.

Input: toàn bộ 02_extract/*.json (cả các file _sodo.json) + manifest.md.
Output: 6 file trong 03_kb/ như prompt mô tả.

Ba điều đừng bỏ qua:
1. Gắn nhãn [GV-NÓI] / [GV-LÀM] / [SUY-LUẬN] cho từng khẳng định. Tôi cần phân biệt
   được đâu là lời giảng viên, đâu là bạn tự suy ra.
2. Mọi khẳng định phải kèm nguồn dạng (b5 @ 12:30). Không nguồn thì đừng viết ra.
3. Bước kiểm chứng ở cuối: lấy ngẫu nhiên 15 khẳng định, mở lại đúng dossier tại
   timestamp đó, kiểm tra xem dossier có thực sự nói vậy không. Cái nào không tìm
   thấy thì xoá hoặc hạ xuống [SUY-LUẬN]. In bảng kết quả kiểm chứng.

File 03_kb/cau_truc_de_thi.md là quan trọng nhất. Câu nào không đủ bằng chứng thì
ghi CHƯA XÁC ĐỊNH, tuyệt đối không đoán cho đủ bảng.
```

---

## PROMPT 3 — Sinh khuôn làm bài (1 lần)

```text
Đọc prompts/P3_sinh_template_cau_hoi.md và làm đúng theo đó.

Input: toàn bộ 03_kb/ + các file đề mẫu papers/*.pdf + khung 04_templates/_KHUNG_MAU.md.
Output: 04_templates/INDEX.md và một file Q<n>-<tên>.md cho mỗi câu trong đề thật.

Bắt đầu bằng Bước 0 và in kết quả ra trước khi làm gì khác: đối chiếu cấu trúc đề
suy từ video (03_kb/cau_truc_de_thi.md) với đề thật trong papers/*.pdf. Số câu có
khớp không? Video gọi là Q5 thì trong đề thật có đúng là Q5 không? Đề hỏi gì mà
video không dạy? Lệch chỗ nào thì LẤY ĐỀ THẬT LÀM CHUẨN.

Khuôn phải ĐIỀN ĐƯỢC chứ không phải mô tả được: có sẵn khối text với chỗ trống
{{...}} để thay, kèm ít nhất một ví dụ đã điền đầy đủ lấy từ 03_kb/snippets/.

Cuối cùng làm Bước 3: lấy từng đề trong papers/ thử làm bài CHỈ bằng khuôn vừa tạo,
chỗ nào khuôn không đủ dùng thì sửa khuôn, rồi báo tôi đã sửa những gì.
```

---

## PROMPT 4 — Làm bài (khi đã dán đề vào `page/de.txt`)

Chạy **3 lần trong 3 hội thoại riêng**, đổi `run1` → `run2` → `run3`.
Nếu đổi được model thì mỗi lượt một model khác nhau.

```text
Đọc prompts/P4_lam_bai_khi_thi.md và làm đúng theo đó.

Đề nằm ở page/de.txt. Ghi bài làm ra page/out/run1.md.

Chỉ đọc: page/de.txt, 04_templates/, 03_kb/playbook.md, 03_kb/rubric.md.
KHÔNG mở 01_raw/ hay 02_extract/ — khuôn đã chứa đủ.

Làm đủ 4 giai đoạn và in ra cả 4:
1. Phân loại từng câu vào khuôn nào, nêu căn cứ. Không khớp khuôn nào thì nói thẳng.
2. Moi dữ kiện từ đề vào bảng của khuôn. Đề không cho thì ghi THIẾU, đừng bịa.
3. Bài làm, giữ nguyên định dạng khuôn, viết như bài nộp thật.
4. Tự chấm theo rubric, có mục nào chưa đạt thì sửa lại rồi in bản cuối.
```

---

## PROMPT 5 — Hợp nhất 3 bản (sau khi có run1, run2, run3)

```text
Đọc prompts/P5_hop_nhat_3_ban.md và làm đúng theo đó.

Input: page/out/run1.md, run2.md, run3.md, page/de.txt, 04_templates/, 03_kb/rubric.md.
Output: page/out/FINAL.md

Với từng câu trong đề, đối chiếu ba bản và phân loại từng điểm khác biệt thành
ĐỒNG THUẬN / ĐA SỐ / BẤT ĐỒNG. Lệch nhỏ như tên một thuộc tính hay một dòng test
case cũng phải ghi ra, đừng bỏ qua vì "đại khái giống nhau".

FINAL.md gồm hai phần: bài làm sạch sẵn sàng nộp, và cuối file là mục
"## CẦN NGƯỜI KIỂM TRA" liệt kê mọi chỗ BẤT ĐỒNG, mọi chỗ THIẾU và [NGOÀI KHUÔN],
mỗi mục một dòng kèm câu hỏi cụ thể tôi cần tự quyết.

Phần thứ hai mới là thứ tôi cần nhất — nó chỉ đúng chỗ tôi phải tự nghĩ.
```

---

## Khi có trục trặc

| Hiện tượng | Dán câu này |
|---|---|
| Whisper một video nghe sai bét | `Xoá 01_raw/<id>/transcript.srt rồi chạy lại: WHISPER_MODEL=mlx-community/whisper-large-v3-mlx bash scripts/01b_transcribe.sh <id> && python3 scripts/02_build_dossier.py <id>` |
| Dossier thiếu chữ trên màn hình | `Chạy: FRAME_INTERVAL=3 bash scripts/01_prep_media.sh <id> && bash scripts/01c_ocr.sh <id> && python3 scripts/02_build_dossier.py <id>` |
| Agent bịa, không trích nguồn | `Mọi khẳng định trong file bạn vừa ghi phải có nguồn (id @ mm:ss). Rà lại, cái nào không dẫn được nguồn từ dossier thì xoá.` |
| Agent định mở mp4 | `Dừng lại. Không mở .mp4. Nội dung video nằm ở 01_raw/<id>/dossier.md.` |
