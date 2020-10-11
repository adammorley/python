#!/usr/bin/python3

'''
returns a tuple (for lookup) of low, high
'''
def mset(a: int, b: int) -> (int, int):
    if (not a) or (not b):
        raise RuntimeError('forgot a or b!')
    if a <= b:
        return (a, b)
    return (b, a)
'''
Given an integer array and a positive integer k, count all distinct pairs with difference equal to k.

have to know you've tracked 6 and 1 twice if its repeated; could removes duplicates from list or could track as "seen" in a map
removal is going to go through array many times, so let's use dict (map in golang, whoops)
'''

def find_distinct_pairs(nums: list, k: int) -> int:
    #assert k > 0, 'k must be positive'
    if k < 1:
        raise RuntimeError('k must be positive')
    elif len(nums) < 2:
        return 0
    m = dict()
    n = 0
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            a, b = nums[i], nums[j]
            s = mset(a, b)
            try:
                m[s]
            except KeyError:
                if (a - b == k) or (b - a == k):
                    m[s] = True
                    n += 1
    return n

nums = [6,1,4,7,2,6,1,2,9,4]
k = 2
print(find_distinct_pairs(nums, k))

