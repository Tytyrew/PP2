import math
import sys

R = float(sys.stdin.readline())
ax, ay = map(float, sys.stdin.readline().split())
bx, by = map(float, sys.stdin.readline().split())

def dist(x, y):
    return math.hypot(x, y)

OA = dist(ax, ay)
OB = dist(bx, by)
AB = math.hypot(bx - ax, by - ay)

# расстояние от центра до прямой AB
dx = bx - ax
dy = by - ay
num = abs(ax * by - ay * bx)
den = math.hypot(dx, dy)
h = num / den if den != 0 else float('inf')

# проекция лежит между A и B?
t = - (ax * dx + ay * dy) / (dx*dx + dy*dy) if dx*dx + dy*dy != 0 else -1

intersects = (h < R and 0 < t < 1)

if not intersects:
    print(f"{AB:.10f}")
else:
    AT = math.sqrt(OA*OA - R*R)
    BT = math.sqrt(OB*OB - R*R)

    dot = ax*bx + ay*by
    cos_theta = dot / (OA * OB)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    theta = math.acos(cos_theta)

    alpha = math.acos(R / OA)
    beta = math.acos(R / OB)

    phi = theta - alpha - beta
    if phi < 0:
        phi = 0.0

    arc = R * phi

    res = AT + BT + arc
    print(f"{res:.10f}")