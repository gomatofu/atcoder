def main():
    # ���炩����a, b����1�����āA0�n�܂�ɂ��Ă����܂�
    # �v�������ꍇ�́Ax // N , x % N �Ə������ق����Ȍ��ł�
    def get_index(x):
        if x < N:
            # 0 �` N - 1 �͑O��
            return 0, x
        else:
            # N ~ 2N - 1 �͌㔼�ł�
            return 1, x - N

    N = int(input())
    S = input()

    """
    ���̂悤�ȓ񎟌����X�g�ɂȂ�܂��B
    L[0]���O���AL[1]���㔼�̕����̃��X�g�ł��B
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
            # 1��������ւ��邾���Ȃ̂ŁA�y�������ł�
            ai, aj = get_index(a)
            bi, bj = get_index(b)
            L[ai][aj], L[bi][bj] = L[bi][bj], L[ai][aj]
        else:
            # 2�̃��X�g�̎Q�Ƃ����ւ��邾���Ȃ̂ŁA������y�������ł�
            L[0], L[1] = L[1], L[0]

    ans = ''.join(L[0]) + ''.join(L[1])  # ''.join()�ł������܂�
    print(ans)


if __name__ == '__main__':
    main()
