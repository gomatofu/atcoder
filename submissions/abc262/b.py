N,M=map(int,input().split())
c=[[False]*(N+1) for _ in range(N+1)]

for i in range(M):
  u,m=map(int,input().split())
  c[u][m]=True
  c[m][u]=True
  
ans=0  
for i in range(1,N+1):
  for j in range(i+1,N+1):
    for k in range(j+1,N+1):
      if c[i][j] and c[j][k] and c[k][i]:
        ans+=1
        
print(ans)
