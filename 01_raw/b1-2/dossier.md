# DOSSIER — b1-2

- file gốc: `YTSave_YouTube_Buoi-1-2-Luyen-prompt-AI-de-Trial_Media_G_le7-qZK64_002_720p.mp4`
- thời lượng: 31.4 phút
- nguồn: transcript tự động (Whisper) + OCR màn hình (Apple Vision), đều chạy offline

> **Độ tin cậy — đọc trước khi dùng:**
> `Nói:` là giọng giảng viên do máy nhận dạng, có thể sai thuật ngữ tiếng Anh.
> `Màn hình:` là chữ OCR từ khung hình, có thể sai vài ký tự nhưng bố cục đúng.
> Khi hai nguồn lệch nhau: **tin `Màn hình` cho tên class / thuộc tính / bảng / code**,
> **tin `Nói` cho lời giải thích và quy trình**. Timestamp là của video gốc.

---

## [00:00]
**Nói:** Ok, thế rồi anh em nhé, trong video này mình sẽ xử lý nốt phần B, cái phần dịch bản B của cái đề trial của anh em nhé. Ok, phần B như thế này nhé, và anh em nhìn qua yêu cầu này, vẫn tương tự thôi, thứ nhất là mình sẽ viết prompt này, review này, tìm ra bug này, và viết prompt để fix. Cái này anh em viết y như form của mình, tới nhau. thì bước đầu tiên này mình đã nói với anh em rất nhiều rồi đúng không
**Màn hình:**
```
Ở cc cốc  LUYỆN TẬP PROMT AI - GO-  +  La ..
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File  Edit View Insert Format  Extensions Help
asad  A 5 100% •  Normal text "  Arial  |- 11] +  BIUAORO  / Editing
2
=
public class RegistrationService {
public boolean registerStudent(Student student, Course course) {
// Check prerequisite
if (course. getPrerequisite() != null &&
Istudent.getCompletedCourses().contains(course.getPrerequisite())) {|
return true; // Bug 1
// Check available seats
if (course.getEnrolled() >= course.getMaxSeats()) { // Bug 2
return false;
4 of 5
// Enroll student and persist
course.getRoster().add(student);
registrationRepo.save(new Registration(student, course)); // Bug 3
return true;
Output format:
^ V 0  ENG  8:14 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
- >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  & ® | =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5 e  A § 100% -  Normal text -  Arial  | - 11] +  0 Editing
3  4  5  6
Output format:
Numbered list of issues
- Explain for each issue
Suggest fix each issue
2. Find bug (0.2)
Bug 1:
Code: return true;
Type: wrong return value
- Why: If student does not meet prerequisite, it should fail, but it return true
Bug 2:
- Code: If (course. getEnrolled) >= course.getMaxSeats(
Type: Logic error
Why: the code does not increase enrolled after a student register, so the number of student
Bug 3:
Code: registrationRepo.save(new Registration(student, course));  4 of 5
Type: data inconsistency
^ V O  ENG  8:14 PM
US
```

## [00:30]
**Nói:** bước đầu tiên khi anh em làm thì đó là anh em cứ viết theo đúng format của mình I am working cái gì đấy đúng không I am working on đúng không thì bây giờ nhé bước vào đây nào xử lý này đầu tiên này là mình sẽ có này không phần 1 mình sẽ review code nhé ok review code này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - GOC  +  La ..  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File  Edit View Insert Format  -OOS 1  Extensions Help
asc8 A S 100%-  Normal text -  Arial  | - [11] +  BI UA•  0 Editing
2  3  5  6 r..?
// Check available seats
if (course. getEnrolled() >= course.getMaxSeats()) { // Bug 2
return false;
I/ Enroll student and persist
course.getRoster().add(student);
registrationRepo.save(new Registration(student, course)); // Bug 3
return true;
Output format:
Numbered list of issues
- Explain for each issue
Suggest fix each issue
2. Find bug (0.2)
Bug 1:
- Code: return true;
Type: wrong return value
- Why: If student does not meet prerequisite, it should fail, but it return true
Bug 2:
- Code:  if (course.getEnrolled()>= course.getMaxSeats())
^ V Q  8:14 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  210 =
• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
.. -  & Share
File  Edit View Insert Format  Tools  Extensions Help
A § 100% -  Normal text  Arial  | - 11] +  • Editing
3  5  6
Bug 1:
Code: return true;
: Why: If student does nat meet prerequisite, it should fail, but it return tre  Type: wrong return value
Bug 2:
Code: if (course.getEnrolled() >= course.getMaxSeats))
Type: Logic error
Why: the code does not increase enrolled after a student register, so the number of student
is wrong
Bug 3:
Code: registrationRepo.save(new Registration(student, course));
Type: data inconsistency
4 of 5
Why: the method saves registration but it can not ensure that the course is updated, lack of
save course such as: courseRepo.save course):
^ V O  ENG  8:15 PM
US  4 415/2026
```

## [01:00]
**Nói:** ok bước đầu tiên này I am working cái gì đấy đúng không vậy nhé tôi sẽ viết luôn cho nhau xem I am working cái này anh em phải thuộc luôn nhé I am cooking on cost
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go: X  +  La ..  -
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  a Saving...  +
& Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 11+  в  / Editing
3  6 ч...?..
- Why: the method saves registration but it can not ensure that the course is updated, lack of
save course such as: courseRepo. save course);
3. Promt fix bug (0.1)
Base on the issue found, please rewrite the registerStudent) method correctly.
Requirement:
- Fix all logical errors
• following coding best practices
- Add comment to explain each fix
2. Kich bản B
5 of 5
4. Review code (0.2)
^ V O  ENG  8:15 PM
US  - 4 4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go:  +  La ..
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKeryQgqQ/edit?tab=t.0  | 1 =
88  C Tất cả dấu trang
LUYẸN TẠP PROMT AI * G 65 Saving...  +
=  & Share
File Edit View Insert Format Tools Extensions Help
a5c1% Normal tert a  Arial  - 11 +  BIVA ORDEVEET  0 Editing
1. Panguiemon  2  3  5
Fix all logical errors
=  following coding best practices
- Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
l am working |  Il
Cand  E0 ENG4 4/15/2026  8:15 PM
```

## [01:30]
**Nói:** được chưa where is change system nào bây giờ mình sẽ xem tiếp nhé phần B này nó yêu cầu cái gì phần B này đây nó vẫn là method thứ 2 thôi thì vẫn là using đâu nè nó sử dụng cái gì đây ok
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go X  +  La ..  -  X
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |  *1• =
88  C Tất cả dấu trang
LUYỆN TẠP PROMT AI # G 65 Saving....  +
=  & Share
File Edit View Insert Format Tools Extensions Help
as ca A S 100% - Normal text =  Arial  - 11+  BIVA ORDERET  0 Editing
4  6 T.l
Fix all logical errors
following coding best practices
- Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
1 am working on a Cautl
R2atg  8:15 PM
4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LIO =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
. e  Share
File Edit View Insert Format Tools  Extensions Help
aa10% Normal text a  Arial  -11+ BI UAOG#  E#BEEE X  Editing
T..!..
Scenario B - GradeService.java (0.5 points)
The following Java method belongs to the GradeService class. It should publish final grades
only when (1) the grading period is officially closed and (2) every enrolled student has a grade
on record. The code contains TWO logical bugs and ONE critical security vulnerability.
Java
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '' + courseld + "*** // Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) [ // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
8:16 PM
4/15/2026
```

## [02:00]
**Nói:** vẫn là sử dụng Java thôi thì vẫn là như cũ anh em nhé using đó I'm working on post registration system using Java đó and spring boot đó biết này không nhớ nhạc sau đó đi please review the following method cái này thì mình dẫn anh em
**Màn hình:**
```
Ớ cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  4I0 =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
â  share
File  Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  / Editing
4  6
Scenario B - GradeService.java (0.5 points)
The following Java method belongs to the GradeService class. It should publish final grades
only when (1) the grading period is officially closed and (2) every enrolled student has a grade
on record. The code contains TWO logical bugs and ONE critical security vulnerability.
Java
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = ' + courseld + '*' // Security bug
) getSingleResult);
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades).size() == course.getRoster).size()) {// Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
^ EQ  ENG  8:16 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | . =
88  D Tất cả dấu trang
LUYỆN TẠP PROMT AI # • 65 Saving....  +
=  & Share
File Edit View Insert Format Tools Extensions Help
aa00% Normal text  Arial  | - [11] +  BIVA ORDE VERTET  0 Editing
6 r.l
Requirement:
Fix all logical errors
: Add comment to explain each fix  following coding best practices
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Pleal
^ E Q  ENG 4) E 4/15/2026  8:16 PM
```

## [02:30]
**Nói:** rồi đúng không following method nói chung là 12 video đầu này thì mình cũng không biết rõ nhớ nhận cho em nhớ in the in the cái gì class có in the cái gì đấy class anh em nào nước lên xem cái gì nhá Đây anh nhìn thấy con này đúng không à in the great vai này bây giờ mình chỉ
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go-  +  La ..  X
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving...  +
=  . e -  & Share
File Edit View Insert Format Tools Extensions Help
aa100% Normal text  Arial  | - 11] +  BIVA ORDERET  0 Editing
bLULL  .......  ....  6  T..!.
Requirement:
Fix all logical errors
: Add comment to explain each fix  following coding best practices
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review dl
Il
AE Q d  8:16 PM
4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LIQ =
88  • Tất cả dấu trang
LUYỆN TẠP PROMT AI *  . c -  & Share
File Edit View Insert Format  Extensions Help
95c8A1%  Normal text -  Arial  - 11+  BIUAOOEO  E #PEE•EEX  / Editing
......7  4
).getSingleResult():
=
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) ( // Logical bug 1
retur "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) ( // Logical bug 2
return "Not all grades entered";
2 of 5
course.setGradesPublished(true);
return "Grades published";
Your tasks for Scenario B:
^ E 0  ENG  8:17 PM
US  4/15/2026
```

## [03:00]
**Nói:** đây là người sợ bài đó Ok chưa Đấy sao bước đầu tiên tiếp theo này giờ mới thớt có xuất bây giờ suốt cái gì ngành đầu dòng nhất đây bước nào này nó sẽ có cái gì anh em nhỉ Đây đầu tiên anh em nhìn đúng ở đây
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go: x  +  La ..  -  X
< → C ® docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  = |  LФ =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
=  & Share
File Edit View Insert  Format Tools  Extensions Help
a sca A S100% ~  Normal text -  Arial  -[11+  BIVA ODOECET  / Editing
1u....  2  3  56 7.?.
=
5of5 <
^ E Q  ENG  8:17 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< > C  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
• -  Share
File  Edit View Insert Format  Extensions Help
asca A S 100% - Normal text ~  Arial  | - 11] +  BIAO  Editing
4  5  6
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades () for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level Low/
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
Vich ban A
^ E  ENG  8:17 PM
US  4/15/2026
```

## [03:30]
**Nói:** xử lý từng cái đầu tiên là gì? là mình sẽ lấy code này từ dữ liệu từ database này tất cả học sinh này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  @ |  4I0 =
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
â  share
File  Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  | - 11] +  BIUAGE  Editing
only when (1) the grading period is officially closed and (2) every enrolled student has a grade
on record. The code contains TWO logical bugs and ONE critical security vulnerability.
Java
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = ' + courseld + "''* // Security bug  2 of 5
). getSing eResuit;
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) | // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
^ EQ  ENG  8:17 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go.  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  " CD  110 =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
Share
File  Edit View Insert Format  Tools  Extensions Help
Normal text -  Arial  | - 10.5 +  BIU A  / Editing
6
Scenario B - GradeService.java (0.5 points)
The following Java method belongs to the GradeService class. It should publish final grades
only when (1) the grading period is officially closed and (2) every enrolled student has a grade
on record. The code contains TWO logical bugs and ONE critical security vulnerability.
Java
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = + courseld +'***// Security bug
). getSingleResult);
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades).size() == course.getRoster().size()) {// Logical bug 2
return "Not all grades entered;
course.setGradesPublished(true);
return "Grades published";
^ E Q  ENG  8:18 PM
US  4/15/2026
```

