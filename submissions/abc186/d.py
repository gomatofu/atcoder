def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
A=LI()

A.sort()
ans=0
S=[0] * (N+1)
for i in range(N):
    S[i+1] = S[i] + A[i]

for i in range(N):
    ans += A[i] * i - S[i]

print(ans)
