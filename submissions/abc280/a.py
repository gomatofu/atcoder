H,W=map(int,input().split())
cnt=0

for i in range(H):
  s=input()
  cnt+=s.count('#')
  
print(cnt)
