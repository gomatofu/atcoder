H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

i,j=0,0
h = set()
p = (0, 0)

while True:
    if grid[i][j] == "U":
      if i==0:
        print(i+1,j+1)
        exit()
      else:
        i-=1
    elif grid[i][j] == "D":
      if i==H-1:
        print(i+1,j+1)
        exit()
      else:
        i+=1
    elif grid[i][j] == "L":
      if j==0:
        print(i+1,j+1)
        exit()
      else:
        j-=1
    elif grid[i][j] == "R":
      if j==W-1:
        print(i+1,j+1)
        exit()
      else:
        j+=1
    p = (i,j)
    if p in h:
        print(-1)
        exit()
    h.add(p)
