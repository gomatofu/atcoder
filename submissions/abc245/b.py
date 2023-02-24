def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
N=II()
A=LI()
A=set(A)

for i in range(N+1):
    if i not in A:
        print(i) 
        exit()
