#!/usr/bin/python3

def fib():
    fibMap = {0: 0, 1: 1}
    highest = 1
    def calc(num):
        nonlocal fibMap
        nonlocal highest
        if num <= highest:
            return fibMap[num]
        for i in range(highest+1, num+1):
            highest = i
            fibMap[highest] = fibMap[highest-1] + fibMap[highest-2]
        return fibMap[num]
    return calc

fibCalc = fib()
print(fibCalc(3))
print(fibCalc(5))
print(fibCalc(25))
print(fibCalc(42))
