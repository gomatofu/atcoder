T=int(input())


for  i in range(T):
  N=int(input())
  A=list(map(int,input().split()))
  cnt=0
  for j in range(N):
    if A[j] % 2 == 0:
        a=0
    else:
        cnt+=1
  print(cnt)
