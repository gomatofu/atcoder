def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,M,H,K = MI()
S = LS()
items = []
for _ in range(M):
        x, y = map(int, input().split())
        items.append((x, y))

def can_survive(N, M, H, K, S, items):
    x, y = 0, 0  # �����ʒu��(0, 0)
    
    # �A�C�e���̈ʒu�������^�ɕϊ�
    item_dict = {tuple(item): True for item in items}
    
    for i in range(N):
        # �̗͂�1����Ĉړ�
        H -= 1
        if S[i] == 'R':
            x += 1
        elif S[i] == 'L':
            x -= 1
        elif S[i] == 'U':
            y += 1
        elif S[i] == 'D':
            y -= 1
        
        # �̗͂����ɂȂ����ꍇ�͓|��Ĉړ�����߂�
        if H < 0:
            return False
        
        # �ړ������_�ɃA�C�e��������A���̗͂�K�����Ȃ�΃A�C�e��������đ̗͂�K�ɂ���
        if (x, y) in item_dict and H < K:
            H = K
            del item_dict[(x, y)]
    
    return True

result = can_survive(N, M, H, K, S, items)
if result:
    print('Yes')
else:
    print('No')
