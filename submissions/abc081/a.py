def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

from collections import defaultdict
N,K=MI()
A=LI()

ACount=defaultdict(int)

for a in A:
    ACount[a]+=1


ACount = sorted(ACount.items(), key=lambda x:x[1])
if len(ACount) <= K:
    print(0)
else:
    vcnt=0
    for i in range(len(ACount)):
        vcnt+=ACount[i][1]
        cnt = len(ACount) - (i+1)
        if cnt <=K:
            print(vcnt)
            exit()

    
