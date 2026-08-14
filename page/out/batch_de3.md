**GIAI ĐOẠN 1 — PHÂN LOẠI**
| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Câu 1 | Q1 - Software Development Model | "manager proposes applying the Kanban model", "Do you agree or disagree", "principles, practices" | Cao |
| Câu 2 | Q2 - Testing | "tested from the smallest unit level up to the fully integrated system level", "type and level/stage of testing" | Cao |
| Câu 3 | Q3 - Identify Requirements | "identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements" | Cao |
| Câu 4 | Q4 - User Stories | "Write 5 user stories based on your answers in Question 3" | Cao |
| Câu 5 | Q5 - Design Patterns | "apply design patterns", "list and describe in detail two design patterns" | Cao |
| Câu 6 | Q6 - Story Map | "Build a story map for the 'Manage Product Sales' activities", có phần "III Notes" | Cao |

**GIAI ĐOẠN 2 — MOI DỮ KIỆN**
**Câu 1:**
- `{{mo_hinh_duoc_de_xuat}}`: Kanban model
- `{{dac_diem_du_an}}`: A cross-functional team of 4-5 skilled developers, continuous feedback, integration requirements expected to emerge and change incrementally, new features delivered and deployed continuously.
- `{{dong_y_hay_khong}}`: Agree.

**Câu 2:**
- `{{yeu_cau_test}}`: from the smallest unit level up to the fully integrated system level.

**Câu 3:**
- `{{so_luong_FR}}`: 5
- `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}`: Security Requirements, 3
- `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}`: Scalability Requirements, 2

**Câu 4:**
- `{{so_luong_US}}`: 5
- `{{danh_sach_FR_tu_Q3}}`: 5 FRs từ câu 3.

**Câu 5:**
- `{{he_thong}}`: Convenient Store Chain Management System (CSCMS)
- `{{tinh_nang_ap_dung}}`: send alerts (pay discrepancy, automatic replenishment) -> Observer; keep tamper-evident audit log -> Singleton.

**Câu 6:**
- `{{tieu_diem_chinh}}`: Manage Product Sales
- `{{cac_chuc_nang}}`: scan products at POS, apply active promotions or loyalty discounts, issue receipt, decrement inventory in real time, automatic replenishment request.

**GIAI ĐOẠN 3 — BÀI LÀM**

**Question 1:**
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualize the Workflow: 
- Explanation: Kanban uses a visual board (Kanban board) to map out all tasks in the development process, allowing the team to see the flow of work.
- Match with project: This matches the project because a "cross-functional team of 4-5 developers, a business analyst, and store-operations representatives" needs a clear visualization of tasks to collaborate effectively.

2. Limit Work in Progress (WIP): 
- Explanation: Kanban limits the number of tasks in progress at any given time to avoid context switching and identify bottlenecks early.
- Match with project: This fits the project because "integration requirements are expected to emerge and change incrementally as stores are on-boarded one by one", requiring the team to focus on completing current tasks before taking on new ones.

3. Manage Flow: 
- Explanation: The model focuses on the continuous, smooth flow of work items through the process rather than time-boxed sprints.
- Match with project: This aligns well since the project requires "new features delivered and deployed continuously throughout" the 12-month rollout phase.

4. Continuous Feedback and Improvement: 
- Explanation: Kanban encourages ongoing collaboration and evolutionary changes to improve the process constantly.
- Match with project: This is suitable because the project involves "store-operations representatives who provide continuous feedback".

Conclusion: Given the project's continuous delivery requirements, emerging integration needs, and the presence of a cross-functional team with continuous feedback, the Kanban model is highly appropriate.

**Question 2:**
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

**Question 3:**
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The cashier must be able to scan products at the POS terminal to record the transaction.
2. The system must automatically apply any active promotions or loyalty discounts and issue a printed or digital receipt.
3. The system must automatically send a replenishment request to the nearest warehouse when a product falls below the re-order threshold.
4. Store managers must be able to view shift schedules and log daily cash reconciliation through a dashboard.
5. HQ administrators must be able to configure product catalogues and pricing rules centrally.

