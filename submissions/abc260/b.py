n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

# ”Šw
for i in range(x):
    amax = max(a)
    amax_index = a.index(amax)
    c.append(amax_index)
    a[amax_index] = -1
    b[amax_index] = -1
    
# ‰pŒê
for i in range(y):
    bmax = max(b)
    bmax_index = b.index(bmax)
    c.append(bmax_index)
    a[bmax_index] = -1
    b[bmax_index] = -1
    
# ”Šw+‰pŒê
p = []
for i in range(len(a)):
    p.append(a[i] + b[i])
for i in range(z):
    pmax = max(p)
    pmax_index = p.index(pmax)
    c.append(pmax_index)
    p[pmax_index] = -1
c.sort()

# print(c)
for i in range(len(c)):
    print(c[i] + 1)
