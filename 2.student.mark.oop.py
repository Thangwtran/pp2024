# INPUT FUNCTION
class Student:
    def __init__(self,id,name,dob,course): # Constructor ??
        self.name = name
        self.id = id
        self.dob = dob
        self.course = course
        
    def showStudent(self):
        print("Name: " + self.name)
        print("Id: " + self.id)
        print("Date of birth: " + self.dob)
        print("Course: " + self.course)
    # getter setter
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
        
    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
        
    def getDob(self):
        return self.dob
    
    def setDob(self,dob):
        self.dob = dob
        
    def getCourse(self):
        return self.course
    
    def setCourse(self,course):
        self.course = course
   
class Course:
    def __init__(self,courseId,courseName,numOfStd):
        self.courseId = courseId
        self.courseName = courseName
        self.numOfStudent = numOfStd
    
    
    def showCourse(self):
        print("CourseId: " + self.courseId)
        print("CourseName: " + self.courseName)
        print("Number of student in course: " + self.numOfStudent)
    
    def inputMark(self,registeredCourse,studentName):
        if(self.courseName == registeredCourse):
            mark = input("Enter mark for student: ")
        print("Student's name: " + studentName)
        print("Register Course: " + registeredCourse)
        print("Mark: " + mark)
    
    # getter setter
    def getCourseId(self):
        return self.courseId
    def setCourseId(self,courseId):
        self.courseId = courseId
    def getCourseName(self):
        return self.courseName
    def setCourseName(self,courseName):
        self.courseName = courseName
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
print("Test Class")
student1 = Student("22BI13404","Thang","30/09/2004","Ads")
student1.showStudent()
print()
course1 = Course("01","Ads","20")
course1.showCourse()
print()
print("==> Enter mark for student <==")
course1.inputMark(student1.getCourse(),student1.getName())