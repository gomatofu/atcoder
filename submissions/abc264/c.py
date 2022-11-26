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
 
delh = list(it.combinations(range(h1),h1-h2)) #削除する行の組み合わせ候補
delw = list(it.combinations(range(w1),w1-w2)) #削除する列の組み合わせ候補
 
flag = False

for dh in delh: #削除する行・列の組み合わせ候補を二重ループ
  for dw in delw:
    a_new = copy.deepcopy(a)
    for h_t in reversed(dh): #候補の行を削除。reversedで数が大きい行から削除
      del(a_new[h_t])
    for w_t in reversed(dw): #候補の列を削除。reversedで数が大きい列から削除
      for a_t in a_new:
        del a_t[w_t]
    if a_new == b: #行列Bと一致したら、二重ループを抜けて、出力
      flag =True
      break
    else:
      continue
if flag:
  print("Yes")
else:
  print("No")
