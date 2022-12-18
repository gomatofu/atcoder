n, w = map(int, input().split())
a = list(map(int, input().split()))
x = []

for i in range(n):
  if a[i]<=w:
    x.append(a[i])

for i in range(n-1):
  for j in range(i+1, n):
    if a[i]+a[j]<=w:
      x.append(a[i]+a[j])

for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      if a[i]+a[j]+a[k]<=w:
        x.append(a[i]+a[j]+a[k])

print(len(set(x)))
