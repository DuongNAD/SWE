**GIAI ĐOẠN 1 — PHÂN LOẠI**
| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Câu 1 | Q1 - Software Development Model | Từ khoá "applying the Kanban model", "Do you agree or disagree" | 100% |
| Câu 2 | Q2 - Testing | Từ khoá "tested from the smallest unit level...", "type and level/stage of testing" | 100% |
| Câu 3 | Q3 - Identify Requirements | Từ khoá "identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements" | 100% |
| Câu 4 | Q4 - User Stories | Từ khoá "Write 5 user stories derived from your answers in Question 3" | 100% |
| Câu 5 | Q5 - Design Patterns | Từ khoá "apply some design patterns", "list and describe in detail two design patterns" | 100% |
| Câu 6 | Q6 - Story Map | Từ khoá "Build a story map for the 'Manage Product Sales' activities", định dạng EOS | 100% |

**GIAI ĐOẠN 2 — MOI DỮ KIỆN**

**Câu 1:**
- `{{mo_hinh_duoc_de_xuat}}`: Kanban model
- `{{dac_diem_du_an}}`: CSCMS là nền tảng quản lý thống nhất, thay thế nhiều công cụ rời rạc. Yêu cầu tích hợp sẽ xuất hiện và thay đổi dần ("emerge and change incrementally") khi các cửa hàng tham gia. Đội dev 4-5 người, có BA và store-operations reps để phản hồi liên tục ("continuously provide feedback"). Tính năng được đưa lên liên tục ("delivered and deployed continuously throughout").
- `{{dong_y_hay_khong}}`: Agree

**Câu 2:**
- `{{yeu_cau_test}}`: tested from the smallest unit level up to the fully integrated system level. focus on program structure (unit), functional requirements (higher levels).

**Câu 3:**
- `{{so_luong_FR}}`: 5 functional requirements
- `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}`: 3 security requirements
- `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}`: 2 scalability requirements

**Câu 4:**
- `{{so_luong_US}}`: 5
- `{{danh_sach_FR_tu_Q3}}`: Lấy từ 5 FRs ở Câu 3. Chú ý sử dụng vai trò là con người, không dùng "As a system".

**Câu 5:**
- `{{he_thong}}`: Convenient Store Chain Management System (CSCMS)
- `{{tinh_nang_ap_dung}}`: Observer (alert for pay discrepancy), Singleton (Audit log or Database connection pool)

**Câu 6:**
- `{{tieu_diem_chinh}}`: "Manage Product Sales"
- `{{cac_chuc_nang}}`: checkout, scan products at POS, apply active promotions/loyalty, issue receipt, decrement inventory.

**GIAI ĐOẠN 3 — BÀI LÀM**

## BẢN NỘP

### Question 1

I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualize the Workflow:
- Explanation: Kanban uses a visual board to map out all tasks in the development process, allowing the team to see the status of every work item transparently.
- Match with project: This matches the project because it relies on a cross-functional team of "4-5 developers, a business analyst, and store-operations representatives" who need a shared, visual understanding of the continuous work flow.

2. Limit Work in Progress (WIP):
- Explanation: Kanban restricts the number of active tasks in any given stage to prevent bottlenecks and improve flow efficiency.
- Match with project: This fits the project because "integration requirements are expected to emerge and change incrementally as stores are on-boarded one by one," requiring the team to manage a steady but unpredictable stream of work without becoming overwhelmed.

3. Continuous Delivery and Flow:
- Explanation: Unlike Scrum's fixed-length sprints, Kanban emphasizes a continuous, smooth flow of tasks from the backlog to completion.
- Match with project: This aligns well since leadership expects "new features delivered and deployed continuously throughout" the 12-month rollout, rather than in fixed, time-boxed batches.

4. Manage and Improve the Flow:
- Explanation: Kanban focuses on continuously monitoring the workflow and adapting processes to optimize lead time and remove inefficiencies.
- Match with project: This is suitable because the team receives "continuous feedback" from store-operations representatives, allowing them to adapt processes quickly as they onboard the full chain over 12 months.

Conclusion: Given the project's continuous delivery needs, incrementally changing integration requirements, and cross-functional feedback loops, the Kanban model is highly appropriate.

