#!/usr/bin/python3

import random

def lottery():
    for i in range(6):
        yield random.randint(1,40)
    
    yield random.randint(1,15)

for r_num in lottery():
    print('next number is {}'.format(r_num))

def fibonacci():
    a, b = 1, 1
    while True:
        yield a+b
        a, b = b, b+a

print(type(fibonacci()))
for i in fibonacci():
    print(i)
    if i > 20:
        print('last')
        break
