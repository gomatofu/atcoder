import math
from decimal import Decimal

A,B=input().split()
A=Decimal(A)
B=Decimal(B)
ans = A*B
ans=math.floor(ans)
print(ans)
