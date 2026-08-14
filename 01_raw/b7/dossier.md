# DOSSIER — b7

- file gốc: `YTSave_YouTube_Buoi-7-Luyen-tap-Q7-Cach-viet-test-case_Media_8QTtCmm6Fq0_002_720p.mp4`
- thời lượng: 41.0 phút
- nguồn: transcript tự động (Whisper) + OCR màn hình (Apple Vision), đều chạy offline

> **Độ tin cậy — đọc trước khi dùng:**
> `Nói:` là giọng giảng viên do máy nhận dạng, có thể sai thuật ngữ tiếng Anh.
> `Màn hình:` là chữ OCR từ khung hình, có thể sai vài ký tự nhưng bố cục đúng.
> Khi hai nguồn lệch nhau: **tin `Màn hình` cho tên class / thuộc tính / bảng / code**,
> **tin `Nói` cho lời giải thích và quy trình**. Timestamp là của video gốc.

---

## [00:00]
**Nói:** Ok, hello anh em nhé, trong video này mình sẽ hướng dẫn anh em làm câu số 7 anh em nhé. Câu số 7 này là câu cuối cùng, ok. Thì câu số 7 này thì mình đã hướng dẫn anh em từ câu 1 đến câu 6 rồi. Và câu số 7 này là câu cuối cùng mình sẽ hướng dẫn anh em. Thì mình nghĩ là câu số 7 này có một cái phần mà ăn điểm chắc chắn 100% ai cũng ăn được 0.5. Và này anh em chỉ cần copy paste thôi. Tuy nhiên thì phần này thì khả năng cao là sẽ không có trong đề thi đâu. Nếu có thì mình nghĩ là Nó sẽ có cái phần Viết dưới này thôi, viết tiết cây thôi
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
9sca100%  Normal text  Arial  | - 11] +  / Editing
6
I. CASE STUDY
Green University is a mid-sized institution with approximately 8,000 students and 400 academic
staff. Each semester, the university must manage course enrollment for all undergraduate and
postgraduate programmes. Currently, students submit paper-based registration forms to their
faculty office, and clerks manually enter the data into spreadsheets. This process is error-prone,
slow, and creates long queues during the registration window. The university's administration
has therefore decided to commission a web-based Course Registration System (CRS) to
automate and streamline the entire workflow.
The CRS is expected to serve four main groups of users. Students need to browse the
catalogue of available courses, check their eligibility based on completed prerequisites, submit
registration requests, and track the status of each request in real time. If a course is fully
booked, a student may join an electronic waitlist; should a registered student later drop the
course, the system automatically notifies and enrolls the first eligible student on the waitlist.
Lecturers need to review the roster of students enrolled in their courses, record midterm and
final grades, and release grades to students once the grading period closes. Academic Staff
(administrators) are responsible for defining the semester timetable, setting and publishing
course quotas, opening and closing the registration window, approving exceptional cases, and
generating enrolment and grade-distribution reports. Finally, a System Administrator manages
user accounts, configures system parameters, and oversees scheduled data backups.
From a technical standpoint, the university imposes several constraints. The system must
remain responsive-handling at least 1,000 simultaneous users during peak registration periods
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RBAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
V  ENG  10:37 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  Luyện tập Q7 - Google Dock x  +  La  ...
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  1 - 11  +  / Editing
generating enrolment and grade-distribution reports. Finally, a System Administrator manages
user accounts, configures system parameters, and oversees scheduled data backups.
From a technical standpoint, the university imposes several constraints. The system must
remain responsive-handling at least 1,000 simultaneous users during peak registration periods
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario - a student successfully registers for an available course
Boundary / edge-case scenario - a student registers for the last available seat
(quota = 1 remaining)
^  ENG  10:38 PM
US  4/23/2026
```

## [00:30]
**Nói:** Còn nếu mà đưa cái này vào thì Anh em sẽ ăn được luôn 0,5% Ok Thì đề lúc nào nó cũng sẽ cho anh em là Phần case study Phần này thì đằng trên mình nói quá nhiều rồi Những câu trước thì anh em đã hiểu quá rõ Vì cái case study của cái bài Của cái đề thi thử này rồi đúng không anh em Chung quy lại Thì cái đề này topic của nó đúng như cái topic của nó thì nó chính là về đăng ký của học ok thì ở đây
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc×  +  La
+ > G  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  # ®  • |  =
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q5 e  A S 100% -  Normal text  Arial  0 Editing
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write ITHREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario — a student successfully registers for an available course
Boundary / edge-case scenario - a student registers for the last available seat
(quota = 1 remaining)/
• Negative / error scenario — a student attempts to register without meeting the
course prerequisite
^ V O  ENG  10:38 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La  ...
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G  +
Share
File Edit View Insert Format Tools Extensions Help
Q5 e  8A100%  Normal text  Arial  | - 11 +  BIUAO  Editing
final grades, and release grades to students once the grading period closes. Academic Staff
(administrators) are responsible for defining the semester timetable, setting and publishing
course quotas, opening and closing the registration window, approving exceptional cases, and
generating enrolment and grade-distribution reports. Finally, a System Administrator manages
user accounts, configures system parameters, and oversees scheduled data backups.
From a technical standpoint, the university imposes several constraints. The system must
remain responsive-handling at least 1,000 simultaneous users during peak registration periods
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RBAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario  — a student successfully registers for an available course
• Boundary / edge-case scenario - a student registers for the last available seat
(quota = 1 remaining)
^  ENG  - Ф)  10:38 PM
US  4/23/2026
```

## [01:00]
**Nói:** câu số 7 này, ý đầu tiên 100% anh em sẽ làm được thôi ý này nhé, anh em chỉ cần copy paste cho mình và mình sẽ chuẩn bị cho anh em để anh em copy paste để cho anh em thì phần này, nó sẽ có là nó sẽ bảo anh em là đưa ra anh em nó sẽ yêu cầu anh em là đưa ra các cái giai đoạn kiểm thử để cho anh em, và nó yêu cầu anh em liệt kê ra, thứ nhất là anh em sẽ bị đưa ra 4 cái giai đoạn kiểm thử anh em cứ nhớ cho mình nhé, 4 cái giai đoạn kiểm thử này sau đó thì là
**Màn hình:**
```
Ớ cốc cốc  • SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  La  ...
< > G  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 #  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% -  Normal text  Arial  | -11 +  E  / Editing
6
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario - a student successfully registers for an available course
Boundary / edge-case scenario - a student registers for the last available seat
(quota = 1 remaining)
a-
^ V O  ENG  10:38 PM
US  4/23/2026
```

## [01:30]
**Nói:** cái nó hỏi là cái gì được kiểm thử và ai là người kiểm thử, ai là người chịu trách nhiệm và phần loại của nó nghĩa là các cái loại kiểm thử được áp dụng đấy là câu đầu tiên nhé thì bây giờ mình sẽ giải quyết ý đầu tiên cho anh em bằng cách là mình sẽ đưa cho anh em ý thuyết trước nhé Ok em chờ mình chút nhé Ok thì các cái kiệp Bây giờ mình sẽ nói cho em lý thuyết chứ nhé đầu
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5] Luyện tập Q7 - Google Doc x  +  La
< → C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  =
88  • Tất cả dấu trang
Luện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BI A  • I  / Editing
3  4  5  6
Cách làm
3
G  10:39 PM
4/23/2026
```
**Màn hình:**
```
Untitled - 1 / 0 - Scrble Lite
Untitled • 1/0 • 1280%  •
^ V 0  ENG -Ф) E 4/23/2026  10:39 PM
```

## [02:00]
**Nói:** tiên này để làm câu một này nhá Nói chung là đi thì anh em có bị vết thôi tí nữa mình hướng dẫn anh em nhé Ok câu đầu tiên ý đầu tiên của cô bạn này thì nó yêu cầu anh em liên kê ra các giai đoạn kiểm thử thì anh em cần phải biết cho mình có bốn ngày đoạn kiểm thử anh em nhé có bốn một là Unix nó là Unite Ok thì cái này là cái gì
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5 / 5 • Fit (123%)  •  S& D
^V  ENG  10:40 PM
US  4423/2026
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled * 5 / 5 • Fit (123%)  •
4gd Unit test.
I a  ste  ENG 4) & 4/23/2026  10:40 PM
```

## [02:30]
**Nói:** thì em cứ nhớ cho mình đối tượng đối tượng của cái kiểm thử này là gì đây nó chính là kiểm thử đơn vị thì nó sẽ kiểm thử bằng cách nào nó đi vào từng class từng cái nhỏ nhất nó đi vào từng cái nhỏ nhất trong cái phần mềm của anh em ví dụ nó đi vào từng cái class từng cái module vân vân đó thì nói chung cái này là cái gì nó sẽ là các cái thành phần nhỏ nhất của má nguồn được chưa như là các hàm phương thức hay là các class
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5 / 5 • Fit (123%)  •
4od Unit testin.
j.
• A  ste  N 4 12342026  10:40 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled  • 5/5 • Fit (123%)  •
4go Unit testin,
j.
I A  ^ VO  10:41 PM
```

## [03:00]
**Nói:** được chưa nhé đó anh em nhớ cho mình nhé thì nó sẽ đi vào từng cái này như là hàm function này hay là method này hay là class nó sẽ đi sâu vào trong những cái này được chưa đấy chính là lý do tại sao nó gọi là kiểm thử đơn vị nó là unit testing đấy nhỉ và mục tiêu nó là gì mục tiêu nó là đảm bảo mỗi đơn vị code này nó sẽ luôn hoạt động một cách logic nói chung là nó sẽ đấm sâu với code
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled  • 5/5 • Fit (123%)  •
4go Unit testin,
ste  NG 2232026  10:41 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
poi  Untitled • 5/5 • Fit (123%)
hom, mother, class
• •  ^ V 0  ENG -Ф) E4/23/2026  10:41 PM
```

## [03:30]
**Nói:** kiểm thử trong code luôn và người thực hiện đây này, hu đây này người thực hiện là ai, nó chính là developer nhớ cho mình nhé nhớ cho mình ok, developer này tiếp theo thì nó là loại kiểm thử đây chứ anh em, loại kiểm thử kiểm thử thì nó là cái gì thì nó sẽ chính là whitebox testing anh em nhớ cho mình nhé whitebox ok đó ok thì anh em chỉ cần nhớ như vậy cho mình thôi nhé đó đấy là cái đầu tiên giai
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5 / 5 • Fit (123%)
ham, mothed, class
^ V  ENG Q) & E4/23/2026  10:41 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled * 5/5 • Fit (123%)
hàm
I mothed, class
Who: Reveliper.
Luại Klểổ..  Whil
• •  ENG  US  4 4/23/2026  10:42 PM
```

## [04:00]
**Nói:** sẽ là unit testing tiếp theo thì anh em sẽ có lại in through integration testing Ok integration testing nó là gì nó là kiểm thử tích hợp vậy thì cái này là cái gì thì anh em cứ nhớ cho mình đối tượng mà cái này test là cái gì nó là sự tương tác giữa các module hoặc
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5/5 • Fit (123%)
hàm  I mothed, class
Who: Reveliper.
Luại Klểổ..  Whitetor testo
^ V  ENG - Ф) 4/23/2026  10:42 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5 / 5 • Fit (123%)  •
Luại Kla...  Whitetoz testing
Intergration test..
^ V  ENG - + E4/23/2026  10:42 PM
```

