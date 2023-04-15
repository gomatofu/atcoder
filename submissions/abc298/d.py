def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

from collections import deque

Q=II()
MOD = 998244353
S = deque([1])
POW10 = [1]
for _ in range(Q + 1):
    POW10.append(POW10[-1] * 10 % MOD)
current_hash = 1
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        S.append(x)
        current_hash = (current_hash * 10 + x) % MOD
        POW10.append(POW10[-1] * 10 % MOD)
    elif query[0] == 2:
        removed_num = S.popleft()
        current_hash = (current_hash - removed_num * POW10[len(S)] % MOD + MOD) % MOD
        POW10.pop()
    else:  # query[0] == 3
        print(current_hash)
