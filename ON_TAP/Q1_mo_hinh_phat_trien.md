# Question 1 — Software Development Model (2.0 điểm)

## 1. Đề sẽ hỏi thế nào
**Nguyên văn tiếng Anh trong đề:**
> "Your development team is highly skilled and experienced. Your manager proposes applying the Kanban model to this project. Do you agree or disagree? List and explain all the main principles, practices, and characteristics of the Kanban model, then match each of them to the project characteristics above to justify your answer. (2.0 points)"

**Dịch sang tiếng Việt:**
> "Đội ngũ phát triển của bạn rất giỏi và giàu kinh nghiệm. Quản lý của bạn đề xuất áp dụng mô hình Kanban cho dự án này. Bạn đồng ý hay không đồng ý? Hãy liệt kê và giải thích tất cả các nguyên tắc, thực hành và đặc điểm chính của mô hình Kanban, sau đó ghép nối từng đặc điểm đó với các đặc điểm của dự án ở trên để biện minh cho câu trả lời của bạn. (2.0 điểm)"

*(Lưu ý: Đề có thể hỏi về Agile, Scrum, XP, hoặc bắt so sánh với Waterfall, nhưng cấu trúc hỏi "Đồng ý/Không đồng ý -> Liệt kê đặc điểm -> Ánh xạ vào Case Study" là cố định).*

## 2. Hiểu bản chất
Để làm được câu này, bạn không cần học thuộc định nghĩa khô khan. Hãy tưởng tượng việc làm phần mềm giống như xây nhà hoặc làm quán ăn:

**1. Waterfall (Mô hình thác nước):**
- **Bản chất:** Giống như xây một ngôi nhà truyền thống. Bạn phải chốt bản vẽ (Requirement) -> Làm móng (Design) -> Xây thô (Code) -> Hoàn thiện (Test) -> Bàn giao (Deploy). Nước chỉ chảy một chiều từ trên xuống, xong bước này mới qua bước kia. (b2 @ 00:30)
- **Ưu điểm:** Rõ ràng, dễ quản lý, biết trước giá tiền và thời gian.
- **Nhược điểm:** Đang xây đến tầng 3 mà khách đổi ý muốn đổi hướng nhà là... chịu chết. Chỉ tích hợp và xem được sản phẩm ở tít giai đoạn cuối cùng. (b2 @ 12:00)

**2. Agile (Mô hình linh hoạt):**
- **Bản chất:** Thay vì bắt khách đợi cả năm để nhận nguyên cái nhà, bạn xây một cái chòi nhỏ cho khách ở tạm (MVP - Sản phẩm khả thi tối thiểu) trong vòng vài tuần. Khách ở thấy thiếu gì thì bạn xây thêm phòng, thêm bếp. Cứ lặp đi lặp lại như vậy (Iterative). (b2 @ 02:00)
- **Ưu điểm:** Khách hàng thấy sản phẩm sớm, có thể đổi ý thoải mái giữa chừng.
- **Nhược điểm:** Khó đoán trước ngày nào xong toàn bộ, dễ bị phình to chi phí.

**3. Scrum (Một khung làm việc của Agile):**
- **Bản chất:** Chia công việc lớn thành các chu kỳ chạy nước rút gọi là "Sprint" (thường dài 2-4 tuần). Đầu Sprint, cả team chốt làm những gì. Trong Sprint, cứ cúi đầu làm, không cho ai chèn thêm việc. Cuối Sprint, đem sản phẩm ra khoe và họp rút kinh nghiệm.

**4. Kanban (Một khung làm việc của Agile):**
- **Bản chất:** Giống như quy trình làm việc trong một quán phở. Bạn có một bảng chia làm 3 cột: "Chờ làm" (To Do) -> "Đang nấu" (Doing) -> "Nấu xong" (Done). Khách gọi món thì ghi giấy dán lên cột "Chờ làm". 
- **Quy tắc vàng:** Giới hạn số lượng việc đang làm (Limit WIP - Work In Progress). Quán chỉ có 2 cái nồi, nên cột "Đang nấu" chỉ được tối đa 2 tờ giấy. Không nhận thêm để tránh đầu bếp bị quá tải và món ăn bị cháy.
- **Dấu hiệu chọn Kanban:** Đội ngũ giỏi, yêu cầu thay đổi liên tục hàng ngày, cần luồng công việc chảy trôi chảy (Continuous flow).

