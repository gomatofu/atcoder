A,B,D=map(int,input().split())

import math

d_rad = math.radians(D) # 角度法を弧度法に変換

a_rotated = A * math.cos(d_rad) - B * math.sin(d_rad)
b_rotated = A * math.sin(d_rad) + B * math.cos(d_rad)

print(a_rotated, b_rotated)
