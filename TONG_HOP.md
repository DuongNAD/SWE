# TỔNG HỢP — SWE202c

Một file duy nhất: đề thi ra gì, ôn ở đâu, vào phòng thi mở cái nào.

---

# PHẦN I — ĐỀ THI RA GÌ

Đã OCR trực tiếp cả 5 file trong `papers/`. Cả 5 nhất quán: **đề thực hành trên EOS,
6 câu, 10 điểm**, có một case study dài (hệ thống phòng khám hoặc chuỗi cửa hàng).

| Câu | Yêu cầu | Điểm | Thời gian |
|---|---|---|---|
| 1 | Đồng ý/không với mô hình đề nêu (Kanban/XP/Scrum/Agile), liệt kê đặc trưng, **ghép từng cái với chi tiết trong đề** | **2.0** | 12ph |
| 2 | a) loại + cấp độ kiểm thử (0.7) · b) ai thực hiện, vì sao (0.3) | **1.0** | 5ph |
| 3 | Liệt kê **5 functional** + 3 và 2 loại phi chức năng *(loại nào tuỳ đề)* | **2.0** | 10ph |
| 4 | Viết **đúng 5 user story** suy ra từ câu 3 | **1.5** | 8ph |
| 5 | Mô tả chi tiết **2 design pattern** đã học trên lớp | **1.0** | 6ph |
| 6 | **Story map** theo định dạng text của EOS | **2.5** | 15ph |

**Câu 3 mỗi đề đòi một loại khác nhau** — phải đọc kỹ:
- paper (1), (4), paper.pdf → 3 **performance** + 2 **usability**
- paper (2), (3) → 3 **security** + 2 **scalability**

### ⚠️ Ba điều phải biết trước

**1. Đề trừ 0.1 điểm mỗi câu trả lời sai.** Hỏi 5 thì viết đúng 5. Viết thừa cho chắc
là mất điểm, không phải được thêm.

**2. Khoá học bạn mua dạy lệch với 5 đề này.** Khoá dạy Use Case Diagram, Class Diagram,
Use Case Specification, Test Case — không đề nào hỏi. Đối chiếu:

| Câu | Đề hỏi | Khoá học |
|---|---|---|
| 1 | Mô hình phát triển | ✅ b2 dạy đúng |
| 2 | Loại + cấp độ kiểm thử | ⚠️ b7 dạy *viết* test case, lệch hướng |
| 3 | Identify requirements | ⚠️ b4 chỉ dạy phần NFR |
| 4 | User stories | ❌ không dạy |
| 5 | Design patterns | ❌ không dạy |
| 6 | Story map | ❌ không dạy |

**5.0/10 điểm không có bài giảng nào chống lưng.** Tài liệu cho câu 4, 5, 6 dựng từ
chính đề thi và kiến thức nền, không phải từ khoá học.

**3. Hai câu chỉ bạn hỏi được:**
- Lớp bạn thi định dạng **6 câu** (như `papers/`) hay khác? Giảng viên trong video nói
  đề thật 5 câu, đề thử 7 câu — ba nguồn nói ba kiểu.
- Lớp dạy **design pattern nào**? Đề ghi rõ *"discussed in the courses"*.

---

# PHẦN II — VÀO PHÒNG THI MỞ CÁI NÀY

## → `page/DIEN_VAO_KHI_THI.txt`

Chỉ cần một file đó. Gồm khung điền tiếng Anh cho cả 6 câu, chú thích tiếng Việt ở
từng chỗ trống, bảng dấu hiệu nhận biết, và checklist rà 4 phút cuối.

**3 phút đầu — đừng bỏ:** đọc case study, ghi ra 5 thứ (tên hệ thống · các vai trò ·
câu về bảo mật · câu về hiệu năng/mở rộng · quy mô đội + deadline). Mọi câu sau đều
lấy từ đó, không bịa thứ đề không nói.

---

# PHẦN III — CHEAT SHEET 6 CÂU

## Câu 1 — Mô hình phát triển (2.0đ)

Phải làm **đủ 3 việc**, thiếu việc 3 là mất nửa điểm:
1. Nói rõ `I agree` / `I disagree`
2. Liệt kê principles + practices + characteristics của mô hình
3. **Ghép từng đặc trưng với một chi tiết cụ thể trong đề**

**Dấu hiệu → kết luận:**

| Trong đề | Chọn |
|---|---|
| requirements keep evolving / emerge and change incrementally | Agile, Kanban → ĐỒNG Ý |
| delivered and deployed continuously | Kanban → ĐỒNG Ý |
| highly skilled and experienced team | Kanban, XP → ĐỒNG Ý |
| green-field, cross-functional team, continuous feedback | Agile, XP → ĐỒNG Ý |
| first release in 2–3 months, full in 9–12 months | XP, Agile → ĐỒNG Ý |
| requirements fixed and fully known from the start | Waterfall |

