def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,K=MI()
l=[]
for i in range(K):
    S=SS()
    l.append(S)

l.sort()
for i in range(K):
    print(l[i])
