S=input()
T=input()
s=[]
scnt=1
# S�̃J�E���g
for i in range(1,len(S)):
  if S[i-1]==S[i]:
    scnt+=1
  else:
    s.append([S[i-1],scnt])
    scnt=1
s.append([S[i],scnt])
         
t=[]
tcnt=1
# T�̃J�E���g
for i in range(1,len(T)):
  if T[i-1]==T[i]:
    tcnt+=1
  else:
    t.append([T[i-1],tcnt])
    tcnt=1
t.append([T[i],tcnt])

# ���������Ⴄ�ꍇ
if len(s)!=len(t):
  print('No')
  exit()
  
for i in range(len(s)):
  smoji=s[i][0]
  tmoji=t[i][0]
  snum=s[i][1]
  tnum=t[i][1]
  
  if smoji!=tmoji:
    print('No')
    exit()
  elif tnum>1 and snum==1:
    print('No')
    exit()
  elif snum>tnum:
    print('No')
    exit()
print('Yes')
