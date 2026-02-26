x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# отражаем B относительно оси Ox
# B' = (x2, -y2)

t = y1 / (y1 + y2)

x = x1 + t * (x2 - x1)
y = 0.0

print(f"{x:.10f} {y:.10f}")