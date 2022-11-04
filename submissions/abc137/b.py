k,x=map(int,input().split())

sta=x-k+1
end=x+k-1
l=[]
for i in range(sta,end+1):
  l.append(i)
print(*l)
