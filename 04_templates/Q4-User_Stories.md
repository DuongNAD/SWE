---
id: Q4
ten: User Stories
nguon_video: [] # Chưa có trong video
do_tin_cay: cao
thoi_gian_de_xuat: 10 phút
---

# NHẬN DIỆN
Đề thuộc câu này khi thấy:
- Từ khoá: `Write X user stories that are derived from your answers in Question 3`.
- Cấu trúc yêu cầu: Chuyển đổi các Functional Requirements (FR) từ Q3 thành cấu trúc User Story chuẩn.
- **Dễ nhầm với:** Tự bịa thêm chức năng mới. Bắt buộc phải lấy từ Q3.

# DỮ KIỆN CẦN MOI TỪ ĐỀ
| Biến | Lấy từ đâu trong đề | Ví dụ |
|---|---|---|
| `{{so_luong_US}}` | Câu 4 | 5 user stories |
| `{{danh_sach_FR_tu_Q3}}` | Câu 3 (Bài làm của mình) | 5 FRs đã viết ở trên |

# QUY TRÌNH (bám playbook, có nguồn)
1. Copy danh sách Functional Requirements (FR) đã làm ở Q3 xuống.
2. Với mỗi FR, xác định Actor (As a...), Action (I want to...), và Benefit/Goal (So that...). Nếu FR chưa rõ Benefit, tự thêm một lý do hợp lý dựa trên Case Study.
3. Chuyển thành cú pháp chuẩn: "As a [role], I want to [action] so that [benefit]."
4. Kiểm tra đúng số lượng đề yêu cầu.

# KHUNG ĐIỀN
> Phần này AI copy ra rồi thay `{{...}}`. Giữ nguyên định dạng, thứ tự, cách đánh số.

```
Here are {{so_luong_US}} user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a [Actor from FR1], I want to [Action from FR1] so that [Benefit/Reason derived from case study].
2. **User Story 2:** As a [Actor from FR2], I want to [Action from FR2] so that [Benefit/Reason derived from case study].
3. **User Story 3:** As a [Actor from FR3], I want to [Action from FR3] so that [Benefit/Reason derived from case study].
4. **User Story 4:** As a [Actor from FR4], I want to [Action from FR4] so that [Benefit/Reason derived from case study].
5. **User Story 5:** As a [Actor from FR5], I want to [Action from FR5] so that [Benefit/Reason derived from case study].
```

# VÍ DỤ ĐÃ ĐIỀN ĐẦY ĐỦ
**Đề:** Write 5 user stories that are derived from your answers in Question 3.
**Bài làm:**
```
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a Receptionist, I want to create a digital profile for patients storing their demographics and history, so that their medical records are centralized and easily accessible.
2. **User Story 2:** As a Nurse, I want to record vital signs (BP, temperature, HR, SpO2) into the system during consultation, so that doctors have accurate, real-time health data for diagnosis.
3. **User Story 3:** As a Doctor, I want to enter ICD-10 diagnoses and treatment plans through structured templates, so that prescriptions and lab orders can be issued accurately and efficiently.
4. **User Story 4:** As a Doctor (or Patient), I want the system to automatically link lab and imaging results to the patient record, so that I can immediately review critical values and alerts.
5. **User Story 5:** As an Administrator, I want to manage user roles, schedules, and fee structures, so that the clinic operates smoothly and staff have the correct access permissions.
```
*(nguồn: Chuyển đổi từ ví dụ FR ở Q3 - paper.pdf)*

# CHECKLIST TỰ CHẤM
- [ ] Đúng số lượng user stories đề yêu cầu.
- [ ] Tuân thủ chặt chẽ cú pháp: "As a [role], I want to [action] so that [benefit]."
- [ ] Nội dung map 1-1 với các Functional Requirements đã viết ở Câu 3.

# BẪY THƯỜNG GẶP
| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Thiếu vế "So that" (mục đích) | Mất 1/3 số điểm mỗi câu | Luôn luôn phải có "So that...". Nếu Case Study không ghi rõ thì tự bịa một lợi ích hợp lý. |
| Role bị chung chung (As a user) | Bị trừ điểm | Role phải rõ ràng: As a Doctor, As a Cashier, As a Customer... |
