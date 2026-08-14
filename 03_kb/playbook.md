# PLAYBOOK: QUY TRÌNH LÀM BÀI

## General
(tonghop @ 01:00) Bước 1: Lập Kế Hoạch Dự Án (Đặt Nền Móng)
   - Thực hiện: Xác định phạm vi dự án, đặt ra các cột mốc quan trọng để quản lý tiến độ, chọn quy trình phát triển có cấu trúc (Incremental hoặc Iterative) để phân chia công việc.
   - Input: Yêu cầu tổng quan về phần mềm cần xây dựng
   - Output: Kế hoạch dự án, phạm vi, cột mốc tiến độ và quy trình phát triển

(tonghop @ 02:00) Bước 2: Thiết Kế Sơ Đồ Hệ Thống (Tạo Bản Thiết Kế Kiến Trúc)
   - Thực hiện: Mô hình hóa hệ thống bằng ngôn ngữ đặc biệt: tạo kịch bản Use Case (mô tả chức năng từ góc nhìn người dùng gồm Actor, Flow of Events, Preconditions, Yêu cầu phi chức năng) và Class (bản mô tả nhóm đối tượng có chung thuộc tính, thao tác, mối quan hệ và ngữ nghĩa).
   - Input: Yêu cầu chức năng và phạm vi hệ thống
   - Output: Bản thiết kế kiến trúc hệ thống (Use Case, Class Diagram)

(tonghop @ 03:30) Bước 3: Xây Dựng và Kiểm Thử (Thi Công và Giám Sát)
   - Thực hiện: Lập trình xây dựng hệ thống song song với kiểm tra và giám sát chất lượng; thực hiện kiểm thử đi săn lùng sai sót qua hai công đoạn: Verification (kiểm tra xây đúng theo bản thiết kế) và Validation (kiểm tra xây đúng sản phẩm khách hàng muốn).
   - Input: Bản thiết kế hệ thống và mã nguồn
   - Output: Sản phẩm phần mềm được kiểm thử, thẩm tra và thẩm định đầy đủ

(tonghop @ 05:00) Bước 4: Hỗ Trợ Phát Triển Bằng AI (Kỷ Nguyên Mới Của AI)
   - Thực hiện: Sử dụng AI tự động viết mã lặp đi lặp lại, dọn dẹp mã phức tạp, giải thích logic khó, rà soát mã tìm lỗi và lỗ hổng bảo mật. Luôn phải rà soát và kiểm tra lại mã do AI sinh ra.
   - Input: Yêu cầu sinh mã, tối ưu mã hoặc rà soát lỗi
   - Output: Mã nguồn được tối ưu/hỗ trợ bởi AI đã qua con người kiểm duyệt

(tonghop @ 06:00) Bước 5: Chuyển Đổi Số & Đạo Đức
   - Thực hiện: Tích hợp công nghệ vào toàn bộ doanh nghiệp dựa trên 4 trụ cột (Công nghệ, Dữ liệu, Quy trình, Quản lý thay đổi), đồng thời quản lý rủi ro đạo đức (tin giả, deepfake, thành kiến, quyền riêng tư dữ liệu, bản quyền).
   - Input: Mục tiêu chuyển đổi doanh nghiệp và ứng dụng phần mềm/AI
   - Output: Hệ thống vận hành doanh nghiệp tạo giá trị mới gắn với trách nhiệm đạo đức

(tonghop @ 03:00) [MẸO] Phân biệt Use Case và Class: Use Case là động từ (hành động), Class là danh từ (đối tượng trong hệ thống).

(tonghop @ 04:00) [MẸO] Phân biệt Verification và Validation: Verification là 'xây đúng thiết kế?', Validation là 'xây đúng cái khách hàng cần?'.

(tonghop @ 06:00) [MẸO] Ghi nhớ 4 trụ cột Chuyển đổi số đóng góp đồng đều 25% mỗi trụ cột: Công nghệ, Dữ liệu, Quy trình, Quản lý thay đổi.

