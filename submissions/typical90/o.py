n, k = map(int, input().split())

def ten_to_nine(n):
    base_9 = ""
    while n!=0:
        base_9 += str(n%9)
        n = n//9
    return int(base_9[::-1])

def eight_to_five(x):
    x = str(x)
    s = x.replace('8', '5')
    return int(s)

if n == 0:
    print(n)
    exit()

for _ in range(k):
    n = int(str(n),8)
    n = ten_to_nine(n)
    n = eight_to_five(n)

print(n)
