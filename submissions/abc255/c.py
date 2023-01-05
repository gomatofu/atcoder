# 入力の受け取り
X,A,D,N=map(int,input().split())

# Sのi項目を計算する関数
def S(i):
    return A+(i-1)*D

# Dがプラスの場合の二分探索
def NibutanPlus(X):

    # (1)区間[左,右]を指定する
    l=0
    r=N

    # (4)1<(右-左)となっている間(2)~(4)を繰り返す
    while 1<r-l:
        # (2)中央=(左+右)//2が条件を満たすか確認
        # (3)(2)の結果より左または右を更新する
        c=(l+r)//2

        if S(c)<=X:
            # 左=中央と更新
            l=c
        else:
            # 右=中央と更新
            r=c

    # l,rを返す
    return l,r

# Dがマイナスの場合の二分探索
def NibutanMinus(X):
    l=0
    r=N

    while 1<r-l:
        c=(l+r)//2

        if S(c)<=X:
            r=c
        else:
            l=c

    return l,r

# Dが0の場合
if D==0:
    # |A-X|が答え
    print(abs(A-X))

# Dがプラスの場合
elif 0<D:
    # Xが初項より小さい場合
    if X<A:
        # (A-X)が答え
        print(A-X)
    # Xが末項より大きい場合
    elif S(N)<=X:
        # (X-末項)が答え
        print(X-S(N))
    # 上記以外
    else:
        # 二分探索でどの項の間にあるか確認
        l,r=NibutanPlus(X)
        # 差が小さいほうが答え
        print(min(X-S(l),S(r)-X))

# Dがマイナスの場合
else:
    # Xが初項より大きい場合
    if A<X:
        # (X-A)が答え
        print(X-A)
    # Xが末項より小さい場合
    elif X<=S(N):
        # (末項-X)が答え
        print(S(N)-X)
    # それ以外
    else:
        # 二分探索でどの項の間にあるか確認
        l,r=NibutanMinus(X)
        # 差が小さいほうが答え
        print(min(S(l)-X,X-S(r)))