## [04:30]
**Nói:** Anh em nhớ cho mình nhé Sự tương tác giữa các module Thì ví dụ anh em có là Module đăng ký Anh em sẽ có là module đăng ký Và nó sẽ kết nối Nó kết nối Kết nối Với database Được chưa anh em Ví dụ như vậy thì nó chính là sự tương tác giữa module
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
poi  Untitled • 5 / 5 • Fit (123%)  •
Luại Kla...  Whitetoz testing
Intergration test...
G  Ste  ENG 4) 4/23/2026  10:42 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled * 5/5 • Fit (123%)
Luại Klen...  Whitetoz testing
Intergration test...
Madule Pay let nt Dis
• •G  ^ V  US  4/23/2026  10:43 PM
```

## [05:00]
**Nói:** Và các dịch vụ Đó anh em nhớ cho mình nhé Đó nhớ cho mình là sự kết nối sự tương tác giữa module và các dịch vụ nhớ cho mình như vậy, và mục tiêu của cái này là gì? để phát hiện ra lỗi trong việc giao tiếp, truyền dữ liệu giữa các thành phần nhớ đơn giản như vậy thôi, đó là phát hiện ra lỗi này trong cái việc mà giao tiếp và truyền dữ liệu giữa các thành phần, anh nhớ như vậy thôi và tiếp theo này, người thực hiện đúng không? who này thì cái này là gì? anh em có nhớ cho mình
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled * 5/5 • Fit (123%)
Luại klei..  Whitetoz testing
Intergration test..
Module Ply' let nt Dis
^  ENG  US  4/23/2026  10:43 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled * 5/5 • Fit (123%)
Intergration test...
Module Pry let nt Dis
I a  Ste  ^ V  ENG  US  - 4/23/2026  10:43 PM
```

## [05:30]
**Nói:** đó là developer đó, hoặc hoặc nhá là qa team anh em có nhớ vậy như cho mình nhá Tí nữa mình sẽ cho em cái em lấy làm cô này luôn bà em chỉ cần copy paste thôi nó ok thì anh em vẫn thấy hiểu qua một chút đấy nhỉ tiếp theo thì loại kiểm thử nhá hai thì em cứ nhớ cho mình cái này trên này quay mốc testing đúng không thì đằng dưới này là người test great box testing Ok nhớ cho mình nhé Ok tiếp theo này đó sau cái interlations này thì nó sẽ là system testing
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled * 5/5 • Fit (123%)
Intergration test...
Module Ply' let nt Dis
Who. Pe Ve.
Site  ENG 4) $ 4/23/2026  10:43 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5/5 • Fit (123%)  •
IT V 1---,  Q A  XIar
туре.
Try-le
^ V 0  10:44 PM
```

## [06:00]
**Nói:** đó là testing hệ thống này nhé system testing để xem nha system testing thì nó gì chắc chắn rồi đúng như cái tên nó thôi là nó sẽ test toàn bộ hệ thống hoàn chỉnh sau khi tích hợp test toàn bộ sau khi mà tích hợp với xe ngang tiết toàn bộ sau khi mà tích hợp đó mục tiêu nó gì mà sẽ xác
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5/5 • Fit (123%)  •
IT V 1---,  at tin
туре.
• H  10:44 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Poi  Untitled • 5/5 • Fit (123%)  •
IT V 1---,  At tim
туре.
Gry-bortestu..
systentest...
test tam to
^ VO  10:44 PM
```

## [06:30]
**Nói:** minh xem là hệ thống này nó đã đáp ứng đủ nhu cầu chưa được chưa anh em nhớ cho mình nhé nó chỉ đơn giản là xác minh xem là đã đáp ứng đủ các yêu cầu chưa Thế thôi rồi chưa đó tiếp theo là người thực hiện nó thì chắc chắn rồi nó sẽ là các cái người tester hay nó còn gọi là kiểu là đội ngũ của QA hoặc là qc team để chơi nhau đó Ok tiếp theo này loại kiểm thử thì trên này mình có
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
L  Untitled * 5/5 • Fit (123%)  •
Tray-bontestu..
systentest...
test tam be
ste  ^ VO  10:44 PM
```
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5/5 • Fit (123%)
test tam bi?
Who tester.  Q.
^ V  ENG -Ф) 4/23/2026  10:45 PM
```

## [07:00]
**Nói:** đây có rồi thì đây nó sẽ là vừa lạnh từ trên nha đó đây nó sẽ vừa lạnh và cuối cùng là cái uat uat là gì nó user acceptance testing không Nó chỉ là xếp thường testing thôi thì cái này nó
**Màn hình:**
```
Untitled - 5 / 5 - Scrble Lite
Untitled • 5/5 • Fit (123%)
test tam be
Who tester.
Team
^ V  US  4/23/2026  10:45 PM
```
**Màn hình:**
```
Untitled - 6 / 5 - Scrble Lite
Untitled • 6/5 • Fit (123%)
VUMO  les ter.
team
Black bose test...
MAT
ite  ENG )E 4/23/2026  10:45 PM
```

## [07:30]
**Nói:** nó sẽ là kiểm thử chấp nhận nó gọi là thế thôi nhưng mà nó kiểu là bây giờ nhiều anh em hiểu đơn giản này nhá mục tiêu của này là gì là nó sẽ đưa cho khách hàng nó sẽ đưa cho chính những người user sẽ đưa cho chính user test luôn ví dụ nhá Bây giờ mình đang làm được mình đang có một trang web nó mình em mình đang có một trang web của họ ví dụ mình đang có một trang web mình có là một trang
**Màn hình:**
```
Untitled - 6 / 5 - Scrble Lite
Poi  Untitled • 6/6 • Fit (123%)  •
lester.
team
Black bose test...
MAT
Site  ENG -Ф) 4/23/2026  10:45 PM
```
**Màn hình:**
```
cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  Thẻ mới  +  La  -
Q  / |
88  • Tất cả dấu trang
+
them mol  Xin vào lớp  hr Roo?  Inbox (35T)  Shapee So...  Đãu Tư Online  VUIK CUPC
Tìm kiếm với Cốc Cốc
ENG  Ф)  10:46 PM
US  4/23/2026
```

## [08:00]
**Nói:** bây giờ ví dụ khi mà anh em mua trang web của mình đúng không? bây giờ ví dụ anh em mua trang web của mình đúng không? khi anh em mua tài liệu của mình, mình làm sao trang web này rồi đúng không? mình không thể biết được là nó còn bất ngờ hay không chính vì vậy mình sẽ luôn luôn đưa ra cho anh em dùng anh em dùng xong mình mới biết là nó có bất kỳ gì nó có bất kỳ và mình sẽ fix tiếp được chứ nhé, đó
**Màn hình:**
```
cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  Thẻ mới  +  La ..
https://tuanvaquantop1.onrender.com  • | Ф
88  • Tất cả dấu trang
Học cùng Tuấn và Quân - Nễn tảng học tập FPT University - tuanvaquanfptu-1.onrender.com
+
r 22°C - Sơn Tây, Hà  TQMaster - Nên tảng luyện thi trực tuyến - tuanvaquantop1.onrender.com
Học cùng Tuấn và Quân - Nễn tảng học tập FPT University - tuanvaquanfpt.onrender.com
Q  tuan - Tìm kiếm trên Cốc Cốc
Tuấn Hưng - Ca sĩ
Tuấn Trần - Diễn viên
TQMaster - Nễn tảng luyện thi trực tuyến - tuanvaquantop1.onrender.com/admin/orders
tuan - Hỏi Al Hay
Tin nóng  Kiến nghị tăng lương cơ sở 13 %  Ngay tuăn sau, Tập đoàn Sơn
- 15 % để bảo đảm cuộc sống  Hải sẽ khởi công tuyến cao tốc
cho cán bộ công chức  xuyên rừng đẹp nhất Việt Na...
Bất động sản
ND NLD - 1 ngày trước  - CAFEF - 1 ngày trước
Pháp luật
Cháy căn hộ tăng 16 chung cư ở TPHCM, người dân hoàng loạn tháo
chav
ENG  10:46 PM
US  4/23/2026
```
**Màn hình:**
```
cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  Học cùng Tuấn và Quần - N  +  La  -
tuanvaquanfptu-1.onrender.com  ICD
88  • Tất cả dấu trang
Tuấn & Quân  +
Khóa học  Dịch vụ  Tài liệu  Coursera  Liên hệ  Admin  Đơn hàng  Admin
Dịch vụ học tập FPT
Học TRANS
Nắm vững kiến thức TRANS, tự tin hoàn thành mọi bài tập
Hỗ Trợ Tài Liệu Ôn Thi
70.000 đ  Đăng ký →
TÀI LIỆU ÔN THI
Ôn tập đúng trọng tâm, đậu môn không
lo
Tài liệu được tổng hợp từ các kỳ thi thực tế, giúp bạn biết chính xác những gì
cần học.
ENG  10:46 PM
US  4/23/2026
```

