s = input()
p = False
for i in range(0,len(s)):
    if int(s[i])%2==1 :
        p = True
        break
if p:
    print("Not v",end="")
else:
    print("V",end="")
print("alid")