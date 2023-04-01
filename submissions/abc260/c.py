def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,X,Y=MI()

r=[0] *(N+1)
b=[0] *(N+1)
r[N]=1

for n in range(N,1,-1):
    r[n-1] += r[n]
    b[n] += r[n] * X
    r[n] = 0

    r[n-1] += b[n]
    b[n-1] += b[n] * Y
    b[n] = 0

print(b[1])
