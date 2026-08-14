# BẢN NỘP

## Question 1
I agree with the manager's suggestion to apply the Kanban model to this project.

Here are the main principles, practices, and characteristics of the Kanban model, and how they match the project characteristics:

1. Visualize the Workflow:
- Explanation: Kanban uses a visual board to show all work items and their status across different stages of development.
- Match with project: This matches the project because a cross-functional team of 4-5 developers, a business analyst, and store-operations representatives needs a shared view to collaborate effectively as "integration requirements are expected to emerge and change incrementally".

2. Limit Work in Progress (WIP):
- Explanation: Kanban restricts the number of active tasks at any given stage to prevent bottlenecks and ensure quality.
- Match with project: This fits the project because the development team is small (4-5 developers) and needs steady, focused development to ensure the "first stores go live within 2 months".

3. Manage Flow and Continuous Delivery:
- Explanation: Kanban focuses on the smooth, continuous delivery of work items without rigid time-boxed sprints.
- Match with project: This aligns well since the project requires "new features delivered and deployed continuously throughout" the 12-month rollout.

4. Implement Feedback Loops and Improve Collaboratively:
- Explanation: Kanban encourages regular reviews and continuous feedback from stakeholders to adapt to changes and improve the process.
- Match with project: This is suitable because the project involves "store-operations representatives who provide continuous feedback" to refine the system as it rolls out to over 200 stores.

Conclusion: Given the project's traits like evolving integration requirements, the need for continuous delivery of new features, and a cross-functional collaborative team, the Kanban model is highly appropriate.

## Question 2
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

## Question 3
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

## Question 4
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a cashier, I want to scan products at the POS terminal to record the transaction so that customers can check out quickly and efficiently.
2. **User Story 2:** As a customer, I want the system to automatically apply active promotions or loyalty discounts during checkout so that I can receive the correct discounted price.
3. **User Story 3:** As a store manager, I want the system to automatically send a replenishment request to the nearest warehouse when stock falls below the threshold so that the store never runs out of products.
4. **User Story 4:** As a warehouse staff member, I want to receive pick-and-pack orders on my handheld device and update the dispatch status so that the system can automatically reconcile stock across all locations.
5. **User Story 5:** As an HQ finance team member, I want to receive an alert whenever there is a pay discrepancy in the daily cash reconciliation so that financial irregularities can be investigated immediately.

## Question 5
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Convenient Store Chain Management System (CSCMS), this pattern can be applied to the alert and notification mechanism. For example, when a "pay discrepancy" is logged during daily cash reconciliation, the reconciliation module (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the store manager's dashboard and the HQ finance team's system, ensuring prompt alerts without tight coupling.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CSCMS, the Singleton pattern can be used for managing the audit logging service. Since the system needs to "keep a tamper-evident audit log of every transaction, stock adjustment, and configuration change," a Singleton AuditLogger ensures that all log entries across different modules are written sequentially to a single centralized log stream, preventing resource conflicts and ensuring data consistency.

## Question 6
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
- 2.1.1 As a store manager, I want the system to record the transaction so that the sales data is saved securely.
- 2.2.1 As a cashier, I want to issue a printed receipt so that the customer has proof of purchase.
- 3.1.1 As a store manager, I want the system to decrement store inventory in real time so that stock levels are accurate.

Release 2----------------------------------------------------------------------
- 1.2.1 As a store manager, I want the system to apply active promotions or loyalty discounts so that the customer gets the correct price automatically.
- 2.2.2 As a cashier, I want to issue a digital receipt so that the customer can receive it via email or SMS.
- 3.2.1 As a store manager, I want the system to send an automatic replenishment request to the warehouse when a product falls below the threshold so that the store does not run out of stock.

---

## CẦN NGƯỜI KIỂM TRA
- Q1 (Nguyên tắc Kanban 4): BẤT ĐỒNG - Run 1 chọn "Feedback Loops", Run 2 chọn "Incremental Change", Run 3 chọn "Make Policies Explicit". Đã chọn "Feedback Loops" (Run 1) vì match chính xác với "continuous feedback" trong case study, bạn đồng ý chứ?
- Q3 (Functional Requirements): BẤT ĐỒNG - Các bản gom/tách FR khác nhau. Đã chốt chọn 5 FR của Run 1 (có bao gồm quy trình warehouse) để minh họa quy trình đa dạng, bạn có muốn thay bằng chức năng "issue receipt" không?
- Q4 (User Stories): ĐA SỐ - Các bản thiểu số (Run 2, 3) có US khác biệt do đi theo bộ FR riêng. Đã gạt bỏ bản thiểu số và đồng bộ 5 US theo 5 FR của Run 1.
- Q6 (Story Map Activities): BẤT ĐỒNG - Các bản phân rã task rất lệch nhau (Run 1 có mảng Warehouse, Run 2,3 bỏ qua). Đã chọn thiết kế của Run 3 (tập trung thuần túy vào Checkout -> Payment -> Inventory) vì chia Release MVP rất xuất sắc, bạn check lại xem đã đủ scope yêu cầu chưa nhé.
