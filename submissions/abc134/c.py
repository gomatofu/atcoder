n=int(input())

l=[int(input()) for i in range(n)]
l2=sorted(l)

for i in range(n):
  if l[i]==l2[-1]:
    print(l2[-2])
  else:
    print(l2[-1])
