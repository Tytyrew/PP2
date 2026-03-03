s = input()
if any(list(map(lambda x: 1 if x.lower() in ('a','e', 'i', 'o','u') else 0,s))): print("Yes")
else: print("No")