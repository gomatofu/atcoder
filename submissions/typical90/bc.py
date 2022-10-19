n,p,q=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
 
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      for l in range(k+1,n):
        for m in range(l+1,n):
          if a[i]%p*a[j]%p*a[k]%p*a[l]%p*a[m]%p==q:
            cnt+=1
        
print(cnt)
