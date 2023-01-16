A,B,K=map(int,input().split())
ans=A
cnt=0

while ans < B:
    ans = ans*K
    cnt+=1

print(cnt)
