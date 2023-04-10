def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,D=MI()
T=LI()

for i in range(1,N):
    if T[i]-T[i-1]<=D:
        print(T[i])
        exit()

print(-1)
