def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,T=MI()
C=LI()
R=LI()
ans = 0


if C.count(T)>=1:
    for i in range(N):
        if C[i]==T:
            ans = max(ans,R[i])
    print(R.index(ans)+1)
else:
    for i in range(N):
        if C[0]==C[i]:
            ans = max(ans,R[i])
    print(R.index(ans)+1)
