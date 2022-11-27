H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]
np_T = lambda x: [list(x) for x in zip(*x)]
S = sorted(np_T(S))
T = sorted(np_T(T))

for w in range(W):
    if S[w] != T[w]:
        print('No')
        exit()
print('Yes')
