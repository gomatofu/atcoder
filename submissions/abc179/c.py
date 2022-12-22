def solve():
    ans = 0
    for a in range(1, N):
        for b in range(1, N):
            c = N - a * b
            if c <= 0:
                break
            ans += 1
    return ans


N = int(input())
ans = solve()
print(ans)
