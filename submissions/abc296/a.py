def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
S=LS()

for i in range(1,N):
    if S[i-1]==S[i]:
        print('No')
        exit()

print('Yes')
