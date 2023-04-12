def main():
    # あらかじめa, bから1引いて、0始まりにしておきます
    # 思いついた場合は、x // N , x % N と書いたほうが簡潔です
    def get_index(x):
        if x < N:
            # 0 ～ N - 1 は前半
            return 0, x
        else:
            # N ~ 2N - 1 は後半です
            return 1, x - N

    N = int(input())
    S = input()

    """
    このような二次元リストになります。
    L[0]が前半、L[1]が後半の文字のリストです。
    L = [['F', 'L'],
         ['I', 'P']]
    """
    _first = list(S[:N])
    _second = list(S[N:])
    L = [_first, _second]

    Q = int(input())
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            # 1文字入れ替えるだけなので、軽い処理です
            ai, aj = get_index(a)
            bi, bj = get_index(b)
            L[ai][aj], L[bi][bj] = L[bi][bj], L[ai][aj]
        else:
            # 2つのリストの参照を入れ替えるだけなので、これも軽い処理です
            L[0], L[1] = L[1], L[0]

    ans = ''.join(L[0]) + ''.join(L[1])  # ''.join()でくっつけます
    print(ans)


if __name__ == '__main__':
    main()
