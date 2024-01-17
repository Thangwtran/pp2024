# INPUT FUNCTION

def inputNumOfStudent():
    student = int(input("The number of student: "))
    return student

def inputStudentInfo():
    id = input("Id: ")
    name = input("Name: ")
    Dob = input("Date of birth: ")
    studentInfo = {
        "ID:" : id,
        "Student's name: " : name,
        "Date of Birth: " : Dob
    }
    return studentInfo

def inputNumOfCourse():
    course = int(input("The number of course: "))
    return course

def inputCourseInfor():
    courseId = input("Enter course ID: ")
    courseName = input("Enter course's name: ")
    courseInfo = {
        "Course ID: " : courseId,
        "CourseName: " : courseName
    }
    return courseInfo

def inputMark():
    IdSelected = input("Enter Course ID: ")
    for i in range(len(courses)):
        if courses[i].get("Course ID:") == IdSelected:
            listMark = {
                "Course ID: " : IdSelected,
                "Course Name: " : courses[i].get("CourseName:"),
                "Student Name: " : input("Enter student's name: "),
                "Mark: ": input("Enter mark of student: ")
            }
    return listMark




# Main
students = []

courses = []
