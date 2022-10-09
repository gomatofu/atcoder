x,y,z=map(int,input().split())
if x>0:
  if (y>0 and y<x and z>y):
    print(-1)
  elif (y>0 and y<x and z<0) :
    print(x+(-1*z*2))
  else:
    print(x)
elif x<0:
  if (y<0 and y>x and z<y):
    print(-1)
  elif (y<0 and y>x and z>0) :
    print((-1*x)+(z*2))
  else:
    print((-1*x))
 
    
    