## [04:00]
**Nói:** ok ok là hình ảnh làm như mình thôi anh em cứ lấy cho mình như mình nói làm đúng yêu cầu làm đúng như mình dẫn nhé không phải nghĩ nhiều chú thích gì thì em lấy cái đấy ok chưa
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  * ®  4I0 =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
Share
File  Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  - | - 10.5 +  / Editing
only when (1) the grading period is officially closed and (2) every enrolled student has a grade
on record. The code contains TWO logical bugs and ONE critical security vulnerability.
Java
public class GradeService {
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '' + courseld + '*** // Security bug
) getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) | // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
^ EQ  ENG  8:18 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  Lal
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • |  • 1Ф
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  • Saved to Drive  +
E  Share
File  Edit View Insert Format  Extensions Help
Q5 e  8A 8100%  Normal text  Arial  | - 10.5 +  BIUA 0O  Editing
the corrected Java method. Present the corrected code with an inline comment on each
=  fix. (0.1 point)
Scenario B — GradeService.java (0.5 points)
The following Java method belongs to the GradeService class. It should publish final grades
only when (1) the grading period is officially closed and (2) every enrolled student has a grade
on record. The code contains TWO logical bugs and ONE critical security vulnerability.  2 of 5
Java
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = ' + courseld + "'* // Security bug
). getSingleResult):
// Guard: grading period must-be closed first
if (Icourse.isGradingPeriodClosed()) | // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades).size() == course.getRoster).size()) {// Logical bug 2
return "Not all grades entered";
course setGradesPublished/tial:
^ E O  ENG  8:18 PM
US  4/15/2026
```

## [04:30]
**Nói:** xong đấy thì xin nha tiếp theo này tiếp theo gì do tác nó ta thì mình sẽ cho nó cái gì thứ nhất nó là mình sẽ yêu cầu nó là em nhìn đề nhé em
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go.  +  La ..
< > C  @ docs.google.com/document/d/1poVw0ljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • |  4I0 =
88  • Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
E  • -  Share
File Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  | - 10.5 +  BIA•  +  0 Editing
7  6 7... ?..
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
3 of 5
1. Kịch ban A
1. Context
2. goal
3.  code
4. output format
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the RegistrationService class
The method should:
^ E Q  ENG  8:18 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  =
• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving...  +
. -  & Share
File Edit View Insert Format Tools Extensions Help
Q 5 e  A § 100% - Normal text =  Arial  | - 10.5 +  BIVA ORDEREET  0 Editing
6
mey miiouno  tamaa vonioony.
Requirement:
Fix all logical errors
- following coding best practices
- Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the GradeService class
The method should:
Fetch course from database
Guard: grading period must be closed first
- Guard: all students must have a grade
Your rl
EQS Ф4/15/2026  8:19 PM
```

## [05:00]
**Nói:** để chỗ do nát này em nhìn đề nhé Nhìn kĩ này xem nó yêu cầu anh em cái gì nhé ta ta ba này trong đó thì có hai lỗi này hai lỗi này mới là cái điều kiện này là sai này và ở trên nha bây giờ có phải là mình sẽ có là viết đúng theo bản sách địa bàn nhé security này và
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  D Tất cả dấu trang
LUYÊN TẬP PROMT AI *  E () Saving..  +
& Share
File  Edit View Insert Format Tools Extensions Help
Q 5  a a A § 100% Normal text  Arial  - 10.5 +  BIUAOOEO  0 Editing
.....  6  . T..!..
. .........
=  Requirement:
Fix all logical errors
following coding best practices
: Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the GradeService class
The method should:
- Fetch course from database
Suard: grading period must be closed tirs
Guard: all students must have a grade
Your task:
^ EQ  ENG  8:19 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Gor  +
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  ICO  • 14
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
• -  Share
File Edit View Insert Format Tools  Extensions Help
95c8 AS 100% - Normal text -  Arial  | - 11] +  Editing
7  4  5  6
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades() for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low/  +
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
1. Kịch bản A
^ E  ENG  8:19 PM
US  4/15/2026
```

## [05:30]
**Nói:** thì là mình sẽ bám sát này nhá Ở đây mình sẽ có là gì mình sẽ có là file nô dịch cổ nô dịch cổ ero in the condition
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go:  +  La ..
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  * ®  • | D
88  • Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
E  • -  Share
File Edit View Insert Format  Extensions Help
asaaA 100% Normal text  Arial  | - 11] +  BIVA OBOE E*•E•E•E  0 Editing
4  5  6
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades() for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and/what the correct logig should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
N  CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
1. Kịch bản A
^  ENG  8:19 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI * • ( Saving...  +
=  & Share
File Edit View Insert Format Tools Extensions Help
Q 5  0 Normal tet n  Arial  I - 10.5 +  BIUAO  HPBEEEX  0 Editing
3  4  5  6
- Tollowing coding best practices
- Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the GradeService class
The method should:
- Fetch course from database
Guard: grading period must be closed firs
. Guard: all students must have a grade
Your task:
- Find logical arrors |
^ E Q  8:20 PM
US  4/15/2026
```

## [06:00]
**Nói:** anh em thứ hai là gì là mình sẽ cần xác định identify còn mình phải tiếp được phải cho nhưng mà thật ra identify identify identify any security đúng không security đúng không anh em nhìn ký đề nhé đám sát vào đây vào đây này security này đấy anh em bám sát nào thế mà bám sát vào đi mà dã rồi anh em nhé
**Màn hình:**
```
Ở cốc cốc  = l  LUYỆN TẬP PROMT AI - GOS  +  La ..  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI #  E " Saving..  +
=  & Share
File Edit View Insert Format Tools Extensions Help
asaaA 100% Normal text  Arial  | - 10.5 +  0 Editing
4  5  6  T..!..
- Tollowing coding best practices
- Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the Grade Service class
The method should:
- Fetch course from database
Guard: grading period must be closed firs
Guard: all students must have a grade
Your task:
Find logical grrors in the condition
^ E Q  ENG  8:20 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • | Ф  • 1Ф  =
• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
E  • -  Share
File  Edit View Insert Format Tools  Extensions Help
Normal text  Arial  | - 11] +  Editing
4  6
=
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades) for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
Kich han A
ENG  8:20 PM
US  4/15/2026
```

## [06:30]
**Nói:** sau đó thì sao chắc chắn rồi lại bám sát đúng như cái form đầu này của mình này nhé nhìn này tìm file check này thêm cái này vào nữa ok ok anh em nó và từ nhớ đọc một chút này bán sát đề và anh em nhớ bởi vì tùy đề đấy à
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go X  +  La ..  X
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI  +
. -  & Share
File Edit View Insert  Format  Tools  Extensions Help
Normal text -  Arial  | - 11] +  BIUAOOI  0 Editing
5
Guard: grading period must be closed first
- Guard: all students must have a grade
Your task:
Find logical errors in the condition
: Identfy any security
5 of5 <
8:20 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
c -  & Share
File Edit View Insert Format  OO S  Extensions Help
95010%  Normal text  Arial  |- _+  I  A  / Editing
1  3  4  5  6
3. Promt fix bug (0.1)
Base on the issue found, please rewrite the registerStudent() method correctly.
Requirement:
Fix all logical errors
: folowing coding best practices
- Add comment to explain each fix
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the GradeService class
The method should:
Fetch course from database
Guard: grading period must be closed first
Guard: all students must have a grade
Your task:
- Find logical errors in the condition
- Identify any security vulnerabilities  5 of5
^E luS Ф 4/15/2026  8:21 PM
```

## [07:00]
**Nói:** mô tả cách này Ok vậy thì cái này ý của nó là mình sẽ còn phải một cái nữa đó là gì đó là xác định cái mức độ rủi ro anh em nhé Cái này nhắc đến bảo vật anh em nhé Cái này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  @ Saved to Drive  +
. . -  & Share
File  Edit View Insert Format  Tools Extensions Help
Q5 e  8A S 100%  Normal text  Arial  - 11 +  BIUAOOEO  0 Editing
2 3  4  5  6 T.?.
=
// Check avallable seats
if (course. getEnrolled() >= course.getMaxSeats()) { // Bug 2
return false;
// Enroll student and persist
course.getRoster().add(student);
registrationRepo.save(new Registration(student, course)); // Bug 3
return true;
Il
Output format:
Numbered list of issues
- Explain for each issue
Suggest fix each issue
2. Find bug (0.2)
4 of 5
Bug 1:
- Code: return true;
Type: wrong return value
- Why: If student does not meet prerequisite, it should fail, but it return true
Bug 2:
- Code:  if (course.getEnrolled() >= course.getMaxSeats())  203
^ E 0  ENG  8:21 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • 10
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
Share
File Edit View Insert Format  Tools  Extensions Help
a5caA100%  Normal text  Arial  |- 11] +  Editing
6  7... ?
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades() for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability typf, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
1. Kịch bản A
1. Context
^ E  ENG  8:21 PM
US  4/15/2026
```

