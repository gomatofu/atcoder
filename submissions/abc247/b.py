def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
N=II()
S = [input().split() for _ in range(N)]
for i in range(N):
    last=False
    first=False
    for j in range(2):
        for k in range(N):
            if i!=k and S[i][j] in S[k]:
                if j==0:
                    last=True
                else:
                    first=True
    if last and first:
        print('No')
        exit()
                

print('Yes')
