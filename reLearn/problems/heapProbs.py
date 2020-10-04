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

def maxNum(nums, n):
    maxes = []
    for i in nums:
        if i not in maxes and len(maxes) < n:
            maxes.append(i)
        else:
            for j in range(0, len(maxes)):
                if i > maxes[j]:
                    maxes[j] = i
    m = sorted(maxes)
    print(m)
    return m[-n]

n = 3
nums = [3,2,1]
print(maxNum(nums, n))
n = 2
nums = [1,2]
print(maxNum(nums, n))
n = 3
nums = [2,2,3,1]
print(maxNum(nums, n))

# without using append or pop
class Stack:
    container: list
    def __init__(self):
        self.container = []
    def push(self, obj):
        last = len(self.container)
        self.container.append(None) # can't figure out how to not use this
        self.container[last] = obj
    def pop(self):
        last = len(self.container)
        t = self.container[last-1]
        del self.container[last-1]
        return t
    def top(self):
        last = len(self.container)
        t = self.container[last-1]
        return t
    def min(self):
        if len(self.container) == 1:
            return self.container[0]
        min = self.container[0]
        for i in range(0, len(self.container)):
            if self.container[i] < min:
                min = self.container[i]
        return min


# need a test
