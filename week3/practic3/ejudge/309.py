pi = 3.14159
class Circle:
    def __init__(self):
        self.radius = 0.00
    def inp(self):
        self.radius = float(input())
    def area(self):
        return self.radius*self.radius*pi
c = Circle()
c.inp()
print(f"{c.area():.2f}")