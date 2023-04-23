def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
S=LS()
cnt=0

for i in range(N):
    if S[i]=='|':
        cnt+=1

    if cnt==1 and S[i]=='*':
        print('in')
        exit()

print('out')