## [08:30]
**Nói:** thì đấy nó chính là cái cái giai đoạn cuối cùng được chứ nhé và nó gọi là nó gọi là Accepted Testing được chứ nhé, đó anh em nhớ đơn giản như vậy thôi và người thực hiện nhé như mình vừa nói rồi, nó chính là user nó chính là user anh em nhé ok chưa, đó thì tiếp theo này nó sẽ có là là cái tiếp theo là cái gì nhỉ Chứ còn cái loại nữa nó còn cái thai đó cái thai thì anh em cứ nhớ
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc  +  Lal
+ → C& docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • |
• Tất cả dấu trang
Luện tập Q7 * G  +
• •  • a-  Share
File Edit View Insert Format Tools Extensions Help
9sc& A S 100% - Normal text =  Arial  |- 11] +  / Editing
1...  3  4  6
Cách làm
-
• A  1 4232026  10:46 PM
```
**Màn hình:**
```
Untitled - 6 / 6 - Scrble Lite
Untitled • 6/6 • Fit (123%)
• A  Ste  ^ VO  ENG 4) 4/23/2026  10:47 PM
```

## [09:00]
**Nói:** cho mình đó là alpha hoặc là beta vết tịch em nhớ thì cho mình đấy nhé Ok xin đó không rồi nhá và kiến thức thứ hai mình muốn đưa đến cho anh em đó là cái kịch bạn tiết cây để cho anh em nó gọi là kỹ thuật tiết cây thì nó sẽ có trong cái khi mà em biết các cái tiết cây thì nó sẽ có một
**Màn hình:**
```
Untitled - 6 / 6 - Scrble Lite
Untitled • 6/6 • Fit (123%)  •
MAT  (users)
10:47 PM
```
**Màn hình:**
```
Untitled - 6 / 6 - Scrble Lite
L  Untitled • 6/6 • Fit (123%)
type.  Alphel Beta testing.
Ste  ^ V O  ENG - Ф) 4/23/2026  10:47 PM
```

## [09:30]
**Nói:** cái nó gọi là các cái kỹ thuật để mà bao phủ được các trường hợp các cái kịch bạn để cho anh em thì nó sẽ đưa cho anh em ba kịch bạn thấy chưa Ví dụ em nhìn trong đề nhé em nhìn cho bề anh nhìn có bảy đây cô này thì trong câu này em nhìn này nó cho anh em ba là kịch bản thứ nhất
**Màn hình:**
```
Untitled - 6 / 6 - Scrble Lite
L  Untitled • 6/6 • Fit (123%)
type.  Alphel Beta testing.
^ VO  10:47 PM
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< →  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  ICO
88  • Tất cả dấu trang
+
X  SWE202c_Practical_Exam_Sample.docx.pdf  • Open with Google Docs  +  :  Share
My Dr  1. Map the four standard testing stages to the CRS development process. For each stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
Home  • Integration Testing
My Drive  System Testing
• User Acceptance Testing (UAT)
• LD Computers
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios listed below:
Present each test case in a table with the columns as below: (10 points)
Shared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario - a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Staired
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
@ Trash  SWE202c_Practical_Exan
TC2
Storage
24h CB of 15 GB used
Gel more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  20.  20%
UC Modeling  Page  15%
3  UC Specification  15%  203
^  ENG  Ф)  10:48 PM
US  4/23/2026
```

## [10:00]
**Nói:** là Happy Pass đúng không Happy Pass nó là cái gì nó sẽ là cái kịch bản mà lý tưởng nhất như là sao mọi điều kiện nó sẽ thoải mái hết ví dụ trong cái này nó khi nào nó gọi là mọi thứ đều thoải tiền đó là sinh viên sẽ đủ điều kiện tiên quyết để cho sinh viên đủ điều kiện tiên quyết để đăng ký khoa học và khi mà đăng ký vào khoa học khoa học đấy sẽ còn chỗ đó thì đấy là cái điều kiện lý tưởng nhất con ấy trường hợp mà xấu đó thì tí nữa mình nói sao được chưa thì đấy nhá Đấy là trường hợp
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  ICO
88  C Tất cả dấu trang
+
Drive  Spatch in Drive
New  My D  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is  88
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
home  • Integration Testing
My Drive  System Testing
• User Acceptance Testing (UAT)|
•LD Computers
Write THREE test cases for the Register for Course' use case, covering the scenarios listed below.
Present each test case in a table with the columns as below: (10 points)
Shared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario — a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Staired
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
D Trash  SWE202c_Practical_Exanl
TC2
Storage
24h CB of 15 GB used
Gel more storage
III. SCORING RUBRIC
Q#  Topic  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
UC Modeling  1.5  15%
UC Specification  1.5  15%
ENG  10:48 PM
US  4/23/2026
```
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP
88  C Tất cả dấu trang
+
Drive  Search in Drive
~
New  My DI  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
rome  • Integration Testing
System Testing
My Drive
• User Acceptance Testing (UAT)|
• LD Computers
Write THREE test cases for the Register for Course' use case, covering the scenarios listed below.  f
Present each test case in a table with the columns as below : (10 points)
Shared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario- a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Statred
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
• Trash  SWE202c Practical_ Exain_-
TC2
Storage
146 CB of 15 GB used
Gel more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
UC Modeling  1.5  15%
UC Specification  1.5  15%
ENG  Ф)  10:48 PM
US  4/23/2026
```

## [10:30]
**Nói:** đấy là trường hợp việc nó bếp trường hợp lý tưởng nhất là không bị bất phải một cái lỗi gì được chưa thứ hai là bao nhiêu đi bắt đi này nó là cái gì nó sẽ là cái mà phân tích giá trị biên chưa em nhớ cho mình nhé Nó gọi là phân tích giá trị biên thì nó là cái gì mà sẽ tập trung vào những cái điểm nhạy cảm với thống ví dụ như là ví dụ như là nhé chỗ trống của một cái con nó chỉ còn đúng một thôi thì xinh nhé cái chỗ trống đấy bằng một cái xinh nhé Đấy những cái điểm mà ngại nhạy cảm mất nghe là
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  ICO
88  C Tất cả dấu trang
+
Drive  Search in Drive
New  My DI  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
rome  • Integration Testing
System Testing
My Drive
• User Acceptance Testing (UAT)|
• L0 1  Computers
f
Write THREE test cases for the 'Register for Course' use case, covering the scenarios listed elow.
Present each test case in a table with the columns as below: (10 points)
Shared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario- a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Statred
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
D Trashi  SWE202c_Practical_Exanl
TC2
Storage
24h CB of 15 GB used
Get more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
2  UC Modeling  1.5  15%
3  UC Specification  1.5  15%
ENG  Ф)  10:48 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  ICO
88  • Tất cả dấu trang
+
Drive  Sodich in Drive
CourseOffering, Registration, Waitlist, Grade, Semester, Report.
My D
Question 6: Testing Stage and Type (15 points)
HOme
1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
My Drive  tested, who is responsible, and which testing types are most applicable: (5 points)
Unit Testing
• Li Computers  Integration Testing
System Testing
Shared with me  User Acceptance Testing (UAT)
Recent  2.  Write THREE test cases for the 'Register for Course' use case, covering the scenarios listed below.
Statred  Present each test case in a table with the columns as below: (10 points)
Happy-path scenario - a student successfully registers for an available course
•  Boundary / edge-case scenario - a student registers for the last available seat (quota = 1 remaining)
Spam  Negative / error scenario — a student attempts to register without meeting the course prerequisite
• Trash  SWE202c_Practical_Exan.
TCID  Test Case Name  Precondition  Test steps  Expected result  Test type
Storage
TC1
2.46 CB of 1b GB used  TC2
Gel more storage
III. SCORING RUBRIC
Торіс  Max Score  Weight  Grader's
Score
ENG  Ф)  10:48 PM
US  4/23/2026
```

## [11:00]
**Nói:** là ví dụ như là hết chỗ hoặc là còn một chỗ thấy cái điểm nhạy cản được chưa Thấy thì là phải có những cái thiết kê như vậy đó tiếp theo thì là cái cuối cùng là cái negatif thì nó là cái gì nghe tiếp này thì nó sẽ là cái trường hợp mà đọc thử các trường hợp sai quy tắc được trên nhà thử các trường hợp mà sai quy tắc cố tình làm lỗi để xem hệ thống nó có chắc lại được không phải cho lỗi như là mình sẽ cố tình làm lỗi nếu mà hệ thống mà kiểu là phát hiện ra lỗi và chặn được cái lỗi
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP
88  • Tất cả dấu trang
+
Drive  Search in Drive
New  My D  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
romel  • Integration Testing
My Drive  System Testing
• User Acceptance Testing (UAT)
• Lo Computers
Write THREE test cases for the Register for Course' use case, covering the scenarios listed below.
Present each test case in a table with the columns as below: (10 points)
Shared with me
Happy-path scenario - a student successfully registers for an available course
Recent  • Boundary / edge-case scenario — a student registers for the last available seat (quota = 1 remaining)
Negative / error scenario — a student attempts to register without meeting the course prerequisite
Staired
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
• Trash  SWE202C  practical Exain.-
TC2
Storage
24h CB of 15 ot used
Get more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
UC Modeling  1.5  15%
3  UC Specification  1.5  15%
ENG  Ф)  10:49 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  ICO
88  C Tất cả dấu trang
+
Drive  Search in Drive
~
New  My DI  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
Homel  • Integration Testing
My Drive  System Testing
• User Acceptance Testing (UAT)
•Li Computers
Write THREE test cases for the Register for Course' use case, covering the scenarios listed below.  f
Present each test case in a table with the columns as below: (10 points)
Shared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario - a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Statred
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
• Trash  SWE202-  Practical Exain.
TC2
Storage
24h CB of 15 Gb used
Gel more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
UC Modeling  1.5  15%
3  UC Specification  1.5  15%
ENG  Ф)  10:49 PM
US  4/23/2026
```

## [11:30]
**Nói:** đấy thì là đúng cái chưa Ví dụ như là học sinh sinh viên mà chưa đủ với điều kiện kiến quyết thì hệ thống này nó phải không cho thằng này học không cho mày đăng ký là chưa Thư Nếu mà hệ thống mà họ vẫn cho này đăng ký tiếp thì là hệ thống đang bị lỗi được chưa đó đó là cái trường hợp cuối cùng là đó thì bạn số nhất Ok thì đấy là vì kiến thức cơ bản cho nhau Ok vậy thì bây giờ mình sẽ sang
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP
88  C Tất cả dấu trang
+
Drive  Search in Drive
New  My DI  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
rome  • Integration Testing
System Testing
My Drive
• User Acceptance Testing (UAT)|
• L0 1  Computers
Write THREE test cases for the Register for Course' use case, covering the scenarios listed below.  f
Present each test case in a table with the columns as below : (10 points)
Shared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario- a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Statred
TCID  Test Case Name  Precondition  Test steps  Expected result Test type
Spam
TC1
D Trashi  SWE202:_ Practical_ Exan_-]
TC2
Storage
24h CB of b GB used
Get more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
UC Modeling  1.5  15%
3  UC Specification  1.5  15%
ENG  Ф)  10:49 PM
US  4/23/2026
```
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Docs  I+  La
< →  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  ICO
88  • Tất cả dấu trang
+
X  SWE202c_Practical_Exam_Sample.docx.pdf  • Open with Google Docs  Share
• User Acceptance lesting (UAT)
My Dr
2. Write THREE test cases for the Register for Course' use case, covering the scenarios listed below.
Present each test case in a table with the columns as below: (10 points)
• Happy-path scenario — a student successfully registers for an available course
Home
Boundary / edge-case scenario — a student registers for the last available seat (quota = 1 remaining)
My Drive  Negative / error scenario - a student attempts to register without meeting the course prerequisite
• Lo Computers  Test Case Name  Expected result
TCID  Precondition  Test steps  Test type
Shared with me  TCI
Recent  TC2
Statred
Spam
•i Trash  III. SCORING RUBRIC  SWE202c_Practical_Exun
Storage
O#  Max Score  Weight  Grader's
Score
146 CB of 15 be used
Software Development Model Selection  2.0  20%
Gel more storage  2  UC Modeling  1.5  15%
UC Specification  1.5  15%
4  Non-Functional Requirements  1.0  10%
Class Diagram  2.5  25%
Testing Stage and Type  1.5  15%
TOTAPage  /  -  100%
203
ENG  Ф)  10:50 PM
US  4/23/2026
```

## [12:00]
**Nói:** cách làm đúng không thì bây giờ chắc chắn rồi mình sẽ phải là có à à Ừ mình sẽ phải là có cái cái gì nhỉ cái cái bản như nhé đi thì anh em cứ nghĩ cho mình các bạn em nghĩ bạn sang là tuyệt đẹp nhất ở đây mình cái 4 này và bốn ngày đó bốn cục và bốn giai đoạn 1234 Ok nó xong rồi nhỉ
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +  La ..
+ C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  + 0 =
• Tất cả dấu trang
Lun tập Q7 * G  +
• a-  • Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIVA GEO  / Editing
1... F  4  5  6
=
Cách làm
N
• •  ^ V Q  10:50 PM
4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc  +  Lal
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  • I CD  =
88  • Tất cả dấu trang
Luyện tập Q7  +
Share
File  Edit  View Insert Format Tools Extensions Help
Q  Image  - [11]+ BI UA0|  GH •  E #S•E•E•E  0 Editing
Table  E Building blocks  4  5  6 r..?.
• Building blocks
& Smart chips
Pe esignature  Premium
G Link  Ctrl+K
4 x 1
• Drawing
Il. Chart
Symbols
Cách làm
E Tab  Shift+F11
- Horizontal line
E Break
• Bookmark
© Page elements  Updated
N
+ Comment  Ctrl+Alt+M
• •  10:50 PM
4/23/2026
```

## [12:30]
**Nói:** ok Ừ thì ở đây nhá thì đầu tiên này nó sẽ làm các giai đoạn đúng không em
**Màn hình:**
```
G c cố  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La ..
< → C ® docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • |  L IQ =
• Tất cả dấu trang
Luyện tập Q7 # G (5 Saving...  +
• a-  © Share
File Edit View Insert Format Tools Extensions Help
asc8 A S 100% -  Normal text -  Arial  - -11+ BI UA GEO  E #S•E•EEEX
L.....  • 2  3 П. 4
3 of 23
Il
Cách làm
• •  ^ V  10:50 PM
```
**Màn hình:**
```
Ớ cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc X  +  Lal
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luện tập Q7 # G 65 Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
A, § 100% - Normal text =  Arial  | - 11] +  BIU A  / Editing
VOGIE TOTTE
^ V Q  ENG  10:51PM
4/23/2026
```

## [13:00]
**Nói:** nó sẽ các giai đoạn này em nhé testing testing Ok tiếp theo là gì nó là quá quá quá tiếp theo nữa là cái gì tiếp theo nữa là ai là người chịu chứng nhận một cái đẻ hù luôn
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
• Tất cả dấu trang
Luyện tập Q7 # G 6) Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A • 100% - Normal text ~  Arial  | - 11] +
4  6
Cách làm
Tét|
^ V O  ENG  10:51 PM
```
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A • 100% - Normal text ~  Arial  | - (11  +  U
1..
Cách làm
Testing Stage  What is tested
G te  ^ EQ  ENG E 4/23/2026  10:51 PM
```

