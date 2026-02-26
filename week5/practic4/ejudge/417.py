import math
import sys

R = float(sys.stdin.readline())
ax, ay = map(float, sys.stdin.readline().split())
bx, by = map(float, sys.stdin.readline().split())

dx = bx - ax
dy = by - ay

A = dx*dx + dy*dy
B = 2*(ax*dx + ay*dy)
C = ax*ax + ay*ay - R*R

eps = 1e-12
res = 0.0

if A < eps:
    # отрезок — точка
    if ax*ax + ay*ay <= R*R:
        res = 0.0
    else:
        res = 0.0
else:
    D = B*B - 4*A*C

    if D < 0:
        # нет пересечений
        if ax*ax + ay*ay <= R*R and bx*bx + by*by <= R*R:
            res = math.hypot(dx, dy)
        else:
            res = 0.0
    else:
        sqrtD = math.sqrt(max(0.0, D))
        t1 = (-B - sqrtD) / (2*A)
        t2 = (-B + sqrtD) / (2*A)

        lo = max(0.0, min(t1, t2))
        hi = min(1.0, max(t1, t2))

        if lo <= hi:
            seg_len = math.hypot(dx, dy)
            res = max(0.0, hi - lo) * seg_len
        else:
            res = 0.0

print("{:.10f}".format(res))