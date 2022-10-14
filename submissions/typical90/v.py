import math
from functools import reduce
num=0
ans=0
a,b,c=map(int,input().split())
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

num=my_gcd(a,b,c)

ans=(a//num-1)+(b//num-1)+(c//num-1) 
  
print(ans)
