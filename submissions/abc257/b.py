N,K,Q=map(int,input().split())
A=list(map(int,input().split()))
L=list(map(int,input().split()))

for i in range(Q):
  index=L[i]-1
  if A[index]+1 not in A and A[index]!=N:
    A[index]+=1
    
print(*A)
