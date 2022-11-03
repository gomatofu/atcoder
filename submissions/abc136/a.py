a,b,c=map(int,input().split())
ans=c-(a-b)
if ans<0:
  print(0)
else:
  print(ans)
