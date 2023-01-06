from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
for i in range(q):
    b=int(input())
    l=bisect_left(a,b)
    if n==l:
      print(abs(a[l-1]-b))
    else:
      print(min(abs(a[l-1]-b),abs(a[l]-b)))