**Security Requirements (3):**
1. All users must authenticate with role-based credentials.
2. Multi-factor authentication (MFA) must be enforced for manager and HQ accounts.
3. All data in transit must be encrypted with TLS 1.3, and data at rest must be encrypted using AES-256.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

**Question 4:**
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal to record the transaction, so that customer checkouts are processed efficiently.
2. **User Story 2:** As a customer, I want the system to apply active promotions or loyalty discounts and issue a receipt, so that I get the correct price and proof of purchase.
3. **User Story 3:** As a store manager, I want the system to send an automatic replenishment request to the nearest warehouse when a product falls below the re-order threshold, so that the store never runs out of stock.
4. **User Story 4:** As a store manager, I want to view shift schedules and log daily cash reconciliation through a dashboard, so that store operations are managed smoothly.
5. **User Story 5:** As an HQ administrator, I want to configure product catalogues and pricing rules centrally, so that all stores have consistent and up-to-date product information.

**Question 5:**
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the real-time notification and alert system. For example, when a "pay discrepancy" occurs (the Subject changes state), the system automatically notifies all subscribed Observers, such as the store manager's dashboard and the HQ finance team, ensuring rapid response without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CSCMS, the Singleton pattern can be used for the system's Audit Logger. Since the system needs to "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change," a Singleton AuditLogger ensures that all logs are written sequentially to a single centralized stream, preventing resource conflicts and maintaining regulatory compliance.

**Question 6:**
A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan Products
   - 1.2 Process Payment
2. Apply Promotions
   - 2.1 Calculate Discounts
   - 2.2 Issue Receipt
3. Manage Inventory
   - 3.1 Update Stock
   - 3.2 Trigger Replenishment

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS terminal so that the system records the transaction.
- 1.2.1 As a cashier, I want to process standard payments so that the checkout can be completed.
- 2.2.1 As a customer, I want the system to issue a basic printed receipt so that I have a record of my purchase.
- 3.1.1 As a store manager, I want the system to decrement inventory in real time so that stock levels are accurate.

Release 2----------------------------------------------------------------------
- 2.1.1 As a customer, I want the system to apply active promotions or loyalty discounts so that I receive the correct price.
- 2.2.2 As a customer, I want the system to issue a digital receipt so that I can keep an electronic copy.
- 3.2.1 As a store manager, I want the system to send an automatic replenishment request when a product falls below the re-order threshold so that the store is always stocked.


**GIAI ĐOẠN 4 — TỰ CHẤM**
| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Trả lời Agree/Disagree rõ ràng | Đạt | Không |
| Q1: Liệt kê đủ các nguyên tắc cốt lõi của mô hình | Đạt | Không |
| Q1: Mỗi nguyên tắc đều có 1 câu map với dữ kiện | Đạt | Không |
| Q2: Liệt kê đủ 4 cấp độ và nêu rõ Who/Why | Đạt | Không |
| Q3: Đúng số lượng FRs/NFRs đề yêu cầu | Đạt | Không |
| Q3: Tất cả requirement lấy từ Case Study | Đạt | Không |
| Q4: Đúng số lượng user stories đề yêu cầu | Đạt | Không |
| Q4: Tuân thủ cú pháp As a... I want to... so that... | Đạt | Không |
| Q4: Map 1-1 với FRs ở Q3 | Đạt | Không |
| Q5: Chọn đúng 2 patterns, có mô tả lý thuyết chung | Đạt | Không |
| Q5: Có phần Áp dụng dính chặt với ngữ cảnh | Đạt | Không |
| Q6: Tuân thủ format 2 phần A và B của EOS | Đạt | Không |
| Q6: Đúng cấu trúc numbering (1.1, 1.1.1, v.v.) | Đạt | Không |
| Q6: User stories phải đủ chủ ngữ con người, "As a system..." là sai | Đạt | Không |

## BẢN NỘP
(Sử dụng nội dung Giai đoạn 3 làm bản nộp chính thức)