## Q1
(b2 @ 05:30) Bước 1: Scan case study để trích xuất từ khóa (Keywords Extraction)
   - Thực hiện: Đọc nhanh văn bản case study trong đề thi để xác định 5 loại dữ kiện: (1) Tên hệ thống (ví dụ: Course Registration System - CRS); (2) Quy trình thủ công/cũ đang dùng (ví dụ: paper-based manual process, enter data into spreadsheets); (3) Danh sách các nhóm người dùng (ví dụ: Students, Lecturers, Academic Staff, System Administrator); (4) Các ràng buộc/rủi ro kỹ thuật (ví dụ: handle 1,000 concurrent users with response time < 3s, TLS 1.2+ encryption, RBAC model); (5) Quy mô và tên tổ chức (ví dụ: 8,000 students, Green University).
   - Input: Đoạn văn bản Case Study trong đề thi.
   - Output: Danh sách các từ khóa (keywords) chính xác để điền vào template.

(b2 @ 04:00) Bước 2: Viết lời giải Question 1.1 (Lựa chọn và biện chứng mô hình Agile)
   - Thực hiện: Áp dụng khung trả lời mẫu (template) cho Question 1.1. Đưa ra đề xuất chọn Agile (Scrum). Lần lượt trình bày lập luận theo 4 tiêu chí bắt buộc của đề: (1) Requirements stability at the outset (đối chiếu quy trình cũ với yêu cầu UI/UX mới); (2) Iterative delivery and stakeholder feedback (liệt kê các nhóm user và chu kỳ sprint 2-4 tuần); (3) Technical risk factors (liệt kê rủi ro chịu tải và bảo mật, giải thích cách Agile dùng MVP thử nghiệm sớm); (4) Team size, duration and change-control process (nêu quy mô sinh viên/tổ chức và cơ chế Sprint Review/Planning). Thay các từ khóa đã scan từ Bước 1 vào các vị trí placeholder <...>.
   - Input: Các từ khóa đã scan + Khung template Question 1.1.
   - Output: Đoạn văn hoàn chỉnh trả lời Question 1.1 (1.0 điểm).

(b2 @ 05:00) Bước 3: Viết lời giải Question 1.2 (So sánh mô hình thay thế Waterfall)
   - Thực hiện: Chọn Waterfall Model làm mô hình thay thế. Lập bảng/danh sách so sánh đối chiếu giữa Agile (Scrum) và Waterfall. Trình bày chính xác 2 ưu điểm (Advantages) và 2 nhược điểm (Disadvantages) cho Agile, và 2 ưu điểm, 2 nhược điểm cho Waterfall. Trong từng ý so sánh, lồng ghép trực tiếp tên hệ thống, nhóm user, tên tổ chức và chỉ số rủi ro chịu tải từ case study vào các vị trí placeholder <...>.
   - Input: Khung template Question 1.2 + Các từ khóa từ case study.
   - Output: Đoạn văn so sánh hoàn chỉnh trả lời Question 1.2 (1.0 điểm).

(b2 @ 17:30) Bước 4: Chấm điểm tự động và đối chiếu bằng AI
   - Thực hiện: Sao chép bài làm đã hoàn thiện, truy cập vào công cụ chấm điểm AI (TQMaster / web q6swe202), dán Groq API key và bài làm vào ô luyện tập để AI chấm điểm chi tiết và hiển thị đáp án mẫu đối chiếu.
   - Input: Bài làm hoàn chỉnh + Groq API Key.
   - Output: Kết quả chấm điểm chi tiết và đáp án mẫu chuẩn.

(b2 @ 05:30) [MẸO] Kỹ thuật scan đề nhanh: Tìm ngay Tên hệ thống (Course Registration System), Quy trình cũ (paper-based / spreadsheets), Nhóm người dùng (Students, Lecturers, Academic Staff, System Admin), Thông số kĩ thuật/Rủi ro (1,000 concurrent users < 3s, TLS 1.2+, RBAC), và Quy mô/Tên trường (8,000 students, Green University).

