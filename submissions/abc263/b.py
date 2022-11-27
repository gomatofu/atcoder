N=int(input())
P=list(map(int,input().split()))

cnt=0

while N!=1:
  N=P[N-2]
  cnt+=1
  
print(cnt)
