class Shape:
    def __init__(self):
        self.length=0
    def inputLen(self):
        self.length=int(input())
    def area(self):
        return ((self.length)*(self.length))
x = Shape()
x.inputLen()
print(x.area())