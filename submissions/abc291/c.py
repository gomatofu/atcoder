from queue import Queue

# �l�����ւ̈ړ���\���x�N�g��
# 0: ���A1: �E�A2: ��A3: ��
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# ����
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
        
# �}�X (X1, Y1) �̒l�𓚂���
print('No')
