def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
N=II()
S=LS()
if 'o' in S and 'x' not in S:
    print('Yes')
else:
    print('No')
