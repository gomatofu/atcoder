n=int(input())
sum1=[0]*(n+1)
sum2=[0]*(n+1)
a=0
b=0
l=[[0 for _ in range(2)]for _ in range(n)]
for i in range(1,n+1):
  sum1[i]=sum1[i-1]
  sum2[i]=sum2[i-1]
  c,p=map(int,input().split())
  if c==1:
    sum1[i]+=p
  else:
    sum2[i]+=p

ans1=0
ans2=0
q=int(input())
for i in range(q):
  l,r=map(int,input().split())
  ans1=sum1[r]-sum1[l-1]
  ans2=sum2[r]-sum2[l-1]
  print(ans1,ans2)
  ans1=0
  ans2=0
  




