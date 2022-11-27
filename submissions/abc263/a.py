import collections

l=list(map(int,input().split()))

c = collections.Counter(l)
for ans in c.values():
  if not (ans==2 or ans==3):
    print('No')
    exit()  
print('Yes')
