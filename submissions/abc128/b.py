n = int(input())
r = []
for i in range(n):
    l = list(input().split())
    l.append(i+1)
    r.append(l)
r.sort(key=lambda x: (x[0],-int(x[1])))
for a in r:
  print(a[2])
