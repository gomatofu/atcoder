N,Q=map(int,input().split())
from collections import defaultdict
d={}
d=defaultdict(int)

for i in range(Q):
  T,A,B=input().split()
  A=A.zfill(10)
  B=B.zfill(10)
  if T=='1':
    d[A+B]=1
  elif T=='2':
    d[A+B]=0
  else:
    if d[A+B]==1 and d[B+A]==1:
      print('Yes')
    else:
      print('No')
      
    
   
  

