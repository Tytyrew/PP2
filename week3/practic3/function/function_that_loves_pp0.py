def f(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(f(1))
print(f(1,2,3,4))