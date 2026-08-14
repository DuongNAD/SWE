# Question 2 — Các Loại Và Mức Độ Kiểm Thử (1.0 điểm)

## 1. Đề sẽ hỏi thế nào
Dưới đây là một ví dụ trích xuất nguyên văn từ đề thi thật:

> **2. Your manager wants the system tested from the smallest unit level up to the fully integrated system level. At the unit level, testing must focus on program structure; at higher levels, testing must be based on functional requirements.**
> **• a. Which type and level/stage of testing does your manager require? (0.7 point)**
> **• b. Who carries out testing at each stage/level, and why are they the best fit for that role? (0.3 point)**

**Bản dịch tiếng Việt:**
> 2. Quản lý của bạn muốn hệ thống được kiểm thử (test) từ cấp độ đơn vị nhỏ nhất cho tới cấp độ hệ thống tích hợp hoàn chỉnh. Ở cấp độ đơn vị, việc kiểm thử phải tập trung vào cấu trúc chương trình; ở các cấp độ cao hơn, kiểm thử phải dựa trên các yêu cầu chức năng.
> • a. Quản lý của bạn yêu cầu những loại (type) và cấp độ/giai đoạn (level/stage) kiểm thử nào? (0.7 điểm)
> • b. Ai là người thực hiện kiểm thử ở mỗi cấp độ/giai đoạn, và tại sao họ lại là người phù hợp nhất cho vai trò đó? (0.3 điểm)

---

## 2. Hiểu bản chất

Mục tiêu chính của kiểm thử là để **chứng minh phần mềm có lỗi (đi săn lùng sai sót)**, chứ không phải để chứng minh phần mềm hoàn hảo không tì vết (tonghop @ 03:30). Nó xoay quanh hai câu hỏi cốt lõi: Verification (Thẩm tra: Xây có đúng thiết kế không?) và Validation (Thẩm định: Xây có đúng thứ khách hàng cần không?) (tonghop @ 04:00).

Để hiểu rõ cách trả lời câu này, bạn cần phân biệt được **Type (Loại kiểm thử)** và **Level (Cấp độ kiểm thử)**. Đừng để tiếng Anh làm bạn rối, hãy hình dung việc **kiểm tra chất lượng của một chiếc xe máy mới sản xuất**.

### A. Type - Loại kiểm thử (Cách nhìn vào sản phẩm)
Đây là cách chúng ta tiếp cận để kiểm tra lỗi. Có 2 cách tiếp cận chính:
1. **White-box testing (Kiểm thử Hộp trắng):** Nhìn xuyên thấu bên trong. 
   - *Ví dụ đời thường:* Bạn là một thợ sửa xe. Bạn tháo tung dàn áo xe máy ra, kiểm tra xem từng con ốc đã vặn chặt chưa, dây điện có cắm đúng cực không. Bạn phải am hiểu cấu trúc bên trong thì mới làm được.
   - *Trong phần mềm:* Kiểm thử tập trung vào "cấu trúc chương trình" (program structure) - tức là người test phải nhìn thấy và đọc được mã nguồn (code) bên trong.
2. **Black-box testing (Kiểm thử Hộp đen):** Chỉ nhìn bên ngoài.
   - *Ví dụ đời thường:* Bạn là người mua xe. Bạn không cần biết bên trong động cơ nối dây thế nào. Bạn chỉ cần cắm chìa khóa, vặn ga, bóp phanh xem xe có chạy đúng chức năng không.
   - *Trong phần mềm:* Kiểm thử dựa trên "yêu cầu chức năng" (functional requirements). Chỉ nhập đầu vào (input) và xem đầu ra (output) có đúng không, không quan tâm code viết thế nào.

### B. Level - Cấp độ kiểm thử (Quy trình từ nhỏ đến lớn)
Đây là thứ tự kiểm tra từ những bộ phận nhỏ nhất cho đến chiếc xe hoàn chỉnh. Gồm 4 cấp độ bắt buộc [NGOÀI-KHOÁ]:
1. **Unit Testing (Kiểm thử Đơn vị):** Kiểm tra từng thành phần nhỏ nhất.
   - *Ví dụ:* Thợ kiểm tra riêng biệt cái bánh xe xem có bị xì hơi không, cái còi có kêu không. 
2. **Integration Testing (Kiểm thử Tích hợp):** Kiểm tra sự kết nối giữa 2 hay nhiều thành phần.
   - *Ví dụ:* Lắp bánh xe vào hệ thống phanh, bóp phanh xem bánh xe có dừng lại đúng cách không.
