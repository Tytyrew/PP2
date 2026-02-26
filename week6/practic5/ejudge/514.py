import re
s = input()
pat = re.compile("[0-9]")
if len(s)==len(pat.findall(s)): print("Match")
else: print("No match")