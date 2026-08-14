# GIAI ĐOẠN 1 — PHÂN LOẠI
| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Q1 | Q1-Software_Development_Model.md | `XP framework`, `manager suggests applying...` | Cao |
| Q2 | Q2-Testing.md | `type and level/stage of testing`, `smallest unit level up to fully integrated` | Cao |
| Q3 | Q3-Identify_Requirements.md | `identify and list: 5 functional requirements, 3 performance...` | Cao |
| Q4 | Q4-User_Stories.md | `Write 5 user stories that are derived from your answers in Question 3` | Cao |
| Q5 | Q5-Design_Patterns.md | `apply some design patterns`, `list and describe in detail two design patterns` | Cao |
| Q6 | Q6-Story_Map.md | `Build a story map for the "Manage Patient Appointments" activities` | Cao |

# GIAI ĐOẠN 2 — MOI DỮ KIỆN
- **Q1:** Mô hình: XP framework. Đặc điểm dự án: highly skilled and experienced members (3-4 experienced developers), tight timeline (first release in 3 months), changing requirements (green-field project whose requirements keep evolving), clinical representatives on team. Đồng ý: Agree.
- **Q2:** Yêu cầu: tested from the smallest unit level up to the fully integrated system level. Unit level focus on program structure, higher levels based on functional requirements.
- **Q3:** Cần 5 Functional Requirements, 3 Performance Requirements, 2 Usability Requirements.
- **Q4:** 5 User stories dựa trên các FRs từ Q3.
- **Q5:** Hệ thống: Clinic Management System (CMS). Tính năng áp dụng: Alerts khi có critical values (Observer), Database Connection Pool xử lý peak transactions (Singleton).
- **Q6:** Tiêu điểm: "Manage Patient Appointments". Chức năng: book online/front desk, real-time availability, SMS/email reminders, live wait-time estimates.

# GIAI ĐOẠN 3 — BÀI LÀM
(Xem Bản Nộp)

# GIAI ĐOẠN 4 — TỰ CHẤM
| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Đủ 4 principles XP, match với đề có trích dẫn | Đạt | Không |
| Q2: Nêu RÕ RÀNG type là white-box hay black-box ở phần (a), đủ 4 levels và Who/Why ở (b) | Đạt | Không |
| Q3: Đúng số lượng 5 FR, 3 Perf, 2 Usab | Đạt | Không |
| Q4: Đủ 5 US, KHÔNG viết "As a system", đóng vai con người | Đạt | Không |
| Q5: Đủ 2 Design Patterns, có ứng dụng bám chặt Case Study | Đạt | Không |
| Q6: Đúng định dạng text thuần A và B, chuẩn cấu trúc đánh số | Đạt | Không |

---

## BẢN NỘP

### Question 1

I agree with the manager's suggestion to apply the XP (Extreme Programming) framework to this project.

Here are the main principles, practices, and characteristics of the XP framework, and how they match the project characteristics:

1. Frequent Releases and Short Development Cycles: 
- Explanation: XP emphasizes delivering working software frequently in short iterations to adapt to changes quickly.
- Match with project: This matches the project requirement of targeting the "first release in 3 months and full completion within 9 months."

2. Embracing Change: 
- Explanation: XP is designed to accommodate and embrace changing requirements even late in the development process.
- Match with project: This fits the project perfectly since it is a "green-field project whose requirements keep evolving."

3. Pair Programming and Skilled Team: 
- Explanation: XP relies on collaborative coding, collective code ownership, and high technical expertise among developers.
- Match with project: This aligns well since the development team consists of "highly skilled and experienced members" and is led by "3-4 experienced developers."

4. Continuous Customer Involvement: 
- Explanation: XP requires an on-site customer representative to provide continuous feedback and clarify requirements.
- Match with project: This is suitable because "clinical representatives" are part of the IT department's team heading the build.

Conclusion: Given the project's evolving requirements, tight timeline, skilled team, and direct clinical representative involvement, the XP framework is highly appropriate.

### Question 2

