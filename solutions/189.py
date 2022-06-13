"""`189. Rotate Array <https://leetcode.com/problems/rotate-array/>`_

>>> nums = [1, 2, 3, 4, 5, 6, 7]
>>> Solution().rotate(nums, 3)
>>> nums
[5, 6, 7, 1, 2, 3, 4]

>>> nums = [-1, -100, 3, 99]
>>> Solution().rotate(nums, 2)
>>> nums
[3, 99, -1, -100]
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        """Rotates the array to the right by k steps."""
        k %= len(nums)

        self.reverse(nums, 0, len(nums))  # Reverse all numbers
        self.reverse(nums, 0, k)  # Reverse skipped numbers again
        self.reverse(nums, k, len(nums))  # Reverse rotated numbers again

    def reverse(self, nums: List[int], start: int, end: int):
        """Makes array reverse in-place."""
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1
