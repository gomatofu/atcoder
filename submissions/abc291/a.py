def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

S=SS()

for i in range(len(S)):
    if S[i].isupper() == True:
        print(i+1)
        exit()
