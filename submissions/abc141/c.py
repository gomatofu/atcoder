import collections
n,k,q=map(int,input().split())

l=[int(input()) for i in range(q)]
s=[k for _ in range(n)]
c = collections.Counter(l)
for i in range(n):
  s[i]-=(q-c[i+1])
  if s[i]>0:
    print('Yes')
  else:
    print('No')


   

