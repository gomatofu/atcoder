s,t=map(int,input().split())
cnt=0

for i in range(101):
  a=i
  for j in range(101):
    b=j
    for k in range(101):
      c=k
      if a+b+c<=s and a*b*c<=t:
        cnt+=1
      
print(cnt)
