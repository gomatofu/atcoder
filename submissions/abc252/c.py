# ���͂̎󂯎��
N=int(input())

# �u0�v~�u9�v�̕\���b���L�^���X�g
# 0�F[0,1,2,3]��Time[0]=[0,1,2,3]�@�Ƃ����悤�ɋL�^����
Time=[[] for i in range(10)]

# �e���̏o���񐔂𐔂��郊�X�g
# C[1][2]=3�Ȃ�u1�v�̕\���b����2��3��\�����ꂽ�@�Ƃ����Ӗ�
Count=[[0]*10 for i in range(10)]

# N��
for i in range(N):
    # ���͂̎󂯎��
    S=input()
    
    # x=0~9
    for x in range(10):
        # S��x�����ڂ𐮐��֕ϊ�
        Sint=int(S[x])

        # �o���񐔂��v���X1
        Count[Sint][x]+=1
        # �\���b�����L�^
        # (�o����-1)*10���v���X����
        Time[Sint].append(x+(Count[Sint][x]-1)*10)

# ����
# �����l�͑傫�߂̐��ɂ��Ă���
ans=10**15

# i=0~9
for i in range(10):
    # �ui�v�𑵂��邽�߂̕b��
    # ��Time[i]�̍ő�
    # ����܂ł̓�����菬������΍X�V
    ans=min(ans,max(Time[i]))

# �������o��
print(ans)
