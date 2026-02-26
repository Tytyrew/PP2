import re
def repl(match):
    return '_'+match.group().lower()
s = input()
print(re.sub(r'[A-Z][^A-Z]+',repl,s))