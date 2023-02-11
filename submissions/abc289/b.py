 # 頂点 v を始点とした深さ優先探索
def dfs(v, G, seen):
     # 頂点 v を探索済みにする
    seen[v] = True
    ans.append(v)
    for v2 in G[v]:
         # v2 がすでに探索済みならば、スキップする
        if seen[v2]: continue
         # v2 始点で深さ優先探索を行う (関数を再帰させる)
        dfs(v2, G, seen)
    return
 
 # main
 # 入力を受け取る
N, M = map(int, input().split())
A=list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for i in range(M):
    G[A[i]].append(A[i]+1)
    G[A[i]+1].append(A[i])

seen = [False for _ in range(N+1)]    # seen[v]：頂点 v が探索済みなら true, そうでないなら false
ans = []
ans2=[]

for v in range(1,N+1):
    # 頂点 v がすでに訪問済みであれば、スキップ
    if seen[v]: continue
    # そうでなければ、頂点 v を含む連結成分は未探索
    # 深さ優先探索で新たに訪問し、答えを 1 増やす
    dfs(v, G, seen)
    ans.sort(reverse=True)
    for a in ans:
        ans2.append(a)
    ans=[]
print(*ans2)