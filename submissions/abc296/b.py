def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

h=['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
w=['8','7', '6', '5', '4', '3', '2', '1']

T = [list(input()) for _ in range(8)]
for i in range(8):
    for j in range(8):
        if T[i][j]=='*':
            print(h[j]+w[i])
