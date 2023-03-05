from collections import deque
N,M=[int(nm) for nm in input().split()]
# ���ȃ��[�v�ӂ̐����Ǘ�
table=[0 for _ in range(N)]
G=[[] for _ in range(N)]
for _ in range(M):
    u,v=[int(a)-1 for a in input().split()]
    if u==v:
        table[u]+=1
    else:
        G[u].append(v)
        G[v].append(u)

seen=[False for _ in range(N)]
for i in range(N):
    if seen[i]:
        continue

    que=deque()
    que.append(i)
    # ���̘A�������Ɋ܂܂�钸�_�ƕӂ̑���
    e,v=0,0
    # ���̘A�������Ɋ܂܂�鎩�ȃ��[�v�ӂ̑���
    eself=0
    while que:
        now=que.popleft()
        v+=1
        eself+=table[now]
        seen[now]=True
        for nex in G[now]:
            e+=1
            if not seen[nex]:
                seen[nex]=True
                que.append(nex)
    
    # �ӂ�2�x�������Ă���
    if v!=e//2+eself:
        print("No")
        exit()

# �S�A�������ŏ����𖞂�����
print("Yes")
