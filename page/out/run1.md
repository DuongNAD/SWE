# P4 — BÀI LÀM SWE202c

## GIAI ĐOẠN 1 — PHÂN LOẠI
| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Q1 | `Q1-Software_Development_Model.md` | `Kanban model`, `manager proposes applying...` | Cao |
| Q2 | `Q2-Testing.md` | `tested from the smallest unit level up to the fully integrated system level` | Cao |
| Q3 | `Q3-Identify_Requirements.md` | `identify and list: 5 functional requirements, 3 security requirements, and 2 scalability requirements` | Cao |
| Q4 | `Q4-User_Stories.md` | `Write 5 user stories based on your answers in Question 3` | Cao |
| Q5 | `Q5-Design_Patterns.md` | `apply design patterns`, `list and describe in detail two design patterns` | Cao |
| Q6 | `Q6-Story_Map.md` | `Build a story map for the "Manage Product Sales" activities` | Cao |

## GIAI ĐOẠN 2 — MOI DỮ KIỆN
**Q1:**
- `{{mo_hinh_duoc_de_xuat}}`: Kanban model
- `{{dac_diem_du_an}}`: Nhóm cross-functional 4-5 dev + BA + operations reps; requirements emerge and change incrementally; continuous deployment; continuous feedback.
- `{{dong_y_hay_khong}}`: Agree

**Q2:**
- `{{yeu_cau_test}}`: from the smallest unit level up to the fully integrated system level. At unit level, focus on program structure; at higher levels, based on functional requirements.

**Q3:**
- `{{so_luong_FR}}`: 5
- `{{loai_NFR_1}}`, `{{so_luong_NFR_1}}`: Security requirements, 3
- `{{loai_NFR_2}}`, `{{so_luong_NFR_2}}`: Scalability requirements, 2

**Q4:**
- `{{so_luong_US}}`: 5
- `{{danh_sach_FR_tu_Q3}}`: 5 FRs từ Q3

**Q5:**
- `{{he_thong}}`: Convenient Store Chain Management System (CSCMS)
- `{{tinh_nang_ap_dung}}`: Alert for pay discrepancy (Observer Pattern); Tamper-evident audit log (Singleton Pattern).

**Q6:**
- `{{tieu_diem_chinh}}`: "Manage Product Sales"
- `{{cac_chuc_nang}}`: scan products at POS, record transaction, apply promotions/discounts, issue receipt, decrement inventory, automatic replenishment.

## GIAI ĐOẠN 3 — BÀI LÀM (DRAFT)
(Phần này được tích hợp thẳng vào Bản Nộp ở Giai đoạn 4 để tiết kiệm không gian, quá trình làm đã tuân thủ đúng định dạng của khuôn).

## GIAI ĐOẠN 4 — TỰ CHẤM
| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| **Q1:** Trả lời Agree/Disagree rõ ràng | Đạt | Không |
| **Q1:** Liệt kê đủ nguyên tắc, có map với đề | Đạt | Không |
| **Q2:** Liệt kê đủ 4 cấp độ kiểm thử, có Who/Why | Đạt | Không |
| **Q3:** Đúng số lượng (5 FR, 3 Sec, 2 Scalability) | Đạt | Không |
| **Q3:** NFR có con số trích từ đề | Đạt | Không |
| **Q4:** Đủ 5 US, có đủ 3 vế (As a, I want to, So that) | Đạt | Không |
| **Q5:** Nêu đủ 2 Design Patterns, mô tả và áp dụng | Đạt | Không |
| **Q6:** Đúng cấu trúc A (Activities/Tasks) và B (Releases) | Đạt | Không |
| **Q6:** Đánh số đúng (1.1 -> 1.1.1), dạng text | Đạt | Không |

---

## BẢN NỘP

### Question 1
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualize the Workflow:
- Explanation: Kanban uses a visual board to show all work items and their status across different stages of development.
- Match with project: This matches the project because a cross-functional team of 4-5 developers, a BA, and reps need a shared view to collaborate effectively as "integration requirements are expected to emerge and change incrementally".

2. Limit Work in Progress (WIP):
- Explanation: Kanban restricts the number of active tasks at any given time to identify bottlenecks and avoid context switching.
- Match with project: This fits the project because "new features delivered and deployed continuously" requires the team to finish current tasks before pulling new ones, ensuring steady delivery across the 12-month timeline.

