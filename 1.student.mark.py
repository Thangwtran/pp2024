# INPUT FUNCTION

def inputNumOfStudent():
    student = int(input("The number of student: "))
    return student

def inputStudentInfo():
    id = input("Id: ")
    name = input("Name: ")
    Dob = input("Date of birth: ")
    studentInfo = {
        'id': id,
        'name' : name,
        'Dob': Dob
    }
    return studentInfo

def inputNumOfCourse():
    course = int(input("The number of course: "))
    return course

def inputCourseInfor():
    courseId = input("Enter course ID: ")
    courseName = input("Enter course's name: ")
    courseInfo = {
       'id' : courseId,
       'name': courseName
    }
    return courseInfo

def inputMark(courses,students):
    marks = {}
    
    for course in courses:
        print(f"Enter marks for students in course {course['name']}")
        marks[course['id']] = []
        
        for student in students:
            mark = float(input(f"Enter mark for {student['name']} in {course['name']}: "))
            studentmarkdict = {
                'studentId': student['id'],
                'mark': mark
            }
            marks[course['id']].append(studentmarkdict)

    return marks

# Listing Functions

## List Courses
def showCourses(courses):
    for course in courses:
        print("ID: ",course['id'])
        print("Name: ",course['name'])
        print("-----------------------------")
def showStudents(students):
    for student in students:
        print("ID: ",student['id'])
        print("Name: ",student['name'])
        print("Date of birth: ", student['Dob'])
        print("----------------------------")

def showMarks(marks,courses,students):
    for course in courses:
        print(f"==> Marks for students in course {course['name']} <==")
        course_marks = marks.get(course['id'], [])
        for mark in course_marks:
            student = next((s for s in students if s['id'] == mark['studentId']), None)
            if student:
                print(f"{student['name']}: {mark['mark']}")
        print("-----------------------------")

        
# Main
students = []
totalStudent = inputNumOfStudent()
print("==> Enter the student's information <==")
for i in range(0,totalStudent):
    s = inputStudentInfo()
    students.append(s)


courses = []
totalCourse = inputNumOfCourse()
print("==> Enter the course's information <==")
for i in range(0,totalCourse):
    c = inputCourseInfor()
    courses.append(c)
    
print("==> Enter mark for students")
marks = inputMark(courses,students)

print("==> List of Course <==")
showCourses(courses)

print()
print("==> List of Student <==")
showStudents(students)

print()
showMarks(marks,courses,students)
