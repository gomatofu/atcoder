N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=[]
for _ in range(K):
  ans.append(0)

if N>=K:
  print(*A[K::],*ans)
else:
  print(*ans[0:N])
    
