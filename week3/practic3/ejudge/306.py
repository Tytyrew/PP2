class Rectangle:
    def __init__(self):
        self.length=0
        self.width=0
    def inputValues(self):
        s = input().split(' ')
        self.length=int(s[0])
        self.width=int(s[1])
    def area(self):
        return self.length*self.width
r = Rectangle()
r.inputValues()
print(r.area())