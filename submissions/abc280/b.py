N=int(input())
A=list(map(int,input().split()))
an=[]
ans=A[0]
s=A[0]
an.append(ans)
for i in range(1,len(A)):
  ans=A[i]-s
  an.append(ans)
  s+=ans
  
print(*an)
