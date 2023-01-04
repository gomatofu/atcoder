from collections import Counter
from itertools import product

N,K=map(int,input().split())
ans=0

S=[input() for _ in range(N)]
for pro in product((True, False), repeat=N):
    L=[]
    cnt=0

    for i in range(N):
        if pro[i]:
            L+=S[i]

    dic = Counter(L)
    for d in dic:
        if dic[d] == K:
            cnt += 1

    ans=max(ans,cnt)
print(ans)
    
