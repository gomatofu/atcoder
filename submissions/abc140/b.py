n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
cnt=sum(b)
s=0

for i in range(1,n):
  s=a[i]-a[i-1]
  if s==1:
    cnt+=c[a[i-1]-1]

print(cnt)