(b2 @ 06:30) [MẸO] Học thuộc hoặc chuẩn bị sẵn khung template chuẩn cho Question 1. Vào phòng thi chỉ cần copy template và điền/thay thế keyword từ đề bài vào các vị trí `<...>`.

(b2 @ 17:30) [MẸO] Sử dụng công cụ chấm điểm AI trên website q6swe202 kết hợp Groq API key để dán bài làm và chấm điểm thử trước khi thi.

## Q2
(capcuu @ 04:30) Bước 1: Tạo System Boundary và điền tên hệ thống
   - Thực hiện: Kéo khối System Boundary ra canvas trong phần mềm vẽ (Visual Paradigm, StarUML...), điền chính xác tên hệ thống từ đề bài vào phần tiêu đề của khối Boundary.
   - Input: Tên hệ thống trong đề bài.
   - Output: Khối System Boundary với tiêu đề tên hệ thống.

(capcuu @ 05:30) Bước 2: Xác định và tạo các Actor (Tác nhân)
   - Thực hiện: Đọc đoạn Đối tượng người dùng (User Groups) để tìm Primary Actors và Secondary Actors.
   - Input: Đoạn văn mô tả User Groups trong case study.
   - Output: Các Actor đặt phía ngoài khối System Boundary.

(capcuu @ 10:30) Bước 3: Trích xuất và tạo các Use Case (Chức năng)
   - Thực hiện: Đọc từng câu mô tả yêu cầu chức năng của từng nhóm người dùng. Đặt tên Use Case theo cấu trúc ĐỘNG TỪ + DANH TỪ.
   - Input: Các câu mô tả chức năng của người dùng.
   - Output: Các elip Use Case nằm bên trong System Boundary.

(capcuu @ 23:30) Bước 4: Nối quan hệ Association giữa Actor và Use Case
   - Thực hiện: Sử dụng đường nối Association nối từng Actor với các Use Case.
   - Input: Mối liên hệ giữa Actor và chức năng tương ứng.
   - Output: Các đường nối Association hoàn chỉnh.

(capcuu @ 25:00) Bước 5: Xác định và vẽ mối quan hệ Include và Extend
   - Thực hiện: Tìm các chức năng bắt buộc đi kèm (Include) và tùy chọn (Extend). Vẽ đường nét đứt <<include>> (trỏ tới phụ thuộc) và <<extend>> (trỏ VỀ gốc).
   - Input: Logic phụ thuộc giữa các Use Case.
   - Output: Các đường nét đứt <<include>> và <<extend>> với đúng chiều mũi tên.

(capcuu @ 32:00) Bước 6: Hoàn thiện sơ đồ và lập bảng mô tả
   - Thực hiện: Chụp ảnh màn hình sơ đồ dán vào bài làm. Viết danh sách/bảng liệt kê chi tiết các Actor, Use Case và quan hệ.
   - Input: Sơ đồ Use Case Diagram.
   - Output: Hình ảnh sơ đồ và bảng liệt kê mô tả.

(capcuu @ 07:00) [MẸO] Đọc đề câu 2: Bỏ qua toàn bộ đoạn văn ngữ cảnh doanh nghiệp ở đầu, đọc thẳng mục 'Đối tượng người dùng' (User Groups) để tiết kiệm thời gian.
(capcuu @ 06:30) [MẸO] Hễ đề thi nhắc đến thanh toán hoặc gửi email/thông báo thì vẽ thêm Secondary Actor là Payment Gateway / Email System.
(ucd1 @ 58:30) [MẸO] Cách nhớ chiều mũi tên: <<include>> xuất phát từ thao tác thực hiện chĩa tới thao tác bắt buộc kèm theo; <<extend>> xuất phát từ thao tác mở rộng/điều kiện chĩa về thao tác chính.
## Q3
(b6 @ 00:30) Bước 1: Đọc kỹ đề bài và template Use Case Specification
   - Thực hiện: Xác định Use Case Name và Use Case ID từ đề bài. Đọc yêu cầu template (điền EVERY field, không bỏ trống phần nào).
   - Input: Đề bài Q3 và Use Case Spec Template trong đề thi sample
   - Output: Use Case Name ('Register for Course'), Use Case ID ('UC-03')

