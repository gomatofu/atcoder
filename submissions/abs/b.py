n=int(input())
l=list(map(int,input().split()))
flg=False
cnt=0

while 1:
  for i in range(n):
    if l[i]%2==1:
      flg=True
  if flg==True:
    break
  for i in range(n):
    l[i]/=2
  cnt+=1
  
print(cnt)
