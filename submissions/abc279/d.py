import math
A,B=map(int,input().split())
#(1)�ŏ��ɂ������֐�f���`����
def f(x):
    return B*x+(A/math.sqrt(1+x))
  
#(2)�֐�f�̍ŏ��l��T��������Ԃ̗��[��l,r�ƒu��(l<=r)
L=0
R=A//B

#(3)�덷��10^-8�������܂�while������
while R-L>2:
  
    #(4)�I�[�o�[�t���[���Ȃ��悤�Ɉȉ��̂悤�ɎO�����_��u��
    l=(L*2+R)//3
    r=(R*2+L)//3
    
    #(5)�X�V���s��
    if f(l) > f(r):
        L = l
    else:
        R = r
        
#(6)�ŏI�I�ɏo�͂���̂�l,r�̂ǂ���ł��ǂ�
ans = 2*A
for i in range(L, R+1):
    ans = min(ans, f(i))
print(f'{ans:.10f}')
