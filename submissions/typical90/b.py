import itertools
n = int(input())
 
for S in itertools.product(['(',')'], repeat=n):
    cnt = 0
    for s in S:
        if s =='(':
            cnt+=1
        else:
            cnt-=1
        if cnt < 0:
            break
    if cnt ==0:
        print(*S,sep='')
