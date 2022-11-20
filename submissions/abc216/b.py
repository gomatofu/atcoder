N=int(input())

S_set=set()

for i in range(N):
  S=input()
  if S in S_set:
    print('Yes')
    exit()
  S_set.add(S)
print('No')
 
