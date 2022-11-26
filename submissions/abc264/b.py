R, C = map(int, input().split())
ans = max(abs(R-8),abs(C-8))

if ans%2==0:
  print('white')
else:
  print('black')
