"""`26. Remove Duplicates from Sorted Array <https://leetcode.com/problems/remove-duplicates-from-sorted-array/>`_

>>> Solution().removeDuplicates([1])
1

>>> Solution().removeDuplicates([1, 1, 2])
2

>>> Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
5
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Remove the duplicates in-place."""
        if len(nums) < 2:
            return len(nums)

        previous = 0
        for current in range(1, len(nums)):
            if nums[current] != nums[previous]:
                previous += 1
                nums[previous] = nums[current]

        return previous + 1