a. Types and levels/stages of testing required by the manager:

TYPES required:
- White-box testing at the unit level, because testing must "focus on program structure".
- Black-box testing at the higher levels, because testing must be "based on functional requirements".

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
- Who: End-users, Clients, or Business Analysts (e.g., Clinical representatives, Doctors, Nurses). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

### Question 3

Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. The system must allow a receptionist or the patient themselves to create a digital profile that stores demographics, health insurance, allergies, and complete medical history.
2. The system must allow nurses to record vital signs (BP, temperature, HR, SpO2) during consultations.
3. The system must allow doctors to enter ICD-10 diagnoses and treatment plans through structured templates.
4. The system must auto-link lab and imaging results to the patient record and trigger immediate alerts for critical values.
5. The system must allow doctors to issue e-prescriptions with automatic drug-drug interaction and allergy checks.

**Performance Requirements (3):**
1. The system must cope with peak transaction volumes without performance degradation, especially during morning rush hours.
2. Under normal operating load, the system shall respond to user interactions (page loading, form submission, search) within 2 seconds.
3. The system shall scale horizontally to support a growing number of patients, clinics, and staff users without any service interruption.

**Usability Requirements (2):**
1. The CMS has to be intuitive and simple to use, even for clinical staff with limited technical experience, featuring a clean and consistent interface with clearly labeled navigation.
2. Color coding must be applied meaningfully in the interface — green to confirm actions and red for errors or critical alerts.

### Question 4

Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a Receptionist, I want to create a digital profile for patients storing their demographics and medical history, so that their records are fully centralized and we can eliminate paper-based workflows.
2. **User Story 2:** As a Nurse, I want to record patient vital signs (BP, temperature, HR, SpO2) into the system, so that doctors have accurate and time-stamped clinical data during the consultation.
3. **User Story 3:** As a Doctor, I want to enter ICD-10 diagnoses and treatment plans using structured templates, so that the clinical workflow is modernized and standardized.
4. **User Story 4:** As a Doctor, I want the system to automatically link lab results to the patient record and alert me of critical values, so that I can immediately respond to severe health risks.
5. **User Story 5:** As a Doctor, I want to issue e-prescriptions that automatically perform drug-drug interaction and allergy checks, so that I can prevent medication errors and ensure patient safety.

### Question 5

Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be applied to the real-time alert system. For example, when lab and imaging results are received and contain "critical values" (the Subject changes state), it immediately notifies all subscribed Observers, such as the responsible Doctor's dashboard, so they can react quickly without tight coupling between the lab module and the doctor's interface.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be used for managing the Database Connection Pool. Since the system must "cope with peak transaction volumes without performance degradation, especially during morning rush hours," a Singleton Connection Pool ensures that the application reuses a single, strictly managed set of database connections, preventing resource exhaustion and maintaining system stability.

### Question 6

A. Activities and User tasks

1. Book Appointments
   - 1.1 View Availability
   - 1.2 Schedule Appointment
2. Manage Queues
   - 2.1 Track Wait Times
   - 2.2 Monitor Patient Queue
3. Handle Notifications
   - 3.1 Send Reminders
   - 3.2 Send Alerts

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a patient, I want to view real-time doctor availability so that I can choose a suitable time slot.
- 1.2.1 As a patient, I want to book an appointment online so that I can secure my consultation in advance.
- 2.2.1 As a receptionist, I want to view the patient queue so that I know who has checked in.
- 3.1.1 As a clinic administrator, I want the system to send automated email reminders to patients so that no-show rates are reduced.

Release 2----------------------------------------------------------------------
- 1.2.2 As a receptionist, I want to book an appointment at the front desk for walk-in patients so that they are added to the system.
- 2.1.1 As a patient, I want to see live wait-time estimates on the day of my visit so that I can manage my schedule better.
- 2.2.2 As a clinic administrator, I want to use dynamic queue management so that I can optimize patient flow during morning rush hours.
- 3.1.2 As a clinic administrator, I want the system to send automated SMS reminders to patients so that they get immediate notifications on their phones.
