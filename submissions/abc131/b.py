n,l=map(int,input().split())

lis=[0]*n

for i in range(n):
  lis[i]=l+i
 
s=set(lis)

if 0 in s:
  print(sum(lis))
elif lis[0]<0:
  print(sum(lis)-lis[-1])
else:
  print(sum(lis)-lis[0])
