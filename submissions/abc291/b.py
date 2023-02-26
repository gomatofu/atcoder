def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
X=LI()
num=len(X)-2*N


X.sort(reverse=True)
X=X[N::]
X.sort()
X=X[N::]

ans=sum(X)/num
print("{:.15f}".format(ans))
