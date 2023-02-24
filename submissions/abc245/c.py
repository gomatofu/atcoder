N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

dp=[[False]*N for i in range(2)]


dp[0][0]=True
dp[1][0]=True


for i in range(N-1):


    if dp[0][i]==True:
        if abs(A[i]-A[i+1])<=K:
            dp[0][i+1]=True

        if abs(A[i]-B[i+1])<=K:
            dp[1][i+1]=True

    if dp[1][i]==True:
        if abs(B[i]-A[i+1])<=K:
            dp[0][i+1]=True

        if abs(B[i]-B[i+1])<=K:
            dp[1][i+1]=True


if dp[0][N-1]==True or dp[1][N-1]==True:
    print("Yes")

else:
    print("No")
