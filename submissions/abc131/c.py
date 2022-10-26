import math

a,b,c,d=map(int,input().split())
g=c*d // math.gcd(c, d)
s1=b-(b//c)-(b//d)+(b//g)
a2=a-1
s2=a2-(a2//c)-(a2//d)+(a2//g)
print(s1-s2)
