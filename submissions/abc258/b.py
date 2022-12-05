N = int(input())
A = [input() for _ in range(N)]
ans = ""
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(N):
    for j in range(N):
        for k in range(8):
            num = ""
            for l in range(N):
                x = (i + dx[k] * l) % N
                y = (j + dy[k] * l) % N
                num += A[x][y]
                # print(num)
            ans = max(ans, num)
print(ans)
