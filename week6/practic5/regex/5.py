import re
s = input()
print(re.findall(r"a[^b]+b",s))