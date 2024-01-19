# INPUT FUNCTION
class Student:
    def __init__(self,id,name,dob,course): # Constructor ??
        self.name = name
        self.id = id
        self.dob = dob
        self.course = course
    
    def inputNumOfStd(self,numOfStd): # class method ?
        self.numOfStd = numOfStd
        
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
student1 = Student("22bi14","Nam","30/09/2004","OOP")
print(student1.name)
print(student1.getName())
print(student1.getCourse())
student1.setCourse("Ads")
print(student1.getCourse())
student1.showStudent()