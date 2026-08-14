---
id: Q5
ten: Design Patterns
nguon_video: [] # Không có trong video, video dạy Class Diagram
do_tin_cay: cao
thoi_gian_de_xuat: 15 phút
---

# NHẬN DIỆN
Đề thuộc câu này khi thấy:
- Từ khoá: `apply some design patterns`, `list and describe in detail two design patterns discussed in the courses`.
- Cấu trúc yêu cầu: Nêu tên 2 Design Patterns, mô tả chi tiết, và ứng dụng nó vào hệ thống trong Case Study.
- **Dễ nhầm với:** Đi vẽ Class Diagram như video ôn tập. KHÔNG VẼ.

# DỮ KIỆN CẦN MOI TỪ ĐỀ
| Biến | Lấy từ đâu trong đề | Ví dụ |
|---|---|---|
| `{{he_thong}}` | Case Study | Clinic Management System (CMS), Convenient Store Chain Management System |
| `{{tinh_nang_ap_dung}}` | Từ phân tích Case Study | Gửi alert (Observer), Tạo tài liệu (Factory), Xử lý State (State) |

# QUY TRÌNH (bám playbook, có nguồn)
1. Chọn 2 Design Patterns phổ biến nhất và dễ trình bày (VD: **Observer**, **Singleton**, **Factory Method**, hoặc **Strategy**).
2. Viết định nghĩa/mô tả chuẩn của pattern (dựa trên kiến thức SWE [NGOÀI-KHOÁ]).
3. Trình bày cách áp dụng pattern đó vào Case Study của đề. (Phần này ăn điểm).

# KHUNG ĐIỀN
> Phần này AI copy ra rồi thay `{{...}}`. Giữ nguyên định dạng, thứ tự, cách đánh số.

```
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: {{pattern_1_name}}**
- **Description:** [Định nghĩa lý thuyết chuẩn về pattern, vd: "The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically."]
- **Application to the system:** In this {{he_thong}}, this pattern can be applied to [Mô tả tính năng trong đề, vd: "send real-time alerts or notifications"]. For example, when [Sự kiện A xảy ra], the [Chủ thể/Subject] notifies all [Các thành phần nhận/Observers] like [Thành phần 1, Thành phần 2] so they can react accordingly without tight coupling.

2. **Design Pattern 2: {{pattern_2_name}}**
- **Description:** [Định nghĩa lý thuyết chuẩn về pattern, vd: "The Singleton pattern ensures that a class has only one instance and provides a global point of access to it."]
- **Application to the system:** In this {{he_thong}}, this pattern can be used for [Mô tả tính năng, vd: "managing the connection to the central database or configuration settings"]. Since the system [Lý do từ đề, vd: "needs to keep a tamper-evident audit log of every transaction"], a Singleton AuditLogger ensures that all logs are written sequentially to a single centralized file or stream, preventing resource conflicts.
```

# VÍ DỤ ĐÃ ĐIỀN ĐẦY ĐỦ
**Đề:** The manager asks you to apply some design patterns to the software system. Please list and describe in detail two design patterns discussed in the courses (1.0 points).
**Bài làm:**
```
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be applied to the real-time notification system. For example, when "critical values trigger immediate alerts" (as stated in the case study), the Patient Record (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the Doctor's Dashboard and the Nursing Station Alert System, ensuring rapid response without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CMS, the Singleton pattern can be used for the system's Configuration Manager or Database Connection Pool. Since the system must "cope with peak transaction volumes without performance degradation," a Singleton Connection Pool ensures that the application reuses a single, managed set of database connections, preventing memory exhaustion and ensuring consistent data access across all clinical modules.
```
*(nguồn: Tự viết, dựa vào đề paper.pdf)*

# CHECKLIST TỰ CHẤM
- [ ] Chọn đúng 2 patterns.
- [ ] Có phần mô tả lý thuyết chung (Description).
- [ ] Có phần Áp dụng (Application) dính chặt với ngữ cảnh/dữ kiện của Case Study.

# BẪY THƯỜNG GẶP
| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Chỉ nêu lý thuyết mà không áp dụng vào dự án | Trừ nửa điểm phần đó | Bắt buộc phải có đoạn "In this system, this pattern can be applied to..." |
| Vẽ Class Diagram | Lạc đề, phí thời gian | Đề yêu cầu "list and describe", KHÔNG yêu cầu "draw". |
