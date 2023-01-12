H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]


rowSum=[]
for i in range(H):
    row=0
    for j in range(W):
        row+=A[i][j]
    rowSum.append(row)

clmSum=[]
for i in range(W):
    clm=0
    for j in range(H):
        clm+=A[j][i]
    clmSum.append(clm)

for i in range(H):
    ans=[]
    for j in range(W):
        cal=rowSum[i]+clmSum[j]-A[i][j]
        ans.append(cal)
    print(*ans,sep=' ')
