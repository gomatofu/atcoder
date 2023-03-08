def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
mod = 998244353

dp = [[0]*10 for _ in range(N+1)]

for i in range(1,10):
    dp[1][i] = 1

for d in range(2,N+1):
    for i in range(1,10):
        if i == 1:
            dp[d][i] = dp[d-1][i] + dp[d-1][i+1]
        elif 2<= i <= 8:
            dp[d][i] = dp[d-1][i-1] + dp[d-1][i] + dp[d-1][i+1]
        elif i == 9:
            dp[d][i] = dp[d-1][i-1] + dp[d-1][i]

        dp[d][i] %= mod
        
print(sum(dp[N])%mod)
