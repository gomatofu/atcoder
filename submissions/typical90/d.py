h,w=map(int, input().split())
l=[[0 for _ in range(w)]for _ in range(h)]
ans=[[0 for _ in range(w)]for _ in range(h)]
row=[0]*h
column=[0]*w

# �v�Z�O�擾
for i in range(h):
  a=list(map(int, input().split())) 
  for j in range(w):
    l[i][j]=a[j]
    
# ��A�s���v�l�擾    
for i in range(h):
  for j in range(w):
    row[i]+=l[i][j]
    column[j]+=l[i][j]
    
# �����v�Z���
for i in range(h):
  for j in range(w):
    ans[i][j]= row[i]+column[j]-l[i][j]

# �o��
for a in ans:
  print(*a)