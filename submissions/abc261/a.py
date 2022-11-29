L1,R1,L2,R2=map(int,input().split())

a=[]
b=[]
for i  in range(L1,R1+1):
  a.append(i)

for i  in range(L2,R2+1):
   b.append(i)
    
ans=sorted(list(set(a) & set(b)))

if len(ans)==0:
  print(0)
else:
  print(ans[-1]-ans[0])
