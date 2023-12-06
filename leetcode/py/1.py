"""
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        time: O(n)
        space: O(n)
        """
        data: dict = dict()

        for i in range(len(nums)):
            r = target - nums[i]
            if r in data:
                return [i, data[r]]
            else:
                data[nums[i]] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        time: O(n^2)
        space: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Ensure j is after i
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Return an empty list if no solution is found


s = Solution()

print(s.twoSum(nums=[2, 7, 11, 15], target=9))
