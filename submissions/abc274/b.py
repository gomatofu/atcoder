h,w=map(int,input().split())
l=[[0 for _ in range(w)]for _ in range(h)]

for i in range(h):
  l[i]=input()
  
ans=[0]*w
cnt=0
for i in range(w):
  for j in range(h):
    if l[j][i]=='#':
      cnt+=1
  ans[i]=cnt
  cnt=0
print(*ans)
