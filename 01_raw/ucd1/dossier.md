# DOSSIER — ucd1

- file gốc: `YTSave_YouTube_Luyen-Use-case-diagram-1_Media_0zr0WJhgp_o_002_720p.mp4`
- thời lượng: 60.7 phút
- nguồn: transcript tự động (Whisper) + OCR màn hình (Apple Vision), đều chạy offline

> **Độ tin cậy — đọc trước khi dùng:**
> `Nói:` là giọng giảng viên do máy nhận dạng, có thể sai thuật ngữ tiếng Anh.
> `Màn hình:` là chữ OCR từ khung hình, có thể sai vài ký tự nhưng bố cục đúng.
> Khi hai nguồn lệch nhau: **tin `Màn hình` cho tên class / thuộc tính / bảng / code**,
> **tin `Nói` cho lời giải thích và quy trình**. Timestamp là của video gốc.

---

## [00:00]
**Nói:** Hello anh em nhé, trong video này mình sẽ hướng dẫn anh em luyện tập câu 2 anh em nhé. Câu 2 này mình cứ đúng form anh em nhé, trước mắt mình sẽ hướng dẫn anh em luyện tập từng câu, sau đó anh em sẽ quay đến đây này, các cái đề hôn tập này nhé. Đây là đề hoàn toàn khác so với các cái so với đề trial, nhưng mà cái form của nó vẫn chỉ có vậy thôi, cho nên anh em chịu khó luyện tập nhé. Ok Thì mình đã để đủ đầy đủ hết cho anh em rồi Nói chung là câu 2 này mình sẽ không đưa lên web Bởi vì là nó có phần vẽ Thì anh em phải chủ động vẽ nhá Nói chung là có rất là nhiều phần mềm để cho anh em viện vẽ nhá
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
• Tất cả dấu trang
Luyện tập Q2  +
• Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% -  Normal text -  Arial  0 Editing
3
Đề trial
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
From a technical standpoint, the university imposes several constraints.  The system must
^ G  ENG  1:56 PM
US  4/18/2026
```
**Màn hình:**
```
Ới cốc cốc  Luện tập Q2 - Google Doc x  +  Ca  ...
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools  Extensions Help
9508A 100% -  Normal text  Arial  - | 11  +  U  Editing
(administrators) are responsible for defining the semester timetable, setting and publishing
course quotas, opening and closing the registration window, approving exceptional cases, and
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
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
points)
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
^ G  ENG  1:56 PM
US  4/18/2026
```

## [00:30]
**Nói:** Đó Ok Thì anh em thích dùng thế nào thì anh em tải về vẽ thôi Ok Đó Thì câu 2 này trước khi vào câu 2 thì mình sẽ dẫn anh em một chút Ờ ok Thì bây giờ Ừ mình sẽ dẫn anh em một chút lý thuyết nữa nhá Ok thì nếu mà anh em mà học lý thuyết đấy nếu anh em học lý thuyết chính thì nó khá là dài nghe mặt cho nên là nếu mà anh em đọc không có
**Màn hình:**
```
côc côC  Luyện tập Q2 - Google Doc  +  La
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
Tất cả dầu trang
Downloads
Luyện tập Q2  +
File Edit  View  Inser  →  Downloads  Search Downloads  Q
Q  +  New -  TL Sort -  • View ~  •I Preview
Home  v Today
A Gallery
Desktop  Gemini_Gene  Gemini_Gene  Không được  test2.mdj  testuc.mdj  draw-io-29.3.  StarUML  SWE202-202
rated_Image  rated_Image  xác nhân  6-installer.ex  Setup  60418T01510
Downloads  jurumgiuru  _(24irrc24irrc  894421.crdo  7.1.0 exe  62-3-001.zip
mgiuru.png  24i.png  wnload
Documents
Pictures
• Videos  Select a file to preview.
SWE202c_Pra  LO7 Exercise-  LO7 Exetcise-  LO7Requirem
ocr-project  ctical_Exam_  Requirement  MovieShopD  ents.pdf
Sample.docx.  sDomainMo  MWorksheet.
Music  pdf  deling.pdf  pdf
v Yesterday
- lưu vd
NWC
SWE202 trial
Project PRF193  Project
PRF193
v Earlier this week
423 items |
ENG  1:56 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  5 Luyện tập Q2 - Google Doca  +  La  ...
+ > G@ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  ICO
• Tất cả dấu trang
Luyện tập Q2  +
• -  Share
File Edit View Insert Format Tools Extensions Help
asca A S 100% ~  Normal text -  Arial  - 1  +  I U A  *-E •EE  E X  Editing
huL.  7  7... 1.
scaling so that additional server capacity can be added smoothly as student numbers grow in
=  future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary of secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actor(s) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
• At least ONE <<include>> relationship - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
• Any actor-generalisation relationships that apply
Site  ^ G V 0  ENG  1:56 PM
US  4/18/2026
```

## [01:00]
**Nói:** xe thì nó rất là dài cho nên mình sẽ dẫn anh em trọng tâm nhất thì ở trong bài này nhá anh em chỉ cần nắm cho mình thôi đó là bài này chắc chắn có vĩ đúng không thì những cái kiến thức cốt lõi đầu là anh em phải biết x tờ là gì để em vẽ được yêu yêu cây đeo Ram được chưa Bài này thì là dùng là vĩ cây diagram thì anh thì anh em chỉ cần nhớ cho mình thôi và cái quan trọng đó là một lãi tử hay nó còn gọi tắt nhân anh em nhé thì cái cái này nhá nó sẽ khoan trước khi nói cái này thì mình sẽ
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
H I  Untitled • 2/2 • Fit (123%)  • •
ste  1:57 PM
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  •
Actor
1:57 PM
```

## [01:30]
**Nói:** cái này là gì Cái này là một mô hình anh em nhé Cái là một mô hình và mô hình này giúp anh em gì nó sẽ giúp anh em nắm bắt hành vi của cái hệ thống dưới góc nhìn của người dùng như là sao ví dụ anh em nhé ví dụ anh em cứ hiểu nó là một góc nhìn người dùng bây giờ ví dụ nhé anh em chờ
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Poi  Untitled • 2/2 • Fit (123%)
Actor
^ G V $  ENG -Ф)E 4/18/2026  1:57 PM
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  •
Actor
ENG - 4)E 4/18/2026  1:57 PM
```

## [02:00]
**Nói:** đây ví dụ đây ví dụ anh em đang là một người dùng đúng không anh em nhìn vào đây thì em thể nhìn thấy cái gì đây em nhìn thấy việc là đăng nhập đúng không đó anh em hãy nhìn thấy đăng nhập nó không ví dụ mình đang nhập bạn thì đây là giao diện của user đúng không thì anh em có phải là người dùng anh em đang nhìn thấy giao diện user thì cái kia kêu ra này anh em thì cái kia ra mẹ thì nó chính là là gì nhận nó chính là cái góc nhìn của người dùng trên em nó chính là góc nhìn của người dùng luôn
**Màn hình:**
```
Untitled - 2/2 - Scrble Lite
Untitled • 2/2 • Fit (123%)
Actor
1:58 PM
```
**Màn hình:**
```
TQMaster - Nên tảng luyện th  x  +
A  tuanvaquantop1.onrender.com/dashboard  *
88  * Bookmarks  Facebook  • youtube  M Hộp thư đến (812) -...  & Drive của tôi - Goo...  5 FPT University Acad...  ChatGPT|  FPT University Learn...  FuOverflow Commu...  HireLogic  Tất cà dấu trang
Trang  Môn  Lý  Đơn  Liên  Cao Thanh
TQMaster  Q Tìm kiếm môn học...  88  chủ  học  thuyết  hàng  hệ  Tuấn  (→> Đăng xuất
Student
L Xem môn học  • Hoàn thành mục tiêu bọc tập
8 bài  9 môn
Bài đã làm  Đã chỉ tiêu  Môn đang học
Hướng dẫn cách học hiệu quả
Xem video để tìm hiểu cách tối ưu hóa quá trình học tập của bạn
WEB HỌC TẬP TUẤN & QUÂN UPDATE 90% - THÊM VIDEO HƯỚNG DẪN DÙNG + CÁCH HỌC ĐIỂM CAO || Tuấn và Quân
Tuăn và Quân FPT UNIVERSITY
CŨC KHUNG
UPDATE
IRO r C &  ENG  (D))  1:58 PM
US  4/18/2026
```

## [02:30]
**Nói:** đó Ok thì bây giờ ví dụ user nó nhìn như vậy hay cái hay là cái cái này à à Ừ ok em chờ mình chút đây mình sẽ mở cho anh em xem Ok thì ví dụ đây anh em thì ví dụ đây là góc nhìn của vẫn là góc nhìn người dùng nhưng mà
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2 / 2 • Fit (123%)|  •
Actor
ENG -Ф)E 4/18/2026  1:58 PM
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  S& g
Actor
zaid  ENG -Ф)E 4/18/2026  1:58 PM
```

## [03:00]
**Nói:** đây với vai trò khác với một cái râu mới đó là với cái râu là admin để xin thì nó sẽ như này đó Ok thì đấy là cái góc nhìn đúng không Đấy là góc nhìn nó sẽ khác nhau đó mày thì ký kêu cây đen ra mày nó sẽ giúp anh em tôi nghe cái gì nhỉ nó sẽ giúp anh em là nó sẽ thể hiện được cho em
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  • O
Actor
ENG - 4)E 4/18/2026  1:59 PM
```
**Màn hình:**
```
=t.0  CD
88  • Tất cả dấu trang
Luyện tập G  +
• -  Share
File Edit View  Insert  Format  Tools Extensions  Help
Q  § 100%  Normal text -  Arial  +  B  U
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)  f
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
• At least ONE <<include>> relationship - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
• Any actor-generalisation relationships that apply
^  ENG  1:59 PM
US  4/18/2026
```

## [03:30]
**Nói:** nó sẽ thể hiện cái góc nhìn của người dùng được cho anh em đó Ok thì em hiểu sơ qua nó như vậy nhá đó hiểu đơn giản là như vậy tiếp theo này thì trong cái ký ký ký thì mình sẽ cần tìm hiểu thứ nhất là hát tờ hát tờ hay nó chính là tắt nhân anh em nhé thì cái tờ này đại diện được gì nó sẽ đại diện một thực thể nằm bên ngoài hệ thống hoặc là một người dùng trên nhau thì hát tờ nó là
**Màn hình:**
```
cốc cốc  +
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyM  =
88  u trang
Luyện tập Q2  +
Share
File Edit View Insert  Format Tools Extensions Help
Normal text  Arial  +  U  A  0. ^
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
points)
All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
• At least ONE <<include>> relationship — provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
• Any actor-generalisation relationships that apply
Site  ^ G V $  ENG  1:59 PM
4/18/2026
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  •
Actor
ENG - 4/18/2026  1:59 PM
```

## [04:00]
**Nói:** cái gì mình sẽ nói ví dụ cho anh em dễ hiểu nhớ mình sẽ nói nhiều lý thuyết ví dụ hát tờ nó có thể là con người ví dụ như là tiêu đình có thể là con người sử dụng hay là giảng viên được trên nhau Và ngoài ra trong actor thì nó sẽ chia ra là hai loại Thứ nhất là một cái actor chính Have primary Thì actor chính nó là gì? Thì anh em cứ nhớ cho mình Cái actor chính thì nó chính là những người như này này
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
poi  Untitled • 2/2 • Fit (123%)  • O
Actor
lite  ^ G V $  ENG -Ф) E4/18/2026  2:00 PM
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled 2/2 Fit (123%)  •
Actor  student 1  - •
2:00 PM
```

## [04:30]
**Nói:** Student hay là giảng viên Còn ví dụ cái tiếp theo là cái actor phụ Cái actor phụ thì nó là cái gì? Hay nó còn gọi là secondary actor được cái xinh em nó thì cái thường nó sẽ thường là các hệ thống bên ngoài hoặc là cái gì dịch vụ mà hệ thống gọi đến từ trên em ví dụ như là cổ thanh toán ngay nhé anh ạ ạ cộng thanh toán Ok đó xinh
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)
-
Actor  studest 1:.
V  ENG  US  4/18/2026  2:00 PM
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
D  Untitled • 2/2 • Fit (123%)
Actor  student 1
AG V  ENG  US  4/18/2026  2:00 PM
```

## [05:00]
**Nói:** em thì em cứ nhớ cho mình đó là cái phụ thì ví dụ như là cổ thanh toán hay là cái máy chủ được là cái chủ gửi mail để cho nhau đó thì tí nữa vào bài chính thì mình sẽ nói cho anh em rõ hơn 12 cái này đó anh em cũng trước mắt anh em lắm cho mình cái này đã và khi em vẽ nhá nó sẽ là cái hình người quê anh em nhá nó đây nó chính là x tờ thì nó chính là cái hình người quê rồi cho nhá nó tiếp theo này em sẽ cần tìm hiểu thêm cho mình nó là về in kênh à quên mất cách từ anh em nhớ cho
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)
Actor  student 1
^ G  ENG  US  4/18/2026  2:01 PM
```
**Màn hình:**
```
Untitled - 2/2 - Scrble Lite
Untitled • 2 / 2 • Fit (123%)  •  S& g
2:01 PM
```

## [05:30]
**Nói:** khi đặt tên thì em phải nhớ cho mình đặt tên nó phải là danh từ anh em nhé Nếu anh em đặt sai thì cũng là mất điểm luôn được chưa anh em tiếp theo này đó là UK thì em cứ nhớ cho mình khi em đặt tên nhé thì nó sẽ là là động từ cộng danh từ được chưa anh em động từ cộng danh từ nhé và khi em vẽ thì nó sẽ là cái hình Ellipse như này được chưa anh em đó ok tí nữa vào bài thì anh em sẽ rõ hơn nhé đây đây để mình bỏ lên cho anh em xem luôn nhìn này nó dễ này đây em nhìn nhé đây hình người quê
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)
Heta  student 1
ENG  US  4/18/2026  2:01 PM
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2 / 2 • Fit (123%)  •
Use are  U+ly
ENG -Ф 4/18/2026  2:01 PM
```

## [06:00]
**Nói:** đây là hát từ trên nhá nó và đây ví dụ nó như này thì đây nó chính là nó chính là cái cái kênh trên nhá thì đây nó phải có là độc từ với danh từ sinh em nó thì UK nó là gì nó là một cái là cái quá trình cụ thể được chưa Nó là một cái mô tả một quá trình mà tương tác cụ thể giữa x
**Màn hình:**
```
LO7Requirements.pdf  +
© FileD:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw v  as Go Ask Copilot ~  - + @| 17  Q  • 2
ENG  2:02 PM
ite  US  4/18/2026
-
```
**Màn hình:**
```
LO7Requirements.pdf  +  X
FileD:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw v  abU Ask Copilot v  +  18  of 23  ED  Q
What is the
^  actor trying to
Student  Register For Courses  accomplish?
THE HONG KONG  DEPARTMENT OF
U UNIVERSITY OF SCIENCE  AND TECHNOLOGY  COMPUTER SCIENCE & ENGINEERING
WHAT IS A GOOD USE CASE?
A use case typically represents a major piece of
functionality that is complete from beginning to end
A use case must deliver something of value to an actor
Generally, it is better to have longer and more
extensive use cases than smaller ones.
ENG  2:02 PM
US  4/18/2026
```

## [06:30]
**Nói:** và hệ thống của sinh em nhớ cho mình nhé là cái quá trình mà tương tác cụ thể giữa x và hệ thống người sinh em đó Ok thì anh em chỉ cần nắm sơ qua như vậy thôi đã tí nữa mình sẽ nói rõ hơn cho anh em ngoài ra thì nó còn một vài cái nữa một vài kiến thức nữa nhưng mà mình nghĩ là mình sẽ để đến vào trong thì mình sẽ nói rõ hơn để xin em chứ nói ngoài này thì cũng không tác dụng lắm
**Màn hình:**
```
LO7Requirements.pdf  +
FileD:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw v  Un Ask Copilot v  +  17  of 23  Q
Add Course Offering  Browse Course Offering  Drop Course Offering
Are these good
use cases?
Select Course Offering  Change Course Offering
Student
What is the
-  actor trying to
Student  Register For Courses  accomplish?
THE HONG KONG  DEPARTMENT OF
LUT UNVERSITY OF SCIENCE  AND TECHNOLOGY  COMPUTER SCIENCE & ENGINEERING
WHAT IS A GOOD USE CASE?
A use case typically represents a major piece of
functionality that is complete from beginning to end.
A use case must deliver something of value to an actor.
ENG  Ф)  2:02 PM
US  4/18/2026
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)
V + 1y
Zaid  ^ GY  ENG -Ф E E4/18/2026  2:02 PM
```

## [07:00]
**Nói:** mình nghĩ là mình sẽ đi từng bước một khi mình giải cái này sau đó thì mình sẽ dẫn anh em chi nhé Ok thì ok đâu để đi xem à Ừ ok để mình xem là còn kiến thức gì đấy nhỉ Ok mình quên mất mình chưa nói cái quan trọng là khi em vẽ nhé nó sẽ có cái hình chữ nhật to bao ngoài từ trên nha em nhớ cho
**Màn hình:**
```
Ở cốc cốc  5 Luện tập Q2 - Google Doc X  +  Lal
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  =
• Tất cả dấu trang
Luện tập Q2 * G  +
E  Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  / Editing
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
• At least ONE <<include>> relationship - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
Any actor-generalisation relationships that apply
ste  ^ G VO  ENG  2:03 PM
US  4/18/2026
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  •
^ G V O  ENG - Q) 4/18/2026  2:04 PM
```

## [07:30]
**Nói:** cái này gọi là gì nó gọi là system Bowery nó là danh giới hệ thống của trang nhé em nhớ cho mình nhé đó cái này chúng ta thì lý thuyết một chút thôi để anh em đi thi nhé Bình em kể làm được thì đây nó chỉ là một cái hình chữ nhật bao khung bên ngoài được cho nhá đó và có một cái nước cực kỳ quan trọng mình quên mình chưa nói đó là cái phần quan hệ ở trên nhá quan hệ nhá Ok thì cái đầu tiên đó là cái à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Poi  Untitled • 2 / 2 • Fit (123%)  •
Land  ^ G V  ENG  2:04 PM
US  4/18/2026
```
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)
Qunhe
Eard  ite  ^ G V  ENG - ( E4/18/2026  2:04 PM
```

## [08:00]
**Nói:** anh em nhìn nhé
**Màn hình:**
```
Untitled - 2 / 2 - Scrble Lite
Untitled • 2/2 • Fit (123%)  •  S& G
Qunhe
1
Eard  ENG * 4/18/2026  2:05 PM
```
**Màn hình:**
```
LO7Requirements.pdf  +
© D:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw v  Un Ask Copilot v  +  17  of 23  Q
Add Course Offering  Browse Course Offering  Drop Course Offering
Are these good
use cases?
Select Course Offering  Change Course Offering
Student
What is the
actor trying to
Student  Register For Courses  accomplish?
DY UNINEASITY DIE SCIENCE  THE HONG KONG  DEPARTMENT OF
AND TECHNOLOGY  COMPUTER SCIENCE & ENGINEERING
WHAT IS A GOOD USE CASE?
A use case typically represents a major piece of
functionality that is complete from beginning to end.
A use case must deliver something of value to an actor.
ENG  2:05 PM
US  4/18/2026
```

## [08:30]
**Nói:** cái này mình sẽ xem cái nào cho anh em dễ nhìn anh em nhìn nhé nó là cái này anh em nhé anh em thấy không nó là cái này này nó không có mũi tên nếu mà anh em nhìn kỹ này tí nữa thì mình sẽ đến các cái dạng kia sau đó như này đấy anh em nhìn nhé
**Màn hình:**
```
LO7Requirements.pdf  +
FileD:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw v  an l  in Ask Copilot v  +@  17  of 23  Q  203
8000 g
functionality that is complete from beginning to end.
A use case must deliver something of value to an actor.
Add Course Offering  Browse Course Offering  Drop Course Offering
Are these good
use cases?
Select Course Offering  Change Course Offering
Student
What is the
actor trying to
Student  Register For Courses  accomplish?
THE HONG KONG  DEPARTMENT O
I AND TECHNO SCENCE  AND TECHNOLOGY  COMPUTER SCIENCE & ENGINEERING
WHAT IS A GOOD USE CASE?
^ G  ENG  2:05 PM
US  4/18/2026
```
**Màn hình:**
```
• LO7Requirements.pdf  +
© FileD:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw -  as i Ask Copilot v  +  20  of 23  ED  Q
ASU USE-CASE MODEL: USE-CASE DIAGRAM
Context diagram
Registrar
Maintain Course Information
Student  Select Courses To Teach
Register For Courses
Instructor
Billing System  Request Enrollment List
«communication» association (implicit)
^ G  ENG  2:05 PM
US  4/18/2026
```

## [09:00]
**Nói:** đấy ok thì đấy nó là cái cái đầu tiên để cho anh em là cái kết nối để cho anh em association ok tiếp theo thì mình sẽ có là cái include mấy cái này thì nói lý thuyết mình sợ anh em khó hiểu nhưng mà mình sẽ vẫn cứ mình sẽ nói qua một chút và mình sẽ cố làm cho anh em biết hiểu nhất nhá thì cái này là gì Cái này mình sẽ đi vào ví dụ nhé Mình không nói lý thuyết ví dụ nhé anh em có là đăng ký môn ví dụ anh em
**Màn hình:**
```
LO7Requirements.pdf  +  X
FileD:/wd%20c%20sang%20d/Downloads/L07Requirements.pdf  Sign in  Chat
Draw  A an Ask Copilot v  +  20  of 23  Q
Context diagram  Registrar
Maintain Course Information
f
Student  Select Courses To Teach
Register For Courses
Instructor
Billing System  Request Enrollment List
«communication» association (implicit)
THE HONG KONG  EPARTMENT O
UNIVERSITY OF SCIENCE  OMPUTER SCIENCE & ENGINEERINO
ACH MOST
ASU USE-CASE MODEL:
^ G  ENG  2:06 PM
US  4/18/2026
```
**Màn hình:**
```
Untitled - 3 / 2 - Scrble Lite
Untitled • 3/2 • Fit (123%)
Jun he'
1, Associatim.
Artar - uce -cas
- include
ENG - ) 4/18/2026  2:06 PM
```

## [09:30]
**Nói:** có là ví dụ bây giờ là trong một hệ thống khóa học đúng không Bây giờ ví dụ anh em đăng ký môn học thì anh sẽ luôn cần gì đó là anh em sẽ luôn cần phải đăng nhập trên em đó nó sẽ luôn cần thì hay anh em hiểu đơn giản như sau đó là yêu yêu cây A thì luôn gọi cái thằng kia cây bê
**Màn hình:**
```
Untitled - 3 / 2 - Scrble Lite
Untitled • 3/2 • Fit (123%)
Wun he'
(Kraí)
1, Associatim.
Actar - uce -cas
include
ENG - 4)E 4/18/2026  2:06 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)
1,  Associatin.  1 Kadi 1.
Artar - uce -cas
include
Đăng Ký môn học.  →)  Rang They.
luse
AGV  US  4/18/2026  2:06 PM
```

## [10:00]
**Nói:** xinh em yêu kia này xin luôn gọi thằng kia bê đó thì đây nó sẽ dùng lá include và khi em đưa vào nhá thì nó sẽ biết khi em đưa vào ấy Vậy thì nó sẽ là như này nó có hai cái dấu hoặc hai cái dấu như thế này như này đó được chưa nha Đó là vì cái quan hệ thứ hai nhá tiếp theo này quan hệ thứ ba
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)
Associatin.
Artar - uce -cas
Đăng ký môn học.  Dang shap
Ause case A  lu:
• • 0  V  US  4/18/2026  2:07 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3 / 3 • Fit (123%)
2 vI curr
Ping ky  ' man hor.  →  Rang Thugs
Ase are A longs u He cases
« includes.
2:07 PM
```

