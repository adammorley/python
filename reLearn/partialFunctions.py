#!/usr/bin/python3

from functools import partial

def mult(a, b):
    return a*b

dbl = partial(mult,2)
print(dbl(4))
