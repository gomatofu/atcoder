A,B,C,D,E,F,X=map(int,input().split())

def cal(a,b,c,X):
    cnt = 0
    ans = 0

    while True:
        # •à‚­
        for _ in range(a):
            cnt+=1
            ans+=b
            if cnt==X:
                return ans

        # ‹x‚Þ
        for _ in range(c):
            cnt+=1
            if cnt==X:
                return ans


Takahashi=cal(A,B,C,X)
Aoki=cal(D,E,F,X)

if Takahashi>Aoki:
    print('Takahashi')
elif Takahashi<Aoki:
    print('Aoki')
else:
    print('Draw')


