import itertools
n=int(input())
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))
l=list(itertools.permutations(range(1,n+1)))
a=l.index(p)+1
b=l.index(q)+1

  
print(abs(a-b))
