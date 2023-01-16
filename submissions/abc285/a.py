import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B=map(int,sys.stdin.readline().rstrip().split())

if (A==1 and B==2) or (A==1 and B==3):
    print('Yes') 
elif (A==2 and B==4) or (A==2 and B==5):
    print('Yes') 
elif (A==3 and B==6) or (A==3 and B==7):
    print('Yes')
elif (A==4 and B==8) or (A==4 and B==9):
    print('Yes')
elif (A==5 and B==10) or (A==5 and B==11):
    print('Yes')
elif (A==6 and B==12) or (A==6 and B==13):
    print('Yes')
elif (A==7 and B==14) or (A==7 and B==15):
    print('Yes')
else:
    print('No')
