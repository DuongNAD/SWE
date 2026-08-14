# GLOSSARY

**Generalization (Kế thừa)**: Mối quan hệ kế thừa trong UML biểu diễn quan hệ cha-con (is-a). Class con kế thừa toàn bộ thuộc tính và phương thức của class cha. Mũi tên có đầu tam giác rỗng trỏ từ class con về class cha. (Ví dụ: Student, Lecturer, AcademicStaff, SystemAdmin kế thừa từ class cha User «abstract».) (b5 @ 32:00)

**Association (Liên kết)**: Mối quan hệ liên kết cơ bản giữa các class có sự tương tác logic với nhau. Bắt buộc phải có nhãn chỉ số số lượng (Multiplicity) ghi rõ ở cả hai đầu liên kết. (Ví dụ: Course (1) --- (1..*) CourseOffering (một môn học có 1 hoặc nhiều lớp mở trong học kỳ).) (b5 @ 33:00)

**Aggregation (Tập hợp rỗng)**: Mối quan hệ tập hợp lỏng lẻo (has-a). Ký hiệu bằng hình thoi rỗng ở phía class chứa. Class phần tử đóng góp tạo nên class chứa, nhưng nếu class chứa bị xóa thì class phần tử vẫn tồn tại độc lập. (Ví dụ: CourseOffering và Waitlist (xóa lớp học CourseOffering thì danh sách sinh viên chờ Waitlist không bị tiêu hủy hoàn toàn).) (b5 @ 40:30)

**Composition (Tập hợp đặc)**: Mối quan hệ tập hợp chặt chẽ (part-of). Ký hiệu bằng hình thoi đặc màu đen ở phía class chứa. Class phần tử thuộc sở hữu hoàn toàn của class chứa, nếu class chứa bị xóa thì class phần tử bị xoá/tiêu hủy theo. (Ví dụ: Semester và CourseOffering (xóa học kỳ Semester thì tất cả các lớp mở CourseOffering trong học kỳ đó bị xóa hoàn toàn).) (b5 @ 42:00)

**Dependency (Phụ thuộc)**: Mối quan hệ phụ thuộc tạm thời giữa 2 class, biểu diễn bằng đường nét đứt có mũi tên. Xảy ra khi một class sử dụng class khác làm tham số, kiểu trả về hoặc biến cục bộ trong phương thức. (Ví dụ: AcademicStaff phụ thuộc vào Report thông qua phương thức generateReport(): Report.) (b5 @ 43:30)

**Primary Actor (Tác nhân chính)**: Là những đối tượng con người trực tiếp thao tác và tương tác với hệ thống (ví dụ: khách hàng, nhân viên, quản trị viên). (Ví dụ: Customer, Vendor, Customer Support Agent, Marketing Staff, Admin) (capcuu @ 05:30)

**Secondary Actor (Tác nhân phụ)**: Là các hệ thống, dịch vụ bên thứ ba tương tác với hệ thống đang được phát triển. (Ví dụ: Payment Gateway (cổng thanh toán ngân hàng/ví điện tử), Email System / Email API) (capcuu @ 06:00)

**Include (Quan hệ bao hàm / kéo theo)**: Là mối quan hệ kéo theo bắt buộc. Khi thực hiện Use Case này thì luôn luôn phải kéo theo việc thực hiện Use Case kia. Mũi tên chỉ từ Use Case chính sang Use Case bắt buộc. (Ví dụ: Muốn Add To Cart thì bắt buộc phải View Detail Product; muốn Process Returns and Refunds thì bắt buộc phải Search Order.) (capcuu @ 26:00)

**Extend (Quan hệ mở rộng / tùy chọn)**: Là mối quan hệ mở rộng tùy chọn. Khi thực hiện xong Use Case gốc, nếu người dùng muốn thì có thể thực hiện thêm Use Case mở rộng chứ không bắt buộc. Mũi tên trỏ ngược từ Use Case mở rộng VỀ Use Case gốc. (Ví dụ: Sau khi Complete Order (đặt hàng thành công), người dùng có thể mở rộng theo dõi đơn hàng (Track Product Status) nếu thích, không bắt buộc.) (capcuu @ 30:30)

