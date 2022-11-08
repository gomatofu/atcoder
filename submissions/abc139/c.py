n=int(input())
h=list(map(int,input().split()))
l=[]
cnt=0
for i in range(1,n):
  if h[i-1]>=h[i]:
    cnt+=1
  else:
    l.append(cnt)
    cnt=0
  
l.append(cnt)   
print(max(l))

