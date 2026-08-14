**GIAI ĐOẠN 1 — PHÂN LOẠI**

| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| 1 | Q1-Software_Development_Model | "proposes applying the Kanban model... Do you agree or disagree" | Cao |
| 2 | Q2-Testing | "tested from the smallest unit level up to the fully integrated system level", "Which type and level/stage" | Cao |
| 3 | Q3-Identify_Requirements | "identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements." | Cao |
| 4 | Q4-User_Stories | "Write 5 user stories based on your answers in Question 3." | Cao |
| 5 | Q5-Design_Patterns | "apply design patterns... List and describe in detail two design patterns" | Cao |
| 6 | Q6-Story_Map | "Build a story map for the 'Manage Product Sales' activities" | Cao |

**GIAI ĐOẠN 2 — MOI DỮ KIỆN**

**Q1**
| Biến | Giá trị |
|---|---|
| `{{mo_hinh_duoc_de_xuat}}` | Kanban model |
| `{{dac_diem_du_an}}` | rapidly expanding retail business, chain of over 200 convenient stores, replacing fragmented spreadsheets with centralized CSCMS, integration requirements expected to emerge and change incrementally, cross-functional team of 4-5 developers, continuous feedback, full chain covered within 12 months with continuous delivery. |
| `{{dong_y_hay_khong}}` | Agree |

**Q2**
| Biến | Giá trị |
|---|---|
| `{{yeu_cau_test}}` | from the smallest unit level up to the fully integrated system level |

**Q3**
| Biến | Giá trị |
|---|---|
| `{{so_luong_FR}}` | 5 functional requirements |
| `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}` | Security, 3 |
| `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}` | Scalability, 2 |

**Q4**
| Biến | Giá trị |
|---|---|
| `{{so_luong_US}}` | 5 user stories |
| `{{danh_sach_FR_tu_Q3}}` | Lấy từ 5 FRs ở Q3 |

**Q5**
| Biến | Giá trị |
|---|---|
| `{{he_thong}}` | Convenient Store Chain Management System (CSCMS) |
| `{{tinh_nang_ap_dung}}` | Observer (cho pay discrepancy alert), Singleton (cho tamper-evident audit log) |

**Q6**
| Biến | Giá trị |
|---|---|
| `{{tieu_diem_chinh}}` | Manage Product Sales |
| `{{cac_chuc_nang}}` | scan products at POS, apply promotions/discounts, issue receipt, decrement inventory, trigger replenishment requests, log daily cash reconciliation, record transactions. |

**GIAI ĐOẠN 3 — BÀI LÀM**

**Question 1**
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualize the workflow: 
- Explanation: Kanban uses a visual board to map out the stages of development so everyone sees the status of tasks.
- Match with project: This matches the project because a "cross-functional team of 4-5 developers, a business analyst, and store-operations representatives" needs a clear shared view to collaborate and provide "continuous feedback".

2. Limit Work In Progress (WIP): 
- Explanation: Kanban restricts the number of tasks in progress to prevent bottlenecks and ensure faster delivery of specific features.
- Match with project: This fits the project perfectly since the small team is under a tight deadline, expecting the "first stores to go live within 2 months".

3. Manage and enhance the flow: 
- Explanation: Kanban focuses on smooth and continuous delivery rather than fixed-length iterations.
- Match with project: This aligns well since new features are "delivered and deployed continuously throughout" the 12-month rollout.

4. Make process policies explicit and Evolve experimentally: 
- Explanation: Kanban encourages clear rules and adapting the process gradually without disrupting current operations.
- Match with project: This is suitable because the "integration requirements are expected to emerge and change incrementally as stores are on-boarded one by one".

Conclusion: Given the project's continuous delivery needs, emerging requirements, and cross-functional team, the Kanban model is highly appropriate.

**Question 2**
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
- Who: End-users, Clients, or Business Analysts (e.g., Store-operations representatives). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

