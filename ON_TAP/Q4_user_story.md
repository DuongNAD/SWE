# Question 4 — User Stories (1.5 điểm)

## 1. Đề sẽ hỏi thế nào
**Nguyên văn tiếng Anh:**
`Write 5 user stories based on your answers in Question 3.`
hoặc
`Write X user stories that are derived from your answers in Question 3.`

**Bản dịch tiếng Việt:**
*Viết 5 câu chuyện người dùng (user story) dựa trên các đáp án (yêu cầu chức năng) bạn đã làm ở Câu 3.*

## 2. Hiểu bản chất
**User Story (Câu chuyện người dùng)** đơn giản là cách chúng ta mô tả một chức năng của phần mềm, nhưng đứng từ góc nhìn của **người sẽ sử dụng nó**, thay vì viết bằng ngôn ngữ máy móc kỹ thuật.

Mục đích của nó là giúp lập trình viên hiểu rõ: **Ai** cần chức năng này? Họ **muốn làm gì**? Và quan trọng nhất là **để được lợi ích gì**?

**Ví dụ đời thường:** Hãy tưởng tượng bạn vào một quán phở.
- Viết theo kiểu kỹ thuật khô khan (giống Functional Requirement): "Hệ thống nhà bếp phải nấu 1 bát phở tái chín trong 3 phút, có hành, không mì chính."
- Viết theo kiểu **User Story**: "Là một **khách hàng đói bụng**, tôi muốn **gọi một bát phở tái chín không mì chính**, để **tôi có thể ăn ngon mà không bị dị ứng**."

Thấy không? User story không quan tâm nhà bếp nấu như thế nào, nó chỉ quan tâm ông khách cần gì và tại sao ông ấy cần.

**Công thức thần thánh (bắt buộc phải thuộc):**
`As a [Role], I want to [Action], so that [Benefit].`
*(Là một [Ai đó], tôi muốn [Làm gì], để [Đạt được lợi ích gì].)*

## 3. So sánh / phân loại
Dưới đây là các khái niệm rất dễ nhầm lẫn khi làm bài:

| Thuật ngữ tiếng Anh | Nghĩa tiếng Việt | Dấu hiệu nhận ra trong đề bài / Cách dùng |
|---|---|---|
| **Functional Requirement (FR)** | Yêu cầu chức năng | Là những câu mô tả hệ thống phải làm gì ở Câu 3. Ví dụ: "The system must allow..." |
| **User Story (US)** | Câu chuyện người dùng | Viết ở Câu 4, được chế lại từ FR ở Câu 3 nhưng áp dụng công thức "As a... I want... so that...". |
| **Role / Actor** | Vai trò / Người dùng | Người thực hiện hành động. Nhận diện qua các từ: Customer, Cashier, Manager, Admin... |
| **Action** | Hành động / Tính năng | Việc mà người dùng muốn làm. Ví dụ: scan products, login, view report. |
| **Benefit / Goal** | Lợi ích / Mục đích | Lý do sâu xa tại sao họ cần chức năng đó. Thường đi sau chữ "so that...". |

## 4. Cách làm bài, từng bước
**Bước 1: Copy các FR đã làm ở Câu 3 xuống.**
Đề bài luôn yêu cầu User Story phải "derived from" (bắt nguồn từ) Câu 3. Không được tự bịa chức năng mới [NGOÀI-KHOÁ]. Lấy đúng 5 chức năng bạn đã viết ở Q3.

**Bước 2: Tìm 3 thành phần (Role, Action, Benefit) cho mỗi FR.**
- Đọc FR, tìm xem ai làm việc đó -> Đó là **Role**.
- Việc đó là gì -> Đó là **Action**.
- Tự suy luận lý do họ làm thế -> Đó là **Benefit** (nếu trong Case Study không ghi, hãy tự chế ra một lợi ích hợp lý).

**Bước 3: Ráp vào công thức chuẩn.**
Bắt đầu gõ: `As a [Role], I want to [Action] so that [Benefit].`

**Bước 4: Kiểm tra lại số lượng.**
Đề bảo viết 5 câu thì viết đủ 5 câu. Đánh số 1, 2, 3, 4, 5 đàng hoàng.

## 5. Câu mẫu tiếng Anh
Chỉ cần dùng đúng 1 cấu trúc duy nhất cho toàn bộ bài:

