l = ['1','2','3','4','5','6','7','8']
print(l)
print(list(map(lambda x: int(x),l)))
print(list(filter(lambda x: int(x) if int(x)%2==0 else "loh",l)))
