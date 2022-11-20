H,M=map(int,input().split())
for i in range(24):
  if H==24:
    H=0
  if H%10 <6 and H//10!=2:
    print(H,M)
    exit()
  elif H//10==2 and M//10<4:
    print(H,M)
    exit()
    
  for j in range(60):
    M+=1
  H+=1
  M=0
