from functools import lru_cache
n=int(input())
@lru_cache(maxsize=None)
def func(n):
  if n > 0:
    return func(n//2)+func(n//3)
  else:
    return 1
print(func(n))
