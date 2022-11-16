import heapq
q=int(input())

hq=[]
s=0

for i in range(q):
  l=list(map(int,input().split()))
  if l[0]==1:
    x=l[1]
    heapq.heappush(hq,x-s)
  elif l[0]==2:
    x=l[1]
    s+=x
  else:
    x=heapq.heappop(hq)
    print(x+s)
    
  
