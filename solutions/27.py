"""`27. Remove Element <https://leetcode.com/problems/remove-element/>`_

>>> Solution().removeElement([], 1)
0

>>> Solution().removeElement([3, 2, 2, 3], 3)
2

>>> Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
5

>>> Solution().removeElement([0, 1, 2, 2, 2, 2, 2, 0, 4], 2)
4
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Removes all occurrences of val in nums in-place."""
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue

            nums[count] = nums[i]
            count += 1

        return count
