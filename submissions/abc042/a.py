l=list(map(int,input().split()))

cnt5=0
cnt7=0
for i in range(3):
  if l[i]==5:
    cnt5+=1
  elif l[i]==7:
    cnt7+=1
    
if cnt5==2 and cnt7==1:
  print('YES')
else:
  print('NO')