## [07:30]
**Nói:** ý cho nó là mình phải xác định cả cái mức độ rủi ro anh em nhé đó thì chỗ này mình sẽ nói rõ cho mình ra một chút nữa này này nhá thì mình sẽ có là sai có không ở ở mức độ rủi ro anh em level nó thì là lao hay là medium hay là hai
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  ICD
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
Share
File  Edit View Insert Format  Tools  Extensions Help
Normal text -  Arial  | - 11] +  BIUAGO  E X  Editing
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades() for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
1. Kịch bản A
1. Context
2.  goal
3. code
4. output format
ENG  8:21 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  D Tất cả dấu trang
LUYÊN TẬP PROMT AI * • S5 Saving....  +
.. -  & Share
File Edit View Insert Format Tools Extensions Help
Arial  | - 11] +  BIUA ORO  EHPBEEEX  / Editing
4  5  6 т...?..
Please review the following method in the Grade Service class
The method should:
- Fetch course from database
: Guard: al students must have a grade  Guard: grading period must be closed first
Your task:
- Find logical errors in the condition
- Identify any security vulnerabilities
- Check coding best practices
- Assign a risk level (Low /]
Caid  8:22 PM
4/15/2026
```

## [08:00]
**Nói:** hay là đi cổ nhé nhé đó anh em nhớ cho mình cái dạng này thì chưa nói cho mình sẽ chưa rất nhiều dạng để em nhớ mà mới cùng anh em thể để cho nó là sắp test được chưa Nói chung là cái này thì anh em tùy em nhé cứ đúng form là được chưa đúng form là được báo sát đề và đúng form là các vấn đề này chưa biết nhau gì như dờ ốp có copy bằng
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  E Saving...  +
. -  & Share
File  Edit View Insert Format Tools Extensions Help
Arial  | - 11] +  BIVA ORDEREET  0 Editing
5
Please review the following method in the GradeService class
=  The method should:
• Fetch course from database
Guard: grading period must be closed first
- Guard: all students must have a grade
Your task:
- Find logical errors in the condition
- Identify any security vulnerabilities
- Check coding best practices  - Assign a risk level (Low / Medium / hil
Zaid  ^ E 0  ENG  8:22 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  D Tất cả dấu trang
LUYÊN TẬP PROMT AI * • () Saving...  +
& Share
File Edit View Insert Format Tools Extensions Help
Arial  | - 11] +  BIUAOOEO  E#PEEEEX  0 Editing
4  5  6 T.?.
Please review the following method in the GradeService class
=  The method should:
- Fetch course from database
: Guard: al studenes must have a grace  Guard: grading period must be closed first
Your task:
- Find logical errors in the condition
- Identify any security vulnerabllties
- Check coding best practices  I
Assign a risk level (Low / Medium / high / Critical)
: Suggest a fix for each issue
Caid  AECENC  8:22 PM
4/15/2026
```

## [08:30]
**Nói:** ok sau tiếp theo là gì có xong rồi thì phút format đúng form mà làm anh em nhé đúng form Ok à bút format phát bút format gì copy luôn nhìn được trên ngang copy luôn ghi đằng trên này cho mình nhá đỡ phải nghĩ nhiều 5 list này x lên này và đấy anh em đó bài này thì nó còn thêm cái nữa
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  4 • =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  ( Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
Arial  | - 11] +  BIVA ORDEREET  0 Editing
4
Please review the following method in the GradeService class
The method should:
- Fetch course from database
Guard: grading period must be closed first
- Guard: all students must have a grade
Your task:
- Find logical errors in the condition
- Identify any security vulnerabllties
- Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Codel
203
^ E 0  ENG  8:22 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go:  +  La ..
< > G @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • |  LIQ =
88  • Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
E  • -  Share
File Edit View Insert Format Tools  Extensions Help
Normal text  Arial  -11+ BIUA0OE  E#SE E•E  E X  0 Editing
4......7 assistantio review pubusniorauestj or poin logical correciness and secumy  T...le
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
3 of 6
CÁCH LÀM
1. Kịch bản A
1.  Context
2.  goal
3.  code
4. output format
1. Review code (0.2)
IL am workino on a Course Registration System using Java and Sorino boot.
^  ENG  8:23 PM
US  4/15/2026
```

## [09:00]
**Nói:** lên này chỗ này nhé thêm cho mình cái nữa là cái thêm một cái nữa là cái mức độ rủi ro bởi vì cái này này mày có cái bảo mật được chưa nhé thì anh em sẽ nêu ra cho mình là thêm cái nữa là
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Goc  +  La -.  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  11• =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  80 10%  Normal text  Arial  |- 11] +  BIUA O#O  0 Editing
it course. get nrollea() >É course. getmaxseats() W Bug 2  5  6 T..T..
retum false:
// Enroll student and persist
course.getRoster().add(student);
registrationRepo.save(new Registration(student, course)); // Bug 3
return true;
Output format:
I Numbered list of issues
-  Explain for each issue
-  Suggest fix each issue
2. Find bug (0.2)
Bug 1:
Code: return true;
Type: wrong return value
Why: If student does not meet prerequisite, it should fail, but it return true
Bug 2:
Code: if (course.getEnrolled() >= course.getMaxSeats())
Type: Logic error
Why: the code does not increase enrolled after a student register, so the number of student
is wrong
^ E O  ENG  8:23 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  • Saved to Drive  +
. . -  & Share
File  Edit View Insert Format  Tools  Extensions Help
5 c aA 100% •  Normal text  Arial  - 11 +  BI U AO  E-#"-E•EEEX  0 Editing
4
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
- Explain for each issue I
- Suggest fix each issue
8:23 PM
4/15/2026
```

## [09:30]
**Nói:** bức độ rủi ro nhé Ok đấy mình cái bài mà liên quan đến bảo mật anh nhé đấy có cái tính bảo mật Ok đó Ok đấy là xong anh em nhé bán sát vào đi mà đấy là anh em đã được không phải hai rồi chưa khá đơn giản thôi nhé Ok phần 2 thích bất ừ
**Màn hình:**
```
Ở cỐc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving...  +
. . -  & Share
File  Edit View Insert Format  Tools Extensions Help
8A E 100%  Normal text  Arial  | - 11] +  0 Editing
4  5
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
- Explain for each issue I
- Rj
- Suggest fix each issue
8:23 PM
4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q5 e  84 10%  Normal text  Arial  | - 11] +  BI UAO  G F •  / Editing
3  4  5  6  T.. !
2. Kịch bản B
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
The method should: Wing metnoa in the graceservice case
• Fetch course from database
-  Guard: grading period must be closed first
- Guard: all students must have a grade
Your task:
Find logical errors in the condition
- Identify any security vulnerabilities
- Check coding best practices
Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;  5 of 6
public String publishGrades (String courseld) (
// Fetch course from database
Course course = (Course) em.createNativeQuery( |
"SELECT ' FROM courses WHERE id = "* + courseld + "'* // Security bug
).getSingleResult():
// Guard: grading period must be closed first
8:24 PM
```

## [10:00]
**Nói:** Facebook này mình sẽ có cái gì ở đây nhá Nhìn ký để này nhé Nhìn ký cái này đầu tiên này thì là anh em nhìn cái security này đúng không thì đầu tiên thì mình sẽ có là security bấm anh em anh em thường thôi anh em thì đi làm bất ngờ anh như này cũng được cho anh em security bất hiểu vậy
**Màn hình:**
```
Ớ cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  E Saving...  +
& Share
File  Edit View Insert Format  Tools Extensions Help
9510%  Normal text  Arial  | - 11] +  BI UAOGAO  0 Editing
// Guard: ali students must have a grade  5  6 r..?..
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
retur "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
4. Find bug (0.2)
203
zald  ^ E O  ENG  8:24 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go-  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  C• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving...  +
.. -  & Share
File  Edit View Insert Format Tools Extensions Help
A 5 100% -  Normal text  Arial  -11 +  UA O  G E  E-#S•E•E•EEX  0 Editing
2  4
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) ( // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
- Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bugl
AECENCE  8:24 PM
4/15/2026
```

## [10:30]
**Nói:** Ok ở đây nhá Ở đây mình sẽ có cái gì ở đây thì mình sẽ để là 3 phần đúng không 4 2 quên quên quên 2
**Màn hình:**
```
Ớ cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
8A 8 100%  Normal text  Arial  | - 10.5 +  G F  E #SE•EEEX  0 Editing
4  5  6 r.?.
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
- Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bugl
^ E 0  8:24 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E 65 Saving...  +
& Share
File  Edit View Insert Format  Tools Extensions Help
Normal text  Arial  | - 10.5 +  BI UA•  • E  E-#"-E•EEEX  / Editing
2  4
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) ( // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
-Numbered list of issues
- Explain for each issue
- Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
^ E Q  ENG Q 4/15/2026  8:25 PM
```

## [11:00]
**Nói:** và quay ok được chưa anh em 3 phần tương tự bậc 2 Ok đấy đầu tiên nhé phần 1 anh em nhìn luôn là cốt này phần này thì sao anh em nhỉ phần này thì anh em nhìn nhé cái chỗ này là cái chỗ lấy kiểu như anh em truy vấn dữ liệu ra thôi thì chỗ
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *• =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  a Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 10.5 +  BI UA•  GH •  / Editing
2  4  5
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
- Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code:
Type
203
^ E O  ENG  8:25 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go: X  +  La ..  X
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File Edit View Insert Format  Tools  Extensions Help
95c100  Normal text -  Arial  | - 10.5 +  BIVA ODO SRIET  0 Editing
......  3 4 5  6 T.l
return "Grades published";
I
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)  6 of 6
Bug 1: Security bug
EO ENG 44/15/2026  8:25 PM
```

## [11:30]
**Nói:** này cái loại của nó anh em cứ nhớ cho mình em nhớ luôn cho mình đó là gì đó là anh em để cho bài này anh em cái bài này anh em để ý này đọc đi đây này cái bài này có một cái rất quan trọng mình quên cho nhắc anh em em phải nhìn kỹ này đây nhá phần b này xác định này thì chưa anh em nhìn đặc biệt cho mình cái này này em security này thì nó phải bao gồm gì hai này mô tả cái mức độ rủi ro
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Arial  | - 10.5 +  BIUAO ORO  0 Editing
Identify any security vulnerabilities
- Check coding best practices
Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = " + courseld + "''' |/ Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) ( // Logical bug 1
return "Grades published";
^ E Q  ENG  8:25 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  " ®
• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
Share
File  Edit View Insert Format  Tools  Extensions Help
95c#A S 100% =| Normal text ~  Arial  | - 11] +  BILA GROE*  Editing
4  5  6
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishrades() for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
Kich hản A
G  ENG  8:26 PM
US  4/15/2026
```

