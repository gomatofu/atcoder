N,M=map(int,input().split())
S = [list(input()) for _ in range(N)]
cnt=0
A=['o']*M

for i in range(N):
  for j in range(i+1,N):
    ans=[]
    for k in range(M):
      if S[i][k] =='o' or S[j][k] =='o':
        ans.append('o')
    if ans == A:
      cnt+=1
print(cnt)
