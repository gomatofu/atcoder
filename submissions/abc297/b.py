def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

S=LS()
BF1=0
BF2=0
R=[]

for i in range(len(S)):
    if S[i]=='B':
        if i%2==0:
            BF1+=1
        else:
            BF2+=1
    if S[i]=='R':
        R.append(i)

if BF1==1 and BF2==1 and 'K'in S[R[0]:R[1]]:
    print('Yes')
else:
    print('No')


