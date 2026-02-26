import re
s = input()
p = re.findall("[0-9]",s)
for i in p: print(i,end=' ')