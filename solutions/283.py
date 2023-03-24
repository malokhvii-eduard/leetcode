"""`283. Move Zeroes <https://leetcode.com/problems/move-zeroes/>`_

>>> nums = [0, 1, 0, 3, 12]
>>> Solution().moveZeroes(nums)
>>> nums
[1, 3, 12, 0, 0]

>>> nums = [0]
>>> Solution().moveZeroes(nums)
>>> nums
[0]
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Move all 0's to the end."""
        if len(nums) < 1:
            return

        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0
