l= [int(i) for i in list(input())]
num=0
for i in range(len(l)):
  if l[i]==1:
    num+=1

print(num)
