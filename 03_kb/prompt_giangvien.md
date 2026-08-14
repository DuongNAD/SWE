# PROMPT GỐC CỦA GIẢNG VIÊN (b1-1, b1-2)

### Prompt AI nhờ review code Java phương thức registerStudent và phát hiện lỗi logic/semantic (b1-1 @ 03:00)
```text
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the RegistrationService class
The method should:
- Check prerequisite
- Check available seats
- Enroll student and persist

Your task:
- Find logical or semantic errors
- Check coding best practices

Here is the code:
public class RegistrationService {
    public boolean registerStudent(Student student, Course course) {
        // Check prerequisite
        if (course.getPrerequisite() != null &&
            !student.getCompletedCourses().contains(course.getPrerequisite())) {
            return true; // Bug 1
        }
        // Check available seats
        if (course.getEnrolled() >= course.getMaxSeats()) { // Bug 2
            return false;
        }
        // Enroll student and persist
        course.getRoster().add(student);
        registrationRepo.save(new Registration(student, course)); // Bug 3
        return true;
    }
}

Output format:
- Numbered list of issues
- Explain for each issue
- Suggest fix each issue
```
Áp dụng cho: Q6

### Prompt AI nhờ sửa toàn bộ bug và viết lại phương thức registerStudent hoàn chỉnh (b1-1 @ 25:30)
```text
Base on the issue found, please rewrite the registerStudent() method correctly.
Requirement:
- Fix all logical errors
- following coding best practices
- Add comment to explain each fix
```
Áp dụng cho: Q6

### Prompt Review Code cho Scenario B (GradeService.java) (b1-2 @ 01:30)
```text
I am working on a Course Registration System using Java and Spring boot.
Please review the following method in the GradeService class
The method should:
- Fetch course from database
- Guard: grading period must be closed first
- Guard: all students must have a grade

Your task:
- Find logical errors in the condition
- Identify any security vulnerabilities
- Check coding best practices
- Assign a risk level (Low / Medium / High / Critical)
- Suggest a fix for each issue

Output format:
- Numbered list of issues
- Explain for each issue
- Risk level
- Suggest fix each issue

Here is the Code:
public class GradeService {
private EntityManager em;
public String publishGrades(String courseId) {
// Fetch course from database
Course course = (Course) em.createNativeQuery(
"SELECT * FROM courses WHERE id = '" + courseId + "'" // Security bug
).getSingleResult();
// Guard: grading period must be closed first
if (!course.isGradingPeriodClosed()) { // Logical bug 1
return "Grades published";
}
// Guard: all students must have a grade
if (course.getGrades().size() == course.getRoster().size()) { // Logical bug 2
return "Not all grades entered";
}
course.setGradesPublished(true);
return "Grades published";
}
}
```
Áp dụng cho: Q6

### Prompt Fix Bug cho Scenario B (GradeService.java) (b1-2 @ 27:00)
```text
Based on the issue found, please rewrite the publishGrades method correctly
Requirements:
- Fix all logical errors
- Replace the native query with a JPA named query
- Follow coding best practices
- Add inline comments to explain each fix
```
Áp dụng cho: Q6