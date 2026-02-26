import re
s = input()
p = input()
r = input()
proc = re.sub(p,r,s)
print(proc)