{
  "id": "b5",
  "so_do": [
    {
      "ts_day_du_nhat": "43:43",
      "ts_xuat_hien": [
        "16:19",
        "17:24",
        "20:04",
        "20:43",
        "22:01",
        "22:09",
        "23:47",
        "24:28",
        "25:17",
        "25:37",
        "25:50",
        "25:54",
        "25:58",
        "26:33",
        "26:37",
        "27:32",
        "28:02",
        "28:39",
        "28:44",
        "28:49",
        "29:11",
        "29:15",
        "29:20",
        "29:57",
        "30:01",
        "30:10",
        "30:48",
        "31:01",
        "31:06",
        "31:16",
        "40:45",
        "43:43"
      ],
      "loai": "class_diagram",
      "ten_bai_toan": "Hệ thống quản lý đăng ký môn học (University Course Registration System)",
      "phan_tu": [
        {
          "ten": "User",
          "kieu": "class",
          "thuoc_tinh": [
            "- userId : String",
            "- fullName : String",
            "- email : String",
            "- passwordHash : String",
            "- role : String"
          ],
          "phuong_thuc": [
            "+ login(email, pwd) : Boolean",
            "+ logout() : void",
            "+ updateProfile(data) : void"
          ]
        },
        {
          "ten": "SystemAdmin",
          "kieu": "class",
          "thuoc_tinh": [
            "- adminId : String",
            "- accessLevel : int",
            "- lastBackup : DateTime"
          ],
          "phuong_thuc": [
            "+ manageUserAccount() : void",
            "+ configureSystem() : void",
            "+ runBackup() : void"
          ]
        },
        {
          "ten": "Student",
          "kieu": "class",
          "thuoc_tinh": [
            "- studentId : String",
            "- program : String",
            "- yearLevel : int",
            "- Attribute1",
            "- gpa : float",
            "- creditEarned : int"
          ],
          "phuong_thuc": [
            "+ browseCatalog() : List",
            "+ submitRegistration() : Registration",
            "+ viewTranscript() : List"
          ]
        },
        {
          "ten": "Lecturer",
          "kieu": "class",
          "thuoc_tinh": [
            "- staffId : String",
            "- department : String",
            "- specialisation : String"
          ],
          "phuong_thuc": [
            "+ viewRoster() : List",
            "+ recordGrade() : void",
            "+ releaseGrades() : void"
          ]
        },
        {
          "ten": "AcademicStaff",
          "kieu": "class",
          "thuoc_tinh": [
            "- staffId : String",
            "- department : String",
            "- adminLevel : int"
          ],
          "phuong_thuc": [
            "+ openRegistrationWindow() : void",
            "+ approveException() : void",
            "+ generateReport() : Report"
          ]
        },
        {
          "ten": "Course",
          "kieu": "class",
          "thuoc_tinh": [
            "- courseCode : String",
            "- title : String",
            "- credits : int",
            "- description : String",
            "- prerequisites : List"
          ],
          "phuong_thuc": [
            "+ checkPrerequisites() : Boolean",
            "+ getOfferings() : List"
          ]
        },
        {
          "ten": "CourseOffering",
          "kieu": "class",
          "thuoc_tinh": [
            "- offeringId : String",
            "- schedule : String",
            "- room : String",
            "- quota : int"
          ],
          "phuong_thuc": [
            "+ isAvailable() : Boolean",
            "+ getEnrolledStudents() : List",
            "+ addToWaitlist() : void"
          ]
        },
        {
          "ten": "Registration",
          "kieu": "class",
          "thuoc_tinh": [
            "- registrationId : String",
            "- submittedAt : DateTime",
            "- status : String",
            "- approvedBy : String"
          ],
          "phuong_thuc": [
            "+ approve() : void",
            "+ reject() : void",
            "+ cancel() : void"
          ]
        },
        {
          "ten": "Waitlist",
          "kieu": "class",
          "thuoc_tinh": [
            "- waitlistId : String",
            "- position : int",
            "- joinedAt : DateTime"
          ],
          "phuong_thuc": [
            "+ promoteNext() : Student",
            "+ removeEntry() : void",
            "+ getPosition() : int"
          ]
        },
        {
          "ten": "Grade",
          "kieu": "class",
          "thuoc_tinh": [
            "- gradeId : String",
            "- midtermScore : float",
            "- finalScore : float",
            "- letterGrade : String",
            "- isReleased : Boolean"
          ],
          "phuong_thuc": [
            "+ calculate() : String",
            "+ release() : void",
            "+ getGPA() : float"
          ]
        },
        {
          "ten": "Semester",
          "kieu": "class",
          "thuoc_tinh": [
            "- semesterId : String",
            "- name : String",
            "- startDate : Date",
            "- endDate : Date",
            "- regWindowOpen : Boolean"
          ],
          "phuong_thuc": [
            "+ openRegistration() : void",
            "+ closeRegistration() : void",
            "+ isActive() : Boolean"
          ]
        },
        {
          "ten": "Report",
          "kieu": "class",
          "thuoc_tinh": [
            "- reportId : String",
            "- type : String",
            "- generatedAt : DateTime",
            "- generatedBy : String",
            "- content : String"
          ],
          "phuong_thuc": [
            "+ generate() : void",
            "+ export() : File",
            "+ schedule() : void"
          ]
        }
      ],
      "quan_he": [
        {
          "tu": "SystemAdmin",
          "den": "User",
          "loai": "generalization",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "",
          "huong": "SystemAdmin -> User"
        },
        {
          "tu": "Student",
          "den": "User",
          "loai": "generalization",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "",
          "huong": "Student -> User"
        },
        {
          "tu": "Lecturer",
          "den": "User",
          "loai": "generalization",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "",
          "huong": "Lecturer -> User"
        },
        {
          "tu": "Student",
          "den": "Registration",
          "loai": "directed association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "submit",
          "huong": "Student -> Registration"
        },
        {
          "tu": "Course",
          "den": "CourseOffering",
          "loai": "association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "has",
          "huong": "Course -- CourseOffering"
        },
        {
          "tu": "CourseOffering",
          "den": "Registration",
          "loai": "association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "for",
          "huong": "CourseOffering -- Registration"
        },
        {
          "tu": "Lecturer",
          "den": "Grade",
          "loai": "directed association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "manage",
          "huong": "Lecturer -> Grade"
        },
        {
          "tu": "Semester",
          "den": "CourseOffering",
          "loai": "association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "",
          "huong": "Semester -- CourseOffering"
        },
        {
          "tu": "CourseOffering",
          "den": "Waitlist",
          "loai": "association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "",
          "huong": "CourseOffering -- Waitlist"
        },
        {
          "tu": "Grade",
          "den": "Registration",
          "loai": "association",
          "multiplicity_tu": "",
          "multiplicity_den": "",
          "nhan": "",
          "huong": "Grade -- Registration"
        }
      ],
      "plantuml": "@startuml\nabstract class User {\n  - userId : String\n  - fullName : String\n  - email : String\n  - passwordHash : String\n  - role : String\n  + login(email, pwd) : Boolean\n  + logout() : void\n  + updateProfile(data) : void\n}\nclass SystemAdmin {\n  - adminId : String\n  - accessLevel : int\n  - lastBackup : DateTime\n  + manageUserAccount() : void\n  + configureSystem() : void\n  + runBackup() : void\n}\nclass Student {\n  - studentId : String\n  - program : String\n  - yearLevel : int\n  - Attribute1\n  - gpa : float\n  - creditEarned : int\n  + browseCatalog() : List\n  + submitRegistration() : Registration\n  + viewTranscript() : List\n}\nclass Lecturer {\n  - staffId : String\n  - department : String\n  - specialisation : String\n  + viewRoster() : List\n  + recordGrade() : void\n  + releaseGrades() : void\n}\nclass AcademicStaff {\n  - staffId : String\n  - department : String\n  - adminLevel : int\n  + openRegistrationWindow() : void\n  + approveException() : void\n  + generateReport() : Report\n}\nclass Course {\n  - courseCode : String\n  - title : String\n  - credits : int\n  - description : String\n  - prerequisites : List\n  + checkPrerequisites() : Boolean\n  + getOfferings() : List\n}\nclass CourseOffering {\n  - offeringId : String\n  - schedule : String\n  - room : String\n  - quota : int\n  + isAvailable() : Boolean\n  + getEnrolledStudents() : List\n  + addToWaitlist() : void\n}\nclass Registration {\n  - registrationId : String\n  - submittedAt : DateTime\n  - status : String\n  - approvedBy : String\n  + approve() : void\n  + reject() : void\n  + cancel() : void\n}\nclass Waitlist {\n  - waitlistId : String\n  - position : int\n  - joinedAt : DateTime\n  + promoteNext() : Student\n  + removeEntry() : void\n  + getPosition() : int\n}\nclass Grade {\n  - gradeId : String\n  - midtermScore : float\n  - finalScore : float\n  - letterGrade : String\n  - isReleased : Boolean\n  + calculate() : String\n  + release() : void\n  + getGPA() : float\n}\nclass Semester {\n  - semesterId : String\n  - name : String\n  - startDate : Date\n  - endDate : Date\n  - regWindowOpen : Boolean\n  + openRegistration() : void\n  + closeRegistration() : void\n  + isActive() : Boolean\n}\nclass Report {\n  - reportId : String\n  - type : String\n  - generatedAt : DateTime\n  - generatedBy : String\n  - content : String\n  + generate() : void\n  + export() : File\n  + schedule() : void\n}\nSystemAdmin -up-|> User\nStudent -up-|> User\nLecturer -up-|> User\nStudent --> Registration : +submit\nCourse -- CourseOffering : +has\nCourseOffering -- Registration : +for\nLecturer --> Grade : +manage\nSemester -- CourseOffering\nCourseOffering -- Waitlist\nRegistration -- Grade\n@enduml",
      "ghi_chu": "Hình cuối (43:43) không hiển thị rõ phần bên trái chứa class AcademicStaff và phần Abstract User bị cắt phía trên. Có một đường nối từ Report lên trên bên trái có thể nối với AcademicStaff hoặc SystemAdmin nhưng bị che khuất và không rõ. Multiplicity trên các đường nối không được vẽ nên bỏ trống. Quan hệ generalization của AcademicStaff với User không được vẽ nhưng có thể suy luận."
    }
  ],
  "bang": [
    {
      "ts": "26:48, 28:18, 30:30",
      "tieu_de": "Danh sách các lớp (Classes) từ Luyện tập Q5",
      "cot": [
        "STT",
        "Class Name",
        "Attributes",
        "Methods",
        "Description"
      ],
      "dong": [
        [
          "5",
          "SystemAdmin",
          "adminId:String\naccessLevel:int\nlastBackup:DateTime",
          "manageUserAccount():void\nconfigureSystem():void\nrunBackup():void",
          "Manage system and user accounts"
        ],
        [
          "6",
          "Course",
          "courseCode:String\ntitle:String\ncredits:int\ndescription:String\nprerequisites:List",
          "checkPrerequisites():Boolean\ngetOfferings():List",
          "Store course info and rules"
        ],
        [
          "7",
          "CourseOffering",
          "offeringId:String\nschedule:String\nroom:String\nquota:int\nenrolledCount:int\nstatus:String",
          "isAvailable():Boolean\ngetEnrolledStudents():List\naddToWaitlist():void",
          "Course in semester with limited seats"
        ],
        [
          "8",
          "Registration",
          "registrationId:String\nsubmittedAt:DateTime\nstatus:String\napprovedBy:String",
          "approve():void\nreject():void\ncancel():void",
          "Store registration request"
        ],
        [
          "9",
          "Waitlist",
          "waitlistId:String\nposition:int\njoinedAt:DateTime",
          "promoteNext():Student\nremoveEntry():void\ngetPosition():int",
          "Manage waiting list"
        ],
        [
          "10",
          "Grade",
          "gradeId:String\nmidtermScore:float\nfinalScore:float\nletterGrade:String\nisReleased:Boolean",
          "calculate():String\nrelease():void\ngetGPA():float",
          "Store and calculate scores"
        ],
        [
          "11",
          "Semester",
          "semesterId:String\nname:String\nstartDate:Date\nendDate:Date",
          "openRegistration():void\ncloseRegistration():void\nisActive():Boolean",
          "Control semester timeline"
        ]
      ],
      "ghi_chu": "Bảng bị thiếu các dòng 1, 2, 3, 4 trong ảnh chụp. Phần header không hiển thị nên tự suy luận tên cột dựa vào nội dung."
    }
  ],
  "anh_bo_qua": []
}