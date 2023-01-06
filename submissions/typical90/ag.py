import math
h,w=map(int,input().split())
if h==1 or w==1:
  print(h*w)
else:
  h=math.ceil(h/2)
  w=math.ceil(w/2)
  print(w*h)
