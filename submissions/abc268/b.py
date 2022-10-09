s=input()
t=input()
num=0

if len(s)<=len(t):
  for i in range(len(s)):
    if s[i]==t[i]:
      num+=1
  if num==len(s):
    print('Yes')
  else:
    print('No')
else:
  print('No')

    