## [10:30]
**Nói:** thì nó sẽ là xe anh em nghi khá là quên hoặc không Nhưng mà để mình nói rõ nói rõ cho anh em nhé Thế này em hiểu đơn giản như này ví dụ khi ngâm thanh toán từ trên thì em thế nào anh em có thể có thể là anh em sẽ áp được mã giảm giá được chưa anh em
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)
Đing ký nom học. →  Rang Thuy
Ause ause A lion gos u Le cajiß
2:07 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)  •
Ause case s  thon got u Le cajas
« include →
3,  Extend.
Thah toán → co  'the ap ta?
• • 0  ^ G V  ENG - Q 4/18/2026  2:07 PM
```

## [11:00]
**Nói:** khi anh em thanh toán anh em sẽ có thể áp mã giảm giá vậy thì ở đây nghĩa là sao, cái tên nghĩa là gì nghĩa là cái use case này xảy ra khi có điều kiện được chưa anh em xảy ra khi và chỉ khi gần như kiểu vậy nghĩa là khi có điều kiện được chưa anh em và cuối cùng là cái thứ 4 là cái rất là ít gặp và mình xem để ngay cả trong Coursera nó sẽ rất là ít dùng được chứ nhé đó là cái Generations
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)  •
Ause case s  thon got u Le cajas
< include →
3,  Extend.
Thah toán → co  'the ap tašgiani
^ G  ENG  US  4/18/2026  2:08 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
thah toan → co
xay ra →
Gen.
lite  ^ G V e  ENG - Ф) E 4/18/2026  2:08 PM
```

## [11:30]
**Nói:** thì cái này nó là gì cái này nó chính là ký thửa cái này rất là ít dùng và ngay cả trong Coursera nó cũng ghi vậy cho nên là mình sẽ nói qua thôi đó chính là extra thì có thể có hết được mấy cái từ con bây giờ mình ví dụ nhé ví dụ nhé mình ví dụ này ví dụ mình có
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
tanh toán → co  " the app mangr im.
xay ra →
Gene.
^ G V •  ENG - Ф) E 4/18/2026  2:08 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)  7 O•
Acton cha
ENG  2:08 PM
US  4/18/2026
```

## [12:00]
**Nói:** là tiêu đình à Ừ mình có là mấy chú đi mình có là staff cái người quản lý hệ thống ấy mình có ba người này đúng không Thì bây giờ ba người này bây giờ ví dụ mình có một cái yêu cây là nó khi đó thì chắc chắn là thằng tiêu đường cũng cần nó in giảm viên cần nó in và ta này cũng cần nó in đó em đó thì bây giờ chẳng nghĩ mình làm một phát
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)
Acton cha
"tal"
Lad  ENG - 4) & 4/18/2026  2:09 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)  • C
stadent-
Legm;
Lecturer.-
staft.
^ G V e  ENG -Ф) 4/18/2026  2:09 PM
```

## [12:30]
**Nói:** là cùng đối này anh em như này nó rất là dối đúng không anh em nó vẫn đúng thôi nhưng mà nó rất là rồi nó ngon nha đó vậy thì bây giờ hay vào đó thì mình sẽ sử dụng cái gì đó là mình sẽ sử dụng cái thằng generalization trên nhé thì bây giờ nó sẽ làm gì nó sẽ có thêm một cái thằng nữa là thằng nó sẽ có thằng là mình sẽ để là yêu dơ đi trường là cái người mà đã đăng ký được chưa
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)  •
stadent-
legm
Lecturer.-
Staft?
ENG -Ф)E 4/18/2026  2:09 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)  •
regi
stalent
legm;
Lecturer.
staft.
ENG - Q) 4/18/2026  2:09 PM
```

## [13:00]
**Nói:** nha Bây giờ nếu mà nó có thêm cái thằng người đã đăng ký này rồi thì bây giờ mình sẽ chỉ cần Cho nó Tất cả mấy thằng này Được chứ anh em Cho tất cả mấy thằng này Kế thừa vào Kế thừa thằng này Được chứ anh em
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)
registered.
stalent
legm;
Lecturer.
staft.
^ G V O  ENG - 4) 4/18/2026  2:10 PM
```
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
L  Untitled • 3/3 • Fit (123%)
→ reg stered user.
stalent
legu
Lecturer.
staft.
^ G V  ENG -Ф) 4/18/2026  2:10 PM
```

## [13:30]
**Nói:** Đó Tất cả mấy thằng này kế thừa Và từ thằng này Mình cho nó vào đây Được chứ anh em Như là thằng cha này Nó dùng cái gì Thì những thằng con này Làm cái đấy Được chứ anh em Đó Anh em hiểu chưa Nó đơn giản vậy thôi nhá Đó Ok Thì đấy là tổng quan Mình chút lý thuyết cho anh em Để anh em hiểu được bài qua anh em nhé Ok đó đó là vì kiến thức để em thể là học vẽ được cái xây này em nhé Ok đó thì bây giờ mình sẽ bắt đầu bước vào cái bài này nhé Ok thì mày này mình sẽ cần biết những cái
**Màn hình:**
```
Untitled - 3 / 3 - Scrble Lite
Untitled • 3/3 • Fit (123%)
→ reg stered user.
stakent
legu  •
Lectues.
staff.
ENG -Ф) 4/18/2026  2:10 PM
```
**Màn hình:**
```
Ở cốc cốc  5 Luyện tập Q2 - Google Doc X  +  La ..
< > G @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  .10 =
• Tất cả dầu trang
Luyện tập Q2 * G  +
Share
File Edit View Insert Format Tools Extensions Help
asea 100%-  Normal text  Arial  | - 11] +  I U A O  E X  0 Editing
T...T..
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actor(s) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boyndary rectangle
• At least ONE <<include>> relationship - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
• Any actor-generalisation relationships that apply
ite  ENG  2:10 PM
US  - ( 4/18/2026
```

## [14:00]
**Nói:** gì thì trong bài này em để ý cho mình này mình nghĩ là mình sẽ về trên sao mà lời nhé Nói chung bạn thích dùng phần mềm nào thì dùng nói chung là nó cũng dễ dùng thôi nó cũng như nhau thôi em nhá đó thì bây giờ nhá bước đầu tiên này chưa phải phản ánh em cái vĩnh này đâu bởi vì là nó còn khá là nhiều phần linh tinh đó bây giờ đầu tiên anh em nhìn nhá Ok em thì nãy mình chút bây giờ mình sẽ dẫn anh em sẽ cái này nhá Ok thì cái này thì xử lý đã đơn giản thôi em nhá thì trong cái này nhá bước
**Màn hình:**
```
Ở cốc cốc  5 Luện tập Q2 - Google Doc X  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
C Tất cả dấu trang
Luyện tập Q2 * G  +
© Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BI UAO  GE D  0 Editing
2  3  4  5  6 7...!..
At least ONE <<include>> relationship  - provide a brief written rationale
At least ONE <<extend>> relationship  - provide a brief written rationale
• Any actor-generalisation relationships that apply
I
AS VENG 4/18/2026  2:11 PM
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< > G  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
• Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View  Insert Format Tools Extensions Help
a se  A 5 100% -  Normal text  Arial  | - 11] +  BILL ORDERED  / Editing
2  3  6
Đề trial
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
From a technical standpoint, the university imposes several constraints.  The system must
ENG  3:38 PM
฿  VI  4/18/2026
```

## [14:30]
**Nói:** đầu tiên này bài tiêu cầu đầu tiên nó là anh em sẽ cần phải xác định ra x tờ đúng không và sau đó mình đã xác định nó là primary hay là secondary được chưa thế là nó lại tự chính hay tự phụ mấy mình có nói rồi đúng không thì ở đây thì ở đây mình sẽ nhìn nhé có mỗi mẹo nhìn nhanh anh em nhìn phát anh em thì nhìn ngay ra những cái tự chính rồi anh em ví dụ anh em nhìn này cách tự chính anh
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  +I@ =
• Tất cả dấu trang
Luyện tập Q2  * D  +
=  • Share
File Edit View Insert Format Tools Extensions Help
asca A S 100% = Normal text =  Arial  | - 11] +  / Editing
2  4
=
Rand  3:38 PM
4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  = l  Luyện tập Q2 - Google Doc  +  La ..
< >  SP  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " CO  4IQ =
• Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View  Insert Format Tools Extensions Help
Q s  A § 100% -  Normal text  Arial  | - 11] +  BIA CO  BESEECE EX  / Editing
2  3  4  5
Đề trial
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
From a technical standpoint, the university imposes several constraints.  The system must
& V  ENG  3:38 PM
VI  4/18/2026
```

## [15:00]
**Nói:** em nhìn phát ra ngay này thì em chỉ đọc cái đoạn này thôi đó anh nhìn nhé có bốn main group of là một này thì nó sẽ có là tiêu đình là một này sau đó nó sẽ có là là lecture này có academic staff này có system administration này chưa thì trước mắt đấy thì là mình sẽ có bốn cái đằng actor cái này mình vứt vào đó nhá Ok thì đây mình vứt cho vào từng cái một nhá Ok và system Ok thì đây
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La  ...
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  / Editing
5
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
final grades,  and release grades to students once the grading period closes. Academic Staff
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
The interface must be accessible on both deskton and mobile browsers and must conform to.
ENG  3:38 PM
VI  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • | CD
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11+  BIAO GE  0 Editing
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
. List at least EIGHT use cases for the CRS. For each use case, state the initiatin
ctor(s) and a one-sentence description of the goal. (0.4 points
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
a-
ENG  3:39 PM
VI  4/18/2026
```

## [15:30]
**Nói:** là gì anh em nhỉ 4 loại này nó là cái gì đây thì cái này đều là primary đúng không primary xinh em đó thì bước đầu tiên mình đã xác định xong bốn loại thì bây giờ mình sẽ xem mục tiêu
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  Ca
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
• Tất cả dấu trang
Luyện tập Q2 # • 65 Saving....  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - | 11  I UA O  0-
3  5  O.....
4...l.. user accounts, contigures system parameters, and oversees scheduled data backups.
From a technical standpoint, the university imposes several constraints. The system must
remain responsive-handling at least 1,000 simultaneous users during peak registration periods
with a page-response time under 3 seconds. Because student records and grade data are  1 of 6
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RBAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
points)
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
ENG  3:39 PM
VI  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  = l  Luyện tập Q2 - Google Doc  +  La ..  -
< > G  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
• Tất cả dấu trang
Luyện tập Q2 * G  @ Saved to Drive  +
. -  • Share
File Edit View Insert Format Tools Extensions Help
Q5e  Normal text  Arial  |- [11 +  BIU  A  E#BE EE X :  / -
3  6
At least ONE <<include>> relationship  - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
N-  1. Identify All actors
Actor  Type  Goal
Students  Primary
Lecturers  Primary
Academic Staff  Primary
System Administrator  Primary
3:39 PM
4/18/2026
```

## [16:00]
**Nói:** muốn cái này là gì để tí nữa mình xem xem còn cái cái kênh đôi gì anh em nhé em bây giờ cứ tự đọc đến đâu mình xử lý đấy đầu tiên này học sinh cần xem các danh mục khóa học có sẵn học xem các danh mục khóa học có sẵn cho chị em đó, thì đây là gì học sinh này xem các danh mục có sẵn này và tiếp theo gì, check xem check cái điều kiện tiên quyết anh em nhé, check dựa trên các cái điều kiện tiên quyết là đã hoàn thành chưa
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  LI• =
88  C Tất cả dấu trang
Luyện tập Q2 * G  +
. c-  • Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text =  Arial  | - 11] +  I U  A 0  / -
2 E  3  7...!..
At least ONE <<include>> relationship  - provide a brief written rationale
• At least ONE <<extend>> relationship — provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary
Lecturers  Primary
Academic Staff  Primary
System Administrator  Primary
G  3:39 PM
4/18/2026
```
**Màn hình:**
```
cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools  Extensions Help
Normal text -  Arial  | - 11] +
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
governed by a role-based access control (RAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
ENG  3:40 PM
VI  4/18/2026
```

## [16:30]
**Nói:** được chưa, sau đó như thế nào submit cái đơn đăng ký để cho anh em, đó, và theo dõi trạng thái của mỗi cái request trong thời gian thực, thì anh em đọc cái đoạn này anh em phải có nhiều ngay cái liên kết cho mình này đầu tiên là phải check điều kiện liên quyết thì sau đó mới submit cái này sau khi submit cái này thì sẽ theo dõi cái này, nếu mà có mà đầy, đúng không? thì thế nào? học sinh sẽ tham gia vào cái danh sách trở được chưa? và
**Màn hình:** (không đổi)

## [17:00]
**Nói:** cái đơn đã đăng ký này sau khi mà đã được kiểu là sau khi mà đã đăng ký thì nào hệ thống sẽ tự động thông báo này để cho anh em nhìn cái hệ thống tự động thông báo để cho anh em thì đây nó là gì nhờ có cái này mà mình đã phát hiện ra cái gì đây nó chính là cái cái gì nhỉ, nó chính là cái x tờ thứ 5 anh em nhé mình có thể gọi nó là gì mình có thể gọi nó là hệ thống tự động thông báo
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc ×  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • /
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools  Extensions Help
a5ca A S 100% - Normal text ~  Arial  +  EX  Editing
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
governed by a role-based access control (BAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
G V  ENG  3:41 PM
VI  4/18/2026
```

## [17:30]
**Nói:** thì mình có thể gọi nó là system ở chỗ này thì mình có thể để nó là notification đi thông báo mà system trên đặt tên của gì cũng được ở trên nha Nói chung là nó phải đúng là danh từ là được anh em thì đây nó chính là xe cần đôi khi ok cho em bây giờ mình sẽ xử lý mục
**Màn hình:**
```
Ở cốc cốc  • Luện tập Q2 - Google Doc X  +  La ..
< ® docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  11 =
88  • Tất cả dấu trang
+
=  Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BI UA O  #SEEEEX  / Editing
7  3  4  5  6 x...?..
• At least ONE ‹<include>> relationship — provide a brief written rationale
• At least ONE <<extend>> relationship — provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary
Lecturers  Primary
Academic Staff  Primary
ATTEN 418/2026  3:41 PM
```
**Màn hình:**
```
Ở cốc cốc  = l  Luện tập Q2 - Google Doc.  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
88  • Tất cả dấu trang
Luyện tập Q2 # • 65 Saving...  +
=  • Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% - Normal text =  Arial  - 11] +  B I  U  A  / -
2 =  4  6
• At least ONE <<extend>> relationship  - provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary
Lecturers  Primary
Academic Staff  Primary
System Administrator  Primary
Notification system  Secondaryl
AS VENG - 4/18/2026  3:41 PM
```

## [18:00]
**Nói:** tiêu nhé Ok thì nãy mình đang đọc rồi đến đây nhá chết thông báo này nếu mà lúc này thì tham gia này khi mà đã đăng ký này thì thì chồng sẽ tự động thông báo và thêm được chưa Thêm cái học sinh đấy vào cái nguyên lý ở trên nha đó Ok thì bây giờ chốt lại là mình sẽ có cái gì thì đầu tiên là tiêu đơn có thể gì chắc chắn rồi có thể đăng ký học gọi chung thì là gì có thể đăng ký học Đấy chưa? Đăng ký học thì là gì?
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
95c8 AS 100% -  Normal text -  Arial  | - 11] +  •E X  :
...?..
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
final grades,  and release grades to students once the grading period closes. Academic Staff
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
The interface must be accessible on both deskton and mobile browsers and must conform to
ENG  3:41 PM
VI  4/18/2026
```
**Màn hình:**
```
Ớ cốc cốc  Luện tập Q2 - Google Doc X  +  La
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
8A 100  Normal text  Arial  |- 11] +  BIUA GEO  Editing
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (RBAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
G  ENG  3:42 PM
VI  4/18/2026
```

## [18:30]
**Nói:** Register Đúng không? Có thể đăng ký học Các cái khóa học Đúng không anh em? Có thể đăng ký các khóa học Sau đó thì nào? Sẽ có thể là gì nữa? Có thể là Sau khi mà đăng ký học thì thế nào? Thì có thể là theo dõi Theo dõi Status Đấy chưa? Và thế nào nữa? Nếu mà lúc này thì thế nào? Ok, đó
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  |
88  C Tất cả dấu trang
Luyện tập Q2 * G  (5 Saving...  +
. c -  © Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, S 100% - Normal text =  Arial  |- [11 +  B I  U  / -
2 E  4  6  -...?..
At least ONE <<extend>> relationship  - provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
N-  1. Identify All actors
Actor  Type  Goal
Students  Primary  Rel
Lecturers  Primary
Academic Staff  Primary
System Administrator  Primary
Notification system  Secondary
3:42 PM
4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  = |  TL Ф =
88  • Tất cả dấu trang
Luyện tập Q2 # G () Saving...  +
c -  • Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text -  Arial  | - 11] +  B I  U  E #BEE E XE  / -
2 E  4  6  M...l..
At least ONE <<extend>> relationship  - provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  legister for courses, trac
tatus,
Lecturers  Primary
Academic Staff  Primary
System Administrator  Primary
Notification system  Secondary
=  ATTC14 418/2026  3:42 PM
```

## [19:00]
**Nói:** Đấy là vì cái thằng học sinh Tiếp theo này, cái thằng sinh viên nhé Tiếp theo này là lecturer đúng không Cần xem lại danh sách À đây, xem lại danh sách Của sinh viên đã tham gia Sau đó gì Ghi ra cái bảng điểm Ghi ra cái điểm của bài giữa kỳ và cuối kỳ này Sau đó thì là công bố điểm này cho học sinh này
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  L IQ =
88  • Tất cả dấu trang
Luyện tập Q2 # • 65 Saving...  +
. -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text =  Arial  | - 11] +  U  A
2 E  4  6  ....!.
At least ONE <<extend>> relationship  - provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
N-  1. Identify All actors
Actor  Type  Goal
Students  Primary  saus plar cay ses, rac
Lecturers  Primary
*  Academic Staff  Primary
System Administrator  Primary
Notification system  Secondary
AST0 418/2026  3:42 PM
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La  ...
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools  Extensions Help
Normal text -  Arial  | - 11 +  0 -
staff. Each semester, the university must manage course enrollment for all undergraduate and
postgraduate programmes. Currently, students submit paper-based registration forms to their  1 of 6
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
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
ENG  3:43 PM
US  4/18/2026
```

## [19:30]
**Nói:** sau khi mà đã kết thúc việc chấm điểm này đó, ok chưa? thì tóm lại là gì? thì sẽ có thể là xem danh sách lớp nhập và công bố điểm thì đây nó sẽ là view roster đúng không? view roster danh sách lớp view class roster danh sách lớp này nhập là nguyên input great em có lịch tích xin anh đó đó Vậy rồi thì xin em tiếp theo này academic
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc ×  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q2 * G  +
• Share
File Edit View Insert Format Tools Extensions Help
95c a A 100% - Normal text =  Arial  |- 11] +  BI U  A  E  0 -
2 B  3
At least ONE include>> relationship  - provide a brief written rationale
• At least ONE <<extend>> relationship  - provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  Register for courses, track
status, join waitlist
Lecturers  Primary  I
Academic Staff  Primary
System Administrator  Primary
Notification system  Secondary
ENG  3:43 PM
US  04 2182026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< > C  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
88  • Tất cả dấu trang
Luyện tập Q2 # • 65 Saving....  +
c -  • Share
File Edit View Insert Format Tools Extensions Help
8A S 100%  Normal text  Arial  |- [11 +  BI U  G F  E#SE E EE X :  / -
2 E  3  6  M...!.
At least ONE <<include>> relationship  - provide a brief written rationale
• At least ONE <<extend>> relationship — provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  Register for courses, track
status, join waitlist
Lecturers  Primary  Vievi class roster, input]
Academic Staff  Primary
System Administrator  Primary
Notification system  Secondary
•GEO  ENG  3:43 PM
US  - 4 4/18/2026
```

