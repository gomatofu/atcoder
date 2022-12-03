S=list(input())
T=list(input())

S.append('A')
for i in range(len(S)):
  if S[i]!=T[i]:
    print(i+1)
    exit()
