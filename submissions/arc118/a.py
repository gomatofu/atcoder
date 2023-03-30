def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

t,N=MI()
s=set()

for i in range(100):
    s.add((100+t)* i  // 100 )

noP=[]
for i in range(100 + t):
    if i not in s:
        noP.append(i)

q, r = divmod(N-1, t)
ans = (100+t) * q + noP[r]
print(ans)
