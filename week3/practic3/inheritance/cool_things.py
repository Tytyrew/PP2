class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def grow(self):
        age += 1
class student:
    def __init__(self,id,gpa):
        self.id = id
        self.gpa = gpa
    def sleep(self):
        gpa -= 1
    #Студент это не человек
class LEGENDARY_STUDENTO_HUMANAIDO(student,human):
    def __init__(self,lvl,name,age,id,gpa):
        self.lvl = lvl
        super().__init__(id,gpa)
c = LEGENDARY_STUDENTO_HUMANAIDO(1,2,3,4,5)

    