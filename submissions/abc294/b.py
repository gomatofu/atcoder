def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

H,W=MI()
alfa = ['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
A = [LI() for _ in range(H)]

for i in range(H):
    ans = []
    for j in range(W):
        for k in range(27):
            if A[i][j] == k:
                ans.append(alfa[k])
        
    print(*ans,sep='')