**Mẫu câu:**
```
I agree with my manager's proposal to apply the <X> model to this project.
Because the project <chi tiết từ đề>, the <tên practice> practice is suitable,
as it allows the team to <lợi ích>.
Therefore, the <X> model is suitable for this project.
```

## Câu 2 — Kiểm thử (1.0đ)

⚠️ *"which **type** and level/stage"* là **HAI câu hỏi**. `type` = white-box/black-box.
`level` = unit → integration → system → acceptance. Chỉ liệt kê level là mất điểm.

| Đề mô tả | Nghĩa |
|---|---|
| focus on program structure | **white-box** |
| based on functional requirements | **black-box** |
| smallest unit level | Unit Testing |
| fully integrated system level | Integration → System |

**Phần (b) gần như không đổi giữa các đề — học thuộc:**
```
Unit Testing        → DEVELOPERS: they wrote the code and understand its internal structure.
Integration Testing → DEVELOPERS + TESTERS: it verifies interfaces between modules built by different people.
System Testing      → QA / TESTING TEAM: they are independent and test against the requirements objectively.
Acceptance Testing  → CUSTOMER / END USERS: only they can confirm it meets real business needs.
```

## Câu 3 — Requirements (2.0đ)

Đếm kỹ. Lấy **từ đề**, không tự nghĩ. Mỗi cái một câu `The system shall…` (hoặc `must`).

| Loại | Săn từ khoá này trong đề |
|---|---|
| Functional | record, scan, apply, issue, update, decrement, replenish, dispatch, reconcile, match, flag, trigger, monitor, configure |
| Security | authenticate, role-based, MFA, encrypt, TLS, AES, audit log, regulatory |
| Performance | within N seconds, under peak load, response time, 99.9% uptime, failover |
| Scalability | support N concurrent, scale horizontally, container orchestration, stateless, as the network grows |
| Usability | intuitive, simple to use, clean and consistent, clearly labeled, color coding |

**Mẫu câu:**
```
The system shall allow <ai> to <làm gì>.
The system shall automatically <làm gì> when <điều kiện>.
The system shall respond to <hành động> within <N> seconds under peak load.
The system shall encrypt <dữ liệu> using <chuẩn>.
The system shall support at least <N> concurrent <gì> without performance degradation.
```

## Câu 4 — User story (1.5đ)

Đúng **5 story**, suy từ câu 3, đủ **3 phần**:
```
As a <VAI TRÒ NGƯỜI>, I want to <LÀM GÌ>, so that <ĐỂ ĐƯỢC GÌ>.
```
⛔ **Không bao giờ viết `As a system`.** Chức năng tự động vẫn quy về người hưởng lợi:
`As a store manager, I want **the system to** send an alert, so that we never run out of stock.`

## Câu 5 — Design pattern (1.0đ)

Đúng **2 pattern**, mỗi cái **4 ý**: Purpose · How it works · Applying to this system · Benefit.

| Pattern | Bản chất | Gắn vào đâu |
|---|---|---|
| **Singleton** | chỉ tồn tại một thể hiện duy nhất | kết nối CSDL, quản lý cấu hình |
| **Observer** | một đối tượng đổi trạng thái → mọi đối tượng theo dõi được báo tự động | cảnh báo tồn kho thấp, thông báo, dashboard |
| **Factory** | tạo đối tượng mà không cần chỉ rõ lớp cụ thể | sinh nhiều loại báo cáo, nhiều loại thanh toán |

⚠️ Ba pattern trên là **phỏng đoán an toàn**, chưa xác minh lớp bạn dạy cái nào.

## Câu 6 — Story map (2.5đ, nặng nhất)

Định dạng text của EOS, **hai phần A và B**. Số hiệu story phải khớp số hiệu task.
```
A. Activities and User Tasks
1. <Activity — động từ + danh từ>
   • 1.1 <user task>
   • 1.2 <user task>
2. <Activity 2>
   • 2.1 <user task>

B. Releases
Release 1        ← việc TỐI THIỂU để hệ thống chạy được
   • 1.1.1 As a <vai trò>, I want to <…>, so that <…>
   • 2.1.1 As a <vai trò>, I want to <…>, so that <…>
Release 2        ← nâng cao, tự động hoá
   • 1.1.2 …
```
Activity = giai đoạn lớn, bám dòng chảy nghiệp vụ trong đề. Ví dụ "Manage Product Sales":
`1. Process Sales Transaction` → `2. Manage Inventory` → `3. Track Performance`.

---

# PHẦN IV — ÔN Ở ĐÂU

Đọc theo thứ tự này, không theo số câu. **Câu 3 → 4 → 6 chiếm 6/10 điểm** và nối liền
nhau: requirement ở câu 3 thành user story ở câu 4, rồi xếp vào release ở câu 6.

