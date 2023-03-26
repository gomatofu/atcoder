def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
from collections import defaultdict
N=II()
A=LI()
ACount=defaultdict(int)
ans=0
cnt=0

for a in A:
    ACount[a-1]+=1
    ACount[a]+=1
    ACount[a+1]+=1

print(max(ACount.values()))
