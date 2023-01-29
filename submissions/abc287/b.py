def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N,M=MI()
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
cnt=0

for s in S:
    s3=s[-3:]
    for t in T:
        if s3==t:
            cnt+=1
            break

print(cnt)
