def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

X=[]
Y=[]
for i in range(3):
    x,y=MI()
    X.append(x)
    Y.append(y)

ansx=0
ansy=0

for i in range(3):
    if X.count(X[i]) == 1:
        ansx =X[i]
    if Y.count(Y[i]) == 1:
        ansy =Y[i]

print(ansx , ansy)
