# Nを入力として受け取る
N = int(input())

# 人の情報をリストに格納する
people = []
for i in range(N):
    S, A = input().split()
    A = int(A)
    people.append((S, A))

# 年齢が最も小さい人を起点として、時計回りの順番で名前を出力する
min_age = min(people, key=lambda x: x[1])
start_index = people.index((min_age))

for i in range(N):
    index = (start_index + i) % N
    print(people[index][0])