## [12:00]
**Nói:** này nói được cho anh em đó cho nên là anh em nhìn nhớ cái bấm một bấm một là security bây giờ mình mình sẽ phải có cốt này, có thai này đúng không? và có thêm một cái nữa là bức độ rủi ro anh em tự đánh giá bức độ rủi ro nó nhé ok, thì ví dụ nhé anh em cứ nhớ luôn cho mình này, ví dụ ở trong bài này anh em nhớ ngay cho mình khi mà anh em thấy cái dòng này
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< > G  @docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File Edit View Insert  Format  Extensions Help
95c8A100%  Normal text -  Arial  - 11] +  G 0 Q  0 Editing
2  3  4  5
return "Grades published";
// Guard: all students must have a grade
if (course. getGrades().size() == course.getRoster().size()) { I/ Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list ofjissues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug  6 of 6
Code:
Type:  203
W/hud
^ E Q  8:26 PM
4/15/2026
```
**Màn hình:**
```
Ở côc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  D Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
. . -  & Share
File Edit View Insert Format  Tools  Extensions Help
asaa A S 100% =  Normal text -  Arial  | - 10.5 +  BIVA ORDEREIET  / Editing
4  5  6  T..T.
Please review the following method in the Grade Service class
The method should:
Fetch course from database
Guard: grading period must be closed first
: Guard: all students must have a grade
Your task:
- Find logical errors in the condition
- Identify any security vulnerabilities
Check coding best practices
Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '' + courseld + "" 7 Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) ( // Logical bug 1
8:26 PM
4/15/2026
```

## [12:30]
**Nói:** select sound dùng đây này anh em dán vào nhé dán vào đã, đây là cái cốt đã cốt này, cốt là nó như này cốt như này thì lỗi của nó là gì? anh em nhớ cho mình đó là FQL Injection để cho mình nhé mẹo đây anh em ạ ok đó FQL Injection tiếp theo là mức độ rủi ro anh em cứ ghi cho mình là critical được chưa đó critical và bây giờ anh em sẽ giải thích cái lỗi này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Goc  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Normal text -  Arial  | - 10.5 +  BIU  A D C AD  0 Editing
4  5  6 7...?.
Please review the following method in the Grade Service class
The method should:
Fetch course from database
Guard: grading period must be closed first
: Guard: all students must have a grade
Your task:
Find logical errors in the condition
- Identify any security vulnerabilities
- Check coding best practices
Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
I/ Fetch course from database
Course course = (Course)lem.createNativeQuery(
"SELECT * FROM courses WHERE id = " + courseld +  // Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
^ E Q  ENG  8:26 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  C• Tất cả dấu trang
LUYỆN TẬP PROMT AI * • S5 Saving..  +
& Share
File  Edit View Insert Format Tools  Extensions Help
Q 5  Normal text  Arial  | - 10.5 +  BIUAO  •  E#PE E EE X  / Editing
2  3  4  5
Output format:
-  Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "'*
Type: SQL injection
Risk level: Critlcal]
Why:
Bug 3: Security bug
- Code:
Type:
• Why:
Bug 3: Security bug
- Code:
Type:
- Why:
8:27 PM
4/15/2026
```

## [13:00]
**Nói:** được chưa anh em thì ở đây bây giờ ví dụ nhé cái cái việc là anh em nhìn vào cái lỗi này đi anh em nhìn này sẽ lấy sao rồi con có đúng không Xong lại có cái gì đấy quay ID đúng để điều kiện không tự nhiên là lấy tất cả từ tí có này mới điều kiện là ID bằng post ID này chưa Đấy là
**Màn hình:**
```
Ới cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E " Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
A 100%  Normal text  Arial  | - 10.5 +  BIUA O  •  0 Editing
2  3  4  5  6 T.!.
Output format:
Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
- Code: SELECT * FROM courses WHERE id = " + courseld + -
Type: SQL injection
Risk level: Critical
Why: |  Il
Bug 3: Security bug
- Code:
Type:
• Why:
Bug 3: Security bug
- Code:
Type:
- Why:
^ E O  8:27 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
. . -  & Share
File  Edit View Insert Format  Tools  Extensions Help
9 5 c a A § 100% = | Normal text -  Arial  | - 10.5 +  / Editing
3  4  6 7...?..
roar taon.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(|
"SELECT * FROM courses WHERE id = "' + courseld + "'' // Security bug
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
8:27 PM
```

## [13:30]
**Nói:** khi nó biết làm viết như này đúng không thì như nào ví dụ từ nhau để mình sao lấy ví dụ gì nó dễ cái này nó kiểu như là dữ liệu của người dùng mà nhập cái cốt ai đi này bảo ấy khi mà dữ liệu người dùng nhập khóa này đi vào thì nó sẽ được thêm trực tiếp và truy vấn sql được cho anh em thì ví dụ như
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Goc  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  * • =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
50 10% •  Normal text -  Arial  | - 10.5 +  BIUA•  0 Editing
3  4
rour iaon.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(|
"SELECT " FROM courses WHERE id = ™ + courseld + ™. / Security bug
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
^ E Q  8:27 PM
4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | | =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
. . .  & Share
File  Edit View Insert Format  Tools  Extensions Help
a scaA § 100% -  Normal text -  Arial  | - 10.5 +  BI UA O  G H  0 Editing
3  4  6 7...?..
roar luon.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT " FROM courses WHERE id = ''' + coursęld + "''' |/ Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
^ E Q  8:28 PM
4/15/2026
```

## [14:00]
**Nói:** có một cái thằng hacker đúng không Nó sẽ có thể chèn cái mã sql vào được cho anh em đó ví dụ nhé cho ví dụ nhé Ví dụ này ví dụ nhé chỗ này đi xuống này ví dụ này nha ví dụ mình có một cái ví dụ là mình tấn công cả lại sẽ nói về các bạn bạn nhé ví dụ này có ai đi nhé ví dụ cho này đâu Mình cho là 1.0001 ở đây nhé thì hoặc làm mình sẽ cho là o này hoặc là mình sẽ cho là một bằng một như này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Goc  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  * • =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
5 c A 8 100% •  Normal text -  Arial  | - 10.5 +  BI A•  0 Editing
3  4  6 T..!.
roar taon.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(|
"SELECT * FROM courses WHERE id = '' + courseld +**'' // Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
^ E Q  8:28 PM
US  4/15/2026
```
**Màn hình:**
```
Ở côc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  .L =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  • Saved to Drive  +
c -  & Share
File Edit View Insert Format  Tools  Extensions Help
asaaA 100% -  Normal text -  Arial  | - 10.5 +  BI U AO  E#GE E•E EX  0 Editing
2  3 4 5.
rour won.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(|
"SELECT * FROM courses WHERE id = '' + courseld + "''' // Security bug
courseld =1]
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
8:28 PM
4/15/2026
```

## [14:30]
**Nói:** thì lúc này chỉ vẫn nó sẽ thành cái gì lúc này nhá nhưng mà chỉ vẫn nó sẽ thành cái gì thì vẫn của nó lúc này nó sẽ thành cái gì nó phải là xe đất sao con có quay ID 1 hoặc 1 bằng 1 không nghĩa cái này lúc này nó sẽ có lại ID bằng này một hoặc là nó sẽ cho là một bằng một như này thì này tức là sao nó sẽ trả về cái gì nó sẽ trả về là tất cả có nhưng mà cái lúc này thì dữ liệu
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - GoC  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  G (5 Saving...  +
c -  & Share
File  Edit View Insert Format Tools Extensions Help  ~
Normal text  Arial  | - 10.5 +  G 0 Q  SPBEEX  0 Editing
3
rour tun.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery( |
"SELECT * FROM courses WHERE id = '' + courseld + '''' // Security bug
courseld =1' or "1)
).getSingleResult();
Lun.
// Guard: grading period must be closed first  203
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
^ E Q  ENG  8:28 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  L• =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  & Share
File  Edit View Insert Format  Tools  Extensions Help
asaaA S 100% -  Normal text  Arial  | - 10.5 +  BIUA0O0O  E #PEEEEX  / Editing
Tour ton.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(|
"SELECT * FROM courses WHERE id = '' + courseld + '''' // Security bug
courseld =1' or "1' = "1"
).getSingleResult();
^ E 0  8:29 PM
4/15/2026
```

## [15:00]
**Nói:** của nó đã bị nick ra ngoài rồi mà xinh em đó nghĩa là tất cả dữ liệu nếu mà đến này thì tất cả dữ liệu sẽ bị nick ra ngoài đấy nhỉ đó thì bây giờ mình sẽ thích bằng cách nào đó là mình sẽ phải cái truy vấn và mình sẽ nói chung là bây giờ nha mình cứ viết từ từ nhá tí nữa mình xử lý sau nói chung là mình có biết từng bước giải thích ở nha Như lấy mình nói là gì cái lỗi critical
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI• =
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
a sca A, § 100% -  Normal text  Arial  | - 10.5 +  BIVA ODESEET  0 Editing
3 4 5.
rour tun.
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery( |
"SELECT * FROM courses WHERE id = '' + courseld + ''' // Security bug
courseld =1' or "1' = "1"
).getSingleResult();
^ E Q  8:29 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  . =
C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  6 Saving..  +
. . -  & Share
File  Edit View Insert Format Tools Extensions Help
Q 5 e  A S 100% -  Normal text  Arial  - 10.5 +  BIVA ORDEREET  / Editing
3 4 5 6 x...?..
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "*
Type: SQL injection
Risk level: Critical
- Why:
Bug 3: Security bug
-  Code:
: Whe:  Type:
Bug 3: Security bug
- Code:  I
Type:
- Why:
6 of 6  203
8:29 PM
4/15/2026
```

## [15:30]
**Nói:** được sao bởi vì là đây user user input có ai đi nha trực tiếp vào được có khi direct direct thì sao thì nó sẽ là s được ép vào cái cái sql khi vấn được truyền nhập đó thì lúc này nào
**Màn hình:**
```
ớ cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
0a 100%  Normal text -  Arial  | - 10.5 +  BIUA OEOI  E"SSEEEEX  / Editing
2  6 r.l.
Output format:
Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "'''
Type: SQL injection  I O
Risk level: Critical
:why: l
A
Bug 3: Security bug
: Tope:  Type:
why:
Bug 3: Security bug
Code:
Type:
Why:
^ E Q  ENG  8:29 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  G 65 Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 10.5 +  BIUAO  E #SE EEEX  O Editing
2  3  4  5  6 T.?
Output format:
Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "''
Type: SQL injection
Risk level: Critical
: Why: User input (courseld) is directly
Bug 3: Security bug
Code:
. .  Type:
Why:
Bug 3: Security bug
Code:
Type:
Why:
8:30 PM
4/15/2026
```

## [16:00]
**Nói:** sau tất cả em in sách SQL Ok đấy em chỉ biết này thôi được chưa đó Ừ ok thì đấy là cái bắt đầu tiên nhá thì để mình
**Màn hình:**
```
Ởi cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  * • =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  a 65 Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
5a10%  Normal text -  Arial  | - 10.5 +  BI UA O  G F D  0 Editing
2  3  4  5  6 r.!.
Output format:
Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "'''
Type: SQL injection
Risk level: Critical
: Why: User input (courseld) is directy added into sal quesl
Bug 3: Security bug
..  Code:
Type:
Why:
Bug 3: Security bug
Code:
Type:
Why:
203
^ E Q  ENG  8:30 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La -.  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  B Saved to Drive  +
c -  & Share
File Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  | - 10.5 +  BI UA O  0 Editing
2  4  6 r..?.
Output format:
Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT • FROM courses WHERE id = " + courseld + "''
Type: SQL injection
Risk level: Critical
: Why: User input (courseld) is directly added into Sql query, so attacker can inject sQUl
Bug 3: Security bug
Code:
..  Type:
Why:
Bug 3: Security bug
Code:
Type:
Why:
^E Q  ENG - Q) E 4/15/2026  8:30 PM
```

## [16:30]
**Nói:** giải thích rõ hơn cho anh em có này có này thì chi tiết hơn thì mình sẽ nói thêm một chút đây thì chỗ này thì nếu mà đấy nhá anh em để ý cho mình này khi mình nói dây dấu này thôi khi mà em để cốt như này thì xinh em thì nó sẽ nào Tại sao cho em lỗi bảo mật mày vì sao nghĩa là nếu mà đến như này thì nghĩa là bạn lấy cái dữ liệu của người dùng nhập vào cái con anh như này ở
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
Normal text -  Arial  | - 10.5 +  BI UA O  G D  / Editing
2  4  5
Output format:
Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "''.
Type: SQL injection
Risk level: Critical
: Why: User input (courseld) is directly added into Sal query, so attacker can inject SQL
Bug 3: Security bug
..  Code:
Type:
Why:
Bug 3: Security bug
Code:
Type:
Why:
203
^ E O  ENG  8:30 PM
US  4/15/2026
```
**Màn hình:**
```
Ở côc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
c -  & Share
File Edit View Insert Format  Tools  Extensions Help
95010%-  Normal text -  Arial  | - 10.5 +  BIUAOGEO  EBESE E•E EX  / Editing
Tore io uic vouc.
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + "'' // Security bug
).getSingleResult():
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
8:35 PM
```

