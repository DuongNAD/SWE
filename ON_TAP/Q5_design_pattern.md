# Question 5 — Design Patterns (1.0 điểm)

## 1. Đề sẽ hỏi thế nào
**Trích văn bản tiếng Anh từ đề thi:**
> "The manager asks you to apply design patterns to the software system. List and describe in detail two design patterns discussed in the courses (1.0 points)."

**Dịch sang tiếng Việt:**
> "Quản lý yêu cầu bạn áp dụng các design pattern vào hệ thống phần mềm. Hãy liệt kê và mô tả chi tiết hai design pattern đã học trong môn học (1.0 điểm)."

## 2. Hiểu bản chất
> [NGOÀI-KHOÁ] Lưu ý: Video ôn tập chỉ dạy cách vẽ sơ đồ Class Diagram cho Question 5, không dạy sâu về Design Pattern. Dưới đây là kiến thức bổ sung giúp bạn hiểu tận gốc bản chất của các Design Pattern phổ biến bằng những ví dụ đời thường, thay vì học vẹt định nghĩa sách vở.

Design Pattern (Mẫu thiết kế) đơn giản là **những cách giải quyết đã được chứng minh là hiệu quả** cho các vấn đề lập trình hay gặp. Giống như các "mẹo vặt" hay "công thức" làm bếp, thay vì tự nghĩ cách giải quyết từ đầu, bạn chỉ cần mang công thức ra áp dụng.

*   **Singleton (Độc nhất vô nhị):** Giống như trong trường đại học chỉ có **đúng một** ông Hiệu trưởng. Bất cứ phòng ban nào cần xin chữ ký thì đều phải tìm đến đúng ông đó, không thể tạo ra ông Hiệu trưởng thứ hai. Trong code, đây là class chỉ cho phép tạo ra duy nhất 1 object (đối tượng), thường dùng cho Kết nối Database (Database Connection) hoặc Ghi nhật ký (Audit Logger) để tránh xung đột tài nguyên.
*   **Observer (Kẻ hóng chuyện / Đăng ký theo dõi):** Giống như bạn bấm chuông (Subscribe) một kênh YouTube. Khi kênh đó ra video mới, YouTube tự động đẩy Notification (Thông báo) cho **tất cả** những người đã đăng ký. Trong code, khi một đối tượng thay đổi trạng thái, nó sẽ tự động báo cho các đối tượng đang "hóng" nó biết. Rất hay dùng cho hệ thống cảnh báo (Alert) hoặc thông báo thời gian thực (Real-time Notification).
*   **Factory (Xưởng sản xuất):** Thay vì bạn tự mua linh kiện về hì hục ráp xe đạp (dùng từ khóa `new` trong code để khởi tạo class), bạn đưa tiền cho một nhà máy (Factory) và nói: "Bán tôi 1 chiếc xe đạp địa hình". Nhà máy sẽ lo việc chế tạo và đưa xe cho bạn. Dùng khi bạn cần tạo ra nhiều loại tài khoản người dùng (Student, Admin) hay báo cáo (Report) mà không muốn lộ logic khởi tạo phức tạp ra ngoài.
*   **Strategy (Chiến thuật linh hoạt):** Giống như đi từ Hà Nội vào Sài Gòn, bạn có thể chọn chiến thuật "Đi máy bay" (nhanh, đắt) hoặc "Đi tàu" (chậm, rẻ). Trong code, pattern này cho phép bạn đổi "thuật toán" lúc hệ thống đang chạy. Ví dụ dễ nhất là tính năng Thanh toán: người dùng có thể chọn Momo, thẻ Visa, hoặc Tiền mặt tùy ý mà không cần đập đi viết lại code.
*   **MVC (Model - View - Controller):** Mô hình kiến trúc giống hệt một nhà hàng.
    *   **View** (Giao diện / Bàn ăn): Nơi khách hàng nhìn thấy menu và món ăn.
    *   **Controller** (Người phục vụ): Nhận yêu cầu (order) từ bàn ăn, kiểm tra rồi báo cho đầu bếp.
    *   **Model** (Đầu bếp / Cơ sở dữ liệu): Chế biến món ăn (xử lý dữ liệu thực) rồi đưa phục vụ bê ra.

