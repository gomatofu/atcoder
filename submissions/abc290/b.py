def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,K=MI()
S=LS()
cnt=0

for i in range(N):
    if cnt==K:
        S[i]='x'
    elif S[i]=='o':
        cnt+=1

print(*S,sep='')

