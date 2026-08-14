# GIAI ĐOẠN 1 — PHÂN LOẠI
| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Câu 1 | Q1 - Software Development Model | "Kanban model", "manager suggests applying", "Do you agree or disagree" | Cao |
| Câu 2 | Q2 - Testing | "tested from the smallest unit level up to the fully integrated system level", "type and level/stage" | Cao |
| Câu 3 | Q3 - Identify Requirements | "identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements" | Cao |
| Câu 4 | Q4 - User Stories | "Write 5 user stories derived from your answers in Question 3" | Cao |
| Câu 5 | Q5 - Design Patterns | "apply some design patterns", "list and describe in detail two design patterns" | Cao |
| Câu 6 | Q6 - Story Map | "Build a story map for the 'Manage Product Sales' activities" | Cao |

# GIAI ĐOẠN 2 — MOI DỮ KIỆN
**Q1**
- `{{mo_hinh_duoc_de_xuat}}`: Kanban model
- `{{dac_diem_du_an}}`: "integration requirements are expected to emerge and change incrementally", "new features delivered and deployed continuously throughout", "cross-functional team of 4-5 developers".
- `{{dong_y_hay_khong}}`: Agree

**Q2**
- `{{yeu_cau_test}}`: from the smallest unit level up to the fully integrated system level

**Q3**
- `{{so_luong_FR}}`: 5 functional requirements
  - 1. Cashier scans products at the POS terminal.
  - 2. System applies any active promotions or loyalty discounts.
  - 3. System decrements inventory at the store in real time.
  - 4. System sends an automatic replenishment request to the nearest warehouse when product falls below re-order threshold.
  - 5. HQ administrators configure product catalogues and pricing rules centrally.
- `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}`: Security requirements, 3
  - 1. All users authenticate with role-based credentials, with multi-factor authentication (MFA) enforced for manager and HQ accounts.
  - 2. All data in transit is encrypted with TLS 1.3, data at rest is encrypted with AES-256.
  - 3. The system keeps a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.
- `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}`: Scalability requirements, 2
  - 1. The platform must support at least 200 concurrent POS sessions without performance degradation.
  - 2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

**Q4**
- `{{so_luong_US}}`: 5 user stories
- `{{danh_sach_FR_tu_Q3}}`: 5 Functional Requirements từ Q3.

**Q5**
- `{{he_thong}}`: Convenient Store Chain Management System (CSCMS)
- `{{tinh_nang_ap_dung}}`: 
  - Pattern 1: Observer (cho tính năng alert discrepancy).
  - Pattern 2: Singleton (cho tính năng Audit log).

**Q6**
- `{{tieu_diem_chinh}}`: Manage Product Sales
- `{{cac_chuc_nang}}`: scan products, apply promotions, record transaction, issue receipt, log daily cash reconciliation, pay discrepancy trigger alert.

# GIAI ĐOẠN 3 — BÀI LÀM

## 1. Kanban Model
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model [NGOÀI KHUÔN], and how they match the project characteristics:

1. Visualizing the Workflow: 
- Explanation: Kanban uses a board to visually represent the status of all tasks, helping teams see the big picture.
- Match with project: This matches the project because a "cross-functional team of 4-5 developers, a business analyst, and store-operations representatives" needs to collaborate and track tasks transparently.

2. Managing and Optimizing Flow: 
- Explanation: Kanban focuses on ensuring a smooth and continuous flow of work from start to finish without time-boxed sprints.
- Match with project: This fits the project perfectly since "new features delivered and deployed continuously throughout" the 12-month rollout.

3. Limit Work in Progress (WIP): 
- Explanation: Kanban restricts the number of active tasks at any given time to avoid bottlenecks and focus on finishing current work.
- Match with project: This aligns well since the team faces a tight deadline where "the first stores to go live within 2 months", requiring high focus on core features first.

4. Embracing Incremental Change: 
- Explanation: Kanban encourages small, continuous improvements rather than sweeping process changes.
- Match with project: This is suitable because "integration requirements are expected to emerge and change incrementally as stores are on-boarded one by one".

Conclusion: Given the project's evolving requirements, continuous delivery expectation, and the need to incrementally onboard independent stores, the Kanban model is highly appropriate.

