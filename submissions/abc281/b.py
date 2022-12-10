import re
S=input()
if len(S)<8:
  print('No')
  exit()
  
alresult=re.findall('[A-Z]+', S)
numresult = re.findall(r"\d+", S)
flg=500
for i in range(len(numresult)):
  if len(numresult[i])==6:
    flg=i

if flg==500:
  print('No')
  exit()
  
if int(numresult[flg])<100000:
  print('No')
  exit()

if int(numresult[flg])>999999:
  print('No')
  exit()
  
for i in range(len(alresult)):
  if len(alresult[i])>1:
    print('No')
    exit()

print('Yes')

  
  
