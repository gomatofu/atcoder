def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
import itertools
import sys
sys.setrecursionlimit(1000000)

N,M=MI()
A =[]

for i in range(M):
    n=II()
    C=LI()
    A.append(C)

L=[]
for i in range(1,N+1):
    L.append(i)

cnt=0
for i in range(1,M+1):
    for pair in itertools.combinations(A, i):
        AC=list(set(itertools.chain.from_iterable(pair)))
        AC.sort()
        if L==AC:
            cnt+=1

print(cnt)
        