---
id: Q2
ten: Testing
nguon_video: [b7] # Lưu ý: Video b7 dạy test case, nhưng đề hỏi lý thuyết các mức độ test
do_tin_cay: trung_binh
thoi_gian_de_xuat: 10 phút
---

# NHẬN DIỆN
Đề thuộc câu này khi thấy:
- Từ khoá: `tested from the smallest unit level up to the fully integrated system level`, `type and level/stage of testing`.
- Cấu trúc yêu cầu: "a. What type and level/stage of testing does your manager require? b. Who performs testing at each stage/level..."
- **Dễ nhầm với:** Việc viết Test Case (như video dạy). Tuy nhiên, câu này thuần lý thuyết.

# DỮ KIỆN CẦN MOI TỪ ĐỀ
| Biến | Lấy từ đâu trong đề | Ví dụ |
|---|---|---|
| `{{yeu_cau_test}}` | Câu 2 | "from the smallest unit level up to the fully integrated system level" |

# QUY TRÌNH (bám playbook, có nguồn)
1. **Trả lời TYPE trước, tách riêng khỏi LEVEL.** Đề hỏi "which **type** *and* level/stage",
   đó là HAI câu hỏi. `type` = white-box / black-box. `level` = unit → integration →
   system → acceptance. Nếu chỉ liệt kê level mà không nói rõ type thì mất một phần
   của 0.7 điểm. Dấu hiệu trong đề:
   - "focus on program structure" → **white-box** (nhìn thấy code bên trong)
   - "based on functional requirements" → **black-box** (không nhìn code)
2. Đọc kỹ câu 2 để xác định các mức độ kiểm thử được nhắc đến (Unit, Integration,
   System, Acceptance). [NGOÀI-KHOÁ: kiến thức chuẩn SWE về các cấp độ kiểm thử].
3. Lập danh sách level theo đúng trình tự từ nhỏ đến lớn.
4. Xác định người thực hiện (Who) và lý do (Why) tương ứng cho từng level.

# KHUNG ĐIỀN
> Phần này AI copy ra rồi thay `{{...}}`. Giữ nguyên định dạng, thứ tự, cách đánh số.

```
a. Types and levels/stages of testing required by the manager:

TYPES required:
- White-box testing at the unit level, because testing must focus on the internal program structure.
- Black-box testing at the higher levels, because testing must be based on functional requirements.

LEVELS/STAGES required, from the smallest to the fully integrated system:
1. Unit Testing: Testing individual components or modules (focusing on program structure).
2. Integration Testing: Testing the interaction between combined units or modules.
3. System Testing: Testing the complete, fully integrated software system to evaluate its compliance with functional requirements.
4. Acceptance Testing (UAT): Final testing based on user expectations and business needs.

b. Who performs testing at each stage/level, and why:
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
- Who: End-users, Clients, or Business Analysts (e.g., Clinical representatives/Store operations reps). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.
```

# VÍ DỤ ĐÃ ĐIỀN ĐẦY ĐỦ
**Đề:** Your manager requires the system to be tested from the smallest unit level up to the fully integrated system level...
**Bài làm:**
(Sử dụng y hệt phần KHUNG ĐIỀN vì đây là câu hỏi lý thuyết tiêu chuẩn và không phụ thuộc nhiều vào Case Study ngoại trừ ví dụ ở Acceptance Testing).
*(nguồn: Tự sinh dựa trên đề thật)*

# CHECKLIST TỰ CHẤM
- [ ] Đã liệt kê đủ 4 cấp độ (Unit, Integration, System, Acceptance).
- [ ] Đã nêu rõ "Who" cho từng cấp độ.
- [ ] Đã giải thích rõ "Why" (tại sao họ phù hợp).

# BẪY THƯỜNG GẶP
| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Đi viết Test Case thay vì trả lời lý thuyết | Lạc đề hoàn toàn (0 điểm) | Đọc kỹ từ khóa "What type and level" và "Who performs". |
| Bỏ quên giai đoạn Acceptance Testing | Mất điểm phần cuối | Luôn nhớ quy trình 4 bước chuẩn của SWE: Unit -> Integration -> System -> Acceptance. |
