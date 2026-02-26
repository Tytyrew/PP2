import math
n = float(input("Input number of sides:"))
l = float(input("Input the length of a side:"))
print("The area of the polygon is:",(n*l*l*math.sin(2*math.pi/n))/(4*(1-math.cos(2*math.pi/n))))