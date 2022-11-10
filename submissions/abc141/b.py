s=input()
cnt=0
for i in range(len(s)):
  num=i+1
  if num%2==0 :
    if (s[i]=='L' or s[i]=='U' or s[i]=='D'):
      cnt+=1
  else:
    if (s[i]=='R' or s[i]=='U' or s[i]=='D'):
      cnt+=1
if cnt==len(s):
  print('Yes')
else:
  print('No')