**Non-Functional Requirement (NFR)**: NFR chính là chỉ số chất lượng của hệ thống, mô tả hệ thống hoạt động như thế nào (khác với Functional Requirement mô tả hệ thống làm cái gì) và bắt buộc phải đo lường được bằng các con số cụ thể (measurable). (Ví dụ: Xử lý ít nhất 1.000 người dùng đồng thời với thời gian phản hồi trang dưới 3 giây; thời gian hoạt động đạt 99.5% trong học kỳ.) (b4 @ 00:30)

**NFR Categories**: Các nhóm thuộc tính chất lượng phổ biến để phân loại NFRs trong phần mềm bao gồm Performance (hiệu năng/tốc độ phản hồi), Security (bảo mật/mã hóa/mật khẩu), Availability (tính sẵn sàng/thời gian hoạt động uptime), Usability (tính dễ sử dụng/giao diện đa thiết bị), Scalability (khả năng mở rộng/chịu tải số lượng lớn user), Maintainability (khả năng bảo trì/dễ sửa code). (Ví dụ: Performance (speed, response time), Security (login, encryption), Availability (uptime), Usability (easy to use), Scalability (nhiều user), Maintainability (dễ sửa code).) (b4 @ 00:50)

**NFR Conflict**: Sự xung đột/mâu thuẫn giữa hai yêu cầu phi chức năng trong cùng một hệ thống, khi việc tối ưu hoặc gia tăng một chỉ số chất lượng này dẫn đến làm suy giảm hoặc cản trở một chỉ số chất lượng khác. (Ví dụ: Security vs Performance (càng mã hóa phức tạp thì xử lý càng chậm), Usability vs Security (bảo mật càng chặt thì người dùng thao tác càng rườm rà), Performance vs Scalability.) (b4 @ 01:30)

**Good AI Prompt (Prompt AI chuẩn)**: Một prompt AI lập trình hiệu quả bắt buộc phải có 4 thành phần: (1) Clear context about the system, (2) Specific goal, (3) Code itself, (4) Expected output format. (Ví dụ: Context: Course Registration System Java Spring Boot; Goal: review method; Code: [snippets]; Output: numbered list of issues with explanations.) (b1-1 @ 01:00)

**Logical or Semantic Bug**: Lỗi logic hoặc ngữ nghĩa trong mã nguồn. Code vẫn biên dịch thành công không có lỗi cú pháp nhưng thực thi ra kết quả sai nghiệp vụ. (Ví dụ: Vi phạm điều kiện tiên quyết nhưng hàm lại trả về true; so sánh số lượng enrolled nhưng không bao giờ tăng số enrolled lên.) (b1-1 @ 00:00)

**Data Inconsistency (Không nhất quán dữ liệu)**: Trạng thái dữ liệu bị bất đồng bộ giữa các entity trong cơ sở dữ liệu khi thực hiện một thao tác nghiệp vụ. (Ví dụ: Lưu bản ghi Registration mới vào database nhưng không lưu/cập nhật thông tin Course tương ứng (thiếu courseRepo.save(course)).) (b1-1 @ 21:30)

**Quy trình tăng trưởng (Incremental process)**: Xây hoàn chỉnh từng tầng của tòa nhà, rồi đưa vào sử dụng ngay. (Ví dụ: Hoàn thiện từng phần/tầng phần mềm rồi đưa vào vận hành trước khi xây phần tiếp theo.) (tonghop @ 01:30)

**Quy trình lặp lại (Iterative process)**: Xây một phiên bản khung sườn cơ bản của toàn bộ tòa nhà trước, sau đó dần dần hoàn thiện nó qua từng vòng lặp (lắp kính, đi dây điện, sơn tường). (Ví dụ: Làm khung sườn toàn hệ thống trước rồi nâng cấp hoàn thiện qua từng vòng lặp.) (tonghop @ 01:30)

**Use Case (Ca sử dụng)**: Mô tả chức năng được yêu cầu của hệ thống từ góc nhìn của người dùng. Coi như là các 'động từ' trong hệ thống. (Ví dụ: Người dùng đăng nhập, tìm kiếm sản phẩm A, thêm vào giỏ hàng và tiến hành thanh toán.) (tonghop @ 02:00)

**Actor**: Nhân vật chính thực hiện kịch bản ca sử dụng trong hệ thống. (Ví dụ: Người dùng / Khách hàng.) (tonghop @ 02:30)

