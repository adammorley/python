#!/usr/bin/python3

nums = [3,4,2,7,12]
for n in map(lambda a: a**2, nums):
    print(n)

a = list(map(lambda a: a*2, nums))
print(a)

b = filter(lambda a: a < 10, nums)
c = list(b)
print(c)

from functools import reduce
d = reduce(lambda a, b: a+b, c)
print(d)
