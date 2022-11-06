a,b=map(int,input().split())
s=0
cnt=0
if b==1:
  print(0)
  exit()
while s<b:
  s+=a
  cnt+=1
  if cnt>1:
    s-=1

print(cnt)
