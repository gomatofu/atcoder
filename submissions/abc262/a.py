Y = int(input())

ans = Y % 4

if ans == 2:
  print(Y)
elif ans == 3:
  print(Y + 3)
elif ans == 1:
  print(Y + 1)
else:
  print(Y + 2)