## [17:00]
**Nói:** trên em nghĩa là nó sẽ lấy cái dữ liệu mà người dùng nhập vào đúng không đó thì rồi nó sao rồi nó nó sẽ nối thẳng vào cái câu lệch kéo này nó xin đối thẳng với câu kéo này nó biết tại sao nó lại nguy hiểm vì là người dùng có thể là sẽ không phải nhập là cái ID nữa người dùng có thể là không phải nhập ID nữa đó mà nó sẽ là nhập một cái câu kéo giả mạo vào thì sao có nghĩa là sao nghĩa là bây giờ ví dụ nhé ví dụ như cái ví dụ lúc nãy của mình nếu mà mình để là con ID là bằng một nó ví dụ nhé
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
95010%  Normal text -  Arial  | - 10.5 +  BI UA OI  / Editing
TIOre 1o uic vouc.  6 T..?..
public class GradeService {|
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '' + courseld + "''* // Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (!course.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
203
^ E Q  ENG  8:35 PM
US
```
**Màn hình:**
```
Ở côc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  28A 8100%  Normal text -  Arial  | - 10.5 +  BIUA0O0O  0 Editing
Tere to ule vouc
public class GradeService (
private EntityManager em;  Entryman an Gradles satring course
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + "'' // Security bug
).getSingleResult();
// Guard: grading period must be closed first
a-
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
8:35 PM
```

## [17:30]
**Nói:** cho ví dụ nhá mình để có ai đi cái này nhá là bằng một Ok thì cái này an toàn đúng không nhập hay nhiều một vào thì cái này mình bình thường cái này an toàn đúng không Nhưng mà thay vì đó hay vì đó nó hay vì đó thì người dùng không nhập ai điều một nữa mà người dùng sẽ nhập là ai đi bằng bằng một cái kia kiểu mới khác em bằng này một này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
95010%  Normal text -  Arial  | - 10.5 +  BIUAO  0 Editing
4  5  6 T..?..
TIare 10 uic vouc.
public class GradeService {
private EntityManager em;
public String publishGrades(String courseld) (
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + "'* // Security bug
).getSingleResult();
// Guard: grading period must be closed first
a-
if (!course.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades(). size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
^ E 0  ENG  8:35 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
- >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
• Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
950A10-  Normal text  Arial  | - 10.5 +  BIUAOO#O  E#GE *E•E EX  / Editing
Trere io mie vouc.
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + ''' // Security bug
courseld = 1  Il
).getSingleResult();
a-
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
I/ Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
EQuSФ4/15/2026  8:36 PM
```

## [18:00]
**Nói:** như này chưa như là nối vào đấy o1 xong lại bằng này một cái nhạc một bằng một thì sao anh em thì nó luôn đúng không phải là nhân gì này ý đây
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
C Tất cả dấu trang
LUYÊN TẬP PROMT AI #  E 6 Saving....  +
& Share
File  Edit View Insert Format  Tools Extensions Help
9510%  Normal text  Arial  | - 10.5 +  BIUA OEO  0 Editing
5
Tore to uic vouc.
public class GradeService {
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + "'* // Security bug
courseld = "1  Il
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
^ E 0  ENG  HФ a  8:36 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  -
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E ") Saving...  . . -  & Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 10.5 +  BIUA O#O  / Editing
Tiure io vie UVUL.
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '' + courseld + "''* // Security bug
courseld ="1 or'1 = 1])
).getSingleResult();
a-
I/ Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
E9S415/2026  8:36 PM
```

## [18:30]
**Nói:** cái này nếu mà đưa vào query đưa vào cái truy vấn thì nó sẽ thành cái gì lúc này nó sẽ thành cách xe lịch sao nguy ai đi này đây em nhỉ Nó sẽ lúc này nó thành này này thay vì là nó cộng cái này nhá thì lúc này nó sẽ thành là như này nhá nó sẽ là quay ID này bằng này để xóa bỏ cho mình ai lúc này nó sẽ bằng 1 như này được chưa, 1 này và O, nó có cái toán từ O này luôn ấy 1 này
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI• =
C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  E 5 Saving...  +
c -  & Share
File  Edit View Insert Format  Tools Extensions Help
a saa A S 100% - Normal text *  Arial  | - 10.5 +  BIVA CEDEREET  / Editing
TIure io vie VViL.  5  6 T.?.
public class GradeService {
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + "'* // Security bug
courseld = "1 'or' 1'= 1"
).getSingleResult():
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade  203
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
^ E 0  ENG  HФ a  8:36 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
+ > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | | =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  ( Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
95 c8 A S 100% - Normal text -  Arial  | - 10.5 +  IBIUAOO E  EHE PE E EE X  0 Editing
Iu u.F  4 5 6 7...?..
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + "'' |/ Security bug
courseld = "1 'or' 1'= 1"
"SELECT * FROM courses WHERE id =1' OR)
a-
).getSingleResult();
I/ Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
ES 415/2026  8:37 PM
```

## [19:00]
**Nói:** bằng này 1 này, như này anh em nhé đó, nó sẽ thành lúc đấy, truy vấn lúc này nó sẽ thành cái này được chưa, nó thành cái này như thế nào điều gì sẽ xảy ra, nghĩa là sao 1 bằng 1 này anh em nhé thì cái 1 bằng 1 ấy, nó luôn đúng được chưa, nếu mà 1 bằng 1 nó luôn luôn đúng, thì nó sẽ như thế nào cái câu SEL nó sẽ lấy tất cả dữ liệu trong cái bảng COS này luôn chứ nó không lấy theo cái điều kiện là ID nữa được chưa anh em? 1 bằng 1 nó luôn đúng mà thì lúc này nó sẽ lấy theo
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - GOC  +  La ..  X
< > C  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  6) Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 10.5 +  BIUAOOEO  0 Editing
6 T.!.
- Assign a risk level (Low / Medium / high / Critical)
=  - Suggest a fix for each issue
Here is the Code:
public class GradeService {
private EntityManager em;
public String publishGrades(String courseld) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '' + courseld + "'* // Security bug
courseld = "1 'or' 1'= 1"
"SELECT * FROM courses WHERE id =1' OR *1" =|
a-
).getSingleResult():
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
^ E Q  ENG  8:37 PM
US  4/15/2026
```
**Màn hình:**
```
Ớ cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  & Share
File  Edit View Insert Format  Tools  Extensions Help
asaaA S 100% -  Normal text -  Arial  | - 10.5 +  BIUAOOEO  / Editing
3 4
Tou lun
Find logical errors in the condition
Identify any security vulnerabilities
Check coding best practices
- Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
Here is the Code:
public class GradeService (
private EntityManager em;
public String publishGrades (String courseld) {
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = "' + courseld + ''' // Security bug
courseld = "1 'or'1 '=' 1"
"SELECT * FROM courses WHERE id =1 OR 1 = 1 I
).getSingleResult();
^ E 0  8:37 PM
4/15/2026
```

## [19:30]
**Nói:** tất cả cái ID, lấy theo tất cả ID thì sao? nếu mà trong một cái hệ thống đúng không? mà nó lấy tất cả thông tin trong cái COS ra thì nó là thành cái gì? là thành cái lộ dữ liệu đúng không? đó, làm dò dỉ dữ liệu ấy thì chính vì vậy nó mình mới viết ở đây này user input bấm cái này vào trực tiếp vào thêm thì nó sẽ thêm truy vấn vào cái này thì cái thằng tấn công vậy nó có thể là nhìn rất ít rất kỹ thu nhau này thì xinh em đó thì nó là vì bản chất của cái này anh em nhé
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Goc  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E () Saving...  +
& Share
File  Edit View Insert Format Tools Extensions Help
asaaA 100%-  Normal text  Arial  | - 10.5 +  BIUA ORO  0 Editing
Guard: grading period must be closed first
Guard: all students must have a grade
Your task:
Find logical errors in the condition
- Identify any security vulnerabilities
- Check coding best practices
Assign a risk level (Low / Medium / high / Critical)
- Suggest a fix for each issue
public class GradeService (
private EntityManager em;
public String publishGrades(String courseld) (
I/ Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = " + courseld + '''' |/ Security bug
).getSingleResult(); I
// Guard: grading period must be closed first
^ E Q  ENG  8:37 PM
US  4/15/2026
```
**Màn hình:**
```
Ở côc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI *  . c -  & Share
File  Edit View Insert Format  Tools  Extensions Help  ~
Normal text -  Arial  | - 10.5 +  E-#"E-EEEX  / Editing
2  4  5  6 т...?.
Output format:
Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "'''
Type: SQL injection
Risk level: Critical
: Why: Uer input (coursell) is directly added into Sal query, so attacker can inject sa
Bug 3: Security bug
Code:
Type:
Why:
Bug 3: Security bug
Code:
Type:
Why:
8:38 PM
4/15/2026
```

## [20:00]
**Nói:** Ok anh em chờ mình một chút nữa mình sẽ quay lại ngay thôi mình phải giúp đi nhắn của bạn cái Ok bước thứ hai là cái này anh em nhé bây giờ anh em cứ làm từng bước có cái cục này vào có không? code này để xem anh em code này thì sao
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  4• =
C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  Normal text  Arial  | - 10.5 +  BIUAOOEO  0 Editing
Tkisk ever  3  4  5  6 T..?..
Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "'*
Type: SQL injection
Riay uetr neut coreal) areay ade mo sal uey o a tcer can ner sct
Bug 3: Security bug
- Code:
Type:
Why:
Bug 3: Security bug
- Code:
Type:
Why:
^ E O  ENG  8:38 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  4Ф =
C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving...  +
& Share
File Edit View Insert Format Tools Extensions Help
Q 5  A § 100% -  Normal text-  Arial  | - 10.5 +  BIVA ORDERIET  / Editing
6 T.?
2.  Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "!*
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
Code: | I
Type:
- Why:
Bug 3: Security bug
Code:
Type:
Why:
^ V Q  ENG  8:43 PM
US  4/15/2026
```

## [20:30]
**Nói:** thì chỗ này cái loại code của nó là gì? chắc chắn rồi nó có sẵn rồi anh em từ từ anh em thì cái code này cái này là thế nào đây cái cô này nhá thì nó loại của nó là gì là em lỗi nó là lỗi logic nhưng mà mình sẽ phải nói là cho mình phân tích lỗi trước đã nhá để biết nó là cái loại gì được cho nhá đó
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  3 Saved to Drive  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
8A 8 100%  Normal text  Arial  | - 10.5 +  BIUA ORO  0 Editing
2 ..  3  4  6 T..?..
2.  Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = "* + courseld + "'*
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sal query, so attacker can inject SQL
Bug 2: Security bug
-  Code:  if (Icourse.isGradingPeriodClosed()
Type:
- Why:
Bug 3: Security bug
Code:
Type:
: Why:
10...
^ V Q  ENG  8:43 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI0 =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
. c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
asaaA S 100% =  Normal text -  Arial  | - 10.5 +  BIUAO  EHPBEEEX  / Editing
2  4  5
Output format:
Numbered list of issues
Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = "' + courseld + "''.
Type: SQL injection
Risk level: Critical
: Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
Code: if (Icourse.isGradingPeriodClosed())
Type:
Why:
Bug 3: Security bug
Code:
Type:
Why:
8:44 PM
```

