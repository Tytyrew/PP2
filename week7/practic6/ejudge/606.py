n = int(input())
s = input().split()
if all(list(map(lambda x: 1 if int(x) >= 0 else 0,s))): print("Yes")
else: print("No")