## [13:30]
**Nói:** và cuối cùng thì là các loại thì mình sẽ có là testing hay hay để cho nhau đó Ok thì mình sẽ xử lý bốn cái này đầu tiên như mình nói rồi đầu tiên là gì nhỉ unit testing ok thứ hai là integration testing
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Dock x  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A • 100% - Normal text ~  Arial  - | 11  +  I U
Cách làm
Testing Stage  What is tested
^ EQ  10:51 PM
ENG 6 4/23/2026
```
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text =  Arial  - 11] +  BI UA
3 Dau ami
Testing Stage  What is tested  Who  Testing type
Unit Testing
^ E Q  ENG  10:52 PM
US  10 423/2026
```

## [14:00]
**Nói:** ok tiếp theo đó là gì kiểm thử tích hợp vào đây system testing và bây khi anh em copy paste cho mình nhé đừng nghĩ nhiều anh em ạ mình sẽ làm cho anh em cái bản chi tiết nhất là anh em đạt được điểm tối đa cô này này chưa cho nên em chỉ cần copy cho mình không Nếu đi thi đọc cô này thì anh em ăn không không phải nằm hiểu luôn Ok thì câu này nhá tương mại à
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Dock x  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A 5 100% -  Normal text  Arial  | - 11) +  BI UA
6
Testing Stage  What is tested  Who  Testing type
Unit Testing
Intergration Testing|
^ E Q  ENG  10:52 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A & 100% - Normal text ~  Arial  | - 11) +  BI UA
6
Testing Stage  What is tested  Who  Testing type
Unit Testing
Integration Testing
System Testing
Il
^ EQ  ENG  10:52 PM
US
```

## [14:30]
**Nói:** đúng không hát xét xét tình đúng không anh em nhớ cho mình nhớ nhớ là phải copy đấy đừng nghĩ nhiều đây em xem này để em hiểu không Ok thì bây giờ mình sẽ đi vào chi tiết này đầu tiên đúng không thì anh em cứ nhớ cho mình cái đầu tiên là cái unit này nó sẽ chết cái gì thì em cứ mặc định cho đó là nó sẽ là in đi vì ngọt con Polin à à mô đun
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A & 100% - Normal text ~  Arial  | - 11] +  BI UA
3  Jaun am  6
Testing Stage  What is tested  Who  Testing type
Unit Testing
Integration Testing
System Testing
Al
^ EQ  ENG  10:52 PM
US
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
+ → C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
9508100% -  Normal text  Arial  | - 11] +  BIA•
4
Cách làm
Testing Stage  What is tested  Who  Testing type
Unit Testing  In
Integration Testing
System Testing
Acceptance Testing
^ E 0  ENG  10:53 PM
US  4/23/2026
```

## [15:00]
**Nói:** mô đun in iso lấy sớm cái này gì như là từng thành phần riêng này được chưa sau đó anh em thêm cho mình đó là xe xe bồ bạc chưa thì em thêm cho mình là nấu in
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
+ C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
9508 100%  Normal text  Arial  | - 11] +  BI UA•
_ 2  3-1 L  4  6
Cách làm
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individua |
Integration Testing
System Testing
Acceptance Testing
I a  ^ E Q  ENG  10:53 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
+ > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIU A O  • FO
4
Cách làm
Testing Stage  What is tested  Who  Testing type
...
Unit Testing  Individual
components / module
in isolation|
Integration Testing
System Testing
Acceptance Testing
• •  ^ E  ENG  10:53 PM
US  4/23/2026
```

## [15:30]
**Nói:** nè lúc in Paris đây xin lỗi dịch nó cho anh em đi kia copy nguyên cái này cho mình nhá Bây giờ mình ở đúng không Thêm luôn này mà đó là mình sẽ đi ăn chết con chết con đi xin trích con đi sân này và có tờ kênh lấy sân Ok đó anh em đến bên đây cho mình nó người thì
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
+ > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIA•  • FO
4
Cách làm
Testing Stage  What is tested  Who  Testing type
LEE
Unit Testing  Individual
components / module
val olation - 6.9, login
Integration Testing
System Testing
Acceptance Testing
• •  ^ E  ENG  10:53 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +  La ..
+ > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  " ®  @ |
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BI A
3 -1  4  6
=
Cách làm
Testing Stage  What is tested  Who  Testing type
...
Unit Testing  Individual
components / module
in isolation - e.g, login
validation logic, gec
Integration Testing
System Testing
Acceptance Testing
• •  ^ E  ENG  10:54 PM
US  4/23/2026
```

## [16:00]
**Nói:** chắc chắn rồi đó là đi proper được nghĩa chất mình vừa nói rồi và tiếp theo ra các cái kiểm cái đầu tiên không quên đó là whitebox testing
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
+ > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  " ®  • I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BA O
4  6
=
Cách làm
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual
components / module
in isolation - e.g, login
validation logic,
check condition|
Integration Testing
System Testing
Acceptance Testing
• •  ^ E  ENG  10:54 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
+ > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 * G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIU
.....
Cách làm
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White
components / module
in isolation - e.g, login
validation logic,
check condition,
quota calculation
Integration Testing
System Testing
Acceptance Testing
203
• •  ^ E Q  ENG  10:54 PM
US  4/23/2026
```

## [16:30]
**Nói:** tiếp theo anh em thêm cho mình nhé đó là functional thêm hết cho mình nhé functional testing nói chung là nhấn copy paste cho mình chỗ này bảo đổi bảo đổi và đi nó cho mình ba cái này bạn tiếp theo nữa thì mình sẽ có là integration testing
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  La
+ > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
E  Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11 +  BIU
Cách làm
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Fl
validation logic,
check condition,
quota calculation
Integration Testing
System Testing
Acceptance Testing
203
• •  ^ EQ  ENG  10:54 PM
US
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  Lal
< > G  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q s  A 5 100%  Normal text  Arial  - 11 +  BIU  1E
Testing Stage  What is tested  Who  Testing type
...
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Valuel
quota calculation
Integration Testing
System Testing
Acceptance Testing
• •  G  ^ E  ENG  10:55 PM
US  4/23/2026
```

## [17:00]
**Nói:** thì mình sẽ có cái gì mình sẽ có là interaction cái này mình có nói rồi interaction mà sẽ là sự là giữa biết tin biết thuyền mô đun em sơ vai nó được cho các mô đun thì nó sẽ và mình sẽ có là ví dụ em kết hợp ví dụ thì em sẽ kiểm
**Màn hình:**
```
Ở cỐc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q s  & A S 100% - Normal text ~  Arial  - 11+  BI U
Testing Stage  What is tested  Who  Testing type
...
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing
System Testing
Acceptance Testing
I a  ^ E  ENG  10:55 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  | - 11) +  BIU
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between!
System Testing
Acceptance Testing
I a  ^  ENG  10:55 PM
-  US  4/23/2026
```

## [17:30]
**Nói:** là cái cuối cùng đó là Android Android con nét tinh mình đang định viết là tương tác giữa mô
**Màn hình:**
```
Ở cỐc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  Ca
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luện tập Q7 * G  @ Saved to Drive  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q s  A 5 100%  Normal text  Arial  - 11 +  BIU
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module -egl
System Testing
Acceptance Testing
203
I a  ^ E  ENG  10:55 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  Ca
< > G  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luện tập Q7 * G 6) Saving...  +
• -  Share
File  Edit View Insert Format Tools Extensions Help
Q s  & A S 100% - Normal text ~  Arial  - 11 +  BI UA
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module - e.g
enrollment modu
System Testing
Acceptance Testing
203
I a  G  ^ E  ENG  10:55 PM
US  4/23/2026
```

## [18:00]
**Nói:** là mô đun nó sẽ là mô đun đăng ký kết nối với mô đun điểm thì là à à à à à à à à à à à à à à à à à Cái này á Cái việc này anh em viết cái ví dụ này
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
• -  Share
File  Edit View Insert Format Tools Extensions Help
Q5 e  & A § 100% - Normal text ×  Arial  - 11 +  BIU A
LIS
Testing Stage  What is tested  Who  Testing type
N  Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module - e.g
enrollment module
connecting
System Testing
Acceptance Testing
I a  ^ E  ENG  10:56 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
• -  Share
File  Edit View Insert Format Tools Extensions Help
Q s  & A S 100% - Normal text ~  Arial  - 11 +  BI UA
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module - e.g
enrollment module
connecting to grade
module, waitlist
System Testing
Acceptance Testing
203
• •  ^ E  ENG  10:56 PM
-  US  4/23/2026
```

## [18:30]
**Nói:** Thì nó sẽ cứ liên quan Nó sẽ liên quan đến việc là Anh em sẽ nhìn Nhìn trong cái Cây study á Để cho anh em Đó Nói chung là cái Anh em sửa lại một chút Cái chỗ ví dụ nhé Chỗ nào anh em viết được ví dụ Thì biết không viết gì thôi Một và Để cho anh em Bởi vì đây này nó chỉ bảo anh em biết thế này thôi nó không bảo anh em là viết quá chi tiết nói chung là anh em viết được
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Dock x  +  Ca
docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A S 100% -  Normal text  Arial  | - 11] +  BI UA  Editing
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario — a student successfully registers for an available course
Boundary / edge-case scenario a student registers for the last available seat
(quota = 1 remaining)
Negative / error scenario — a student attempts to register without meeting the
course prerequisite
ENG  10:56 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A S 100% -  Normal text  Arial  | - 11] +  BI UA  F•E •E-E  E X  Editing
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most appilcable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario - a student successfully registers for an available course
Boundary / edge-case scenario - a student registers for the last available seat
(quota = 1 remaining)
a-
Negative / error scenario — a student attempts to register without meeting the
course prereguisite
G  E  ENG  10:57 PM
US  4/23/2026
```

## [19:00]
**Nói:** thì anh em sẽ được điểm cao nó thấy cô dễ tính vẫn được điểm thôi nhưng mà nói chung là chỗ này anh em cố gắng bám sát bám sát cái cái cây study là anh em ăn cái chỗ này thì Willis sẽ kích cái hoạt động thông báo kích hoạt cái thông báo trong cái case study nó có nếu mà
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  La
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
• -  Share
File  Edit View Insert Format Tools Extensions Help
Q s  A 8 100% -  Normal text  Arial  - 11 +  BIU
6
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module - e.g
enrollment module
connecting to grade
module, waitlist I
System Testing
Acceptance Testing
• •  ENG  10:57 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luện tập Q7 - Google Doc X  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools  Extensions Help
Normal text  Arial  0 Editing
3  .1.e
automate and streamline the entire workflow
The CRS is expected to serve four main groups of users. Students need to browse the
catalogue of available courses, check their eligibility based on completed prerequisites, submit
registration requests, and track the status of each request in real time. If a course is fully
booked, a student may join an electronic waitlist; should a registered student later drop the
course, the system automatically notifies and enrolls the first eligible student on the waitlist.
Lecturers need to review the roster of students enrolled in their courses, record midterm and
final grades, and release grades to students once the grading period closes. Academic Staff
(administrators) are responsible for defining the semester timetable, setting and publishing
course quotas, opening and closing the registration window, approving exceptional cases, and
generating enrolment and grade-distribution reports. Finally, a System Administrator manages
user accounts, configures system parameters, and oversees scheduled data backups.
From a technical standpoint, the university imposes several constraints. The system must
remain responsive-handling at least 1,000 simultaneous users during peak registration periods
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RBAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
tuture years.
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
G  Ste  ENG  10:57 PM
US  4/23/2026
```

## [19:30]
**Nói:** đây, the system auto kích hoạt cái thông báo này lên vào cái thằng đầu tiên trong tên sách trừ thì mình sẽ có là mình sẽ có là triggering notification nó sơ vai ok thì cái này nhưng mình nói rồi một là nó sẽ là thằng đi lúc cộng với thằng tester
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La  ...
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
• Tất cả dấu trang
Luyện tập Q7 # G  +
Share
File Edit View Insert Format Tools Extensions Help
5  A § 100% -  Normal text  Arial  | - 11] +  BI UA  / Editing
Question 7: Testing Stage and Type (1.5 points) I
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario — a student successfully registers for an available course
• Boundary / edge-case scenario — a student registers for the last available seat
(quota = 1 remaining)
Negative / error scenario- a student attempts to register without meeting the
course prerequisite
• a  ENG  10:57 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A § 100% - Normal text ~  Arial  - [ 11 ] +  BI UA  *•E•E-E
3 Jaur iam
Testing Stage  What is tested  Who  Testing type
....
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering nofffic
System Testing
Acceptance Testing
• •  ^ E  ENG  10:57 PM
US  4/23/2026
```

