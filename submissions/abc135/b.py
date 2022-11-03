n=int(input())
l=list(map(int,input().split()))
ls=sorted(l)
cnt=0

for i in range(n):
  if l[i]!=ls[i]:
    cnt+=1
    
if cnt==0 or cnt==2:
  print('YES')
else:
  print('NO')
