n=int(input())
l=list(map(int,input().split()))

a=max(l)
ans=l.index(a)
print(ans+1)
