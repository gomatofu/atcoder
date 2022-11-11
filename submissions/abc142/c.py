n=int(input())
l=list(map(int,input().split()))
ls=[0]*(n+1)
for cnt, itm in enumerate(l, start=1):
    ls[itm]= cnt

print(*ls[1::])
   
