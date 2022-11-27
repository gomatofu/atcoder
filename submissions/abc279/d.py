import math
A,B=map(int,input().split())
#(1)最小にしたい関数fを定義する
def f(x):
    return B*x+(A/math.sqrt(1+x))
  
#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
L=0
R=A//B

#(3)誤差が10^-8を下回るまでwhile文を回す
while R-L>2:
  
    #(4)オーバーフローしないように以下のように三等分点を置く
    l=(L*2+R)//3
    r=(R*2+L)//3
    
    #(5)更新を行う
    if f(l) > f(r):
        L = l
    else:
        R = r
        
#(6)最終的に出力するのはl,rのどちらでも良い
ans = 2*A
for i in range(L, R+1):
    ans = min(ans, f(i))
print(f'{ans:.10f}')
