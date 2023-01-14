import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = II()
A = LI()
Q = II()
A.sort()

def is_ok(mid,B):
     if A[mid] <= B:
         return True
     else:
         return False
 
def binary_search(left, right,B): 
     while right - left > 1:
         mid = (left + right) // 2
         if is_ok(mid,B):
             left = mid
         else:
             right = mid
     return left , right
 
for i in range(Q):
    B = int(input())
    left,right = binary_search(0,N,B)
    if left < 0:
        left = 0

    if right >= N:
        right = N-1
    ans = min(abs(A[left]-B),abs(A[right]-B))
    print(ans)
