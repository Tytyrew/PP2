def isprime(a):
    if (a<=1): return False
    i = 2
    while(i*i<=a):
        if (a%i==0): return False
        i+=1
    return True
n = int(input())
for i in range(1,n+1):
    if (isprime(i)): print(i,end=' ')
