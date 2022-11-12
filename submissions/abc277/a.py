n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in  range(n):
  if k==l[i]:
    ans=i+1
    
print(ans)

