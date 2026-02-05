class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,gpa):
        super().__init__(name)
        self.gpa = gpa
    def display(self):
        print("Student: ",self.name,', GPA: ',self.gpa,sep='')
inp = input().split(' ')
s = Student(inp[0],float(inp[1]))
s.display()