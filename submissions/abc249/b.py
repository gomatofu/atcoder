S=list(input())
l=[]
upcnt=0
lowcnt=0

for i in range(len(S)):
    if S[i].isupper():
        upcnt+=1
    else:
        lowcnt+=1

    l.append(S[i])

l=set(l)
l=list(l)

if len(l)==len(S) and upcnt>0 and lowcnt>0:
    print('Yes')
else:
    print('No')
