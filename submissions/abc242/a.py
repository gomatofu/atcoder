def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

A,B,C,X = MI()
if A >= X:
    print('{:.12f}'.format(1))
elif B < X:
    print('{:.12f}'.format(0))
else:
    ans = C/(B-A)
    print('{:.12f}'.format(ans))
