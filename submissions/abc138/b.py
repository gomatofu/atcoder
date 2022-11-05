n=int(input())
l=list(map(int,input().split()))

s=0

for i in range(n):
  s+=1/l[i]

ans=1/s
print(ans)

