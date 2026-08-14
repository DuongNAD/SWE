## GIAI ĐOẠN 1 — PHÂN LOẠI

| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Câu 1 | Q1-Software_Development_Model | "XP framework", "Do you agree or disagree? List and explain all main principles... then match each one to the project characteristics" | Cao |
| Câu 2 | Q2-Testing | "tested from the smallest unit level up to the fully integrated system level", "What type and level/stage of testing" | Cao |
| Câu 3 | Q3-Identify_Requirements | "identify and list: 5 functional requirements, 3 performance requirements, and 2 usability requirements" | Cao |
| Câu 4 | Q4-User_Stories | "Write 5 user stories based on your answers in Question 3" | Cao |
| Câu 5 | Q5-Design_Patterns | "apply design patterns", "List and describe in detail two design patterns" | Cao |
| Câu 6 | Q6-Story_Map | "Build a story map for the 'Manage Patient Appointments' activities" | Cao |

## GIAI ĐOẠN 2 — MOI DỮ KIỆN

**Câu 1:**
- `{{mo_hinh_duoc_de_xuat}}`: XP framework
- `{{dac_diem_du_an}}`: Green-field project with evolving requirements, 3-4 experienced developers, clinical representatives, target first release in 3 months and full completion within 9 months.
- `{{dong_y_hay_khong}}`: Agree

**Câu 2:**
- `{{yeu_cau_test}}`: "from the smallest unit level up to the fully integrated system level", "At the unit level, testing must focus on program structure", "at higher levels, testing must be based on functional requirements"

**Câu 3:**
- `{{so_luong_FR}}`: 5
- `{{loai_NFR_1}}`: performance
- `{{so_luong_NFR_1}}`: 3
- `{{loai_NFR_2}}`: usability
- `{{so_luong_NFR_2}}`: 2

**Câu 4:**
- `{{so_luong_US}}`: 5
- `{{danh_sach_FR_tu_Q3}}`: 5 FRs từ Câu 3.

**Câu 5:**
- `{{he_thong}}`: Clinic Management System (CMS)
- `{{tinh_nang_ap_dung}}`: real-time alerts/critical values (Observer), Database connection / Configuration (Singleton).

**Câu 6:**
- `{{tieu_diem_chinh}}`: "Manage Patient Appointments"
- `{{cac_chuc_nang}}`: booked online or at the front desk, real-time doctor availability, automated SMS/email reminders, dynamic queue management with live wait-time estimates.

## GIAI ĐOẠN 3 — BÀI LÀM

*(Được bao gồm trong phần BẢN NỘP)*

## GIAI ĐOẠN 4 — TỰ CHẤM

| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| C1: Rõ Agree/Disagree | Đạt | Không |
| C1: Đủ 4 nguyên tắc XP & Map với Case Study | Đạt | Không |
| C2: Nêu đủ 4 cấp độ kiểm thử & Who/Why | Đạt | Không |
| C2: Nêu rõ type là white-box hay black-box ở (a) | Đạt | Không |
| C3: Đúng 5 FR, 3 Performance, 2 Usability | Đạt | Không |
| C4: Đúng 5 US, cấu trúc "As a...", map với Q3 | Đạt | Không |
| C4: KHÔNG viết "As a system" ở các user stories | Đạt | Không |
| C5: Nêu 2 design patterns, description & application | Đạt | Không |
| C6: Format A. Activities và B. Releases chuẩn EOS | Đạt | Không |

## BẢN NỘP

### Question 1
I agree with the manager's suggestion to apply the XP (Extreme Programming) framework to this project.

Here are the main principles, practices, and characteristics of the XP framework, and how they match the project characteristics:

1. Frequent Releases and Short Development Cycles: 
- Explanation: XP emphasizes delivering working software frequently in short iterations.
- Match with project: This matches the project requirement of targeting the first release in 3 months and full completion within 9 months.

2. Embracing Change: 
- Explanation: XP is designed to accommodate changing requirements even late in development.
- Match with project: This fits the project perfectly since it is a green-field project with evolving requirements.

3. Pair Programming and Skilled Team: 
- Explanation: XP relies on collaborative coding and high technical expertise.
- Match with project: This aligns well since the IT department leads the development with 3-4 experienced developers.

