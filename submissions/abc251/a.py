S=input()
 
ans=[]
for i in range(6):
  ans.append(S[i%len(S)])
  
print(*ans,sep='')
