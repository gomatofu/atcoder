N=int(input())
LR = [list(map(int,input().split())) for _ in range(N)]
LR.sort()

nowL=LR[0][0]
nowR=LR[0][1]

for i in range(1,N):

    nextL=LR[i][0]
    nextR=LR[i][1]

    if nowR < nextL:
        print(nowL,nowR)
        nowL=LR[i][0]
        nowR=LR[i][1]
    else:
        if nowR < nextR:
            nowR = nextR

print(nowL,nowR)
