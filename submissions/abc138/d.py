# �󂯎��
N,Q=map(int, input().split())

# �Ȃ����Ă��钸�_�̃��X�g�����
# 1��2,3,4���Ȃ����Ă���Ȃ�connect[1]=[2,3,4]
connect=[[] for _ in range(N+1)]

# �󂯎��
for _ in range(N-1):
    a,b=map(int, input().split())
    # a����b�Ab����a���Ȃ����Ă���
    connect[a].append(b)
    connect[b].append(a)

# �e���_�̃J�E���^��p��
counter=[0]*(N+1)

# �󂯎��
for _ in range(Q):
    p,x=map(int, input().split())
    # p��counter��x�𑫂�
    counter[p]+=x

# que=����p�ӂ���
from collections import deque
que=deque()

# �X�^�[�g�n�_=1������
que.append(1)

# �K��ς݃`�F�b�N�����
# False�Ȃ�K��܂��ATrue�Ȃ�K��ς�
visited=[False]*(N+1)
# 1���X�^�[�g�n�_�͖K��ς݂ɂ���
visited[1]=True

# que=������ɂȂ�܂�
while len(que)>0:
    # ���̍�������o����now�Ɋi�[
    now=que.popleft()
    # now�̃J�E���^�̒l��now_number�Ɋi�[
    now_number=counter[now]
    # now����Ȃ����Ă��钸�_�����ɉ��=to
    for to in connect[now]:
        # �����܂��K��ς݂łȂ����
        if visited[to]==False:
            # counter��now�̃J�E���^�̒l�𑫂�
            counter[to]+=now_number
            # �K��ς݃`�F�b�N����
            visited[to]=True
            # ���ɓ����
            que.append(to)

# 0�ȊO��counter���o��
print(*counter[1:])
