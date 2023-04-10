def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

H,W=MI()

for i in range(H):
    S=LS()
    for j in range(1,W):
        if S[j]=='T' and S[j-1]=='T':
            S[j-1],S[j] = 'P','C'
    print(*S,sep='')
