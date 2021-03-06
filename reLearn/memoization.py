#!/usr/bin/python3

from functools import lru_cache

@lru_cache(maxsize=256)
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fib(num-1) + fib(num-2)

print(fib(3))
print(fib(5))
print(fib(25))
print(fib(42))