**Flow of Events**: Chuỗi các hành động mà actor thực hiện. (Ví dụ: Đăng nhập -> Tìm kiếm -> Thêm giỏ hàng -> Thanh toán.) (tonghop @ 02:30)

**Preconditions**: Điều kiện tiên quyết phải có trước khi thực hiện ca sử dụng. (Ví dụ: Người dùng phải đăng nhập rồi mới được thanh toán.) (tonghop @ 02:30)

**Yêu cầu phi chức năng**: Các yêu cầu về ràng buộc kỹ thuật, thời gian hoặc hiệu năng của hệ thống. (Ví dụ: Hệ thống phải đăng ký xong cho một sinh viên trong vòng chưa đầy một giây.) (tonghop @ 02:30)

**Class (Lớp)**: Bản mô tả một nhóm đối tượng có chung thuộc tính, thao tác, mối quan hệ và ngữ nghĩa. Coi như các 'danh từ' trong hệ thống. (Ví dụ: Class Khách Hàng chứa tên, email, lịch sử mua hàng.) (tonghop @ 03:00)

**Kiểm thử phần mềm**: Công việc của kiểm thử viên là đi săn lùng sai sót; mục tiêu chính là để chứng minh rằng phần mềm có lỗi. (Ví dụ: Chạy các ca kiểm thử để tìm ra lỗi sai trong ứng dụng.) (tonghop @ 03:30)

**Verification (Thẩm tra)**: Trả lời câu hỏi: 'Chúng ta có đang xây tòa nhà đúng theo bản thiết kế không? Các chức năng có hoạt động đúng như mô tả không?' (Ví dụ: Đối chiếu sản phẩm xây ra với bản tài liệu thiết kế.) (tonghop @ 04:00)

**Validation (Thẩm định)**: Trả lời câu hỏi: 'Chúng ta có đang xây đúng tòa nhà mà khách hàng muốn không? Liệu sản phẩm này có thực sự giải quyết được vấn đề của họ hay không?' (Ví dụ: Đánh giá mức độ hài lòng và đáp ứng bài toán thực tế của khách hàng.) (tonghop @ 04:00)

**Mạng Nơ-ron (Neural Network)**: Mô hình suy nghĩ giống dây chuyền lắp ráp siêu thông minh gồm: Lớp đầu vào (nhận dữ liệu thô), Lớp ẩn (trích xuất đặc trưng và học các mẫu), Lớp đầu ra (đưa ra dự đoán dựa trên xác suất). (Ví dụ: Phán đoán hình ảnh với xác suất 98% là con mèo.) (tonghop @ 04:30)

**Chuyển đổi số**: Tích hợp công nghệ vào mọi ngóc ngách của một doanh nghiệp dựa trên 4 trụ cột: Công nghệ (25%), Dữ liệu (25%), Quy trình (25%), Quản lý thay đổi (25%). (Ví dụ: Chuyển đổi toàn diện tổ chức để tạo giá trị mới.) (tonghop @ 06:00)

**Waterfall Model**: Mô hình phát triển phần mềm tuần tự như một thác nước chảy từ trên đỉnh xuống dưới, nước chỉ có thể chảy một chiều và không thể quay ngược trở lại lên trên. Các giai đoạn (Requirement -> Design -> Code -> Test -> Deploy) làm xong bước nào mới chuyển sang bước tiếp theo, không được quay lại chỉnh sửa yêu cầu ban đầu. (Ví dụ: Khi làm xong Requirement và chuyển sang Design thì không thể quay trở lại sửa Requirement được nữa.) (b2 @ 00:30)

**Agile Model (Scrum)**: Mô hình phát triển phần mềm linh hoạt (flexible), vận hành theo vòng tròn lặp lại (iterative). Quy trình đi từ Requirement -> Design -> Code -> Test -> Deploy, sau đó nhận phản hồi từ khách hàng/người dùng để tiếp tục lặp lại, cập nhật và bổ sung tính năng ở các chu kỳ (Sprint) tiếp theo. (Ví dụ: Phát triển và bàn giao phần mềm theo các Sprint từ 2 đến 4 tuần để nhận phản hồi liên tục.) (b2 @ 02:00)

