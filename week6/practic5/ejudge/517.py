import re
s = input()
print(len(re.findall("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",s)))