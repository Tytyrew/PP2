n = int(input())
a = input().split()
res = filter(lambda x: int(x)%2==0,a)
print(len(list(res)))