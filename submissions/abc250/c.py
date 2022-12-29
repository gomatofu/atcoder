N, Q = map(int, input().split())
a = list(range(N+1))
inv = list(range(N+1))

for _ in range(Q):
    x = int(input())
    posX = inv[x]
    posOther = posX + 1
    if posOther == N+1:
        posOther = N-1
    other = a[posOther]
    a[posX], a[posOther] = a[posOther], a[posX]
    inv[x], inv[other] = inv[other], inv[x]

print(*a[1:])
