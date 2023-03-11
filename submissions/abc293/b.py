def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()
A=LI()
B=[]
s=set()

for i in range(N):
    B.append(i+1)
    if i+1 not in s:
        s.add(A[i])

diff_list = set(B) ^ set(s)

diff=list(diff_list)
diff.sort()
print(len(diff))
print(*diff)
