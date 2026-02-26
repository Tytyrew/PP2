import re
s = input()
p = re.findall("^[A-Z,a-z]+[0-9]$",s)
if (len(p)!=0): print("Yes")
else: print("No")