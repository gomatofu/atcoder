n=int(input())
a,b,c=list(map(int,input().split()))
num=9999
ans=9999
for i in range(num):
  for j in range(num-i):
    cz=n-a*i-b*j
    if cz<0:
      break
    if cz%c==0:
      ans=min(ans,i+j+cz//c)
print(ans)