## [20:00]
**Nói:** staff đó thì em xem mẹ academic staff này thì nó sẽ có gì nó sẽ có là chịu trách nhiệm gì đây quản lý nó kiểu là quản lý cái thử có nhiều anh em nhé tiết lập và công khai các cách các cái kiểu là chỉ tiêu thông tin liên quan đến cái khóa học chưa mở và đóng đăng ký này phê duyệt các cái
**Màn hình:**
```
Ở cốc cốc  = l  Luyện tập Q2 - Google Doc X  +  La ..
< > G  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  L IQ =
88  • Tất cả dấu trang
Luyện tập Q2 # G 65 Saving....  +
. c-  • Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text -  Arial  | - 11] +  I U  G Đ  0 -
2 E  3  V...!.
At least ONE <<include>> relationship  - provide a brief written rationale
• At least ONE <<extend>> relationship — provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  Register for courses, track
status, join waitlist
Lecturers  Primary  Viev class roster, input grade"
and |
Academic Staff  Primary
System Administrator  Primary
Notification system  Secondary
^G E O  ENG  3:43 PM
US  4/18/2026
```
**Màn hình:**
```
cốc cốc  Luyện tập Q2 - Google Doc  +  La
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luện tập Q2 * G  @ Saved to Drive  +
Share
File Edit View Insert  Format Tools Extensions Help
95c8 A S 100% - Normal text ~  Arial  | - 11] +  0 -
2 :
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
final grades,  and release grades to students once the grading period closes. Academic Staff
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
The interface must be accessible on both deskton and mobile browsers and must conform to
ENG  3:44 PM
US  4/18/2026
```

## [20:30]
**Nói:** trường hợp ngoại lệ này và tạo ra cái các cái việc là tham gia và phân làm báo cáo phân phối biển thì nó sẽ là thứ nhất này quản lý thời gian đúng không thì nó sẽ là mà nít menis tham table quản lý thì có hiểu này làm báo cáo nữa phân phối điểm đúng không Nói chung là à
**Màn hình:**
```
Luện tập Q2 - Google Doc x  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools  Extensions Help
5caAS10  Normal text  Arial  Editing
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
governed by a role-based access control (RAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
E  ENG  3:44 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc.  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®
88  • Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text *  Arial  |- 11] +  BIU  #S-E-E-EEX E  0 -
2 E  6
1. Identify All actors
Actor  Type  Goal
Students  Primary  Register for courses, track
status, join waitlist
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage time|
System Administrator  Primary
Notification system  Secondary
^ GE Q  ENG - Q E 4/18/2026  3:44 PM
```

## [21:00]
**Nói:** mình cứ dùng y như trong bài đi và phim Face Face luôn Exception luôn Được chưa
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®  L Q =
88  C• Tất cả dấu trang
Luyện tập Q2 * G  • Saved to Drive  +
Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A 5 100% -  Normal text  Arial  |- [11 +  I U  #E F= - E • E-E
2 E  3.. L.  6
1. Identify All actors
Actor  Type  Goal
Students  Primary  egister for courses, trac
tatus, join waitlis
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable
System Administrator  Primary
Notification system  Secondary
^ G E O  ENG  3:44 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  = l  Luện tập Q2 - Google Doc  +  La ..
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
88  • Tất cả dấu trang
Luyện tập Q2 # • 65 Saving....  +
• Share
File Edit View Insert Format Tools Extensions Help
95c8 AS 100% - Normal text =  Arial  | - 11] +  BI U  G F  / -
2 T  3  6
At least ONE ‹include>> relationship  - provide a brief written rationale
• At least ONE <<extend>> relationship — provide a brief written rationale
• Any actor-generalisation relationships that apply
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  Register for courses, track
status, join waitlist
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quotas,
approve
System Administrator  Primary
Notification system  Secondary
^ GE  ENG  3:45 PM
US  - 4 4/18/2026
```

## [21:30]
**Nói:** Tiếp theo này Là system admin Thì mình sẽ có gì đây Quản lý account chắc chắn rồi Không để thiếu rồi Quản lý account thì mình sẽ thêm vào luôn Quản lý account Gì nữa Quản lý account này Sau đó thì mình sẽ có là là cấu hình hệ thống đó và xa lưu dữ liệu thì chưa Đằng sau đó là xa lưu dữ liệu đấy bệnh cập
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  LI =
88  • Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text =  Arial  | - [11] +  I U  A  0 -
2 E  3  6  ..Te.
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  egister for courses, trac
atus, join waitlis
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quotas
approve exceptions
System Administrator  Primary
Notification system  Secondary
^G EO  ENG  3:45 PM
US  4 4/18/2026
```
**Màn hình:**
```
i cốc cốc  Luện tập Q2 - Google Doc  +  La
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®
88  • Tất cả dấu trang
Luyện tập Q2  * G  @ Saved to Drive  +
• -  * Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  0 -
7...!..
ites long queues during the registration window. The university's administrati
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
generating enrolment and grade-distribution reports. Finally, a System Administrator inanages
user accounts, configures system parameters, and oversees scheduled data backups.
From a technical standpoint, the university imposes several constraints. The system must
remain responsive-handling at least 1,000 simultaneous users during peak registration periods
with a page-response time under 3 seconds. Because student records and grade data are
sensitive, all communication must be encrypted using TLS 1.2 or higher, and access must be
governed by a role-based access control (BAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
nriman, or cocondar actor in ? nainte
^ GE  ENG  3:45 PM
US  4/18/2026
```

## [22:00]
**Nói:** đà tài đến thôi cho nhanh nhanh nhé Nói chung là chỗ này làm đơn giản này thôi tiếp theo này là hệ thống thông báo đó thì là thế nào gửi thông báo tự động đó thì nó sẽ đã xem auto notification của quên đi đâu anh em ok được chưa Đấy thế thôi gửi thông báo tự động được chưa nha nó vậy là mình đã xử lý
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CD
88  • Tất cả dấu trang
Luyện tập Q2 * G () Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A S 100% - Normal text ~  Arial  |- [11 +  U  A  F•E E-E
2 E  3  5  6
Actor  Type  Goal
Students  Primary  Seus rin ores, rac
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  lanage timetable, quota
pprove exception
System Administrator  Primary
configures system, |
Notification system  Secondary
•  G  ^G E O  ENG  3:45 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  ICO
88  • Tất cả dấu trang
Luyện tập Q2 * G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A § 100% - Normal text ~  Arial  |- [11] +  U  :  0 -
2 T  3  4  5  6
Actor  Type  Goal
Students  Primary
Segs r n ors, rac
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quota:
approve exception
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  sendautomated notification
for wai
co-
^ G EO  ENG  3:46 PM
US  4/18/2026
```

## [22:30]
**Nói:** cái ý đầu tiên Ok ý tiếp theo này nhà mình sẽ liệt kê có liệt kê ra các cái kêu cây liệt kê cây thì mình sẽ có gì đây nó bản liệt kê ít nhất 8 cái như là mình có được lấy là
**Màn hình:**
```
Ở cốc cốc  5 Luện tập Q2 - Google Doc X  +  La ..
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • | CD
88  • Tất cả dấu trang
Luện tập Q2 # G@ Saved to Drive  +
=  Share
File Edit View Insert Format Tools Extensions Help
9508 100-  Normal text  Arial  | - 11] +  BIUA•  0 -
6  ..?..
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitist/
ENG  3:46 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cồc  5 Luện tập Q2 - Google Doc X  +  La ..
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  40 =
88  • Tất cả dấu trang
Luyện tập Q2 # E@Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
as ca A S 100% = Normal text =  Arial  | - 11] +  BIU A O  #BEEE X  Editing
3
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2 of 6
2, Liet ke use case
203
3:46 PM
4/18/2026
```

## [23:00]
**Nói:** là 4 bằng 8 để xem nhau thì đây mình sẽ lại tạo bản như vậy nhưng sớm hay bồ lại có ba cái kéo xuống này là bốn cái bởi vì là nó còn cái là cái là tắt nhân khởi tạo đó Ừ ok cái đầu tiên là mình là ai đi số tự tiếp theo là tươi tiếp theo là cái khởi tạo tiếp theo là mục đích Ok đó 12
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CD
88  C Tất cả dấu trang
Luyện tập Q2 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, S 100% - Normal text ~  Arial  | - 11 +  U  A  "•EEE  E X  / Editing
3  4  graces and pubiisn grades  ..!..
Academic Staff  Primary  lanage timetable, quota
pprove exception
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notificatior
or waitlis
2, Liet ke use case
^G EQ  ENG  3:46 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®
88  • Tất cả dấu trang
Luyện tập Q2 * G 6) Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, 100% - Normal text -  Arial  |- [11] +  I  U  E BS E •EE E XE  / -
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
ID  Use casel
^GEO  ENG Ф) 4/18/2026  3:47 PM
```

## [23:30]
**Nói:** 3 4 5 6 7 8 Ok trước mắt là tám cái đó nhá sau đó thêm mình sẽ thêm sau Ok đầu tiên này
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q2 # G 6) Saving...  +
. e  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100%  Normal text  Arial  | - [11 +  U  #V-E•E-EEX :  / -
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
ID  Use case  In I
G  ^GEQ  ENG - Ф) 4/18/2026  3:47 PM
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc.  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  LIФ =
• Tất cả dấu trang
Luyện tập Q2 * G 65 Saving..  +
. g -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A § 100% - Normal text -  Arial  | - 11] +  BI UA•  E#SE E•EE X E
3  Tur wall?!  1..
2, Liet ke use case
ID  Use case  Initiating actor  Goal
2
Il
ASE 418/2026  3:47 PM
```

## [24:00]
**Nói:** kia cây một đúng không thì giờ chắc chắn rồi đó là nó sẽ là cái này xem được tiêu đường đó gì để xem các cái danh mục của khoa học có sẵn đúng không? thì là xem danh sách khoa học đúng không? thì bây giờ là gì? mình có thể để là xem danh sách khoa học đúng không? browse cross xem danh mục khoa học
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®  LI@ =
88  • Tất cả dấu trang
Luyện tập Q2 # • 65 Saving....  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  8 A S 100% - Normal text ~  Arial  | - (11  +  U  / -
apron Uroopmiane  6  .1.e
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
Use case  = +
ID  Initiating actor  Goal
2
^G E O  ENG  3:47 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc.  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Д | CD  LIA =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
. g -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A 5 100% -  Normal text  Arial  |- [11] +  BI UA  E#S-EEEE X E  / -
ur manid  6
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course |
2
4
ASE 4182026  3:48 PM
```

## [24:30]
**Nói:** được chưa? tra cứu danh mục khoa học cái này là student đúng không? mục tiêu là gì? mục tiêu là Ok mục tiêu là gì là để xem thôi nó sẽ là viewport list and details Đấy xinh không? Đó ok chưa? Đó thì bây giờ mình sẽ thế thôi tiếp theo cái tiếp theo là gì?
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  L IQ =
• Tất cả dấu trang
Luyện tập Q2 # • 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  8 A S 100% - Normal text ~  Arial  | - 11 +  BI UA  E #EECEX
6
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course
catalogue
a-
4
203
" • r O  ^ G E •  3:48 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc.  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  1 1Ф
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
A § 100% -  Normal text -  Arial  |- [11] +  BI UA  E SE EEE X  / -
3  6  .....
TOT TORNOE
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detaill
4
ASC 418/2026  3:48 PM
```

## [25:00]
**Nói:** được chắc chắn rồi không phải thiếu đó gì đó là sau khi mà xong này thì cái gì đấy là điều kiện tiên quyết đúng không thì nó sẽ làm sách đó chắc điều kiện tiên quyết hoặc trách trách điều kiện kiện này được chưa vẫn là con tiêu được để làm gì đây thì nó sẽ là kiểm tra điều kiện nó bảo
**Màn hình:**
```
Ới cốc cốc  Luyện tập Q2 - Google Doc x  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  L IQ =
C Tất cả dấu trang
Luyện tập Q2  +
Share
File  Edit View Insert Format Tools Extensions Help
A S 100% -  Normal text  Arial  | - 11] +  I U
3  6
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
4
203
G  ^G EQ  ENG  3:48 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  LI0 =
• Tất cả dấu trang
Luyện tập Q2 #  • Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
A S 100% -  Normal text  Arial  | - 11] +  BIU  A  = #SE•E•EE X E  / -
Mur malle
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
Check prerequisites  I l
4
5
^ GEO  ENG Q) E 4/18/2026  3:49 PM
```

## [25:30]
**Nói:** con đi sân trách con đi sân before before registration before sắp mít registration Ok trước khi đăng ký phải chắc điều kiện kiên quyết trước kiên quyết Ok tiếp theo gì là chắc
**Màn hình:**
```
Ớ cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®  L IQ =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
O -  Share
File  Edit View Insert Format Tools Extensions Help
A 5 100% -  Normal text "  Arial  | - [11 +  I U  A
3  6
Tur mansi
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
Check prerequisites  Student  Il
4
203
^ GE Q  ENG  3:49 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  LIO =
• Tất cả dấu trang
Luyện tập Q2 # G 6 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help  ~
Q 5  A § 100% - Normal text -  Arial  | - 11] +  I U  E #BECEEX  / -
3  6  .T..
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
2  Check prerequisites  Student  Check cendition
before registration|
4
^G EQ  ENG  3:49 PM
US
```

## [26:00]
**Nói:** sau khi mà trách ký nào thì sắp đi thôi sắp biết gây vết chơi trần quý quý yêu cầu trên em cái này vẫn là tiêu đồn thôi Ok thì đây mình sẽ có là gì mục tiêu là gì gửi đi làm gì để đăng
**Màn hình:**
```
Ớ cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  L IQ =
• Tất cả dấu trang
Luyện tập Q2 * G  @ Saved to Drive  +
0 -  Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A, S 100% - Normal text ~  Arial  | - 11 +  BIU
6  V..!.
2, Liet ke use case
ID  Use case  Initiating actor  Goal
Browse course catalogue  Student  lew course lis
nd deta
4 +  Student  Check condition
before registration
4
G  ^G EO  ENG  3:49 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc  +  La ..  -
< →  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
• Share
File Edit View Insert Format Tools Extensions  Help
Normal text  Arial  - 11] +  BI UAO  / -
AuLL  1  6
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  iew course lis
nd deta
Check prerequisites  Student  Check condition
before registration
Submit registration request  Student
5
...
ENG  3:50 PM
US  4/18/2026
```

## [26:30]
**Nói:** register for specific specific cost và tiếp theo sau khi gửi như thế nào thì chắc chắn rồi thì sẽ phải là join join nếu mà lúc này đầy đúng không Nếu mà lúc đầy thì mình sẽ phải doi Willis đúng không Vì này nó vẫn là
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  • |
• Tất cả dấu trang
Luyện tập Q2 # G 6) Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIU A O  / -
1  2
3  Submit registration request  Student  Rel I
5
203
G  ^GEO  3:50 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
• -  Share
File Edit View Insert Format Tools Extensions Help
as e  A, § 100% - Normal text ~  Arial  |- [11] +  BIU  A  E#*E E•E  E X
L...  4  Derore regisraton?..
3  Submit registration request  Student  egister Tor
pecific cours
Join
welL 2
^G EO  ENG Q) E 4/18/2026  3:50 PM
```

## [27:00]
**Nói:** Steven cho anh em thì đây nó sẽ là đăng ký khóa học khi đã đầy đúng không thì nó sẽ là register register quen dơ có đi cùng Ok nó tiếp theo là gì năm nó em cái thứ năm nhé anh em nhé Thì là gì à đúng rồi sau khi
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®  • I CD
88  • Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
E  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A, S 100% - Normal text ~  Arial  | - 11] +  BIU  E X
2  Derore registration.. ?..
Submit registration request  Student  kegister tor a
pecific courst
4  Join waitlist
203
^G E O  ENG  3:50 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc x  +  La  ...
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  ICO
• Tất cả dấu trang
Luện tập Q2 * G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
A 100%-  Normal text  Arial  | - 11] +  BI U
t.....  1  2  3  Torare regsran "... ?...
Submit registration request  Student  egister for a
pecific cours
Join waitlist  Student  Register when the
^GEO  ENG  3:51 PM
US
```

## [27:30]
**Nói:** mà có cái này đấy nếu mà đầy đúng không thì là mình sẽ vứt vào trong cái danh sách chờ và thế đó là mình sẽ bằng chích thời theo dõi thời gian thực chắc tên tớ tên tớ theo dõi hạ thái này tên tớ đúng không cho mày nó ghi mà anh em đây này đây đây check the status for request
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
• Tất cả dấu trang
Luyện tập Q2 # G 6 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11) +  BIU  • AD
2  3
berore registration "
Submit registration request  Student  egister tor
pecific cours
Join waitlist  Student  course ruin the a
1. 2
203
• -  ENG  3:51 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  = l  Luện tập Q2 - Google Doc X  +  La ..
< →  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  + 1Ф
• Tất cả dấu trang
Luyện tập Q2 # G@Saved to Drive  +
E  Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  U  0 -
Browse course catalogue  student  View course list  ..?.
and detail
=
Check prerequisites  Student  Check condition
before registration
ALL 1
Submit registration request  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
Track statusl
LLL 2
^ GE  ENG  3:51 PM
US  4/18/2026
```

## [28:00]
**Nói:** được chưa đó thì là mình sẽ phải trách trạng thái theo dõi trạng thái như thế nào và tiếp thì hết hết tiêu đơn đấy tiêu đơn này nó kêu được này ở đây mình sẽ có là gì xem các cái thôi tên
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®  L IQ =
88  C• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
E  • -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  8 A S 100% - Normal text ~  Arial  |- [11 +  I  U  *•E•E-E
Browse course catalogue  student  View course list  .!..
and detail
Check prerequisites  Student  Check condition
before registration
LLLL 1
Submit registration request  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
Track registratistatus
.Ler ?
^ G E  ENG  3:51 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  LIO =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, S 100% - Normal text =  Arial  | - 11] +  BI UAO  = #EE-EE X  / -
2  6
Submit registration request  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
5  Track registration status  Student
ele? DU
.. 3
^ G E O  ENG  3:52 PM
US  4/18/2026
```

## [28:30]
**Nói:** tiếp theo mình sẽ đến cái người là giảng viên đúng không biết là giảm viên thôi nhá giảm viên thì có rất là ít chức năng thôi đó là xem danh sách và nhập điểm được không Thì bây giờ mình sẽ có là view roster không mình quên mất đúng rồi quên mất đúng không
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • | CD
• Tất cả dấu trang
Luyện tập Q2 # G 6) Saving...  +
0 -  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% -  Normal text  Arial  | - [11 +  BI UA O  E#E EEE XE  0 -
2
Submit registration reuest  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  Viewl
S "7
G  ^G EQ  ENG  3:52 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  LIO =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
E  Share
File Edit View Insert Format Tools Extensions Help
Q 5  8 A S 100% - Normal text ×  Arial  |- 11] +  BI UA O  #=• E•E-E
6  1..
Submit registration request  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  View status
View rosl
^G E O  ENG  3:52 PM
US  4/18/2026
```

## [29:00]
**Nói:** à không em xem danh sách này mình nghĩ là không cần cho vào đúng nhỉ bởi vì là anh em nhớ cho mình nhé bởi vì cây này mình làm là tối nhất thì ví dụ ở đây nó xem cái này rồi xem thêm hết rồi em sẽ có là đầu tiên là view
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  * ®  LIO =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A 5 100% -  Normal text "  Arial  | - [11] +  BIUA•  E #EEEX  0 -
vi  6  1..
Submit registration reuest  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  View status
^ G E Q  ENG  3:52 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  L IQ =
• Tất cả dấu trang
Luyện tập Q2 * G  +
Share
File Edit View Insert Format Tools Extensions Help
Q5 e  A § 100% -  Normal text  Arial  |- 11] +  BIU  A 0  • #S-E-EEEX  0 -
6
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  iew course list
and detai
Check prerequisites  Student  Check condition
before registration
Submit registration request  Student  Register for a
specific course
Join waitlist  Student  Register when the
course is full
Track registration status  Student  View status
^ GE  ENG  3:53 PM
US  4/18/2026
```

## [29:30]
**Nói:** Android raster tiếp theo là mình sẽ có là giảm viên sẽ có gì đấy nhỉ có là record à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  =
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q5 e  8 100%  Normal text  Arial  | - [11] +  BIU
2  Derore regstration ?..
Submit registration request  Student  legister tor a
pecific course
Join waitlist  Student  Register when the
course is full
Track registration status  Student  View status
Viel
^G EO  ENG  3:53 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La ..
< >  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |  LIQ =
• Tất cả dấu trang
Luện tập Q2 * G  +
• -  Share
File Edit View Insert Format Tools Extensions  Help
as ca A S 100% - Normal text ~  Arial  | - 11] +  BI U  E X
...i...  Derore registration?..
Submit registration request  Student  register tor a
specific course
Join waitlist  Student  Register when the
course is full
Track registration status  Student  View status
View enrolled roster
Record grades I
1. 3
ENG  3:53 PM
US
```

