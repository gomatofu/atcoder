h,w=map(int, input().split())
l=[[0 for _ in range(w)]for _ in range(h)]
ans=[[0 for _ in range(w)]for _ in range(h)]
row=[0]*h
column=[0]*w

# 計算前取得
for i in range(h):
  a=list(map(int, input().split())) 
  for j in range(w):
    l[i][j]=a[j]
    
# 列、行合計値取得    
for i in range(h):
  for j in range(w):
    row[i]+=l[i][j]
    column[j]+=l[i][j]
    
# 答え計算代入
for i in range(h):
  for j in range(w):
    ans[i][j]= row[i]+column[j]-l[i][j]

# 出力
for a in ans:
  print(*a)
