import functools
a = [1,2,3,4,5]
l = functools.reduce(lambda x,y: x*y, a)
print(l)