## 2. Testing Types and Levels
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

## 3. Identify Requirements
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must allow the cashier to scan products at the point-of-sale (POS) terminal during checkout.
2. The system must automatically apply any active promotions or loyalty discounts to the transaction.
3. The system must decrement inventory at the store in real time after a checkout.
4. The system must send an automatic replenishment request to the nearest warehouse when a product falls below its re-order threshold.
5. The system must allow HQ administrators to configure product catalogues and pricing rules centrally.

**Security Requirements (3):**
1. All users authenticate with role-based credentials, with multi-factor authentication (MFA) enforced for manager and HQ accounts.
2. All data in transit is encrypted with TLS 1.3, and data at rest is encrypted with AES-256.
3. The system keeps a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

## 4. User Stories
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal so that I can quickly process the customer's checkout.
2. **User Story 2:** As a cashier, I want the system to apply any active promotions or loyalty discounts so that the customer is charged the correct discounted amount.
3. **User Story 3:** As a store manager, I want the system to decrement inventory in real time so that our stock levels are always accurate.
4. **User Story 4:** As a warehouse staff member, I want the system to send an automatic replenishment request when a product falls below the re-order threshold so that the store never runs out of stock.
5. **User Story 5:** As an HQ administrator, I want to configure product catalogues and pricing rules centrally so that all stores have unified and up-to-date pricing.

## 5. Design Patterns
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern** [NGOÀI KHUÔN]
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the real-time alert system. For example, when a "pay discrepancy triggers an alert" (as stated in the case study), the Shift Management Module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the Store Manager's Dashboard and the HQ Finance Team's system, ensuring rapid response without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern** [NGOÀI KHUÔN]
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be used for managing the audit logger. Since the system needs to "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change," a Singleton AuditLogger ensures that all security logs are written sequentially to a single centralized stream, preventing resource conflicts and ensuring data integrity.

## 6. Story Map
A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan Products
   - 1.2 Finalize Transaction
2. Handle Promotions
   - 2.1 Apply Discounts
3. Reconcile Sales
   - 3.1 Log Daily Cash
   - 3.2 Handle Discrepancies

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS terminal so that I can quickly add items to the customer's bill.
- 1.2.1 As a cashier, I want the system to record the transaction and issue a printed receipt so that the sale is finalized.
- 3.1.1 As a store manager, I want to log daily cash reconciliation so that I can ensure the cash register matches the system records.

Release 2----------------------------------------------------------------------
- 1.2.2 As a cashier, I want the system to issue a digital receipt as an alternative to printed ones so that paper waste is reduced.
- 2.1.1 As a cashier, I want the system to automatically apply active promotions or loyalty discounts so that the customer is charged the correct amount.
- 3.2.1 As a store manager, I want the system to trigger an alert to HQ finance if a pay discrepancy is found so that it can be investigated promptly.


# GIAI ĐOẠN 4 — TỰ CHẤM
| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1 - Đã trả lời Agree/Disagree rõ ràng | Đạt | Không |
| Q1 - Đã liệt kê đủ các nguyên tắc cốt lõi của mô hình | Đạt | Đã liệt kê 4 đặc điểm của Kanban |
| Q1 - Mỗi nguyên tắc đều có 1 câu map với dữ kiện cụ thể trong đề | Đạt | Không |
| Q2 - Đã liệt kê đủ 4 cấp độ | Đạt | Không |
| Q2 - Đã nêu rõ "Who" và "Why" cho từng cấp độ | Đạt | Không |
| Q3 - Đúng số lượng FRs, Security, Scalability | Đạt | Đúng 5 FR, 3 Security, 2 Scalability |
| Q3 - Tất cả requirement lấy từ đề | Đạt | Không |
| Q4 - Đúng số lượng user stories | Đạt | Đúng 5 stories |
| Q4 - Cú pháp chuẩn "As a... I want... so that..." | Đạt | Không |
| Q5 - Chọn đúng 2 patterns và mô tả | Đạt | Observer và Singleton |
| Q5 - Áp dụng dính chặt với ngữ cảnh | Đạt | Đã map với Pay discrepancy và Audit log |
| Q6 - Tuân thủ format 2 phần A và B | Đạt | Không |
| Q6 - Viết user stories bám sát tasks phần A | Đạt | Không |
| Q6 - Không dùng "As a system" | Đạt | Cú pháp "As a cashier, I want the system to..." |

