import re
s = input()
p = re.search("\S+@\S+\.\S+",s)
if p is None: print("No email")
else: print(p.group())