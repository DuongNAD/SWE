# DANH SÁCH TEMPLATE CHO KÌ THI THỰC HÀNH SWE

Dưới đây là bảng định tuyến dựa trên cấu trúc đề thi **thực tế** (đã đối chiếu và điều chỉnh so với bài giảng video). Lấy các file `Q<n>.md` tương ứng để giải bài.

| Câu trong đề | Dấu hiệu nhận biết trong đề | → Khuôn (File) | Thời gian nên dành | Bẫy chính |
|---|---|---|---|---|
| **Q1** | `XP framework`, `Kanban model`, `manager suggests applying...` | `Q1-Software_Development_Model.md` | 15 phút | Quên match lý thuyết với dữ kiện dự án (Case Study). |
| **Q2** | `type and level/stage of testing`, `smallest unit level up to fully integrated` | `Q2-Testing.md` | 10 phút | Nhầm sang viết Test Case, trong khi đây là câu hỏi lý thuyết 4 mức độ test. |
| **Q3** | `identify and list: X functional requirements, Y performance...` | `Q3-Identify_Requirements.md` | 15 phút | Bịa thêm requirement thay vì trích xuất từ văn bản Case Study. |
| **Q4** | `Write X user stories that are derived from your answers in Question 3` | `Q4-User_Stories.md` | 10 phút | Quên vế "so that" (lợi ích/mục đích) trong User Story. |
| **Q5** | `apply some design patterns`, `list and describe in detail two design patterns` | `Q5-Design_Patterns.md` | 15 phút | Chỉ nêu lý thuyết chay mà không có đoạn áp dụng vào Case Study. |
| **Q6** | `Build a story map`, `Activities and User tasks`, `Releases` | `Q6-Story_Map.md` | 25 phút | Đánh số thứ tự lộn xộn, hoặc dùng bảng thay vì list text thuần tuý theo chuẩn EOS. |

---

## ⚠️ NẾU ĐỀ KHÔNG KHỚP KHUÔN NÀO BÊN TRÊN
Trường hợp gặp câu hỏi lạ (không giống cấu trúc 6 câu trên), quy trình dự phòng:

1. **Nhận dạng nhanh:** Đọc kỹ từ khóa (liên quan đến Use Case Diagram? Class Diagram? Test Case?). Nếu giống các dạng trong `03_kb/` mà chưa có trong danh sách trên, lục lại kiến thức ở `03_kb/` để lấy format. (Khả năng này thấp vì đề chuẩn đã thay đổi).
2. **Tuân thủ Format:** Luôn làm theo yêu cầu trực tiếp của câu hỏi. Nếu đề bắt liệt kê (List) thì gạch đầu dòng. Nếu đề bắt lý giải (Justify) thì phải có trích dẫn từ Case Study.
3. **Sử dụng Playbook chung:** 
   - Đọc kỹ Case Study.
   - Chia nhỏ yêu cầu.
   - Giải quyết tuần tự.
   - Luôn ưu tiên dùng thông tin từ đề, hạn chế kiến thức ngoại vi tự sáng tác (trừ lý thuyết nền).

## LỖ HỔNG (So với video bài giảng)
Cấu trúc đề thật **khác biệt hoàn toàn** so với video ôn tập. AI cần bám sát các Template mới này, bỏ qua các template cũ nếu có xung đột:
- **Video dạy:** Use Case Diagram, Use Case Specification, Class Diagram, Vẽ vời UML.
- **Đề thật hỏi:** Lý thuyết Testing, phân tích Requirements (FR, NFR), Design Patterns, Text-based Story Map. (Gần như không có vẽ sơ đồ đồ hoạ phức tạp trên giấy/UML).