## 3. So sánh / phân loại

| Thuật ngữ tiếng Anh | Nghĩa tiếng Việt | Dấu hiệu nhận ra trong đề để dùng (Application) |
| :--- | :--- | :--- |
| **Singleton** | Độc thân / Duy nhất | Khi Case Study nhắc đến **Audit log**, **Database connection**, **Configuration**. (Những phần dùng chung toàn hệ thống). |
| **Observer** | Theo dõi / Thông báo | Khi Case Study nhắc đến **Alert**, **Notification**, **Trigger**. (Sự kiện xảy ra và hệ thống tự động báo cho ai đó). |
| **Factory** | Xưởng tạo đối tượng | Khi hệ thống có nhiều loại báo cáo (Reports) hoặc nhiều nhóm người dùng (User groups) cần khởi tạo. |
| **Strategy** | Chiến lược thay thế | Khi hệ thống có nhiều **phương thức thanh toán** (Payment methods) hoặc nhiều cách tính chiết khấu (Discount rules). |
| **MVC** | Mô hình 3 lớp (giao diện - xử lý - dữ liệu) | Khi đề cập giao diện UI tách biệt với cơ sở dữ liệu. |

## 4. Cách làm bài, từng bước

Dạng bài này **chỉ viết chữ**, tuyệt đối **KHÔNG VẼ SƠ ĐỒ**.

*   **Bước 1: Chọn 2 Pattern dễ viết nhất.** (Khuyên dùng: **Observer** và **Singleton** vì gần như đề thi nào cũng nhét hai cái này vào được).
*   **Bước 2: Viết lý thuyết (Description).** Ghi định nghĩa chuẩn bằng tiếng Anh. (Học thuộc 2 câu mẫu ở Phần 5).
*   **Bước 3: Liên hệ thực tế (Application to the system).** Đây là phần quan trọng nhất để lấy điểm. Bạn phải đọc Case Study tìm các dữ kiện (ví dụ tính năng gửi thông báo, tính năng ghi log) để chứng minh pattern đó giúp ích gì cho hệ thống.
    *   *Mẹo:* Scan đề tìm chữ "alert / notify" -> Nhét chữ đó vào phần Application của Observer.
    *   *Mẹo:* Scan đề tìm chữ "audit log / security log" -> Nhét chữ đó vào phần Application của Singleton.
*   **Bước 4: Hoàn thành bài làm.** Ghép theo form: Tên Pattern -> Description -> Application.

## 5. Câu mẫu tiếng Anh

Học thuộc các câu này để mang vào phòng thi:

| Mẫu câu tiếng Anh | Nghĩa tiếng Việt | Dùng khi nào |
| :--- | :--- | :--- |
| *The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically.* | Pattern Observer định nghĩa mối quan hệ 1-nhiều, để khi một đối tượng đổi trạng thái, mọi kẻ phụ thuộc đều được tự động thông báo. | Viết phần lý thuyết (Description) cho **Observer**. |
| *The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.* | Pattern Singleton đảm bảo một class chỉ có duy nhất một đối tượng và cung cấp điểm truy cập toàn cục tới nó. | Viết phần lý thuyết (Description) cho **Singleton**. |
| *In this system, this pattern can be applied to...* | Trong hệ thống này, pattern này có thể áp dụng cho... | Mở bài cho phần **Áp dụng (Application)**. |
| *For example, when a pay discrepancy is logged, the system automatically notifies the store manager.* | Ví dụ, khi có chênh lệch thanh toán, hệ thống tự động báo cho quản lý cửa hàng. | Câu chốt ví dụ áp dụng cho **Observer** (thay sự kiện tùy theo đề). |
| *A Singleton AuditLogger ensures that all logs are written sequentially to a single centralized file.* | Một AuditLogger (dạng Singleton) đảm bảo mọi nhật ký đều được ghi tuần tự vào một file tập trung duy nhất. | Câu chốt ví dụ áp dụng cho **Singleton**. |

