#!/usr/bin/python3

def findMax(nums: list) -> int:
    assert len(nums) > 1, 'must have more than one element'
    maxi = None
    for i in range(0, len(nums)-1):
        if maxi is None:
            maxi = nums[i] * nums[i+1]
        else:
            v = nums[i] * nums[i+1]
            if v > maxi:
                maxi = v
    return maxi

one = [2,3,-2,4]
two = [-2,0,-1]
print(findMax(one))
print(findMax(two))
