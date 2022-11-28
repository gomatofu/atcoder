N=int(input())
A=[0]+list(map(int,input().split()))

ans=0
cnt=0

for i in range(1,N+1):
  if A[i]==i:
    cnt+=1
    
  j=A[i]
  if i<j and A[j]==i:
    ans+=1
    
ans+=cnt*(cnt-1)//2

print(ans)
