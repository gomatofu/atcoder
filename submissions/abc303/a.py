def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
S=SS()
T=SS()
cnt=0

for i in range(N):
    if S[i] == '1' and T[i] == "l":
        cnt+=1
    elif S[i] == 'l' and T[i] == "1":
        cnt+=1
    elif S[i] == '0' and T[i] == "o":
        cnt+=1
    elif S[i] == 'o' and T[i] == "0":
        cnt+=1
    elif S[i] ==  T[i]:
        cnt+=1

if cnt == N:
    print('Yes')
else:
    print('No')
