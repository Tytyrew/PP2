import re
def repl(match):
    return match.group()+' '
print(re.sub("[A-Z][^A-Z]+",repl,input()))