(b6 @ 02:30) Bước 2: Xác định các Actor (Primary và Secondary)
   - Thực hiện: Xác định ai kích hoạt use case (Primary Actor, ví dụ Student). Xác định hệ thống hoặc bên thứ ba hỗ trợ (Secondary Actor). Mặc định secondary actor thường là System, ngoại trừ trường hợp có bên thứ ba như Payment Gateway, Mapping Service API.
   - Input: Mô tả case study và danh sách actor ở Q2
   - Output: Actor(s): Student (primary); System (secondary)

(b6 @ 03:30) Bước 3: Xác định Preconditions và Post conditions
   - Thực hiện: Trích xuất từ case study điều kiện cần phải có trước khi thực hiện use case (Preconditions: đã đăng nhập, đợt đăng ký đang mở, đủ môn tiên quyết) và trạng thái hệ thống sau khi kết thúc use case (Post conditions: đăng ký thành công hoặc vào waitlist).
   - Input: Kịch bản nghiệp vụ trong đề bài
   - Output: Các gạch đầu dòng Preconditions và Post conditions

(b6 @ 05:00) Bước 4: Viết Main Flow (Basic Path / Luồng chính thành công)
   - Thực hiện: Liệt kê theo thứ tự đánh số 1, 2, 3... tương tác giữa Primary Actor và System từ lúc bắt đầu đến khi kết thúc thành công (8 bước tiêu chuẩn).
   - Input: Luồng nghiệp vụ chuẩn trong case study
   - Output: Danh sách các bước Main Flow (từ bước 1 sinh viên chọn Browse Courses đến bước 8 kết thúc thành công)

(b6 @ 06:30) Bước 5: Viết Alternative Flows (Luồng thay thế)
   - Thực hiện: Xác định các điểm rẽ nhánh trong Main Flow (ví dụ bước 4 check tiên quyết thất bại, bước 5 hết chỗ) và viết kịch bản xử lý tương ứng (Alternative Flow A, Alternative Flow B) với các mã A1-A4, B1-B3.
   - Input: Các tình huống nghiệp vụ phụ trong case study
   - Output: Alternative Flow A (nếu hết chỗ -> waitlist), Alternative Flow B (nếu tạch tiên quyết -> báo lỗi)

(b6 @ 08:30) Bước 6: Viết Exception Flow và Business Rules
   - Thực hiện: Viết luồng sự cố kỹ thuật (Exception Flow: lỗi mạng, sự cố DB ở bất kỳ bước nào) và liệt kê các quy tắc nghiệp vụ áp dụng (Business Rules: trùng lịch, giới hạn tín chỉ, thứ tự ưu tiên waitlist).
   - Input: Yêu cầu kỹ thuật và ràng buộc kinh doanh của bài toán
   - Output: Exception Flow (E1-E3) và Business Rules

(b6 @ 06:00) [MẸO] Khi viết UC Specification, bám sát từng câu từng chữ trong bài case study để trích ra Preconditions, Main Flow và Alternative Flows, không tự nghĩ ra quy trình khác.

(b6 @ 01:30) [MẸO] Trích xuất Use Case Name từ câu Q2 trước đó nếu đề bài lấy lại use case đã liệt kê ở Q2 (ví dụ: 'Submit registration request' trùng với 'Register for Course').

(b6 @ 10:30) [MẸO] Với câu hỏi NFR (Q4), 2 nhóm NFR dễ lấy điểm nhất luôn là Hiệu năng (Performance - Response time) và Bảo mật (Security - Encryption/TLS).

(b6 @ 11:30) [MẸO] Đề thi PE SWE202c thường tập trung vào các hệ thống quen thuộc: Đăng ký học (FAP), Quản lý thư viện, hoặc Hệ thống thi (EOS/SDP).

