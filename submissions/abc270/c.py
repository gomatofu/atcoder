from collections import deque

N,X,Y=map(int,input().split()); X-=1; Y-=1
G=[[] for _ in range(N)]
for i in range(N-1):
  u,v=map(int,input().split()); u-=1; v-=1
  G[u].append(v); G[v].append(u)

D=deque(); D.append(X)
seen=[0]*N; seen[X]=1
rec={}
while D:
  now=D.popleft()
  for nxt in G[now]:
    if seen[nxt]:
      continue
    seen[nxt]=1
    rec.setdefault(nxt,now)
    D.append(nxt)

ans=[]
n=Y
while n!=X:
  ans.append(n+1)
  n=rec[n]
ans.append(n+1)
print(*reversed(ans),sep=" ")
