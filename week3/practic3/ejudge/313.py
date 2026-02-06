def filter(n):
    if n<=1: return False
    i = 2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
inp = input().split(' ')
ans = []
filt = lambda x,a : a.append(x) if filter(inp[i]) else ''
for i in range(0,len(inp)):
    inp[i] = int(inp[i])
    filt(inp[i],ans)
if len(ans)==0:
    print("No primes")
else:
    for i in range(0,len(ans)):
        print(ans[i],end=' ')