4. Continuous Customer Involvement: 
- Explanation: XP requires a customer representative on-site to provide continuous feedback.
- Match with project: This is suitable because clinical representatives are part of the development team to support the implementation.

Conclusion: Given the project's tight timeline, experienced team, evolving requirements, and direct involvement of clinical representatives, the XP framework is highly appropriate.

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
- Who: End-users, Clients, or Business Analysts (e.g., Clinical representatives). 
- Why: They are the domain experts who ensure the system meets real-world business needs before release.

### Question 3
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. Receptionists or patients must be able to create a digital profile storing demographics, health insurance, allergies, and full medical history.
2. Receptionists or patients must be able to book appointments online or at the front desk with real-time doctor availability.
3. Nurses must be able to record vital signs (BP, temperature, HR, SpO2) during the consultation.
4. Doctors must be able to enter ICD-10 diagnoses and treatment plans via structured templates.
5. Administrators must be able to manage user roles (RBAC), schedules, and fee structures.

**Performance Requirements (3):**
1. The system must cope with peak transaction volumes without performance degradation, especially during morning rush hours.
2. Under normal operating load, the system shall respond to user interactions (page loading, form submission, search) within 2 seconds.
3. The system shall scale horizontally to support a growing number of patients, clinics, and staff users without service interruption.

**Usability Requirements (2):**
1. The CMS must be intuitive and easy to use, even for clinical staff with limited technical experience.
2. Color coding must be used meaningfully - green to confirm actions, red for errors or critical alerts - so staff can act quickly without ambiguity.

### Question 4
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a Receptionist, I want to create a digital profile storing a patient's demographics, health insurance, allergies, and medical history so that their records are centralized and easily accessible.
2. **User Story 2:** As a Patient, I want to book appointments online with real-time doctor availability so that I can easily schedule my visits without calling the clinic.
3. **User Story 3:** As a Nurse, I want to record vital signs (BP, temperature, HR, SpO2) into the system during the consultation so that doctors have accurate, real-time health data for diagnosis.
4. **User Story 4:** As a Doctor, I want to enter ICD-10 diagnoses and treatment plans via structured templates so that medical records are standardized and accurately documented.
5. **User Story 5:** As an Administrator, I want to manage user roles, schedules, and fee structures so that the clinic operates smoothly and staff have the correct access permissions.

### Question 5
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be applied to the real-time alert system. For example, when "critical values trigger immediate alerts" (as stated in the case study) for lab results, the Lab Result Record (Subject) changes its state. It then automatically notifies all subscribed Observers, such as the Doctor's Dashboard, ensuring rapid response without tightly coupling the components.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be used for managing the Database Connection Pool. Since the system must "cope with peak transaction volumes without performance degradation, especially during morning rush hours," a Singleton Connection Pool ensures that the application reuses a single, managed set of database connections, preventing memory exhaustion and ensuring consistent data access across all clinical modules.

### Question 6
A. Activities and User tasks

1. Book Appointments
   - 1.1 View Doctor Availability
   - 1.2 Schedule Appointment
2. Manage Queues
   - 2.1 Track Wait Times
   - 2.2 Route Patients
3. Handle Notifications
   - 3.1 Send Reminders
   - 3.2 Send Alerts

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a patient, I want to view real-time doctor availability online so I can find a suitable time slot.
- 1.2.1 As a patient, I want to book an appointment online to secure a consultation.
- 2.1.1 As a receptionist, I want to track patient check-ins at the front desk so I know who is waiting.
- 3.1.1 As a clinic manager, I want the system to send automated email reminders to patients so they don't miss their appointments.

Release 2----------------------------------------------------------------------
- 1.2.2 As a receptionist, I want to book an appointment at the front desk for walk-in patients so that they are added to the schedule.
- 2.1.2 As a patient, I want to see live wait-time estimates on the day of the visit so I can manage my time better.
- 2.2.1 As a clinic manager, I want dynamic queue management to optimize patient flow during morning rush hours.
- 3.1.2 As a clinic manager, I want the system to send automated SMS reminders for higher open rates compared to emails.
- 3.2.1 As a doctor, I want the system to send immediate alerts for critical lab values so I can act quickly.
