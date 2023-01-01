from math import gcd


def aseq_sum(a1, d, n):
    return n * (2 * a1 + (n - 1) * d) // 2


def calc(x):
    return aseq_sum(x, x, N // x)


N, A, B = map(int, input().split())
lcm = (A * B) // gcd(A, B)
ans = aseq_sum(1, 1, N) - calc(A) - calc(B) + calc(lcm)
print(ans)
