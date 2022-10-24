w,h,x,y=map(int,input().split())

ans1=0
ans2=0

ans1=w*h/2

if 2*x==w and 2*y==h:
  ans2=1
  
print(ans1,ans2)

    
