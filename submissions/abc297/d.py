def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())


A,B = MI()
ans=0
if A<B:
    A,B = B,A

while B>0:
    ans+=A//B
    A%=B
    A,B = B,A
print(ans-1)
