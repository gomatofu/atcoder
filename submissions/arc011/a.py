def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

m,n,N = MI()

T=N
while N>=m:
	N-=(m-n)
	T+=n

print(T)
