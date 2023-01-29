import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = II()
cnt=0
for i in range(N):
    S=SS()
    if S=='For':
        cnt+=1
    else:
        cnt-=1

if cnt>0:
    print('Yes')
else:
    print('No')
