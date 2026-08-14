# Question 3 — Identify Requirements (2.0 điểm)

## 1. Đề sẽ hỏi thế nào
Trích nguyên văn tiếng Anh từ đề thi thực tế (page/de.txt):
> "3. Based on the project description above, identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements. (2.0 points)"

**Bản dịch tiếng Việt:**
Dựa trên mô tả dự án ở trên, hãy xác định và liệt kê: 5 yêu cầu chức năng, 3 yêu cầu bảo mật và 2 yêu cầu về khả năng mở rộng. (2.0 điểm)

## 2. Hiểu bản chất
Để làm đúng câu này, bạn cần phân biệt rạch ròi hai khái niệm:

- **Functional Requirements (Yêu cầu chức năng - FRs):** 
Hiểu đơn giản: Là việc hệ thống **LÀM ĐƯỢC GÌ**. Giống như bạn mua một chiếc điện thoại, yêu cầu chức năng là nó phải gọi được điện, chụp được ảnh, lướt được web. Trong bài thi, nó chính là các hành động (động từ) mà người dùng (Actor) hoặc hệ thống có thể thao tác. (Ví dụ: Thu ngân bấm quét mã vạch, hệ thống tính tiền, in hóa đơn).

- **Non-functional Requirements (Yêu cầu phi chức năng - NFRs):**
Hiểu đơn giản: Là hệ thống **LÀM ĐIỀU ĐÓ NHƯ THẾ NÀO (tốt ra sao)**. Giống như chiếc điện thoại ở trên, yêu cầu phi chức năng là nó chụp ảnh mất bao lâu (tốc độ), pin xài được mấy ngày, có mật khẩu vân tay không (bảo mật). Chú ý cốt lõi: NFR **bắt buộc phải đo lường được bằng các con số cụ thể (measurable)** (b4 @ 01:00).

Các loại NFR hay gặp trong đề thi:
- **Performance (Hiệu năng/Tốc độ):** Đánh giá tốc độ phản hồi. VD: Quán ăn phục vụ món phải nhanh dưới 3 phút. Trong IT: Tải trang hiển thị dưới 2 giây.
- **Security (Bảo mật):** An toàn dữ liệu và quyền truy cập. VD: Quán ăn có bảo vệ trông xe và thẻ từ. Trong IT: Đăng nhập cần 2 lớp (MFA), mã hoá dữ liệu (AES, TLS).
- **Scalability (Khả năng mở rộng/Chịu tải):** Khả năng phục vụ khi đột ngột đông khách. VD: Quán có thể kê thêm 10 bàn khi đông mà không vỡ trận. Trong IT: Hệ thống chịu được 1.000 người dùng đồng thời, hoặc thêm cửa hàng mới dễ dàng.
- **Usability (Tính dễ sử dụng):** Thân thiện, dễ hiểu. VD: Menu quán có hình to rõ ràng ai nhìn cũng hiểu. Trong IT: Giao diện trực quan cho cả người không rành công nghệ.

## 3. So sánh / phân loại
Bảng các khái niệm dễ nhầm lẫn và cách 'soi' ra chúng trong đề:

| Thuật ngữ tiếng Anh | Nghĩa tiếng Việt | Dấu hiệu nhận ra trong đoạn văn Case Study |
|---|---|---|
| **Functional Requirement** | Yêu cầu chức năng (Làm được cái gì) | Các hành động mô tả người dùng làm gì: *"user logs in"*, *"cashier scans products"*, *"system records"*, *"system sends alert"*. |
| **Non-functional Requirement** | Yêu cầu phi chức năng (Chất lượng ra sao) | Các đoạn mô tả thông số kỹ thuật (thường ở đoạn gần cuối bài): *"Performance"*, *"Security"*, *"concurrent users"*, *"encryption"*. |
| **Security Requirement** | Yêu cầu bảo mật | Có các từ khóa: *"authenticate"*, *"credentials"*, *"MFA"*, *"encrypt"*, *"TLS 1.3"*, *"AES-256"*, *"audit log"*. |
| **Performance Requirement** | Yêu cầu hiệu năng (tốc độ) | Có các từ khóa: *"respond within X seconds"*, *"load within X seconds"*. |
| **Scalability Requirement** | Yêu cầu về khả năng mở rộng | Có các từ khóa: *"concurrent POS sessions"*, *"scale horizontally"*, *"adding new stores"*, *"without performance degradation"*. |
| **Usability Requirement** | Yêu cầu về tính dễ sử dụng | Có các từ khóa: *"clean interface"*, *"intuitive"*, *"color coding"*. |

