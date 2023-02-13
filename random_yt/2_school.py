class Student:
    def __init__(self,name,age,grade):
        self.name =name
        self.age =age
        self.grade =grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_student = max_students
        self.students = []
    
    # mendeklarasikan jumlah maksimal siswa
    def add_student(self,student):
        if len(self.students)< self.max_student:
            self.students.append(student)
            return True
        return False
    
    #untuk mendapatkan nilai rata rata dari semua siswa    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value/ len(self.students)

#---------------------instansiasi-----------------
s1 = Student("Nur",19,100)
s2 = Student("Taufik",19,75)
s3 = Student("Teguh",19,85)

course = Course("Science",3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

#print(course.students[0].name)
print(course.get_average_grade())





