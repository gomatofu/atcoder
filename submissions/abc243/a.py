def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

V,A,B,C=MI()

while True:
    if V<A:
        print('F')
        exit()
    V-=A

    if V<B:
        print('M')
        exit()
    V-=B

    if V<C:
        print('T')
        exit()
    V-=C
    
