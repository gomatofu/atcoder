n,m=map(int,input().split())
l2=0
r2=10**5
for i in range(m):
  l,r=map(int,input().split())
  l2=max(l2,l)
  r2=min(r,r2)

if l2>r2:
  print(0)
else:
  print(r2-l2+1)