## Q4
(b4 @ 02:00) Bước 1: Tạo bảng NFR 3 cột theo đúng template đề thi
   - Thực hiện: Vẽ hoặc chép bảng đáp án gồm đúng 3 cột: Category | NFR Description | Acceptance Criterion.
   - Input: Yêu cầu đề thi Part 1 của Question 4
   - Output: Khung bảng NFR 3 cột

(b4 @ 03:00) Bước 2: Xác định các loại NFR (Category) và trích xuất Acceptance Criterion từ đề bài
   - Thực hiện: Liệt kê các Category phổ biến: Performance, Security, Availability, Usability, Scalability (nên làm 5 cái để phòng thiếu). Đọc đoạn kỹ thuật/ràng buộc ở cuối case study, copy chính xác các câu chứa chỉ số đo lường cụ thể vào cột Acceptance Criterion.
   - Input: Đoạn văn kỹ thuật và ràng buộc hệ thống trong Case Study đề thi
   - Output: Các dòng Category và dữ liệu tiêu chí chấp nhận ở cột Acceptance Criterion

(b4 @ 04:30) Bước 3: Viết câu mô tả NFR (NFR Description)
   - Thực hiện: Sử dụng cấu trúc 'The system should [action/quality]' hoặc 'The system must [action/quality]' để mô tả mục tiêu chất lượng tổng quan cho từng Category.
   - Input: Các Category NFR đã chọn (Performance, Security, Availability, Usability, Scalability)
   - Output: Các câu mô tả ở cột NFR Description

(b4 @ 15:30) Bước 4: Chọn cặp NFR bị xung đột (Part 2 Conflict)
   - Thực hiện: Chọn cặp Security và Performance. Đây là cặp xung đột điển hình, phổ biến và dễ giải thích nhất.
   - Input: Bảng NFR ở Part 1
   - Output: Tên cặp xung đột: Security and Performance

(b4 @ 17:00) Bước 5: Giải thích nguyên nhân xung đột (Explain Reason)
   - Thực hiện: Trình bày lý do: Security bảo vệ dữ liệu bằng mã hóa (encryption) và kiểm soát truy cập (access control), nhưng điều này đòi hỏi thêm tài nguyên xử lý (need more processing), dẫn tới hệ thống có thể bị chậm đi khi nhiều người dùng truy cập đồng thời (system can slower when many users use it at the same time).
   - Input: Khái niệm bảo mật và hiệu năng trong ngữ cảnh bài toán
   - Output: Đoạn giải thích lý do xung đột (Explain: Reason)

(b4 @ 20:00) Bước 6: Đề xuất chiến lược dung hòa/đánh đổi (Trade-off Strategy)
   - Thực hiện: Nêu giải pháp kỹ thuật dung hòa: Dùng mã hóa đơn giản và nhanh (simple and fast encryption), lưu cache vai trò người dùng (cache user roles to reduce processing), đồng thời dùng thêm server / mở rộng máy chủ (more server/scaling) để giữ hệ thống chạy nhanh mà vẫn đảm bảo an toàn.
   - Input: Vấn đề xung đột giữa Security và Performance
   - Output: Đoạn giải pháp Trade-off hoàn chỉnh

(b4 @ 05:00) [MẸO] Cách lấy Acceptance Criterion nhanh nhất: Cuộn xuống đoạn văn chứa thông số kỹ thuật (technical constraints) ở cuối Case Study, copy nguyên văn các câu chứa con số tiêu chuẩn (1,000 users, 3s, TLS 1.2, 99.5%, WCAG 2.1) dán thẳng vào cột Acceptance Criterion.

(b4 @ 15:30) [MẸO] Nên luôn luôn chọn cặp xung đột 'Security and Performance' vì là cặp dễ giải thích nguyên nhân (Mã hóa + Phân quyền = Tốn CPU/xử lý làm máy chậm) và dễ đưa ra giải pháp Trade-off nhất (Mã hóa nhanh + Cache user roles + Horizontal scaling).

(b4 @ 26:20) [MẸO] Ghi nhớ bộ từ khóa (keywords) để nhận diện và mô tả nhanh các Category: Performance (speed, response time), Security (login, encryption), Availability (uptime), Usability (easy to use), Scalability (nhiều user), Maintainability (dễ sửa code).

