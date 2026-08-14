**GIAI ĐOẠN 1 — PHÂN LOẠI**

| Câu trong đề | Khớp khuôn nào | Căn cứ (dấu hiệu nào) | Độ chắc chắn |
|---|---|---|---|
| Câu 1 | Q1-Software_Development_Model | "manager suggests applying the XP framework... Do you agree or disagree?" | Cao |
| Câu 2 | Q2-Testing | "What type and level/stage of testing... Who performs testing" | Cao |
| Câu 3 | Q3-Identify_Requirements | "identify and list: 5 functional requirements, 3 performance requirements, and 2 usability requirements" | Cao |
| Câu 4 | Q4-User_Stories | "Write 5 user stories that are derived from your answers in Question 3" | Cao |
| Câu 5 | Q5-Design_Patterns | "apply some design patterns... list and describe in detail two design patterns" | Cao |
| Câu 6 | Q6-Story_Map | "Build a story map for the 'Manage Patient Appointments' activities" | Cao |

**GIAI ĐOẠN 2 — MOI DỮ KIỆN**

**Q1 - Software Development Model:**
- `{{mo_hinh_duoc_de_xuat}}`: XP framework
- `{{dac_diem_du_an}}`: Green-field project whose requirements keep evolving; highly skilled team of 3-4 experienced developers and clinical representatives; tight schedule (first release in 3 months, full completion within 9 months).
- `{{dong_y_hay_khong}}`: Agree

**Q2 - Testing:**
- `{{yeu_cau_test}}`: from the smallest unit level up to the fully integrated system level. At the unit level, testing must focus on program structure; at higher levels, testing must be based on functional requirements.

**Q3 - Identify Requirements:**
- `{{so_luong_FR}}`: 5
- `{{loai_NFR_1}}`: Performance, `{{so_luong_NFR_1}}`: 3
- `{{loai_NFR_2}}`: Usability, `{{so_luong_NFR_2}}`: 2

**Q4 - User Stories:**
- `{{so_luong_US}}`: 5 user stories
- `{{danh_sach_FR_tu_Q3}}`: 5 Functional Requirements từ Câu 3.

**Q5 - Design Patterns:**
- `{{he_thong}}`: Clinic Management System (CMS)
- `{{tinh_nang_ap_dung}}`: 
  - Pattern 1 (Observer): Critical values trigger immediate alerts / real-time low-stock alerts.
  - Pattern 2 (Singleton): Database connections for peak transaction volumes or Single Sign-On Identity Platform.

**Q6 - Story Map:**
- `{{tieu_diem_chinh}}`: Manage Patient Appointments
- `{{cac_chuc_nang}}`: Online or front desk booking, real-time doctor availability, automated SMS/email reminders, dynamic queue management with live wait-time estimates.

**GIAI ĐOẠN 3 — BÀI LÀM**

1.
I agree with the manager's suggestion to apply the XP (Extreme Programming) framework to this project.

Here are the main principles, practices, and characteristics of the XP framework, and how they match the project characteristics:

1. Frequent Releases and Short Development Cycles:
- Explanation: XP emphasizes delivering working software frequently in short iterations.
- Match with project: This matches the project requirement of targeting the first release in just 3 months and full completion within 9 months.

2. Embracing Change:
- Explanation: XP is designed to accommodate changing requirements even late in development.
- Match with project: This fits the project perfectly since it is a green-field project whose requirements keep evolving.

3. Pair Programming and Skilled Team:
- Explanation: XP relies on collaborative coding and high technical expertise.
- Match with project: This aligns well since the IT department heads the build with a team consisting of highly skilled and experienced members (3-4 experienced developers).

4. Continuous Customer Involvement:
- Explanation: XP requires a customer representative on-site to provide continuous feedback.
- Match with project: This is suitable because clinical representatives are already part of the development team to ensure the system modernizes clinic operations correctly.

Conclusion: Given the project's tight timeline, highly skilled team, and changing requirements, the XP framework is highly appropriate.

2.
a. Types and levels/stages of testing required by the manager:

TYPES required:
- White-box testing at the unit level, because testing must focus on the program structure.
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
- Who: End-users, Clients, or Business Analysts (e.g., Doctors, Nurses, Receptionists, and Administrators).
- Why: They are the domain experts who ensure the Clinic Management System meets real-world medical workflows before release.

3.
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. Receptionists (or patients) must be able to create a digital profile that stores demographics, health insurance, allergies, and the complete medical history.
2. Nurses must be able to record vital signs (BP, temperature, HR, SpO2) during the consultation.
3. Doctors must be able to enter ICD-10 diagnoses and treatment plans through structured templates.
4. Doctors must be able to raise lab and imaging orders (X-ray, ultrasound, MRI) electronically from the EMR.
5. Administrators must be able to manage user roles (RBAC), schedules, fee structures, and view KPI dashboards.

