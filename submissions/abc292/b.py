def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,Q=MI()
ans = [[0] * 2 for _ in range(N+1)]

for i in range(Q):
    evt,x = MI()

    if evt == 1:
        ans[x][0]+=1
    elif evt == 2:
        ans[x][1]+=1
    else:
        if ans[x][0]>=2 or ans[x][1]>=1:
            print('Yes')
        else:
            print('No')



