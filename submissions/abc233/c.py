from itertools  import product
from math import prod
N,X=map(int,input().split())
L=[]
for _ in range(N):
    lis = list(map(int,input().split()))
    a,t = lis[0],lis[1:]
    L.append(t)

cnt=0

for l in product(*L):
    if prod(l) == X:
        cnt+=1

print(cnt)

