def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

S=LS()
num= len(S)//2

for i in range(num):
    S[2*i-2],S[2*i-1] = S[2*i-1],S[2*i-2]

print(*S,sep='')