### Question 2

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
- Who: End-users, Clients, or Business Analysts (e.g., store-operations representatives). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

### Question 3

Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must allow the cashier to scan products at the point-of-sale (POS) terminal to record transactions.
2. The system must automatically apply any active promotions or loyalty discounts during checkout.
3. The system must decrement inventory at the store in real time after every transaction.
4. The system must automatically send a replenishment request to the nearest warehouse when a product falls below its re-order threshold.
5. The system must allow HQ administrators to configure product catalogues and pricing rules centrally.

**Security Requirements (3):**
1. The system must authenticate all users with role-based credentials and enforce multi-factor authentication (MFA) for manager and HQ accounts.
2. The system must encrypt all data in transit with TLS 1.3 and data at rest with AES-256.
3. The system must keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

### Question 4

Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal, so that I can quickly and accurately record the customer's transaction.
2. **User Story 2:** As a customer (or cashier), I want the system to automatically apply active promotions or loyalty discounts during checkout, so that the correct final price is calculated.
3. **User Story 3:** As a store manager, I want the system to decrement inventory in real time after every checkout, so that store stock levels are always accurate.
4. **User Story 4:** As a warehouse staff member, I want the system to automatically send a replenishment request when a product falls below its re-order threshold, so that I can quickly pick and pack orders to prevent stockouts.
5. **User Story 5:** As an HQ administrator, I want to configure product catalogues and pricing rules centrally, so that pricing updates are pushed consistently to all store locations simultaneously.

### Question 5

Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert and notification mechanism. For example, when a "pay discrepancy" is detected (the Subject changes state), the system automatically notifies all subscribed Observers, such as the store manager's local interface and the HQ finance team's dashboard. This ensures immediate awareness of issues without tightly coupling the checkout module to the reporting modules.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be used for the system's Audit Logger. Since the system must "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years," a Singleton Audit Logger ensures that all logs are written sequentially to a single centralized, protected stream. This prevents resource conflicts from concurrent POS sessions and maintains strict regulatory compliance.

### Question 6

A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan Products
   - 1.2 Apply Promotions
2. Complete Transaction
   - 2.1 Process Payment
   - 2.2 Issue Receipt
3. Update Operations
   - 3.1 Decrement Inventory
   - 3.2 Log Transaction

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS so I can quickly add them to the transaction.
- 2.1.1 As a cashier, I want to process standard payments so the customer can complete their purchase.
- 2.2.1 As a cashier, I want the system to issue a printed receipt so the customer has a record of the transaction.
- 3.1.1 As a store manager, I want the system to decrement inventory in real time so that stock levels remain accurate.

Release 2----------------------------------------------------------------------
- 1.2.1 As a cashier, I want the system to automatically apply active promotions so the final price is calculated correctly without manual checking.
- 1.2.2 As a cashier, I want the system to apply loyalty discounts so that registered customers receive their benefits automatically.
- 2.2.2 As a customer, I want to receive a digital receipt so I can keep an electronic record and reduce paper waste.
- 3.2.1 As an HQ administrator, I want the system to keep a tamper-evident audit log of every transaction so that regulatory compliance is met.


**GIAI ĐOẠN 4 — TỰ CHẤM**

| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Liệt kê đủ nguyên tắc Kanban và map với đề | Đạt | Không |
| Q2: Có nói RÕ type (white-box/black-box) ở phần a | Đạt | Không |
| Q2: Nêu rõ 4 level, Who, Why | Đạt | Không |
| Q3: Đúng số lượng 5 FR, 3 Security, 2 Scalability | Đạt | Không |
| Q4: Viết đúng 5 User stories | Đạt | Không |
| Q4: Không dùng "As a system", tuân thủ format | Đạt | Không |
| Q5: Đúng 2 Design Patterns (Observer, Singleton) | Đạt | Không |
| Q5: Có mô tả lý thuyết + giải thích ứng dụng vào Case Study | Đạt | Không |
| Q6: Đúng định dạng 2 phần A và B của EOS | Đạt | Không |
| Q6: User stories trong B map với tasks trong A | Đạt | Không |
