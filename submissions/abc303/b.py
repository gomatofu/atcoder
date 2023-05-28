def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
import math
def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

N,M = MI()
A =[]
c = combinations_count(N, 2)
for i in range(M):
    a = LI()
    A.append(a)

l=[]
for i in range(M):
    for j in range(1,N):
        if A[i][j-1] > A[i][j]:
            s,t = A[i][j-1] , A[i][j]
        else: 
            s,t =  A[i][j] , A[i][j-1]
        l.append([s,t])

arr = list(map(list, set(map(tuple, l))))

print(c - len(arr))
