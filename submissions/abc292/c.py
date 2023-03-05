def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N = int(input())
from collections import defaultdict
d = defaultdict(int)


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

for i in range(1, N):
    d[i] = len(make_divisors(i))


ans = 0
for i in d:
    ans += d[i]*d[N-i]
    
print(ans)
