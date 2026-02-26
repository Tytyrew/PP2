def gen(n):
    while n>=0:
        yield n
        n-=1
for i in gen(int(input())): print(i)