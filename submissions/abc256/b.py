N=int(input())
A=list(map(int,input().split()))
S=[]
cnt=0

for i in range(N):
  S.append(0)
  for j in range(len(S)):
    S[j] += A[i]
    if S[j] >= 4:
      cnt+=1
      S[j]=-1000
      
print(cnt)
