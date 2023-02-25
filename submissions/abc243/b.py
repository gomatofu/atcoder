def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
A=LI()
B=LI()

cnt1=0
cnt2=0
C=set(B)

for i in range(N):

    if A[i]==B[i]:
        cnt1+=1
    elif A[i] in C:
        cnt2+=1

print(cnt1)
print(cnt2)
