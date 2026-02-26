def even_numbers(n):
    i = 0
    while i<=n:
        yield i
        i+=2
n = int(input())
for i in even_numbers(n): print(i)