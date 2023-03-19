def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
A=LI()
ans = []

for i in range(N):
    if A[i] %2==0:
        ans.append(A[i])

print(*ans)
