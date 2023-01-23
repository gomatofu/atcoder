import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N,P,Q,R,S=map(int,input().split())
A = LI()
B=[]

num = Q-P+1
for i in range(num):
    A[P-1+i],A[R-1+i] = A[R-1+i] ,A[P-1+i]

print(*A)
