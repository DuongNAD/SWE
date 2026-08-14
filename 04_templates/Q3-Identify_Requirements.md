---
id: Q3
ten: Identify Requirements
nguon_video: [b4] # NFRs, mở rộng thêm FRs
do_tin_cay: cao
thoi_gian_de_xuat: 15 phút
---

# NHẬN DIỆN
Đề thuộc câu này khi thấy:
- Từ khoá: `identify and list: X functional requirements, Y performance requirements, Z usability requirements`.
- Cấu trúc yêu cầu: Bắt liệt kê chính xác số lượng FRs và NFRs (Performance, Security, Usability, Scalability, v.v.).
- **Dễ nhầm với:** Tự bịa ra yêu cầu. Phải lấy từ Case Study.

# DỮ KIỆN CẦN MOI TỪ ĐỀ
| Biến | Lấy từ đâu trong đề | Ví dụ |
|---|---|---|
| `{{so_luong_FR}}` | Câu 3 | 5 functional requirements |
| `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}` | Câu 3 | 3 performance requirements / security requirements |
| `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}` | Câu 3 | 2 usability requirements / scalability requirements |

# QUY TRÌNH (bám playbook, có nguồn)
1. Quét Case Study để tìm các chức năng (việc user làm) -> Đưa vào Functional Requirements (FRs).
2. Quét Case Study để tìm các ràng buộc (thời gian phản hồi, tải trọng, MFA, mã hoá, UI thân thiện) -> Đưa vào Non-Functional Requirements tương ứng.
3. Đảm bảo trích xuất ĐÚNG SỐ LƯỢNG mà đề yêu cầu, không thừa không thiếu.

# KHUNG ĐIỀN
> Phần này AI copy ra rồi thay `{{...}}`. Giữ nguyên định dạng, thứ tự, cách đánh số.

```
Based on the project description, here are the identified requirements:

**Functional Requirements ({{so_luong_FR}}):**
1. [FR1: Actor + Action + Object, e.g., "The system must allow Receptionists to create a digital profile for patients."]
2. [FR2: Actor + Action + Object]
3. [FR3: Actor + Action + Object]
4. [FR4: Actor + Action + Object]
5. [FR5: System + Action, e.g., "The system must send automatic SMS/email reminders."]

**{{loai_NFR_1}} Requirements ({{so_luong_NFR_1}}):**
1. [NFR1: trích xuất cụm từ trong đề, e.g., "The interface should be clean and consistent, with clearly labeled navigation."]
2. [NFR2: trích xuất từ đề, e.g., "Color coding must be applied meaningfully — green to confirm actions, red for errors."]
3. [NFR3: ...]

**{{loai_NFR_2}} Requirements ({{so_luong_NFR_2}}):**
1. [NFR1: trích xuất từ đề, e.g., "The system shall respond to user interactions within 2 seconds."]
2. [NFR2: trích xuất từ đề, e.g., "The system must cope with peak transaction volumes without performance degradation during morning rush hours."]
```

# VÍ DỤ ĐÃ ĐIỀN ĐẦY ĐỦ
**Đề:** identify and list: 5 functional requirements, 3 performance requirements, and 2 usability requirements (dựa trên Case Study Y tế).
**Bài làm:**
```
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. Receptionists or patients must be able to create a digital profile that stores demographics and medical history.
2. Nurses must be able to record vital signs (BP, temperature, HR, SpO2) during consultation.
3. Doctors must be able to enter ICD-10 diagnoses and treatment plans through structured templates.
4. The system must automatically link lab and imaging results to the patient record.
5. The system must allow administrators to manage user roles (RBAC), schedules, and fee structures.

**Performance Requirements (3):**
1. The system must cope with peak transaction volumes without performance degradation during morning rush hours.
2. Under normal operating load, the system shall respond to user interactions (page loading, form submission, search) within 2 seconds.
3. The system shall scale horizontally to support a growing number of patients and staff users without service interruption.

**Usability Requirements (2):**
1. The CMS has to be intuitive and simple to use, even for clinical staff with limited technical experience.
2. Color coding must be applied meaningfully — green to confirm actions, red for errors or critical alerts.
```
*(nguồn: Trích xuất từ paper.pdf)*

# CHECKLIST TỰ CHẤM
- [ ] Đúng số lượng FRs đề yêu cầu.
- [ ] Đúng số lượng NFRs cho mỗi loại (Performance/Security/Usability/Scalability).
- [ ] Tất cả các requirement đều lấy ý từ đoạn văn Case Study, không tự bịa (không hallucinate).

# BẪY THƯỜNG GẶP
| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Liệt kê thừa hoặc thiếu số lượng | Mất điểm nhỏ lẻ | Đếm cẩn thận trước khi nộp. |
| Tự nghĩ ra requirement hợp lý nhưng không có trong đề | Mất điểm hoàn toàn cho ý đó | Tìm chính xác cụm từ / câu trong Case Study tương ứng với NFR hoặc FR. |