## [20:00]
**Nói:** nó thì anh em cứ biết thế này thôi còn bên này thì nghe thức thêm cho mình đó là anh em sẽ có đầu tiên đó là Black đúng nhỉ à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc x  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
• Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ~  Arial  | - [11 +  BI UA  *•E•E-E
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service (
System Testing
Acceptance Testing
^ E  ENG  10:58 PM
US  4/23/2026
```
**Màn hình:**
```
Untitled - 5 / 6 - Scrble Lite
Untitled  • 5 / 6 • Fit (123%)
systentest...
test tam to
Who tester.
team
Black bad  terd
ENG  US  4/23/2026  10:58 PM
```

## [20:30]
**Nói:** Ừ ok em biết mỗi này không phải chưa hoặc là anh em thêm cho mình cái là API testing Ok đó tiếp theo nữa thì mình sẽ có là system testing thì nó sẽ có cái gì
**Màn hình:**
```
Untitled - 5 / 6 - Scrble Lite
Untitled * 5/6 • Fit (123%)
vio.  Pe Vl.-.  LA tia
type.
Gry- bortestu:
systentest...
test tam to
^  ENG  US  4/23/2026  10:58 PM
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La  ...
+ > C® docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
G  • -  Share
File Edit View Insert Format Tools Extensions Help
95 ca A S 100% - Normal text ~  Arial  | - [11 +  BIU  "•E•E-E
2  .T..
Cách làm
Testing Stage  What is tested  Who  Testing type
...
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing
Acceptance Testing
• •  G  ^ E  ENG  10:59 PM
US  4/23/2026
```

## [21:00]
**Nói:** trong cái này nhá thì anh em viết cho mình đó là dựng em chi anh em sửa cho mình cái này em biết đúng như mình nhé anh em nhớ phải sửa nhé em chi em chi toàn bộ cái hệ thống này như thế nào bây giờ ví dụ mình đang để là CRS này để xem em đó hãy chữ nhật tất cả nghĩ nghĩa là mình là đang viết cái toàn bộ hệ thống này đúng không thì cái
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  C Tất cả dấu trang
Luyện tập Q7 * G  +
=  Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100% = Normal text =  Arial  - [ 11] +  BIU  *•E -E-  E X
.saor-e.y, vy.'  Funcua icalng
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  Il
Acceptance Testing
• •  G He  ^ E Q  ENG  10:59 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  +
< > C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # GO Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11 +  I U
1...
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggerina notification
serv entire ®P
System Testing  The entrie CRS
Acceptance Testing
1, 6
co-
• •  ^ E  ENG  10:59 PM
US  4/23/2026
```

## [21:30]
**Nói:** là cái hệ thống cost registration system đúng không, đó, thì mình đang viết là CRS, nghĩa là anh em phải đi thì anh em phải đổi lại cái chỗ này nhé, mình sẽ bôi đậm đây này, đấy, đổi lại cái chỗ này, đấy, toàn bộ hệ thống này thấy chưa, mình sẽ phải là toàn bộ hệ thống này sẽ thế nào, S tất cả chức năng, nghĩa là toàn bộ hệ thống này, tất cả chức năng và yêu cầu phi chức năng, thấy chưa, thì phải test nó đúng không, đó, thì mình sẽ
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text ~  Arial  - 11 +  BIUA  "EE-
3 Juun iam
Testing Stage  What is tested  Who  Testing type
....
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS
Acceptance Testing
Ste  E  ENG  10:59 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G® Saved to Drive  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ~  Arial  | - [11 +  BIU A  "HE E-  E X
3 Juum ram
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service (
System Testing  The entise CRS as a r
Acceptance Testing
• •  ENG  11:00 PM
-  US  4/23/2026
```

## [22:00]
**Nói:** là src system nó cũng là phải hoàn toàn bộ hoàn thành hoàn thiện toàn bộ chức năng của hệ thống về trường mà tất cả tất cả thông sinh nội trường Snow picture And non functional requirement
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  La  ...
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A § 100% - Normal text ~  Arial  | - [11 +  BI UA  "HE•E-
3 -
Testing Stage  What is tested  Who  Testing type
N  Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service (
...
System Testing  The entire CRS as a i
Acceptance Testing
I a  ^ E  ENG  11:00 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  • Luyện tập Q7 - Google Doc  +  La  ...
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ~  Arial  | - 11] +  BIU  "HE•E-
3 →
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a °
complete system - all I
functional!
Acceptance Testing
• a  ^  ENG  11:00 PM
E  US  4/23/2026
-
```

## [22:30]
**Nói:** Anh em cứ copy cho mình nhé Chỗ nào mình phải sửa thì anh em sửa Đấy chưa Đó Ví dụ Non functional requirement thì anh em nhớ cho mình Đúng 3 cái thôi rồi mình đã nói với anh em rất là nhiều ở trong các câu như câu 4 rồi có ví dụ như là em sẽ có phương phong được em sẽ có phong mình security này được chưa Và anh sẽ có là
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  La  ...
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  ICO
• Tất cả dấu trang
Luyện tập Q7 * G S) Saving..  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ×  Arial  | - 11] +  BI UA  "HE E-
3 →
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a °
complete system - all
functional features
and non - functional I
Acceptance Testing
I a  ^  E  ENG  11:00 PM
-  US  4/23/2026
```

## [23:00]
**Nói:** biết bà cái không là hai cái không được trên nhau anh em phải cho mình vân vân rồi này chắc chắn rồi thì anh em xin cứ viết cho mình làm QA QA này hoặc là testing tìm nói chung là cái đội này nó sẽ là cái gì nhóm và đảm bảo chất lượng được chưa
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  La  ...
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ×  Arial  | - 11] +  BI UA
3 →
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a °
complete system - all
functional features
and non - functional
requirements
(Performance)
Acceptance Testing
I a  Ste  ^ E  ENG  11:01 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  La  ...
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  ICO
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ×  Arial  | - 11] +  BI UA  EM DE  "HE-E
2
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing |
complete system - all
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing
• •  ^ E  ENG  11:01 PM
-  US  4/23/2026
```

## [23:30]
**Nói:** đó thì tiếp theo này nó sẽ là cái này nó là cái gì thì ở chỗ này kiểm thử toàn nó là loại gì có kính em kể cho mình làm cách bắt thương ra nhớ trên này nhá em bỏ hết cái này đi em để biết mình một loại không đó bởi vì là cái này là cái đặc trưng không cần mình dài dài testing đúng rồi nha đó tiếp theo nữa nó hoa thì là cái cái cuối cùng phải
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc x  +  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  ICO
• Tất cả dấu trang
Luyện tập Q7 # G® Saved to Drive  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  Normal text  Arial  | - 11] +  BI UA  "HE-E
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login  Functional Testing
validation logic,
check condition,  Boundary Value
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team|
complete system - all
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing
• •  ^  E  ENG  11:01 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La'
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ×  Arial  | - 11] +  BIU  *•E •E-E
3
Testing Stage  What is tested  Who  Testing type
N-  Unit Testing  Individual  Developers  White-box Testing
components / module
in isolation - e.g, login
validation logic,
check condition,
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service (
System Testing  The entire CRS as a  QA/ Testing team  Black-bax
complete system - all
functional features
and non - functional
requirements
(Performance,
security,...)
Acceptance Testing
• a  ^ E 0  ENG  11:02 PM
US  4/23/2026
```

## [24:00]
**Nói:** Cái cuối cùng này thì mình sẽ làm gì? Cái cuối cùng này nhé thì mình sẽ cho là mình nghĩ là mình sẽ phải là cho nó nhẹ nhàng hơn một chút thì mình sẽ ghi ngắn gọn thôi, ví dụ như chỗ này nhé anh em chỉ cần ghi chung chung cho mình thôi là à mình sẽ ghi là business
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luện tập Q7 - Google Doc X  La
+ C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
• Tất cả dấu trang
Luện tập Q7 # GO Saved to Drive  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11 +  U
6
validation logic,
check condition,
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system -all
functional features
and non-functional
requirements
(Performance,
security...)
Acceptance Testing
^ EQ  ENG  11:02 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100% - Normal text ~  Arial  - 11 +  I U  EM DE  "•E•E-E
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non -functional
requirements
(Performance,
security...)
Acceptance Testing
• •  ^ EQ  ENG  11:02 PM
US  4/23/2026
```

## [24:30]
**Nói:** business requirement anh quay mình quay mình quay mình em mình sẽ phải kiểm tra lại các cái yêu cầu nhiệm vụ và các giao diện là chưa thì những cái này thì nó là phim đừng hay là các staff chưa phải như là cái này nó phải lấy trong cái đề đều chơi nhau
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La
< > C  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
=  Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100% - Normal text ~  Arial  - 11 +  I  U  *•E E-E
1..
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non -functional
requirements
(Performance,
security...)
Acceptance Testing  Bussiness requirl
• •  ^ EQ  ENG  11:02 PM
US
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La
< > C  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
Q5 e  8 A S 100% - Normal text ~  Arial  |- 11 +  I U  *•E •E•E
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service (
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing  Business
requirements and
UI/UX
• •  ^ E Q  ENG  11:03 PM
US  4/23/2026
```

## [25:00]
**Nói:** thực ra những cái chú như này đây là mình đang muốn viết đều nhất để chơi nhau đó anh em chỉ cần thứ nhất là kênh ba này em đổi cái này thôi Thấy chưa Ví dụ cái này nhá Cái này thì em dư dư nguyên này cho mình interaction between mô đun thì phải giữ nguyên được chưa Nhưng mà anh em sợ là hay thay đổi cái này không hay đủ đã thay đổi những cái xe mồ này được chưa Đó ok thế là ngon
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La
< > C  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100% - Normal text ~  Arial  | - [11 +  BIU  *•E •E•E
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non -functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student |
requirements and
UI/UX
• •  ^ EQ  ENG  11:03 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  La  ...
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G 6) Saving...  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q s  @ A § 100% - | Normal text *  Arial  - 11+ BI UA
3 -  6
resung saye  VVIIO
Unit Testing  Individual components  Developers  White-box Testing
/ module in isolation -
e.g, login validation
logic, check condition,
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non- functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff
requirements and
UI/UX
• •  ^ E Q  ENG  11:03 PM
US  4/23/2026
```

## [25:30]
**Nói:** được chưa Ở thì tiếp theo này à quên còn cái thằng cuối cùng này nữa rồi xe nhé thằng cuối cùng này thì nó là alpha hoặc là beta có alpha gạch bị ta testing anh em nhớ này cho mình là ngon được chưa nó Ok chưa biết đúng như này là ngon ngon anh nhé Để vậy là anh em được 0,5 rồi anh nhận đây là phát 1
**Màn hình:**
```
Ới cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  La
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  Normal text  Arial  -11+
.....  YVIU
resung staye  resiny sype
Unit Testing  Individual components  Developers  White-box Testing
/ module in isolation -
e.g, login validation
logic, check condition,
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non- functional
requirements
(Performance,
security,...)
Acceptance Testing  Business  Student/ Staff
requirements and
UI/UX
• a  ENG  11:03 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD)
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
95 ca A S 100% - Normal text ~  Arial  - [ 11 ] +  I  U  1E  *•E•E-E
mouut, wamet
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
UI/UX
• a  ^ E Q  ENG  11:04 PM
US
```

## [26:00]
**Nói:** Ok đó tắt một anh nhé và tiếp tục xuống đây à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à thì cái phát 2 này nó sẽ khó hơn một chút để cho nhau đấy lý do tại sao nó trên nhau một cái không phải là một cái một điểm đi nhầm nhắc thì cái thứ hai nó là phép viết cái cây nhầm nhắc nó thì em
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +
< → C ® docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 # G 6 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
asc8 100% -  Normal text -  Arial  - 11+ BI UA•  CHD TECEEEE X  0 Editing
TaL...  2  4
Cách làm
1 I
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual components  Developers  White-box Testing
IRO R C G O C O  ^ E 0  ENG  11:04 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  Luyện tập Q7 - Google Dock x  +  La
+ > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q5 e  Normal text  Arial  | - 11 +  BI UA  Editing
1..
=  1 of 23
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario — a student successfully registers for an available course
• Boundary / edge-case scenario — a student registers for the last available seat
(quota = 1 remaining)
Negative / error scenario - a student attempts to register without meeting the
course prerequisite
E  ENG  11:04 PM
-  US  4/23/2026
```

## [26:30]
**Nói:** biết đúng cho mình cái con đây nó ví dụ như trong bìa cái kia nha trong bề này nó có đúng cái bạn như này chưa tiếp cây một này cái cây đi là cái cây niềm này điều kiện trước này và các bước tiết và cái kỳ vọng kết quả kỳ vọng này và cái loại tiết được chưa thì bây giờ nhé em nhìn này bước đầu tiên mình cần làm gì là mình phải biết bạn đúng không bước đầu tiên vẽ bạn này
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luện tập Q7 - Google Doc  +
< > G  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A, § 100% -  Normal text  Arial  1 - 11  +  BIUAD  E  Editing
7... le
governed by a role-based access control (RBAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time  1 of 23
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 7: Testing Stage and Type (1.5 points)
1. Map the four standard testing stages to the CRS development process. For each stage,
state what is tested, who is responsible, and which testing types are most applicable:
(0.5 points)
2. Write THREE test cases for the 'Register for Course' use case, covering the scenarios
listed below. Present each test case in a table with the columns: Test Case ID | Test
Case Name | Precondition | Test Steps | Expected Result | Testing Type. (1.0 points)
• Happy-path scenario — a student successfully registers for an available course
Boundary / edge-case scenario - a student registers for the last avallable seat
(quota = 1 remaining)
Ste  ^  ENG  11:04 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5] Luyện tập Q7 - Google Doc x  +  La l
< → C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  • CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
E  Share
File Edit View Insert Format Tools Extensions Help
as ca A S 100% - Normal tely =  Arial  | - 11] +  BI UA•  0 Editing
1....  2  4
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
UI/UX
Part 2:
• A  ^ EQ  11:05 PM
US  4/23/2026
```

## [27:00]
**Nói:** mình lại cái này không đây Ok thì đây nhá anh em bấm Insert này bây giờ mình sẽ mẽ đúng như cái này luôn 123456 và vẽ bàn thiết kênh 123456 và bán thiết kênh Ok thì bây giờ mình sẽ có gì đầu tiên mình copy luôn anh nhé đi
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  La
< → C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
• Tất cả dấu trang
Luyện tập Q7 # G® Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text -  Arial  | - 11] +  BIU A O  / Editing
Alpha/Beta Testing  ... I..
Acceptance Testing  Business  Student/ Staff
4 +  requirements and
UI/UX
Part 2:
• •  ^E O  11:05 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  • CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 6 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A • 100% - Normal text =  Arial  0 Editing
11
Il
Part 2:
• •  ^ EQ  ENG  11:05 PM
4/23/2026
```

## [27:30]
**Nói:** mình đã sẵn sàng cái này rồi chơi nhé đi thì nhận thấy sẵn cái này rồi à à à à à à à à à à à à à Ok đó xong bây giờ mình sẽ xử lý từng cái một đây cho mình sẽ hiện kết cây một
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Docs  1 +  La
- >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP  I CO
88  • Tất cả dấu trang
+
SWE202c_Practical_Exam_Sample.docx.pdf  • Open with Google Docs  :  * Share
My D  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
Home  • Integration Testing
My Lowel  System Testing
• User Acceptance Testing (UAT)
LD Comouters
Write THREE test cases for the 'Register for Course' use case, covering the scenarios listed below.  f
Present each test case in a table with the columns as below: (10 points)
Shared with mo
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario - a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Test Case Name  Precondition  Test steps  Expected result Test type
Stand
TCI
• Trash
TC2
Storage
Gel more storage
III. SCORING RUBRIC
Q#  Торіс  Max Score  Weight  Grader's
Score
Software Development Model Selection  2.0  20%
UC Modeling  Page  -  Q  I+  15%
3  UC Specification  15%
^  ENG  Ф)  11:05 PM
US  4/23/2026
```
**Màn hình:**
```
Ởi cốc cốc  SWE202 - Google Drive  Luện tập Q7- - Google Doc  +  La ..
docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  • I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
a-  Share
File Edit View Insert Format Tools Extensions Help
A, § 100% - Normal text =  Arial  U
2 B  6
Part 2:
TCID  Test Case  Precondition  Test steps  Expected
Name  result
m-
^ EQ  11:06 PM
```

## [28:00]
**Nói:** 23 Ok đó thì cái thằng kết cây đêm này thì nó là cái gì chắc chắn rồi đây đi nó cho sẵn anh được đúng không phải viết cho đúng 3 kịch bản này thì em chỉ cần việc copy và cho mình thôi anh em nhớ cho mình ra đi khi cố gắng làm mỗi câu câu nào cũng là một ít thì nghe sẽ được một điểm đấy câu nào cũng là một ít tấm tay mà anh em chỉ làm đúng một ít thôi em được điểm đó
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
• Tất cả dấu trang
Luyện tập Q7 * G S) Saving..  +
0 -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A 100% -  Normal text  Arial  | - [11 +  BI UA O  G H D  F•E E•E  E X
2 E  3 П 4 П  ... ?..
Part 2:
4+  TCID  Test Case  Precondition  Test steps  Expected  Test type
Name  result
203
• •  ^ E Q  ENG  11:06 PM
US
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luện tập Q7 - Google Doc  +  La l
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
A, § 100% - Normal text =  Arial  |- 11] +  BI U
4  5
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
Name  result
TC1  Happy-path
TC2  Boundary
TC3
• A  ^ EQ  11:06 PM
US  4/23/2026
```

## [28:30]
**Nói:** đi việc là anh em biết được một ít hay không anh em sẽ được quyết định là em được bao nhiêu liệu có bát hay không nó ok để mà làm tất cả cái này thì nó cũng không có đâu nhé anh em khi trên phía thì em được copy paste mà nó ok và đặc biệt anh em nào mà mua tài liệu mình chắc chắn đừng có quên anh em đang xem video này thì em đừng có quên là phải tải toàn bộ cái folder của sw202 này
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  • Luyện tập Q7 - Google Doc X  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
0 -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A, S 100% - Normal text -  Arial  | - 11 +  BIU  E  FE E•E  E X
11  4  6  Lee lee
Part 2:
TCID  Precondition  Test steps  Expected  Test type
Tost Case  result
TC1  Happy-path
TC2  Boundary
TC3  Negative
• a  ^ EQ  ENG  11:06 PM
US
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Dock x  +
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A • 100% - Normal text ~  Arial  - 11 +
1..
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path
TC2  Boundary
TC3  Negative
• •  ^ EQ  11:07 PM
US
```

## [29:00]
**Nói:** là ok thì sau khi mình biết ba đây rồi đúng không thì bây giờ mình sẽ làm gì Bây giờ mình sẽ cần phải thực hiện thứ nhất đó là cái cái điều kiện này đúng không như là cái điều kiện trước đó thì mình sẽ làm gì thì là cái điều kiện như mình vừa nói rồi khi mà kịch bản này sẽ ra tuyệt
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  Ca
< >  drive.google.com/drive/u/0/folders/16ZsDgSYH6tqRzhDEM8kkD-KQ8cFJvOSP
88  • Tất cả dấu trang
+
X  SWE202c_Practical_Exam_Sample.docx.pdf  • Open with Google Docs  +  :  * Share
My Dr  1. Map the four standard testing stages to the CRS development process. For cach stage, state what is
tested, who is responsible, and which testing types are most applicable: (5 points)
• Unit Testing
• Integration Testing
My Blue  System Testing
• User Acceptance Testing (UAT)|
•LD Computers
2. Write THREE test cases for the Register for Course' use case, covering the scenarios listed below:
Present each test case in a table with the columns as below: (10 points)
Brared with me
• Happy-path scenario — a student successfully registers for an available course
Recent  Boundary / edge-case scenario - a student registers for the last available seat (quota = 1 remaining)
• Negative / error scenario — a student attempts to register without meeting the course prerequisite
Stamuel
TCID  Test Case Name  Precondition  Test steps  Expected result  Test type
Stam
TCI
# Trash
TC2
Storage
Lel mone storage
III. SCORING RUBRIC
Q#  Topic  Max Score  Weight  Grader's
Score
Software Development Model Selection  20  20%
UC Modeling  Page  4  -  Q  I+  15%
3  UC Specification  15%
E  ENG  11:07 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A & 100% - Normal text ~  Arial  - 11] +  U
6  .!..
Part 2:
TCID  est Case  Precondition  Test steps  Expected  Test type
Vame  result
TC1  Happy-path
TC2  Boundary
TC3  Negative
• •  ^ EQ  ENG  11:07 PM
US
```

## [29:30]
**Nói:** nhất nghĩa là việc bạn này lý tưởng nhất thì nó sẽ bao gồm lắm học sinh đăng ký đã đăng ký thành công đăng học sinh đã đăng ký thành công đấy nhạc tiếp theo là gì tiếp theo là gì tiếp theo tiếp theo là khóa học này có học này có sẵn được chưa có sẵn và nó còn chỗ được chưa nó khóa học có sẵn còn chỗ
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A & 100% - Normal text ~  Arial  - 11] +  I U
1..
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
Vame  result
TC1  Happy-path
TC2  Boundary
TC3  Negative
• a  ^ EQ  ENG  11:07 PM
US  04 423/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  - | 11  +  U  # = - EE E
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  student
logged in;
Course avai
TC2  Boundary
TC3  Negative
• •  ^ EQ  ENG  11:08 PM
US  4/23/2026
```

## [30:00]
**Nói:** tiếp theo tiếp theo là gì là nó sẽ chết đúng không Nó sẽ chết điều kiện điều kiện cũng được đáp ứng được chưa điều kiện ở nhiều kiếp liên quyết cũng được đáp ứng ở trên nhau đó vì cô ta thì quay nó cũng được đáp ứng được chưa đó mà đấy là cái điều kiện này cho đấy là cái điều kiện đầu tiên là điều
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  & A S 100% - Normal text ~  Arial  | - 11  +  BI U
Part 2: (
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  stadent
logged in;
Course
available
TC2  Boundary
TC3  Negative
^ EQ  ENG  11:08 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  • Luyện tập Q7 - Google Doc X  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G@ Saved to Drive  +
0 -  Share
File Edit View Insert Format Tools Extensions Help
asc8 A 100% -  Normal text  Arial  I - (11  +  BIU  #E F - E • E E  E X
1 1
Part 2: (
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  stadent
logged in;
Course
available;
Prerequisites
met
TC2  Boundary
TC3  Negative
^ E Q  ENG  11:08 PM
US  4/23/2026
```

## [30:30]
**Nói:** mọi thứ nó đều lý tưởng nhé thì các bước tiết thì sao các bước tiết thì nào, chắc chắn rồi bước đầu tiên bước đầu tiên là gì là thằng học sinh này nó phải duyệt xem qua nó phải xem qua hết xem qua hết cái danh mục các cái môn mà có sẵn
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
=  0 -  Share
File Edit View Insert Format Tools Extensions Help
Q5 e  8 A S 100% - Normal text ~  Arial  I - (11  I U  #=- E•E-E
1 1
Part 2: (
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student
logged in;
Course
available;
Prerequisites
met
TC2  Boundary
TC3  Negative
• •  ^ E Q  ENG  11:08 PM
US
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 6) Saving..  +
0 -  Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100%<  Normal text "  Arial  I - (11  I U  #E F - E E E  E X
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student  1, Bwol
logged in;
Course
available;
Prerequisites
met
TC2  Boundary
TC3  Negative
• •  ^ E Q  ENG  11:09 PM
US  4/23/2026
```

## [31:00]
**Nói:** đúng không anh em nó phải xem qua hết nó là duyệt danh sách các khóa học cái này nó có sẵn trong mấy rồi anh em nhé ok bước đầu tiên là nó phải duyệt qua đúng không anh em bước tiếp theo là gì 2
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
0 -  Share
File Edit View Insert Format Tools Extensions Help
a sca A S100%<  Normal text "  Arial  I - (11  I U  #E F - E E E  E X
1 1  2 :
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student  1, Browse
logged in;  catalogue|
Course
available;
Prerequisites
met
TC2  Boundary
TC3  Negative
• •  ^ E 0  ENG  11:09 PM
US
```
**Màn hình:**
```
Ở cỐc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G6 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  8 A 8 100% Normal text "  Arial  - 11  I  # = - EE E
Part 2:
= +
TCID  Test Case  Precondition  Test steps  Expected  Test type
Name  result
TC1  Happy-path  Student logged in; I  1, Browse
Course available;  catalogue|
Prerequisites met
TC2  Boundary
TC3  Negative
• •  ^ EQ  ENG  11:09 PM
US  4/23/2026
```

## [31:30]
**Nói:** bước tiếp theo là nó phải trọn quá nó phải chọn khóa học Đấy chưa Và bước tiếp theo nữa Bước tiếp theo nữa là gì Chọn khóa học là như sao Click vào cái nút đăng ký Click vào cái nút Play OK Sau khi mà nó xem Chọn và đăng ký Đấy là các bước để nó hoạt động
**Màn hình:**
```
Ở cỐc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  - 11  +  I U  #E FEE E
...
Part 2:
TCID  Test Case  Precondition  Test steps  Expected  Test type
Name  result
TC1  Happy-path  Student logged in;  1, Browse
Course available;  catalogue  I
Prerequisites met
TC2  Boundary
TC3  Negative
• a  ^ EQ  ENG  11:09 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  La
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  _ CO
88  • Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
8A8100%  Normal text  Arial  - 11  BI U
ran z:
TOID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student logged in:  1, Browse
Course available  catalogue
Prerequisites met
2, Select course
3, Click "Register|
TC2  Boundary
TC3  Negative
• •  O He  ^ E  ENG  11:10 PM
US  4/23/2026
```

## [32:00]
**Nói:** Tiếp theo Nó sẽ chỉ cần là Đăng nhập vào Xem danh sách Và đủ điều kiện Được chưa Đó Nếu mà đủ điều kiện Kết quả kỳ vọng thì sao Kết quả kỳ vọng như thế nào Thì Nó sẽ hiển thị ra System Đúng không Đây là điều kiện lý tưởng nhất Đúng không Đây là tiết trong điều kiện lý tưởng nhất Thì Hệ thống nó phải hiển thị ra Đúng không Là Regis Nó có thể hiển thị ra là Regis Thành công
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +
docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  • I CD
88  • Tất cả dấu trang
Luện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11  BI U
ran 2:
=
TOID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student logged in:  1, Browse
Course available  catalogue
Prerequisites met
2, Select course
3, Click "Register"
TC2  Boundary
TC3  Negative
I a  • Her  ^ E Q  ENG  11:10 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc x
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
8 A 8 100% Normal text " …  Arial  | - | 11  BIU A
ran 2:
TOID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student logged in:  1, Browse  System
Course available:  catalogue  displays
Prerequisites met  "Res|
2, Select course
3, Click "Register"
TC2  Boundary
TC3  Negative
• •  • He  ^ E  ENG  11:10 PM
US  4/23/2026
```

## [32:30]
**Nói:** Ví dụ như là Regis Regis Chasing success Ừ thôi nó hoặc là nó và nữa và nó sẽ thế nào khi mà thêm đăng ký thành công rồi thì nói là nó nó sẽ
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×
docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  • I CD
• Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
8A 8100%  Normal text  Arial  - 11  BI UA
ran 2:
TOID  Test Case  Precondition  Test steps  Expected  Test type
result
TC1  Happy-path  Student logged in:  1, Browse  System
Course available  catalogue  displays
Prerequisites met  "Res
2, Select course
3, Click "Register"
TC2  Boundary
TC3  Negative
• •  ^ E Q  ENG  11:10 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc X  Ca
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
8 A 8 100% Normal text " …  Arial  1 - 11  BI UA
ran z:  -16  т..
TOID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in:  1, Browse  System displays
Course available:  catalogue  "Registration
Prerequisites met  success  I
2, Select course
3, Click "Register"
TC2  Boundary
TC3  Negative
• •  ^ E  ENG  11:11 PM
US  4/23/2026
```

## [33:00]
**Nói:** update raster trên nhau nó sẽ đáp đến raster để cho em nó sẽ update cái danh sách được chưa và cái kiểu này kiểu gì em nhận đây nó là cái kiểu là không chỉ có anh em nhớ cho mình nhá nó không chỉ có là mấy thằng này đâu phải chưa anh em có nhớ cho mình sau khi mà nó làm một loạt như này thì
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  Ca
docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
• Tất cả dấu trang
Luện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
80 100%  Normal text  Arial  | - 11  BI UA
ran z:  -16  т..
TOID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in:  1, Browse  System displays *
Course available  catalogue  "Registration
Prerequisites met  successful" arid
2, Select course
3, Click "Register"
TC2  Boundary
TC3  Negative
• •  ENG  11:11 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100%~  Normal text  Arial  - 11  BI U  "•E -E-
÷ 6
module, waitiist
=  triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing  3 of 23
complete system - all
functional features
and non - functional
Il  requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
UI/UX
• •  Site  ^  ENG  11:11 PM
US  4/23/2026
```

## [33:30]
**Nói:** nó là thằng xin lỗi nét tỉnh Ok ok ok ok tiếp theo này thì mình sẽ có cái gì nữa tiếp theo thì mình sẽ có là biên đúng không Cái biên này thì sao ví dụ như là như mình có nói rồi chưa em nó
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  Lal
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luện tập Q7 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A, § 100% -  Normal text  Arial  | - | 11] +  BIUA
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in:  1, Browse  System displays
Course available:  catalogue  *Registration
Prerequisites met  successful and
2, Select course  update roster
3, Click "Register"
TC2  Boundary
TC3  Negative
• •  • te  ^ E  ENG  11:11 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
• -  Share
File  Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  | - 11] +  BIU A
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional  -
Course available;  catalogue  "Registration  Testing|
Prerequisites met  successful and
2, Select course  update roster
3, Click "Register"
TC2  Boundary
TC3  Negative
• •  ^ E  ENG  11:11 PM
US  4/23/2026
```

## [34:00]
**Nói:** có các cái giá trị mà nhẹ cảm được chưa bằng 1 được chưa remaining được chưa tiếp theo thì mình sẽ có cái gì mình sẽ có là student đối với anh em nó thì anh em con nó hai điều kiện này nó thì nghĩa là sao một chỉ tiêu khoa học chỉ còn đúng một chú cháu hay là sinh viên đáp ứng đủ điều kiện kiên quyết nó thì làm chỉ
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  La'
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  | - 11] +
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available;  catalogue  *Registration  Testing
Prerequisites met  successful and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Caurse quota = 1]
TC3  Negative
• •  ^ E  ENG  11:12 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luện tập Q7 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  | - 11] +
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available;  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1
remaining: Student
meets prerequities
TC3  Negative
• •  ^ E  ENG  11:12 PM
US  4/23/2026
```

## [34:30]
**Nói:** tiêu thì chỉ còn một thôi đúng không đó chỉ tiêu thì chỉ còn một thôi mình sẽ ghép những cái giá trị biên mà mình sẽ tiếp các cái giá trị biên được chưa thì đây mình sẽ các bước thực hiện như thế nào mình sẽ có là chắc chắn rồi đầu tiên phải chọn khoa học có spence xì x
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
• -  Share
File  Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text ~  Arial  | - 11] +  BIU A
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available;  catalogue  *Registration  Testing
Prerequisites met  successful and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course  prerequisites
remain
meets prerequities®
TC3  Negative
E  ENG  11:12 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La'
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A § 100% - Normal text ~  Arial  | - 11] +  BIU  A  #E F - E • E E
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available;  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Seleft course si
remainina: Student
meets prerequisites
TC3  Negative
^ E  ENG  11:13 PM
US  4/23/2026
```

## [35:00]
**Nói:** sau đó thì sao sau khi chọn vào click đăng ký đó như này thì sao cái kết quả mình muốn mong nó sẽ làm System Register Student và hãy nào cái thách sản rồi, cái này bằng 1
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La'
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A § 100% - Normal text ~  Arial  | - 11] +  BIU  A  #E F • E • EE
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available;  catalogue  "Registration  Testing
Prerequisites met  successful and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course
remaining; Student  specific)
meets prerequisites
TC3  Negative
^ E  ENG  11:13 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc X  +  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ~  Arial  | - 11  +  "•E•E-E  E X
-1 6  1..
Part 2:
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers*
remaining; Student  specitic  student|
meets prerequisites
2, Click "Register"
TC3  Negative
• •  ^ E  ENG  11:13 PM
US  4/23/2026
```

## [35:30]
**Nói:** đúng không? cái này chỉ tiêu là còn 1 thôi thì sau khi thằng này, hệ thống này cho thằng học sinh đăng ký rồi thì nó sẽ thế nào? nó sẽ cho là thằng học sinh này chỉ tiêu lúc này sẽ chỉ còn là bằng 0 được chưa, đúng không thằng này đang là 1 sau khi mà thằng này đăng ký thành công thì có phải lấy thống cho thằng học sinh này đăng ký được chưa, sau đó thì cái chỉ tiêu chỉ còn là 1 đúng không, đó và cái thằng học sinh tiếp theo
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc X  +  La
< →  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
E  Share
File Edit View Insert Format Tools Extensions Help
Q 5  8 A S 100% - Normal text ~  Arial  - [ 11 ] +  F•E E-E  E X
-1 6  1..
Part 2:  •
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers*
remaining; Student  specific  student: Quota =
meets prerequisites  A
2, Click "Register"
TC3  Negative
• •  ^ E Q  ENG  11:14 PM
US  04 4232026
```

## [36:00]
**Nói:** next user được chưa, sẽ như thế nào nó sẽ bứt nó vào playlist được chưa, bứt nó vào playlist trên em đúng không Khi mà hết chỉ tiêu thì cái thằng còn lại chẳng có bước nó mà quên ít thì còn là gì đó đúng không thì đây nó sẽ là kiểm thử bằng 3 đôi đi được chưa đó cho mình nhá Nó là bà Rory Văn được chưa tiếp theo nữa này tiếp theo cuối cùng đúng không cái
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc X  +  La
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ×  Arial  - [ 11 ] +  "•E•E-E  E X
+7 6  1..
Part 2:  •
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers -
remaining; Student  specitic  student: Quota =
meets prerequisites  O ; next use]
2, Click "Register"
TC3  Negative
• •  ^ E  ENG  11:14 PM
US  -4 4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc x  +  La'
< > G  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ×  Arial  - [ 11 ] +  "HEE-  E
2
Part 2:
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
...
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundaryl
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees 'Waitlist'
4  TC3  Negative
• •  ^ E  ENG  11:14 PM
US  4/23/2026
```

## [36:30]
**Nói:** cuối cùng thì mình sẽ có cái gì cái cây cuối cùng này là cái trường hợp mà cố tình cho lỗi được chưa thì mình sẽ cho nắng tiêu đừng không hoàn thành không hoàn thành requirement ari quay mấy có nghĩa là không hoàn thành không đủ điều kiện được chưa không đáp ứng điều kiện thì thôi
**Màn hình:**
```
cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
• Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
Share
File  Edit View Insert Format Tools Extensions Help
Q  Normal text  Arial  11  BI UA
4  1...
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees 'Waitlist'
4  TC3  Negative
• •  ^ E  ENG  11:14 PM
-  US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q  Normal text -  Arial  BI UA
4  5  7
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
...-
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  *Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
...
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees Waitlist'
TC3  Negative  Student has no!
completed rel
• •  G  ^ E  ENG  11:15 PM
-  US  4/23/2026
```

## [37:00]
**Nói:** phải chưa nghĩa là mình sẽ cho nó là không đáp ứng điều kiện thì bây giờ mình sẽ cho nó là là gì là mình sẽ phải select khóa học xe lệch box chờ hai lá mình có mít chọn khoa học rồi đăng ký chưa thì đây mình sẽ có gì system nó sẽ thế nào khi mà có lỗi xảy ra nó thì nói là chạy này nó phải
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q  Normal text  Arial  +  BI UA
4  7
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
...
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees 'Waitlist'
TC3  Negative  Student has no!
completed required
Dase coul
I a  ^ E  ENG  11:15 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65. Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
Normal text  Arial  -  11  +  BIU
2  4  7
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type  •
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
...
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0; next user
2, Click "Register"  sees Waitlist
TC3  Negative  Student has not  1, Select course
completed required  I
base course  2, Click "Register"
• •  E  ENG  11:15 PM
US  4/23/2026
```

## [37:30]
**Nói:** nó ra registration có thằng này không đủ điều kiện thì làm sao đăng ký được thì chặt nó chưa sau đó thì hiển thị ra lỗi lấy lâu rồi chưa lấy lâu là gì là là cái này mình có thể là ở đây
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Normal text -  Arial  +  BI UA
2  4  +1 6  1..
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type  •
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
...
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0; next user
2, Click "Register"  sees Waitlist'
TC3  Negative  Student has not  1, Select course  System
completed required  I
base course  2, Click "Register"
• •  E  ENG  11:15 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
Q  Normal text  Arial  -  11  +  BI UA
2  4  +1] 6  7
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type  •
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
...
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees 'Waitlist'
TC3  Negative  Student has not  1, Select course  System blocks
completed required  registration;
base course  2, Click "Register"  Display error:"
E  ENG  11:16 PM
US  4/23/2026
```

## [38:00]
**Nói:** nhưng mà lúc này nó sẽ là nó bị trên nhau như là không đủ điều kiện để trên nhau đó mà cái kiểm thử này nó sẽ là negative testing anh em chỉ làm đơn giản này thôi là anh em đi thi vụ cho mình đấy nhỉ anh em chỉ làm
**Màn hình:**
```
cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
• Tất cả dấu trang
Luện tập Q7 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q  Normal text  Arial  11  +  BIU A
4  7
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available;  catalogue  *Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
...
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees 'Waitlist'
TC3  Negative  Student has not  1, Select course  System blocks
completed required  registration;
base course  2, Click "Register"  Display error: PI
• •  G  ^ EQ  ENG  11:16 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  La  ...
→  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # GO Saved to Drive  +
Share
File  Edit View Insert Format Tools Extensions Help
8100%  Normal text  Arial  11  +  BIUA
2  4
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0; next user
2, Click "Register"  sees Waitlist
TC3  Negative  Student has not  1, Select course  System blocks  Negative Testing
completed required  registration;
base course  2, Click "Register"  Display
error: "Prerequisit
es not met*
• •  ^ E  ENG  11:16 PM
-  US  4/23/2026
```

## [38:30]
**Nói:** lắm gọi này thôi Thế chứ nếu bạn trên này nhớ điểm kỹ hơn đấy như mình và lấy mình biết thêm đấy thì em phải viết thêm mà kính em sẽ được điểm cao đấy nhỉ đó em cứ vứt hết vào cho mình nhé à à ở trên này thì mình nghĩ là biết hết vào đi cho nó cho được nhiều cái này nhá lại bao lý value trên này luôn nó chưa nó kiểm tra từ
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X
< >  @ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q s c#A §100%<  Normal text  Arial  - 11  +  BI UA  #*-E-E-E  :
Cách làm
=
Part 1:
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual components  Developers  White-box Testing
/ module in isolation -
e.g, login validation
logic, check condition,
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
^ E  ENG  11:16 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  • SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  La
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luện tập Q7 # G 65 Saving...  +
•  Share
File  Edit View Insert Format Tools Extensions Help
Q s  8A 8100%  Normal text  Arial  -  11  +  BI U  1E
4
Testing Stage  What is tested  Who  Testing type
Unit Testing  Individual components  Developers  White-box Testing
/ module in isolation -  Functional Testing
e.g, login validation  Boundary valuel  I
logic, check condition,
quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - eg
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non- functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
UI/UX
• a  ^ E  ENG  11:17 PM
US  4/23/2026
```

## [39:00]
**Nói:** mô đun mà tiếp theo mình sẽ có là cái dưới này cho anh em thêm cho mình là API testing em biết được cái này thì em sẽ được điểm cao đấy nhạc đó ok và tiếp theo nhé cái chỗ này này, anh em nhìn thấy mình để cái chỗ này không đó, thì chỗ này nhé anh em cố gắng viết cho mình thấy được thì là ngon ví dụ ở đây nhé, performance testing
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  La
docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luện tập Q7 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  8A 8100%  Normal text  Arial  | - 11] +  BI UA
1  2  3  4  6
=
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course available:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0; next user
2, Click "Register"  sees 'Waitlist'
TC3  Negative  Student has not  1, Select course  System blocks  Negative Testing
completed required  registration;
base course  2, Click "Register"  Display
error: "Prerequisit
es not met"
^ E  ENG  11:17 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cỐc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  La'
< >  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luện tập Q7 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  8 10%  Normal text  Arial  | - 11  +  I  U  A  tE  E
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all
functional features
and non - functional
requirements
(Performance,
sécurity...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing  A
requirements and
Ul/UX
@
• •  ^ E 0  ENG  11:17 PM
US  4/23/2026
```

## [39:30]
**Nói:** được chưa, cái này nhé nó rất là giống câu 4, được chưa anh em ví dụ như cái này, thì anh em ví dụ anh em viết là performance được chưa, hay là anh em viết là security security và khi anh em biết security testing nếu mà anh em mà đẳng cấp thì anh em chọn cho mình được chưa em chọn cho mình một ví dụ là anh em cực kỳ đẳng cấp là anh em sẽ ăn được điểm cao này
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luện tập Q7 - Google Doc ×  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  & A S 100% - Normal text ×  Arial  11  +  I  U  A  tE  E
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all  Performance Testing
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
UI/UX
• •  ^ EQ  ENG  11:17 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  +  Ca
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  Normal text  Arial  11  +  I  U  A  tE
..1..
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all  Performance Testing
functional features
and non - functional
requirements
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
Ul/UX
• •  ^ EQ  ENG  11:17 PM
US  4/23/2026
```

## [40:00]
**Nói:** cho mình cái này chưa đó thì tức là sao nếu mà kiểm tra bảo mật thì mình sẽ dùng cái gì mình sẽ sử dụng cái này đúng không thì em kiểu anh em biết thì ví dụ vào đấy thì làm nó sẽ được hiệu cao đó đó Ok chưa đấy Nói chung là linh hoạt anh em nhé có này thì cứ để này thôi đấy nha đó đó là cách
**Màn hình:**
```
Ớ côi cc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +  La
< > C® docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  I CD
• Tất cả dấu trang
Luyện tập Q7 # G 65 Saving...  +
• -  Share
File Edit View Insert Format Tools Extensions Help
asca A S 100% -  Normal text -  Arial  | - [11] +  BI UA O  #GE E E
1 m  2  4  6  V..!.
2 of 23
• Negative / error scenario — a student attempts to register without meeting the  vegast ve eror scenario
^ E Q  11:18 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  SWE202 - Google Drive  Luyện tập Q7 - Google Doc ×  La
< →  docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm/dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q7 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q s  8100%  Normal text  Arial  -  11  +  I U  1E
loğic, čheck condition,
=  quota calculation
Integration Testing  Interaction between  Developers + Tester  Gray-box Testing
module - e.g  API Testing
enrollment module
connecting to grade
module, waitlist
triggering notification
service
System Testing  The entire CRS as a  QA/ Testing team  Black-box Testing
complete system - all  Performance Testing
functional features  Security Testing
and non - functional  (encrypted using TLS
requirements  1.2 or higher)  Il
(Performance,
security...)
Acceptance Testing  Business  Student/ Staff  Alpha/Beta Testing
requirements and
∞o-
• •  ^ E  ENG  11:18 PM
-  US  4/23/2026
```

## [40:30]
**Nói:** để mình làm câu bạch trên em thì anh em cố gắng đi thì nhớ ví dụ cái này em copy được rồi này copy này đi khi bắt một copy bắt hai copy nốt để anh em chỉ chỉnh sửa cái phần này thôi đấy thì trên nhau chỉnh sửa bài này còn đi kia có biết chưa đó nhớ cho mình nhé Ok vậy thì đi sau này mình Đó là toàn bộ 7 câu Mình hướng dẫn anh em
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5 Luyện tập Q7 - Google Doc X  +
+ → C ® docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0
88  • Tất cả dấu trang
LuYện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100%~  Normal text  Arial  | - 11] +  BIU  *-E-EE
6  V...!.
Part 2:
TCID  rest Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
Course avallable:  catalogue  "Registration  Testing
Prerequisites met  successful" and
2, Select course  update roster
3, Click "Register"
TC2  Boundary  Course quota = 1  1, Select course  System registers  Boundary value
remaining; Student  specific  student; Quota =
meets prerequisites  0 ; next user
2, Click "Register"  sees "Waitlist
TC3  Negative  Student has not  1, Select course  System blocks  Negative Testing
G  ^ E  ENG  11:18 PM
US  4/23/2026
```
**Màn hình:**
```
Ở cốc cốc  & SWE202 - Google Drive  5] Luyện tập Q7 - Google Doc x  +  Lal
< → C@ docs.google.com/document/d/18igTkGmh7rRhjpHNXgUaE6ZAP5mm7dsfyCqmM3U5644/edit?tab=t.0  •CD
• Tất cả dấu trang
Luện tập Q7 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11 +  Editing
.u....  4  5  6
Il
Part 2:
TCID  Test Case  Precondition  Test steps  Expected result  Test type
Name
TC1  Happy-path  Student logged in;  1, Browse  System displays  Functional
G  ^ E Q  ENG  11:19 PM
-  US  4/23/2026
```
