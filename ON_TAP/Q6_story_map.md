# Question 6 — Story Map (2.5 điểm)

## 1. Đề sẽ hỏi thế nào
Trích nguyên văn từ đề thi:
> "Build a story map for the "Manage Product Sales" activities described in the project above. (2.5 points)"

*Dịch sang tiếng Việt:*
> "Hãy xây dựng một bản đồ câu chuyện (story map) cho các hoạt động "Quản lý Bán hàng" (Manage Product Sales) được mô tả trong dự án ở trên. (2.5 điểm)"

## 2. Hiểu bản chất
**Story Map (Bản đồ câu chuyện) là gì?**
Hãy tưởng tượng bạn đang lên kế hoạch mở một quán phở mới. Bạn không thể làm mọi thứ lộn xộn, mà phải phân chia rõ ràng:
- **Activity (Hoạt động lớn):** Quán phở có 3 khâu chính là *Đón khách*, *Làm phở*, và *Thanh toán*.
- **User Task (Công việc cụ thể):** Trong khâu *Đón khách*, nhân viên phải làm các việc nhỏ hơn là *Xếp bàn* và *Đưa menu*. Trong khâu *Thanh toán*, nhân viên phải *Tính tiền* và *In hóa đơn*.
- **Release (Giai đoạn phát hành):** Bạn không thể hoàn hảo ngay từ ngày đầu tiên. 
  - **Release 1 (Ngày khai trương):** Chỉ làm những thứ cơ bản nhất để quán chạy được. Ví dụ: Khách gọi mồm (không cần menu), tính tiền mặt.
  - **Release 2 (Tháng thứ hai):** Nâng cấp xịn hơn. Ví dụ: Dùng menu iPad, quét mã QR thanh toán chuyển khoản.
- **User Story (Câu chuyện người dùng):** Là cách bạn diễn đạt lại công việc đó từ góc nhìn của một người cụ thể. Ví dụ: *"Là một người bồi bàn (Ai), tôi muốn quét mã QR thanh toán (Làm gì), để tôi thu tiền nhanh hơn (Mục đích)"*.

=> **Story Map** trong phát triển phần mềm chính là việc bạn sắp xếp các tính năng của phần mềm theo đúng hệ thống phân cấp như vậy: Từ mảng việc lớn (Activity) chia thành các thao tác nhỏ (User Task), và phân bổ chúng xem cái nào làm trước cho phiên bản cơ bản (Release 1), cái nào làm sau cho phiên bản nâng cao (Release 2).

## 3. So sánh / phân loại
Dưới đây là bảng phân biệt các khái niệm dễ nhầm lẫn trong bài Story Map:

| Thuật ngữ tiếng Anh | Nghĩa tiếng Việt | Dấu hiệu nhận ra / Cách trình bày |
|---|---|---|
| **Activity** | Mảng hoạt động lớn | Là các nhóm tính năng lớn. Đánh số: `1`, `2`, `3`... (Ví dụ: `1. Process Checkout`). |
| **User Task** | Công việc / Thao tác | Chi tiết hơn Activity, là các hành động cụ thể. Đánh số: `1.1`, `1.2`, `2.1`... |
| **User Story** | Câu chuyện người dùng | Mô tả chi tiết mong muốn từ góc nhìn người dùng. **Bắt buộc** bắt đầu bằng `As a... I want to...`. Đánh số 3 cấp: `1.1.1`, `1.2.1`... |
| **Release** | Đợt phát hành / Bàn giao | Gồm Release 1 (Core/MVP - tính năng cốt lõi) và Release 2 (Advanced - tính năng nâng cao/tự động hóa). |

## 4. Cách làm bài, từng bước
Tuân thủ tuyệt đối cấu trúc được hướng dẫn ở phần "III Notes" của đề thi. Hệ thống chấm EOS sẽ chấm theo định dạng này.

- **Bước 1: Lấy tiêu điểm từ đề.** Đọc câu hỏi 6 để xem họ bắt làm Story Map cho mảng nào (ví dụ: "Manage Product Sales").
- **Bước 2: Viết Phần A - Activities.** Chia tiêu điểm đó thành 2-4 mảng hoạt động lớn. Ví dụ: 1. Process Checkout (Xử lý thanh toán), 2. Handle Payment (Nhận tiền), 3. Update Inventory (Cập nhật kho).
- **Bước 3: Viết Phần A - User Tasks.** Dưới mỗi Activity, gạch đầu dòng 2-4 công việc cụ thể. Đánh số chuẩn `1.1`, `1.2`...
- **Bước 4: Viết Phần B - Release 1 (Cốt lõi).** Liệt kê các chức năng bắt buộc phải có để hệ thống chạy được cơ bản (như quét mã vạch, tính tiền, trừ kho, in hóa đơn giấy). Viết dưới dạng User Story (`As a...`). Chú ý mã số: `1.1.1` phải tương ứng với task `1.1` ở phần A.
- **Bước 5: Viết Phần B - Release 2 (Nâng cao).** Liệt kê các chức năng nâng cấp "sang xịn mịn" hơn (như tự động áp mã giảm giá, gửi hóa đơn điện tử qua SMS, cảnh báo kho tự động).

*(Mẹo: Hãy nhớ nguyên tắc đánh số của đề thi: Activity `1` -> User Task `1.1` -> User Story trong Release `1.1.1` hoặc `1.1.2`)*.

## 5. Câu mẫu tiếng Anh
Các câu User Story (Phần B) thường rất dài và khó viết nếu tiếng Anh yếu. Hãy học thuộc một số mẫu sau:

