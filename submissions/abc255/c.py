# ���͂̎󂯎��
X,A,D,N=map(int,input().split())

# S��i���ڂ��v�Z����֐�
def S(i):
    return A+(i-1)*D

# D���v���X�̏ꍇ�̓񕪒T��
def NibutanPlus(X):

    # (1)���[��,�E]���w�肷��
    l=0
    r=N

    # (4)1<(�E-��)�ƂȂ��Ă����(2)~(4)���J��Ԃ�
    while 1<r-l:
        # (2)����=(��+�E)//2�������𖞂������m�F
        # (3)(2)�̌��ʂ�荶�܂��͉E���X�V����
        c=(l+r)//2

        if S(c)<=X:
            # ��=�����ƍX�V
            l=c
        else:
            # �E=�����ƍX�V
            r=c

    # l,r��Ԃ�
    return l,r

# D���}�C�i�X�̏ꍇ�̓񕪒T��
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

# D��0�̏ꍇ
if D==0:
    # |A-X|������
    print(abs(A-X))

# D���v���X�̏ꍇ
elif 0<D:
    # X��������菬�����ꍇ
    if X<A:
        # (A-X)������
        print(A-X)
    # X���������傫���ꍇ
    elif S(N)<=X:
        # (X-����)������
        print(X-S(N))
    # ��L�ȊO
    else:
        # �񕪒T���łǂ̍��̊Ԃɂ��邩�m�F
        l,r=NibutanPlus(X)
        # �����������ق�������
        print(min(X-S(l),S(r)-X))

# D���}�C�i�X�̏ꍇ
else:
    # X���������傫���ꍇ
    if A<X:
        # (X-A)������
        print(X-A)
    # X��������菬�����ꍇ
    elif X<=S(N):
        # (����-X)������
        print(S(N)-X)
    # ����ȊO
    else:
        # �񕪒T���łǂ̍��̊Ԃɂ��邩�m�F
        l,r=NibutanMinus(X)
        # �����������ق�������
        print(min(S(l)-X,X-S(r)))
