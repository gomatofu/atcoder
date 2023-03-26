def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
W=list(input().split(' '))

w=['and','not','that','the','you']

for i in range(N):
    if W[i] in w:
        print('Yes')
        exit()

print('No')
