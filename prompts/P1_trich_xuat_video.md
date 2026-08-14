# P1 — TRÍCH XUẤT 1 VIDEO

**Chạy trong:** Antigravity, một hội thoại agent riêng cho mỗi video
**Model:** model rẻ/nhanh cũng đủ — đây là việc bóc tách, không phải suy luận
**Input:** `01_raw/<id>/dossier.md` + `manifest.md`
**Output:** `02_extract/<id>.json`

**Gọi bằng một câu:**
`Đọc prompts/P1_trich_xuat_video.md và làm cho b5. Ghi ra 02_extract/b5.json.`

> Agent KHÔNG mở file `.mp4`. Toàn bộ nội dung video đã nằm trong `dossier.md`
> dưới dạng `Nói:` (lời giảng) + `Màn hình:` (chữ OCR), đều có timestamp.

---

## Nhiệm vụ

Đọc `01_raw/<id>/dossier.md` từ đầu đến cuối và trích xuất thành JSON đúng schema
bên dưới, ghi vào `02_extract/<id>.json`. Đây là khoá luyện thi SWE202c — giảng viên
hướng dẫn cách làm từng câu hỏi trong đề. Xem `manifest.md` để biết video này dạy câu nào.

## 6 quy tắc bắt buộc

1. **Không bịa.** Chỉ ghi thứ có trong dossier. Không bổ sung kiến thức SWE bạn tự biết.
   Muốn thêm gì ngoài dossier → bỏ vào `ghi_chu_ngoai_khoa` và đánh dấu rõ.
2. **Mọi mục phải có `ts`** — lấy đúng mốc `## [mm:ss]` của dossier.
3. **Ưu tiên THAO TÁC hơn LÝ THUYẾT.** "Actor là người tương tác với hệ thống" gần như
   vô giá trị. "Đọc đề thấy chữ 'quản lý' thì gạch chân, đó chắc chắn là một use case"
   mới là thứ cần lấy.
4. **Chép nguyên văn khối `Màn hình:`** khi nó là class diagram, bảng test case, code,
   hay use case description. Giữ nguyên cột, thứ tự dòng, ký hiệu. Không tóm tắt.
5. **Bắt bằng được các câu mở đầu bằng:** "cái này thi hay ra", "nhớ là", "sai chỗ này là
   mất điểm", "thầy/cô chấm sẽ nhìn vào", "mẹo là", "bước một là" → `luu_y_cham_diem`,
   `meo_lam_bai`.
6. **Transcript sai chính tả thuật ngữ là chuyện thường.** Nếu `Nói:` ghi "cờ lát đai ơ gram"
   mà `Màn hình:` ghi "Class Diagram" thì lấy bản trên màn hình. Chỗ nào thật sự không
   đoán được → `cho_khong_ro`, không viết bừa cho trôi.

## Schema — ghi ra file JSON hợp lệ, không kèm lời dẫn

```json
{
  "id": "b5",
  "tieu_de_tu_suy_ra": "",
  "cau_hoi_lien_quan": ["Q5"],
  "do_dai_phut": 52.7,

  "dan_bai": [{ "ts": "00:00", "muc": "giảng viên làm gì trong đoạn này" }],

  "quy_trinh_lam_bai": [
    {
      "buoc": 1,
      "ten_buoc": "",
      "lam_gi_cu_the": "chi tiết đủ để người khác lặp lại được",
      "dau_vao": "lấy thông tin gì từ đề",
      "dau_ra": "sinh ra cái gì",
      "cau_noi_goc": "trích nguyên văn từ dossier",
      "ts": "03:12"
    }
  ],

  "vi_du_giang_vien_lam": [
    {
      "de_bai_goc": "chép nguyên văn đề đang được giải",
      "bai_lam_hoan_chinh": "chép TOÀN BỘ đáp án từ khối Màn hình, giữ nguyên bảng/sơ đồ",
      "giang_giai": "vì sao làm vậy",
      "ts": "07:40"
    }
  ],

  "khai_niem": [{ "thuat_ngu": "", "dinh_nghia_theo_giang_vien": "", "vi_du": "", "ts": "" }],

  "cau_chu_mau": [{ "dung_khi": "viết use case description", "mau": "The system shall …", "ts": "" }],

  "luu_y_cham_diem": [{ "noi_dung": "", "muc_do": "chac_chan|co_the", "ts": "" }],
  "meo_lam_bai": [{ "meo": "", "ts": "" }],
  "loi_sai_thuong_gap": [{ "loi": "", "cach_tranh": "", "ts": "" }],
  "prompt_ai_giang_vien_dung": [{ "muc_dich": "", "prompt_nguyen_van": "", "ts": "" }],

  "so_do_va_bang": [
    { "ts": "", "loai": "class_diagram|use_case|bang_test_case|code|khac",
      "noi_dung_chep_lai": "chép đầy đủ" }
  ],

  "cho_khong_ro": [{ "ts": "", "ly_do": "" }],
  "ghi_chu_ngoai_khoa": [],
  "do_bao_phu": "đã đọc hết dossier: có/không"
}
```

## Tự kiểm trước khi ghi file

- [ ] Video dạy "cách làm Qx" mà `quy_trinh_lam_bai` chỉ có 2–3 bước → bạn đã bỏ sót, đọc lại.
- [ ] `bai_lam_hoan_chinh` đã chép đầy đủ hay mới tóm tắt? Bắt buộc đầy đủ.
- [ ] Mọi phần tử có `ts`?
- [ ] File ghi ra là JSON parse được?

## Nếu dossier quá dài (> ~15.000 token)

Xử lý nửa đầu trước, ghi `02_extract/<id>_p1.json`, mở hội thoại mới làm nửa sau
`_p2.json`. P2 sẽ ghép lại. Đừng cố nhồi một lượt — chất lượng trích xuất tụt thấy rõ.

---

## Phụ lục — nếu muốn cho AI xem video trực tiếp

Chỉ dùng khi dossier không đủ (ví dụ cần thấy thao tác chuột kéo thả). Cắt lát bằng
`bash scripts/02_chunk_video.sh b5` rồi đưa từng lát 12 phút cho Gemini qua AI Studio.
Tốn khoảng **17.000 token mỗi phút video** — đắt gấp ~30 lần đường dossier, cân nhắc kỹ.
