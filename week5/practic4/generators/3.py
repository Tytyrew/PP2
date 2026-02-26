def three_4_divis(n):
    i = 0
    while i<=n:
        yield i
        i+=12
n = int(input())
for i in three_4_divis(n): print(i)