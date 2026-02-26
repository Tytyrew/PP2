import re
p = re.findall("[0-9]+",input())
for i in p: 
    if len(i)>1:print(i)