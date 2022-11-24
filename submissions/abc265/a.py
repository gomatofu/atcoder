x,y,n=map(int,input().split())

if x*3<y:
  print(x*n)
else:
  print(y*(n//3)+x*(n%3))