**Minimum Viable Product (MVP)**: Sản phẩm khả thi tối thiểu được phát triển sớm trong các Sprint ban đầu của Agile để tiến hành thử nghiệm tải/hiệu năng và bảo mật ngay từ đầu dự án. (Ví dụ: Xây dựng bản MVP để test khả năng chịu tải 1,000 người dùng đồng thời thay vì đợi đến cuối dự án.) (b2 @ 03:20)

**Actor (Tác nhân)**: Một thực thể nằm bên ngoài hệ thống (có thể là con người hoặc hệ thống/dịch vụ bên ngoài) tương tác trực tiếp với hệ thống để đạt được mục tiêu. Ký hiệu là Stick figure (hình người que). Tên Actor bắt buộc phải là Danh từ (Noun). (Ví dụ: Student, Lecturer, Academic Staff, System Administrator, Notification System) (ucd1 @ 03:30)

**Primary Actor (Tác nhân chính)**: Tác nhân con người trực tiếp sử dụng hệ thống và khởi tạo tương tác để đạt được mục tiêu công việc chính của mình. (Ví dụ: Student (học sinh đăng ký học), Lecturer (giảng viên nhập điểm)) (ucd1 @ 04:00)

**Secondary Actor (Tác nhân phụ)**: Hệ thống, dịch vụ hoặc phần mềm bên ngoài hỗ trợ hệ thống chính thực hiện tác vụ (như gửi email, cổng thanh toán, hệ thống lưu trữ). (Ví dụ: Notification System (hệ thống gửi email tự động), Payment Gateway) (ucd1 @ 04:30)

**Use Case (Trường hợp sử dụng)**: Một chuỗi các hành động/tương tác cụ thể giữa Actor và hệ thống nhằm mang lại một kết quả có giá trị cho Actor. Ký hiệu là Ellipse (hình elip). Tên Use Case bắt buộc là Động từ + Danh từ (Verb + Noun). (Ví dụ: Browse course catalogue, Submit registration request, Record grades) (ucd1 @ 05:30)

**System Boundary (Ranh giới hệ thống)**: Khung hình chữ nhật bao quanh tất cả các Use Case, xác định phạm vi nội bộ của hệ thống. Tất cả Actor phải đặt BÊN NGOÀI ranh giới này, còn tất cả Use Case phải đặt BÊN TRONG. (Ví dụ: Khung chữ nhật mang tên 'Course Registration System') (ucd1 @ 07:00)

**Association (Liên kết)**: Mối quan hệ giao tiếp đơn giản giữa Actor và Use Case. Trên sơ đồ vẽ bằng đường nét liền không có mũi tên. (Ví dụ: Đường nét liền từ Student nối đến Browse course catalogue) (ucd1 @ 08:00)

**<<include>> Relationship**: Mối quan hệ thể hiện hành vi BẮT BUỘC. Use Case chính A luôn luôn tự động triệu gọi Use Case B mỗi khi A được thực thi. Chiều mũi tên nét đứt: trỏ từ Use Case chính sang Use Case bắt buộc (A --<<include>>--> B). (Ví dụ: Submit registration request --<<include>>--> Check prerequisites (luôn phải kiểm tra môn tiên quyết trước khi nộp đơn)) (ucd1 @ 09:00)

**<<extend>> Relationship**: Mối quan hệ thể hiện hành vi MỞ RỘNG CÓ ĐIỀU KIỆN (chỉ xảy ra khi thỏa mãn điều kiện nhất định, không bắt buộc lúc nào cũng chạy). Chiều mũi tên nét đứt: trỏ từ Use Case mở rộng VỀ Use Case chính (B --<<extend>>--> A). (Ví dụ: Join waitlist --<<extend>>--> Submit registration request (chỉ khi lớp học đã đầy chỉ tiêu mới tham gia waitlist)) (ucd1 @ 10:30)

**Primary Actor**: Tác nhân chính - người dùng trực tiếp sử dụng ứng dụng/hệ thống để tương tác và đạt được mục tiêu của họ. (Ví dụ: Customers, Delivery Riders, Warehouse Staff, Managers) (b3-2 @ 07:00)

**Secondary Actor**: Tác nhân phụ - thường là hệ thống bên thứ ba tích hợp với ứng dụng hoặc bộ phận chỉ nhận thông báo thụ động mà không khởi tạo hành động trực tiếp. (Ví dụ: Payment Gateway, Mapping Service API, Procurement Team) (b3-2 @ 07:30)

