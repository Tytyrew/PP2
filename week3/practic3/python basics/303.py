def str_to_dig_conv(s):
    if s=="ONE": return 1
    elif s=="TWO": return 2
    elif s=="THR": return 3
    elif s=="FOU": return 4
    elif s=="FIV": return 5
    elif s=="SIX": return 6
    elif s=="SEV": return 7
    elif s=="EIG": return 8
    elif s=="NIN": return 9
    elif s=="ZER": return 0
def dig_to_str_conv(n):
    if n==1: return "ONE"
    elif n==2: return "TWO"
    elif n==3: return "THR"
    elif n==4: return "FOU"
    elif n==5: return "FIV"
    elif n==6: return "SIX"
    elif n==7: return "SEV"
    elif n==8: return "EIG"
    elif n==9: return "NIN"
    elif n==0: return "ZER"
def str_to_int(s):
    n = int(0)
    for i in range(0,len(s),3):
        n *= 10
        n += str_to_dig_conv(s[i]+s[i+1]+s[i+2])
    return n
def int_to_str(n):
    s = ''
    if n < 0:
        s = '-'
        n *= (-1)
    while n>0:
        s = dig_to_str_conv(n%10)+s
        n//=10
    return s
def split_to_two_str_and_get_op_t(s):
    i = 0
    while (s[i]!='+' and s[i]!='-' and s[i]!='*' and s[i]!='/'): i += 1
    return s[:i] , s[i], s[(i+1):]
def calc(s1,op_t,s2):
    n1=str_to_int(s1)
    n2=str_to_int(s2)
    if op_t=='+': return n1+n2
    elif op_t=='-': return n1-n2
    elif op_t=='*': return n1*n2
    elif op_t=='/': return n1//n2

s1,op_t,s2 = split_to_two_str_and_get_op_t(input())

print(int_to_str(calc(s1,op_t,s2)))