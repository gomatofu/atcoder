s=input()
l=[]
for i in range(4):
  l.append(s[i])
l.sort()
if l[1] == l[2]:
  print('No')
elif l[0]==l[1] and l[2]==l[3]:
  print('Yes')
else:
  print('No')
    
    