# BẢN NỘP
## 1. Kanban Model
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualizing the Workflow: 
- Explanation: Kanban uses a board to visually represent the status of all tasks, helping teams see the big picture.
- Match with project: This matches the project because a "cross-functional team of 4-5 developers, a business analyst, and store-operations representatives" needs to collaborate and track tasks transparently.

2. Managing and Optimizing Flow: 
- Explanation: Kanban focuses on ensuring a smooth and continuous flow of work from start to finish without time-boxed sprints.
- Match with project: This fits the project perfectly since "new features delivered and deployed continuously throughout" the 12-month rollout.

3. Limit Work in Progress (WIP): 
- Explanation: Kanban restricts the number of active tasks at any given time to avoid bottlenecks and focus on finishing current work.
- Match with project: This aligns well since the team faces a tight deadline where "the first stores to go live within 2 months", requiring high focus on core features first.

4. Embracing Incremental Change: 
- Explanation: Kanban encourages small, continuous improvements rather than sweeping process changes.
- Match with project: This is suitable because "integration requirements are expected to emerge and change incrementally as stores are on-boarded one by one".

Conclusion: Given the project's evolving requirements, continuous delivery expectation, and the need to incrementally onboard independent stores, the Kanban model is highly appropriate.

## 2. Testing Types and Levels
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

## 3. Identify Requirements
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must allow the cashier to scan products at the point-of-sale (POS) terminal during checkout.
2. The system must automatically apply any active promotions or loyalty discounts to the transaction.
3. The system must decrement inventory at the store in real time after a checkout.
4. The system must send an automatic replenishment request to the nearest warehouse when a product falls below its re-order threshold.
5. The system must allow HQ administrators to configure product catalogues and pricing rules centrally.

**Security Requirements (3):**
1. All users authenticate with role-based credentials, with multi-factor authentication (MFA) enforced for manager and HQ accounts.
2. All data in transit is encrypted with TLS 1.3, and data at rest is encrypted with AES-256.
3. The system keeps a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

## 4. User Stories
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal so that I can quickly process the customer's checkout.
2. **User Story 2:** As a cashier, I want the system to apply any active promotions or loyalty discounts so that the customer is charged the correct discounted amount.
3. **User Story 3:** As a store manager, I want the system to decrement inventory in real time so that our stock levels are always accurate.
4. **User Story 4:** As a warehouse staff member, I want the system to send an automatic replenishment request when a product falls below the re-order threshold so that the store never runs out of stock.
5. **User Story 5:** As an HQ administrator, I want to configure product catalogues and pricing rules centrally so that all stores have unified and up-to-date pricing.

## 5. Design Patterns
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the real-time alert system. For example, when a "pay discrepancy triggers an alert" (as stated in the case study), the Shift Management Module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the Store Manager's Dashboard and the HQ Finance Team's system, ensuring rapid response without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be used for managing the audit logger. Since the system needs to "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change," a Singleton AuditLogger ensures that all security logs are written sequentially to a single centralized stream, preventing resource conflicts and ensuring data integrity.

## 6. Story Map
A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan Products
   - 1.2 Finalize Transaction
2. Handle Promotions
   - 2.1 Apply Discounts
3. Reconcile Sales
   - 3.1 Log Daily Cash
   - 3.2 Handle Discrepancies

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS terminal so that I can quickly add items to the customer's bill.
- 1.2.1 As a cashier, I want the system to record the transaction and issue a printed receipt so that the sale is finalized.
- 3.1.1 As a store manager, I want to log daily cash reconciliation so that I can ensure the cash register matches the system records.

Release 2----------------------------------------------------------------------
- 1.2.2 As a cashier, I want the system to issue a digital receipt as an alternative to printed ones so that paper waste is reduced.
- 2.1.1 As a cashier, I want the system to automatically apply active promotions or loyalty discounts so that the customer is charged the correct amount.
- 3.2.1 As a store manager, I want the system to trigger an alert to HQ finance if a pay discrepancy is found so that it can be investigated promptly.
