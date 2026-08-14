# P4 — LÀM BÀI KHI CÓ ĐỀ

## GIAI ĐOẠN 1 — PHÂN LOẠI

| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| 1 | Q1-Software_Development_Model.md | "Kanban model", "manager proposes applying", "Do you agree or disagree" | 100% |
| 2 | Q2-Testing.md | "tested from the smallest unit level up to the fully integrated system level", "type and level/stage of testing" | 100% |
| 3 | Q3-Identify_Requirements.md | "identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements." | 100% |
| 4 | Q4-User_Stories.md | "Write 5 user stories based on your answers in Question 3" | 100% |
| 5 | Q5-Design_Patterns.md | "apply design patterns to the software system. List and describe in detail two design patterns" | 100% |
| 6 | Q6-Story_Map.md | "Build a story map for the 'Manage Product Sales' activities" | 100% |

## GIAI ĐOẠN 2 — MOI DỮ KIỆN

**Câu 1:**
- `{{mo_hinh_duoc_de_xuat}}`: Kanban model
- `{{dac_diem_du_an}}`: Cross-functional team of 4-5 developers, a business analyst, and store-operations representatives; continuous feedback; first stores go live within 2 months and full chain within 12 months; new features delivered and deployed continuously; requirements expected to emerge and change incrementally.
- `{{dong_y_hay_khong}}`: Agree

**Câu 2:**
- `{{yeu_cau_test}}`: tested from the smallest unit level up to the fully integrated system level. At the unit level, testing must focus on program structure; at higher levels, testing must be based on functional requirements.

**Câu 3:**
- `{{so_luong_FR}}`: 5 functional requirements
- `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}`: Security requirements, 3
- `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}`: Scalability requirements, 2

**Câu 4:**
- `{{so_luong_US}}`: 5 user stories
- `{{danh_sach_FR_tu_Q3}}`: 5 Functional Requirements đã phân tích ở Câu 3.

**Câu 5:**
- `{{he_thong}}`: Convenient Store Chain Management System (CSCMS)
- `{{tinh_nang_ap_dung}}`: Alert for pay discrepancy (Observer pattern), Tamper-evident audit log (Singleton pattern).

**Câu 6:**
- `{{tieu_diem_chinh}}`: Manage Product Sales
- `{{cac_chuc_nang}}`: Cashier scans products at POS terminal, system records transaction, applies active promotions or loyalty discounts, issues printed or digital receipt, real-time inventory decrement, automatic replenishment request.

## GIAI ĐOẠN 3 — BÀI LÀM

**Question 1:**
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualize the Workflow: 
- Explanation: Kanban emphasizes creating a visual representation of work items (usually on a Kanban board) to understand the workflow and identify bottlenecks.
- Match with project: This fits the project because it involves a "cross-functional team of 4-5 developers, a business analyst, and store-operations representatives," which requires clear visibility of tasks for effective collaboration across different roles.

2. Limit Work in Progress (WIP): 
- Explanation: Kanban limits the number of tasks in progress at any time to improve focus, reduce context switching, and speed up delivery.
- Match with project: This is suitable because the project has a tight deadline where "the first stores go live within 2 months" and requires steady, focused, and rapid development to meet the initial launch date.

3. Manage Flow and Continuous Delivery: 
- Explanation: Kanban focuses on optimizing the flow of work to ensure continuous and smooth delivery of features without waiting for fixed iteration boundaries.
- Match with project: This matches the project requirement where "new features are delivered and deployed continuously throughout" the 12-month rollout.

4. Make Policies Explicit and Feedback Loops: 
- Explanation: Kanban relies on clear rules for moving work and continuous feedback from stakeholders to improve the process and adapt to changes.
- Match with project: This aligns well since the project includes "store-operations representatives who provide continuous feedback" and integration requirements "are expected to emerge and change incrementally."

Conclusion: Given the project's need for continuous deployment, evolving requirements, and constant stakeholder feedback, the Kanban model is highly appropriate.

**Question 2:**
a. Types and levels/stages of testing required by the manager:
Based on the requirement to test from the smallest unit level up to the fully integrated system level, the manager requires the following stages (often referred to as the V-Model or standard testing levels):
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
- Who: End-users, Clients, or Business Analysts (e.g., store-operations representatives or HQ administrators). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

**Question 3:**
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must record the transaction when the cashier scans products at the point-of-sale (POS) terminal.
2. The system must apply any active promotions or loyalty discounts during checkout.
3. The system must automatically decrement store inventory in real time.
4. The system must send an automatic replenishment request to the nearest warehouse when any product falls below the re-order threshold.
5. The system must trigger an alert to both the store manager and the HQ finance team when there is a pay discrepancy.

**Security Requirements (3):**
1. All users must authenticate with role-based credentials.
2. Multi-factor authentication (MFA) must be enforced for manager and HQ accounts.
3. All data in transit must be encrypted with TLS 1.3, and data at rest encrypted using AES-256.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

**Question 4:**
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal to record the transaction so that I can process customer checkouts accurately.
2. **User Story 2:** As a customer, I want the system to apply active promotions or loyalty discounts during checkout so that I can save money on my purchases.
3. **User Story 3:** As a store manager, I want the system to decrement store inventory in real time so that stock levels are always accurate.
4. **User Story 4:** As a store manager, I want the system to send an automatic replenishment request to the nearest warehouse when a product falls below the threshold so that the store never runs out of stock.
5. **User Story 5:** As an HQ finance team member, I want to receive an alert when there is a pay discrepancy so that I can investigate and resolve financial issues quickly.

**Question 5:**
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert mechanism for pay discrepancies. For example, when a daily cash reconciliation reveals a discrepancy, the Cash Reconciliation module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the Store Manager's dashboard and the HQ Finance Team's alert system, ensuring rapid response without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), the Singleton pattern can be used for the system's Audit Logger. Since the system must "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years," a Singleton AuditLogger ensures that all logs are written sequentially to a single centralized log stream, preventing resource conflicts and maintaining the integrity of the tamper-evident records.

**Question 6:**
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
- 2.1.1 As a system, I want to record the transaction so that the sales data is saved securely.
- 2.2.1 As a cashier, I want to issue a printed receipt so that the customer has proof of purchase.
- 3.1.1 As a system, I want to decrement store inventory in real time so that stock levels are accurate.

Release 2----------------------------------------------------------------------
- 1.2.1 As a system, I want to apply active promotions or loyalty discounts so that the customer gets the correct price automatically.
- 2.2.2 As a cashier, I want to issue a digital receipt so that the customer can receive it via email or SMS.
- 3.2.1 As a system, I want to send an automatic replenishment request to the warehouse when a product falls below the threshold so that the store does not run out of stock.

## GIAI ĐOẠN 4 — TỰ CHẤM

| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Trả lời Agree/Disagree, liệt kê đủ nguyên tắc, map trích dẫn | Đạt | Không |
| Q2: Liệt kê đủ 4 cấp độ, nêu rõ Who, giải thích Why | Đạt | Không |
| Q3: Đúng số lượng 5 FRs, 3 Security, 2 Scalability, trích từ case study | Đạt | Không |
| Q4: 5 User Stories, đủ cấu trúc As a... I want to... so that..., bám sát Q3 | Đạt | Không |
| Q5: Đúng 2 pattern, có lý thuyết, có ứng dụng dính chặt case study | Đạt | Không |
| Q6: Tuân thủ format A/B, đánh số chuẩn, US bám sát Task | Đạt | Không |

## BẢN NỘP
*(Bản nộp chính thức chính là nội dung ở GIAI ĐOẠN 3)*
