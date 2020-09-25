#!/usr/bin/python3

import heapq

nums = [2,1,9,4,3,5,10]
print(nums)
heapq.heapify(nums)
print(nums)
heapq.heappush(nums, 44)
print(nums)

nums = [3,2,1,5,6,4]
s = sorted(nums)
print(nums[len(nums)-3])
heapq.heapify(nums)
print(nums)
print(nums[-3])

def MergeSort(toSort: list):
    if len(toSort) == 1 or len(toSort) == 0:
        return toSort
    mid = int(len(toSort) / 2)
    toSort0 = toSort[:mid]
    toSort1 = toSort[mid:]
    return merge(MergeSort(toSort0), MergeSort(toSort1))

def merge(toSort0, toSort1):
    new = []
    ts0 = 0
    ts1 = 0
    while ts0 < len(toSort0) or ts1 < len(toSort1):
        if ts1 == len(toSort1):
            new.append(toSort0[ts0])
            ts0 += 1
        elif ts0 == len(toSort0):
            new.append(toSort1[ts1])
            ts1 += 1
        elif toSort0[ts0] <= toSort1[ts1]:
            new.append(toSort0[ts0])
            ts0 += 1
        elif toSort0[ts0] >= toSort1[ts1]:
            new.append(toSort1[ts1])
            ts1 += 1
    return new

nums = [3,2,1,5,6,4]
new = MergeSort(nums)
print('next')
print(new)
print(new[-2])
