s=input()
ans=0
for i in range(len(s)):
  if s[i]=="a":
    ans=i+1
    
if ans==0:
  print(-1)
else:
  print(ans)
