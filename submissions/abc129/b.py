n=int(input())
l=list(map(int,input().split()))
ans=10000000
s1=0
s2=sum(l)

for i in range(n):
  s2-=l[i]
  s1+=l[i]
  ans=min(ans,abs(s2-s1))
print(ans)
