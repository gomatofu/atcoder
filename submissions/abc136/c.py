n=int(input())
l=list(map(int,input().split()))

for i in range(n-2,-1,-1):
  if l[i+1]<l[i]:
    l[i]-=1
    if l[i+1]<l[i]:
      print('No')
      exit()

print('Yes')
