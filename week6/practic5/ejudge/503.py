import re

s = input()
sub = input()
m = re.findall(sub,s)
print(len(m))