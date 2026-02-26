import re
s = input()
m = re.findall("[A-Z]",s)
print(len(m))