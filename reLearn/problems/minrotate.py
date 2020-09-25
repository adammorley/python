#!/usr/bin/python3

from typing import Iterable

def findMin(nums: Iterable[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    mid = int(len(nums) / 2)
    if len(nums) < mid and nums[mid+1]  < nums[mid]:
        return nums[mid+1]
    left = findMin(nums[0:mid])
    right = findMin(nums[mid:])
    if left < right:
        return left
    elif right < left:
        return right


nums = [3,4,5,7,8,9,1,2]
print(findMin(nums))
