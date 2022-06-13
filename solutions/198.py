"""`198. House Robber <https://leetcode.com/problems/house-robber/>`_

>>> Solution().rob([1, 2, 3, 1])
4

>>> Solution().rob([2, 7, 9, 3, 1])
12

>>> Solution().rob([1, 2])
2
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        before_before_profit = nums[0]
        before_profit = max(nums[0], nums[1])
        current_profit = 0

        for i in range(2, len(nums)):
            current_profit = max((nums[i] + before_before_profit), before_profit)
            before_before_profit = before_profit
            before_profit = current_profit

        return current_profit
