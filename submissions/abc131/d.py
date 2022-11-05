n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]

st.sort(key=lambda x: x[1])

su = 0
last_time = 0
for s,t in st:
  su += s
  if t < su:
    print("No")
    exit()
print("Yes")
