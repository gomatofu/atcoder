S=input()
ans=[0]*len(S)
cnt=0
for i,s in enumerate(S):
  if s=="R":
    cnt+=1
  else:
    ans[i] += cnt // 2
    ans[i - 1] += (cnt + 1) // 2
    cnt = 0
    
cnt=0
ans=ans[::-1]

for i,s in enumerate(S[::-1]):
  if s=="L":
    cnt+=1
  else:
    ans[i] += cnt // 2
    ans[i - 1] += (cnt + 1) // 2
    cnt = 0

print(*ans[::-1], sep=' ')
