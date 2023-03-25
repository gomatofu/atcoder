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

for a in A:
    ACount[a]+=1

    if ACount[a]%2==0:
        ans+=1

print(ans)
