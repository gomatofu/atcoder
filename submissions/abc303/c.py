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
    x, y = 0, 0  # 初期位置は(0, 0)
    
    # アイテムの位置を辞書型に変換
    item_dict = {tuple(item): True for item in items}
    
    for i in range(N):
        # 体力を1消費して移動
        H -= 1
        if S[i] == 'R':
            x += 1
        elif S[i] == 'L':
            x -= 1
        elif S[i] == 'U':
            y += 1
        elif S[i] == 'D':
            y -= 1
        
        # 体力が負になった場合は倒れて移動をやめる
        if H < 0:
            return False
        
        # 移動した点にアイテムがあり、かつ体力がK未満ならばアイテムを消費して体力をKにする
        if (x, y) in item_dict and H < K:
            H = K
            del item_dict[(x, y)]
    
    return True

result = can_survive(N, M, H, K, S, items)
if result:
    print('Yes')
else:
    print('No')