**Performance Requirements (3):**
1. The system must cope with peak transaction volumes without performance degradation, especially during morning rush hours.
2. Under normal operating load, the system shall respond to user interactions (page loading, form submission, search) within 2 seconds.
3. The system shall scale horizontally to support a growing number of patients, clinics, and staff users without any service interruption.

**Usability Requirements (2):**
1. The CMS has to be intuitive and simple to use, even for clinical staff with limited technical experience.
2. Color coding must be applied meaningfully - green to confirm actions, red for errors or critical alerts — so staff can act quickly without confusion.

4.
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a Receptionist, I want to create a digital profile for a patient, so that their demographics and medical history are stored in a single centralized platform.
2. **User Story 2:** As a Nurse, I want to record vital signs during the consultation, so that the clinical team has up-to-date and time-stamped health data.
3. **User Story 3:** As a Doctor, I want to enter ICD-10 diagnoses and treatment plans using structured templates, so that the consultation records are consistent and accurate.
4. **User Story 4:** As a Doctor, I want to raise lab and imaging orders electronically, so that the results can be auto-linked to the patient record for quick review.
5. **User Story 5:** As an Administrator, I want to manage user roles and schedules, so that staff users have appropriate access (RBAC) and clinic operations run smoothly.

5.
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be applied to send critical alerts or reminders. For example, when critical lab values are entered (Subject changes state), the system immediately notifies the relevant Doctors and Nurses (Observers) so they can react accordingly without tight coupling between the lab module and the notification interface.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CMS, this pattern can be used for managing the central database connection pool. Since the system must cope with peak transaction volumes and respond within 2 seconds, a Singleton Connection Pool ensures that the application reuses a single, managed set of connections, preventing resource conflicts and performance degradation during morning rush hours.

6.
A. Activities and User tasks

1. Book Appointments
   - 1.1 View real-time doctor availability
   - 1.2 Schedule appointments online or at the front desk
2. Manage Queues
   - 2.1 View live wait-time estimates
   - 2.2 Manage patient check-ins
3. Handle Notifications
   - 3.1 Send automated SMS reminders
   - 3.2 Send automated email reminders

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a patient, I want to view real-time doctor availability so that I can choose a suitable consultation time.
- 1.2.1 As a receptionist, I want to schedule appointments at the front desk so that walk-in patients can be served.
- 2.2.1 As a receptionist, I want to manage patient check-ins so that the doctors know who has arrived.
- 3.1.1 As a clinic manager, I want the system to send automated SMS reminders so that patients do not forget their appointments.

Release 2----------------------------------------------------------------------
- 1.2.2 As a patient, I want to schedule appointments online so that I do not have to call the clinic.
- 2.1.1 As a patient, I want to view live wait-time estimates on the day of the visit so that I can minimize my physical waiting time at the clinic.
- 3.2.1 As a clinic manager, I want the system to send automated email reminders so that patients receive detailed appointment information.

**GIAI ĐOẠN 4 — TỰ CHẤM**

| Tiêu chí | Đạt/Chưa | Sửa gì |
|---|---|---|
| Q1: Có Agree/Disagree rõ ràng | Đạt | Không cần sửa |
| Q1: Liệt kê đủ principle và match với Case study | Đạt | Không cần sửa |
| Q2: Nêu rõ type (white-box/black-box) ở phần (a) | Đạt | Không cần sửa |
| Q2: 4 cấp độ test, Who và Why | Đạt | Không cần sửa |
| Q3: Đúng số lượng 5 FRs, 3 PRs, 2 URs | Đạt | Không cần sửa |
| Q4: 5 User stories từ Q3, dùng "As a <người>", "I want to", "so that" | Đạt | Không cần sửa |
| Q5: 2 design patterns (Description, Application) | Đạt | Không cần sửa |
| Q6: Đúng chuẩn format A và B | Đạt | Không cần sửa |

## BẢN NỘP

1.
I agree with the manager's suggestion to apply the XP (Extreme Programming) framework to this project.

Here are the main principles, practices, and characteristics of the XP framework, and how they match the project characteristics:

1. Frequent Releases and Short Development Cycles:
- Explanation: XP emphasizes delivering working software frequently in short iterations.
- Match with project: This matches the project requirement of targeting the first release in just 3 months and full completion within 9 months.

2. Embracing Change:
- Explanation: XP is designed to accommodate changing requirements even late in development.
- Match with project: This fits the project perfectly since it is a green-field project whose requirements keep evolving.

3. Pair Programming and Skilled Team:
- Explanation: XP relies on collaborative coding and high technical expertise.
- Match with project: This aligns well since the IT department heads the build with a team consisting of highly skilled and experienced members (3-4 experienced developers).

