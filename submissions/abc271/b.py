N,Q=map(int,input().split())
l=[[None] * (10*9) for _ in range(N)]
for i in range(N):
  L=list(map(int,input().split()))
  l[i]=L[1::]

for i in range(Q):
  S,T=map(int,input().split())
  S=S-1
  T=T-1
  print(l[S][T])
