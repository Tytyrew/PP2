n = int(input())
arr = input().split(' ')
q = int(input())
add = lambda a,x: a + x
mult = lambda a,x: a*x
power = lambda a,x: a**x
myabs = lambda a,x: a if a>0 else -a
for i in range(0,n):
    arr[i] = int(arr[i])
for i in range(0,q):
    inp = input().split(' ')
    if (inp[0]=='abs'):
        inp.append(-1)
        func = lambda a,x: a if a>0 else -a
    elif (inp[0]=='add'):
        func = lambda a,x: a + x
    elif (inp[0]=='multiply'):
        func = lambda a,x: a*x
    elif (inp[0]=='power'):
        func = lambda a,x: a**x
    for i in range(0,n):
        arr[i] = func(arr[i],int(inp[1])) 
for i in range(0,n):
    print(arr[i],end=' ')