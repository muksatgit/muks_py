
# INHERITANCE

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)



class WorkingStudent(Student):
    def __init__(self, name, school, salery):
        super().__init__(name, school)
        self.salery = salery

    @property #by adding this decorator you conver a method into a properity which is getter
    def weekly_salery(self):
        return self.salery/40


student1 = Student("kriday", "Pillens")
student2 = WorkingStudent("Myra Sharma", "Vittra, Loomvegan", 50)

print(student1.name)
print(student2.weekly_salery)