4. Continuous Customer Involvement:
- Explanation: XP requires a customer representative on-site to provide continuous feedback.
- Match with project: This is suitable because clinical representatives are already part of the development team to ensure the system modernizes clinic operations correctly.

Conclusion: Given the project's tight timeline, highly skilled team, and changing requirements, the XP framework is highly appropriate.

2.
a. Types and levels/stages of testing required by the manager:

TYPES required:
- White-box testing at the unit level, because testing must focus on the program structure.
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
- Who: End-users, Clients, or Business Analysts (e.g., Doctors, Nurses, Receptionists, and Administrators).
- Why: They are the domain experts who ensure the Clinic Management System meets real-world medical workflows before release.

3.
Based on the project description, here are the identified requirements:

**Functional Requirements (5):**
1. Receptionists (or patients) must be able to create a digital profile that stores demographics, health insurance, allergies, and the complete medical history.
2. Nurses must be able to record vital signs (BP, temperature, HR, SpO2) during the consultation.
3. Doctors must be able to enter ICD-10 diagnoses and treatment plans through structured templates.
4. Doctors must be able to raise lab and imaging orders (X-ray, ultrasound, MRI) electronically from the EMR.
5. Administrators must be able to manage user roles (RBAC), schedules, fee structures, and view KPI dashboards.

**Performance Requirements (3):**
1. The system must cope with peak transaction volumes without performance degradation, especially during morning rush hours.
2. Under normal operating load, the system shall respond to user interactions (page loading, form submission, search) within 2 seconds.
3. The system shall scale horizontally to support a growing number of patients, clinics, and staff users without any service interruption.

**Usability Requirements (2):**
1. The CMS has to be intuitive and simple to use, even for clinical staff with limited technical experience.
2. Color coding must be applied meaningfully - green to confirm actions, red for errors or critical alerts — so staff can act quickly without confusion.

4.
Here are 5 user stories derived from the functional requirements in Question 3:

1. **User Story 1:** As a Receptionist, I want to create a digital profile for a patient, so that their demographics and medical history are stored in a single centralized platform.
2. **User Story 2:** As a Nurse, I want to record vital signs during the consultation, so that the clinical team has up-to-date and time-stamped health data.
3. **User Story 3:** As a Doctor, I want to enter ICD-10 diagnoses and treatment plans using structured templates, so that the consultation records are consistent and accurate.
4. **User Story 4:** As a Doctor, I want to raise lab and imaging orders electronically, so that the results can be auto-linked to the patient record for quick review.
5. **User Story 5:** As an Administrator, I want to manage user roles and schedules, so that staff users have appropriate access (RBAC) and clinic operations run smoothly.

5.
Here are two design patterns that can be applied to the software system, along with their detailed descriptions and applications:

1. **Design Pattern 1: Observer Pattern**
- **Description:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Application to the system:** In this Clinic Management System (CMS), this pattern can be applied to send critical alerts or reminders. For example, when critical lab values are entered (Subject changes state), the system immediately notifies the relevant Doctors and Nurses (Observers) so they can react accordingly without tight coupling between the lab module and the notification interface.

2. **Design Pattern 2: Singleton Pattern**
- **Description:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
- **Application to the system:** In this CMS, this pattern can be used for managing the central database connection pool. Since the system must cope with peak transaction volumes and respond within 2 seconds, a Singleton Connection Pool ensures that the application reuses a single, managed set of connections, preventing resource conflicts and performance degradation during morning rush hours.

6.
A. Activities and User tasks

1. Book Appointments
   - 1.1 View real-time doctor availability
   - 1.2 Schedule appointments online or at the front desk
2. Manage Queues
   - 2.1 View live wait-time estimates
   - 2.2 Manage patient check-ins
3. Handle Notifications
   - 3.1 Send automated SMS reminders
   - 3.2 Send automated email reminders

B. Releases

Release 1----------------------------------------------------------------------
- 1.1.1 As a patient, I want to view real-time doctor availability so that I can choose a suitable consultation time.
- 1.2.1 As a receptionist, I want to schedule appointments at the front desk so that walk-in patients can be served.
- 2.2.1 As a receptionist, I want to manage patient check-ins so that the doctors know who has arrived.
- 3.1.1 As a clinic manager, I want the system to send automated SMS reminders so that patients do not forget their appointments.

Release 2----------------------------------------------------------------------
- 1.2.2 As a patient, I want to schedule appointments online so that I do not have to call the clinic.
- 2.1.1 As a patient, I want to view live wait-time estimates on the day of the visit so that I can minimize my physical waiting time at the clinic.
- 3.2.1 As a clinic manager, I want the system to send automated email reminders so that patients receive detailed appointment information.