**Include Relationship («include»)**: Mối quan hệ bắt buộc: Use Case chính bắt buộc phải gọi/sử dụng Use Case phụ để hoàn thành công việc. Mũi tên nét đứt trỏ từ Use Case chính sang Use Case phụ được include. (Ví dụ: Checkout --«include»--> Process payment; Navigate to customer --«include»--> Use map) (b3-2 @ 38:00)

**Extend Relationship («extend»)**: Mối quan hệ mở rộng: Chức năng mở rộng chỉ xảy ra khi có điều kiện đặc biệt hoặc ngoại lệ/lỗi. Mũi tên nét đứt luôn trỏ từ Use Case mở rộng VỀ Use Case chính. (Ví dụ: Retry Payment --«extend»--> Checkout; Receive Restock Alert --«extend»--> Update inventory) (b3-2 @ 41:30)

**Generalization Relationship**: Quan hệ kế thừa giữa các Actor hoặc Use Case: Actor con kế thừa tất cả chức năng của Actor cha và có thêm chức năng riêng. (Ví dụ: Các Actor (Customer, Rider, Manager...) kế thừa từ Actor cha 'System User' để sử dụng chung tính năng Login) (b3-2 @ 45:30)

**Actor phụ / Tác nhân bên ngoài (External System Actor)**: Tác nhân là hệ thống phần mềm bên thứ ba liên kết tích hợp với hệ thống đang thiết kế (như hệ thống bảo hiểm Insurance Provider System). Phải kí hiệu thêm stereotype «system» để phân biệt với tác nhân người dùng. (Ví dụ: «system» Insurance Provider System) (b3-3 @ 04:00)

**Actor Generalization (Kế thừa Tác nhân)**: Tạo một Actor cha tổng quát (như Medical Staff) chứa các quyền/hành động chung (như Login), các Actor con (Doctor, Nurse, Medical Records Officer) sẽ kế thừa từ Actor cha này. (Ví dụ: Doctor, Nurse, Medical Records Officer -- Generalization --> Medical Staff) (b3-3 @ 26:30)

