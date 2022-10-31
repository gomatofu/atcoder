n=int(input())
l=list(map(int,input().split()))
l.sort()
sta=l[n//2-1]
end=l[n//2]
ans=end-sta
  
print(ans)
