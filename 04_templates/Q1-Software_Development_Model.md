---
id: Q1
ten: Software Development Model
nguon_video: [b2]
do_tin_cay: cao
thoi_gian_de_xuat: 15 phút
---

# NHẬN DIỆN
Đề thuộc câu này khi thấy:
- Từ khoá: `XP framework`, `Kanban model`, `Scrum`, `Agile`, `Waterfall`, `manager suggests applying...`
- Cấu trúc yêu cầu: "Do you agree or disagree? List and explain all main principles, practices, and characteristics of the [Model] framework, then match each of them to the project characteristics above to justify your answer."
- **Dễ nhầm với:** Không dễ nhầm, luôn là câu 1 của đề.

# DỮ KIỆN CẦN MOI TỪ ĐỀ
| Biến | Lấy từ đâu trong đề | Ví dụ |
|---|---|---|
| `{{mo_hinh_duoc_de_xuat}}` | Trong câu hỏi số 1 | XP framework, Kanban model |
| `{{dac_diem_du_an}}` | Đoạn mô tả Case Study (thời gian, đội ngũ, yêu cầu thay đổi, công nghệ) | Nhóm 3-4 dev giỏi, thời gian gấp (3 tháng release), yêu cầu thay đổi liên tục. |
| `{{dong_y_hay_khong}}` | Suy luận dựa trên độ phù hợp của mô hình với đặc điểm dự án | Agree |

# QUY TRÌNH (bám playbook, có nguồn)
1. Đọc mô hình đề xuất trong câu 1.
2. Quyết định Agree hay Disagree dựa vào Case Study (thường là Agree).
3. Liệt kê các principles, practices, characteristics của mô hình đó.
4. Ánh xạ (match) từng đặc điểm của mô hình với thông tin trong Case Study để chứng minh.

# KHUNG ĐIỀN
> Phần này AI copy ra rồi thay `{{...}}`. Giữ nguyên định dạng, thứ tự, cách đánh số.

```
I {{dong_y_hay_khong}} with the manager's suggestion to apply the {{mo_hinh_duoc_de_xuat}} to this project.

Here are the main principles, practices, and characteristics of the {{mo_hinh_duoc_de_xuat}}, and how they match the project characteristics:

1. [Characteristic/Principle 1 of Model]: 
- Explanation: [Brief explanation of what it is]
- Match with project: This matches the project because [Quote/Reference from Case Study, e.g., "the requirements keep evolving"].

2. [Characteristic/Principle 2 of Model]: 
- Explanation: [Brief explanation of what it is]
- Match with project: This fits the project because [Quote/Reference from Case Study].

3. [Characteristic/Principle 3 of Model]: 
- Explanation: [Brief explanation of what it is]
- Match with project: This aligns well since [Quote/Reference from Case Study].

4. [Characteristic/Principle 4 of Model]: 
- Explanation: [Brief explanation of what it is]
- Match with project: This is suitable because [Quote/Reference from Case Study].

Conclusion: Given the project's [summarize key project traits like tight timeline, experienced team, changing requirements], the {{mo_hinh_duoc_de_xuat}} is highly appropriate.
```

# VÍ DỤ ĐÃ ĐIỀN ĐẦY ĐỦ
**Đề:** Your manager suggests applying the XP framework to this project. Do you agree or disagree? List and explain all main principles...
**Bài làm:**
```
I agree with the manager's suggestion to apply the XP (Extreme Programming) framework to this project.

Here are the main principles, practices, and characteristics of XP, and how they match the project characteristics:

1. Frequent Releases and Short Development Cycles: 
- Explanation: XP emphasizes delivering working software frequently in short iterations.
- Match with project: This matches the project requirement of targeting the first release in 3 months and full completion within 9 months.

2. Embracing Change: 
- Explanation: XP is designed to accommodate changing requirements even late in development.
- Match with project: This fits the project perfectly since it is a green-field project whose requirements keep evolving.

3. Pair Programming and Skilled Team: 
- Explanation: XP relies on collaborative coding and high technical expertise.
- Match with project: This aligns well since the IT department heads the build with 3-4 experienced developers.

4. Continuous Customer Involvement: 
- Explanation: XP requires a customer representative on-site to provide continuous feedback.
- Match with project: This is suitable because clinical representatives are part of the team to support the development.
```
*(nguồn: Tự sinh dựa trên đề thật paper.pdf)*

# CHECKLIST TỰ CHẤM
- [ ] Đã trả lời Agree/Disagree rõ ràng.
- [ ] Đã liệt kê đủ các nguyên tắc cốt lõi của mô hình.
- [ ] Mỗi nguyên tắc đều có 1 câu map với dữ kiện cụ thể trong đề (có trích dẫn).

# BẪY THƯỜNG GẶP
| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Chỉ liệt kê lý thuyết mà không match với Case Study | Mất nửa số điểm | Luôn có phần "Match with project" ở mỗi ý. |
| Phản đối (Disagree) nhưng giải thích không hợp lý | Lập luận yếu, mất điểm | Thường đề xuất của manager là đúng (Agree). Nếu Disagree, phải có lý do cực kỳ vững chắc từ Case Study (ví dụ: đề xuất Waterfall cho dự án yêu cầu đổi liên tục). |