## [21:00]
**Nói:** thì bây giờ nhé anh em thì nhìn này đây nếu mà không có dấu khác này không Nếu mà chưa chưa đóng cái chấm điểm đúng không? đóng cái chấm điểm lại, đúng không? thì return cái nghĩa là công khai điểm điểm đã công khai thì nhìn phát anh em biết sai luôn, đúng không? chưa đóng chấm điểm mà đã công khai, đúng không? thì đây là lỗi, đúng không? vậy thì sai ở chỗ nào? sai ở chỗ này bỏ cái dấu chấm 2 này đi là sao?
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go-  +  La ..  X
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File Edit View Insert Format  Tools  Extensions Help
95c1%  Normal text -  Arial  | - 10.5 +  BI UA•  G 0 Q  0 Editing
3 4. L  5  6 r.!.
// Fetch course from database
Course course = (Course) em.createNativeQuery(|
"SELECT " FROM courses WHERE id = '' + courseld + "'' // Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
^ V Q  ENG  8:44 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |  L• =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  & Share
File Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  | - 10.5 +  BIUAOO#O  E HPBEEEX  / Editing
t..7  4
).getSingleResult();
// Guard: grading period must be closed first
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
}
// Guard: all students must have a grade
-  if (course.getGrades().size() == course.getRoster().size()) { I/ Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
8:44 PM
```

## [21:30]
**Nói:** vậy sai là sai cái gì? đúng không? vậy thì wrong mình có thể ghi là wrong condition là cái từ trên nhau đó mình đi là nếu mà có nếu mà cái này có thì nó bị tên mình kia nghĩa là sai rồi xanh đấm than đúng không Bây giờ mình sẽ viết như thế nào thì mình sẽ chỉ cần nói là nếu nếu mà g
**Màn hình:**
```
Ớ cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  11• =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  Normal text -  Arial  | - 10.5 +  BIVA ORDERET  0 Editing
reium urdues puirisicu?
Output format:
Numbered list of issues
Explain for each issue
Risk level
: Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = " + courseld + "*-
. .  Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directiy added into Sql query, so attacker can inject SQL
Bug 2: Security bug
Code: if (Icourse.isGradingPeriodClosed())
Type:
- Why:
Bug 3: Security bug
Code:
Type:
- Why:
^ V Q  ENG  8:44 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  O Saved to Drive  +
c -  & Share
File Edit View Insert Format Tools  Extensions Help
9 5c a A § 100% = | Normal text -  Arial  | - 10.5 +  BIUA O#O  B#ESE EE EX  / Editing
KisK lever  2  4  6 r...?..
Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT • FROM courses WHERE id = "" + courseld + "'*
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directiv added into Sal query, so attacker can iniect SQL
Bug 2: Security bug
Code: if (!course.isGradingPeriodClosed())
Type: Wrong condition
- Why: i I
Bug 3: Security bug
- Code:
Type:
Why:
E uS 4/15/2026  8:45 PM
```

## [22:00]
**Nói:** Reading is not closed đó Zen system xuất hiện xuất nó
**Màn hình:**
```
Ởi cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -
< →  C  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *1• =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving...  +
. -  & Share
File  Edit View Insert Format Tools Extensions Help  ~
0 100%  Normal text  Arial  | - 10.5 +  BA O  G 0 Q  / Editing
Kisk lever  4  5  6 7...?..
Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = ' + courseld + "'*
Bug 2: Security bug
- Code: if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
- Why: If gar
Bug 3: Security bug
- Code:
Type:
Why:
NE O ENG  Hc a  8:45 PM
US  4/15/2026
```
**Màn hình:**
```
Ở côc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  D Tất cả dấu trang
LUYỆN TẬP PROMT AI * • ( Saving....  +
c -  & Share
File Edit View Insert Format Tools Extensions Help  ~
Normal text  Arial  | - 10.5 +  BI UA O  E HPBEEEX  / Editing
KisK ever  2  3  4  5  6
Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = ™ + courseld + "'*
Type: SQL injection
isk level: Critica
Why: User input (courseld) is directiv added into Sal querv, so attacker can iniect SC
Bug 2: Security bug
Code: if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
- Why: If grading is not closed then system shol
Bug 3: Security bug
Code:
Type:
Why:
8:45 PM
```

## [22:30]
**Nói:** phát lịch great nói anh em nó nếu mà chưa đóng cái kia thì không được sau cái điểm ra đúng không bắt cốt return vì tôi cái gì vì tôi là công khai điểm của anh em đó đơn giản thôi nhé Ok sau đó ý hay rất đơn giản Ok tiếp theo nào đây
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI• =
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  6 Saving...  +
. g -  & Share
File  Edit View Insert Format Tools Extensions Help
a saaA S 100% -  Normal text  Arial  | - 10.5 +  BI UA•  G H •  / Editing
Kisk lever  4  5  6 7... ?..
Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = ' + courseld + "'*
Bug 2: Security bug
- Code: if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
- Why: If grading is not closed then system should not pl
Bug 3: Security bug
Code:
Type:
Why:
^ E Q  ENG  Hc a  8:45 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LIQ =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  3 Saved to Drive  +
. . .-  & Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  A E 100% -  Normal text  Arial  | - 10.5 +  BIU  A  E#PEEEEX  / Editing
3  5  6 7...?..
if (Icourse.isGradingPeriodClosed()) [ // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) ( // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published":  Il
Output format:
- Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE Id = " + courseld + ".-
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
ME CEN  8:46 PM
US  4/15/2026
```

## [23:00]
**Nói:** thứ ba này em nhìn cái bài này khá đơn giản thôi nó nó khác một tí ở chỗ này không Nhưng anh em xem này Ừ nếu đây anh em nhìn nhá lỗi thứ ba này này nó cổ bắp 2 này thì nó sẽ là cái gì thì nó đang có là nếu mà có chấm à Ok thì đây cho em nhìn nhá Cái này là cái gì cái này số lượng điểm số lượng đầu
**Màn hình:**
```
Ới cốc cốc  LUYỆN TẬP PROMT AI- Gos  +  La ..
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  1I• =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E Saving..  +
c -  & Share
File  Edit View Insert Format Tools Extensions Help
asaaA 100% -  Normal text  Arial  | - 10.5 +  BI A•  GF •  SPBEEX  / Editing
2  3  4  5  6 7...?..
2.  Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = ' + courseld + "'*
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sal query, so attacker can inject SQL
Bug 2: Security bug
Code: if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retum "Grades
published"; |
Bug 3: Security bug
Code:  Il
Type:
Why:
L0..
^ E Q  ENG  8:46 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - GO  +  La ..
+ > C  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
95caA100%  Normal text "  Arial  | - 10.5 +  BIUAOGEO  E#PE EEE X  0 Editing
2  3  6 r.l.
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course. getGrades(). size() == course.getRoster().size()) ( // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
- Code: SELECT * FROM courses WHERE id = " + courseld + "**
Tima. SOl iniectian
^ E Q  8:46 PM
```

## [23:30]
**Nói:** đúng không? em nhớ cho mình đây là số lượng đầu điểm có này là gì? như cái bài phần 2 mình đã nói với anh em rồi đó, cái này thì nó là cái gì? thì nó chính là cái danh sách đây là danh sách này danh sách lại còn chấm sai trong danh sách này có bao nhiêu thì nghĩa là sao? nghĩa là đây là số lượng điểm mà bằng số lượng sinh viên trong cái danh sách
**Màn hình:**
```
Ở cốc cốc  = l  LUYỆN TẬP PROMT AI - GOC  +  La ..  -  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
C Tất cả dấu trang
+
LUYỆN TẠP PROMT AI *  . -  & Share
File Edit View Insert Format  Tools  Extensions Help
asc810% -  Normal text  Arial  | - 10.5 +  B I UAOGEO  0 Editing
2  3  4  6 T...?..
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
// Guard: all students must have a grade
if (course.getGrades(). size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
- Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
- Code: SELECT * FROM courses WHERE Id = " + courseld + "-C
a. GAl inioction
^ E 0  ENG  Hc a  8:46 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  -  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI@ =
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
. a-  & Share
File  Edit View Insert Format  Tools  Extensions Help
Normal text "  Arial  | - 10.5 +  BIU AO  0 Editing
.u...7  6 T.l.
if (Icourse.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
I/ Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
Explain for each issue
Risk level
Suggest fix each issue
2. Find bug (0.2)
8:47 PM
4/15/2026
```

## [24:00]
**Nói:** số lượng điểm mà bằng số lượng sinh viên trong danh sách Thì lại trả về là không Chưa nhập Đúng không? Thì lại trả về là Tất cả đều chưa được nhập điểm Được chưa? Đó Quá vô lý rồi đúng không? Quá dễ rồi Đúng không? Câu này quá dễ rồi Được chưa? Nhìn phát ra luôn Thì cái này là gì? Code này, đầu tiên code này Có cái này đã Được chưa? Đó Type của nó là gì? Của nó là gì đây?
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -  X
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
. -  & Share
File Edit View Insert Format  Tools  Extensions Help
Normal text  Arial  - 10.5 +  BIUA•  G F D  0 Editing
2  3  4  5
if (!course.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
I/ Guard: all students must have a grade
if (course. getGrades(). size() == course. getRoster(), size()) { // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
Explain for each issue
Risk level
Suggest fix each issue
2. Find bug (0.2)
^ E Q  8:47 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go•  +  La ..
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  TL Ф =
88  C• Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E () Saving...  +
• e a-  & Share
File  Edit View Insert Format Tools Extensions Help
Q 5  Normal text  Arial  | - 10.5 +  BIUA0O E  E-#"•EEEEX  0 Editing
1  2  4  5
Code: SELECT * FROM courses WHERE id = " + courseld+"**
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
: Code: i (Course is GracingPeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retum "Grades
published"
Bug 3: Security bug
- Code:if (course.getGrades().size() == course.getRoster().size())|
Type:
- Why:
a-
AECNCC  8:47 PM
4/15/2026
```

## [24:30]
**Nói:** Là vẫn là wrong condition con lịch sử đó vẫn là con lịch sử sang điều kiện chưa Tại sao có nếu đây anh em nếu này nếu này người đó như mình có nói số lượng điện mà rồi mà bằng mà bằng số lượng tiêu đơn chưa Ừ thì sao thì thế nào nhớ là sao minh nhạc minh ongret
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  O Saved to Drive  +
• e a-  & Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  2100%  Normal text  Arial  | - 10.5 +  BIUAOOEO  E-#SE•EEEX  0 Editing
2  4  5  6 T.!
Code: SELECT * FROM courses WHERE id = " + courseld + '*.
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
: Code: ir (course is Gracing PeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retum "Grades
published"
Bug 3: Security bug
- Code:if (course.getGrades().size() == course.getRoster().size())
Type:
- Why:
^ E 0  ENG  8:47 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  | =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI * • S5 Saving...  +
. g -  & Share
File  Edit View Insert Format Tools Extensions Help
ascaA 100% •  Normal text -  Arial  | - 10.5 +  BIUAOO E  E-#Y•E•EEEX  0 Editing
2  4  5  6
Code: SELECT * FROM courses WHERE id = " + courseld + '**
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
- Code:  if (Icourse.isGradingPeriodClosed))
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retur "Grades
published"
Bug 3: Security bug
Code:if (course.getGrades().size() == course.getRoster().size())
Type: Wrong condition
- Why: If grades = students]
a-
8:48 PM
4/15/2026
```

## [25:00]
**Nói:** ongret ongret enter có đáng nhập rồi chưa bất cốt thế nào nó cốt này mình tên cái gì có gì bảo anh em nhé Đấy đơn giản thì thôi thế là xong Ok cho anh em nó khá đơn giản luôn chẳng có gì Ok nó vậy là mình đã xử lý xong cái này
**Màn hình:**
```
Ởi cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..
→  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
88  C Tất cả dấu trang
LUYỆN TẬP PROMT AI *  G 6 Saving...  +
• e a-  & Share
File  Edit View Insert Format Tools Extensions Help
a saa A S 100% -  Normal text -  Arial  | - 10.5 +  BIUAOOEO  E #SEEEEX  0 Editing
4  5  6 7...?..
Code: SELECT * FROM courses WHERE id = " + courseld + '*.
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
: Code:  if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code return "Grades
published"
Bug 3: Security bug
Code:if (course.getGrades().size() == course.getRoster().size())
Type: Wrong condition
- Why: If grades = students -> means all grade/
a-
203
^ E 0  ENG  8:48 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  L1• =
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
8A 100%  Normal text -  Arial  | - 10.5 +  BI AO  EBEEEEX  0 Editing
6 r..?.
if (Icourse.IsGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
ll Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) ( // Logical bug 2
return "Not all grades entered";
course.setGradesPublished(true);
return "Grades published";
Output format:
- Numbered list of issues
- Explain for each issue
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = ™ + courseld + ".-
Type: SQL injection
Risk level: Critical
Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
^E Q  8:48 PM
4/15/2026
```

## [25:30]
**Nói:** bài này thì khá là đơn giản thôi không có gì cả nói chung là phần B này thì lại dễ hơn để cho anh em phần B này lại dễ hơn phần A một chút ok đó vậy thì bây giờ bước cuối cùng bước cuối cùng là gì đây bước cuối cùng là mình sẽ là fix đo mình xem nào
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  -
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI@ =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  a 65 Saving...  +
c -  & Share
File  Edit View Insert Format Tools Extensions Help
Normal text "  Arial  | - 10.5 +  BI A O  G 0 Q  E-#SE•E•EEX  / Editing
2  3  4  5  6
2.  Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = '+ courseld + "'*
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
Code:  if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retum "Grades
published"
Bug 3: Security bug
Code:if (course.getGrades() size()== course.getRoster().size())
Type: Wrong condition
Why: If grades = students -> means all grades are entered, but code return Not all grades |
^  ENG  8:48 PM
US  4/15/2026
```
**Màn hình:**
```
Ởi cốc cốc  LUYỆN TẬP PROMT AI - Gor  +  La ..  X
+ > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
• Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q s  Normal text  Arial  | - 10.5 +  BIU A O  / Editing
3  6
Output format:
=
Numbered list of issues
Explain for each issue
Suggest fix each issue
2. Find bug (0.2)
Bug 1:
Code: return true;
Bug 2:
- Code: if (course.getEnrolled) >= course.getMaxSeats))
Type: Logic error  4 of 7
Why: the code does not increase enrolled after a student register, so the number of student
is wrong
Bug 3:
:  Code: registrationRepo.save(new Registration(student, course)):
Type: data inconsistency
^ E Q  ENG  8:49 PM
US  4/15/2026
```

## [26:00]
**Nói:** anh em nhìn nhé viết prompt để fix cái vấn đề này này đúng không Vậy thì sao quá đơn giản rồi đúng không Bây giờ mình có thể là làm theo rất là nhiều cách đối anh em thì bây giờ mình có thể làm có trước mắt mình có mày nhìn thấy thích gần như là giống nhau nhưng mà anh em phải nhìn nhé thích này nhìn xem có gì mới không có cái này đó trên nhau đó có cái này có này mới chưa Nhạc bây giờ nhá em có phải đây này có đây đó nhá sau đó
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go X  +  La :.
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  " ®  410 =
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
E  • -  Share
File  Edit View Insert Format  Extensions Help
as ca A S 100% - Normal text ~  Arial  | - 10.5 +  BIUADOE  / Editing
4  5  6
Your tasks for Scenario B:
• Write an Al Prompt for Security and Logic Review. Write a prompt asking an Al
assistant to review publishGrades) for both logical correctness and security
vulnerabilities. Specify the language and framework (Java / JPA), describe the method's
intended behaviour, and request that each issue be explained with a risk level (Low /
Medium / High / Critical). (0.2 points)
• Identify All Issues. Based on the Al review, explain all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
Kich han A
ENG  8:49 PM
^  US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go:  +  La ..
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  L10 =
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File Edit View Insert Format Tools  Extensions Help
95c8A100%  Normal text  Arial  | - [11] +  BI UAOO  +  Editing
HuLu  6
• Identify All issues. Based on the Ai review, explaln all three issues: the two logical
bugs (which condition is wrong and what the correct logic should be) and the security
vulnerability (name the vulnerability type, describe how an attacker could exploit it in the
CRS, and assign a risk level). (0.2 points)
• Write an Al Prompt to Fix the Issues. Write a follow-up prompt instructing the Al to
provide the fully corrected Java method, replacing the native query with a JPA named
query (parameterised). Present the corrected code with inline comments for each fix.
(0.1 point)
CÁCH LÀM
1. Kịch bản A
1. Context
2.  goal
3. code
4. output format
1. Review code (0.2)
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the RegistrationService class
The method should:
ME CENG  8:49 PM
US  4/15/2026
```

## [26:30]
**Nói:** mình sẽ có cái đây bây con này chưa mà thôi mình bảo rồi cái chỗ này mình sẽ cố gắng là làm sao để biết rõ ràng là nhau mình sẽ không có phí biết để nhắn thể luyện tập chỗ này mình sẽ để là ở con Ok, phần này được gốc 0.1 điểm thôi
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Goc  +  La ..  -  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI• =
C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  +
c -  & Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  8A 8 100%  Normal text  Arial  | - 10.5 +  B A O  0 Editing
6 T.?
/l Check available seats
if (course. getEnrolled() >= course.getMaxSeats()) { // Bug 2
return false;
// Enroll student and persist
course.getRoster().add(student);
registrationRepo.save(new Registration(student, course)); // Bug 3
return true;
Output format:
- Numbered list of issues
- Explain fol each issue
Suggest fix each issue
2. Find bug (0.2)
Bug 1:
- Code: return true;
: Why: If student does not meet prenequisite, it should fail, but it retum true  Type: wrong return value
Bug 2:
- Code:  if (course.getEnrolled() >= course.getMaxSeats())  203
^ E O  ENG  8:49 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  L10 =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI *  E " Saving...  +
& Share
File Edit View Insert Format Tools Extensions Help
asaa 10%  Normal text -  Arial  | - 11] +  BIUAeE  E-#*•E-E•EEX  0 Editing
5  P.le.
Code: SELECT * FROM courses WHERE id = "* + courseld + ''*
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
- Code:  if (Icourse.isGradingPeriodClosed))
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retur "Grades
published"
Bug 3: Security bug
Code:if (course.getGrades().size() == course.getRoster().size())
Type: Wrong condition
- Why: If grades = students -> means all grades are entered, but code retur Not all grades
entered
3. Promt fix) (0.2)
^ E Q  ENG  8:50 PM
US  4/15/2026
```

## [27:00]
**Nói:** Ok, thì ở đây nhé, mình sẽ viết buôn này Ok, phần này nhé, mình sẽ viết là gì? Base On on the the issue
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go  +  La ..  -
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  1I0 =
88  • Tất cả dấu trang
LUYÊN TẬP PROMT AI *  O Saved to Drive  +
& Share
File  Edit View Insert Format  Tools  Extensions Help
Q 5  Normal text  Arial  | - 11] +  BIU AO  E-#SE•E•EEX  0 Editing
6  T..!.
Code: SELECT * FROM courses WHERE id = "+ courseld +"-
Type: SQL injection
Risk level: Critical
- Why: User input (courseld) is directly added into Sql query, so attacker can inject SQL
Bug 2: Security bug
- Code:  if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retum "Grades
published"
Bug 3: Security bug
Code:if (course.getGrades().size() == course.getRoster().size())
Type: Wrong condition
- Why: If grades = students -> means all grades are entered, but code retur Not all grades
entered
3. Promt fix code (0.2)
^  ENG  8:50 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go:  +  La ..
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  L10 =
• Tất cả dấu trang
LUYẸN TẠP PROMT AI *  E Saving...  +
. . -  & Share
File Edit View Insert Format Tools Extensions Help
95 c8 A S 100% - Normal text =  Arial  - 11 +  I  UAO  G E  E#*E E•E EX  Editing
2  3  4  5  6
Bug 3: Security bug
Code:if (course. getGrades().size() == course.getRoster().size())
Type: Wrong condition
: Why: If grades = students-» means all grades are entered, but codereturn Not all grades
3. Prompt fix code (0.1)
^ E 0  8:50 PM
US  4/15/2026
```

## [27:30]
**Nói:** vào dựa trên cái vấn đề mà đã tìm được nó lì quỳ lại quỳ lại đơn biết lại cái gì em xem cô này đây anh chưa đó cứ công thức mà làm rồi nhá lát à à mấy
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go-  +  La ..  -
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI• =
• Tất cả dấu trang
LUYỆN TẠP PROMT AI *  6 Saving...  +
c -  & Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BIUA•  #BEEEX  / Editing
2  3  5  6  T..!..
Bug 3: Security bug
=
Code:if (course. getGrades().size() == course.getRoster().size())
Type: Wrong condition
: Wiy: If grades = students- » means all grades are entered, but code returm Not al grades
entered
3. Prompt fix code (0.1)
Il
Base on the
203
^ E 0  ENG  8:50 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Gor  +  La ..  X
+ > G  @docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
88  C Tất cả dấu trang
LUYẸN TẠP PROMT AI * G 6 Saving...  +
=  & Share
File Edit View Insert Format Tools Extensions Help
asc8A S100% -  Normal text  Arial  | - 10.5 +  BI UA O  GOD E"#S E EEEX  0 Editing
2.....7  2  3  4  5  . 6 T.. T.
Base on the issue found, please rewrite the publishGjades|
-
8:51 PM
```

## [28:00]
**Nói:** đó method correct đi xe nhạc đó sau đó đi sao requirement được chưa requirement này đó ở đây thì mình sẽ có là gì mình sẽ có là thứ nhất không bị thiếu rồi fix all logical nhé cô eo trên em đó tiếp nha anh em nhìn cho mình cái lưu ý place nó đâu rồi
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go: X  +  La ..  X
+ → C ® docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • =
88  • Tất cả dấu trang
LUYỆN TẬP PROMT AI * • () Saving...  +
=  . -  & Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  -15BIVA CAET  0 Editing
1.....7  2  3  4  5
=
Il
Base on the issue found, please rewrite the publishGrades method
^ E Q  ENG  8:51 PM
US
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go  +  La -.  X
+ > @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  • . 1
88  D Tất cả dấu trang
LUYỆN TẠP PROMT AI * • Saved to Drive  +
& Share  +
File Edit View Insert Format Tools Extensions Help
95 ca A S 100% - Normal text -  Arial  1-105+BIVA ODOEREX  0 Editing
t.....  2  4  5
=
Base on the issue found, please rewrite the publishGrades method correctiy
Requirements:
- Fix all
8:51 PM
```

## [28:30]
**Nói:** bài nhắn nhắn con luôn đi có luôn đi anh em nói mình mình em cứ chủ động nhá cái chỗ này em không cần đúng pháp hay gì đâu anh em cứ viết cho ra ý là được mềm quên
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go: x  +  La ..  X
* > G @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  *• =
D Tất cả dấu trang
LUYỆN TẠP PROMT AI # G ( Saving....  +
& Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  - 10.5 +  BIUA•  0 Editing
......  2  3  4  5
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical erl
^ E 0  ENG  8:51 PM
4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go:  +  La ..  -
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  • Tất cả dấu trang
LUYỆN TẠP PROMT AI *  E@ Saved to Drive  +
& Share
File Edit View Insert Format|  Tools Extensions Help
9scaAS100%-  Normal text -  Arial  | - 10.5 +  BIU A•  E#PEEEEX  / Editing
3  4  5
Base on the issue found, please rewrite the publishGrades method correctly
Reguirements:
- Fix all logical errors
• Replace the native query with a JPA namep query
-
^ E 0  ENG C  8:52 PM
4/15/2026
```

## [29:00]
**Nói:** Ok Đấy viết này thôi Tiếp theo là gì Đó là gì Có gì thì mình viết đấy trên ảnh nhé nhìn đề này Đấy Present Ok, cái này là còn comment các thú đúng không Tiếp theo nhá Mình vừa nói rồi, chắc chắn rồi cái gì mình thích này xong thì mà có gì thì mình thêm cái đấy chưa Nếu mà hết rồi thì mình sẽ có lâu
**Màn hình:**
```
Ở cốc cốc  5 LUYỆN TẬP PROMT AI - Go: x  +  La ..  X
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  LI• =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
c -  & Share
File Edit View Insert Format  OO S  Extensions Help
9scaAS10-  Normal text  Arial  | - 10.5 +  BIUAO  HD Н YEEEEX  / Editing
-.  4  5  6 r.?.
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical errors
- Replace the native query with a JPA named query I
^ E Q  8:52 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go:  +  La ..  X
< > C  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKeryQgqQ/edit?tab=t.0  1 =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  +
& Share
File Edit View Insert Format  Extensions Help
Normal text  Arial  | - 11) +  BI UA O  ESPBEEEX  0 Editing
3  4  5
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical errors
- Replace the native query with a JPA named query
Eald  ^ E Q  8:52 PM
US  4/15/2026
```

## [29:30]
**Nói:** qua lâu không ổn cốt cốt đình best practice có nhạc đấy như kia thôi mà cuối cùng em có nhìn like comment x comment x xong cái câu đầu tiên này
**Màn hình:**
```
Ở cốc cốc  = LUYỆN TẬP PROMT AI - Go X  +  La ..  X
< > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |  110 =
88  C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  E " Saving...  +
& Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 11] +  BI UA O  GODE SS E•EEEX  0 Editing
H.L.  4  6 r.?.
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical errors
Replace the native quefy with a JPA named query
- Follow cl
203
^ E Q  ENG  8:52 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go x  +  La ..  -
+ > G  @ docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  L • =
C Tất cả dấu trang
LUYỆN TẠP PROMT AI *  E@ Saved to Drive  +
& Share
File  Edit View Insert Format Tools Extensions Help
asea A S 100% -  Normal text -  Arial  |- 11] +  Editing
2  3  4  5  6 r...?..
published"
Bug 3: Security bug
Code:if (course.getGrades().size() == course.getRoster().size())
Type: Wrong condition
- Why: If grades = students -> means all grades are entered, but code retur Not all grades
3.  Prompt fix code (0.1)
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical errors
- Replace the native query with a JPA named query
- Follow coding best practices
Add inline comments to explain each fix
203
^ E 0  ENG  8:53 PM
US  4/15/2026
```

## [30:00]
**Nói:** bây giờ bước tiếp theo là tự chấm điểm mình nhé ai chắc chắn chấm sẽ nặng tay hơn các thầy luôn chấm điểm ok, chờ thôi, xem nó bao nhiêu điểm ... chết quên mất thiếu
**Màn hình:**
```
Ở cốc cốc  = l  LUYỆN TẬP PROMT AI - Go  +  La ..  X
< →  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  =
C Tất cả dấu trang
LUYÊN TẬP PROMT AI *  • Saved to Drive  +
& Share
File  Edit  View Insert Format Tools  Extensions Help
Q 5  A, § 100% -  Normal text  Arial  I- 11+  BIUAOOEO  0 Editing
3  4  5  6 r..?.
course.setGradesPublished(true);
return "Grades published";
Output format:
Numbered list of issues
- Explain for each issue  Il
Risk level
- Suggest fix each issue
2. Find bug (0.2)
Bug 1: Security bug
Code: SELECT * FROM courses WHERE id = "' + courseld + ™*-
Type: SQL injection
Risk level: Critical
Why: User input (courseld) is directly added into Sqi query, so attacker can inject SQL
Bug 2: Security bug  6 of 7
Code:  if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
- Why: If grading is not closed then system should not publish grades, but code retum "Grades
published"
^ EQ  ENG  8:53 PM
US  4/15/2026
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Go:  ® Al Prompt for Code Review  La ..  -
< >  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0
88  • Tất cả dầu trang
LUYỆN TẬP PROMT AI *  +
. •  & Share
File Edit View Insert Format  Tools  Extensions Help
Q s  A § 100% - Normal text -  Arial  | - 10.5 +  / Editing
2  4
Code:  if (Icourse.isGradingPeriodClosed))
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code retur "Grades
published"
Bug 3: Security bug
• Code: (bourse getGrades@) size() == course.getRoster)size())
Type: Wrong condition
- Why: If grades = students -> means all grades are entered, but code return Not all grades
entered
3. Prompt fix code (0.1)
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
Fix all logical errors
- Replace the native query with a JPA named query
ENG  8:53 PM
US  4/15/2026
```

## [30:30]
**Nói:** không phải chứ một Ok Nói chung là cũng ngon đấy nhé đó như này là ok rồi được chơi nhắm đó nói thì bị trừ mấy cái bớt bạn thôi anh em cứ biết đại khái như mình là như vậy thì chưa anh em cứ
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMT AI - Gor  • AI trong lập trình  I+  La ..
< > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  110 =
• Tất cả dấu trang
LUYỆN TẠP PROMI Al in • SWE202  +
& Share
File  Edit View Insert Format Tools Extensions Help
Q s  A § 100% -  Normal text  Arial  | - 10.5 +  / Editing
4  5  6 7... ?..
Code:  if (Icourse.isGradingPeriodClosed())
Type: Wrong condition
Why: If grading is not closed then system should not publish grades, but code return "Grades
published"
Bug 3: Security bug
• Code:if (course.getGrades) size() == course.getRoster() size))
Type: Wrong condition
- Why: If grades = students -> means all grades are entered, but code return Not all grades
entered
3. Prompt fix code (0.1)
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical errors
- Replace the native query with a JPA named query  203
^ EQ  ENG  8:53 PM
US  4/15/2026
```
**Màn hình:**
```
cốc cốc  LUYỆN TẬP PROMPT AI - Googlc  AI trong lập trình  +  La ..
chatgpt.com/c/69df9851-ae94-8322-8946-521622d4e315  | | =
88  D Tất cả dấu trang
ChatGPT v  •••  +
+ Dùng bản Plus x  I, Chia sẻ
0.1/0.1
C Đoạn chat mới
Q Tìm kiếm đoạn chat
C. Dự án  Tổng điểm
••• Thêm  0.9 / 1.0
Gàn đây  ฿ Rất tốt - bài này đi thi hoàn toàn ăn điểm cao
AI trong lập trình
Yêu cầu nội dung phần A  Chỗ cần sửa để full 1.0
Hướng dẫn Format Đáp Án  Chi cần sửa 2 ý:
Định dạng dáp án tự động
Scenario A bug 2
Cập nhật tài liệu học
Viết rõ hơn:
Format câu hỏi đáp án
Đáp án chuẩn theo format  Bug type: missing state update
Why: enrolled is checked but never incremented after adding a student
Đáp án trắc nghiệm
Đáp án câu hỏi trắc nghiệm
Format đáp án chuẩn  Scenario B labels
Đăng ký HSK-HSKK nhanh
+ Hỏi bất kỳ điều gì  •Ie.
Quân Cao Th...  Nâng cấp
Free  ChatGPT có thể mắc lỗi. Hãy kiểm tra các thông tin quan trong. Vui lòng tham khảo Iùy chon cookie.
E  ENG  8:54 PM
US  4/15/2026
```

