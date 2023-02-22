def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())
N,K=MI()
A=LI()
B=list(set(A))
B.sort()
cnt=0

for i in range(len(B)):
    if i != B[i]:
        print(i)
        exit()
    if cnt == K:
        print(cnt)
        exit()
    cnt += 1
print(max(B) + 1)
