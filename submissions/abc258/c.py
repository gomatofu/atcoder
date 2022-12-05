N,Q=map(int,input().split())
S=input()
start=0

for i in range(Q):
  flg,x=map(int,input().split())
  if flg==1:
    start=(start-x)%N
  elif flg==2:
    print(S[(start+x-1)%N])
