# Đề FE SWE201c — fuoverflow.com

Mục tiêu: gom toàn bộ đề trắc nghiệm FE/RE của môn SWE201c trên
<https://fuoverflow.com/forums/SWE201c/>, OCR ra text, chấm đáp án bằng AI rồi thống kê.

## Trạng thái: ĐANG KẸT Ở PAYWALL

Ảnh đề là **tệp đính kèm** của bài viết. Tài khoản `duonganhdn2000@gmail.com`
(username `Dương Anh1`, 1.041 FUO Point) đã đăng nhập được nhưng **mọi ảnh đều trả HTTP 403**
với trang lỗi *"Bạn cần nâng cấp để truy cập"*.

Xem <https://fuoverflow.com/account/upgrades> — tài khoản chưa có gói nào:

| Gói | Giá | Quyền liên quan |
|---|---|---|
| FUO MEMBER | 48.000₫ / 1 tháng | *Xem được các tài liệu của thành viên đăng*, *Xem và tải các tài liệu* |
| FUO VIP | 200.000₫ / 8 tháng | như Member + khác |
| FUO NOVA | 650.000₫ / 4 năm | như Vip + khác |

FUO Point **không** đổi được sang gói — trang nâng cấp chỉ nhận tiền.

### Đường vòng đã thử và loại

- **Ảnh thu nhỏ** `data.fuoverflow.com/attachments/...` tải được tự do, nhưng chỉ **400×150**.
  Câu ngắn thì đọc gắng gượng được, câu dài (có code, sơ đồ) thì mất chữ hoàn toàn.
  Vision OCR trả về rỗng, phóng to 4× vẫn rỗng. Không dùng làm ngân hàng câu hỏi được.
- Xem không đăng nhập: 403 y hệt.

## Đã lấy được (không cần gói)

- `out/KIEM_KE.md` — 22 đề gắn nhãn "Đề Thi FE" (FE + RE + TE), tổng **1.094 ảnh câu hỏi**.
- `anh/_meta/thumbs.tsv` — `đề · loại · số câu · id đính kèm · link ảnh thu nhỏ`, 1.094 dòng.
- `anh/_thao_luan/*.txt` — toàn văn 22 luồng.
- `out/dap_an_thanh_vien.json` — **đáp án tham khảo do thành viên chốt trong bài**, bóc từ
  văn bản: `sp24-fe` (50 câu), `su2023-te2` (50), `sp24-re` (45), `su2024-te2` (36).
  Người đăng ghi rõ "có thể sai" — chỉ dùng để đối chiếu, không phải nguồn chuẩn.

## Chạy tiếp khi đã có gói Member

```bash
python3 06_swe201c_fe/scripts/recv.py 8787          # máy thu ảnh, ghi vào anh/<đề>/
```

Mở fuoverflow.com trong tab đã đăng nhập → dán `scripts/tai_anh.js` vào console.
Theo dõi bằng `__JOB`. Xong thì:

```bash
06_swe201c_fe/scripts/bin/ocrde 06_swe201c_fe/anh/<đề>/*.jpg > 06_swe201c_fe/out/<đề>.txt
```

`scripts/bin/ocrde` là OCR bằng Vision framework của macOS — offline, không tốn quota AI.
Biên dịch lại: `swiftc -O -o scripts/bin/ocrde scripts/ocr_de.swift`.
