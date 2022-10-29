a,b,c,d,e,f=map(int,input().split())
s=(a*b*c)-(d*e*f)
w=998244353 
ans=s%w

print(ans)
