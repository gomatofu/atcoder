N=int(input())
S=list(input())
index=[]
cnt=0

for i in range(N):
  if S[i]=='\"':
    cnt+=1
    
  if cnt% 2 == 0 and S[i]==',':
    index.append(i)

for i in index:
  S[i]='.'

print(*S,sep='')
