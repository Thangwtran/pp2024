import math


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
            mark = float(input("Enter " + self.courseName + " mark for " + studentName + ": "))
            mark_rounded = math.floor(mark*10)/10 # Round down to 1 digit decimal
        
            print()
            print("<== Enter Mark SuccessFull ==>")
            print("Student's name: " + studentName)
            print("Register Course: " + registeredCourse)
            print("Mark: ", mark_rounded)
            print()
        else: 
            print("==> Does not find the course <==")
    
    
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
def listCourse(courses):
    for course in courses:
        print("ID: ",course.getCourseId())
        print("Name: ",course.getCourseName())
        print("-----------------------------")

def listStudent(students):
    for std in students:
        print("Id: " + std.getId())
        print("Name: " + std.getName())
        print("Date of Birth: " + std.getDob())
        print("-------------------------------")

        
# Main
courses = []
students = []
while True:
    print("1. Add course")
    print("2. Add student")
    print("3. List students")
    print("4. List courses")
    print("5. Enter mark for student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        courseId = input("Enter course id: ")
        courseName = input("Enter course name: ")
        numOfStd = input("Enter number of students: ")
        course = Course(courseId, courseName, numOfStd)
        courses.append(course)
    elif choice == '2':
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        course = input("Enter student course: ")
        student = Student(id, name, dob, course)
        students.append(student)
    elif choice == '3':
        listStudent(students)
    elif choice == '4':
        listCourse(courses)
    elif choice == '5':
        registeredCourse = input("Enter registered course: ")
        studentName = input("Enter student name: ")
        for student in students:
            if student.getName() == studentName:
                for course in courses:
                    course.inputMark(registeredCourse, studentName)
            else:
                print("Does not find student name: " + studentName)
    elif choice == '6':
        break
    else:
            print("Invalid choice. Please enter a number between 1 and 6.")

