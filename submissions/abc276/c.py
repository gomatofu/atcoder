n=int(input())
p=list(map(int,input().split()))

sorted_suffix=[p.pop()]

while p[-1]<sorted_suffix[-1]:
  sorted_suffix.append(p.pop())
  
sorted_suffix.sort()

i = len(sorted_suffix) - 1

while sorted_suffix[i] > p[-1]:
    i -= 1
p[-1],sorted_suffix[i]=sorted_suffix[i],p[-1]
sorted_suffix.sort(reverse=True)
print(*(p+sorted_suffix))
