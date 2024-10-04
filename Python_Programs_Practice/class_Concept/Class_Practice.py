"""
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def student_Name(self):
        print("Nme", self.name)

    def student_Average_Marks(self):
        No_of_Sub = len(self.marks)
        total_marks = sum(self.marks)
        average = total_marks / No_of_Sub
        return average


Student1 = Student("Ravi", [88, 90, 95])
 
Student1.student_Name()
print(Student1.student_Average_Marks())
