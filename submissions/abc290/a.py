def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,M=MI()
A=LI()
B=LI()
s=0

for b in B:
    s+=A[b-1]

print(s)
