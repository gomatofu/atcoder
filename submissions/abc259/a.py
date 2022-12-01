N,M,X,T,D=map(int,input().split())

if X<M:
  print(T)
elif X>=M:
  tall=T-((X-M)*D)
  print(tall)
