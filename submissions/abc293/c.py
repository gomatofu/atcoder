from itertools import product
from collections import Counter
H, W = map(int, input().split())
A = [[]]
for i in range(H):
    side = [-1] + list(map(int, input().split()))
    A.append(side)

ans_set = set()
 
for bits in product([0, 1], repeat=H+W-2):
    C = Counter(bits)
    if C[0] == H - 1:
        ans_set.add(bits)
 
ans_list = list(ans_set)

cnt=0
for pro in ans_list:
    ans=set()
    x,y = 1,1
    ans.add(A[x][y])
    for p in pro:
        if p==0:
            x+=1
            ans.add(A[x][y])
        if p==1:
            y+=1
            ans.add(A[x][y])
    if  len(ans) == H+W-1:
        cnt+=1
print(cnt)
