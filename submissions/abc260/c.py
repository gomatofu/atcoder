N,X,Y=map(int,input().split())
red=[0]*(N+1)
blue=[0]*(N+1)

red[N]=1

for i in range(N,1,-1):
  red[i-1]+=red[i]
  blue[i]+=red[i]*X
  red[i]=0
  
  red[i-1]+=blue[i]
  blue[i-1]+=blue[i]*Y
  blue[i]=0
  
print(blue[1])

