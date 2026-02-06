class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class student:
    def __init__(self,id,gpa):
        self.id = id
        self.gpa = gpa
    #Студент это не человек
class LEGENDARY_STUDENTO_HUMANAIDO(student,human):
    def __init__(self):
        super().__init__()