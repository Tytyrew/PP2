def square_seg(l,r):
    while l<=r:
        yield l*l
        l += 1
a = int(input())
b = int(input())
for i in square_seg(a,b): print(i)