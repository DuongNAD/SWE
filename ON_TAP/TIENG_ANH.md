# Tiếng Anh cho bài thi SWE202c

Bạn **không cần giỏi tiếng Anh** để làm được bài này. Đề thi chỉ dùng đi dùng lại
khoảng 40 cụm từ, và bài làm chỉ cần 6 mẫu câu. Học đúng chỗ đó là đủ 10 điểm.

Tài liệu này chia làm 3 phần: **đọc hiểu đề** → **viết đáp án** → **lỗi hay mắc**.

---

## PHẦN 1 — ĐỌC HIỂU ĐỀ

### 1.1 Câu lệnh trong đề (bắt buộc thuộc — hiểu sai là làm lạc đề)

| Tiếng Anh | Nghĩa | Nó bắt bạn làm gì |
|---|---|---|
| **identify and list** | xác định và liệt kê | Chỉ cần liệt kê, KHÔNG cần giải thích dài |
| **describe in detail** | mô tả chi tiết | Phải giải thích nhiều ý, liệt kê tên là mất điểm |
| **list and explain** | liệt kê và giải thích | Mỗi mục nêu tên **và** một câu giải thích |
| **justify your answer** | biện luận cho câu trả lời | Phải nói **VÌ SAO**, dựa vào chi tiết trong đề |
| **match each of them to** | ghép từng cái với | Nối 1-1: mỗi đặc trưng ↔ một chi tiết trong đề |
| **derived from** | suy ra từ | Phải lấy từ câu trước, không được nghĩ cái mới |
| **based on** | dựa trên | Như trên |
| **Do you agree or disagree?** | bạn đồng ý hay không? | Phải nói rõ **I agree** hoặc **I disagree** ngay câu đầu |
| **who carries out / who performs** | ai thực hiện | Trả lời bằng chức danh: developer, tester, customer |
| **the best fit for that role** | phù hợp nhất với vai trò đó | Phải nêu lý do vì sao người đó hợp |
| **Build a story map for…** | dựng story map cho… | Theo đúng định dạng ở phần III Notes |
| **at least** | ít nhất | Con số tối thiểu |
| **without performance degradation** | không bị giảm hiệu năng | Đây là **scalability/performance requirement** |

### 1.2 Từ khoá trong Case Study → thuộc loại requirement nào

Đây là kỹ năng ăn điểm câu 3. Đọc case study, thấy từ nào thì xếp vào nhóm đó ngay.

**FUNCTIONAL — hệ thống LÀM GÌ.** Nhận ra bằng động từ:

| Từ | Nghĩa |
|---|---|
| record / log | ghi nhận, lưu lại |
| scan | quét (mã vạch) |
| apply | áp dụng (khuyến mãi, quy tắc) |
| issue | phát hành (hoá đơn, đơn thuốc) |
| update | cập nhật |
| decrement | trừ đi, giảm xuống |
| replenish / replenishment | bổ sung hàng |
| dispatch | gửi đi, điều phối |
| reconcile | đối soát, khớp sổ |
| match … against … | đối chiếu … với … |
| flag | đánh dấu (để xem lại) |
| trigger | kích hoạt, làm bật lên |
| monitor / track | theo dõi |
| configure | cấu hình, thiết lập |
| onboard | đưa vào hệ thống |

**SECURITY — bảo mật:**

| Từ | Nghĩa |
|---|---|
| authenticate | xác thực danh tính |
| role-based credentials | thông tin đăng nhập theo vai trò |
| multi-factor authentication (MFA) | xác thực nhiều lớp |
| encrypt / encryption | mã hoá |
| in transit / at rest | đang truyền / đang lưu trữ |
| TLS 1.3, AES-256 | tên các chuẩn mã hoá |
| tamper-evident audit log | nhật ký không thể sửa lén |
| regulatory requirements | yêu cầu pháp lý |

**PERFORMANCE — hiệu năng.** Luôn có **con số + đơn vị thời gian**:

