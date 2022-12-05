N,X=map(int,input().split())
S='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''

for i in range(26):
  ans+=S[i]*N
  
print(ans[X-1])
