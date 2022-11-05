import collections
N = int(input())
s = ["".join(sorted(input())) for _ in range(N)]

ans = 0
c=collections.Counter(s)
for si in set(s):
    n = c[si]
    ans += n * (n-1) // 2
print(ans)
