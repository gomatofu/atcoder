n,m=map(int,input().split())
l=[[] for i in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  l[a].append(b)
  l[b].append(a)
  

for i in range(1,len(l)):
  l[i].sort()
  print(len(l[i]),*l[i])
