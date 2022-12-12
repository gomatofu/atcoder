N=int(input())
ans=[]
for i in range(N):
  pri=[]  
  for j in range(N):
    if i<j:
      break
    
    if i==j or j==0:
      pri.append(1)
    else:
      a=ans[i-1][j-1]+ans[i-1][j]
      pri.append(a)
  print(*pri)
  ans.append(pri)
