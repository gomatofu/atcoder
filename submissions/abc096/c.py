def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

H,W=MI()
S=[LS() for _  in range(H)]
visit = [['.' for i in range(W)]for _ in range(H)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            for dx , dy in zip(dxs,dys):
                x , y = dx+w,dy+h
                if 0<=x<W and 0<=y<H and S[y][x] == '#':
                    visit[h][w] = visit[y][x] = '#'

for h in range(H):
    for w in range(W):
        if S[h][w] != visit[h][w]:
            print('No')
            exit()

print('Yes')




