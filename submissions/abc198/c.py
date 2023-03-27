def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

import math

R,X,Y=MI()
D=math.sqrt(X**2 + Y**2)
if D < R:
    print(2)
else:
    print(math.ceil(D/R))
