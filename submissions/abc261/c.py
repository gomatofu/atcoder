N=int(input())

from collections import defaultdict
scnt=defaultdict(int)

for i in range(N):
  s=input()
  
  if scnt[s]==0:
    print(s)
  else:
    print(s+"("+str(scnt[s])+")")
    
  scnt[s]+=1
   
