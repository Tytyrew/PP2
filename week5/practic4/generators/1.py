def square(n):
    i = 0
    while i*i<=n:
        yield i*i
        i += 1
for i in square(50):
    print(i)