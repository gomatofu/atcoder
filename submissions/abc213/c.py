h,w,n=map(int,input().split())
row=[]
clm=[]
for i in range(n):
  r,c=map(int,input().split())
  row.append(r)
  clm.append(c)
  
rows=sorted(set(row))
clms=sorted(set(clm))
dr={}
dc={}

dr = {x: i for i, x in enumerate(rows, 1)}
dc = {x: i for i, x in enumerate(clms, 1)}
  
for r,c in zip(row,clm):
  print(dr[r],dc[c])
