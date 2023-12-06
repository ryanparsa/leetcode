"""
https://leetcode.com/problems/number-of-good-pairs/
"""


def numIdenticalPairs(nums: list[int]) -> int:
    pairs = 0
    c = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            c += 1
            if nums[i] == nums[j] and i < j:
                pairs += 1
    print(c)
    return pairs


def numIdenticalPairs(nums: list[int]) -> int:
    pairs = 0
    c = 0
    p1 = 0
    p2 = 1

    while p1 < len(nums):
        c += 1
        if nums[p1] == nums[p2]:
            if p1 < p2:
                pairs += 1
        p2 += 1
        if p2 == len(nums):
            p1 += 1
            p2 = p1
    print(c)
    return pairs


def numIdenticalPairs(nums: list[int]) -> int:
    pairs = 0
    hmap = {}
    c = 0
    for n in nums:
        c += 1
        if n in hmap:
            pairs += hmap[n]
            hmap[n] += 1
        else:
            hmap[n] = 1
    print(c)
    return pairs


assert numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4
assert numIdenticalPairs(nums=[1, 1, 1, 1]) == 6
assert numIdenticalPairs(nums=[1, 2, 3]) == 0
