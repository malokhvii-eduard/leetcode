"""`219. Contains Duplicate II <https://leetcode.com/problems/contains-duplicate-ii/>`_

>>> Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
True

>>> Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
True

>>> Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
False

>>> Solution().containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3)
True
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Returns true if there are two distinct indices i and j in the array such
        that nums[i] == nums[j] and abs(i - j) <= k."""
        indices = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in indices:
                if i - indices[num] <= k:
                    return True
                else:
                    indices[num] = i
            else:
                indices[num] = i

        return False
