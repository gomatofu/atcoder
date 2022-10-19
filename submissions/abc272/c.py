N=int(input())

A=list(map(int,input().split()))

even=[]

odd=[]

for i in range(N):

  if A[i]%2==0:

    even.append(A[i])

  else:

    odd.append(A[i])

even=sorted(even,reverse=True)

odd=sorted(odd,reverse=True)

if len(even)<2:

  even=[0,0]

if len(odd)<2:

  odd=[0,0]

p=even[0]+even[1]

q=odd[0]+odd[1]

if p>0 or q>0:

  if p>=q:

    print(p)

  else:

    print(q)

if p==q==0:

  print(-1)
