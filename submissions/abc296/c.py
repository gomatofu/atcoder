def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,X=MI()
A=LI()

A_set=set(A)

for i in range(N):
    s=A[i]-X
    if s in A_set:
        print('Yes')
        exit()

print('No') 