**5. XP - Extreme Programming (Lập trình cực hạn):**
- **Bản chất:** [NGOÀI-KHOÁ] Giống như Scrum nhưng đẩy các kỹ thuật lập trình lên mức "cực hạn". Hai người code chung một máy (Pair programming), test viết trước cả khi viết code (TDD), và khách hàng phải "ngồi ngay cạnh" dev để chốt yêu cầu liên tục.
- **Dấu hiệu chọn XP:** Đề bài nhắc đến đội ngũ dev cực giỏi, quy mô nhóm nhỏ, yêu cầu thay đổi chóng mặt.

## 3. So sánh / phân loại

| Thuật ngữ Tiếng Anh | Nghĩa Tiếng Việt | Dấu hiệu nhận ra trong đề bài |
|---|---|---|
| **Waterfall** | Mô hình Thác nước (Tuần tự) | "Well-understood requirements", "Stable", "Strict deadlines", "Clear scope". *Thường dùng làm mô hình đối lập để so sánh.* |
| **Agile / Scrum** | Mô hình Linh hoạt / Lặp lại | "Requirements evolve", "Feedback needed", "Cross-functional team", "Sprints of 2-4 weeks". |
| **Kanban** | Mô hình bảng Kanban | "Continuous delivery", "Limit work in progress", "Smooth flow", "Support/Maintenance phase". |
| **MVP (Minimum Viable Product)** | Sản phẩm khả thi tối thiểu | "Deliver early", "Test load/security early", "First release in X months". (b2 @ 03:20) |
| **Iterative process** | Quy trình lặp lại | "Incrementally", "Continuously throughout", "Releases". (tonghop @ 01:30) |

## 4. Cách làm bài, từng bước

Theo Playbook (b2 @ 04:00) và Template, đây là cách bạn lấy trọn 2.0 điểm:

*   **Bước 1: Quyết định Agree hay Disagree.**
    *   Thường đề xuất của manager là **đúng**. Hãy ghi: *I agree with the manager's suggestion...*
*   **Bước 2: Quét (Scan) dữ kiện trong đề.** (b2 @ 05:30)
    *   Tìm và gạch chân: Tính chất yêu cầu (thay đổi hay cố định?), Đội ngũ (bao nhiêu người, giỏi không?), Thời gian (cần release sớm không?), Sự tham gia của khách hàng.
*   **Bước 3: Liệt kê 4 đặc điểm của mô hình và Ánh xạ.**
    *   Với mỗi đặc điểm của mô hình (ví dụ Kanban có 4 đặc điểm: Visualize Workflow, Limit WIP, Continuous Flow, Feedback Loops).
    *   Phải có 2 phần: **Explanation** (Giải thích ngắn gọn) và **Match with project** (Copy/trích dẫn đúng câu trong đề bài để chứng minh).
*   **Bước 4: Kết luận.**
    *   Tóm tắt lại: Dựa vào các đặc điểm trên, mô hình này là cực kỳ phù hợp.

## 5. Câu mẫu tiếng Anh

Vào phòng thi chỉ cần chép các mẫu này và điền vào chỗ trống:

| Câu mẫu Tiếng Anh | Nghĩa Tiếng Việt | Dùng khi nào |
|---|---|---|
| I agree with the manager's suggestion to apply the `<Model_Name>` to this project. | Tôi đồng ý với đề xuất của quản lý về việc áp dụng `<Mô hình>` cho dự án này. | Mở bài (luôn dùng). |
| **Explanation:** `<Model_Name>` emphasizes `<tính_chất_mô_hình>`. | Giải thích: `<Mô hình>` nhấn mạnh vào `<tính_chất>`. | Dùng để giải thích ngắn lý thuyết của mô hình. |
| **Match with project:** This matches the project because `<trích_dẫn_từ_đề>`. | Khớp với dự án: Điều này phù hợp vì `<trích dẫn đề>`. | Dùng để lấy điểm vận dụng (rất quan trọng). |
| Given the project's `<tóm_tắt_đặc_điểm>`, the `<Model_Name>` is highly appropriate. | Dựa trên `<đặc điểm dự án>`, mô hình `<Mô hình>` là vô cùng phù hợp. | Chốt lại ở phần kết luận. |