## 6. Ví dụ đầy đủ

Dưới đây là một bài làm hoàn chỉnh bằng tiếng Anh dựa trên Case Study của hệ thống **CSCMS (Convenient Store Chain Management System)** trong đề mẫu.

**Bài làm:**

Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

**1. Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert and notification mechanism. For example, when a "pay discrepancy" is logged during daily cash reconciliation, the reconciliation module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the store manager's dashboard and the HQ finance team's system, ensuring prompt alerts without tight coupling.
> *(Giải thích tiếng Việt: Đoạn Application lấy đúng chi tiết "pay discrepancy triggers an alert" trong đề để áp dụng Observer, chỉ ra Chủ thể (Subject) là chức năng đối soát, Người theo dõi (Observer) là màn hình quản lý. Điểm tuyệt đối vì lồng ghép chặt chẽ Case Study).*

**2. Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CSCMS, the Singleton pattern can be used for managing the audit logging service. Since the system needs to "keep a tamper-evident audit log of every transaction," a Singleton AuditLogger ensures that all log entries across different modules are written sequentially to a single centralized log stream, preventing resource conflicts and ensuring data consistency.
> *(Giải thích tiếng Việt: Đoạn Application lấy đúng chi tiết "keep a tamper-evident audit log" trong đề để áp dụng Singleton, lý giải rằng việc ghi log phải tập trung ở đúng 1 đối tượng duy nhất để không bị tranh chấp tài nguyên).*

## 7. Bẫy hay mất điểm

| Lỗi sai chết người | Hậu quả | Cách tránh |
| :--- | :--- | :--- |
| **Đi vẽ sơ đồ Class Diagram** | Lạc đề hoàn toàn, mất trắng điểm phần này, lãng phí thời gian thi. | Đọc kỹ đề, nếu yêu cầu "list and describe" thì KHÔNG VẼ. Nếu đề hỏi vẽ thì sẽ nói rõ chữ "draw Class Diagram". |
| **Chỉ nêu lý thuyết suông** | Bị trừ đi một nửa số điểm của câu. | Bắt buộc phải viết phần **Application to the system**, gọi đúng tên hệ thống từ đề bài ra. |
| **Chọn bừa Pattern mà không thuộc tiếng Anh** | Viết lủng củng, sai ngữ pháp, giám khảo đọc không hiểu. | Tốt nhất nên học thuộc lòng 2 câu lý thuyết tiếng Anh của **Observer** và **Singleton** ở trên để làm mọi bài. |

## 8. Tự kiểm tra

**Hãy tự trả lời các câu hỏi sau để nhớ bài:**
1. Nếu đề bài yêu cầu hệ thống "send an automatic replenishment request" (gửi yêu cầu bổ sung hàng tự động khi hết hàng). Bạn nên áp dụng Pattern nào là hợp lý nhất?
2. Tại sao lại dùng Singleton cho tính năng ghi nhật ký hệ thống (Audit Log) thay vì tạo ra nhiều đối tượng Log ở nhiều nơi?
3. Nếu đề hỏi "List and describe 2 design patterns", bạn có cần mở StarUML lên vẽ sơ đồ thiết kế không?

**Đáp án đối chiếu:**
1. **Observer Pattern**. (Vì có sự thay đổi trạng thái - từ còn hàng sang hết hàng, dẫn đến gửi thông báo tự động cho kho).
2. Vì nếu có nhiều đối tượng cùng ghi log một lúc vào 1 file, file sẽ bị lỗi hoặc tranh chấp tài nguyên. Cần Singleton để quản lý tập trung "độc nhất vô nhị".
3. **Tuyệt đối KHÔNG**. Chỉ giải thích và áp dụng bằng chữ. Đừng để dính bẫy đi vẽ hình.
