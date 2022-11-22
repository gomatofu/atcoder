ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
dx,dy = map(int,input().split())
 
def S(x0,y0,x1,y1,x2,y2):
    return x0*y1+x1*y2+x2*y0-y0*x1-y1*x2-y2*x0
 
p1 = S(ax,ay,bx,by,cx,cy)
p2 = S(bx,by,cx,cy,dx,dy)
p3 = S(cx,cy,dx,dy,ax,ay)
p4 = S(dx,dy,ax,ay,bx,by)
if p1 > 0 and p2 > 0 and p3 > 0 and p4 > 0:
    print("Yes")
else:
    print("No")
