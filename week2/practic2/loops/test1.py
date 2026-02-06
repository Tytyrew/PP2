import sys

n=int(input())

d={}

for i in range(n):
    s = sys.stdin.readline().rstrip().split(' ')
    
    if s[0]=="set":
        ans = str(s[2])
        for i in range(3,len(s)):
            ans = ans+" "+s[i]
        d[s[1]] = ans
    elif s[0]=="get":
        if s[1] in d: print(d[s[1]])
        else: print("KE: no key",s[1],"found in the document")
    else:
        print("pls god save me")
