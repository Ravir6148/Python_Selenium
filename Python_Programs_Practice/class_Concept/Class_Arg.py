class Student:
    def __init__(self, name, age, add, marks):
        self.name = name
        self.age = age
        self.add = add
        self.marks = marks

    def student_info(self):
        print("Student Name = ", self.name)
        print("Student Age = ", self.age)
        print("Student Add = ", self.add)
        print("Student Marks = ", self.marks)


sObj = Student("Ravi", 31, "BTM", 40)
sObj.student_info()