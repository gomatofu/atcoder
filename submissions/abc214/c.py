N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))

ans=[None]*N
ans[0]=T[0]

for i in range(N*2):
  ans[(i+1)%N]=min(ans[i%N]+S[i%N],T[(i+1)%N])

for a in ans:
  print(a)
