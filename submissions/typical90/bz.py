N,M=map(int,input().split())
num=[0]*(N+1)
for _ in range(M):
  a,b=map(int,input().split())
  if a>b:
    num[a]+=1
  else:
    num[b]+=1

c=0
for a in num:
  if a==1:
    c+=1
print(c)
