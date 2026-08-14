---
id: Q6
ten: Story Map
nguon_video: [] # Không có trong video. Video dạy AI in coding.
do_tin_cay: cao
thoi_gian_de_xuat: 25 phút
---

# NHẬN DIỆN
Đề thuộc câu này khi thấy:
- Từ khoá: `Build a story map for the "X" activities`.
- Có hẳn một phần "III Notes" ở dưới hướng dẫn cách viết Story Map trên phần mềm EOS.
- Cấu trúc: A. Activities and User tasks, B. Releases.

# DỮ KIỆN CẦN MOI TỪ ĐỀ
| Biến | Lấy từ đâu trong đề | Ví dụ |
|---|---|---|
| `{{tieu_diem_chinh}}` | Câu 6 | "Manage Patient Appointments", "Manage Product Sales" |
| `{{cac_chuc_nang}}` | Case Study (lọc các ý liên quan đến tiêu điểm chính) | online booking, real-time availability, queue management, SMS reminders |

# QUY TRÌNH (bám playbook, có nguồn)
1. Đọc lại hướng dẫn trong "III Notes" của đề. Phải đúng format 2 phần: A và B.
2. Chia tiêu điểm chính (`{{tieu_diem_chinh}}`) thành 2-4 **Activities** lớn (ví dụ: Booking, Management, Notification).
3. Dưới mỗi Activity, list ra 2-4 **User Tasks**.
4. Chuyển sang Phần B (Releases). Thường chia làm 2-3 Releases.
5. Liệt kê các **User Stories** cụ thể cho từng User Task, nhét vào các Release tương ứng (Release 1 làm các chức năng cốt lõi, Release 2 làm chức năng nâng cao).
6. Tuân thủ tuyệt đối cách đánh số: Activity `1`, User Task `1.1`, User Story `1.1.1`.

# KHUNG ĐIỀN

> ⛔ **LUẬT SỐ 1 — kiểm tra trước khi viết bất kỳ story nào:**
> Mỗi dòng trong phần B phải bắt đầu bằng `As a <VAI TRÒ CON NGƯỜI>`.
> Vai trò hợp lệ: cashier, store manager, warehouse staff, customer, HQ admin,
> receptionist, doctor, nurse, pharmacist… — lấy từ danh sách actor trong đề.
> **`As a system` là SAI.** Chức năng chạy tự động vẫn phải quy về người hưởng lợi:
> `As a <người hưởng lợi>, I want the system to <hành động tự động>, so that <lợi ích>.`

> Phần này AI copy ra rồi thay `{{...}}`. Giữ nguyên định dạng, thứ tự, cách đánh số theo chuẩn EOS mà đề yêu cầu.

```
A. Activities and User tasks

1. <Activity 1 name>
   - 1.1 <User task 1 of activity 1>
   - 1.2 <User task 2 of activity 1>
2. <Activity 2 name>
   - 2.1 <User task 1 of activity 2>
   - 2.2 <User task 2 of activity 2>
3. <Activity 3 name>
   - 3.1 <User task 1 of activity 3>
   - 3.2 <User task 2 of activity 3>

B. Releases

Release 1----------------------------------------------------------------------
<List user stories for Release 1 - Core functionalities>
- 1.1.1 [User Story description, e.g., As a patient, I want to view available doctor slots]
- 1.2.1 [User Story description, e.g., As a patient, I want to book an appointment]
- 2.1.1 [User Story description...]
- 3.1.1 [User Story description...]

Release 2----------------------------------------------------------------------
<List user stories for Release 2 - Advanced/Enhancements>
- 1.1.2 [User Story description, e.g., As a patient, I want to filter doctors by specialty]
- 2.2.1 [User Story description, e.g., As a receptionist, I want to see a live wait-time estimate]
- 3.2.1 [User Story description, e.g., As a store manager, I want the system to send automated SMS reminders]
```

# VÍ DỤ ĐÃ ĐIỀN ĐẦY ĐỦ
**Đề:** Build a story map for the "Manage Patient Appointments" activities described in the project above. (2.5 points)
**Bài làm:**
```
A. Activities and User tasks

1. Book Appointments
   - 1.1 View Availability
   - 1.2 Schedule Appointment
2. Manage Queues
   - 2.1 Track Wait Times
   - 2.2 Route Patients
3. Handle Notifications
   - 3.1 Send Reminders
   - 3.2 Send Alerts

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a patient, I want to view doctor availability so I can find a time slot.
- 1.2.1 As a patient, I want to book an appointment online to secure a consultation.
- 2.1.1 As a receptionist, I want to track patient check-ins so I know who is waiting.
- 3.1.1 As a store manager, I want the system to send basic email reminders to patients 1 day before the visit.

Release 2----------------------------------------------------------------------
- 1.2.2 As a receptionist, I want to book an appointment at the front desk for walk-in patients.
- 2.1.2 As a patient, I want to see live wait-time estimates on the day of the visit so I can manage my time.
- 2.2.1 As a clinic manager, I want dynamic queue management to optimize patient flow.
- 3.1.2 As a store manager, I want the system to send automated SMS reminders for higher open rates.
```
*(nguồn: Phóng tác từ paper.pdf)*

# CHECKLIST TỰ CHẤM
- [ ] Tuân thủ format 2 phần: A (Activities and Tasks) và B (Releases).
- [ ] Đúng cấu trúc numbering (1.1, 1.1.1, v.v.).
- [ ] Viết user stories trong phần B phải đủ chủ ngữ (As a...) và bám sát các task ở phần A.

# BẪY THƯỜNG GẶP
| Lỗi | Hậu quả | Cách đánh |
|---|---|---|
| Vẽ bảng (table) hoặc dùng ascii art | Sai yêu cầu hệ thống thi EOS | Bắt buộc dùng đúng text list (danh sách) như mục III Notes của đề hướng dẫn. |
| User story ở phần B không tương ứng với User Task ở phần A | Bị trừ điểm logic | User story `X.Y.Z` BẮT BUỘC phải là triển khai của User task `X.Y`. |

# LUẬT BỔ SUNG (thêm sau khi chạy thử đề papers/paper (3).pdf)

**Cấm viết `As a system, I want to …`.** User story luôn viết từ góc nhìn con người
được hưởng lợi. Chức năng chạy tự động thì viết:
`As a <người hưởng lợi>, I want **the system to** <hành động tự động>, so that <lợi ích>.`

Ví dụ sai → đúng:
- ❌ `As a system, I want to decrement inventory in real time.`
- ✅ `As a store manager, I want the system to decrement inventory in real time, so that stock levels are always accurate.`
