#!/usr/bin/python3


def repeat5(func):
    def repeater(f):
        for i in range(5):
            f()
    repeater(func)

@repeat5
def printHi():
    print('hi')

print('foo')
#p = Printer()
#p.printHi()
