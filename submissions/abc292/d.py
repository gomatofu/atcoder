from collections import deque
N,M=[int(nm) for nm in input().split()]
# 自己ループ辺の数を管理
table=[0 for _ in range(N)]
G=[[] for _ in range(N)]
for _ in range(M):
    u,v=[int(a)-1 for a in input().split()]
    if u==v:
        table[u]+=1
    else:
        G[u].append(v)
        G[v].append(u)

seen=[False for _ in range(N)]
for i in range(N):
    if seen[i]:
        continue

    que=deque()
    que.append(i)
    # この連結成分に含まれる頂点と辺の総数
    e,v=0,0
    # この連結成分に含まれる自己ループ辺の総数
    eself=0
    while que:
        now=que.popleft()
        v+=1
        eself+=table[now]
        seen[now]=True
        for nex in G[now]:
            e+=1
            if not seen[nex]:
                seen[nex]=True
                que.append(nex)
    
    # 辺は2度数えられている
    if v!=e//2+eself:
        print("No")
        exit()

# 全連結成分で条件を満たせば
print("Yes")