## 6. Ví dụ đầy đủ

**Đề bài nhỏ:** Áp dụng Kanban cho dự án QuickMart (QVM) có nhóm 4-5 dev, business analyst, yêu cầu thay đổi liên tục, và bàn giao tính năng mới liên tục.

**Bài làm chuẩn:**
I agree with the manager's suggestion to apply the Kanban model to this project.
*(Đồng ý với đề xuất)*

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. **Visualize the Workflow:**
- **Explanation:** Kanban uses a visual board to show all work items and their status. *(Giải thích lý thuyết)*
- **Match with project:** This matches the project because a cross-functional team of 4-5 developers needs a shared view as "integration requirements are expected to emerge and change incrementally". *(Lấy câu trong đề nhét vào)*

2. **Limit Work in Progress (WIP):**
- **Explanation:** Kanban restricts the number of active tasks to prevent bottlenecks.
- **Match with project:** This fits the project because the team is small (4-5 developers) and needs steady focus to ensure the "first stores go live within 2 months".

3. **Manage Flow and Continuous Delivery:**
- **Explanation:** Kanban focuses on the smooth, continuous delivery of work items.
- **Match with project:** This aligns well since the project requires "new features delivered and deployed continuously throughout" the 12-month rollout.

4. **Implement Feedback Loops:**
- **Explanation:** Kanban encourages regular reviews from stakeholders.
- **Match with project:** This is suitable because the project involves "store-operations representatives who provide continuous feedback".

Conclusion: Given the project's traits like evolving requirements and continuous delivery, the Kanban model is highly appropriate.

## 7. Bẫy hay mất điểm

Theo Rubric (b2 @ 05:30), đây là những chỗ sinh viên hay chết oan:

| Lỗi sai phổ biến | Hậu quả | Cách phòng tránh |
|---|---|---|
| Chỉ chép lý thuyết suông về Agile/Kanban mà không lồng dữ liệu đề bài. | Mất nửa số điểm câu này. | **Bắt buộc** phải có dòng "Match with project" và trích dẫn ("...") nguyên văn câu trong đề bài. |
| Phản đối (Disagree) nhưng giải thích yếu. | Mất điểm lập luận. | Thường đề xuất của manager trong đề thi là hợp lý (Agree). Hãy chọn Agree trừ khi đề quá vô lý (VD: dùng Waterfall cho dự án yêu cầu đổi hàng ngày). (Q1-*.md) |
| Đề bắt so sánh Agile và Waterfall, nhưng liệt kê thiếu số lượng. | Mất điểm ý (partial credit). | Bắt buộc phải đủ ít nhất 2 ưu điểm (Advantages) và 2 nhược điểm (Disadvantages) cho MỖI mô hình. (b2 @ 05:00) |
| Chọn Waterfall cho dự án mới có rủi ro cao, yêu cầu chưa chốt. | Sai tư duy kỹ sư. | Luôn ưu tiên Agile/Scrum cho dự án mới, Waterfall chỉ dùng để so sánh làm nền. (b2 @ 12:00) |

## 8. Tự kiểm tra

Đọc xong tài liệu, hãy thử tự trả lời các câu hỏi sau để nhớ lâu:

1. Điểm khác biệt lớn nhất giữa Scrum và Kanban là gì? (Gợi ý: Cột thời gian và WIP).
2. Khi viết câu trả lời cho câu 1, cụm từ nào bắt buộc phải có để lấy điểm thực hành (không bị trừ điểm lý thuyết suông)?
3. Nếu đề bài nói: "Khách hàng muốn chốt xong toàn bộ chức năng, ký hợp đồng rồi 1 năm sau mới nhận bàn giao", bạn chọn Agile hay Waterfall?

---
**Đáp án tự kiểm tra:**
1. Scrum chạy theo chu kỳ thời gian cố định (Sprint 2-4 tuần). Kanban không có chu kỳ cố định mà tập trung vào luồng trôi chảy (Flow) bằng cách giới hạn số lượng công việc đang làm (Limit WIP).
2. Phải có phần "Match with project: This matches the project because..." (Trích dẫn dữ liệu Case Study).
3. Waterfall (Thác nước), vì yêu cầu đã đóng băng và không cần giao hàng sớm.
