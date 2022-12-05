K=int(input())

if K<60:
  K = format(K, '02')  
  print('21:'+str(K))
else:
  K-=60
  K = format(K, '02')  
  print('22:'+str(K))