## Q5
(b5 @ 01:30) Bước 1: Lập bảng Part 1 - Domain Class Descriptions
   - Thực hiện: Kẻ bảng 5 cột: # | Class Name | Attributes (with data types) | Methods | Responsibility. Liệt kê toàn bộ các class được gợi ý trong đề bài (User, Student, Lecturer, AcademicStaff, SystemAdmin, Course, CourseOffering, Registration, Waitlist, Grade, Semester, Report).
   - Input: Danh sách Suggested classes trong đề bài Question 5
   - Output: Khung bảng Part 1 gồm 12 class với đầy đủ các cột thông tin

(b5 @ 02:30) Bước 2: Xác định thuộc tính và phương thức cho Class cha User
   - Thực hiện: Đánh dấu User là «abstract». Viết phương thức trước (login(email, pwd): Boolean, logout(): void, updateProfile(data): void), sau đó suy ngược ra các thuộc tính bắt buộc (userId: String, fullName: String, email: String, passwordHash: String, role: String).
   - Input: Yêu cầu người dùng chung trong Case Study
   - Output: Chi tiết thuộc tính và phương thức cho Class User «abstract»

(b5 @ 05:00) Bước 3: Hoàn thiện chi tiết attributes, data types và methods cho các class còn lại
   - Thực hiện: Lần lượt điền ít nhất 3 thuộc tính kèm kiểu dữ liệu (String, int, float, DateTime, Boolean, List) và 2 phương thức cho 11 class con và domain class khác (Student, Lecturer, AcademicStaff, SystemAdmin, Course, CourseOffering, Registration, Waitlist, Grade, Semester, Report).
   - Input: Case Study đề thi và chức năng của từng nhóm người dùng / thực thể
   - Output: Bảng Part 1 đầy đủ 12 class với chi tiết thuộc tính, kiểu dữ liệu, phương thức và trách nhiệm

(b5 @ 32:00) Bước 4: Vẽ mối quan hệ Kế thừa (Generalization) trong UML Diagram
   - Thực hiện: Sử dụng công cụ Generalization (mũi tên tam giác rỗng). Nối 4 class con (Student, Lecturer, AcademicStaff, SystemAdmin) chỉ về class cha User («abstract»).
   - Input: Class User «abstract» và 4 class người dùng cụ thể
   - Output: 4 đường Generalization trỏ từ Student, Lecturer, AcademicStaff, SystemAdmin về User

(b5 @ 33:00) Bước 5: Vẽ các mối quan hệ Liên kết (Association)
   - Thực hiện: Dùng đường Association nối các cặp class có liên kết trực tiếp với nhau: Course – CourseOffering (has), CourseOffering – Registration (for), Student – Registration (submit), Lecturer – Grade (manage).
   - Input: Các class có sự tương tác chức năng trực tiếp
   - Output: Các đường nối Association giữa các cặp class

(b5 @ 40:30) Bước 6: Vẽ mối quan hệ Tập hợp (Aggregation và Composition)
   - Thực hiện: Phân biệt và vẽ:
- Aggregation (hình thoi rỗng): Nối từ Waitlist đến CourseOffering (vì xóa CourseOffering thì sinh viên trong Waitlist vẫn tồn tại).
- Composition (hình thoi đặc): Nối từ Semester đến CourseOffering (vì xóa Semester thì toàn bộ CourseOffering trong kỳ đó bị tiêu hủy theo).
   - Input: Các quan hệ chứa đựng/tập hợp giữa Waitlist-CourseOffering và Semester-CourseOffering
   - Output: Đường Aggregation (thoi rỗng) giữa Waitlist và CourseOffering; Đường Composition (thoi đặc) giữa Semester và CourseOffering

