H,W=map(int,input().split())
R,C=map(int,input().split())
cnt=0
if H==1:
    cnt+=0
elif R==1 or R==H:
    cnt+=1
else:
    cnt+=2

if W==1:
    cnt+=0
elif C==1 or C==W:
    cnt+=1
else:
    cnt+=2


print(cnt)