3. **System Testing (Kiểm thử Hệ thống):** Kiểm tra tổng thể sau khi lắp ráp xong hoàn toàn.
   - *Ví dụ:* Lắp ráp xong cả chiếc xe máy, nổ máy chạy thử xem tổng thể chiếc xe hoạt động trơn tru không, đèn đóm có sáng hết không.
4. **Acceptance Testing / UAT (Kiểm thử Chấp nhận):** Giao cho khách hàng dùng thử.
   - *Ví dụ:* Khách hàng trực tiếp lái thử chiếc xe. Nếu họ thấy vừa ý và đúng nhu cầu, họ sẽ "chấp nhận" (accept) mua chiếc xe đó (b7 @ 07:00).

---

## 3. So sánh / phân loại

Dưới đây là các khái niệm tiếng Anh và dấu hiệu để bạn nhận diện trong đề thi.

| Thuật ngữ tiếng Anh | Nghĩa tiếng Việt | Dấu hiệu nhận ra trong đề |
|---|---|---|
| **White-box testing** | Kiểm thử hộp trắng (nhìn vào code) | Có từ khóa: `focus on program structure` |
| **Black-box testing** | Kiểm thử hộp đen (test tính năng) | Có từ khóa: `based on functional requirements` |
| **Unit Testing** | Kiểm thử đơn vị | `smallest unit level` |
| **Integration Testing**| Kiểm thử tích hợp | `interaction`, `connecting` (giữa các module) |
| **System Testing** | Kiểm thử toàn hệ thống | `fully integrated system`, `the entire system` |
| **Acceptance Testing** | Kiểm thử chấp nhận (của User) | `business needs`, `user expectations` |

---

## 4. Cách làm bài, từng bước

Đề hỏi lý thuyết, nên bạn không cần tự bịa ra quá nhiều thông tin. Hãy áp dụng đúng các bước sau:

**Bước 1: Trả lời phần "Type" (Loại kiểm thử)**
- Đề hỏi "Which type AND level...", đây là cái bẫy. Phải trả lời rõ "Type" riêng ra.
- Trả lời: "White-box testing" cho mức unit (vì đề nhắc tới 'focus on program structure').
- Trả lời: "Black-box testing" cho mức cao hơn (vì đề nhắc tới 'based on functional requirements').

**Bước 2: Trả lời phần "Level" (Cấp độ kiểm thử)**
- Liệt kê theo đúng thứ tự 4 cấp độ từ nhỏ đến lớn: Unit -> Integration -> System -> Acceptance.
- Viết kèm một câu giải thích ngắn gọn cho mỗi cấp độ.

**Bước 3: Trả lời câu "b" - Who và Why**
- Đối với mỗi cấp độ (Unit, Integration, System, Acceptance), bạn liệt kê 2 gạch đầu dòng:
  - `Who`: Ai là người làm?
  - `Why`: Tại sao họ phù hợp nhất?

---

## 5. Câu mẫu tiếng Anh

Sử dụng trực tiếp các mẫu câu này vào bài thi, không cần sáng tạo thêm.

| Mẫu câu tiếng Anh | Nghĩa tiếng Việt | Dùng khi nào |
|---|---|---|
| **White-box testing at the unit level, because testing must focus on the internal program structure.** | Kiểm thử hộp trắng ở cấp độ đơn vị, vì việc kiểm thử tập trung vào cấu trúc chương trình. | Trả lời phần "Type" dựa vào từ khóa trong đề. |
| **Black-box testing at the higher levels, because testing must be based on functional requirements.** | Kiểm thử hộp đen ở cấp độ cao, vì việc kiểm thử dựa trên yêu cầu chức năng. | Trả lời phần "Type" dựa vào từ khóa trong đề. |
| **Testing individual components or modules.** | Kiểm thử từng thành phần hoặc mô-đun riêng lẻ. | Giải thích chức năng của Unit Testing. |
| **Testing the interaction between combined units or modules.** | Kiểm thử sự tương tác giữa các đơn vị được kết hợp. | Giải thích chức năng của Integration Testing. |
| **Testing the complete, fully integrated software system.** | Kiểm thử toàn bộ hệ thống phần mềm đã tích hợp. | Giải thích chức năng của System Testing. |
| **Final testing based on user expectations and business needs.** | Kiểm thử bước cuối dựa trên mong đợi của người dùng và nhu cầu nghiệp vụ. | Giải thích chức năng của Acceptance Testing. |
| **They wrote the code and understand the internal program structure.** | Họ viết mã nguồn và hiểu cấu trúc chương trình. | Lý do Developer thực hiện Unit Testing. |

