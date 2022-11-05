n=int(input())
l=list(map(int,input().split()))

l.sort()
s=l[0]
for i in range(1,n):
  s=(s+l[i])/2
print(s)