(b5 @ 43:30) Bước 7: Vẽ mối quan hệ Phụ thuộc (Dependency)
   - Thực hiện: Dùng đường nét đứt có mũi tên (Dependency) trỏ từ AcademicStaff sang Report vì phương thức generateReport(): Report trong AcademicStaff nhận/trả về kiểu dữ liệu Class Report.
   - Input: Phương thức generateReport(): Report trong AcademicStaff
   - Output: Mũi tên nét đứt Dependency từ AcademicStaff trỏ đến Report

(b5 @ 45:30) Bước 8: Thêm chỉ số số lượng (Multiplicity Labels)
   - Thực hiện: Bổ sung chỉ số Multiplicity ở CẢ HAI ĐẦU của các đường Association. Ví dụ: Course (1) --- (1..*) CourseOffering; Student (1) --- (0..*) Registration; CourseOffering (1) --- (1) Registration; Lecturer (1) --- (0..*) Grade.
   - Input: Yêu cầu multiplicity labels at both ends trong đề bài
   - Output: Các nhãn chỉ số 1, 1..*, 0..* hiển thị đầy đủ tại hai đầu các mối quan hệ Association

(b5 @ 02:30) [MẸO] Mẹo suy ra thuộc tính từ phương thức: Nhìn vào các phương thức chính của class (ví dụ login(email, pwd)), suy ngược ngay ra các thuộc tính bắt buộc của class đó (email, passwordHash, userId).

(b5 @ 18:30) [MẸO] Mẹo quy ước quyền truy cập (Visibility): Mọi thuộc tính (Attributes) để quyền private (-), mọi phương thức (Methods) để quyền public (+).

(b5 @ 40:30) [MẸO] Mẹo chọn cặp class làm Aggregation và Composition chuẩn nhất: Chọn Waitlist - CourseOffering cho Aggregation (hình thoi rỗng), chọn Semester - CourseOffering cho Composition (hình thoi đặc).

(b5 @ 44:00) [MẸO] Mẹo xác định mối quan hệ Dependency: Tìm phương thức có kiểu trả về là một Class khác (ví dụ generateReport(): Report trong AcademicStaff) -> nối đường nét đứt mũi tên từ AcademicStaff sang Report.

## Q6
(b1-1 @ 01:00) Bước 1: Viết Prompt AI Review Code
   - Thực hiện: Xác định 4 phần: Context, Goal, Code, Output format. Yêu cầu AI tìm lỗi logic, lỗ hổng bảo mật và gợi ý cách sửa.
   - Input: Đoạn code gốc từ đề bài.
   - Output: Prompt review code.

(b1-1 @ 10:30) Bước 2: Phân tích và trình bày danh sách Bug
   - Thực hiện: Trình bày từng bug theo cấu trúc: Code, Type, Why, Risk level (nếu là security bug).
   - Input: Lỗi logic/bảo mật đã phát hiện.
   - Output: Danh sách bug phân tích đầy đủ.

(b1-1 @ 25:30) Bước 3: Viết Prompt Fix Bug
   - Thực hiện: Yêu cầu AI viết lại hàm hoàn chỉnh dựa trên các lỗi đã tìm được, tuân thủ coding best practices và thêm comments.
   - Input: Kết quả các bug ở Bước 2.
   - Output: Prompt fix bug hoàn chỉnh.

(b1-2 @ 30:00) Bước 4: Tự kiểm tra và chấm điểm
   - Thực hiện: Đối chiếu bài làm với thang điểm, đảm bảo gán đúng nhãn loại bug và giải thích đầy đủ.
   - Input: Bài làm hoàn chỉnh.
   - Output: Bài làm đạt điểm tối đa.

(b1-1 @ 03:30) [MẸO] Tận dụng ngay các câu chữ mô tả trong đề bài để chép vào phần Context và Goal của Prompt AI.
(b1-2 @ 12:30) [MẸO] Nhìn thấy lệnh SQL nối chuỗi trực tiếp -> Khẳng định ngay là lỗi SQL Injection, Risk level Critical.
## Q7
(b7 @ 12:00) Bước 1: Tạo bảng 4 giai đoạn kiểm thử (Part 1)
   - Thực hiện: Tạo bảng gồm 4 cột: Testing Stage | What is tested | Who | Testing type. Liệt kê 4 giai đoạn: Unit Testing, Integration Testing, System Testing, Acceptance Testing.
   - Input: Đề bài Yêu cầu 1 của Question 7
   - Output: Bảng khung 4 giai đoạn kiểm thử

