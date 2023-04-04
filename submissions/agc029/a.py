def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
from collections import deque
S=LS()
SD=deque(S)
cnt=0
ans=0

for i in range(len(S)):
    sd = SD.popleft()
    if sd == 'W':
        cnt+=1
        sum=(i+1)-cnt
        ans+=sum

    
print(ans)
