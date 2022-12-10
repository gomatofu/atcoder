N,T=map(int,input().split())
A=list(map(int,input().split()))
T=T%sum(A)

for i, t in enumerate(A):
    if t >= T:
        print(i+1, T)
        exit()
    T -= t
