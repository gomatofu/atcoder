N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))

def is_ok(mid):
    tmp_val = 0 
    cut_cnt = 0 
    for i in range(N):
        if A[i] - tmp_val >= mid and L - A[i] >= mid:
            cut_cnt += 1
            tmp_val = A[i]
    if cut_cnt >= K:
        return True
    else:
        False
 
def binary_search(left, right):
     while right - left > 1:
         mid = (left + right) // 2
         if is_ok(mid):
             left = mid
         else:
             right = mid
     return left , right
 
left,right = binary_search(-1,L+1)
print(left)
