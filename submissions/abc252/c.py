# 入力の受け取り
N=int(input())

# 「0」~「9」の表示秒数記録リスト
# 0：[0,1,2,3]⇔Time[0]=[0,1,2,3]　というように記録する
Time=[[] for i in range(10)]

# 各数の出現回数を数えるリスト
# C[1][2]=3なら「1」の表示秒数に2が3回表示された　という意味
Count=[[0]*10 for i in range(10)]

# N回
for i in range(N):
    # 入力の受け取り
    S=input()
    
    # x=0~9
    for x in range(10):
        # Sのx文字目を整数へ変換
        Sint=int(S[x])

        # 出現回数をプラス1
        Count[Sint][x]+=1
        # 表示秒数を記録
        # (出現回数-1)*10をプラスする
        Time[Sint].append(x+(Count[Sint][x]-1)*10)

# 答え
# 初期値は大きめの数にしておく
ans=10**15

# i=0~9
for i in range(10):
    # 「i」を揃えるための秒数
    # ⇔Time[i]の最大
    # これまでの答えより小さければ更新
    ans=min(ans,max(Time[i]))

# 答えを出力
print(ans)
