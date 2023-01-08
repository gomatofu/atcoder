from itertools import product
import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = II()

for pro in product(('(', ')'), repeat=N):
    cnt = 0

    for p in pro:
        if p == '(':
            cnt+=1
        else:
            cnt-=1
        
        if cnt < 0:
            break
    
    if cnt == 0:
        print(*pro,sep='')
