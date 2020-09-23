#!/usr/bin/python3 

from functools import lru_cache

@lru_cache(maxsize=256)
def factorial(n):
    assert n > 0, 'positive ints only for now'
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(3))
print(factorial(5))
print(factorial(67))