| Mẫu câu tiếng Anh (User Story) | Nghĩa tiếng Việt | Dùng khi nào |
|---|---|---|
| `As a cashier, I want to scan products at the POS terminal so that the items are added to the checkout list.` | Là một thu ngân, tôi muốn quét mã vạch tại máy POS để sản phẩm được thêm vào hóa đơn. | Thường nằm ở **Release 1** (chức năng cốt lõi bắt buộc phải có để bán hàng). |
| `As a cashier, I want the system to record the transaction so that the sales data is saved securely.` | Là thu ngân, tôi muốn hệ thống ghi nhận giao dịch để dữ liệu bán hàng được lưu an toàn. | Nằm ở **Release 1** (lưu dữ liệu cốt lõi). |
| `As a customer, I want the system to apply active promotions or loyalty discounts so that I get the correct price automatically.` | Là khách hàng, tôi muốn hệ thống tự áp dụng khuyến mãi để tôi được tính đúng giá. | Thường nằm ở **Release 2** (tính toán tự động). |
| `As a store manager, I want the system to send an automatic replenishment request to the warehouse when a product falls below the threshold, so that my store never runs out of stock.` | Là quản lý cửa hàng, tôi muốn hệ thống tự gửi yêu cầu nhập hàng khi sản phẩm dưới ngưỡng, để cửa hàng không bị hết hàng. | Thường nằm ở **Release 2** (cảnh báo tự động). |

> ⚠️ **KHÔNG BAO GIỜ viết `As a system, I want to…`**
> User story luôn nhìn từ góc độ **con người được hưởng lợi**, không phải từ góc độ
> máy móc. Chức năng tự động thì viết: `As a <người hưởng lợi>, I want **the system to**
> <làm gì tự động>, so that <lợi ích của người đó>`.
> Viết `As a system` là lỗi kinh điển, người chấm nhận ra ngay.

## 6. Ví dụ đầy đủ
**Đề bài:** Build a story map for the "Manage Product Sales" activities... (2.5 điểm)

**Bài làm mẫu:**
```text
A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan Products
   - 1.2 Apply Discounts
2. Handle Payment and Receipt
   - 2.1 Record Transaction
   - 2.2 Issue Receipt
3. Update Inventory
   - 3.1 Decrement Stock
   - 3.2 Trigger Replenishment

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS terminal so that the items are added to the checkout list.
- 2.1.1 As a store manager, I want the system to record the transaction so that the sales data is saved securely.
- 2.2.1 As a cashier, I want to issue a printed receipt so that the customer has proof of purchase.
- 3.1.1 As a store manager, I want the system to decrement store inventory in real time so that stock levels are accurate.

Release 2----------------------------------------------------------------------
- 1.2.1 As a store manager, I want the system to apply active promotions or loyalty discounts so that the customer gets the correct price automatically.
- 2.2.2 As a cashier, I want to issue a digital receipt so that the customer can receive it via email or SMS.
- 3.2.1 As a store manager, I want the system to send an automatic replenishment request to the warehouse when a product falls below the threshold so that the store does not run out of stock.
```
**Chú thích (Tại sao lại viết thế này):**
- **Phần A** chỉ toàn các động từ ngắn gọn (Scan, Apply, Record, Issue, Decrement).
- **Phần B, Release 1** chứa các nghiệp vụ thô sơ nhất: Quét mã (`1.1.1`), Lưu dữ liệu (`2.1.1`), In hóa đơn giấy (`2.2.1`), Trừ kho (`3.1.1`).
- **Phần B, Release 2** chứa các nghiệp vụ thông minh, tiện ích: Tự động giảm giá (`1.2.1`), Gửi hóa đơn điện tử (`2.2.2`), Tự động gọi hàng (`3.2.1`).
- **Đánh số logic:** Chú ý `2.2.2` (hóa đơn điện tử) chính là bản nâng cấp thứ hai của Task `2.2 Issue Receipt`.

## 7. Bẫy hay mất điểm
| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Vẽ bảng (table) thay vì viết text. | Không tương thích hệ thống thi, mất trắng điểm. | Bắt buộc trình bày bằng **danh sách text (list)** giống y hệt phần III Notes của đề. |
| Đánh số lộn xộn, User Story không khớp với User Task. | Bị trừ điểm logic nặng. | User Story mang mã số `X.Y.Z` **bắt buộc** phải là việc thực thi chi tiết của User Task `X.Y`. |
| Viết User Story thiếu chủ ngữ (`As a...`). | Mất điểm cú pháp User Story. | Luôn bắt đầu câu trong phần B bằng `As a [ai đó/hệ thống], I want to...` |

## 8. Tự kiểm tra
1. Để phân biệt tính năng nào đưa vào Release 1, tính năng nào đưa vào Release 2, tiêu chí quan trọng nhất là gì?
2. User Task `2.1` là "Login to system". Vậy User Story của nó trong Release 1 nên được đánh mã số là gì?
3. Có bắt buộc mọi User Task ở phần A đều phải xuất hiện trong Release 1 không?

---
**Đáp án tự kiểm tra:**
1. Release 1 chứa tính năng cốt lõi (Core/MVP) bắt buộc phải có để hệ thống hoạt động cơ bản. Release 2 chứa các tính năng nâng cao, tự động hóa, tối ưu trải nghiệm (Advanced).
2. Đánh số là `2.1.1` (Số `2` là Activity, số `1` là Task, số `1` cuối cùng là thứ tự story của task đó).
3. Không bắt buộc. Có những User Task nâng cao (như Apply Discounts) có thể để dành hoàn toàn sang Release 2 mới bắt đầu phát triển. Tương ứng, User story của nó sẽ nằm ở Release 2.
