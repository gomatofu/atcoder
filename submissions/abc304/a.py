# N����͂Ƃ��Ď󂯎��
N = int(input())

# �l�̏������X�g�Ɋi�[����
people = []
for i in range(N):
    S, A = input().split()
    A = int(A)
    people.append((S, A))

# �N��ł��������l���N�_�Ƃ��āA���v���̏��ԂŖ��O���o�͂���
min_age = min(people, key=lambda x: x[1])
start_index = people.index((min_age))

for i in range(N):
    index = (start_index + i) % N
    print(people[index][0])
