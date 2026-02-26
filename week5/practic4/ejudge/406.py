import sys
n = int(input())
if (n<=0): sys.exit(0)
elif (n==1): print(0,sep='',end='')
elif (n==2): print(0,',',1,sep='',end='')
else: print(0,',',1,',',sep='',end='')
f1 = 0
f2 = 1
f3 = 1
for i in range (3,n):
    print(f3,end=',')
    f1 = f2
    f2 = f3
    f3 = f2 + f1
if (n>=3): print(f3,end='')