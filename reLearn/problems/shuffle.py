#!/usr/bin/python3

def shuffle(nums: list, n: int) -> list:
    #p = int(len(nums) / n) + 1
    p = n
    new = []
    for i in range(0, p):
        new.append(nums[i])
        new.append(nums[p+i])
    return new

print(shuffle([2,5,1,3,4,7], 3))
print(shuffle([1,2,3,4,4,3,2,1], 4))
print(shuffle([1,1,2,2], 2))
