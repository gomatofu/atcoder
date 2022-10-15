n = int(input())
a = list(map(int, input().split()))
 
a.sort(reverse = True)
b = set(a)
dic = {}
 
for i in range(n):
  if a[i] not in dic.keys():
    dic[a[i]] = 1
  else:
    dic[a[i]] += 1


for x in dic.values():
  print(x)
  
for i in range(n - len(dic)):
  print(0)