(b7 @ 14:30) Bước 2: Điền chi tiết thông tin Part 1 bám sát Case Study
   - Thực hiện: Điền cụ thể What is tested (ví dụ trong CRS: login validation logic, enrollment module connecting to grade module, entire CRS, business requirements/UI), Who (Developers, Developers + Tester, QA/Testing team, Student/Staff), và Testing type (White-box, Gray-box/API, Black-box/Performance/Security, Alpha/Beta). Bám sát các từ khóa từ Case Study để đạt điểm tối đa.
   - Input: Case Study đề bài (CRS) + lý thuyết 4 giai đoạn kiểm thử
   - Output: Bảng Part 1 hoàn chỉnh đạt 0.5 điểm

(b7 @ 27:00) Bước 3: Tạo bảng Test Case 6 cột (Part 2)
   - Thực hiện: Bấm Insert Table trong Google Docs tạo bảng với 6 cột đúng theo tiêu đề đề bài yêu cầu: TCID | Test Case Name | Precondition | Test Steps | Expected Result | Testing Type.
   - Input: Đề bài Yêu cầu 2 của Question 7
   - Output: Khung bảng Test Case 6 cột

(b7 @ 27:30) Bước 4: Viết Test Case TC1 (Happy-path scenario)
   - Thực hiện: Điền TCID: TC1. Test Case Name: Happy-path. Precondition: Student logged in; Course available; Prerequisites met. Test steps: 1, Browse catalogue 2, Select course 3, Click "Register". Expected result: System displays "Registration successful" and update roster. Test type: Functional Testing.
   - Input: Kịch bản 1 đề bài (student successfully registers for an available course)
   - Output: Dòng test case TC1 hoàn chỉnh

(b7 @ 33:30) Bước 5: Viết Test Case TC2 (Boundary / edge-case scenario)
   - Thực hiện: Điền TCID: TC2. Test Case Name: Boundary. Precondition: Course quota = 1 remaining; Student meets prerequisites. Test steps: 1, Select course specific 2, Click "Register". Expected result: System registers student; Quota = 0; next user sees 'Waitlist'. Test type: Boundary value.
   - Input: Kịch bản 2 đề bài (student registers for the last available seat - quota = 1 remaining)
   - Output: Dòng test case TC2 hoàn chỉnh

(b7 @ 36:30) Bước 6: Viết Test Case TC3 (Negative / error scenario)
   - Thực hiện: Điền TCID: TC3. Test Case Name: Negative. Precondition: Student has not completed required base course. Test steps: 1, Select course 2, Click "Register". Expected result: System blocks registration; Display error: "Prerequisites not met". Test type: Negative Testing.
   - Input: Kịch bản 3 đề bài (student attempts to register without meeting the course prerequisite)
   - Output: Dòng test case TC3 hoàn chỉnh

(b7 @ 01:00) [MẸO] Chuẩn bị sẵn mẫu bảng 4 giai đoạn kiểm thử từ trước, khi đi thi gặp Q7 chỉ cần dán bảng vào và chỉnh sửa ví dụ trong cột 'What is tested' cho phù hợp với đề bài Case Study là ăn trọn 0.5 điểm trong chưa đầy 2 phút.

(b7 @ 28:00) [MẸO] Nên làm mỗi câu trong đề thi một ít để lấy điểm từng phần tóm tay, không bỏ trống bất kỳ câu nào.

(b7 @ 35:30) [MẸO] Với kịch bản Boundary (quota = 1), Expected Result phải ghi rõ cả 2 ý: 1. Đăng ký thành công cho sinh viên hiện tại và quota giảm về 0; 2. Người tiếp theo (next user) đăng ký sẽ nhìn thấy trạng thái 'Waitlist'.

