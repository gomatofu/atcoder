H,W=map(int,input().split())
L = [list(input()) for _ in range(H)]

x=[]
y=[]

for i in range(H):
  for j in range(W):
    if L[i][j]=='o':
      x.append(i)
      y.append(j)
      
ans=abs(x[0]-x[1])+abs(y[0]-y[1])
print(ans)