| Mẫu câu tiếng Anh (Copy nguyên xi) | Nghĩa tiếng Việt | Dùng khi nào |
|---|---|---|
| **As a** [Role], **I want to** [Action] **so that** [Benefit] | Là một [Role], tôi muốn [Action] để [Benefit]. | Luôn luôn dùng công thức này cho mọi User Story. |
| **As a Customer**, I want to... | Là một khách hàng, tôi muốn... | Khi chức năng dành cho người mua hàng/người dùng cuối. |
| **As an Admin**, I want to... | Là quản trị viên, tôi muốn... | Khi chức năng dành cho người quản lý hệ thống. |
| **As a System**, I want to... | Là hệ thống, tôi muốn... | Chấp nhận được nếu chức năng tự động (vd: gửi email), nhưng ưu tiên dùng người thật hơn. |

## 6. Ví dụ đầy đủ
**Đề nhỏ:** Write 5 user stories based on your answers in Question 3. (Trích đề QuickMart Vietnam)

**Phân tích từ Câu 3 (FR):**
Bạn có 1 FR ở Câu 3 là: "The system must allow cashiers to scan products at the POS terminal and record the transaction."
- Role: Cashier (Thu ngân)
- Action: scan products at the POS terminal (quét mã vạch sản phẩm)
- Benefit (tự suy luận): tính tiền nhanh cho khách.

**Bài làm hoàn chỉnh (tiếng Anh):**
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal to record the transaction so that customers can check out quickly and efficiently.
*(Là thu ngân, tôi muốn quét sản phẩm để khách hàng thanh toán nhanh chóng).*
2. **User Story 2:** As a customer, I want the system to automatically apply active promotions or loyalty discounts during checkout so that I can receive the correct discounted price.
*(Là khách hàng, tôi muốn hệ thống tự áp dụng khuyến mãi để được mua giá rẻ).*
3. **User Story 3:** As a store manager, I want the system to automatically send a replenishment request to the nearest warehouse when stock falls below the threshold so that the store never runs out of products.
*(Là cửa hàng trưởng, tôi muốn hệ thống tự gọi hàng khi sắp hết để kho không bao giờ trống).*
4. **User Story 4:** As a warehouse staff member, I want to receive pick-and-pack orders on my handheld device and update the dispatch status so that the system can automatically reconcile stock across all locations.
*(Là nhân viên kho, tôi muốn nhận đơn trên máy cầm tay để hệ thống tự cập nhật tồn kho).*
5. **User Story 5:** As an HQ finance team member, I want to receive an alert whenever there is a pay discrepancy in the daily cash reconciliation so that financial irregularities can be investigated immediately.
*(Là nhân viên tài chính tổng công ty, tôi muốn nhận cảnh báo khi có sai lệch tiền mặt để xử lý ngay).*

## 7. Bẫy hay mất điểm

| Lỗi sai phổ biến | Hậu quả | Cách tránh |
|---|---|---|
| **Thiếu vế "so that" (Mục đích)** | Mất ngay 1/3 số điểm của câu đó. | Bắt buộc phải có chữ "so that...". Nếu đọc đề không thấy lợi ích là gì, hãy mạnh dạn **tự bịa** ra một lợi ích logic, hợp lý. |
| **Role bị chung chung** | Bị trừ điểm. | Không viết "As a user" (Là một người dùng). Phải viết rõ: As a Doctor, As a Cashier... |
| **Bịa ra tính năng mới** | Sai yêu cầu đề, không được tính điểm. | Phải chế lại đúng 5 cái FR mà bạn đã viết ở Câu 3. Nhìn Q3 viết gì thì Q4 bám theo y chang. |
| **Không đánh số thứ tự** | Trình bày rối rắm. | Luôn viết rõ: 1. User Story 1: ... |

## 8. Tự kiểm tra
Hãy tự trả lời các câu hỏi sau để xem bạn đã nắm chắc phần này chưa nhé:
1. Công thức bắt buộc của User Story gồm 3 phần nào? Bắt đầu bằng những chữ tiếng Anh nào?
2. Nếu FR ở Câu 3 là "The system must send a welcome email when a user registers", hãy chuyển nó thành User Story (giả sử Role là New User).
3. Tại sao không nên viết "As a user" ở đầu câu User Story?

---
**Đáp án:**
1. Role, Action, Benefit. Công thức: "As a [Role], I want to [Action], so that [Benefit]".
2. "As a New User, I want to receive a welcome email when I register so that I know my account was created successfully."
3. Vì "user" quá chung chung. Phải xác định đúng vai trò cụ thể (khách hàng, admin, thu ngân...) để hệ thống phân quyền cho đúng.
