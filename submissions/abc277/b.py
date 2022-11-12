n=int(input())
l1=['H','D','C','S']
l2=['A', '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']
l1=set(l1)
l2=set(l2)
s2=[]
ans=0
for i in range(n):
  s=input()

  s2.append(s)
  if s[0] in l1 and s[1] in l2:
    ans+=1


s2=set(s2)
if len(s2)!=n:
  print('No')
elif ans!=n:
  print('No')
else:
  print('Yes')
 
