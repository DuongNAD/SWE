# P1b — ĐỌC CẤU TRÚC SƠ ĐỒ TỪ ẢNH

**Chạy cho:** `ucd1`, `b5`, `b7`, `b3-2`, `b3-3` — các video có sơ đồ / bảng.
Video thuần giảng lý thuyết thì bỏ qua bước này.

**Chuẩn bị:**
```bash
python3 scripts/03_frames_for_attach.py b5
```
rồi kéo cả thư mục `01_raw/b5/attach/` vào ô chat của Antigravity.
**Tên file chính là mốc thời gian** (`12m30s.jpg` = phút 12 giây 30).

**Output:** `02_extract/<id>_sodo.json`

---

## Vì sao có bước này

`dossier.md` lấy chữ trong sơ đồ bằng OCR, nên có tên class và tên thuộc tính,
nhưng **mất hết quan hệ**: không biết mũi tên nối từ đâu tới đâu, hướng nào,
là association hay inheritance hay composition, multiplicity `1..*` gắn ở đầu nào.
Với Q5 và use case diagram, đó chính là phần được chấm.

Bước này bạn **nhìn thẳng vào ảnh** để lấy lại phần cấu trúc đó.

## Nhiệm vụ

Với mỗi ảnh được đính kèm, nếu ảnh có sơ đồ hoặc bảng thì mô tả lại **cấu trúc**
của nó. Ảnh chỉ có chữ chạy hoặc màn hình không liên quan thì bỏ qua, đừng ép.

### Quy tắc

1. **Mốc thời gian lấy từ tên file.** `07m45s.jpg` → `ts: "07:45"`.
2. **Mô tả quan hệ theo hướng.** Không viết "A và B có liên quan". Viết
   "A ──1..*──▷ B, mũi tên đặc hướng về B, là composition".
3. **Ảnh mờ hoặc sơ đồ vẽ dở thì nói thẳng** trong `ghi_chu`, đừng đoán cho đủ.
   Sơ đồ đang vẽ dở ở phút 10 và hoàn chỉnh ở phút 14 → lấy bản phút 14, ghi rõ.
4. **Một sơ đồ xuất hiện ở nhiều ảnh** thì gộp thành một mục, lấy bản đầy đủ nhất,
   liệt kê mọi `ts` mà nó xuất hiện.
5. **Bảng thì chép đủ header và mọi dòng**, giữ đúng thứ tự cột.

### Ghi ra `02_extract/<id>_sodo.json`

```json
{
  "id": "b5",
  "so_do": [
    {
      "ts_day_du_nhat": "14:20",
      "ts_xuat_hien": ["10:05", "12:40", "14:20"],
      "loai": "class_diagram|use_case_diagram|sequence|activity|khac",
      "ten_bai_toan": "hệ thống gì, nếu đọc được",
      "phan_tu": [
        { "ten": "Book", "kieu": "class",
          "thuoc_tinh": ["- bookId : String", "- title : String"],
          "phuong_thuc": ["+ borrow() : void"] }
      ],
      "quan_he": [
        { "tu": "Member", "den": "Loan", "loai": "association",
          "multiplicity_tu": "1", "multiplicity_den": "0..*",
          "nhan": "borrows", "huong": "Member -> Loan" }
      ],
      "plantuml": "@startuml\nclass Book {\n  - bookId : String\n}\n@enduml",
      "ghi_chu": "chỗ nào mờ, chỗ nào vẽ dở"
    }
  ],
  "bang": [
    { "ts": "22:10", "tieu_de": "Test case cho chức năng Login",
      "cot": ["ID", "Precondition", "Test data", "Expected result"],
      "dong": [["TC01", "…", "…", "…"]] }
  ],
  "anh_bo_qua": ["03m20s.jpg — chỉ là slide chữ"]
}
```

Trường `plantuml` là bắt buộc với mọi sơ đồ: viết lại sơ đồ dưới dạng PlantUML để
sau này P3/P4 tái sử dụng được. Nếu không đủ thông tin dựng PlantUML, để chuỗi rỗng
và nói lý do trong `ghi_chu` — đừng bịa quan hệ cho đủ cú pháp.

## Tự kiểm

- [ ] Mỗi sơ đồ có ít nhất một quan hệ được mô tả kèm hướng và multiplicity?
- [ ] Bảng nào cũng có đủ header và đủ số dòng nhìn thấy?
- [ ] Chỗ nào đoán mà không chắc đã ghi vào `ghi_chu` chưa?
