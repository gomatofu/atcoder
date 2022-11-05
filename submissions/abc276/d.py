import math
n=int(input())
a=list(map(int,input().split()))
cnt=0 
l=[]
g=0  
for i in a: 
  g=math.gcd(g,i)


for i in range(n):
  a[i]//=g
  while a[i] % 2 == 0:
    a[i] //= 2
    cnt += 1
    
  while a[i] % 3 == 0:
    a[i] //= 3
    cnt += 1
    
  l.append(a[i])
    
se=set(l)
if len(se)==1:
  print(cnt)
else:
  print(-1)