## [31:00]
**Nói:** đúng phòng anh em ăn được một điểm thôi các thầy sẽ cho anh em điểm thì chưa chỉ cần anh em biết là đúng phòng thôi Ok vậy thì video này mình sẽ dừng lại ở đây và các video tiếp nhé Đây chỉ là để thi thử thôi và còn một đống đề của mình nữa mình sẽ up vào để nghe có thể luyện tập thêm nhiều Ok, vậy thì 3 anh em nhé Đi dòng này mình xếp từng ở đây
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMPT AI - G X  ® AI trong lập trình  La ..  -
+ > C  docs.google.com/document/d/1poVw0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  4Ф =
88  C Tất cả dấu trang
LUYÊN TẬP PROMPT AI  +
& Share
File Edit View Insert Format  Extensions Help
a 10% Normal text "  Arial  |- [11] +  BIUAOORO  E #EGE EE EX  / Editing
4  6
Base on the issue found, please rewrite the publishGrades method correctly
Requirements:
Fix all logical errors
Replace the native query with a JPA named query
Follow coding best practices
- Add inline comments to explain each fix
AE OEN 4/15/2026  8:54 PM
```
**Màn hình:**
```
Ở cốc cốc  LUYỆN TẬP PROMPT AI - G. X  ® AI trong lập trình  La ..  -  X
+ > G  docs.google.com/document/d/1poVww0SljyvYA6Yg0n3MF8RCyjeZ3bT9dUKerryQgqQ/edit?tab=t.0  |
C Tất cả dấu trang
LUYỆN TẬP PROMPT AI # • () Saving....  +
.. -  & Share
File Edit View Insert Format Tools Extensions Help
Normal text  Arial  | - 10.5 +  BIUA OEO  0 Editing
2  3  5  6
Base on the issue found, please rewrite the publishGrades method correctiy
Requirements:
Fix all logical errors
: Replace the native query with a JPA named query
-  Follow coding best practices
- Add inline comments to explain each fix
^EQ  8:54 PM
```
