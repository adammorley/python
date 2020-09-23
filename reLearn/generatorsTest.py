#!/usr/bin/python3

def genMath(num):
    for i in range(0, num):
        yield i * num

for n in genMath(5):
    print(n)
