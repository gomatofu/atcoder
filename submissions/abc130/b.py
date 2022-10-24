n,x=map(int,input().split())
l=list(map(int,input().split()))
sum=[0]*(n+1)

for i in range(1,n+1):
  sum[i]=sum[i-1]+l[i-1]

cnt=0
for s in sum:
  if s<=x:
    cnt+=1
    
print(cnt)
