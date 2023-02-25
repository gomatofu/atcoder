def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
from collections import defaultdict

N=II()
p=[]
y_set=set()
for i in range(N):
    x,y=MI()
    p.append([x,y])
    y_set.add(y)

S=LS()

dictL = defaultdict(list)
dictR = defaultdict(list)

for i in range(N):
    x,y=p[i]

    if S[i] == 'L':
        dictL[y].append(x)
    else:
        dictR[y].append(x)

for y in y_set:
    if 1 <= len(dictL[y]) and 1 <= len(dictR[y]):
        if min(dictR[y]) < max(dictL[y]):
            print('Yes')
            exit()

print('No')
