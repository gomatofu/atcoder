def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

import bisect

N,M=MI()
A=LI()
B=LI()
C=[]
C = A + B
C.sort()


A_sort=[]
B_sort=[]
for a in A:
    i = bisect.bisect_left(C, a)  # bisect_right‚Å‚à‚¢‚¢‚Å‚·
    A_sort.append(i+1)
print(*A_sort)

for b in B:
    i = bisect.bisect_left(C, b)  # bisect_right‚Å‚à‚¢‚¢‚Å‚·
    B_sort.append(i+1)
print(*B_sort)