**Question 3**
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. Cashiers must be able to scan products at the POS terminal to record transactions.
2. The system must allow cashiers to apply any active promotions or loyalty discounts during checkout.
3. The system must issue a printed or digital receipt when a customer checks out.
4. Store managers must be able to view shift schedules and log daily cash reconciliation through a dashboard.
5. HQ administrators must be able to configure product catalogues and pricing rules centrally.

**Security Requirements (3):**
1. All users must authenticate with role-based credentials, and multi-factor authentication (MFA) must be enforced for manager and HQ accounts.
2. All data in transit must be encrypted with TLS 1.3, and data at rest must be encrypted using AES-256.
3. The system must keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

**Question 4**
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal to record transactions, so that customers can check out quickly and efficiently.
2. **User Story 2:** As a cashier, I want to apply active promotions or loyalty discounts during checkout, so that customers receive their eligible benefits.
3. **User Story 3:** As a cashier, I want to issue a printed or digital receipt, so that the customer has a clear record of their purchase.
4. **User Story 4:** As a store manager, I want to view shift schedules and log daily cash reconciliation on a dashboard, so that I can effectively manage store operations and finances.
5. **User Story 5:** As an HQ administrator, I want to configure product catalogues and pricing rules centrally, so that changes are applied consistently across all store locations.

**Question 5**
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert system for pay discrepancies. For example, when a discrepancy occurs during the daily cash reconciliation, the reconciliation module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the Store Manager's Dashboard and the HQ finance team's notification service, ensuring both parties receive the alert immediately without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be used for managing the audit log. Since the system must "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change", a Singleton AuditLogger ensures that all logs from various modules are written sequentially and safely to a single centralized file or stream, preventing resource conflicts and maintaining the integrity of the records.

**Question 6**
A. Activities and User tasks

1. Process Checkout
   - 1.1 Scan products
   - 1.2 Apply discounts
   - 1.3 Issue receipt
2. Update Inventory
   - 2.1 Trigger replenishment
3. Manage Operations
   - 3.1 Log cash reconciliation

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS terminal so I can record the transaction.
- 1.3.1 As a cashier, I want to issue a printed receipt so the customer has a record of the purchase.
- 2.1.1 As a warehouse staff member, I want the system to receive automatic replenishment requests so I can pick and pack orders.
- 3.1.1 As a store manager, I want to log daily cash reconciliation so the day's earnings are recorded.

Release 2----------------------------------------------------------------------
- 1.2.1 As a cashier, I want to apply active promotions or loyalty discounts so customers get their eligible benefits.
- 1.3.2 As a cashier, I want to issue a digital receipt so the customer receives an eco-friendly record.


**GIAI ĐOẠN 4 — TỰ CHẤM**

| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Có Agree/Disagree rõ ràng | Đạt | Không |
| Q1: Liệt kê đủ nguyên tắc của mô hình | Đạt | Không |
| Q1: Map nguyên tắc với Case Study | Đạt | Không |
| Q2: Có Type rõ ràng là white-box/black-box | Đạt | Không |
| Q2: Có đủ Level, Who, Why | Đạt | Không |
| Q3: Đúng số lượng 5 FRs | Đạt | Không |
| Q3: Đúng số lượng 3 Security, 2 Scalability | Đạt | Không |
| Q4: 5 User stories | Đạt | Không |
| Q4: Không dùng "As a system" | Đạt | Không |
| Q4: Tuân thủ "As a... I want to... so that..." | Đạt | Không |
| Q5: Nêu đúng 2 patterns | Đạt | Không |
| Q5: Mô tả lý thuyết và áp dụng thực tế | Đạt | Không |
| Q6: Đúng chuẩn form A/B của EOS | Đạt | Không |

## BẢN NỘP
*(Nội dung BẢN NỘP đã hoàn hảo ở Giai đoạn 3, không có mục "Chưa" nào cần phải sửa lại. Bạn có thể sử dụng trực tiếp nội dung Giai đoạn 3 để nộp bài).*
