import re
def repl(match):
    return match.group()[1].upper()
s = input()
print(re.sub(r'_[a-zA-Z]',repl,s))