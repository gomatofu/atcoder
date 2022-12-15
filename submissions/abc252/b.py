N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
index=[]
for i in range(N):
  if A[i]==max(A):
    index.append(i+1)

for b in B:
  for i in index:
    if b==i:
      print('Yes')
      exit()
      
print('No')
