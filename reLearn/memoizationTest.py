#!/usr/bin/python3

from functools import lru_cache

@lru_cache(maxsize=256)
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(6))
print(fib(22))
print(fib(23))
print(fib(35))
print(fib(36))
