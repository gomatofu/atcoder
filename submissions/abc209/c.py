N=int(input())
C=list(map(int,input().split()))
mod=10**9+7
C.sort()
ans=1

for i in range(N):
  ans=ans*(C[i]-i)%mod
  
print(ans)
