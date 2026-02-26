import re
s = input()
print(re.search(' .+,',s).group()[1:-1],re.search("[0-9]+",s).group(),sep=' ')