| Cụm | Nghĩa |
|---|---|
| respond within 2 seconds | phản hồi trong vòng 2 giây |
| under peak load | khi tải cao điểm |
| response time | thời gian phản hồi |
| 99.9% uptime | thời gian hoạt động 99,9% |
| automated failover | tự động chuyển dự phòng khi hỏng |

**SCALABILITY — khả năng mở rộng:**

| Cụm | Nghĩa |
|---|---|
| support N concurrent sessions | chịu được N phiên cùng lúc |
| scale horizontally | mở rộng theo chiều ngang (thêm máy) |
| container orchestration | điều phối container |
| stateless and versioned | không lưu trạng thái, có đánh phiên bản |
| without manual infrastructure changes | không cần sửa hạ tầng thủ công |

**USABILITY — dễ dùng:**

| Cụm | Nghĩa |
|---|---|
| intuitive / simple to use | trực quan / dễ dùng |
| clean and consistent interface | giao diện gọn và nhất quán |
| clearly labeled navigation | điều hướng có nhãn rõ ràng |
| color coding | mã hoá bằng màu sắc |
| limited technical experience | ít kinh nghiệm kỹ thuật |

### 1.3 Từ báo hiệu chọn mô hình phát triển (câu 1)

| Cụm trong đề | Nghĩa | Kết luận |
|---|---|---|
| requirements keep evolving | yêu cầu thay đổi liên tục | → Agile / Kanban |
| emerge and change incrementally | phát sinh và đổi dần dần | → Agile / Kanban |
| delivered and deployed continuously | bàn giao và triển khai liên tục | → Kanban |
| green-field project | dự án làm mới từ đầu | → Agile |
| cross-functional team | đội đa chức năng | → Agile / Scrum |
| continuous feedback | phản hồi liên tục | → Agile |
| highly skilled and experienced | đội giỏi, nhiều kinh nghiệm | → Kanban hợp |
| requirements are fixed / fully known | yêu cầu cố định, biết hết từ đầu | → Waterfall |

---

## PHẦN 2 — VIẾT ĐÁP ÁN

Cả bài thi chỉ cần **6 mẫu câu**. Học thuộc 6 cái này là viết được toàn bộ.

### Mẫu 1 — Requirement (câu 3)
```
The system shall + ĐỘNG TỪ NGUYÊN THỂ + phần còn lại.
```
- `The system shall record every transaction at the POS terminal.`
  = Hệ thống phải ghi nhận mọi giao dịch tại máy tính tiền.
- `The system shall encrypt all data at rest using AES-256.`

> **shall** = "phải", dùng trong tài liệu kỹ thuật. Sau `shall` là động từ **nguyên thể
> không "to"**. Viết `shall to record` là SAI.

### Mẫu 2 — User story (câu 4)
```
As a <VAI TRÒ>, I want to <LÀM GÌ>, so that <ĐỂ ĐƯỢC GÌ>.
```
- `As a cashier, I want to scan products at the POS terminal, so that customers
  can check out quickly.`
  = Với vai trò thu ngân, tôi muốn quét sản phẩm ở máy tính tiền, để khách thanh
  toán nhanh.

> Sau `I want to` là động từ nguyên thể. Sau `so that` là **một mệnh đề đầy đủ**
> (có chủ ngữ + động từ), thường dùng `can` / `will be able to`.

### Mẫu 3 — Biện luận (câu 1)
```
Because the project <ĐẶC ĐIỂM LẤY TỪ ĐỀ>, the <TÊN> practice is suitable,
as it allows the team to <LỢI ÍCH>.
```
- `Because the project requirements emerge and change incrementally, the
  continuous delivery practice is suitable, as it allows the team to release
  features as soon as they are ready.`

### Mẫu 4 — Ai làm kiểm thử (câu 2b)
```
<CẤP ĐỘ> is carried out by <AI>, because they <LÝ DO>.
```
- `Unit testing is carried out by the developers, because they wrote the code and
  understand its internal structure.`

