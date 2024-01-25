from functools import lru_cache


@lru_cache(maxsize=1000)
def fubonacii(n):
    if n == 1:
        return n
    elif n == 2:
        return 2
    else:
        return fubonacii(n - 1) + fubonacii(n - 2)


for num in range(1, 101):
    print(num, ':', fubonacii(num))
