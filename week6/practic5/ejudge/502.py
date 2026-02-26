import re

s = input()
sub = input()
m = re.search(sub,s)
if m is None: print("No")
else: print("Yes")