S=list(input())
AT='atcoder'

cnt=0
for i in range(len(AT)):
  index=S.index(AT[i])
  cnt+=abs((i+1)-(index+1))
  S.pop(index)
  S.insert(i, AT[i])
print(cnt)
