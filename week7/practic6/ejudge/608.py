input()
a = sorted(set(map(lambda x:int(x),input().split())))
for i in range(len(a)): print(a[i],end=' ')