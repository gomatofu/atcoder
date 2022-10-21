from math import sin, cos, hypot, pi, atan2
 
T = int(input())
L, X, Y = map(int, input().split())
 
Q = int(input())
 
for _ in range(Q):
    e = int(input())
    y = -sin(e * 2 * pi / T) * (L / 2)
    z = -cos(e * 2 * pi / T) * (L / 2) + L / 2
    d = hypot(X, Y - y)
    theta = atan2(z, d)
    print(theta * 180 / pi)
