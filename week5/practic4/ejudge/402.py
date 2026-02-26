n = int(input())
i = 0
while(i<=n-2):
    print(i,end=',')
    i+=2
if (n%2==0): print(n)
else: print(n-1)