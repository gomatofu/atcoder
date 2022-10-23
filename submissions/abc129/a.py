l=list(map(int,input().split()))
num=100+100
ans=100+100
for i in range(3):
  for j in range(3):
    if i!=j:
      num=l[i]+l[j]
    if ans >num:
      ans=num
print(ans)

    
