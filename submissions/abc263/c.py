from itertools import combinations

N,M = list(map(int, input().split()))
for l in combinations(range(1, M + 1), N):
    print(*l, sep=' ')
