import re

s = input()
m = re.match(r"Hello", s)
if m is None: print("No")
else: print("Yes")