## [30:00]
**Nói:** được chưa em Ok thì bây giờ mình viết này nhá đó là gì đầu tiên này xem danh sách đúng không
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La
< →  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  • I CD  =
• Tất cả dấu trang
Luyện tập Q2 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
A S 100% -  Normal text  Arial  | - 11] +  BI U
2
perore registration
Submit registration request  Student  register tor a
specific course
4  Join waitlist  Student  Register when the
course is full
Track registration status  Student  View status
View enrolled roster
Record and Regrades
G  ENG  3:53 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc.  +  La ..
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q5 e  A S 100% -  Normal text  Arial  |- 11] +  BIU A  • # *- E EE
6  L..!e
3  Submit registration request  Student  Register for :
pecific course
Join waitlist  Student  •gister when t
urse is 1
Track registration status  Student  View status
6  View enrolled roster
Record grades
8  Reagrades
^GE O  ENG  3:54 PM
US  4/18/2026
```

## [30:30]
**Nói:** view nó chỉ là letter r đây là gì view roster view roster user list
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • I CD
C Tất cả dấu trang
Luyện tập Q2  * D " Saving....  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A S 100% -  A Norma text y  Arial  |- [11 +  BI UA O
=
Submit registration request  Student  Register for
pecific cours
Join waitlist  Student  gister when t
urse is 1
Track registration status  Student  View status
View enrolled roster
Record grades
8  Release Grades
8 ~
^ G E  ENG  3:54 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< >  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
• Tất cả dấu trang
Luện tập Q2 # G@ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions  Help
Normal text  Arial  - 11] +  BI U
4  V...!..
Submit registration request  Student  Register for a
specific course
Join waitlist  Student
Track registration status  Student  View status
6  View enrolled roster  Lecturer  View roster I
Record grades  Lecturer
8  Release grades  Lecturer
ENG  3:54 PM
US  4/18/2026
```

## [31:00]
**Nói:** list student em rồi có cái này anh em nhé tiếp nhau là mình sẽ có là record với input giờ bí thơ em final great của anh em nó còn này là gì công bố điểm không thì là chỉ cần căm công bố điểm
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CD
C• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A § 100% -  Normal text  Arial  |- [11 +  BIU  A  F•E E-E
4  ..!..
Submit registration request  Student  Register for :
pecific courst
4  Join waitlist  Student
Track registration status  Student  View status
6  View enrolled roster  Lecturer  View the list'sl
Record grades  Lecturer
8  Release grades  Lecturer
4
G  ^ GE  ENG  3:54 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • | D
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
E  Share
File Edit View Insert Format Tools Extensions Help
Q5 e  84 10  Normal text  Arial  |- [11] +  BI U
3  4  6  ...?.
Submit registration request  Student  Register for a
pecific course
Join waitlist  Student
5  Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
Record grades  Lecturer  input the midterm
and fl
Release grades  Lecturer
G  ^ GE  ENG  "Ф (  3:55 PM
US  4/18/2026
```

## [31:30]
**Nói:** thôi là pháp lý great trên nhà thấy rồi chí này Ok xong mày làm mình đã xử lý xong cái đúng không tiếp theo là thằng này chưa khá là mất thời gian đấy Ok thì thằng này mình sẽ xử lý như
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CD
C• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A 5 100% -  Normal text "  Arial  |- [11 +  BIU  A
6  V..!.
Submit registration request  Student  Register for a
pecific course
Join waitlist  Student
5  Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer
^ G E  ENG  3:55 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc.  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
• Tất cả dấu trang
Luyện tập Q2 * G 65 Saving….  +
Share
File  Edit View Insert Format Tools Extensions Help
A, § 100% - Normal text ~  Arial  - 11 +  I U
2  3  4
specific course
Join waitlist  Student  Register when the
course is ful
5  Track registration status  Student  View status
6  View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
3 !. 1  8  Release grades  Lecturer  Publish grades
Academic Staff
Lelee.4
eleeS
^G E Q  ENG  -Ф (  3:55 PM
US  4/18/2026
```

## [32:00]
**Nói:** thế nào anh em để ý cho mình này ở đây thì nó có những vai trò gì quản lý tài khoản này cấu hình này chứ nhầm nhầm quản lý thì có biểu này chỉ tiêu hóa học này và phê duyệt các cái trường hợp thì đầu tiên là gì đầu tiên thì chắc đắn rồi quản lý có hiểu 3D hay một sức có anh em mấy thằng này bộ thì đây mình sẽ có gì đây mình sẽ có là nó sẽ có thể là tao này có quản lý
**Màn hình:**
```
ới cốc cốc  Luyện tập Q2 - Google Doc  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
A S 100% -  Normal text "  Arial  - 11 +  BI IU  E X
2  3  4
specific course
Join waitlist  Student  Register when the
course is ful
5  Track registration status  Student  View status
6  View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
8  Release grades  Lecturer  Publish grades
Academic Staff
....... S
^ G E °  ENG  3:55 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La  ...
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
A, § 100% - Normal text -  Arial  I- 11 +  B I U  E X
2  4
specific course
Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  View status
6  View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
3 . E  8  Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff
elu. 4
6 . 1.. 5
^ G E  ENG  3:56 PM
US  4/18/2026
```

## [32:30]
**Nói:** tạo là một này update này nó có biểu tham thiên một bữa trưa anh em nó Ok Nói chung là có thể ít phải chưa tiếp nhau quản lý thử có biểu này sau đó thì là nó sẽ có thể là cấu hình cái này nó sẽ có thể là nó đang trên này nó có một cái open open và close cái registration cái registration
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2  * • 6 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
A § 100% - Normal text ~  Arial  |- 11 +  B I U  # =- E • E-E  E X
2  3  4
specific course
Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  View status
6  View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
3 1.  8  Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create|
6 . 1 ..5
G  ^G EO  ENG  3:56 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  = l  Luyện tập Q2 - Google Doc  +  La ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  | D  1 1Ф
88  • Tất cả dấu trang
Luyện tập Q2  * D  +
E  Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text ~  Arial  | - 11] +  BI U  A  #*EE-E  E X :
6  L. lee
Cách làm
1. Identify All actors
Actor  Type  Goal
Students  Primary  Register for courses, track
status, join waitlist
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quotas,
approve exceptions
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2 Liet kençe case
^ G E  ENG  3:56 PM
US  4/18/2026
```

## [33:00]
**Nói:** Windows ấy nghĩa là có thể đóng và mở với cửa sổ đăng ký để chơi nhau thì nghĩa là mình sẽ có thể kênh Windows cửa sổ đăng ký để chơi nhắn thì nó có thể mở hoặc đóng mà Ừ thì đây mình sẽ có thể để là còn trâu open and close
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La ..  -
< > G  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  • |
• Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
Q5 e  8AS100%  Normal text  Arial  | - 11] +  0 -
scaling so that additional server capacity can be added smoothly as student numbers grow in
tuture years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary  1of7
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
points)
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
• At least ONE <<include>> relationship - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
Any actor-generalisation relationships that apply
G  ^ GE  ENG  3:56 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La  ...
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  LCD
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text -  Arial  | - 11] +  BI U  P•EEE
2  3  4  .1..
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
8  Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  Create, update
timetable
^ G E O  ENG  3:57 PM
US  4/18/2026
```

## [33:30]
**Nói:** Thế thôi mình biết đơn giản với em nhé không cần cầu kỳ chơi nha 11 đủ ý là sao tiếp theo mình sẽ có cái gì nhỉ hết rồi anh em ạ tiếp theo là mình không còn cái duyệt nữa đúng không thì mình sẽ có là ở cô à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2 # G 6) Saving...  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, S 100% - Normal text =  Arial  | - [11] +  BI U  A  F•E EPE
2  3  4  .?..
student enrolled the
course
Record grades  Lecturer  Input the midterm
and final grades
8  Release grades  Lecturer  Publish grades
9  Academic Staff  Create, update
timetable
Academic Staffl
T.
^ G E O  ENG  3:57 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc ×  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  410 =
88  • Tất cả dấu trang
Luyện tập Q2 # G  +
=  0 -  Share
File Edit View Insert Format Tools Extensions Help
as ca A S 100% - Normal text ~  Arial  | - 11] +  U  A  # SEE E  0-
1....  2  4  approve hopese  .?..
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2of7
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
2  Check prerequisites  Student  Check condition
before registration
^GEO  ENG  3:57 PM
US  4/18/2026
```

## [34:00]
**Nói:** phê duyệt cái này phê duyệt toàn bộ đúng không anh em phê duyệt các cái trường hợp ngoại lệ đúng không thì cái này thì vẫn là thuộc cái này đúng không anh ạ đó ok thì cái phê duyệt này thì nó sẽ làm gì
**Màn hình:**
```
Ởi cốc cốc  Luyện tập Q2 - Google Doc  +  La  ...
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 * G () Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
A, S 100% -  Normal text "  Arial  | - [11] +  B I U  E SEE• E
4  6
specific course
4  Join waitlist  Student  Register when the
course is full
Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  approve exceptions
^ G  E  ENG  3:57 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La ..
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " CO  LIQ =
88  • Tất cả dấu trang
+
Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100%~  Normal text -  Arial  | - 11 +  BIU A O
6  L..le
=  2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  /iew course list
and detai
2  Check prerequisites  Student  Check condition
before registration
Il
Submit registration request  Student  Register for a
specific course
4  Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  View status
^ GE  ENG  5:25 PM
US  4/18/2026
```

## [34:30]
**Nói:** thì cái này nó sẽ là nó sẽ duyệt thủ công đúng không các cái cây đặc biệt anh em có cho là duyệt cho việc thủ công và mình sẽ cho là để thủ công cái gì nhỉ mình cứ cho là ở khu
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2 #  +
Share
File  Edit View Insert Format Tools Extensions Help
A § 100% -  Normal text  Arial  - 11 +  BIU  # X•E•E•E
4  6  1..
Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions
^ G  E  ENG  5:25 PM
US  4/18/2026
```
**Màn hình:**
```
ởi cốc cốc  Luyện tập Q2 - Google Doc  +  La
3:  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
A § 100% Normal text "  Arial  - 11 +  BIU  #E F E E E
3  4  6
Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
imetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually I
.1.6. 1..5
ENG  5:25 PM
US  4/18/2026
```

## [35:00]
**Nói:** space cây Ok đấy để này thôi em nhé tiếp theo nữa thì chắc chắn rồi đó là gì nhỉ Đó là báo cáo của anh em thì cái này nó sẽ nằm trong cái system rồi nó đây mà chơi nhé à à à à à à à à à à à à à à à
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 * G 6 Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
A S 100% -  Normal text  Arial  - 11 +  BIU  #E V - E • E E
2  3  4  6
Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the  •
course
7  Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually l  I
G  E  ENG  5:25 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La  ...
< > G  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
88  • Tất cả dấu trang
Luyện tập Q2  +
=  Share
File Edit View Insert Format Tools Extensions Help
Q 5  A § 100% -  Normal text  Arial  | - [11] +  I U  #E F • E • E-E
3. 0..  4  6  .7..
=  1. Identify All actors
•
Actor  Type  Goal
Students  Primary  gister for courses, tra
tus, join waitl
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quotas,
approve exceptions
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
Ilico cacal  intelina balAr
AG E O  ENG  5:26 PM
US  4/18/2026
```

## [35:30]
**Nói:** đó là à quên quên nhấc nhầm nhầm nhầm anh em nhé vẫn chưa xong cái này là chưa xong anh em nhé bởi vì đây anh em nhìn nhé cái này đến tận đây này anh em nhé em này đây là trường hợp ngoại lệ rồi nhá Thực ra cái này anh em có thể có có thể không đều được rồi chứ nhé Nhưng mà ở đây nó cho thế rồi thì mình vẫn cho hết vào anh em nhé Ok thì em nhìn này em nhìn cho mình nhé em này Zen
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< →  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2 #  +
Share
File Edit View Insert Format Tools Extensions Help
Q 5  A, S 100% - Normal text ~  Arial  | - 11 +  I  U  #VEE-E
3  4  5  6
Actor  Type  Goal
Students  Primary  gister for courses, tra  •
atus, join waitl
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quotas,
approve exceptions
System Administrator  • Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
ID  Use case  Initiating actor  Goal
co-  1  Browse course catalogue  Student  View course list
and detail
^GE O  ENG  5:26 PM
US  4/18/2026
```
**Màn hình:**
```
Ở côc cốc  Luện tập Q2 - Google Doc X  +  Ca
C  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  EX  Editing
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
governed by a role-based access control (RAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
ENG  5:26 PM
US  4/18/2026
```

## [36:00]
**Nói:** cái này nó là một use case đúng không? thì cái này nó là gì? nó là generate report đúng không? bởi vì là nó sẽ có là cái report của việc là tham gia và phân phối điểm đúng không? thì bây giờ mình sẽ cho là generate report nó sẽ là 12 này generate report đúng không anh em? thì cái này nó sẽ thuộc vào vẫn là cái này đó ok thì cái này nó sẽ chỉ là
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc.  +  La  ...
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • | CD
88  • Tất cả dấu trang
Luyện tập Q2  +
Share
File Edit View Insert Format Tools Extensions Help
Q s  A § 100% -  Normal text  Arial  | - 11 +  BIUADOE  / Editing
booked, a student may join an erecuronic walis; snour a registered staent ater arop une
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
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
points)
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
^ GE  ENG  5:26 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc x  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0
• Tất cả dấu trang
Luyện tập Q2 * G  @ Saved to Drive  +
Share
File  Edit View Insert Format Tools Extensions Help
A, § 100% - | Normal text ~  Arial  I- 11 +  BIU  #VEE  E X
2  3  4  1..
Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  - Manually approve
special case
12  Generate reports
ENG  5:27 PM
US  4/18/2026
```

## [36:30]
**Nói:** thống kê đăng ký thôi đúng không thì nó sẽ là export export này registration này and phân phối điểm đúng không distribution ok à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
Ởi cốc cốc  Luyện tập Q2 - Google Doc  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 #  @ Saved to Drive  +
Share
File  Edit View Insert Format Tools Extensions Help
A, S 100% -  Normal text -  Arial  - 11 +  BIU  # X•E•E•E  E X
2  3  4  6  1..
Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the  •
course
Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
Generate reports  Academic Staff
^ G  ENG  5:27 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  *  CD
• Tất cả dấu trang
Luyện tập Q2 # G 6) Saving..  +
Share
File Edit View Insert Format Tools Extensions Help
A, § 100% - Normal text ~  Arial  - 11 +  BI U  #VEFE  E X
3  4  6
and final grades
Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
12  Generate reports  Academic Staff  Export registration "
+  and grade
distribution
u, 6
G  ^ G EQ  ENG  5:27 PM
US  4/18/2026
```

## [37:00]
**Nói:** mình sẽ có cái gì đây system admin đúng không thì mình sẽ có là quản lý tài khoản đúng không Chắc chắn rồi thì mình sẽ phải có là mẹ đi đúng không user account đúng anh em thì ở đây thì mình cái này là cái xếp tầm áp nhìn nó nó quen mồm đọc không Ok thì đây nhá Ở đây thì mình sẽ có cái gì
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc  +  Ca  ..
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2 * G  @ Saved to Drive  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIUAOOD  0 -
...... booked, a student may jom an erecronic wals; snoud a registerea stucent ater arop ine
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
governed by a role-based access control (RAC) model so that each user sees only the
functions and data relevant to their role. The platform must be available 99.5% of the time
during the semester, with any planned maintenance scheduled outside the registration window.
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actors) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
points)
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
ENG  5:27 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CD
• Tất cả dấu trang
Luyện tập Q2 * G 65 Saving..  +
=  Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A, § 100% - Normal text -  Arial  | - 11] +  I U  # V•E•E-E  :
2  6
1. Identify All actors
•
Actor  Type  Goal
Students  Primary  2 of7
register for courses, track
status, join waitiis*
Lecturers  Primary  View class roster, input
4 +  grades and publish grades
Academic Staff  Primary  Manage timetable, quotas,
approve exceptions
System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
In  Inteo caca  inteina naAr
E  ENG  5:28 PM
US  4/18/2026
```

## [37:30]
**Nói:** thì ở đây mình sẽ quản lý tài khoản thì chắc chắn rồi thì đó là mình sẽ chỉ là cái quản lý tài khoản chưa đâu xem trên này nó ghi như nào thì mình sẽ ghi nguyên như thế không bởi vì là quản lý tài khoản thì nó chỉ quản lý của tài khoản không đấy nó chỉ thế này không có quản lý tài khoản thì nó là quản lý tài khoản trên nha Ok thế đâu tiếp theo cái 14 này có 14 thì sao 14 thì là mình sẽ có là
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2 # G 6 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
5  A E 100% -  Normal text  Arial  |- 11 + B I U
supmi regisirauion request  Sueent  1..
Kegister or a
specific course
4  Join waitlist  Student  Register when the
course is full
5  Track registration status  Student  View status
View enrolled roster  Lecturer  View the list
student enrolled the
course
7  Record grades  Lecturer  put the midter
id final grade
8  Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Crete, update
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
12  Generate reports  Academic Staff  Export registration
and grade
distribution  I
13  Manage user accounts  System
Adminstratorl
•  ^  E  ENG  5:28 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2 * G6) Saving..  +
Share
File  Edit View Insert Format Tools Extensions Help
@ A E 100% - | Normal text "  Arial  - 11 +  B I U  FE E•E  E X
2  4  ..T.
student enrolled the
course
Record grades  Lecturer  Input the midterm
and final grades
Release grades  Lecturer  Publish grades
Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
12  Generate reports  Academic Staff  Export registration
and grade
distribution
13  Manage user accounts  System  manages user
Administrator  accoants,l
G  ^ G E  ENG  5:28 PM
US  4/18/2026
```

## [38:00]
**Nói:** cái cuối cùng hết rồi cái này thì có mỗi cái quản lý tài khoản rồi mấy cái này thì không cần anh em nhá Tại vì mấy cái này nằm trong tài khoản hết rồi đúng không cấu hình hệ thống hay là backup dữ liệu thì nó vẫn thế thôi thôi nha thì chỉ có mỗi là đến cái cuối nhá cái này có cái gì thì
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La  ...
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
A E 100% -  Normal text  Arial  - 11 +  BI U
2  3  4  6
and final grades
Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  Create, update
timetable
10  Madage registration  Academic Staff  Control open and
close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
12  Generate reports  Academic Staff  Export registration
and grade
distribution
13  Manage user accounts  System  manages user
Administrator  account
8 >
G  ^G EO  ENG  5:28 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La ..
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  • |
88  • Tất cả dấu trang
Luyện tập Q2 * G  +
=  0 -  Share
File Edit View Insert Format Tools Extensions Help
as e  8 A S 100% Normal text ~  Arial  | - 11] +  BI U  A  0 -
2-1  3  .1..
System Administrator  Primary  manages user accounts,
configures system, back up
data
I  Notification system  - Secondary  Send automated notification
for waitlist
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
2  Check prerequisites  Student  Check condition
before registration
ENG  5:29 PM
US  4/18/2026
```

## [38:30]
**Nói:** chắc chắn rồi nó có một cái thôi đó là gửi đi thông báo tự động đúng không thì mình sẽ chỉ cần gọi với là cái này nó là xem auto nội dung xe tải xe chơi nhạc rồi nó bán tự động thôi cái này thì nó chỉ là send email email ví dụ như bạn gọi email email còn phụ có thế rồi ok
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc x  +  La  ...
< →  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  ICO
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving..  +
• -  Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11 +  I  U  A  #E SEE E
6
data
Notification system  Secondary  Send automated notification
for waitlist
2 of 7
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  /iew course lis
and detai
2  Check prerequisites  Student  Check condition
before registration
ENG  5:29 PM
US  4/18/2026
```
**Màn hình:**
```
Ởi cốc cốc  Luyện tập Q2 - Google Doc x  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 # G 65 Saving....  +
Share
File  Edit View Insert Format Tools Extensions Help
A § 100% Normal text "  Arial  |- [11] +  B I U  P•E•EE
2  3  4  .?..
student enrolled the
course
Record grades  Lecturer  nput the midterr
ind final grade
Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approv.
pecial case
12  Generate reports  Academic Staff  Export registration
and grade
distribution
13  Manage user accounts  System  manages user
Administrator  account
14  Send automated  Notification system
notifications
G  ^ GE  ENG  5:29 PM
US  4/18/2026
```

