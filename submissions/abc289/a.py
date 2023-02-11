def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

s=list(input())

for i in range(len(s)):
    if s[i]=='1':
        s[i]='0'
    else:
        s[i]='1'

print(*s,sep='')