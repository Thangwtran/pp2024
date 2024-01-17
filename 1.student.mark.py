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
    print(f"Enter marks for student int c {courses['name']}")
    marks = {}
    marks[courses['id']] = []
    for student in students:
        mark = float(input(f"Enter mark for {student['name']}"))
        studentmarkdict = {
            'studentId' : students['id'],
            'mark' : mark
        }
        mark[courses['id']] += [studentmarkdict]
    

# Listing Functions



# Main
students = []
totalStudent = inputNumOfStudent()
print("==> Enter the student's information <==")
for i in range(0,totalStudent):
    s = inputStudentInfo()
    students += s
courses = []
