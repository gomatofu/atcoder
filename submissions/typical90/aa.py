n=int(input())

lis=set()

for i in range(n):
  a=input()
  if a not in lis:
    print(i+1)
    lis.add(a)
