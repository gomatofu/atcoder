def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def SS(): return input()
def LS(): return list(input())

N=II()




def rotate(matrix):
    return list(zip(*matrix[::-1]))

def check_match(matrix_a, matrix_b):
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            if matrix_a[i][j] == 1 and matrix_b[i][j] != 1:
                return False
    return True

def can_rotate(matrix_a, matrix_b):
    for _ in range(4):
        if check_match(matrix_a, matrix_b):
            return True
        matrix_a = rotate(matrix_a)
    return False

# —á:
A = [LI() for _ in range(N)]
B = [LI() for _ in range(N)]
if can_rotate(A, B):
    print('Yes')
else:
    print('No')
