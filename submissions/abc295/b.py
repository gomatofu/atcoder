def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

R,C=MI()
grid = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j].isdecimal():
            for k in range(R):
                for l in range(C):
                    m = abs(i-k)+abs(j-l)
                    if int(grid[i][j])>=m and grid[k][l].isdecimal()==False:
                        grid[k][l]='.'
            grid[i][j]='.'

for i in range(R):
    print(*grid[i],sep='')
