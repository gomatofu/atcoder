import itertools as it
import copy
h1,w1 = map(int,input().split())
a = []
for _ in range(h1):
  a.append(list(map(int,input().split())))
  
h2,w2 = map(int,input().split())
b = []
for _ in range(h2):
  b.append(list(map(int,input().split())))
 
delh = list(it.combinations(range(h1),h1-h2)) #�폜����s�̑g�ݍ��킹���
delw = list(it.combinations(range(w1),w1-w2)) #�폜�����̑g�ݍ��킹���
 
flag = False

for dh in delh: #�폜����s�E��̑g�ݍ��킹�����d���[�v
  for dw in delw:
    a_new = copy.deepcopy(a)
    for h_t in reversed(dh): #���̍s���폜�Breversed�Ő����傫���s����폜
      del(a_new[h_t])
    for w_t in reversed(dw): #���̗���폜�Breversed�Ő����傫���񂩂�폜
      for a_t in a_new:
        del a_t[w_t]
    if a_new == b: #�s��B�ƈ�v������A��d���[�v�𔲂��āA�o��
      flag =True
      break
    else:
      continue
if flag:
  print("Yes")
else:
  print("No")
