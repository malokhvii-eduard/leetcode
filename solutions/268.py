"""`268. Missing Number <https://leetcode.com/problems/missing-number/>`_

>>> Solution().missingNumber([3, 0, 1])
2

>>> Solution().missingNumber([0, 1])
2

>>> Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
8
"""

from itertools import zip_longest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Returns the only number in the range that is missing from the array."""
        n = len(nums)
        for actual, expected in zip_longest(sorted(nums), range(n + 1), fillvalue=-1):
            if actual != expected:
                return expected