### Mẫu 5 — Mô tả design pattern (câu 5)
```
The <TÊN> pattern <ĐỊNH NGHĨA>. In this project, it can be used to <ÁP DỤNG>.
This makes the system <LỢI ÍCH>.
```
- `The Observer pattern defines a one-to-many dependency so that when one object
  changes state, all its dependents are notified automatically. In this project,
  it can be used to notify the store manager when stock falls below the
  threshold. This makes the system more maintainable and loosely coupled.`

### Mẫu 6 — Kết luận
```
Therefore, the <X> model is suitable for this project.
```

### Từ nối nên dùng (viết trôi hơn, không cần từ khó)

| Từ | Nghĩa | Dùng khi |
|---|---|---|
| Because / Since | Bởi vì | Nêu lý do |
| Therefore / Thus | Do đó | Kết luận |
| In addition / Moreover | Ngoài ra | Thêm ý |
| However / In contrast | Tuy nhiên / Ngược lại | Nêu ý trái chiều |
| For example | Ví dụ | Đưa ví dụ |
| This means that | Điều này nghĩa là | Giải thích thêm |

---

## PHẦN 3 — LỖI HAY MẮC

| Sai | Đúng | Vì sao |
|---|---|---|
| The system shall **to** record… | The system shall **record**… | sau `shall` là động từ nguyên thể, không có `to` |
| The system shall **records**… | The system shall **record**… | sau `shall` không chia ngôi |
| I want **scan** products | I want **to scan** products | sau `want` phải có `to` |
| so that customers **checking out** | so that customers **can check out** | sau `so that` cần mệnh đề đầy đủ |
| allow the manager **view** reports | allow the manager **to view** reports | `allow somebody **to** do` |
| The system shall **be** encrypt data | The system shall **encrypt** data | thừa `be` |
| Developers **is** carried out… | Unit testing **is** carried out **by developers** | câu bị động: việc bị làm, không phải người |
| 5 **requirement** | 5 **requirements** | danh từ đếm được, số nhiều thêm `s` |
| **Datas** | **Data** | `data` không có dạng số nhiều |

**Ba từ dễ nhầm:**
- `requirement` (yêu cầu) ≠ `requirements specification` (bản đặc tả yêu cầu)
- `test case` (ca kiểm thử) ≠ `testing` (việc kiểm thử) ≠ `tester` (người kiểm thử)
- `stage` = `level` = cấp độ. Đề dùng lẫn lộn hai từ này, cùng nghĩa.

---

## LUYỆN 20 PHÚT MỖI NGÀY

**Ngày 1–2 — đọc hiểu.** Mở `page/de.txt`, đọc case study, gạch chân mọi từ ở
Phần 1.2. Tự phân loại vào functional / security / performance / scalability.
Chưa cần viết gì.

**Ngày 3–4 — chép mẫu.** Lấy 5 requirement bạn vừa tìm, viết lại bằng mẫu
`The system shall…`. Chép tay, đừng gõ.

**Ngày 5 — user story.** Đổi 5 requirement đó thành 5 user story bằng mẫu 2.

**Ngày 6 — câu 1 và câu 2.** Học thuộc khối phần (b) câu 2 trong
`page/DIEN_VAO_KHI_THI.txt` — nó gần như không đổi giữa các đề, thuộc là ăn 0.3 điểm.

**Ngày 7 — làm nguyên một đề** trong `papers/`, bấm giờ, không nhìn tài liệu.
Xong so với `page/out/FINAL.md`.

> Mẹo: **không cần viết hay, chỉ cần viết đúng mẫu.** Người chấm tìm đúng cấu trúc
> và đúng nội dung lấy từ đề. Câu văn đơn giản, đúng ngữ pháp, đúng số lượng —
> đó là bài 10 điểm.