**SQL Injection**: Lỗ hổng bảo mật nghiêm trọng xảy ra khi dữ liệu người dùng nhập (user input) được nối trực tiếp vào câu lệnh SQL native query mà không qua tham số hóa, cho phép kẻ tấn công chèn các đoạn mã SQL tùy ý (như 1' OR '1'='1') để phá vỡ logic truy vấn và khai thác/trích xuất trái phép dữ liệu. (Ví dụ: SELECT * FROM courses WHERE id = '" + courseId + "' khi courseId nhận giá trị "1' OR '1'='1") (b1-2 @ 12:30)

**JPA Named Query / Parameterized Query**: Giải pháp khắc phục SQL Injection trong JPA/Hibernate bằng cách sử dụng tham số truyền vào (parameter binding) thay vì nối chuỗi SQL trực tiếp. (Ví dụ: Thay native query nối chuỗi bằng Query sử dụng setParameter("courseId", courseId)) (b1-2 @ 28:30)

**Wrong Condition**: Lỗi logic trong lập trình khi biểu thức kiểm tra điều kiện if bị viết ngược (ví dụ thừa dấu phủ định !) hoặc mâu thuẫn với kết quả trả về (return value). (Ví dụ: if (!course.isGradingPeriodClosed()) trả về 'Grades published' khi kỳ chấm điểm CHƯA đóng) (b1-2 @ 21:00)

**Risk Level**: Phân loại mức độ nguy hiểm của lỗi/lỗ hổng bảo mật (Low / Medium / High / Critical). Lỗi SQL Injection có khả năng làm rò rỉ toàn bộ CSDL được xếp vào mức Critical. (Ví dụ: Risk level: Critical cho lỗi SQL Injection trong GradeService.java) (b1-2 @ 07:30)

**Unit Testing**: Kiểm thử đơn vị, đi vào từng thành phần nhỏ nhất của mã nguồn như hàm (function), phương thức (method), class trong sự cô lập (in isolation) để đảm bảo mỗi đơn vị code hoạt động đúng logic. (Ví dụ: login validation logic, check condition, quota calculation) (b7 @ 02:00)

**Integration Testing**: Kiểm thử tích hợp, kiểm tra sự tương tác và truyền dữ liệu giữa các module hoặc dịch vụ với nhau sau khi đã qua Unit Testing. (Ví dụ: enrollment module connecting to grade module, waitlist triggering notification service) (b7 @ 04:00)

**System Testing**: Kiểm thử hệ thống, kiểm tra toàn bộ hệ thống hoàn chỉnh sau khi tích hợp để xác minh hệ thống đáp ứng đủ các yêu cầu chức năng (functional) và phi chức năng (non-functional: performance, security...). (Ví dụ: The entire CRS as a complete system, test performance (1000 users), security (TLS 1.2+)) (b7 @ 06:00)

**User Acceptance Testing (UAT)**: Kiểm thử chấp nhận người dùng, giao sản phẩm trực tiếp cho end-user hoặc khách hàng dùng thử để xác minh đáp ứng đúng business requirements và UI/UX. (Ví dụ: Student/Staff sử dụng hệ thống CRS (Alpha/Beta Testing)) (b7 @ 07:00)

**Happy-path scenario**: Kịch bản kiểm thử lý tưởng nhất, trong đó mọi điều kiện đều thuận lợi và không gặp bất kỳ lỗi nào. (Ví dụ: Sinh viên đủ điều kiện tiên quyết, khóa học còn chỗ và đăng ký thành công) (b7 @ 10:00)

**Boundary / edge-case scenario**: Kịch bản phân tích giá trị biên, tập trung vào các điểm nhạy cảm của hệ thống ở giới hạn cho phép. (Ví dụ: Đăng ký vào khóa học khi chỉ còn đúng 1 chỗ trống (quota = 1)) (b7 @ 10:30)

**Negative / error scenario**: Kịch bản kiểm thử trường hợp sai quy tắc, cố tình tạo ra tình huống lỗi để xem hệ thống có phát hiện và chặn lại đúng cách hay không. (Ví dụ: Sinh viên chưa hoàn thành môn tiên quyết cố tình bấm đăng ký môn học) (b7 @ 11:00)

**Use Case Specification (UC Spec)**: Mô tả chi tiết cách hệ thống hoạt động khi thực hiện một use case cụ thể, bao gồm điều kiện đầu vào, đầu ra, luồng chính, các luồng thay thế và ngoại lệ. (Ví dụ: Mô tả chi tiết Use Case 'Register for Course' (UC-03).) (b6 @ 01:00)

**Primary Actor & Secondary Actor**: Primary Actor là tác nhân chính khởi tạo/tương tác trực tiếp với hệ thống (vd: Student). Secondary Actor là hệ thống hoặc bên thứ ba hỗ trợ hoàn thành use case (mặc định là System, hoặc Payment Gateway, Mapping Service API). (Ví dụ: Student (primary); System (secondary)) (b6 @ 02:30)

**Preconditions & Post conditions**: Preconditions là điều kiện bắt buộc phải thỏa mãn trước khi bắt đầu use case. Post conditions là trạng thái kết quả của hệ thống sau khi use case hoàn thành (thành công hoặc rẽ nhánh). (Ví dụ: Precondition: Student logged in; Post condition: Enrolled or waitlisted) (b6 @ 03:30)

**Main Flow (Basic Path)**: Luồng chính (kịch bản lý tưởng) diễn ra thành công từ đầu đến cuối không gặp lỗi hay rẽ nhánh. (Ví dụ: Các bước 1-8 đăng ký khóa học thành công) (b6 @ 05:00)

**Alternative Flow (Luồng thay thế)**: Luồng rẽ nhánh từ một bước trong Main Flow khi gặp tình huống nghiệp vụ khác (vd: hết chỗ, tạch tiên quyết). (Ví dụ: Alternative Flow A (At step 5, if full -> waitlist)) (b6 @ 06:30)

**Exception Flow (Luồng ngoại lệ)**: Luồng xử lý khi xảy ra sự cố kỹ thuật hệ thống (lỗi mạng, lỗi database) ở bất kỳ bước nào. (Ví dụ: At any step, network/database error -> E1, E2, E3) (b6 @ 08:30)

**Business Rules (Quy tắc nghiệp vụ)**: Các quy tắc, ràng buộc logic kinh doanh mà hệ thống phải tuân thủ trong quá trình thực thi use case. (Ví dụ: Không đăng ký trùng lịch, tối đa 24 tín chỉ/kỳ) (b6 @ 09:00)