| # | File | Thời gian |
|---|---|---|
| 1 | `ON_TAP/TIENG_ANH.md` | 40ph |
| 2 | `ON_TAP/Q3_requirements.md` | 45ph |
| 3 | `ON_TAP/Q4_user_story.md` | 30ph |
| 4 | `ON_TAP/Q6_story_map.md` | 60ph |
| 5 | `ON_TAP/Q1_mo_hinh_phat_trien.md` | 45ph |
| 6 | `ON_TAP/Q2_kiem_thu.md` | 30ph |
| 7 | `ON_TAP/Q5_design_pattern.md` | 30ph |

Mỗi file 8 mục: dịch đề → **hiểu bản chất bằng ví dụ đời thường** → bảng so sánh Anh-Việt
→ cách làm từng bước → câu mẫu tiếng Anh → ví dụ đầy đủ → bẫy mất điểm → tự kiểm tra.

`ON_TAP/TIENG_ANH.md` là phần riêng cho người yếu tiếng Anh: 40 cụm từ đề hay dùng,
từ vựng xếp sẵn theo loại requirement, 6 mẫu câu, bảng lỗi ngữ pháp
(`shall to record` sai → `shall record` đúng).

---

# PHẦN V — HỆ THỐNG ĐÃ LÀM GÌ

**Số hoá 6,5 giờ khoá học** — 12 video → audio + 4.688 khung hình + 1.215 ảnh chuyển cảnh
→ transcript (Whisper large-v3) + OCR màn hình (Apple Vision) → 12 file `dossier.md`
(2,1 triệu ký tự, có timestamp) → 18 file JSON trích xuất → `03_kb/` (78 KB) → 6 khuôn làm bài.

Toàn bộ phần AI chạy bằng `agy` (Antigravity CLI), quota Antigravity.

## Đã kiểm chứng

**5/5 đề trong `papers/` đạt toàn bộ** kiểm thử tự động: đúng số lượng requirement theo
từng đề, đúng 5 user story đủ công thức, đúng 2 pattern, đúng định dạng story map,
số hiệu story khớp task, câu 2 nêu rõ white-box/black-box.

Đáng chú ý: khuôn **đọc được đề đòi loại requirement nào** — đề nào hỏi security+scalability
thì ra security+scalability, đề nào hỏi performance+usability thì đổi theo. Câu 1 cũng vậy,
đề hỏi Kanban thì biện luận Kanban, hỏi XP thì chuyển sang XP.

## Chưa kiểm chứng — đọc kỹ

- **5/5 chỉ chứng minh đúng cấu trúc, số lượng, định dạng.** Không chứng minh nội dung hay.
- Trong lúc chấm tôi phải sửa bộ chấm **6 lần**, và cả 6 lần "lỗi" hoá ra là lỗi của bộ chấm
  chứ không phải của bài làm. Đừng tin con số 5/5 hơn mức nó xứng đáng.
- Ba video chỉ trích ra 1 ví dụ mẫu dù tên gợi ý có nhiều đề hơn (`b3-3` = "Q2 đề số 2 **và 3**").
- `03_kb/cau_truc_de_thi.md` **đã lỗi thời** (lập từ video, ghi Q7 và "AI in Coding").
  Dùng bảng ở Phần I thay thế.

## Việc phải làm trước ngày thi

1. **Hỏi giảng viên lớp thi định dạng nào.** Mọi thứ ở đây dựng theo định dạng 6 câu.
2. **Hỏi lớp dạy design pattern nào.**
3. **Làm thử một đề trong `papers/`, bấm giờ 60 phút, không nhìn tài liệu.** Rồi so với
   `page/out/FINAL.md`.

---

# PHẦN VI — LỆNH

Có đề mới, muốn AI làm thử (3 lượt độc lập rồi hợp nhất):
```bash
# dán đề vào page/de.txt trước
bash scripts/98_thu_de.sh
```
Đọc mục `## CẦN NGƯỜI KIỂM TRA` trong `page/out/FINAL.md` **trước** khi đọc bài làm —
đó là chỗ ba lượt bất đồng, tức là chỗ AI đang đoán.

Kiểm lại toàn bộ khuôn sau khi sửa gì đó:
```bash
bash scripts/95_kiem_thu_hoi_quy.sh && python3 scripts/94_cham_hoi_quy.py
```

| File | Vai trò |
|---|---|
| `page/DIEN_VAO_KHI_THI.txt` | **mở cái này lúc thi** |
| `ON_TAP/` | 8 file ôn tập |
| `04_templates/` | khuôn cho AI làm bài |
| `03_kb/`, `02_extract/`, `01_raw/*/dossier.md` | dữ liệu gốc từ khoá học — **đừng xoá** |
| `BAN_GIAO.md` | báo cáo chi tiết hơn về rủi ro lệch định dạng đề |
