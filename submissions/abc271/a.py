N=int(input())
ans = hex(N)[2:]

if len(ans)==1:
  ans='0'+ans
  
print(ans.swapcase())
