import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = II()
S = list(input())
S.insert(0, '')
for i in range(1,N):
    cnt=0
    for j in range(1,N+1):
        if j+i<N+1:
            if S[j]!=S[j+i]:
                cnt+=1
            else:
                break
    print(cnt)
        