## 4. Cách làm bài, từng bước
**Bước 1: Đọc kỹ số lượng đề yêu cầu**
Kiểm tra xem đề bắt liệt kê chính xác số lượng là bao nhiêu. Ví dụ đề yêu cầu 5 FR, 3 Security, 2 Scalability. Bạn phải ghi ra ĐÚNG con số này, không được thừa hay thiếu.

**Bước 2: Tìm Functional Requirements (Yêu cầu chức năng)**
Đọc lướt (scan) Case Study, tìm các đoạn nói về quy trình làm việc của từng nhóm người dùng (Cashier, Store Manager, Warehouse staff...).
Lọc ra các hành động. Biến chúng thành câu mệnh lệnh bằng cách bắt đầu với *"The system must allow [Ai đó] to [Làm gì đó]"* hoặc *"The system must automatically [Làm gì đó]"*.

**Bước 3: Tìm Non-Functional Requirements (Yêu cầu phi chức năng)**
Kéo ngay xuống những đoạn văn gần cuối bài (thường bắt đầu bằng *"On the security front..."*, *"For scalability..."*, *"Technically..."*).
Trích xuất y nguyên văn các câu chứa con số tiêu chuẩn đo lường (measurable) tương ứng với từng loại NFR. (b4 @ 05:00)

**Bước 4: Trình bày ra bài làm**
Chia rõ ràng thành các mục Heading (vd: **Functional Requirements (5):**). Đánh số thứ tự 1, 2, 3... dưới mỗi mục và dán nội dung vào.

## 5. Câu mẫu tiếng Anh
Học thuộc các mẫu câu này, lúc đi thi bạn chỉ cần copy/gõ lại và thay thế ruột bên trong:

| Mẫu câu tiếng Anh | Nghĩa tiếng Việt | Dùng khi nào |
|---|---|---|
| `"The system must allow [Actor] to [Action]."` | Hệ thống phải cho phép [Ai đó] làm [Hành động]. | Khi mô tả Functional Requirement từ góc nhìn người dùng. VD: *"The system must allow cashiers to scan products."* |
| `"The system must automatically [Action]."` | Hệ thống phải tự động [Hành động]. | Khi mô tả Functional Requirement mà hệ thống tự động chạy ngầm. VD: *"The system must automatically send a replenishment request."* |
| `"All data in transit must be encrypted with [Standard]."` | Mọi dữ liệu truyền tải phải được mã hoá bằng [Chuẩn mã hoá]. | Khi viết Security Requirement. Copy thẳng chuẩn mã hoá (VD: TLS 1.3) từ Case Study. |
| `"The platform must support at least [Number] concurrent sessions."` | Nền tảng phải chịu được ít nhất [Số lượng] phiên truy cập đồng thời. | Khi viết Scalability Requirement hoặc Performance. |
| `"The system must respond within [Time]."` | Hệ thống phải phản hồi trong vòng [Thời gian]. | Khi viết Performance Requirement. (vd: *"respond within 1 second"*) |

## 6. Ví dụ đầy đủ
**Đề bài nhỏ (Trích từ Case Study QuickMart):**
> "...When a customer checks out, the cashier scans products at the point-of-sale (POS) terminal; the system records the transaction...
> On the security front, all users authenticate with role-based credentials, and multi-factor authentication (MFA) is enforced... all data in transit is encrypted with TLS 1.3...
> For scalability, the platform must support at least 200 concurrent POS sessions without performance degradation..."

**Bài làm hoàn chỉnh (Viết bằng tiếng Anh):**
```text
Based on the project description, here are the identified requirements:

**Functional Requirements (2):**
1. The system must allow cashiers to scan products at the POS terminal and record the transaction.
2. The system must automatically apply active promotions or loyalty discounts during checkout.

**Security Requirements (2):**
1. All users must authenticate with role-based credentials, and multi-factor authentication (MFA) must be enforced for manager and HQ accounts.
2. All data in transit must be encrypted with TLS 1.3, and data at rest must be encrypted using AES-256.

**Scalability Requirements (1):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
```

