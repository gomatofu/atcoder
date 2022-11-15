import bisect
n,m=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
B.sort()

ans=float("inf")

for a in A:
  i=bisect.bisect_left(B, a)
  if 0 <= i -1 < m:
    B1 = B[i-1]
    ans = min(ans,abs(a-B1))
  if 0 <= i <m:
    B2 = B[i]
    ans = min(ans,abs(a-B2))
    
print(ans)
