a,b,c=map(int,input().split())
if a>c:
  s=c
  e=a
else:
  s=a
  e=c
for i in range(s,e+1):
  if b==i:
    print('Yes')
    exit()
    
print('No')
