n=int(input())
l=list(map(int,input().split()))

ans=[]

for i in range(n):
  s=[l[i],i+1]
  ans.append(s)
  
ans.sort(key=lambda x: (x[0]))
print(ans[n-2][1])
