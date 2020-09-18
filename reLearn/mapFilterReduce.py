#!/usr/bin/python3

from functools import reduce

pets = ['alfred', 'tabitha', 'william']
upets = []

for pet in pets:
    upets.append(pet.upper())

print(upets)

people = ['sally', 'sue', 'joe']
upeople = list(map(str.upper, people))
print(upeople)

nums = [12, 35, 64, 22]
def filterLow(num):
    return num > 20

highNums = list(filter(filterLow, nums))
print(highNums)

def upscale(num1, num2):
    return (num1+num2)*2

total = reduce(upscale, highNums)

print(total)
