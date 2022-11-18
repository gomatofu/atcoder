from itertools import permutations
S,K=input().split()
K=int(K)
S=list(S)
S.sort()
S_set=set()
cnt=0
for seq in permutations(S,len(S)):
  if seq not in S_set:
    cnt+=1
    S_set.add(seq)
    if K==cnt:
      print(*seq,sep='')
      exit()
  

 
