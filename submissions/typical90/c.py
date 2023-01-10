import sys
from collections import deque
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = II()
G = [[] for _ in range(N)]

for _ in range(N-1):
  A, B = map(int, input().split())
  G[A-1].append(B-1)
  G[B-1].append(A-1)

def dfs(s):
    dist = [-1] * N 
    dist[s] = 0
    Q = deque()
    Q.append(s)
    while Q:
        v = Q.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                Q.append(nv)
                dist[nv] = dist[v] + 1
    return dist


dist0 = dfs(0)
index = dist0.index(max(dist0))
r_dist = dfs(index)
print(max(r_dist) + 1)
