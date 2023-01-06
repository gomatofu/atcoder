n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum=0
for i in range(n):
  sum+=abs(a[i]-b[i])
  
if sum>k:
  print('No')
elif sum%2!=k%2:
  print('No')
else:
  print('Yes')
