N,A,B=map(int,input().split())

flg=True

for i in range(A*N):
    L=[]
    m2=i//A
    if m2 % 2 == 0:
        flg=True
    else:
        flg=False
        
    for j in range(B*N):
        m=j//B
        if flg:
            if m % 2 == 0:
                L.append('.')
            else:
                L.append('#')
        else:
            if m % 2 == 0:
                L.append('#')
            else:
                L.append('.')
    
    
    print(*L,sep='')
