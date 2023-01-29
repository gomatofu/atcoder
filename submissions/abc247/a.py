import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
S = list(input())
ans = []
ans.append('0')
for i in range(1,4):
    if S[i-1] == '1':
        ans.append('1')
    elif S[i-1] == '0':
        ans.append('0')
        
print(*ans,sep='')

