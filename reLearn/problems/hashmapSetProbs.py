#!/usr/bin/python3


def findIndexes(nums, tgt):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if tgt == nums[i] + nums[j]:
                return [i,j]

nums = [2,7,11,15]
tgt = 9
print(findIndexes(nums, tgt))
nums = [3,2,4]
tgt = 6
print(findIndexes(nums, tgt))
nums = [3,3]
tgt = 6
print(findIndexes(nums, tgt))

def dups(nums) -> bool:
    seen = dict()
    for i in nums:
        try:
            if seen[i]:
                return True
        except KeyError:
            seen[i] = True
    return False

print(dups([1,2,3,1]))
print(dups([1,2,3,4]))
print(dups([1,1,1,3,3,4,3,2,4,2]))

def single(nums) -> int:
    seen = dict()
    for i in nums:
        try:
            if seen[i] == False:
                seen[i] = True
        except KeyError:
            seen[i] = False
    for k, v in seen.items():
        if v == False:
            return k
    assert True

print(single([2,2,1]))
print(single([4,1,2,1,2]))

def kFreq(nums, k) -> list:
    count = dict()
    for i in nums:
        try:
            count[i] += 1
        except KeyError:
            count[i] = 1
    sort = sorted(count.items(), key=lambda a: a[1], reverse=True)
    r = []
    c = 0
    for i in sort:
        if c == k:
            break
        r.append(i[0])
        c += 1
    return r

nums = [1,1,1,2,2,3]
k = 2
print(kFreq(nums, k))
nums = [1]
k = 1
print(kFreq(nums, k))


