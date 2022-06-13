"""`1. Two Sum <https://leetcode.com/problems/two-sum/>`_

>>> Solution().twoSum([2, 7, 11, 15], 9)
[0, 1]

>>> Solution().twoSum([3, 2, 4], 6)
[1, 2]

>>> Solution().twoSum([3, 3], 6)
[0, 1]
"""

from itertools import combinations
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Returns indices of the two numbers such that they add up to target."""
        for i, j in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]