3. Manage Flow:
- Explanation: Kanban focuses on the smooth, continuous delivery of work items rather than time-boxed sprints.
- Match with project: This aligns well since the full chain will be covered "incrementally as stores are on-boarded one by one", demanding a continuous flow rather than rigid iterations.

4. Implement Feedback Loops and Improve Collaboratively:
- Explanation: Kanban encourages regular review of the process for continuous improvement based on team feedback.
- Match with project: This is suitable because the project involves "store-operations representatives who provide continuous feedback" to refine the system as it rolls out to over 200 stores.

Conclusion: Given the project's traits like evolving integration requirements, the need for continuous delivery of new features, and a cross-functional collaborative team, the Kanban model is highly appropriate.

### Question 2
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
- Who: End-users, Clients, or Business Analysts (e.g., store-operations representatives). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

### Question 3
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must allow cashiers to scan products at the POS terminal and record the transaction.
2. The system must automatically apply active promotions or loyalty discounts during checkout.
3. The system must automatically send a replenishment request to the nearest warehouse when a product falls below the re-order threshold.
4. The system must allow warehouse staff to receive pick-and-pack orders on their handheld devices and update the dispatch status after delivery.
5. The system must trigger an alert to both the store manager and the HQ finance team if any pay discrepancy is logged in the daily cash reconciliation.

**Security Requirements (3):**
1. All users must authenticate with role-based credentials, and multi-factor authentication (MFA) must be enforced for manager and HQ accounts.
2. All data in transit must be encrypted with TLS 1.3, and data at rest must be encrypted using AES-256.
3. The system must keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change for at least three years.

**Scalability Requirements (2):**
1. The platform must support at least 200 concurrent POS sessions without performance degradation.
2. The backend must scale horizontally through container orchestration so that adding new stores requires no manual infrastructure changes.

### Question 4
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal to record the transaction so that customers can check out quickly and efficiently.
2. **User Story 2:** As a customer, I want the system to automatically apply active promotions or loyalty discounts during checkout so that I can receive the correct discounted price.
3. **User Story 3:** As a store manager, I want the system to automatically send a replenishment request to the nearest warehouse when stock falls below the threshold so that the store never runs out of products.
4. **User Story 4:** As a warehouse staff member, I want to receive pick-and-pack orders on my handheld device and update the dispatch status so that the system can automatically reconcile stock across all locations.
5. **User Story 5:** As an HQ finance team member, I want to receive an alert whenever there is a pay discrepancy in the daily cash reconciliation so that financial irregularities can be investigated immediately.

### Question 5
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert and notification mechanism. For example, when a "pay discrepancy" is logged during daily cash reconciliation, the reconciliation module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the store manager's dashboard and the HQ finance team's system, ensuring prompt alerts without tight coupling.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CSCMS, the Singleton pattern can be used for managing the audit logging service. Since the system needs to "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change," a Singleton AuditLogger ensures that all log entries across different modules are written sequentially to a single centralized log stream, preventing resource conflicts and ensuring data consistency.

### Question 6
A. Activities and User tasks

1. Process Customer Checkout
   - 1.1 Scan Products
   - 1.2 Apply Discounts
   - 1.3 Issue Receipt
2. Manage Inventory Operations
   - 2.1 Update Stock Levels
   - 2.2 Reorder Products
3. Fulfill Warehouse Orders
   - 3.1 Receive Orders
   - 3.2 Dispatch Goods

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a cashier, I want to scan products at the POS terminal so that the system records the transaction.
- 1.3.1 As a cashier, I want to issue a basic printed receipt so that the customer has proof of purchase.
- 2.1.1 As a system, I want to decrement store inventory in real time so that stock levels are accurate.
- 3.1.1 As warehouse staff, I want to receive pick-and-pack orders on my handheld device so that I can prepare the items for dispatch.

Release 2----------------------------------------------------------------------
- 1.2.1 As a customer, I want the system to automatically apply active promotions or loyalty discounts so that I get the correct price.
- 1.3.2 As a customer, I want to receive a digital receipt so that I can save paper and keep a digital record.
- 2.2.1 As a store manager, I want the system to send automatic replenishment requests to the warehouse when a product falls below the threshold so that we avoid stockouts.
- 3.2.1 As warehouse staff, I want to update the dispatch status after delivery so that the system reconciles stock across all locations automatically.
