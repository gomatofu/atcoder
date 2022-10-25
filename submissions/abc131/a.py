s=[int(i) for i in list(input())]
cnt=0
for i in range(1,len(s)):
  if s[i]==s[i-1]:
    cnt+=1
    
if cnt>0:
  print('Bad')
else:
  print('Good')
