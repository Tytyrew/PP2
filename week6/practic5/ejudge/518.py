import re
s = input()
print(len(re.findall(re.escape(input()),s)))