## [39:00]
**Nói:** nhé Thì đấy là 14g cây cây nhá Ok vậy là mình đã xử lý xong cái này nó anh em ở đây mình sẽ xử lý ở đây thì nó sẽ tiếp theo này nó bảo mình làm vĩ cái này đúng không anh em đó ra này nó nghe thì bây giờ mình xem gì đó là bây giờ mình sẽ là vào đây này
**Màn hình:**
```
Ởị cốc cốc  Luyện tập Q2 - Google Doc  +  La  ...
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
88  • Tất cả dấu trang
Luyện tập Q2 * G 6) Saving...  +
Share
File  Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11 +  BIU  FE E E  E X
2  3  4  ..l.
student entolled the
course
Record grades  Lecturer  nput the midterr
ind final grade
Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approv.
pecial case
12  Generate reports  Academic Staff  Export registration
and grade
distribution
13  Manage user accounts  System  manages user
Administrator  account
14  Send automated  Notification system  Send email
notifications
^ G E  ENG  5:29 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  5 Luyện tập Q2 - Google Doc X  +  La ..
< > C  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  " ®  | D  . 14
• Tất cả dấu trang
Luyện tập Q2 * G  +
=  • -  Share
File Edit View Insert Format Tools Extensions Help
a sca A S 100% ~  Normal text  Arial  | - 11] +  B I U AO  Editing
1...  ....T.
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
goal and whether they are a primary or secondary actor. (0.3 points)
2. List at least EIGHT use cases for the CRS. For each use case, state the initiating
actor(s) and a one-sentence description of the goal. (0.4 points)
3. Draw a complete UML Use Case Diagram for the CRS. The diagram must include: (0.8
• All identified actors, placed correctly inside or outside the system boundary
• All major use cases inside the system boundary rectangle
• At least ONE <<include>> relationship - provide a brief written rationale
• At least ONE <<extend>> relationship - provide a brief written rationale
• Any actor-generalisation relationships that apply
AC E O  ENG  5:30 PM
US  - Ф 4/18/2026
```

## [39:30]
**Nói:** anh em tùy anh em nhé Nếu mà anh em nào mà dùng bất cứ phần mềm nào cũng được anh em nhé Đây mình dưới hạn anh em nói chung là mình tải một lúc nhiều phần mềm lắm cho nên là tùy anh em nói chung là tùy anh em cái này thì mình đang dùng là Star ML nhá đó thì nếu mà anh em vào này anh em bấm cho mình vào Model này Add diagram này chọn cho mình use case diagram này đó sau đó thì bước đầu tiên
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc X  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  CD
• Tất cả dấu trang
Luyện tập Q2 * G  +
Share
File  Edit View Insert Format Tools Extensions Help
Q 5  A § 100% - Normal text ~  Arial  | - [11] +  BI U  E X  0 Editing
2  4
Actor  Type  Goal
Students  Primary
Segs r n ors, rac
Lecturers  Primary  View class roster, input
grades and publish grades
Academic Staff  Primary  Manage timetable, quotas,
approve exceptions
System Administrator  Primary  manages user accounts,
configures system, back up
Il  data
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
^ G E  ENG  5:30 PM
US  4/18/2026
```
**Màn hình:**
```
StarUML (TRIAL MODE
File  Edit Format Model  Tools  View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  G Untitled
MI  al Model
TOOLBOX  EDITORS
Classes (Basic)
= Class
© Interface
_ Association
_ Directed Association
° Aggregation
Composition
Dependency
İ Generalization
* Interface Realization
Classes (Advanced)
100%
ENG  5:30 PM
US  4/18/2026
```

## [40:00]
**Nói:** nhá anh em làm đúng cho mình ba bước đầu tiên này cái đầu tiên là vào phát anh em phải làm cho mình như sau thứ nhất là anh em sẽ chọn cho mình là use case subject này đấy cái này nó chính là cái gì anh anh em biết đâu Chính là cái gì nhỉ bao nhiêu lý system nhá thì ở đây nhá mình sẽ là cái chữ nhật cái này mình đã nói đi trước với anh em từ trước rồi đúng không Thì bây giờ nhớ anh em bấm cho mình
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
a Main - Model  • Untitled
E) UseCaseDiagram1 - Modeli  & Model
E Modeli
i UseCaseDiagram1
TOOLBOX  EDITORS
• Properties
Use Cases  name  UseCaseDiagraml
i Package  defaultDiagram
• Use Case Subject  • Documentation
• Use Case
9 Actor
•l Frame
Association
Directed Association
i Generalization
Dependency
Include
i Modell  * Use aseDiagram: [UMLUseCaseDiagram)  100%
^ G  ENG  5:30 PM
US  4/18/2026
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +
< →  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  . 10
• Tất cả dấu trang
Luyện tập Q2 * G  +
=  • ea-  Share
File Edit View Insert Format Tools Extensions Help
a5 e  A § 100% - Normal text =  Arial  |- 11] +  "BE-EEX  0 Editing
.....  3  4  appure uAnipiUro  6  ..!..
=  System Administrator  Primary  manages user accounts,
configures system, back up
data
Notification system  Secondary  Send automated notification
4 +  for waitlist
2, Liet ke use case
ID  Use case  Initiating actor  Goal
1  Browse course catalogue  Student  View course list
and detail
2  Check prerequisites  Student  Check condition
before registration
• •  ^GE O  ENG  5:31 PM
*  US  4/18/2026
```

## [40:30]
**Nói:** vào đây này em lên đây nhá đầu tiên là cái tên nó gọi đây này tin đây này chưa điện thoại mà anh em anh em sẽ lấy cho mình đây em bấm đây cho mình nhá đó là cái x tờ đúng không x tờ thì bây giờ mình đang
**Màn hình:**
```
Ở cốc cốc  Luện tập Q2 - Google Doc X  +  La  ..
< >  C  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  I CO
88  • Tất cả dấu trang
Luyện tập Q2 * =  +
Share
File Edit View Insert Format Tools Extensions Help
Normal text -  Arial  - 11] +  / Editing
slow, and creates long queues during the registration window. The university's administration
has therefore decided to commission a web-based Course Registration System (CRS) to
automate and streamline the entire workfiow.  1 of 7
The CRS is expected to serve four main groups of users. Students need to browse the
catalogue of available courses, check their eligibility based on completed prerequisites, submit
registration requests, and track the status of each request in real time. If a course is fully
booked, a student may join an electronic waitlist; should a registered student later drop the
course, the system automatically notifies and enrolls the first eligible student on the waitlist.
Lecturers need to review the roster of students enrolled in their courses, record midterm and
final grades, and release grades to students once the grading period closes. Academic Staff
(administrators) are responsible for defining the semester timetable, setting and publishing
course quotas, opening and closing the reyistration window, approving exceptional cases, and
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
Question 2: UC Modeling (1.5 points)
1. Identify ALL actors in the Course Registration System. For each actor, state their primary
G  ENG  5:31 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools  View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
Main - Model  y Untitled
9] UseCaseDiagram1 - Model1  & Model
Course Registration System  E Modeli
2] UseCaseDiagram1
• Course Registration System
TOOLBOX  EDITORS
• Styles
Use Cases  Font  Arial  13
i Package  Color  • Inherit
• Use Case Subject  Line Style  J 6°
• Use Case  Format
} Actor  Label
[O]  [T]
• Frame
• Association
Alignment  al-  cu
Directed Association
i Generalization  • Properties
Dependency  Course Registration Sy:
= Include
i Modell  • UseCaseSubjecti [UMLUseCaseSubject]  90%
ENG  5:31 PM
US  4/18/2026
```

## [41:00]
**Nói:** 1, 2, 3, 4, 5 Để xem anh em Lại tiếu 1 Ok đây, mình nhấp ở đây nhé Sau đó thì anh em đặt tên cho mình Để 2 pin này cho dễ nhìn nhé anh em nhé Ok, đó, 5 Thì bây giờ mình sẽ copy tên của mấy thằng ấy vào đây
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model  Tools  View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Main - Model  EB  5) Untitled
9] UseCaseDiagram1 - Modeli  & Model
Course Registration System  a Modeli
9] UseCaseDiagram1
• Course Registration System
7 Actori
Actori
**
TOOLBOX  EDITORS
• Properties
Use Cases  name  Actor1
i Package  stereotype  Q.
• Use Case Subject  visibility  public
• Use Case  isAbstract
Actor 8  isFinalSpecialization
Frame  isLeal
_ Association  • Documentation
1 Directed Association
İ Generalization
Dependency
I Include
i Modell  9 AStOCI [UMLACtOr)  90%
^  ENG  5:31 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
2 Main - Model  " Untitled
19] UseCaseDiagram 1 - Modeli  MI  & Model
Course Registration System  4 Modell
2 UseCaseDiagram1
Course Registration System
Actorl  % Actorl
% Actor2
& Actors
* Actor4
} Actor5
Actor2
9.
TOOLBOX  EDITORS
ictors
• Styles
Use Cases  Font  Arial  13
i Package  Color  • Inherit
Actor3
• Use Case Subject  Line Style
• Use Case  Format
} Actor  Label
[O]  Er]
• Frame
_ Association
Alignment  al-  cu
Directed Association
İ Generalization  • Properties
I Dependency  Actors
: Include
i Modell  % Actors [UMLActor]  80%
ENG  5:32 PM
US  4/18/2026
```

## [41:30]
**Nói:** thằng nhất là Steven đó ok thứ 2 này copy đi nhỏ nhảy 3 là nói chung là anh em vào anh em cứ làm y như mình nhá bước đầu tiên đừng nghĩ nhiều đó là mình sẽ phải lấy hết ra đã sau đó mình tính sau ok 5 nhưng mà cái này cực kỳ đặc biệt anh em này
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model  Tools  View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Main - Model  6) Untitled
2] UseCaseDiagram1 - Modell  MI  & Model
Course Registration System  a Modeli
2] UseCaseDiagram1
^  • Course Registration System
(Studenti  ₴ Actorl
& Actor2
Actor4  * Actor3
% Actor4
} Actor5
Actor2
TOOLBOX  EDITORS
^  • Styles
Use Cases  Actor5  Font  Arial  13
i Package  Color  • Inherit
Actor3
• Use Case Subject  Line Style
• Use Case  Format
} Actor  Label
(a]  [O]  ET]
•l Frame
Association
Alignment  cu
1 Directed Association
İ Generalization  • Properties
Dependency  Actorl
: Include
i Modell  % Actors [UMLActor  80%
ENG  5:32 PM
E  US  4/18/2026
```
**Màn hình:**
```
cốc cốc  Luyện tập Q2 - Google Doc X  +
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  G  ICO
• Tất cả dấu trang
Luyện tập Q2 *  +
Share
File Edit View Insert Format Tools Extensions Help
Q  100% -  Normal text -  Arial  +  B  I  =" #S-EE•R
2-:
Churonto  Drimon  Donictor to
Luyện tập Q2 - Google Docs - C...  • StarUML (TRIAL MODE)  Phân tích Actor và Use Case - G...  OBS 31.1.2 - Cấu hình: Không tê...  Sticky Notes
for waitlist
2, Liet ke use case
ID  Use case  Initiating actor  Goal
Browse course catalogue  Student  View course list
and detail
^ G  ENG  5:32 PM
US  4/18/2026
```

## [42:00]
**Nói:** Cái này cực kì lưu ý cho mình nhé Cái x tờ này nhé Nó là cái x tờ phụ Đúng không? Thì anh em phải thêm cho mình Anh em phải thêm cho mình nhé Đó là
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Main - Model  9 Untitled
19] UseCaseDiagram1 — Modeli  & Model
Course Registration System  a Modell
2] UseCaseDiagram1
Course Registration System
Student  Student
% Lecturers
System Administ  * Academic Staff
} System Administrator
7 Notification system
Lecturers
TOOLBOX  EDITORS
• Styles
Use Cases  Arial  13
Notification system
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  Line Style
• Use Case  Format
? Actor  Label
[O]  [T]
Frame
Association
Alignment
Directed Association
i Generalization  • Properties
Dependency  Notification system
: Include  stereotype
a Modell  Notincation system [UMLActor  80%
ENG  5:32 PM
E  US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  1 Untitled
19] UseCaseDiagram 1 - Modeli  MI  & Model
Course Registration System
& Modell
: UseCaseDiagram1
Course Registration System
Student  Student
& Lecturers
System Administ  * Academic Staff
} System Administrator
7 Notification system
0) Constraint1
Lecturers
TOOLBOX  EDITORS
• Styles
Use Cases  Font  Arial  13
• Notication system
i Package  Color  • Inherit
Academic Staff  7 0
• Use Case Subject  Line Style
• Use Case  Format
? Actor  Label
[O]  [T]
•l Frame
• Association
Alignment  cu
Directed Association  dijo
i Generalization  • Properties
1 Dependency  Notification system
= Include  stereotype
i Modell  * Notification system [UMLActor  80%
ENG  Ф)  5:33 PM
US  4/18/2026
```

## [42:30]
**Nói:** dưới nhé mình sẽ bạn mình mới dùng cái này mình còn anh em nhớ anh em chờ mình một chút để mình nghiên cứu lại một chút
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools  View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Main - Model  y Untitled
9] UseCaseDiagram1 - Modeli  MI  & Model
Course Registration System  à Modell
2] UseCaseDiagram1
Course Registration System
Student  Student
& Lecturers
System Administ  * Academic Staff
÷ System Administrator
7 Notification system
0) Constraint1
Lecturers
TOOLBOX  EDITORS
• Styles
Use Cases  Arial  13
Notification system
• Package  Color  • Inhent
Academic Staff
• Use Case Subject  Line Style
• Use Case  Format
% Actor  Label
(0)  ET)
Frame
Association
Alignment  ol-  cu
1 Directed Association
İ Generalization  • Properties
1 Dependency  Notification system
i Include  stereotype
a Modell  Notlication System [UMLActor)  80%
ENG  Ф)  5:33 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  • Untitled
MI  Eat Model
19] UseCaseDiagram 1 - Modeli  Course Registration System
E) Modell
9) UseCaseDiagram1
• Course Registration System
Student  * Student
* Lecturers
System Administ  Academic Staff
* System Administrator
9 Notification system
• Constrainti
Lecturers  • Operation1
₺ Actor1
TOOLBOX  Q  EDITORS
Actor1  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  Line Style
• Use Case  Format  =i l
9 Actor  Label
[O]  Er)
• Frame
• Association
Alignment  o|-
Directed Association
i Generalization  › Properties
Dependency  Actorl
I Include  stereotype
a Modell  * Actor 1 [UMLActor]  80%
ENG  ф)  5:33 PM
US  4/18/2026
```

## [43:00]
**Nói:** cho nó đi tôi biết mà luôn đi Ok đấy thì anh nha Ok đó thì tiếp theo mình sẽ có là cái gì đây biết
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
Main - Model  • Untitled
MI  Ea Model
19] UseCaseDiagram1 - Modeli  Course Registration System
E Modell
2] UseCaseDiagram 1
• Course Registration System
Student  * Student
* Lecturers
System Administrator  } Academic Staff
? System Administrator
% Notification system
• Constraint
Lecturers  • Operation1
} Actor1
TOOLBOX  EDITORS
Actor1  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  Line Style
• Use Case  Format  =i l
% Actor  Label
(0)  ET)
• Frame
Association
Alignment  ol-  cu
1 Directed Association
İ Generalization  • Properties
1 Dependency  System Administrator
: Include  stereotype
E Modell  ¢ System Aaminıstrator [UMLActor  80%
ENG  Ф)  5:33 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)  X
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
Main - Model  EB  4 Untitled
Ea Model
119] UseCaseDiagram 1 - Modeli  Course Registration System
E Modell
X] UseCaseDiagram1
• Course Registration System
Student  System Administrator  & Student
* Lecturers
} Academic Staff
* System Administrator
* Notification system
• Constraint1
Lecturers  • Operation1
} Notification system
TOOLBOX  EDITORS
Notification system
Use Cases
• Package
Academic Staff
• Use Case Subject
• Use Case
? Actor
•l Frame
Association
I Directed Association
i Generalization
/ Dependency
- Include
80%
ENG  Ф)  5:40 PM
US  4/18/2026
```

## [43:30]
**Nói:** cái gì cây và anh em nhé Đây mình sẽ có 1 2 14 cái đúng không nha Nó bảo là ít nhất là 8 mà thì cho 14 cái trên nha thì 14 cái này mình sẽ cho cái gì em bấm vào đây cho mình này cho mình 14 ra một hai này chết bóng nhỏ một này hai này ba này bốn này năm sáu bảy tám chín người 11 12 13 14
**Màn hình:**
```
Ởi côc cốc  Luyện tập Q2 - Google Doc x  +  La
< >  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  •CD
88  •• Tất cả dầu trang
Luyện tập Q2 #  +
E  0 -  Share
File Edit View Insert Format Tools Extensions Help
Q  100% -  Normal text -  Arial  -  +  B  I  +  S-E •E :
configures system, back up
data
Notification system  Secondary  Send automated notification
for waitlist
2, Liet ke use case
= +-
ID  Use case  Initiating actor  Goal
co-  1  Browse course catalogue  Student  View course list
and detail
2  Check prerequisites  Student  Check condition
before registration
*  ^ G E  ENG  5:40 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
3 Main - Model  19) UseCaseDiagram1
12] UseCaseDiagram1 - Modelt  • Course Registration System
Course Registration System  • UseCase1
• UseCase2
• UseCase3
UseCasel  ₽ Student
Student  System Administrator
* Lecturers
% Academic Staff
UseCase3
} System Administrator
7  * Notification system
^  •) Constrainti
Lecturers  • Operation1
& Notification system
TOOLBOX  EDITORS
Notification system  • Properties
Use Cases  name  UseCase3
i Package  stereotype  Q.
Academic Staff
• Use Case Subject  visibility  public
• Use Case  isAbstract
7 Actor  isFinalSpecialization
Frame  isLeaf
_ Association  • Documentation
Directed Association
i Generalization
I Dependency
= Include
a Modell  UseCase3 (UMLUseCase)  80%
ENG  5:41 PM
US  4/18/2026
```

## [44:00]
**Nói:** Ừ ok chơi nha cứ thêm như thế đã được chưa sau đó thì mình bắt đầu như hết vào thì cho anh em anh em cứ đi hết là cho mình đã thì đây ạ Út sạch và cho mình một ngày à 2 này
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model  Tools  View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
a Main - Model  Untitled
E Model
2] UseCaseDiagram1 - Modeli  Course Registration System
E Modeli
2] UseCaseDiagram1
• Course Registration System
Student  System Administrator  ₽ Student
% Lecturers
% Academic Staff
* System Administrator
* Notification system
() Constrainti
Lecturers  • Operation1
} Notification system
TOOLBOX  EDITORS
Notification system  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inhent
Academic Staff
• Use Case Subject  Line Style  J 5
• Use Case "  Format
% Actor  Label
(0)  [T]
• Frame
_ Association
Alignment
Directed Association
i Generalization  • Properties
/ Dependency  Course Registration Sy:
L Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject)  80%
ENG  Ф)  5:41 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)  X
File  Edit  Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  © UseCase10
MI  • UseCase11
2] UseCaseDiagram1 — Modeli  Course Registration System
• UseCase12
Browse course ca  • UseCase13
UseCase2  UseCase14
8 8  UseCase3
Student  UseCase4  System Administrator  Student
& Lecturers
* Academic Staff
UseCases  UseCase7  UseCase8  * System Administrator
UseCased
% Notification system
• Constrainti
Lecturers  • Operation1
UseCase12  } Notification system
UseCase9  UseCase11
TOOLBOX  UseCase10  EDITORS
Notification system  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  UseCase13  UseCase14  Line Style
• Use Case  Format
2 Actor  Label
EO]  [T]
2l Frame
Association
Alignment  al-  cu
Directed Association
İ Generalization  • Properties
Dependency  Browse course catalogue
= Include  stereotype
E] Modell  Usecase: [UMLUseCase]
course is till
ENG  5:41 PM
US  4/18/2026
```

