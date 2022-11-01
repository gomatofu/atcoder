import math

n,d=map(int,input().split())
l=[0]*n
for i in range(n):
  l[i]=list(map(int,input().split()))
  
cnt=0

for i in range(n):
  for j in range(i+1,n):
    s=0
    for k in range(d):
      s+=abs(l[i][k]-l[j][k])**2
    s=math.sqrt(s)
    if s%1==0:
      cnt+=1
  
print(cnt)
