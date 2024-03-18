"""`217. Contains Duplicate <https://leetcode.com/problems/contains-duplicate/>`_

>>> Solution().containsDuplicate([1, 2, 3, 1])
True

>>> Solution().containsDuplicate([1, 2, 3, 4])
False

>>> Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
True
"""

from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return true if any value appears at least twice in the array, and return
        false if every element is distinct.
        """
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if num in counter and counter[num] > 1:
                return True

        return False
