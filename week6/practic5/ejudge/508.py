import re
s = input()
spl = input()
p = re.split(spl,s)
print(p[0],end='')
for i in range(1,len(p)): print(',',p[i],end='',sep='')