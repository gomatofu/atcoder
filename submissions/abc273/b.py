x,k=map(int, input().split())
pow10=1
m=1
for i in range(k):
  x//=pow10
  m=x%10
  if m<=4:
    x-=m
  else:
    x+=(10-m)
  x*=pow10
  pow10*=10
print(x)