## [44:30]
**Nói:** rồi rồi bước này anh em cứ làm cho mình ba bước đầu tiên thì anh em cứ làm đơn giản này cho mình 3 4 5
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  • UseCase10
MI  • UseCase11
19] UseCaseDiagram1 - Model1  Course Registration System
• UseCase12
Browse course catalogue  • UseCase13
• UseCase14
Check prerequisites  UseCase3
Student  UseCase4  System Administrator  & Student
& Lecturers
Academic Staff
UseCase5  UseCase7  UseCase8  } System Administrator
UseCase
2 Notification system
• Constrainti
Lecturers  • Operation1
UseCase12  } Notification system
UseCase9  UseCase11
TOOLBOX  UseCase10  EDITORS
Notification system  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  UseCase13  UseCase14  Line Style  2 5
• Use Case  Format
? Actor  Label
[T]
Frame
l Association
Alignment  cu
Directed Association  dijo
i Generalization  • Properties
I Dependency  Course Registration Sy:
LT Include  stereotype
i Modell  Course Kegistration System (UMLUseCaseSubjecti  80%
ENG  Ф)  5:41 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  • UseCase10
• UseCase11
19] UseCaseDiagram1 - Modelt  Course Registration System
• UseCase12
Browse course catalogue  • UseCase13
• UseCase14
Check prerequisites
Student  UseCase4  System Administrator  & Student
UseCase6  & Lecturers
Submit registration request
Academic Staff
UseCase7  UseCases  } System Administrator
* Notification system
Join waitlist  UseCase9  • Constrainti
Lecturers  • Operation1
UseCase12  } Notification system
UseCasell
TOOLBOX  UseCase10  EDITORS
Notification system  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  UseCase13  UseCase14  Line Style
• Use Case  Format
} Actor  Label
(O)  [T]
Frame
• Association
Alignment  ol-  cu
Directed Association
i Generalization  • Properties
Dependency  Join wartlist
ET Include  stereotype
E Modell  Course Registration System  • join wartlist [UMLUseCase]  80%
ENG  Ф)  5:42 PM
US  4/18/2026
```

## [45:00]
**Nói:** Ok mình đang phải cân nó nào làm sao để cho nó đẹp nhất anh em nhé
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Modet  • UseCase8
MI  • UseCase11
9] UseCaseDiagram1 - Modelt  Course Registration System
• UseCase12
Browse course catalogue  • UseCase13
• UseCase14
Check prerequisites
Student  UseCase4  System Administrator  % Student
UseCase6  * Lecturers
Submit registration request
Academic Staff
UseCase7  UseCases  * System Administrator
Join waitlist  * Notification system
UseCase9  • Constrainti
Lecturers  • Operation1
UseCast 10
UseCase12  & Notification system
UseCase11
TOOLBOX  EDITORS
Notification system  • Styles
Use Cases  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  UseCase13  UseCase14  Line Style
• Use Case  Format
? Actor  Label
(H)  (01]  ET]
Frame
_ Association
Alignment
I Directed Association
İ Generalization  • Properties
Dependency  UseCase10
i Include  stereotype
E] Modell  • UseCase10 [UMLUseCasel  80%
C  ENG  5:42 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)  X
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  MODEL EXPLORER
2) Main - Model  • UseCase7
MI  • UseCase&
2] UseCaseDiagram1 — Modeli  Course Registration System
• UseCase12
Browse course catalogue  • UseCase13
• UseCase14
Check prerequisites
Student  UseCase4  System Administrator  & Student
UseCase6  * Lecturers
Submit registration request
} Academic Staff
UseCase7  UseCases  System Administrator
Join waitlist  } Notification system
• Constrainti
Lecturers  • Operation1
Track registration status
UseCase12  & Notification system
TOOLBOX  View enrolled roster  EDITORS
Notification system  • Styles
Use Cases  Record grades  Font  Arial  13
• Package  Color  • Inherit
Academic Staff
• Use Case Subject  UseCase13  UseCase14  Line Style
• Use Case  Format
2 Actor  Label
(H]  [a]  (0)]  ET]
• Frame
Association
Alignment  o|-
I Directed Association
i Generalization  • Properties
7 Dependency  Course Registration Sy:
ET Include  stereotype
E Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  5:42 PM
US  4/18/2026
```

## [45:30]
**Nói:** chồng anh nhau đẩy này sang đây dễ bởi vì hai cái kia một chiếc hơi nhiều Ok Ok Đây là không Cái này thì
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  • UseCase4
• UseCase7
9] UseCaseDiagram1 - Modell  Course Registration System
• UseCase8
Browse course catalogue  • UseCase12
• UseCase14
Check prerequisites
Student  UseCase4  System Administrator  % Student
UseCase6  & Lecturers
Submit registration request
Academic Staff
UseCase7  UseCases  } System Administrator
Join waitlist  } Notification system
• Constrainti
Lecturers  • Operation1
Track registration status
UseCase12  & Notification system
TOOLBOX  View enrolled roster  EDITORS
Notification system  • Styles
Use Cases  Record grades  Font  Arial  13
• Package  Color  • Inherit
Academic Staff  Release grades
• Use Case Subject  UseCase14  Line Style
• Use Case  Format
? Actor  Label
(a]  (0)  [T]
Frame
Association
Alignment  cu
I Directed Association
İ Generalization  • Properties
i Dependency  Release grades
i Include  stereotype
i Modell  Release grades [UMLUseCase]  80%
C  ENG  Ф)  5:42 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
3 Main - Model  • Browse course catalogue
• UseCase4
9] UseCaseDiagram1 - Modeli  Course Registration System
• UseCase7
Browse course catalogue  Academic Staff  • UseCase8
• UseCase12
Check prerequisites  } Student
Student  UseCase4
UseCase  & Lecturers
Submit registration request  7 Academic Staff
UseCase7  UseCase8  } System Administrator
Join waitlist  * Notification system
System Administrator
() Constrainti
Track registration status  • Operation1
UseCase12  } Notification system
Lecturers
TOOLBOX  View enrolled roster  EDITORS
• Styles
Use Cases  Record grades  Font  Arial  13
i Package  Notification system  Color  • Inherit
Release grades
• Use Case Subject  Line Style
• Use Case  Manage timetable  Format
2 Actor  Label
(a]  Er]
Frame
Association
Alignment  ol-  cu
I Directed Association
İ Generalization  • Properties
1 Dependency  System Administrator
i Include  stereotype
E Modell  System Administrator (UMLActor]  80%
ENG  Ф)  5:43 PM
US  4/18/2026
```

## [46:00]
**Nói:** mình sẽ nhắc sang đây để này nó đẹp anh em nhé cho nó dễ nhìn em ạ à Ok hiện tại mình đang để tạm như này đã ok à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
cốc cốc  Luyện tập Q2 - Google Doc ×  +  La  -
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  CD
• Tất cả dấu trang
Luyện tập Q2 #  +
] -  Share
File Edit View Insert Format Tools Extensions Help
5  100% -  Normal text -  Arial  -  +  I  A  "-E-E- :
2
View enrolled roster  Lecturer  View the list
=  student enrolled the
course
7  Record grades  Lecturer  Input the midterm
and final grades
8  Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  reate, updati
imetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
12  Generate reports  Academic Staff  Export registration
and grade
distribution
13  Manage user accounts  System  manages user
Administrator  account
14  Send automated  Notification system  Send email confirm
notifications
^ G  E  ENG  5:43 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)  X
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q
2 Main - Modet  • Browse course catalogue
MI  • UseCase4
18] UseCaseDiagram1 — Modeli  Course Registration System
• UseCaset
Browse course catalogue  • UseCase&
Manage timetable  • UseCase12
Check prerequisites  Academic Staff  P Student
Student  UseCase4
seCasee  * Lecturers
Submit registration request  & Academic Staff
UseCase  UseCase8  System Administrator
Join waitlist  * Notification system
• Constraintl
System Administrator  • Operation1
Track registration status  UseCase12  & Notification system
Lecturers
TOOLBOX  EDITORS
View enrolled roster  • Styles
Use Cases  Font  Arial  13
i Package  Notification system  Color  • Inherit
Record grades
• Use Case Subject  Line Style
• Use Case  Release grades  Format
7 Actor  Label
(:]  [O]  [T]
Frame
Association
Alignment  ol-
I Directed Association
Generalization  • Properties
1 Dependency  name  UseCase6
Include  stereotype
E] Modell  • Course Registration System  2 UseLase [UMLUseCase)  80%
E  C  ENG  Ф)  5:43 PM
US  4/18/2026
```

## [46:30]
**Nói:** Ok xong đó thì nha bước đầu tiên xong vậy thì bây giờ anh em bắt đầu vào này đầu tiên là anh
**Màn hình:**
```
* • StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q
3 Main - Model  • Browse course catalogue
MI  • UseCase4
8] UseCaseDiagram1 — Modeli  Course Registration System
• UseCase
Browse course catalogue  • UseCase8
Manage timetable  • UseCase12
Check prerequisites  Academic Staff  % Student
Student  UseCase4
Manage registration window  * Lecturers
Submit registration request]
₺ Academic Staff
UseCase8  System Administrator
Join waitlist  UseGaseT
* Notification system
• Constrainti
System Administrator  • Operation1
UseCase12  & Notification system
Lecturers  Track registration status
TOOLBOX  EDITORS
View enrolled roster  • Styles
Use Cases  Arial  13
i Package  Notification system  Color  • Inherit
Record grades
• Use Case Subject  Line Style
• Use Case  Release grades  Format
2 Actor  Label
[b]  ET]
Frame
Association
Alignment  al-  cu
Directed Association
i Generalization  • Properties
T Dependency  UseCase?
: Include  stereotype
ta Modell  UseKase/ [UMLUseCase)  80%
C  ENG  5:43 PM
US  4/18/2026
```
**Màn hình:**
```
* • StarUML (TRIAL MODE)  X
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  MODEL EXPLORER
3) Main - Model  6B  • Generate reports
MI  • Manage user accounts
12] UseCaseDiagram1 - Modelt  Course Registration System
• Send automated notifications
Browse course catalogue  • Browse course catalogue
Manage timetable
• Approve exceptions
Check prerequisites  Academic Staff  } Student
Student
Manage registration window  * Lecturers
Submit registration request
} Academic Staff
Approve exceptions  System Administrator
Join waitlist  * Notification system
( Constrainti
System Administrator  • Operation1
Generate reports
& Notification system
Lecturers  Track registration status
TOOLBOX  EDITORS
View enrolled roster  Manage user accounts  • Styles
Use Cases  Font  Arial  13
• Package  Notification system  Color  • Inherit
Record grades
• Use Case Subject  Send automated notifications  Line Style
• Use Case  Release grades  Format
? Actor  Label
[T]
Frame
Association
Alignment  al-  cu
Directed Association
i Generalization  • Properties
Dependency  Course Registration Sy:
i Include  stereotype
ta Modell  Course Registration System [UMLUseCaseSubject)  80%
ENG  5:44 PM
US  4/18/2026
```

