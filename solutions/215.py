"""`215. Kth Largest Element in an Array <https://leetcode.com/problems/kth-largest-element-in-an-array/>`_

>>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
5

>>> Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
4
"""


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the Kth largest element in the array."""
        k = len(nums) - k

        def quickSelect(left, right):
            """Find the Kth largest element in the array via Quickselect algorithm."""
            pivot, pointer = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1

            nums[pointer], nums[right] = nums[right], nums[pointer]

            if pointer > k:
                return quickSelect(left, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, right)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)
