#!/usr/bin/python3

nums = [1,2,3,4]
new = []
for i in range(0, len(nums)):
    p = 1
    for j in range(0, len(nums)):
        if j == i:
            continue
        p = p * nums[j]
    new.append(p)

print(new)
