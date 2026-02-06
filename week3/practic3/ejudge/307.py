import math
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def inputPoint(self):
        s = input().split(' ')
        self.x = int(s[0])
        self.y = int(s[1])
    def printPoint(self):
        print('(',self.x,', ',self.y,')',sep='')
    def move(self,A):
        self.x=A.x
        self.y=A.y
    def dist(self,A):
        return ((self.x-A.x)**2 + (self.y-A.y)**2)**0.5
P = Point()
Inp = Point()
Inp.inputPoint()
P.move(Inp)
P.printPoint()
Inp.inputPoint()
P.move(Inp)
P.printPoint()
Inp.inputPoint()
print(f"{P.dist(Inp):.2f}")
#print(P.dist(Inp))
