x=[int(i) for i in list(input())]
xs=set(x)

if len(xs)==1:
  print("Weak")
  exit()
  
cnt=0
for i in range(1,4):
  if x[i-1]+1==x[i]:
    cnt+=1

  if (x[i-1]+1)%10==0:
    cnt+=1
    
if cnt==3:
  print("Weak")
else:
  print("Strong")
