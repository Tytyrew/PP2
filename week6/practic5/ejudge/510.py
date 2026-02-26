import re
s = input()
if re.sub("cat",s) is None and re.sub("dog",s) is None: print("No")
else: print("Yes")