**Chú thích vì sao lại viết như vậy:**
- **Ở FR 1 và 2:** Ý được lấy từ đoạn văn mô tả hành động tính tiền (*"cashier scans products..."* và *"applies any active promotions..."*). Ta dùng mẫu câu *"The system must..."* ghép với các cụm từ này. Đảm bảo đúng với quy tắc lấy ý từ bài (playbook b6 @ 06:00).
- **Ở Security 1 và 2:** Nhặt y nguyên các câu chứa ràng buộc bảo mật: *"authenticate"*, *"MFA"*, *"encrypted with TLS 1.3"*. Đi thi trên phần mềm, bạn có quyền bôi đen copy y chang câu trong đề thả vào, không cần sáng tạo thêm ngữ pháp.
- **Ở Scalability 1:** Lấy câu có chứa tham số chịu tải: *"200 concurrent POS sessions"*.

## 7. Bẫy hay mất điểm
Đây là những lỗi sinh viên rất hay mắc phải dẫn đến mất điểm oan uổng:

| Lỗi thường gặp | Hậu quả | Cách tránh (Giải pháp) |
|---|---|---|
| **Tự nghĩ ra chức năng (Hallucinate)** không có trong đề bài | Mất toàn bộ điểm của ý đó | Tuyệt đối chỉ lấy ý/câu chữ từ đoạn văn Case Study, copy nguyên cụm từ tiếng Anh. KHÔNG tự suy diễn logic. |
| **Liệt kê thiếu hoặc thừa** số lượng đề bài yêu cầu | Bị trừ điểm vụn vặt | Đọc thật kỹ số lượng đề bài bắt buộc (VD: 5 functional, 3 security) và đếm lại cẩn thận trước khi chuyển câu khác. |
| **Viết NFR quá chung chung**, không có con số (Ví dụ: *"Hệ thống phải chạy nhanh"*) | Không được tính điểm (NFR bắt buộc phải đo lường được - measurable) (b4 @ 01:00) | Copy chính xác các câu có chứa **thông số kỹ thuật** (vd: *"under 2 seconds"*, *"99.9% uptime"*, *"TLS 1.3"*) từ cuối đề bài. |

## 8. Tự kiểm tra
Bạn hãy tự trả lời 3 câu hỏi sau để củng cố kiến thức nhé:

1. Làm sao để phân biệt nhanh giữa Functional Requirement và Non-Functional Requirement khi đọc một câu trong đề bài?
2. Nếu đề bài không có thông số cụ thể nào về tốc độ phản hồi nhưng lại hỏi "Performance Requirement", bạn sẽ lấy thông tin gì, hay tự nghĩ ra con số như "under 3 seconds"?
3. Việc người dùng phải điền form đăng nhập vào hệ thống thì thuộc về Functional Requirement hay Security Requirement?

---
*(Xem đáp án ở ngay bên dưới)*

<br>
<br>

**Đáp án tham khảo:**
1. **Functional Requirement** (yêu cầu chức năng) luôn gắn với "Ai (Actor) làm hành động gì", ví dụ *"cashier scans products"*. **Non-functional Requirement** (yêu cầu phi chức năng) luôn mô tả "làm như thế nào, có tốt không" và bắt buộc đi kèm các con số đo lường kỹ thuật (seconds, %, standards) (b4 @ 01:00).
2. **Tuyệt đối không tự bịa con số [NGOÀI-KHOÁ].** Mọi thông tin phải trích xuất từ đề. Đề thi SWE202c luôn giấu các thông số này ở một đoạn văn (thường là đoạn kỹ thuật cuối bài). Nếu đề thực sự không có số (cực hiếm), hãy copy câu mô tả chữ về hiệu năng gần nhất trong bài.
3. Việc hệ thống hiển thị Form Đăng nhập cho người dùng nhập email/mật khẩu, so sánh và cho phép vào hệ thống là **Functional Requirement** (chức năng Đăng nhập). Tuy nhiên, việc quy định "Đăng nhập phải xác thực 2 bước (MFA) và mật khẩu phải mã hoá theo chuẩn SHA-256" lại là **Security Requirement**. Hãy đọc kỹ xem đề nhấn mạnh vào hành động chức năng hay nhấn mạnh vào tính an toàn của hệ thống.
