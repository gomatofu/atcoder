X, K, D = map(int, input().split())

new_X = abs(X) % D
new_K = K - abs(X) // D

if new_K <= 0:
    answer = abs(X) - K*D
else:
    if new_K % 2 == 0:
        answer = new_X
    else:
        answer = abs(new_X - D)

print(answer)
