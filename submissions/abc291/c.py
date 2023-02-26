from queue import Queue

# 四方向への移動を表すベクトル
# 0: 下、1: 右、2: 上、3: 左
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 入力
N=int(input())
S=list(input())

S_set = set()
x,y = 0 , 0
S_set.add((x,y))

for s in S:
    if s == 'R':
        x, y = x + 1, y
    elif s == 'L':
        x, y = x - 1, y
    elif s == 'U':
        x, y = x , y + 1
    elif s == 'D':
        x, y = x , y - 1

    if (x,y) in S_set:
        print('Yes')
        exit()

    S_set.add((x,y))
        
# マス (X1, Y1) の値を答える
print('No')
