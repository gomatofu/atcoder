def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
A,B,C,D=MI()
if A<C:
    print('Takahashi')
elif C<A:
    print('Aoki')
else:
    if B<=D:
        print('Takahashi')
    else:
        print('Aoki')
