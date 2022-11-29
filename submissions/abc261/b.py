N=int(input())

A=[]

for i in range(N):
  a=list(input())
  A.append(a)
  
for i in range(N):
  for j in range(i+1,N):
    if A[i][j] =='W' and A[j][i]!='L':
      print('incorrect')
      exit()
    if A[i][j] =='L' and A[j][i]!='W':
      print('incorrect')
      exit()
    if A[i][j] =='D' and A[j][i]!='D':
      print('incorrect')
      exit()
  
print('correct')
