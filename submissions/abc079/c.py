from itertools import product
import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
L = list(input())

for pro in product(('+', '-'), repeat=3):
    i=0
    calS=''
    for p in pro:
        calS+=L[i]+str(p)
        i+=1
    calS+=L[3]

    if eval(calS) == 7:
        print(calS + '=7')
        exit()