---

## 6. Ví dụ đầy đủ

**Đề bài nhỏ:**
Assume your manager wants the system tested from the smallest unit level up to the fully integrated system level. At the unit level, testing must focus on program structure; at higher levels, testing must be based on functional requirements.
a. Which type and level/stage of testing does your manager require? (0.7 point)
b. Who carries out testing at each stage/level, and why are they the best fit for that role? (0.3 point)

**Bài làm hoàn chỉnh bằng tiếng Anh:**

**a. Types and levels/stages of testing required by the manager:**

TYPES required:
- White-box testing at the unit level, because testing must focus on the internal program structure.
- Black-box testing at the higher levels, because testing must be based on functional requirements.

LEVELS/STAGES required, from the smallest to the fully integrated system:
1. Unit Testing: Testing individual components or modules.
2. Integration Testing: Testing the interaction between combined units or modules.
3. System Testing: Testing the complete, fully integrated software system to evaluate its compliance with functional requirements.
4. Acceptance Testing (UAT): Final testing based on user expectations and business needs.

**b. Who performs testing at each stage/level, and why:**

1. Unit Testing: 
- Who: Developers. 
- Why: They wrote the code and understand the internal program structure (White-box testing).

2. Integration Testing: 
- Who: Developers or specialized Integration Testers (QA). 
- Why: They understand how different modules interact and can debug data flow issues.

3. System Testing: 
- Who: Independent Testing Team (QA/QC). 
- Why: They test the system as a whole against the functional requirements without bias (Black-box testing).

4. Acceptance Testing: 
- Who: End-users, Clients, or Business Analysts (e.g., Store-operations representatives). *(Chú ý: Chỗ này có thể lấy tên đối tượng khách hàng thực tế trong đề bài, ví dụ ở đây là Store-operations reps)*
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

---

## 7. Bẫy hay mất điểm

| Lỗi sai thường gặp | Hậu quả | Cách tránh |
|---|---|---|
| Bỏ quên trả lời "Type" (chỉ liệt kê 4 Level). | Bị trừ một phần lớn điểm của ý "a". | Đọc kỹ câu hỏi, thấy chữ "type and level" thì phải chia rõ ra 2 phần: TYPES required và LEVELS required. |
| Đi kẻ bảng vẽ Test Case (nhầm sang câu lập Test Case). | Lạc đề hoàn toàn, nhận 0 điểm. | Nhận diện đúng từ khóa câu này là hỏi lý thuyết: `type and level/stage of testing`. |
| Bỏ quên giai đoạn Acceptance Testing (UAT). | Bị mất điểm phần liệt kê cuối cùng. | Luôn thuộc lòng thứ tự 4 cấp: Unit -> Integration -> System -> Acceptance. (U-I-S-A) |
| Ở câu b, chỉ ghi "Who" mà quên giải thích "Why". | Bị trừ nửa số điểm của ý "b". | Làm bài theo dạng gạch đầu dòng rõ ràng: `- Who:` và `- Why:` cho từng cấp độ. |

---

## 8. Tự kiểm tra

**Câu 1:** Đề bài hỏi "Which type and level of testing...", nếu bạn chỉ ghi 4 giai đoạn kiểm thử từ nhỏ đến lớn thì bạn mất điểm phần nào?
**Câu 2:** Tại sao kiểm thử hệ thống (System Testing) lại dùng phương pháp Black-box testing thay vì White-box testing?
**Câu 3:** Giai đoạn Integration Testing kiểm tra yếu tố gì?
**Câu 4:** Kể tên 4 cấp độ kiểm thử theo đúng thứ tự từ nhỏ nhất đến lớn nhất.

**Đáp án:**
- **Câu 1:** Mất điểm phần "Type" (chưa trả lời White-box và Black-box testing).
- **Câu 2:** Vì ở cấp độ hệ thống, mục đích là kiểm tra xem hệ thống có làm đúng chức năng yêu cầu không (dựa trên functional requirements) thay vì nhìn vào cấu trúc mã nguồn bên trong.
- **Câu 3:** Kiểm tra sự tương tác và kết nối giữa các module/đơn vị code riêng lẻ khi ghép chúng lại với nhau.
- **Câu 4:** Unit Testing -> Integration Testing -> System Testing -> Acceptance Testing.
