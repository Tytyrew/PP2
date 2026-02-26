import sys

m = int(sys.stdin.readline())
g = 0
n = 0

for _ in range(m):
    scope, value = sys.stdin.readline().split()
    value = int(value)

    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
    # local — игнорируем

print(g, n)