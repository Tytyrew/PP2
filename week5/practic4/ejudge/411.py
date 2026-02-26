def clear(s):
    if (len(s)==0): return ''
    if (s[0]!='{'): return s
    a = []
    di = {}
    cnt = 0
    vs = ''
    for i in range(1,len(s)-1):
        if (s[i]=='{' or s[i]=='[' or s[i]=='('): cnt+=1
        if (s[i]=='}' or s[i]==']' or s[i]==')'): cnt-=1
        if (cnt==0 and s[i]==','): 
            j = 0
            for j in range (0,len(vs)):
                if (vs[j]==':'):
                    break
            di[vs[0:j]] = clear(vs[j+1:len(vs)])
            vs = ''
        else: vs = vs+s[i]
    j = 0
    for j in range (0,len(vs)):
        if (vs[j]==':'):
            break
    if (vs==''): return {}
    di[vs[0:j]] = clear(vs[j+1:len(vs)])
    return dict(sorted(di.items()))
def update(d,upd):
    for i in upd:
        if (i in d):
            if ( type(upd[i])!=type({}) or type(d[i])!=type({}) ): 
                if (upd[i]=='null'): d.pop(i)
                else: d[i] = upd[i]
            else: d[i] = update(d[i],upd[i])
        else: d[i] = upd[i]
        if (i in d and len(d[i])==0): d.pop(i)
    return d
def out(d):
    cnt = 0
    print("{",end='')
    for i in d:
        cnt+=1
        print(i,end=':')
        if ( type(d[i])!=type({}) ): 
            if ( cnt<len(d) ): print(d[i],end=',')
            else: print(d[i],end='')
        else: 
            out(d[i])
            if ( cnt<len(d) ): print(',',end='')
    print("}",end='')
s1 = input()
s2 = input()
d = clear(s1)
upd = clear(s2)
ans = update(d,upd)
out(ans)