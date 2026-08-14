# KẾT QUẢ THỰC THI P4

## GIAI ĐOẠN 1 — PHÂN LOẠI
| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| 1 | Q1-Software_Development_Model.md | "Kanban model", "manager proposes applying", "Do you agree or disagree" | 100% |
| 2 | Q2-Testing.md | "smallest unit level up to the fully integrated system level", "type and level/stage of testing" | 100% |
| 3 | Q3-Identify_Requirements.md | "identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements" | 100% |
| 4 | Q4-User_Stories.md | "Write 5 user stories based on your answers in Question 3" | 100% |
| 5 | Q5-Design_Patterns.md | "apply design patterns", "describe in detail two design patterns" | 100% |
| 6 | Q6-Story_Map.md | "Build a story map", "Manage Product Sales" | 100% |

## GIAI ĐOẠN 2 — MOI DỮ KIỆN

**Câu 1:**
- `{{mo_hinh_duoc_de_xuat}}`: Kanban model
- `{{dac_diem_du_an}}`: Nhóm có 4-5 dev kinh nghiệm, requirements sẽ "emerge and change incrementally", continuous delivery (new features delivered continuously), timeline kéo dài (12 months).
- `{{dong_y_hay_khong}}`: Agree

**Câu 2:**
- `{{yeu_cau_test}}`: from the smallest unit level up to the fully integrated system level

**Câu 3:**
- `{{so_luong_FR}}`: 5 functional requirements
- `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}`: Security, 3
- `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}`: Scalability, 2

**Câu 4:**
- `{{so_luong_US}}`: 5 user stories
- `{{danh_sach_FR_tu_Q3}}`: 5 Functional Requirements từ Câu 3

**Câu 5:**
- `{{he_thong}}`: Convenient Store Chain Management System (CSCMS)
- `{{tinh_nang_ap_dung}}`: Observer (alert for pay discrepancy) và Singleton (tamper-evident audit log)

**Câu 6:**
- `{{tieu_diem_chinh}}`: Manage Product Sales
- `{{cac_chuc_nang}}`: POS checkout, apply promotions, issue receipt, update inventory, auto-replenishment.

## GIAI ĐOẠN 3 — BÀI LÀM
(Bản nháp được giữ nguyên và tinh chỉnh ở Giai đoạn 4, kết quả cuối cùng nằm ở phần Bản Nộp).

## GIAI ĐOẠN 4 — TỰ CHẤM
| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Trả lời Agree/Disagree và có lý do match Case Study | Đạt | Không |
| Q2: Đủ 4 cấp độ Test và Who/Why | Đạt | Không |
| Q3: Trích đúng số lượng FRs, Security, Scalability từ đề | Đạt | Không |
| Q4: Viết đúng 5 User Stories từ Q3, đủ vế "So that" | Đạt | Không |
| Q5: Nêu 2 Pattern, mô tả và ứng dụng vào CSCMS | Đạt | Không |
| Q6: Đúng format A/B của EOS, numbering chuẩn | Đạt | Không |

---

## BẢN NỘP

**Question 1**
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualizing the Workflow:
- Explanation: Kanban uses a visual board to map out the entire process, showing the status of work items.
- Match with project: This matches the project requirement of having a cross-functional team and continuous feedback from store-operations representatives, making work visible to all stakeholders.

2. Limiting Work in Progress (WIP):
- Explanation: Kanban restricts the number of active tasks at any given stage to prevent bottlenecks and ensure quality.
- Match with project: This fits the project because the development team is small (4-5 developers) and needs to manage changing scopes smoothly since "integration requirements are expected to emerge and change incrementally."

3. Managing Flow and Continuous Delivery:
- Explanation: Kanban focuses on a smooth, continuous flow of tasks from start to finish without rigid timeboxed sprints.
- Match with project: This aligns well since the project requires "new features delivered and deployed continuously throughout" the 12-month rollout.

4. Incremental and Evolutionary Change:
- Explanation: Kanban encourages small, continuous improvements rather than sweeping, disruptive changes.
- Match with project: This is suitable because the system replaces legacy tools incrementally "as stores are on-boarded one by one."

Conclusion: Given the project's need for continuous delivery, evolving requirements, and incremental onboarding, the Kanban model is highly appropriate.

**Question 2**
a. Types and levels/stages of testing required by the manager:
Based on the requirement to test from the smallest unit level up to the fully integrated system level, the manager requires the following stages:
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

**Question 3**
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must allow the cashier to scan products at the point-of-sale (POS) terminal to record transactions.
2. The system must automatically apply any active promotions or loyalty discounts during checkout.
3. The system must issue a printed or digital receipt for the customer after a transaction.
4. The system must decrement store inventory in real time and automatically send a replenishment request to the nearest warehouse when a product falls below the re-order threshold.
5. The system must trigger an alert to both the store manager and the HQ finance team when any pay discrepancy is logged.

**Security Requirements (3):**
1. All users must authenticate with role-based credentials, and multi-factor authentication (MFA) must be enforced for manager and HQ accounts.
2. All data in transit must be encrypted with TLS 1.3, and data at rest must be encrypted using AES-256.
3. The system must keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

**Question 4**
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal so that the system can record the transaction quickly.
2. **User Story 2:** As a cashier, I want the system to automatically apply active promotions or loyalty discounts during checkout so that the customer pays the correct discounted amount.
3. **User Story 3:** As a cashier, I want to issue a printed or digital receipt so that the customer has a physical or digital record of their purchase.
4. **User Story 4:** As a store manager, I want the system to decrement inventory and automatically send a replenishment request to the warehouse when stock is low so that the store never runs out of products.
5. **User Story 5:** As an HQ finance administrator, I want to receive an alert whenever a pay discrepancy is logged so that I can investigate and resolve financial issues immediately.

**Question 5**
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert system for pay discrepancies. For example, when a "pay discrepancy" is logged by the system (the Subject), it automatically notifies all subscribed Observers, such as the Store Manager's dashboard and the HQ finance team, so they can react accordingly without tight coupling.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be used for managing the audit logger. Since the system "keeps a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years", a Singleton AuditLogger ensures that all log entries are written sequentially to a single centralized stream or file, preventing resource conflicts and ensuring the log remains tamper-evident.

**Question 6**
A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan Products
   - 1.2 Complete Payment
2. Manage Promotions and Loyalty
   - 2.1 Apply Active Promotions
   - 2.2 Apply Loyalty Discounts
3. Handle Post-Transaction
   - 3.1 Issue Receipt
   - 3.2 Update Inventory and Replenishment

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS so the system can record the transaction.
- 1.2.1 As a cashier, I want to complete the payment so the transaction is finalized.
- 2.1.1 As a cashier, I want the system to automatically apply active promotions so the customer gets the correct price.
- 3.1.1 As a cashier, I want to issue a printed receipt so the customer has a record.
- 3.2.1 As a system, I want to decrement store inventory in real time so stock levels are accurate.

Release 2----------------------------------------------------------------------
- 2.2.1 As a cashier, I want the system to apply loyalty discounts so member customers are rewarded.
- 3.1.2 As a cashier, I want to issue a digital receipt so we can save paper.
- 3.2.2 As a system, I want to automatically send a replenishment request to the nearest warehouse when stock falls below the re-order threshold so we don't run out of products.