## [47:00]
**Nói:** em sử dụng cái xong xin tết trên đồng cái association này thì bây giờ anh em bấm vào anh em với cái nào thì em sẽ nói cái đấy sẽ nhau à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  • Generate reports
MI  • Manage user accounts
19] UseCaseDiagram1 - Modell  Course Registration System
• Send automated notifications
Browse course catalogue  • Browse course catalogue
Manage timetable
• Approve exceptions
Check prerequisites  Academic Staff  ₽ Student
Student
Manage registration window  * Lecturers
Submit registration request  % Academic Staff
Approve exceptions  } System Administrator
Join waitlist  ÷ Notification system
( Constraintl
System Administrator  • Operation1
Generate reports
& Notification system
Lecturers  Track registration status
TOOLBOX  EDITORS
View enrolled roster  Manage user accounts  • Styles
Use Cases  Font  Arial  13
# Package  Notification system  Color  • Inherit
Record grades
• Use Case Subject  Send automated notifications  Line Style
• Use Case  Release grades  Format
% Actor  Label
(0]  [T]
Frame
Association
Alignment  cu
1 Directed Association
İ Generalization  • Properties
I Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  5:44 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  Invalid connection (UMLAssociation)  *  MODEL EXPLORER  Q.
E Main - Model  • Approve exceptions
Invalid connection (UMLAssociation)  * Student
9] UseCaseDiagram1 - Modell  MI
Course Registration System  (Student-Browse course catalogue
Browse course catalogue  (Student-Check prerequisites)
Manage timetable  (Student-Submit registration reque
Check prerequisites  Academic Staff  (Student-Join waitlist)
Student
Manage registration window  *lecturers
Submit registration request  % Academic Staff
Approve exceptions  * System Administrator
Join waitlist  2 Notification system
• Constraint1
• Operation1
Generate reports  System Administrator
7 Notification system
Lecturers  Track registration status
TOOLBOX  EDITORS
View enrolled roster  Manage user accounts  • Properties
Use Cases  name
i Package  Notification system  stereotype  Q.
Record grades
• Use Case Subject  Send automated notifications  visibility  public
• Use Case  Release grades  isDerived
% Actor
endl.name
Frame
endl.reference  Student
Association
endl.stereotype
1 Directed Association
endl.visibility  public
i Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
= Include  endl.multiplicity
E Modell  % Student  JI [UMLAssociation]  80%
E  ENG  5:44 PM
US  4/18/2026
```

## [47:30]
**Nói:** Ok mình để này trong việc anh em nhé
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  Invalid connection (UMLAssociation)  *  MODEL EXPLORER
3 Main - Model  * * Student
• (Student-Browse course catalogue
9] UseCaseDiagram 1 - Modell  Course Registration System  • _ (Student-Check prerequisites)
Browse course catalogue  (Student-Submit registration reque
Manage timetable  • (Student-Join waitlist)
Check prerequisites  Academic Staff  (Student-Track registration status)
Student
Manage registration window  ₴ Lecturers
Submit registration request  } Academic Staff
Approve exceptions  * System Administrator
Join waitlist  2 Notification system
• Constraint1
• Operation1
Generate reports  System Administrator
} Notification system
Lecturers  Track registration status
TOOLBOX  EDITORS
View enrolled roster  Manage user accounts  • Properties
Use Cases  name
i Package  Notification system  stereotype  Q.
Record grades
• Use Case Subject  Send automated notifications  visibility  public
• Use Case  Release grades  isDerived
% Actor
endl.name
Frame
end .reference  Student
Association
endl stereotype
T Directed Association
endl.visibility  public
i Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
- Include  endl.multiplicity
i Modell  % Student  / [UMLAssociation]  80%
ENG  5:44 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  (View enrolled roster-Course Re
9] UseCaseDiagram 1 - Modell  MI  • Track registration status
Course Registration System
• Record grades
Q  Browse course catalogue  • Release grades
Manage timetable
Check prerequisites  • Manage timetable
Student  Academic Staff  • Generate reports
Manage registration window  • Manage user accounts
Submit registration request
• Send automated notifications
Approve exceptions  • Browse course catalogue
Join waitlist  • Approve exceptions
7  ? Student
Track registration status  System Administrator  • _ (Student-Browse course catalogue
Generate reports
• (Student-Check prerequisites)
TOOLBOX  EDITORS
View enrol →  Manage user accounts  • Properties
Use Cases  name
• Package  Notification system  stereotype  Q.
Record grades
• Use Case Subject  Send automated notifications  visibility  public
• Use Case  Release grades  isDerived
? Actor
endl.name
Frame
endl.reference  View enrolled roster
• Association a
endl. stereotype
Directed Association
endl. visibility  public
İ Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
Include  endl.multiplicity
i Modell  Course Registration System  • View enrolled roster  [UMLAssociation)  80%
case lancs
ENG  Ф)  5:45 PM
US  4/18/2026
```

## [48:00]
**Nói:** Ok thế này nó không bị trồng lên nhau anh nhỏ Ok tiếp theo này anh em cứ làm như mình thôi anh vào anh em cứ giã này cho mình à à Ừ ok 3 này cả nhà đúng rồi đúng rồi mấy cái này thì một thôi
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Invalid connection (UMLAssociation)
2 Main - Model  • Track registration status
9] UseCaseDiagram1 - Modell  MI  • Record grades
Course Registration System
• Release grades
Browse course catalogue  • Manage timetable
Manage timetable
Check prerequisites  • Generate reports
Student  Academic Staff  • Manage user accounts
Manage registration window  • Send automated notifications
Submit registration request
• Browse course catalogue
Approve exceptions  • Approve exceptions
Join waitlist  7 Student
• (Student-Browse course catalogue
Track registration status  System Administrator  • _ (Student-Check prerequisites)
Generate reports
• (Student-Submit registration reque
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Notification system  Color  • Inherit
Record grades
• Use Case Subject  Send automated notifications  Line Style  JIUS
• Use Case  Release grades  Format
7 Actor  Label
[T]
Frame
Association
Alignment
1 Directed Association  diji
i Generalization  • Properties
Dependency  Record grades
i Include  stereotype
i Modell  Course Registration System  • Kecora grades [UMLUseCase)  80%
ENG  5:45 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View  Window Debug Help
WORKING DIAGRAMS  Invalid connection (UMLAssociation)  *  MODEL EXPLORER
3 Main - Model  * Lecturers
(Lecturers-View enrolled roster)
9] UseCaseDiagram1 - Modell  Course Registration System  / (Lecturers-Record grades)
Browse course catalogue  J (Lecturers-Release grades)
Manage timetable  Academic Staff
Check prerequisites  (Academic Staff-Manage timetable
Student  Academic Staff
Manage registration window  (Academic Staff-Manage registratic
Submit registration request  (Academic Staff-Approve exceptior
Approve exceptions  * System Administrator
Join waitlist  & Notification system
• Constraint1
• Operation1
Track registration status  Generate reports  System Administrator
7 Notification system
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
2 Actor
endl.name
Frame
endl.reference  % Academic Staff
Association a
endl stereotype
Directed Association
endl.visibility  public
İ Generalization
endl.navigable  unspecified
/ Dependency
endl.aggregation  none
El Include  endl.multiplicity
i Modell  % Academic Staff  [UMLAssociation]  80%
Aciease graces
C  ENG  5:45 PM
US  4/18/2026
```

## [48:30]
**Nói:** rồi nha đó sao thì xinh nha bây giờ bố này nó xong có như vậy là anh em đã xong rất là nhiều người em nhá anh em đã gần như là xong gần xong rồi thì xinh nha bây bước tiếp theo là anh em sẽ xác định cái quan hệ nó là xong rồi xinh nha đó như là quan hệ của nó mình sẽ xử lý như nào thì
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q
2 Main - Model  • (Lecturers-Record grades)
(Lecturers-Release grades)
I UseCaseDiagram1 - Modell  Course Registration System  } Academic Staff
Browse course catalogue  | (Academic Staff-Manage timetable
Manage timetable  (Academic Staff-Manage registratic
Check prerequisites  Academic Staff  (Academic Staff-Approve exceptior
Student
Manage registration window  (Academic Staff-Course Registratio
Submit registration request  (Academic Staff-Generate reports)
Approve exceptions  System Administrator
Join waitlist  & Notification system
• Constraint1
• Operation1
Track registration status  Generate reports  System Administrator
} Notification system
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
? Actor
endl.name
Frame
endl.reference  Academic Staff
• Association
endl stereotype
1 Directed Association
endl.visibility  public
İ Generalization
endl.navigable  unspecified
* Dependency
endl.aggregation  none
L Include  endl.multiplicity
i Modell  % Academic Staff  J [UMLAssociation]  80%
ENG  Ф)  5:45 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
2 Main - Model  * Academic Statt
(Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modelt  MI
Course Registration System  (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Manage timetable  (Academic Staff-Course Registratio
Check prerequisites  Academic Staff  (Academic Staff-Generate reports)
Student
Manage registration window  * System Administrator
Submit registration request  (System Administrator-Manage usE
Approve exceptions  % Notification system
Join waitlist  • Constraint1
• Operation1
} Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
2 Actor
endl.name
Frame
endl.reference  Notification system
_ Association
endl stereotype
Directed Association
endl.visibility  public
i Generalization
endl.navigable  unspecified
/ Dependency
endl.aggregation  none
i Include  endl.multiplicity
i Modell  % Notification system  [UMLAssociation]  80%
E  ENG  Ф)  5:46 PM
US  4/18/2026
```

## [49:00]
**Nói:** đó là mình sẽ xử lý cái in lúc và cái xe nói nha thì mình sẽ xử lý in lúc và xe như nào thì ở đây mình sẽ có là cái lúc thì Ừ ok em mình tiếp tục nhá Nãy mình lại có người gọi Ok Ok thì bây giờ nhá mình đang nói đâu nhỉ Bây giờ là cái quan hệ đúng anh em thì mình sẽ là mình sẽ có cái quan hệ là include và xe nó không bị đánh hướng dẫn anh em trong phần lý thuyết rồi include là khi nào đó
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model lools  View  Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  * Academic Statt
(Academic Staff-Manage timetable
9] UseCaseDiagram1 - Modell  Course Registration System  • (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Manage timetable  (Academic Staff-Course Registratio
Check prerequisites  Academic Staff  (Academic Staff-Generate reports)
Student
Manage registration window  % System Administrator
Submit registration request  _ (System Administrator-Manage usE
Approve exceptions  & Notification system
Join waitlist  • Constraint1
• Operation1
% Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
2 Actor
endl.name
Frame
end reference  } Notification system
_ Association
endl stereotype
Directed Association
endl.visibility  public
İ Generalization
end1.navigable  unspecified
Dependency
endl.aggregation  none
i Include  endl.multiplicity
2 Modell  } Notification system  I [UMLAssociation]  80%
E  C  ENG  Ф)  5:47 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
2 Main - Model  * Academic Statt
(Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modelt  MI
Course Registration System  (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Manage timetable  (Academic Staff-Course Registratio
Check prerequisites  Academic Staff  (Academic Staff-Generate reports)
Student
Manage registration window  * System Administrator
Submit registration request  (System Administrator-Manage usE
Approve exceptions  * Notification system
Join waitlist  • Constrainti
• Operation1
} Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
2 Actor
endl.name
Frame
end reference  Notification system
_ Association
endl stereotype
Directed Association
endl.visibility  public
i Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
I Include  endl.multiplicity
ta Modell  % Notification system  [UMLAssociation)  80%
E  ENG  Ф)  5:47 PM
US  4/18/2026
```

## [49:30]
**Nói:** là ví dụ mình nói luôn trong bài này ví dụ như là cái UK3 này đúng không là cái gì Cái này là cái này là cái này là sắp mít sắp mít registration đúng không thì cái này là cái khi mà sinh viên gửi đi cái yêu cầu đăng ký đúng không gửi yêu cầu đăng ký thì nó sẽ thế nào mỗi một lần mà để cái này trước
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  * Academic Statt
• (Academic Staff-Manage timetable
9] UseCaseDiagram1 - Modell  Course Registration System  • (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Manage timetable  _ (Academic Staff-Course Registratio
Check prerequisites  Academic Staff  (Academic Staff-Generate reports)
Student
Manage registration window  ? System Administrator
Submit registration request  • (System Administrator-Manage use
Approve exceptions  & Notification system
Join waitlist  • Constraint1
• Operation1
% Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
% Actor
endl.name
Frame
endl.reference  } Notification system
Association
endl stereotype
Directed Association
endl.visibility  public
İ Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
1 Include  endl.multiplicity
i Modell  % Notification system  [UMLAssociation]  80%
C  ENG  Ф)  5:47 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
2 Main - Model  * Academic Statt
(Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modelt  MI
Course Registration System  (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Manage timetable  (Academic Staff-Course Registratio
Check prerequisites  Academic Staff  (Academic Staff-Generate reports)
Student
Manage registration window  * System Administrator
Submit registration request  (System Administrator-Manage usE
Approve exceptions  * Notification system
Join waitlist  • Constrainti
• Operation1
} Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
2 Actor
end1.name
Frame
endl.reference  Notification system
_ Association
endl. stereotype
Directed Association
endl.visibility  public
i Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
if Include  endl.multiplicity
25 Modell  % Notification system  [UMLAssociation)  80%
E  C  ENG  Ф)  5:48 PM
US  4/18/2026
```

## [50:00]
**Nói:** Mỗi khi mà sinh viên đột đơn đăng ký Thì hệ thống sẽ phải làm gì nhỉ Thì hệ thống sẽ luôn luôn bắt buộc Phải là kiểm tra điều kiện Tiên quyết đúng không Đây này anh em nhé Đó đây này Mình sẽ kéo này ra đây một chút Và mình sẽ kéo này ra đây một chút Đó Mình sẽ kéo thẳng ra đây cho anh em thấy nhìn này
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  * Academic Statt
• (Academic Staff-Manage timetable
9] UseCaseDiagram1 - Modell  Course Registration System  • (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Manage timetable  _ (Academic Staff-Course Registratio
Check prerequisites  Academic Staff  (Academic Staff-Generate reports)
Student
Manage registration window  ? System Administrator
Submit registration request  • (System Administrator-Manage use
Approve exceptions  & Notification system
Join waitlist  • Constraint1
• Operation1
% Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
Use Cases  name
i Package  Record grades  Notification system
stereotype  Q.
• Use Case Subject  Send automated notifications  visibility  public
Release grades
• Use Case  isDerived
% Actor
endl.name
Frame
end .reference  } Notification system
Association
endl stereotype
Directed Association
endl.visibility  public
İ Generalization
endl.navigable  unspecified
Dependency
endl.aggregation  none
1 Include  endl.multiplicity
i Modell  % Notification system  [UMLAssociation]  80%
ENG  Ф)  5:48 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
E Main - Model  * Academic Statt
(Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modell  MI
Course Registration System  (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Check prerequisites  Manage timetable  (Academic Staff-Course Registratio
Student  Academic Staff  (Academic Staff-Generate reports)
Manage registration window  % System Administrator
_ (System Administrator-Manage use
Approve exceptions  & Notification system
Submit registration request
Join waitlist  • Constraint1
• Operation1
% Notification system
Track registration status  Generate reports  System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
? Actor  Label
[O]  Er]
•l Frame
_ Association
Alignment  ol-  cul
Directed Association
İ Generalization  • Properties
1 Dependency  Submit registration reque
1 Include  stereotype
2 Modell  Course Registration System  • Submit registration reditest [UMLUseCase]  80%
C  ENG  Ф)  5:48 PM
US  4/18/2026
```

## [50:30]
**Nói:** Đó Thì đầu tiên nhá Thì khi mà sinh viên gửi cái này đi Gửi yêu cầu này đi đúng không Thì nó sẽ làm mỗi khi mà gửi cái này Thì nó phải check cái này Đúng không Đó chính vì vậy Cái này gửi đi Thì check cái này Hành vi này nó luôn xảy ra Không thể bỏ qua đúng không Nghĩa là gửi cái này thì phải check cái này Đấy là điều mà chắc chắn nó luôn luôn xảy ra đúng không Như mình đã hướng dẫn anh em ở trong kỹ thuyết rồi Đó đúng không Nó luôn luôn thế nào đấy đúng không Buộc phải kiểm tra thế nào đấy
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  * Academic Statt
(Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modell  Course Registration System  (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Check prerequisites  Manage timetable  (Academic Staff-Course Registratio
Student  Academic Staff  (Academic Staff-Generate reports)
Manage registration window  * System Administrator
_ (System Administrator-Manage use
Approve exceptions  & Notification system
Join waitlist  0) Constraint1
Submit registration request
o Operation1
% Notification system
Track registration status  Generate reports  . System Administrator
(Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
2 Actor  Label
(0]  [T]
Frame
Association
Alignment  cu
Directed Association
i Generalization  • Properties
Dependency  Course Registration Sy:
i Include  stereotype
i Modell  course Registration Systent (UMLUseCaseSubject)  80%
ENG  5:48 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
23 Main - Model  * Academic Statt
| (Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modelt  MI
Course Registration System  / (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Check prerequisites  Manage timetable  (Academic Staff-Course Registratio
Student  Academic Staff  (Academic Staff-Generate reports)
Manage registration window  7 System Administrator
(System Administrator-Manage usE
Approve exceptions  * Notification system
Join waitlist  Submit registrition request  • Constrainti
• Operation1
} Notification system
Track registration status  Generate reports  - System Administrator
(Notification system—Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
2 Actor  Label
[0]  [T]
Frame
_ Association
Alignment  al-  cu
Directed Association
i Generalization  • Properties
I Dependency  Course Registration Sy:
= Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  5:49 PM
US  4/18/2026
```

## [51:00]
**Nói:** anh em nó tương tự như mình bái đăng ký môn học thì bắt buộc là phải trước phải phải đăng nhập đúng không phải login thì bây giờ cái này tương tự như vậy để mà gửi được cái request này thì phải check cái này đúng không thì đây nó chính là include đúng không anh em thì nó chính là đây bấm vào include này nhớ từ đây sang đây được xin nhé Đó ok chưa đó Vậy là anh em đã xử lý xong với quan hệ nhá tiếp
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
23 Main - Model  * Academic Statt
| (Academic Staff-Manage timetable
9] UseCaseDiagram 1 - Modelt  MI
Course Registration System  / (Academic Staff-Manage registratic
Browse course catalogue  (Academic Staff-Approve exceptior
Check prerequisites  Manage timetable  (Academic Staff-Course Registratio
Student  Academic Staff  (Academic Staff-Generate reports)
Manage registration window  * System Administrator
(System Administrator-Manage use
Approve exceptions  * Notification system
Join waitlist  Submit registration request  • Constrainti
• Operation1
} Notification system
Track registration status  Generate reports  - System Administrator
_ (Notification system-Send automa
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
2 Actor  Label
(0)  [T]
Frame
• Association
Alignment  al-  cu
Directed Association
i Generalization  • Properties
1 Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  5:49 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  LT (Submit registration request→Chi
9] UseCaseDiagram 1 - Modell  • Join waitlist
Course Registration System
• Manage registration window
Browse course catalogue  • View enrolled roster
Check prerequisites  Manage timetable
• Track registration status
Student  Academic Staff  • Record grades
«include»  Manage registration window  • Release grades
• Manage timetable
Approve exceptions  • Generate reports
Join waitlist  Submit registration request  • Manage user accounts
• Send automated notifications
Track registration status  System Administrator  • Browse course catalogue
Generate reports
Lecturers  • Approve exceptions
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
2 Actor  Label
(01]  Er]
Frame
_ Association
Alignment
Directed Association
İ Generalization  • Properties
I Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  5:49 PM
US  4/18/2026
```

## [51:30]
**Nói:** theo này cái in của lúc đã bắt buộc đúng không thì đây là bắt buộc rồi chứ chưa đấy là giải quyết xong cái gì đâu Cái đầu tiên của đề nhắc đây này lúc từ chưa đó Ok cho anh em đó thì tiếp theo tiếp theo này mình sẽ có cái gì tiếp theo là mình sẽ có là xten đúng không thì bây giờ nếu mà xten đúng không thì mình sẽ có cái gì
**Màn hình:**
```
Ởi côc cốc  Luyện tập Q2 - Google Doc  +  La
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  CD
• Tất cả dấu trang
Luyện tập Q2 *  +
E  Share
File Edit View Insert Format Tools Extensions Help
Q  5  100% -  Normal text -  Arial  -  +  B  I  A
3  4
8  Release grades  Lecturer  Publish grades
9  Manage timetable  Academic Staff  Create, update
timetable
10  Manage registration  Academic Staff  Control open and
window  close registration
window
11  Approve exceptions  Academic Staff  Manually approve
special case
12  Generate reports  Academic Staff  Export registration
and grade
distribution
13  Manage user accounts  System  manages user
Administrator  account
14  Send automated  Notification system  Send email confirm
notifications
7
• •  ^ GE  ENG  5:50 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Course Registration System
Main - Model  Browse course catalogue  LT (Submit registration request→Chi
9] UseCaseDiagram1 - Model1  Check prerequisites  Manage timetable  • Join waitlist
Academic Staff  • Manage registration window
• View enrolled roster
Manage registration window
«include•  • Track registration status
• Record grades
Approve exceptions
Submit registration request  • Release grades
• Manage timetable
• Generate reports
Track registration status  Generate reports  - system Administrator  • Manage user accounts
Lecturers  • Send automated notifications
View enrolled roster  • Browse course catalogue
• Approve exceptions
Manage user accounts
TOOLBOX  OK  EDITORS
Record grades  Notification system  • Styles
Use Cases  Send automated notifications  Font  Arial  13
i Package  Release grades  Color  • Inherit
• Use Case Subject  Line Style
• Use Case  Format
Actor  Label
(0]  [T]
Frame
Association
Alignment  cu
Directed Association
İ Generalization  • Properties
I Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  5:50 PM
US  4/18/2026
```

## [52:00]
**Nói:** rất đơn giản thôi xten là điều kiện đúng không là hành vi mà kiểu mở rộng có điều kiện không phải lúc nào cũng xảy ra được chưa anh em mở rộng có điều kiện thì nghĩa là sao nếu mà lớp gửi cái này đi này lớp mà lại đầy mình kéo nhỏ này lại kéo này thì cái này tí nữa đúng không phải khi mà lớp đời đúng không đó thì nó sẽ nhắm sinh viên vào trong danh khách trở đúng không nó vậy thì cái này nó chính là cái điều kiện này mở rộng này thì đây nó sẽ lấy xe này
**Màn hình:**
```
*  • StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
8 Main - Model  6B  T (Submit registration request→Chi
9] UseCaseDiagram 1 - Modell  • Join waitlist
Course Registration System
• Manage registration window
Browse course catalogue  • View enrolled roster
Check prerequisites  Manage timetable
• Track registration status
Student  Academic Staff  • Record grades
«include»  Manage registration window  • Release grades
• Manage timetable
Approve exceptions  • Generate reports
Join waitlist  Submit registration request  • Manage user accounts
• Send automated notifications
Track registration status  - System Administrator  • Browse course catalogue
Generate reports
Lecturers  • Approve exceptions
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
Actor  Label
(0]  [T]
Frame
_ Association
Alignment  cu
Directed Association
İ Generalization  • Properties
Dependency  Course Registration Sy:
If Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
C  ENG  Ф)  5:50 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  (Submit registration request→Che
9] UseCaseDiagram1 - Modell  MI  • Join waitlist
Course Registration System
• Manage registration window
Browse course catalogue  • View enrolled roster
Check prerequisites  Manage timetable
• Track registration status
Student  Academic Staff  • Record grades
Manage registration window  • Release grades
circuse
• Manage timetable
Join waitlist  Approve exceptions  • Generate reports
Submit registration request  • Manage user accounts
• Send automated notifications
Track registration status  - System Administrator  • Browse course catalogue
Generate reports
Lecturers  • Approve exceptions
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Send automated notifications  Line Style
Release grades
• Use Case  Format
Actor  Label
[0)  [T]
Frame
• Association
Alignment  ol-  cu
Directed Association  dijo
i Generalization  • Properties
I Dependency  Course Registration Sy:
= Include  stereotype
B Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  5:50 PM
US  4/18/2026
```

## [52:30]
**Nói:** nó kia chưa à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à à là từ cái xe này thì cái này ở trên bấm nhầm đây em nhá mình sẽ phải nói đây đó như này đứng nguyên
**Màn hình:**
```
*  • StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
8 Main - Model  6B  (Submit registration request→Chi
9] UseCaseDiagram 1 - Modell  • Join waitlist
Course Registration System
• Manage registration window
Browse course catalogue  • View enrolled roster
Check prerequisites  Manage timetable
• Track registration status
Student  Academic Staff  • Record grades
Manage registration window  • Release grades
circuse
• Manage timetable
Join waitlist  Approve exceptions  • Generate reports
Submit registration request  • Manage user accounts
• Send automated notifications
Track registration status  System Administrator  • Browse course catalogue
Generate reports
Lecturers  • Approve exceptions
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Font  Arial  13
• Use Case Subject
Record grades  Notification system  • Inherit
• Use Case  Color
Send automated notifications  Line Style
9 Actor
Release grades
Format
El Frame
Label
/ Association
(0]  [T]
I Directed Association
J Generalization  Alignment  al-  cu
* Dependency
: Include  • Properties
El Extend  Course Registration Sy:
Annotations  stereotype
i Modell  Course Registration System [UMLUseCaseSubject)  80%
C  ENG  5:50 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
5 Main - Model  ET (Join waitlist→Join waitlist)
8] UseCaseDiagram1 - Modell  MI  • Manage registration window
Course Registration System  • View enrolled roster
Browse course catalogue  • Track registration status
Check prerequisites  Manage timetable
• Record grades
Student  Academic Staff  • Release grades
Manage registration window  • Manage timetable
• Generate reports
Join waitist 01 D  Approve exceptions  • Manage user accounts
Submit registration request  • Send automated notifications
• Browse course catalogue
Track registration status  System Administrator  • Approve exceptions
Generate reports
Lecturers  • 7 Student
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Properties
• Use Case Subject  name
Record grades  Notification system  source
• Use Case  • Join wartlist
Send automated notifications  target  • Join waitlist
% Actor
Release grades
stereotype  Q
El Frame
visibility  public
_ Association
condition
1 Directed Association
extensionLocations -
4 Generalization
• Documentation
Dependency
ET Include
ET Extend
Annotations
is Modell  Course Registration System  • Join waitlist  Ef (UMLExtend)
ENG  Ф)  5:51 PM
US  4/18/2026
```

## [53:00]
**Nói:** nhau đó thì cái này nó sẽ là gì nó sẽ là cái y4 này xe thế này như là chỉ khi khoa học mà đầy chỉ tiêu không có nghĩa là khi mà đầy chỉ khi mà không có đầy đúng không thì mới có thể là vào được này ở trên nha đó nhớ cho mình nhá Ừ ok rồi đó Vậy thì là cái này nói tên đúng không thì còn
**Màn hình:**
```
*  • StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
8 Main - Model  • Manage registration window
9] UseCaseDiagram1 - Modell  • View enrolled roster
Course Registration System  • Track registration status
Browse course catalogue  • Record grades
Check prerequisites  Manage timetable
• Release grades
Student  Academic Staff  © Manage timetable
Manage registration window  • Generate reports
• Manage user accounts
Join waitlist  Approve exceptions  • Send automated notifications
Submit registration request  • Browse course catalogue
• Approve exceptions
Track registration status  System Administrator  & Student
Generate reports
Lecturers  • (Student-Browse course catalogue
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts
• Use Case Subject
Record grades  Notification system
• Use Case
Send automated notifications
% Actor
Release grades
2 Frame
Association
Directed Association
- Generalization
Dependency
=
Include
Ef Extend
Annotations
80%
ENG  Ф)  5:51 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
8 Main - Model  ET (Join waitlist→Submit registratior
2] UseCaseDiagram 1 - Modell  • Manage registration window
Course Registration System  • View enrolled roster
Browse course catalogue  • Track registration status
Check prerequisites  Manage timetable
• Record grades
Student  Academic Staff  • Release grades
Manage registration window  • Manage timetable
• Generate reports
Join waitlist  Approve exceptions  • Manage user accounts
Submit registration request  • Send automated notifications
• Browse course catalogue
Track registration status  - System Administrator  • Approve exceptions
Generate reports
* Student
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Font  Arial  13
• Use Case Subject
Record grades  Notification system  • Inherit
• Use Case  Color
Send automated notifications  Line Style
% Actor
Release grades  =i l
Format
El Frame
Label
_ Association
(0)  [T)
I Directed Association
¡ Generalization  Alignment  al-  cu
Dependency  dijo
= Include  • Properties
eT Extend  Course Registration Sy:
Annotations  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  5:51 PM
US  4/18/2026
```

## [53:30]
**Nói:** một cái nữa nữa này thì là cái nằm trên này rồi xin nghe cái này chưa Thì cái này nó sẽ xảy ra khi nào nó nghe thì chắc chắn rồi anh em nhìn anh em đọc cái này chỗ gửi thông báo tự động này đây đây nhé đây khi mà lúc lúc đầy nhắm vào danh sách chờ này sau đó thì sao thì khi mà cái thằng này
**Màn hình:**
```
*  • StarUML (TRIAL MODE)
File  Edit  Format  Model  Tools  View  Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Course Registration System
3 Main - Model  Browse course catalogue  ET (Join waitlist→ Submit registratior
9] UseCaseDiagram 1 - Modell  Manage timetable  • Manage registration window
^  Check prerequisites
Academic Staff  • View enrolled roster
Manage registration window  • Track registration status
• Record grades
«extend»  • Release grades
Join waitlist  Approve exceptions
Submit registration request  • Manage timetable
• Generate reports
• Manage user accounts
^  Track registration status  Generate reports  - System Administrator  • Send automated notifications
Lecturers  • Browse course catalogue
View enrolled roster  • Approve exceptions
* Student
manace user accounts
TOOLBOX  OK  EDITORS
Record grades  Notification system  • Styles
Send automated notifications  Font  Arial  13
• Use Case Subject
Release grades  Color  • Inherit
• Use Case
Line Style
% Actor
Format
El Frame
Label
_ Association
(0]  [T]
I Directed Association
4 Generalization  Alignment  al-  cu
* Dependency  • go
in Include  • Properties
eT Extend  Course Registration Sy:
Annotations  stereotype
a Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  5:51 PM
US  4/18/2026
```
**Màn hình:**
```
cốc cốc  Luyện tập Q2 - Google Doc X  +  La  ..
docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  I CO
88  • Tất cả dấu trang
Luyện tập Q2 *  +
E  C -  Share
File Edit View Insert Format Tools Extensions Help
Q  100% -  Normal text •  Arial  +  B  I
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
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
future years.
Question 2: UC Modeling (1.5 points)
E  ENG  5:52 PM
US  4/18/2026
```

## [54:00]
**Nói:** mà được thấy vào lớp này thì sẽ hệ thống sẽ auto thông báo đúng không và tự động cho cái thằng này cái danh sách đó thì cái này nhá nó phải liên quan anh em nhìn này nhá thì em có phải thấy nó liên quan là từ cái thằng này không với cái thằng thằng quên đi theo thì cái là sao khi mà có chú chống ấy thì thế nào hệ thống tự động thông báo cho thằng sinh viên trong danh sách trong sinh viên đầu danh
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model  Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Modet  Ef (Join waitlist→Submit registration
9] UseCaseDiagram1 - Modelt  MI  • Manage registration window
Course Registration System  • View enrolled roster
Browse course catalogue  • Track registration status
Check prerequisites  Manage timetable
• Record grades
Student  Academic Staff  • Release grades
Manage registration window  • Manage timetable
• Generate reports
Join waitlist  Approve exceptions  • Manage user accounts
Submit registration request  • Send automated notifications
• Browse course catalogue
Track registration status  System Administrator  • Approve exceptions
Generate reports
* Student
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Font  Arial  13
• Use Case Subject
Record grades  Notification system  • Inherit
• Use Case  Color
Line Style
% Actor  Send automated notifications
Release grades
Format
• Frame
Label
Association
()  (a]  [O]  [T]
Directed Association
* Generalization  Alignment  al-  cu
/ Dependency
if Include  • Properties
ef Extend  Send automated notificat
Annotations  stereotype
E Modell  • Course Registration System  send automated notilications [UMLUseCase]
E  ENG  ф)  5:52 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  ET (Join waitlist→Submit registratior
2] UseCaseDiagram1 - Modell  MI  • Manage registration window
Course Registration System  • View enrolled roster
Browse course catalogue  • Track registration status
Check prerequisites  Manage timetable
• Record grades
Student  Academic Staff  • Release grades
Manage registration window  • Manage timetable
• Generate reports
Join waitlist  Approve exceptions  • Manage user accounts
Submit registration request  • Send automated notifications
• Browse course catalogue
Track registration status  System Administrator  • Approve exceptions
Generate reports
% Student
Lecturers
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
• Use Case Subject  Arial  13
Record grades  Notification system  • Inherit
• Use Case  Color
9 Actor  Line Style
Release grades  Send automated notifications
Format  =i l
2] Frame
Label
I Association
(0)  ET]
Directed Association
¡ Generalization  Alignment
* Dependency
= Include  • Properties
ei Extend  Send automated notificat
Annotations  stereotype
i Modell  • Course Registration System  Send automated notifications [UMLUseCasel
ENG  5:52 PM
US  4/18/2026
```

## [54:30]
**Nói:** sách đúng không đó thì có phải là mình sẽ có mình sẽ có là từ thằng này mình sẽ có lại tên với cái Đó, đây này Đó, ok chứ anh em Đó, đó là mình quan hệ nha Đó Ok chứ anh em Đấy chưa, đó Thì ở đây Cái này thì Ok, xong rồi
**Màn hình:**
```
*  • StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  ET (Join waitlist→ Submit registration
9] UseCaseDiagram 1 - Modell  MI  • Manage registration window
Course Registration System  • View enrolled roster
Browse course catalogue  • Track registration status
Check prerequisites  Manage timetable
• Record grades
Student  Academic Staff  • Release grades
Manage registration window  • Manage timetable
circles
• Generate reports
Join waitlist  Approve exceptions  • Manage user accounts
Submit registration request  • Send automated notifications
• Browse course catalogue
Track registration status  System Administrator  • Approve exceptions
Generate reports
Lecturers  * Student
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Font  Arial  13
• Use Case Subject
Record grades  Notification system  • Inherit
• Use Case  Color
Line Style
9 Actor  Send automated notifications
Release grades
Format
Frame
Label
Association
(0)  [T]
I Directed Association
4 Generalization  Alignment  cu
Dependency  djo
if Include  • Properties
ef Extend  Send automated notificat
Annotations  stereotype
i Modell  • Course Registration System  Send automated notifications [UMLUseCase]  80%
C  ENG  Ф)  5:52 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
8 Main - Model  ET (Send automated notifications».
2] UseCaseDiagram 1 - Modell  MI  • Browse course catalogue
Course Registration System  © Approve exceptions
Browse course catalogue  * Student
Check prerequisites  Manage timetable
(Student-Browse course catalogue
Student  Academic Staff  (Student-Check prerequisites)
Manage registration window  / (Student-Submit registration reque
(Student-Join waitlist)
Join waitlist  Approve exceptions  (Student-Track registration status)
Submit registration request  7 Lecturers
• (Lecturers-View enrolled roster)
Track registration status  System Administrator  • J (Lecturers-Record grades)
Generate reports
Lecturers  (Lecturers-Release grades)
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
• Use Case Subject
Record grades  Notification system
• Use Case
% Actor  Send automated notifications
Release grades
El Frame
_ Association
I Directed Association
¡ Generalization
Dependency
= Include
ef Extend
Annotations
80%
ENG  ф)  5:53 PM
US  4/18/2026
```

## [55:00]
**Nói:** Đó, thì bây giờ mình sẽ Nhìn qua lại một chút Ok, anh em lại chờ một chút Ok mình sẽ tiếp tục nói anh em nhé Mình cứ bị gián đoạn anh em ạ Ok vậy là bài này như này là coi như là xong anh em nhé Bài này đến đây là xong anh em nhé Bởi vì sao mình nói vậy Thực ra bài này ấy Khi mà mình đọc đề anh em ạ Thì bài này khi mà đọc đề ấy Mình không thấy có chỗ nào ấy Nó nói về việc là Là có một cái thằng nào đấy Bao hết Nghĩa là nó sẽ không có cái
**Màn hình:**
```
6 *  ASE 418/2026  5:58 PM
```
**Màn hình:**
```
cốc cốc  Luện tập Q2 - Google Doc  +  Ca
< >  C  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  I CO
88  • Tất cả dấu trang
Luyện tập Q2 #  +
E  0 -  Share
File Edit View Insert Format Tools Extensions Help
Q  100% -  Normal text >  Arial  +  B  I
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
The interface must be accessible on both desktop and mobile browsers and must conform to
WCAG 2.1 Level AA accessibility standards. The architecture should also support horizontal
scaling so that additional server capacity can be added smoothly as student numbers grow in
ENG  5:59 PM
US  4/18/2026
```

## [55:30]
**Nói:** Generalization Nghĩa là cái kế thừa anh em nhé Bởi vì sao mình nói vậy Bởi vì là nếu mà bình thường ấy thì anh em nhìn nhá nếu mà chỗ này mà dùng để vẽ cái generalization cũng được thôi bởi vì là cái thằng system administrator administrator này này thì nó thế nào? thì nó lại có cái là quản lý tất cả các tài khoản user nếu mà thằng này có thể quản lý tất cả tài khoản user thì lại
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
23) Main - Model  Ef (Send automated notifications→.
2] UseCaseDiagram1 - Modell  MI  • Browse course catalogue
Course Registration System  • Approve exceptions
Browse course catalogue  * Student
Check prerequisites  Manage timetable
(Student-Browse course catalogue
Student  Academic Staff  (Student-Check prerequisites)
Manage registration window  • (Student-Submit registration reque
(Student-Join waitlist)
Join waitlist  Approve exceptions  (Student-Track registration status)
Submit registration request  * Lecturers
•I (Lecturers-View enrolled roster)
Track registration status  Generate reports  System Administrator  (Lecturers-Record grades)
Lecturers  I (Lecturers-Release grades)
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
• Use Case Subject
Record grades  Notification system
• Use Case
7 Actor  Send automated notifications
Release grades
Bl Frame
Association
1 Directed Association
¡ Generalization
- Dependency
i Include
ET Extend
Annotations
ENG  5:59 PM
US  4/18/2026
```
**Màn hình:**
```
*  • StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  ET (Send automated notifications».
9] UseCaseDiagram 1 - Modeli  MI  • Browse course catalogue
Course Registration System  • Approve exceptions
Browse course catalogue  * Student
Check prerequisites  Manage timetable
(Student-Browse course catalogue
Student  Academic Staff  (Student-Check prerequisites)
Manage registration window  (Student-Submit registration reque
«extend»  (Student-Join waitlist)
Join waitlist  Approve exceptions  (Student-Track registration status)
Submit registration request  } Lecturers
• (Lecturers-View enrolled roster)
Track registration status  System Administrator  • _ (Lecturers-Record grades)
Generate reports
Lecturers  (Lecturers-Release grades)
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
• Use Case Subject
Record grades  Notification system
• Use Case
9 Actor  Send automated notifications
Release grades
El Frame
Association
1 Directed Association
* Generalization
Dependency
if Include
ET Extend
Annotations
80%
ENG  Ф)  5:59 PM
US  4/18/2026
```

## [56:00]
**Nói:** nó cũng không rõ lắm nói chung là cái này ấy thì thường là nếu mà để có cái Nếu mà có thể nhá Có thể nó sẽ như này anh em nhá Nó sẽ là cái thằng Thằng sinh viên và giảng viên này Nó sẽ đều là con Và cả thằng này nữa đều là con của Cái thằng này Được chứ anh em Thì lúc đấy mình sẽ vẽ được cái kế thừa Tuy nhiên thì bài này nó cũng không bảo bắt buộc Cho nên là mình cũng không cần vẽ vào thêm anh em nhá Cái này nó không bắt buộc nên là mình chả vẽ thêm Mà chính trong coserai anh em nhá
**Màn hình:** (không đổi)

## [56:30]
**Nói:** Nó cũng không bắt buộc Được chứ anh em thì thường ấy, nếu mà để cho nó mà chắc chắn nhất ấy, thì là mình sẽ có thêm một cái tờ nữa ở đây này mình sẽ đặt nó là regist đây này nhưng mà lúc mình nói với anh em cái cái lý thuyết ấy thì ví dụ mình để như này thì tất cả mấy thằng này đều là con của thằng này tất cả mấy thằng này là con của thằng này và thằng này nó sẽ đập vào cái login
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  ET (Send automated notifications→.
91 UseCaseDiagram 1 - Modell  • Browse course catalogue
Course Registration System  • Approve exceptions
Browse course catalogue  * Student
Check prerequisites  Manage timetable
(Student-Browse course catalogue
Student  Academic Staff  J (Student-Check prerequisites)
Manage registration window  (Student-Submit registration reque
«extend»  (Student-Join waitlist)
Join waitlist  Approve exceptions  J (Student-Track registration status)
Submit registration request  } Lecturers
• (Lecturers-View enrolled roster)
Track registration status  System Adrinistrator  • J (Lecturers-Record grades)
Generate reports
Lecturers  I (Lecturers-Release grades)
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
• Use Case Subject
Record grades  Notification system
• Use Case
9 Actor  Send automated notifications
Release grades
# Frame
Association
Directed Association
* Generalization
Dependency
= Include
ef Extend
Annotations
80%
ENG  Ф)  6:00 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE  X
File  Edit Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
2 Main - Model  • (Academic Statt-Manage timetable
(Academic Staff-Manage registratic
19] UseCaseDiagram 1 - Modelt  MI
Course Registration System  (Academic Staff-Approve exceptior
Browse course catalogue  (Academic Staff-Course Registratio
Check prerequisites  Manage timetable  (Academic Staff-Generate reports)
Academic Staff  % System Administrator
Student
Manage registration window  J (System Administrator-Manage use
} Notification system
«extend»
Join waitlist  Approve exceptions  0) Constraint1
Submit registration request  • Operation1
7 Notification system
Track registration status  (Notification system-Send automa
Generate reports  System Administrator
& Registered user
Lecturers
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
Use Cases
i Package  Record grades  Notification system
• Use Case Subject
Release grades  Send automated notifications
• Use Case
} Actor
Frame
• Association
Directed Association
Registered user
i Generalization
Dependency
Et Include
^ -
80%
ENG  Ф)  6:00 PM
US  4/18/2026
```

## [57:00]
**Nói:** nhưng mà ở đây nó không có cái login là gì thì trên nha trên là không cần thiết trên nha đó nói chung là bài này không cần thiết được chưa Và như trong có sẽ là nó cũng không cần tiết cho nên là mình không nói nhiều vì cái này với anh em nhé Và bây giờ để anh em chắc chắn hiểu lại một lần nữa mình sẽ nói cho anh em quan hệ bởi vì có lẽ là cái khó nhất là cái quan hệ thôi Ok thì chỗ này nó sẽ như này em nhé Thì bây giờ nhé ví dụ đang như này không ạ Bây giờ mình xóa bọn mình mình nói lại mà thôi chả xóa nữa cái này đi nào bây giờ nhá anh em nhìn này anh em nhớ cho mình này in cơ lúc là gì là là bao gồm nó
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  • (Academic Statt-Manage timetable
J (Academic Staff-Manage registratic
9] UseCaseDiagram1 - Modell  MI
Course Registration System  (Academic Staff-Approve exceptior
Browse course catalogue  (Academic Staff-Course Registratio
Check prerequisites  Manage timetable  • (Academic Staff-Generate reports)
Academic Staff  * System Administrator
Student
Manage registration window  (System Administrator-Manage use
} Notification system
Join waitlist  Approve exceptions  0) Constraintl
Submit registration request  • Operation1
7 Notification system
Track registration status  (Notification system-Send automa
Generate reports  System Administrator
& Registered user
Lecturers
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
Use Cases
i Package  Record grades  Notification system
• Use Case Subject
Release grades  Send automated notifications
• Use Case
9 Actor
Frame
Association
T Directed Association
İ Generalization
I Dependency
• Include
80%
ENG  Ф)  6:00 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
5 Main - Model  • • Submit registration request
9] UseCaseDiagram 1 - Modelt  Ef (Submit registration request→Chi
Course Registration System  if (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist-Submit registratio
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
«extend»  • Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
Use Cases
i Package  Record grades  Notification system
• Use Case Subject
Release grades  Send automated notifications
• Use Case
2 Actor
Frame
_ Association
Directed Association
İ Generalization
Dependency
- Include
A-
80%
E  ENG  Ф)  6:17 PM
US  4/18/2026
```

## [57:30]
**Nói:** không anh em thêm dài nhập nhớ cho mình như này nhá là gì đó là khi mà mình sắp biết đúng không nó thì luôn luôn phải trách cái này thì mới gửi đi được rồi xin em anh em nhớ cho mình nhá để mà gửi cái cái quét này có gửi được cái đăng ký này thì phải kiểm tra điều kiện được chưa đó thì nghĩa là cái thằng này gọi thằng này được xin nhé mà gọi thì là mình sẽ nhắm mũi tên về đây nhớ cho mình
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
3 Main - Model  4 Submit registration request
9] UseCaseDiagram 1 - Modell  (Submit registration request-›Chi
Course Registration System  if (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist→ Submit registratio
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
«extend»  • Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»
Manage user accounts
Use Cases
i Package  Record grades  Notification system
• Use Case Subject
Release grades  Send automated notifications
• Use Case
? Actor
Frame
Association
Directed Association
İ Generalization
Dependency
1 Include
80%
ENG  ф)  6:17 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  4 O Submit registration request
9] UseCaseDiagram1 - Modell  if (Submit registration request→Chi
Course Registration System  if (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist-Submit registration
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
• Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  © Release grades
• Manage timetable
Track registration status  Generate reports  - System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»  • Styles
Manage user accounts
Use Cases  Font  Arial  13
• Package  Record grades  Notification system  • Inherit
Color
I Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
} Actor  Label
(01]  Er]
Frame
Association
Alignment
Directed Association
İ Generalization  • Properties
I Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
C  ENG  Ф)  6:17 PM
US  4/18/2026
```

## [58:00]
**Nói:** nhé để mà gửi được cái cái đăng ký này thì phải gọi thằng này chết cho nên mình dùng in cân lút thì luôn luôn phải gọi thằng này chết được chưa đó thì nghĩa là bao gồm mà thì nghĩa là sắp biết đồ chơi sẽ bao gồm điều kiện thì mới gửi đi được thì mình sẽ có cái nút vào mũi tên cắm như này đó rồi chưa Đấy là mình cũng luôn nhá quan hệ này tiếp theo là cái này không ạ thì em có nhớ cho mình ít tên không là nó sẽ mở rộng nó mở rộng là nó có điều kiện nó là có hoặc là không như là những
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  4 O Submit registration request
9] UseCaseDiagram1 - Modell  if (Submit registration request→Chi
Course Registration System  if (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist-Submit registratio
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
• Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  - System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»  • Styles
Manage user accounts
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
? Actor  Label
[O]  Er]
Frame
Association
Alignment
I Directed Association
İ Generalization  • Properties
Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
C  ENG  Ф)  6:18 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  4 O Submit registration request
9] UseCaseDiagram1 - Modell  if (Submit registration request→Chi
Course Registration System
if (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Manage timetable
Check prerequisites  (Join waitlist-Submit registration
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
• Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»  • Styles
Manage user accounts
Use Cases  Font  Arial  13
• Package  Record grades  • Inherit
Color
• Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
} Actor  Label
ET]
Frame
Association
Alignment
Directed Association
İ Generalization  • Properties
i Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
C  ENG  Ф)  6:18 PM
US  4/18/2026
```

## [58:30]
**Nói:** điều kiện đấy thì đây có phải là khu lớp thì mình mới có cái thằng à nhớ cho mình nhớ chiều mũi tên cắm lại cây chính như là sao ví dụ nhá Nếu mà không có cái danh sách chờ được chưa thì nó có người đi được không có câu trả lời là có nhá đúng không nó vẫn gửi được yêu cầu hàng gửi được cái đăng ký đi nhưng mà phụ nữ kệ thôi đúng không Nhưng mà bây giờ nó sinh ra cái này để làm gì như là có điều kiện này có hoặc không đúng không thì như là khi mà lớp mà đầy người rồi thì nó nhắm
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER  Q.
E Main - Model  6B  4 • Submit registration request
9] UseCaseDiagram 1 - Modell  Et (Submit registration request→Chi
Course Registration System
af (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist→ Submit registratio
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
«extend»  • Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  - System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»  • Styles
Manage user accounts
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
7 Actor  Label
(0]  [T]
Frame
Association
Alignment  al-
Directed Association
İ Generalization  • Properties
Dependency  Course Registration Sy:
L Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  6:18 PM
US  4/18/2026
```

## [59:00]
**Nói:** mũi tên được chưa đó và kiếm chiều cũng tên nó luôn trỏ vào cái thằng yêu cây chính là trên em nhớ cho mình nhá và tiếp theo này cái này tương tự như vậy nhá Thì giờ anh em nhìn nó luôn trỏ vào những cái chính nhé mũi tên luôn trỏ mấy cái chính đấy lý do mình nói sao như là bây giờ trong danh sách trời đúng không Nếu mà lớp mà đầy rồi đúng không đó khi mà nó sẽ gửi email tự động mà nó sẽ gửi cho thằng email cho thằng tự đầu tiên tự động gửi email cho thằng đầu tiên đúng không
**Màn hình:** (không đổi)

## [59:30]
**Nói:** đó thì có phải là có cái này cũng được mà không có cũng chả sao bởi vì nằm trong danh sách trời rồi mà cái việc là người không Nó là nhiều có thể có hoặc không đúng không cho nên là cái thằng yêu cây chính rất là thằng này đúng không Và cái này chỉ là điều kiện mở rộng ra có khi mình dùng ít em và cái mũi tên cắm vào cái yêu cây chính cái trường đó đó là cái này em cần nắm rõ cho mình nhé đó anh em có nhớ cái mẹo gì là nếu mà muốn chất cái gì đấy là đi kèm cái điều kiện bắt buộc
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
3 Main - Model  • • Submit registration request
91 UseCaseDiagram 1 - Modell  MI  If (Submit registration request→Chi
Course Registration System
if (Submit registration request→Chi
Browse course catalogue  • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist→ Submit registratior
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
«extend»  • Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  - System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
Manage user accounts  • Styles
Use Cases  Arial  13
Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
? Actor  Label
(0)  Er]
Frame
_ Association
Alignment
Directed Association
İ Generalization  • Properties
Dependency  Course Registration Sy:
Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  6:19 PM
US  4/18/2026
```
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
Main - Model  • • Submit registration request
8] UseCaseDiagram 1 - Modelt  Ef (Submit registration request→Chi
Course Registration System
= (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist→ Submit registration
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
• Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
Manage timetable
Track registration status  Generate reports  - System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»  • Styles
Manage user accounts
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
} Actor  Label
(0)  [T)
Frame
_ Association
Alignment  al-  cu
Directed Association
i Generalization  • Properties
Dependency  Course Registration Sy:
i Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  6:19 PM
US  4/18/2026
```

## [60:00]
**Nói:** Ừ đấy còn nếu mà có cái điều kiện có có không đây này thì mình sẽ dùng ít tên được xây nhau đó Ok đó Vậy thì đấy là cái bài bài này nhá Ừ ok mình sẽ chụp cái này lại này Ok mình sẽ nhắm vào đây cho anh em tham khảo nhé Ok vậy là mình đã hoàn thành xong trên nha Ừ ok vẫn nhìn rõ đó Ok vậy là mình đã hoàn thành xong bài hành nhá Ngoài ra thì còn rất nhiều bài
**Màn hình:**
```
• StarUML (TRIAL MODE)
File  Edit  Format  Model Tools View Window Debug Help
WORKING DIAGRAMS  *  MODEL EXPLORER
E Main - Model  4 Submit registration request
9] UseCaseDiagram1 - Modell  i (Submit registration request→Chi
Course Registration System
af (Submit registration request→Chi
Browse course catalogue  • • Join waitlist
Check prerequisites  Manage timetable
(Join waitlist→ Submit registratio
Student  Academic Staff  • Manage registration window
Manage registration window  • View enrolled roster
«extend»  • Track registration status
Join waitlist  Approve exceptions  • Record grades
Submit registration request  • Release grades
• Manage timetable
Track registration status  Generate reports  - System Administrator  • Generate reports
Lecturers  • Manage user accounts
TOOLBOX  EDITORS
View enrolled roster
«extend»  • Styles
Manage user accounts
Use Cases  Font  Arial  13
i Package  Record grades  Notification system  • Inherit
Color
• Use Case Subject  Line Style
Release grades  Send automated notifications
• Use Case  Format
2 Actor  Label
(a]  (0]  [T]
Frame
Association
Alignment  al-
Directed Association
İ Generalization  • Properties
Dependency  Course Registration Sy:
= Include  stereotype
i Modell  Course Registration System [UMLUseCaseSubject]  80%
ENG  Ф)  6:20 PM
US  4/18/2026
```
**Màn hình:**
```
cốc cốc  Luyện tập Q2 - Google Doc  +  La
→  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q  I CD
88  • Tất cả dấu trang
+
Luyện tập Q2 * @  () Saving...  „0 -  Share
File Edit View Insert Format Tools Extensions Help
Q  100% -  Normal text -  Arial  E#SE E :
Stusene  Ace Stall
Manage registracion window
Join waitist  Appeove exceptions
ок!  Track registrasion status  Sene ale fero  - System Administratse
Vien erited roster
wanace ueet acccont
Recoed graden  Notification aystem
Send automated ast/fications
^ G  ENG  6:20 PM
US  4/18/2026
```

## [60:30]
**Nói:** trên nhau đó Ok thì em thích luyện tập nhé Ok bây giờ nhé thì cho mình xin dừng lại đây thôi à
**Màn hình:**
```
Ở cốc cốc  •I Luện tập Q2 - Google Doc X  +  La ..
< > G  @ docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  Q = ®  • |  LIQ =
• Tất cả dấu trang
Luyện tập Q2 * •  +
=  / Share
File Edit View Insert Format Tools Extensions Help
100% -  Normal text -  Arial  = - 11 +  I A GRO  0 -
Ste  ENG 4) 4/18/2026  6:20 PM
```
**Màn hình:**
```
Ở cốc cốc  Luyện tập Q2 - Google Doc  +  La ..
< > C  docs.google.com/document/d/1fxrE5g9KHEHpPn6fyMTV_zTOIZC2jiKanzqsjBQcP5Q/edit?tab=t.0  110 =
88  • Tất cả dấu trang
Luyện tập Q2 * ®  +
. a-  Share
File Edit View Insert Format Tools Extensions Help
ascaAS  100% -  Normal text -  Arial  0 -
3  . 4
• •  lite  ^G EO  6:20 PM
US  4/18/2026
```
